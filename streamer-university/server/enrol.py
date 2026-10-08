#!/usr/bin/env python3
"""Enrolment endpoint for lrtvs.gy/university/enrol/submit. Stdlib only.
Listens on 127.0.0.1:8160. nginx proxies POST /university/enrol/submit to it (see nginx-university.conf).
Writes one CSV row per enrolment to /opt/streameru/enrol.csv (mode 600) and returns {"number": n}.
The CSV is the only copy. It is never committed, never emailed, never pasted into chat."""
import csv, json, os, pathlib, time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

CSV = pathlib.Path(os.environ.get("ENROL_CSV", "/opt/streameru/enrol.csv"))
FIELDS = ["number", "received", "name", "handle", "age", "guardian", "town", "track", "gear", "contact", "why", "ip"]
MAX = 4000

class H(BaseHTTPRequestHandler):
    def _send(self, code, obj):
        b = json.dumps(obj).encode(); self.send_response(code)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.rstrip("/").endswith("/health"): return self._send(200, {"ok": True, "count": count()})
        self._send(404, {"error": "not found"})
    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0 or n > MAX: return self._send(413, {"error": "bad length"})
        try: o = json.loads(self.rfile.read(n))
        except Exception: return self._send(400, {"error": "bad json"})
        if not isinstance(o, dict) or not str(o.get("name", "")).strip() or not str(o.get("contact", "")).strip():
            return self._send(400, {"error": "name and contact needed"})
        row = {k: str(o.get(k, ""))[:600].replace("\n", " ").strip() for k in FIELDS if k not in ("number", "received", "ip")}
        row["received"] = time.strftime("%Y-%m-%d %H:%M:%S"); row["ip"] = self.headers.get("X-Real-IP", self.client_address[0])
        row["number"] = count() + 1
        CSV.parent.mkdir(parents=True, exist_ok=True); new = not CSV.exists()
        with open(CSV, "a", newline="") as f:
            w = csv.DictWriter(f, FIELDS)
            if new: w.writeheader()
            w.writerow(row)
        os.chmod(CSV, 0o600); self._send(200, {"number": row["number"]})
    def log_message(self, *a): pass

def count():
    if not CSV.exists(): return 0
    with open(CSV, newline="") as f: return max(0, sum(1 for _ in f) - 1)

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", int(os.environ.get("PORT", 8160))), H).serve_forever()
