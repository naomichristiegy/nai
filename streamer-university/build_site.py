#!/usr/bin/env python3
"""Rockland Streamer University: builds the static site into site/ and a phone preview into preview/.
python3 build_site.py        (stdlib only)
Deploy: scp -r site/* root@67.205.145.217:/var/www/lrtvs-home/university/   (from the Mac, see DEPLOY.md)
"""
import json, html, pathlib, shutil

ROOT = pathlib.Path(__file__).parent
SITE = ROOT / "site"
PREVIEW = ROOT / "preview"
LESSONS = json.loads((ROOT / "content/lessons.json").read_text())
GRADS = json.loads((ROOT / "content/graduates.json").read_text())
FONT = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;600;800&display=swap">'

CSS = """
/* Layout: one column, 44rem wide, left-aligned. Storm: navy cloud banks, light-blue lightning, a sky-blue hairline. */
:root{
  --ink:#0B1A33; --paper:#F3F7FC; --bolt:#1F6EBE; --bolt-ink:#16528F; --cloud:#D6EBFF; --mute:#5B6B84; --line:#C9DBF0; --card:#FFFFFF;
  --display:"Figtree",Avenir Next,Avenir,Segoe UI,system-ui,sans-serif; --body:"Figtree",Avenir Next,Avenir,Segoe UI,system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){ --ink:#ECF4FF; --paper:#071024; --bolt:#3FA9F5; --bolt-ink:#7DD4FF; --cloud:#11284A; --mute:#9FB3D1; --line:#1E3558; --card:#0E1B36; color-scheme:dark } }
:root[data-theme="dark"]{ --ink:#ECF4FF; --paper:#071024; --bolt:#3FA9F5; --bolt-ink:#7DD4FF; --cloud:#11284A; --mute:#9FB3D1; --line:#1E3558; --card:#0E1B36; color-scheme:dark }
*{box-sizing:border-box}
[hidden]{display:none!important}
body{margin:0;background:var(--paper);color:var(--ink);font:400 1.0625rem/1.55 var(--body);-webkit-text-size-adjust:100%}
.wrap{max-width:44rem;margin:0 auto;padding-inline:1rem;padding-block:0 4rem}
.rainbow{height:4px;background:linear-gradient(90deg,#7DD4FF,#3FA9F5,#1F3B68)}
header.top{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding-block:1rem;border-bottom:1px solid var(--line)}
header.top a{color:var(--ink);text-decoration:none;font-weight:800;letter-spacing:.01em}
header.top nav{display:flex;gap:1rem;font-weight:600;font-size:.95rem}
header.top nav a{color:var(--bolt-ink)}
h1,h2,h3{font-family:var(--display);text-wrap:balance;line-height:1.1;margin:0}
h1{font-size:clamp(2.2rem,8vw,3.6rem);font-weight:800;letter-spacing:-.02em}
h2{font-size:1.5rem;font-weight:800;margin-top:3rem;margin-bottom:1rem}
h3{font-size:1.1rem;font-weight:800}
p{margin:0 0 1rem}
.eyebrow{font-size:.8rem;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--bolt-ink)}
.hero{padding-block:2.5rem 2rem;position:relative}
.hero .splat{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden;
  background:radial-gradient(ellipse 14rem 6rem at 95% 8%,var(--cloud) 0 55%,transparent 72%),radial-gradient(ellipse 10rem 5rem at 70% 0%,var(--cloud) 0 50%,transparent 72%),radial-gradient(ellipse 9rem 4rem at 100% 40%,var(--cloud) 0 50%,transparent 72%)}
.hero .bolt{position:absolute;right:4%;top:0;height:62%;width:auto;z-index:-1;pointer-events:none;opacity:.55;filter:drop-shadow(0 0 6px var(--bolt))}
@media (max-width:520px){.hero .bolt{right:1%;height:48%;opacity:.35}}
.hero p.lead{font-size:1.25rem;max-width:34rem;margin-top:1rem}
.cta{display:flex;flex-wrap:wrap;gap:.75rem;margin-top:1.5rem}
.btn{display:inline-block;padding:.8rem 1.25rem;border-radius:999px;font-weight:800;text-decoration:none;border:2px solid var(--bolt)}
.btn.primary{background:var(--bolt);color:#fff}
.btn.ghost{color:var(--bolt-ink)}
.btn:focus-visible,a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid var(--bolt);outline-offset:2px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(10rem,1fr));gap:.75rem 1.5rem;margin-top:2rem;padding:1rem 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.facts div{min-width:0}
.facts b{display:block;font-family:var(--display);font-weight:800;font-size:1.15rem;font-variant-numeric:tabular-nums}
.facts span{color:var(--mute);font-size:.9rem}
ul.plain{list-style:none;padding:0;margin:0;display:grid;gap:.6rem}
ul.plain li{padding-left:1.4rem;position:relative;min-width:0}
ul.plain li::before{content:"";position:absolute;left:0;top:.55em;width:.7rem;height:.7rem;border-radius:50%;background:var(--bolt)}
.tracks{display:grid;gap:.75rem}
.track{display:grid;grid-template-columns:7.5rem 1fr;gap:.25rem 1rem;padding:.75rem 0;border-bottom:1px solid var(--line);min-width:0}
.track b{font-family:var(--display);font-weight:800}
.track span{color:var(--mute);font-size:.95rem}
@media (max-width:420px){.track{grid-template-columns:1fr}}
ol.lessons{list-style:none;padding:0;margin:0;counter-reset:l}
ol.lessons li{display:grid;grid-template-columns:3rem 1fr;gap:0 .75rem;padding:.75rem 0;border-bottom:1px solid var(--line);min-width:0}
ol.lessons li .n{font-family:var(--display);font-weight:800;color:var(--bolt-ink);font-variant-numeric:tabular-nums;font-size:1.3rem}
ol.lessons li a{color:var(--ink);text-decoration:none;font-weight:600}
ol.lessons li a:hover{color:var(--bolt-ink)}
ol.lessons li .k{display:block;color:var(--mute);font-size:.85rem}
table{border-collapse:collapse;width:100%;font-size:.95rem}
.tablewrap{overflow-x:auto}
th,td{text-align:left;padding:.5rem .6rem .5rem 0;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);font-weight:600}
td b{font-variant-numeric:tabular-nums}
.box{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--bolt);padding:1rem 1.1rem;border-radius:.5rem;margin:1.5rem 0}
.box h3{margin-bottom:.4rem}
.note{color:var(--mute);font-size:.9rem}
footer{margin-top:4rem;padding-top:1.5rem;border-top:1px solid var(--line);color:var(--mute);font-size:.9rem}
footer a{color:var(--bolt-ink)}
/* lesson page */
.lesson-head{padding-block:2rem 1rem}
.lesson-head h1{font-size:clamp(1.9rem,7vw,2.8rem)}
ol.steps{padding-left:1.4rem;margin:0;display:grid;gap:.5rem}
ol.steps li{min-width:0}
.check{list-style:none;padding:0;margin:0;display:grid;gap:.5rem}
.check label{display:flex;gap:.6rem;align-items:flex-start;padding:.6rem .75rem;background:var(--card);border:1px solid var(--line);border-radius:.5rem;cursor:pointer}
.check input{margin-top:.25rem;accent-color:var(--bolt);width:1.1rem;height:1.1rem;flex:none}
.pager{display:flex;justify-content:space-between;gap:1rem;margin-top:3rem;font-weight:600}
.pager a{color:var(--bolt-ink);text-decoration:none;min-width:0}
/* form */
form{display:grid;gap:1rem}
.field{display:grid;gap:.35rem;min-width:0}
.field label{font-weight:600}
.field small{color:var(--mute)}
input[type=text],input[type=tel],input[type=email],select,textarea{width:100%;font:inherit;padding:.7rem .8rem;border:1px solid var(--line);border-radius:.5rem;background:var(--card);color:var(--ink)}
textarea{min-height:6rem;resize:vertical}
fieldset{border:1px solid var(--line);border-radius:.5rem;padding:.75rem 1rem;display:grid;gap:.5rem;min-width:0}
legend{font-weight:600;padding:0 .3rem}
fieldset label{display:flex;gap:.5rem;align-items:center}
button.btn{font:inherit;cursor:pointer;background:var(--bolt);color:#fff;border:2px solid var(--bolt)}
.status{padding:1rem;border-radius:.5rem;background:var(--cloud);color:var(--ink)}
.grads-empty{padding:2rem 1rem;border:2px dashed var(--line);border-radius:.75rem;text-align:left}
.grad{display:grid;grid-template-columns:3.5rem 1fr;gap:.25rem 1rem;padding:.75rem 0;border-bottom:1px solid var(--line)}
.grad .no{font-family:var(--display);font-weight:800;color:var(--bolt-ink);font-variant-numeric:tabular-nums}
@media (prefers-reduced-motion:no-preference){.btn{transition:transform .15s ease}.btn:hover{transform:translateY(-1px)}}
"""

