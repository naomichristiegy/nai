# Deploy Rockland Streamer University (from the Mac, which holds the droplet access)

1. Build: `python3 build_site.py` (site/) and `python3 art/build_art.py` (art/out/). Swap the font for Avenir Next Heavy in `art/build_art.py` first if the Mac has it.
2. Pages: `scp -r site/* root@67.205.145.217:/var/www/lrtvs-home/university/`
3. Endpoint: `scp server/enrol.py root@67.205.145.217:/opt/streameru/enrol.py` and `scp server/streameru-enrol.service root@67.205.145.217:/etc/systemd/system/`, then on the droplet `systemctl enable --now streameru-enrol` and `curl -s 127.0.0.1:8160/health`.
4. nginx: add `server/nginx-university.conf` inside the lrtvs.gy 443 block in `/etc/nginx/sites-enabled/gy-extra`, back up first to `/root/nginx-backups/`, `nginx -t`, `systemctl reload nginx`.
5. Live classroom: add MediaMTX path `class` in `/opt/mediamtx/mediamtx.yml` (copy of `ch10` with its own key, publish user `studio`), restart mediamtx, and point a copy of the Channel 10 watch page at `/live/hls/class/index.m3u8` served as `/university/live/`. Key goes on a USB to the MSI, never in chat.
6. Directory: add "Rockland Streamer University, https://lrtvs.gy/university/" to the Education or TV section of `LRTVS-DIRECTORY` in the littlerock repo and rebuild lrtvs.gy.
7. Check from a phone: front page, lesson 1, enrol form sends and gets a number, graduates page.
8. Reading the list: `ssh root@67.205.145.217 cat /opt/streameru/enrol.csv`. Never copy it into a chat or a repo.
