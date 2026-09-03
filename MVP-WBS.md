# MVP — the deltas to a proven loop

The work breakdown for **Step 4: cross the minimum public-launch threshold.** Not the full
global-fraternity buildout (that WBS exists in the quarry and is mostly Step-5 scale
scaffolding — councils, elections, chapters, alumni, expansion). This is the hull: the
smallest set of deltas that lets a man who does not already know Kevin walk the loop, and
lets us *see* whether it closes.

Read with `HANDOFF.md` (state) and `CONSTELLATION.md` (what exists). For how this hull nests
inside the full 11-section fraternity WBS (and the outstanding tasks across both), see
`WBS.md`. Owners: **K** Kevin, **C** collaborator, **A** AI-assist (me, where a login or a
human is not required).

## What MVP is (the done-test)

> One complete loop runs as a **system**, not as Kevin's personal mentorship: a stranger
> finds GAP → is sorted in → walks the corpus with a big brother and the companion → is
> tracked in the ledger. MVP is *done* when that path is demonstrably runnable end to end
> and the one metric is instrumented.

The one metric (from `HANDOFF.md`): **does a little brother become a big brother.** MVP
makes the loop runnable; the loop is *proven* when the metric first reads one. Three
brothers are walking now — the system around them is what MVP builds.

## Critical path (MVP-blocking — do these)

Each is small. The point is that together they close the loop.

### WP1 · The front door routes a man — website go-live
The content is done (`website/site-plan.md`); this is implementation, not authoring.
- Do the plan's "before publishing the video" list: add the Join Us sorting question (required long-text), set the "You knocked." autoresponse, rename submit to "Take the First Step", embed the intro video on Home, resequence Program List → The Journey. **~2 hrs of Wix work.**
- Owner: **K** (Wix login) — **A** can co-drive in the in-app browser if you authenticate.
- Depends on: nothing. **Highest leverage, do first.**
- Done when: a stranger can land, feel seen, knock, submit the sorting question, and get the autoresponse.

### WP2 · The companion is live — Phase 1 deploy
- Stand up the Claude Project (or Custom GPT) per `companion/deployment.md`: paste `companion/system-prompt.md`, load the canon in priority order, run the five boundary tests, put the link behind member login on the site.
- Owner: **K** / **A**-assist. **~1–2 hrs.**
- Depends on: nothing (canon is curated). Site link placement depends on WP1.
- Done when: a brother can open the companion, get a canon-grounded session, and the crisis + Big-Brother-simulation boundaries hold.

### WP3 · Intake → the walk is wired
The seam between the public door and the corpus. Mostly a decision + a checklist, not a build.
- Define the exact hand-off: form submission → Kevin's personal reply/conversation → assign a big brother → hand the first instrument (the 3-Day Reset as entry, then the self-assessment). Write it as a one-page intake runbook in `operations/`.
- Owner: **K** (owns pairing) / **C** to draft the runbook.
- Depends on: WP1 (the form).
- Done when: there is a written, repeatable path from "form submitted" to "walking, with a big brother assigned."

### WP4 · The loop is instrumented — ledger live
- Fill the **private** ledger (`operations/ledger-template.csv` → a private sheet) with the three current brothers; set the weekly cadence (`operations/ledger.md`).
- Owner: **K**. **~30 min + weekly.**
- Depends on: nothing.
- Done when: every walking brother has a row, and the weekly drift check is a standing habit.

### WP5 · The MVP reading path is navigable
The corpus a man actually walks for MVP is ready; confirm the path holds together.
- Confirm the public "Journey" sequence (3-Day Reset → Coin → Brother 1–3 → Nosce Te Ipsum → Allostatic Audit → the self-assessment) is coherent and each piece is reachable. Books 1–3 are to voice; Father/Nosce first-draft are usable as-is for the walk.
- Owner: **C/K**. **Light — a read-through, not new authoring.**
- Done when: a brother can move through the sequence without hitting a missing or contradictory piece.

## Quality deltas (loop runs without these — they raise efficacy)

Not blocking MVP; schedule after the loop is live.
- **Father + Nosce Te Ipsum to voice** — first draft is walkable now; finishing raises the walk's quality (`HANDOFF.md`).
- **Full visual site rebuild + live-page audit** — beyond WP1's two hours: the dark/gold rebuild, mobile pass, SEO (`website/site-plan.md`, `website/copy-audit.md`). The live-page audit needs the Wix login.
- **Settle the About-page life arc** (`website/copy-audit.md`) — a one-line fix, but a decision (K).

## Replication delta (this is what MVP ultimately exists to enable)
- **One brother reaches back and raises a little brother.** The founder can guide the first replication personally; that already proves the loop *can* close. Removing the dependence on Kevin — so any big brother can run the walk — is the **Book of the Big Brother** (`corpus/big-brother/OUTLINE.md`, not yet written). Writing it is the delta from "loop closes with the founder" to "loop closes without him." MVP-adjacent: needed to prove the loop is *self*-replicating, not just founder-driven.

## Explicitly deferred (NOT pre-MVP — resist these keels)
The source WBS is full of these; they are Step 5, and building them now is the project's
historical failure mode.
- Legal entity filing, 501(c)(10)/(c)(3) determinations, the IP company / trust — needed before money-at-scale, **not** before the first loop (`governance/legal-structure.md`, for counsel).
- Leadership Council formation, officer elections, national/international structure, chapters, alumni relations, expansion (source WBS §§4–11).
- The Phase-2 app (visual coin, persistent memory, database) and the Layer-4 intelligence/finance/tool engine (`companion/reference/layer4-intelligence.md`) — earned once men are walking, not before.

## The critical path in one line
**WP1 (site) → WP2 (companion) → WP3 (intake) + WP4 (ledger) + WP5 (path check)** — a few
hours of focused work, most of it gated only on Kevin's Wix login and a decision or two.
After that, MVP is live and the only thing left is time and the metric.