def top(rel):
    return f'''<div class="rainbow"></div><div class="wrap">
<header class="top"><a href="{rel}">Rockland Streamer U</a><nav><a href="{rel}#lessons">Lessons</a><a href="{rel}enrol/">Enrol</a><a href="{rel}graduates/">Graduates</a></nav></header>'''

FOOT = '''<footer><p>Rockland Streamer University is a Little Rock school in Berbice, Guyana. Live classes stream on <a href="https://lrtvs.gy/live/">Channel 10 live</a>. Music bed by <a href="https://885rockfm.com">88.5 Rock FM</a>. Part of the <a href="https://lrtvs.gy/">Little Rock directory</a>.</p>
<p>Family-friendly, always. Pink paint, never gore.</p></footer></div>'''

def doc(title, body, rel, desc):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#0B1A33">{FONT}<link rel="stylesheet" href="{rel}style.css"></head>
<body>{top(rel)}{body}{FOOT}</body></html>'''

def index_body(rel):
    lessons = "".join(
        f'<li><span class="n">{l["n"]:02d}</span><div><a href="{rel}lessons/{l["n"]:02d}/">{html.escape(l["title"])}</a><span class="k">Week {l["week"]} · {html.escape(l["kind"])}</span></div></li>'
        for l in LESSONS)
    return f'''
