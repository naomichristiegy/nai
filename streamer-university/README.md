# Rockland Streamer University: what is built

Name chosen by Naomi on 8 Oct 2026. Plan: `GRAND-PLAN.md`. Deploy steps: `DEPLOY.md` (from the Mac).

| Piece | Where | Status |
|-------|-------|--------|
| Site: front page, 12 lesson pages, enrol form, graduates wall | `site/` (built by `build_site.py` from `content/lessons.json` and `content/graduates.json`) | built, checked at phone width, not deployed |
| Phone preview of the site | `preview/` (published as a claude.ai artifact) | published |
| Enrolment endpoint + systemd unit + nginx snippet | `server/` | written and tested locally, not deployed |
| Twitch team art and OBS scene cards | `art/out/*.png` (built by `art/build_art.py`) | built with DejaVu; rebuild with Avenir Next Heavy on the Mac |
| Certificate maker (PNG + PDF, numbered) | `art/certificate.py` | built, sample in `art/out/certificate-sample.*` |
| Copy: NewsWatch story, 88.5 liners, social posts, Twitch team bio, sponsor one-pager, enrolment reply | `COPY.md` | written |
| Legal drafts: enrolment agreement, minors policy, media release, music and platform policy | `legal/` | drafted for Naomi's review |
| Live classroom (MediaMTX path `class`, watch page copy) | droplet | not started, Mac job |
| Streamer U scene collection in Streamlabs | MSI laptop | sent to the MSI session |

Add a graduate: append to `content/graduates.json` (`{"number":1,"name":"...","track":"...","channel":"https://..."}`), run `python3 build_site.py`, redeploy `site/graduates/`.
Make a certificate: `python3 art/certificate.py --name "Full Name" --track Hosts --number 1 --date "19 December 2026" --handle name`.
