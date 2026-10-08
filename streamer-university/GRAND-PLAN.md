# Little Rock Streamer University: the grand plan

Written 8 Oct 2026 by Fancy in a cloud session. Nothing here is built yet. Naomi decides the name, the price and the date; everything else below is ready to execute.

## 1. What it is, in one breath

A school in Berbice that turns ordinary people into working live streamers in six weeks, then gives them a network to stream on. Little Rock already owns the network (Channel 10 live at lrtvs.gy/live, 88.5 Rock FM, LRTVS NewsWatch, the Twitch channels, PINKLAND games) and the know-how (the OBS and Streamlabs recipes, the Twitch kits, the MediaMTX server). The university packages that know-how into lessons and the network into a graduation stage. No other school in Guyana can offer the stage.

Working name: **Little Rock Streamer University** (short: **Streamer U**, handle `streameru`). Alternatives if she prefers: *LRTVS Streamer Academy*, *The Pink Room School*. The school belongs to Little Rock, the family brand. It is never described as founded by Naomi.

## 2. Who it is for (five tracks, one curriculum)

| Track | Who | Where they end up |
|-------|-----|-------------------|
| Gamers | 13+ (with a guardian under 18), Fortnite and PINKLAND players | Twitch and YouTube channels on the Streamer U Twitch team |
| Hosts | talkers, DJs, church and community voices | 88.5 Rock FM guest slots, Channel 10 live shows |
| Live sellers | market vendors, salons, small shops | TikTok and Facebook Live selling, Shopify link in bio |
| Reporters | citizen reporters for LRTVS NewsWatch | phone live hits into Channel 10 live and NewsWatch |
| Events | weddings, church services, sports, school events | one-phone or one-laptop event streams to lrtvs.gy/live |

Everyone takes the same twelve lessons. The track decides the graduation project.

## 3. The curriculum: six weeks, twelve lessons

Two lessons a week: one live class on Saturday (in the studio and streamed on Channel 10 live), one self-paced lesson page with a video and an assignment. Every assignment is a real stream, starting at two minutes long.

| Week | Lesson | Assignment |
|------|--------|------------|
| 1 | **Go live from a phone today.** TikTok, Instagram, Facebook, YouTube on a phone. Framing, light, sound in a Berbice room. | A two-minute live, any platform |
| 1 | **Your channel, your name.** Picking a handle, profile picture, banner, bio. Country and age settings. Two-factor on every account. | Channel set up on two platforms |
| 2 | **Audio first.** Why viewers forgive bad video and never bad audio. Phone mics, a US$20 lavalier, headsets, room echo. | A five-minute live where chat says the audio is clean |
| 2 | **The computer stream.** OBS Studio from zero: scenes, sources, the stream key (never shared), 720p30 on wifi, 1080p60 on a wire. Streamlabs as the easy road. | First OBS stream, dropped frames at zero |
| 3 | **Scenes and brand.** Starting soon, live, BRB, ending. Name bug, chat overlay, alerts. The Twitch kit as the template. | Five-scene collection built |
| 3 | **Talk to nobody, then to everybody.** Hosting an empty room, reading chat, the first 30 seconds, the hook, the schedule. | A 30-minute stream with a fixed start time |
| 4 | **Games on stream.** Game capture, console capture, PINKLAND browser games, Fortnite settings for streaming. Family-friendly content rules. | A game stream with a webcam |
| 4 | **Music and the law.** What gets a channel muted or banned. Using 88.5 Rock FM as the licensed station bed. Copyright strikes, DMCA, fair use myths. Taught by Naomi. | Stream using only cleared audio |
| 5 | **Money.** Twitch Affiliate and Partner, YouTube Partner, TikTok gifts, sponsors, selling on live, Shopify link in bio, how a Guyanese streamer gets paid out. | A revenue plan on one page |
| 5 | **Safety and minors.** Doxxing, location leaks, kids on camera, guardians, moderation, AutoMod, blocking, when to stop a stream. | Moderation settings screenshot, moderator named |
| 6 | **Clips, VODs and growth.** Clipping, shorts, posting schedule, cross-posting to TikTok, thumbnails, titles that get clicked. | Three clips from your own VOD |
| 6 | **Graduation stream.** A one-hour show on the Streamer U stage, judged live. | The graduation stream |