<section class="hero"><div class="splat"></div><svg class="bolt" viewBox="0 0 60 300" aria-hidden="true"><polyline points="38,0 26,70 40,74 18,160 34,162 10,300" fill="none" stroke="var(--bolt-ink)" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/><polyline points="30,74 46,110" fill="none" stroke="var(--bolt-ink)" stroke-width="2" stroke-linecap="round"/><polyline points="24,162 8,200" fill="none" stroke="var(--bolt-ink)" stroke-width="2" stroke-linecap="round"/></svg>
<div class="eyebrow">Berbice, Guyana · Cohort 1 · free</div>
<h1>Rockland Streamer University</h1>
<p class="lead">Six weeks. Twelve lessons. You go live in the first hour, and you graduate with a one-hour show on Little Rock's own network.</p>
<div class="cta"><a class="btn primary" href="{rel}enrol/">Enrol for Cohort 1</a><a class="btn ghost" href="https://lrtvs.gy/live/">Watch the live class</a></div>
<div class="facts">
<div><b>Mon 19 Oct</b><span>enrolment opens, 20 seats</span></div>
<div><b>Sat 7 Nov, 10:00</b><span>class 1, live from the Pink Room</span></div>
<div><b>Sat 19 Dec</b><span>graduation showcase</span></div>
<div><b>GY$0</b><span>Cohort 1 is sponsored</span></div>
</div></section>

