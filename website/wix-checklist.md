# Wix Implementation Checklist (WP1)

The "before the video goes out" list from `site-plan.md`, tracked. Full copy for every
item is in `site-plan.md`; this is the do-it checklist with the click-paths. Site is
Wix **Studio** (dark dashboard, "Edit Site" opens the canvas editor).

## Done (live)
- [x] **Sorting question reworded + required** on the Join Us / Application Form — label "In your own words, what is happening in your life right now…", placeholder "Take your time with this…", marked required.
- [x] **Submit button** already reads **"Take the First Step."**
- [x] **"You knocked." autoresponse** built and **ACTIVE** — Automations → "Join Us autoresponse — You knocked" (trigger: Application Form submitted). Emails every real submitter. Sender shows "Gamma Alpha Pi" / reply-to kevin@gammaalphapi.com; the Wix free-plan footer line needs a paid plan to remove.

## To do — the canvas parts (in the Editor: "Edit Site")

These are drag-and-drop; do them by hand. Exact copy is in `site-plan.md` under each page.

### 1. Embed the intro video on Home
1. **Edit Site** → make sure the page dropdown (top-left) says **Home**.
2. Decide the video source: a **YouTube link** (easiest — the GAP channel) or an upload to Wix Video Library.
3. Left toolbar **Add (+)** → **Video** → **Video Player** (for upload) or **Embed → YouTube/Social** (for a link). Drag it into the page, in the testimony area / above the fold.
4. Paste the YouTube URL (or pick the uploaded file). Set **Autoplay OFF**. Choose a strong thumbnail (you looking at camera).
5. Resize to full-width; check it on **mobile** (the phone icon, top of the editor).
6. **Publish** (top-right) when the page is right — that push is yours.

### 2. Add the door image + "Knock" button on Home
1. Source a **heavy wooden door with an iron knocker** image (stock or your own). Upload via **Add (+) → Image**.
2. Place it full-width in the Home "door" section (near the bottom, before the Creed).
3. Above it, add a **Text** element: **Ask. Seek. Knock.** (gold), with **Matthew 7:7** small beneath.
4. **Add (+) → Button**, label it **Knock**, and set its link to the **Join Us** page (`/join-us`). This is the only CTA on Home.
5. On **mobile**, make sure the door is visible and **Knock** sits above the fold or right under the door.
6. **Publish**.

### 3. Resequence "Program List" → "The Journey"
1. In the Editor, open the **Program List** page. Rename it (page settings → page name / nav label) to **The Journey**; confirm its URL/slug is acceptable (the site-plan nav assumes `/challenges`).
2. Reorder the existing program entries into this exact order, each with the one-line description from `site-plan.md` (Page Three):
   1. The 3-Day Reset — "Start here…"
   2. The Book of the Coin
   3. Book of the Brother 1 of 3
   4. Book of the Brother 2 of 3
   5. Book of the Brother 3 of 3
   6. Nosce Te Ipsum
   7. The Allostatic Audit
   8. The Path of Ownership
3. Update the page **nav label** to **The Journey** and its position in the menu (Home · About · The Journey · Join Us · Books, Coin and Merch).
4. **Publish**.

## Also on the plan (later, not blocking launch)
Full visual rebuild (dark `#111111` / gold `#8B6914`), mobile pass, SEO titles/descriptions,
remove the PayPal donate button, move Contact to footer-only. All specified in `site-plan.md`.

## Two open confirmations
- The autoresponse is scoped to the **Application Form** (the only new Wix form). There is also **one Old Form** in Forms & Submissions — confirm the live Join Us page uses the new Application Form, not the old one, so the autoresponse fires.
- The sorting question is now **required**; if you'd rather it stay optional, toggle it back in Forms → Application Form → that field → Field Settings.