Graduates get: a certificate (PDF, pink, numbered), a place on the Streamer U Twitch team, a listing on the graduates wall at lrtvs.gy/university, and first call for 88.5 and Channel 10 guest slots.

## 4. Where it lives online

Everything reuses the Little Rock stack: static HTML on the droplet behind nginx, the same way lrtvs.gy/live and the PINKLAND games are served.

| Piece | URL | Built from |
|-------|-----|-----------|
| Front page, tracks, dates, enrol button | `https://lrtvs.gy/university/` | new static page, Guyana Days layer, PWA like the watch page |
| Twelve lesson pages | `https://lrtvs.gy/university/lessons/01` to `/12` | one template, text plus embedded video plus assignment |
| Live classroom | `https://lrtvs.gy/university/live/` | the Channel 10 watch page pointed at a new MediaMTX path `class` |
| Enrolment form | `https://lrtvs.gy/university/enrol/` | static form posting to a small endpoint on the droplet, writes a CSV, emails Naomi |
| Graduates wall | `https://lrtvs.gy/university/graduates/` | generated from one JSON file |
| Class group | GYAFF group "Streamer U Cohort 1" | her own messenger, not WhatsApp |
| Twitch team | `twitch.tv/team/streameru` | created from the therockfm885 account |
| Lesson videos | YouTube, unlisted playlist on the 88.5 or personal channel | recorded in the studio on the MSI |
| Payments (cohort 2 onward) | Shopify product "Streamer U tuition" | the existing Shopify store |

## 5. Hardware: three kits

| Kit | Contents | Cost (US$, approx) | Who |
|-----|----------|-------------------|-----|
| Phone kit | the student's phone, clip-on ring light, wired lavalier mic, small tripod | 40 to 60 | every student, week 1 |
| Laptop kit | any laptop with a GeForce or a recent Intel or AMD chip, USB mic, webcam, wired internet | 0 if owned, 150 for mic and webcam | gamers and hosts, week 2 |
| Studio kit | the Pink Room: MSI laptop running OBS or Streamlabs, studio camera, 88.5 audio feed, ring lights | already owned | live classes and graduation |

The studio is also the lending library: a student without a laptop books the Pink Room for their assignment.

## 6. Money

- **Cohort 1 is free.** Twenty students, founding class. The price of free is a testimonial and a graduation stream on the network.
- **Sponsors pay for cohort 1.** The 88.5 advertiser list (littlerockgy.com/advertisers) is offered "Sponsor of Streamer U": logo on the site, a read on every live class, a stall at graduation. Target: three sponsors.
- **Cohort 2 is paid.** Naomi sets the price. Placeholder for the plan: GY$ price to be decided, paid by Shopify checkout, with two sponsored seats per cohort.
- **Graduates earn, Little Rock earns.** Graduates streaming on the Streamer U team keep their own platform money. Streams that air on Channel 10 live or 88.5 are paid guest slots on Little Rock's existing advertising, not a cut of the student's channel.
- **Merch.** Streamer U shirts and the pink certificate frame through Shopify, month two.

## 7. Legal and safety (Naomi's part, she is the lawyer)

Documents to draft before enrolment opens:
1. Enrolment agreement and code of conduct (family-friendly, pink paint never gore, no harassment, attendance).
2. Minors policy: 13 to 17 only with a guardian's signature, guardian present for the first live, no home address or school on stream.
3. Media release: Little Rock may rebroadcast class and graduation streams.
4. Platform compliance sheet: Twitch, YouTube, TikTok minimum ages and country settings, stated plainly to students.
5. Music policy: 88.5 Rock FM's stream is the only station bed used in class; students clear their own music or use platform libraries.
6. Privacy: the enrolment CSV lives on the droplet only, never in git, never in chat.

Rules carried from every Little Rock project: no always-listening devices in the studio, secrets move by USB, every Little Rock account's country is United States, Justus stays off camera.