<h2>What you leave with</h2>
<ul class="plain">
<li>A channel that looks finished: name, art, five scenes, clean audio.</li>
<li>Twelve real streams behind you, each one an assignment.</li>
<li>A numbered certificate and a place on the Rockland Streamer U Twitch team.</li>
<li>Your graduation hour carried on Channel 10 live, read out on 88.5 Rock FM.</li>
<li>First call for guest slots on 88.5 and Channel 10.</li>
</ul>

<h2>Five tracks, one classroom</h2>
<p>Everyone takes the same twelve lessons. Your track decides what your graduation show is.</p>
<div class="tracks">
<div class="track"><b>Gamers</b><span>Fortnite and PINKLAND players, 13+ with a guardian under 18. Graduate to Twitch and YouTube.</span></div>
<div class="track"><b>Hosts</b><span>Talkers, DJs, church and community voices. Graduate to 88.5 guest slots and Channel 10 shows.</span></div>
<div class="track"><b>Live sellers</b><span>Market vendors, salons, small shops. Graduate to TikTok and Facebook Live selling with a shop link.</span></div>
<div class="track"><b>Reporters</b><span>Citizen reporters. Graduate to phone live hits into Channel 10 live and LRTVS NewsWatch.</span></div>
<div class="track"><b>Events</b><span>Weddings, services, sports, school events. Graduate to one-phone event streams on lrtvs.gy/live.</span></div>
</div>

<h2 id="lessons">The twelve lessons</h2>
<p>Saturdays 10:00 to 12:00 Guyana time are live in the Pink Room and on Channel 10 live. The other lesson each week is yours to do at home. Every assignment is a real stream.</p>
<ol class="lessons">{lessons}</ol>

<h2>What you need</h2>
<div class="tablewrap"><table>
<tr><th>Kit</th><th>What</th><th>About</th></tr>
<tr><td><b>Phone kit</b></td><td>your phone, a clip-on light, a wired lavalier mic, a small tripod</td><td>US$40 to 60</td></tr>
<tr><td><b>Laptop kit</b></td><td>a laptop, a USB mic, a webcam, wired internet</td><td>US$150 if you own the laptop</td></tr>
<tr><td><b>Studio kit</b></td><td>the Pink Room: book it for an assignment if you have no laptop</td><td>included</td></tr>
</table></div>

<div class="box"><h3>Sponsor a seat</h3><p>Cohort 1 is paid for by Little Rock's advertisers. A sponsor gets a read on every live class, a logo on this page and a stall at graduation. Rates are on the <a href="https://littlerockgy.com/advertisers/">Little Rock advertiser page</a>.</p></div>

<h2>House rules</h2>
<ul class="plain">
<li>Family-friendly, on every channel in this school. Pink paint, never gore.</li>
<li>Students 13 to 17 enrol with a guardian who signs and sits in on the first live.</li>
<li>Nothing private on stream: no addresses, schools, plates, documents.</li>
<li>Cleared music only. The 88.5 Rock FM stream is cleared for every student.</li>
<li>Stream keys are passwords. Never read aloud, never typed in chat, never on screen.</li>
</ul>
'''

def lesson_body(l, rel):
    n = l["n"]
    prev = LESSONS[n-2] if n > 1 else None
    nxt = LESSONS[n] if n < len(LESSONS) else None
    body = "".join(f"<p>{html.escape(p)}</p>" for p in l["body"])
    steps = "".join(f"<li>{html.escape(s)}</li>" for s in l["steps"])
    checks = "".join(f'<li><label><input type="checkbox" id="c{n}-{i}" data-key="rsu-l{n}-{i}">{html.escape(c)}</label></li>' for i, c in enumerate(l["checklist"]))
    pager = '<nav class="pager">'
    pager += f'<a href="{rel}lessons/{prev["n"]:02d}/">← {prev["n"]}. {html.escape(prev["title"])}</a>' if prev else f'<a href="{rel}">← All lessons</a>'
    pager += f'<a href="{rel}lessons/{nxt["n"]:02d}/">{nxt["n"]}. {html.escape(nxt["title"])} →</a>' if nxt else f'<a href="{rel}graduates/">Graduates wall →</a>'
    pager += '</nav>'
    return f'''
<section class="lesson-head"><div class="eyebrow">Lesson {n} · Week {l["week"]} · {html.escape(l["kind"])}</div>
<h1>{html.escape(l["title"])}</h1><p class="lead">{html.escape(l["summary"])}</p></section>
{body}
<h2>Do it</h2><ol class="steps">{steps}</ol>
<div class="box"><h3>Assignment</h3><p>{html.escape(l["assignment"])}</p></div>
<h2>Before you post it</h2><ul class="check">{checks}</ul>
<p class="note">Ticks stay on this phone only.</p>
{pager}
<script>
(function(){{var b=document.querySelectorAll('.check input');b.forEach(function(c){{try{{c.checked=localStorage.getItem(c.dataset.key)==='1'}}catch(e){{}}
c.addEventListener('change',function(){{try{{localStorage.setItem(c.dataset.key,c.checked?'1':'0')}}catch(e){{}}}})}})}})();
</script>'''

def enrol_body(rel):
    return f'''
<section class="lesson-head"><div class="eyebrow">Cohort 1 · 20 seats · free</div>
<h1>Enrol</h1><p class="lead">Enrolment opens Monday 19 October. Classes start Saturday 7 November at 10:00 in the Pink Room, Berbice. Fill this in and Little Rock will message you.</p></section>
<form id="enrol" novalidate>
<div class="field"><label for="name">Your name</label><input type="text" id="name" name="name" required autocomplete="name"></div>
<div class="field"><label for="handle">Handle you want to stream as</label><input type="text" id="handle" name="handle" autocomplete="off"><small>Leave blank if you have not picked one. Lesson 2 helps.</small></div>
<fieldset><legend>Age</legend>
<label><input type="radio" name="age" value="18+" id="age18" checked> 18 or over</label>
<label><input type="radio" name="age" value="13-17" id="age13"> 13 to 17, with a guardian</label></fieldset>
<div class="field" id="guardianField" hidden><label for="guardian">Guardian's name</label><input type="text" id="guardian" name="guardian"><small>The guardian signs the enrolment form and sits in on your first live.</small></div>
<div class="field"><label for="town">Village or town</label><input type="text" id="town" name="town" autocomplete="address-level2"></div>
<div class="field"><label for="track">Track</label><select id="track" name="track">
<option>Gamers</option><option>Hosts</option><option>Live sellers</option><option>Reporters</option><option>Events</option><option>Not sure yet</option></select></div>
<fieldset><legend>You would stream from</legend>
<label><input type="checkbox" name="gear" value="phone" id="gphone"> a phone</label>
<label><input type="checkbox" name="gear" value="laptop" id="glaptop"> a laptop</label>
<label><input type="checkbox" name="gear" value="studio" id="gstudio"> I would need the Pink Room</label></fieldset>
<div class="field"><label for="contact">WhatsApp or GYAFF number</label><input type="tel" id="contact" name="contact" required autocomplete="tel"><small>Used only to reach you about the school. Kept on Little Rock's own server, never published.</small></div>
<div class="field"><label for="why">What do you want to stream, and why?</label><textarea id="why" name="why" maxlength="600"></textarea></div>
<button class="btn primary" type="submit" id="send">Send my enrolment</button>
<div class="status" id="status" hidden></div>
</form>
<script>
(function(){{
var f=document.getElementById('enrol'),st=document.getElementById('status'),g=document.getElementById('guardianField');
function tog(){{g.hidden=!document.getElementById('age13').checked}}
document.querySelectorAll('input[name=age]').forEach(function(r){{r.addEventListener('change',tog)}});tog();
f.addEventListener('submit',function(e){{e.preventDefault();
 var d=new FormData(f),o={{}};d.forEach(function(v,k){{o[k]=o[k]?o[k]+', '+v:v}});
 if(!o.name||!o.contact){{st.hidden=false;st.textContent='Your name and a number to reach you are needed.';return}}
 if(o.age==='13-17'&&!o.guardian){{st.hidden=false;st.textContent='Under 18 needs a guardian\\'s name.';return}}
 st.hidden=false;st.textContent='Sending…';
 fetch('submit',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(o)}})
 .then(function(r){{if(!r.ok)throw 0;return r.json()}})
 .then(function(j){{st.textContent='Received. You are number '+j.number+' on the list. Little Rock will message you on that number.';f.querySelector('#send').disabled=true}})
 .catch(function(){{st.textContent='The form could not reach the school right now. Message 88.5 Rock FM on Facebook (facebook.com/88.5rockfm) with your name, your track and your number instead.'}})
}});
}})();
</script>'''

def graduates_body(rel):
    if not GRADS:
        items = '''<div class="grads-empty"><h3>Cohort 1 graduates on Saturday 19 December 2026.</h3><p>Twenty names, twenty channels, twenty one-hour shows. The wall fills in that evening.</p><p><a class="btn ghost" href="../enrol/">Be one of them</a></p></div>'''
    else:
        items = "".join(f'<div class="grad"><span class="no">{g["number"]:03d}</span><div><b>{html.escape(g["name"])}</b> · {html.escape(g["track"])}<br><a href="{html.escape(g["channel"])}">{html.escape(g["channel"])}</a></div></div>' for g in GRADS)
    return f'''