## 8. Launch timeline

| Date | Milestone | Who |
|------|-----------|-----|
| Thu 8 Oct | Plan written | Fancy, done |
| by Mon 12 Oct | Name, logo direction, tuition decision | Naomi |
| by Fri 16 Oct | Site, lesson template, enrol form, Twitch team art, GYAFF group spec built | Fancy (cloud and Mac) |
| Sat 17 Oct | Soft announce: one line on 88.5, a NewsWatch story, the lrtvs.gy directory entry | Naomi on air, Fancy writes the story (never in her voice as self-promotion; it is a Little Rock announcement) |
| Mon 19 Oct | Enrolment opens, 20 seats | site live |
| Fri 30 Oct | Cohort 1 chosen, GYAFF group opened, kits list sent | Naomi picks, Fancy sends |
| Sat 7 Nov, 10:00 GYT | Class 1 live from the Pink Room on Channel 10 live | Naomi hosts, MSI streams |
| every Sat to 12 Dec | Classes 3, 5, 7, 9, 11 live; even lessons self-paced | |
| Sat 19 Dec | Graduation showcase: 20 one-hour streams across the day on the Streamer U team, highlights on Channel 10 live | everyone |
| Jan 2027 | Cohort 2 opens, paid, sponsored seats | |

## 9. What Fancy builds, by machine

**Cloud session (this repo):** site pages, lesson template and the twelve lesson texts, enrol form front end, certificate generator, graduates wall generator, Twitch team and sponsor art, the NewsWatch announcement, this plan kept current.

**MacBook Air (main Fancy, has the droplet):** deploy `/university/` to nginx, add MediaMTX path `class` with its own key, the enrol endpoint and its CSV, DNS unchanged (lrtvs.gy already resolves).

**MSI laptop (the studio stream machine):** the Streamer U scene collection in OBS or Streamlabs (Starting soon, Class, Student screen share, BRB, Ending), the studio camera as source, 88.5 audio bed, record every class locally as the lesson video. This is the same recipe as `TWITCH-885-KIT/STREAMLABS-885-STATION-CAM.md`, re-skinned.

**Pink GeForce desktop:** not needed for the school. Stays on Unreal and ROCKLAND GAMES.

## 10. Clicks only Naomi can make

1. Pick the name and say yes or no to the logo direction (pink, crown motif from the Queen of Ace rebrand, never the old shield).
2. Decide cohort 2 tuition and whether cohort 1 is free.
3. Create the Twitch team from the therockfm885 account (Fancy cannot; it needs her login).
4. Create the GYAFF group and add Fancy's enrolment bot later if wanted.
5. Say the one line on 88.5 and approve the NewsWatch story.
6. Sign off the four legal documents in section 7.
7. Host Saturday classes. Fancy runs the stream; Naomi teaches.

## 11. First seven days, day by day

- **Day 1 (today):** read this, answer section 10 items 1 and 2 in one message.
- **Day 2:** Fancy builds the front page and enrol form, sends the preview link.
- **Day 3:** Fancy writes lessons 1 to 4 and records nothing yet; Naomi reads them on her phone.
- **Day 4:** Twitch team art and sponsor one-pager done; Naomi forwards the one-pager to three advertisers.
- **Day 5:** MSI session builds the Streamer U scene collection and does a five-minute private test to the `class` path.
- **Day 6:** NewsWatch story drafted, 88.5 one-liner drafted.
- **Day 7 (Sat 17 Oct):** soft announce on air. Enrolment opens Monday.

## 12. How this plan reaches the MSI and the Mac

This file lives in the `nai` repo on branch `claude/charming-fermi-spma9x`. Any Claude Code session opened inside a clone of this repo reads `CLAUDE.md` automatically and can open this plan. On the MSI: clone the repo, open that folder in Claude Desktop or run `claude remote-control` in it, and say "read streamer-university/GRAND-PLAN.md and build the Streamer U scenes". The plan should later move to the `littlerock` repo next to `TWITCH-885-KIT`, where the rest of Little Rock lives.