<section class="lesson-head"><div class="eyebrow">The wall</div><h1>Graduates</h1><p class="lead">Every graduate of Rockland Streamer University, by certificate number, with the channel they stream on.</p></section>
{items}'''

def build():
    if SITE.exists(): shutil.rmtree(SITE)
    if PREVIEW.exists(): shutil.rmtree(PREVIEW)
    SITE.mkdir(); PREVIEW.mkdir()
    (SITE / "style.css").write_text(CSS)
    (SITE / "index.html").write_text(doc("Rockland Streamer University", index_body("./"), "./", "Six-week streaming school in Berbice, Guyana, by Little Rock. Enrol for Cohort 1."))
    for l in LESSONS:
        d = SITE / "lessons" / f"{l['n']:02d}"; d.mkdir(parents=True)
        (d / "index.html").write_text(doc(f"Lesson {l['n']}: {l['title']}", lesson_body(l, "../../"), "../../", l["summary"]))
    (SITE / "enrol").mkdir(); (SITE / "enrol/index.html").write_text(doc("Enrol at Rockland Streamer University", enrol_body("../"), "../", "Enrol for Cohort 1, free, twenty seats."))
    (SITE / "graduates").mkdir(); (SITE / "graduates/index.html").write_text(doc("Rockland Streamer University graduates", graduates_body("../"), "../", "Every graduate and the channel they stream on."))
    # Phone preview for the artifact: the front page without the document skeleton, same files beside it.
    (PREVIEW / "index.html").write_text(f'<title>Rockland Streamer University</title>{FONT}<link rel="stylesheet" href="style.css">{top("./")}{index_body("./")}{FOOT}')
    for p in SITE.rglob("*"):
        if p.is_file() and p.name != "index.html" or p.parent != SITE:
            if p.is_file():
                t = PREVIEW / p.relative_to(SITE); t.parent.mkdir(parents=True, exist_ok=True); shutil.copy(p, t)
    n = sum(1 for _ in SITE.rglob("*.html"))
    print(f"site: {n} pages in {SITE}; preview in {PREVIEW}")

if __name__ == "__main__":
    build()
