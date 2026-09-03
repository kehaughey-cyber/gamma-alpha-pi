# Handoff / State

The living "you are here" for this repo. Read this and `CLAUDE.md` at the start of
a session. Seeded by the session that scaffolded the repo (2026-09-01); update it as
state changes.

## Decisions locked (do not relitigate without reason)

- **Build shape:** a repo-with-instructions plus a companion, not an app-first build.
  The leanest companion is this repo read by an assistant. Ship the hull; the app is
  deferred by design, not cut.
- **The four-problem model is the operational spine:** fear, not starting, not
  finishing, missing information. Every system component maps to one of these.
- **The gates are self-enforcing.** Honesty moves a man, self-deception stalls him,
  no one can force it; the corpus's recursion does the wearing-down. The guide never
  adjudicates the crossing. He watches for drift. Do not build a judge.
- **Two tracks, one program.** The guide track is the back half of the learner track,
  formalized. One replicating level (learner → guide) is enough for the MVP;
  guide-certifies-guide is a later concern.
- **Voice:** the Father is the standard. "Orient, not flatter or condemn." Hunt the
  failure mode: wherever the man vanishes and a list appears, the voice dropped.
- **Formats:** corpus `.md` is canonical; `.docx` is the authoring copy; regenerate
  with `tools/docx_to_md.py` after a rewrite.

## In flight

- Corpus: Coin, Brother, Field Manual rewritten to voice. Father and Nosce Te Ipsum
  still first draft. Big Brother outlined only (`corpus/big-brother/OUTLINE.md`).
- Three brothers are walking now. The loop is not yet proven closed.
- **Constellation mapped (2026-09-01):** the full quarry inventory, keyed to repo
  destinations with a gap picture, is in `CONSTELLATION.md`. Framework lanes
  scaffolded: `governance/`, `website/`, `brand/`, `operations/instruments/` (README
  stubs, empty by design, ready to fill). Repo is public at
  `github.com/kehaughey-cyber/gamma-alpha-pi` — a collaborator can already see it.
- **Companion brain curated (2026-09-01):** `companion/` now holds the deployable
  runtime `system-prompt.md` (with coin + I AM sections merged from their addenda),
  `deployment.md` (Phase-1 stand-up), `ai-conduct.md` (governing constitution), and
  `reference/` (living-coin map; Layer-4 vision marked deferred). A working Phase-1
  Companion can be stood up from these plus the canon today.
- Two things surfaced for Kevin: (a) coin geometry — the deployable prompt and both
  coin addenda say 50 segments / 7.2° / 45 visible; the older architecture doc says
  45 / 8°, treated as superseded pending Kevin's word. (b) The "segment lights →
  credential → gates mentorship" idea drifts toward a judge; parked as an open design
  question, not Phase-1 behavior.
- Note: `GAP/GAP_System_Prompt.docx` is the **book-rewriting** prompt (authoring tool),
  not the companion brain — belongs in `tools/`, still to file.
- Companion tail worked (2026-09-01): narrative/calling pieces confirmed by Kevin as
  raw brain dumps (possible video seed) — left in the quarry, not imported. Kevin
  cleared publish on the personal material, now curated in: `system/forge-journey.md`
  (the full 10-phase "BIOS", complements not replaces `system/user-journey.md`) and
  `system/voice-references/` (The Extension Cord, The Hill with the Ashes — the concrete
  companions to `system/voice.md`). The "Confidential" cover stamp was dropped from the
  Forge doc as self-contradictory in a public repo; "All Rights Reserved" kept.
- **Loose ends cleared (2026-09-01):** book-rewriting prompt curated to
  `tools/book-rewriting-prompt.md` (authoring tool, not the companion brain). Coin symbol
  canon lives in `corpus/coin/book-of-the-coin.md` (~70k words, a chapter per symbol) —
  `companion/reference/coin-symbols.md` is a one-line quick index that defers to the book,
  not a competing canon. The **life
  arc is reconciled**: three stages (son→brother→father) is canonical — it is coin symbol
  #6, Constitution §2.4, and the corpus; the Forge's six (…Husband/King/Elder) are finer
  seasons layered on, noted in `system/forge-journey.md` (Kevin can promote the six if he
  wants). Coin **geometry now confirmed** 50 segments × 7.2° by the coin's own symbol
  reference (45 visible). `GAP_Seek_Ye_First_Master.docx` = funnel content (Website/GTM).
- Still genuinely open: the Forge **metallurgy vocabulary** (adopt repo-wide or keep
  scoped); the four **legal questions for counsel** (parked in `governance/legal-structure.md`).
- **Instruments curated (2026-09-01):** `operations/instruments/` holds the flagship NTI
  `self-assessment.md` (all 45 named aspects + method — richer than the living-coin digest,
  now cross-linked), `allostatic-audit.md`, and `community-map.md`. Left as products/quarry:
  the 35k-word Gratitude Journal, the 3-Day Reset and 90-Minute Mission curricula; the
  community doc's liability waiver + safety plan routed to operations/governance.
- **Ledger stood up (2026-09-01):** `operations/ledger.md` (method, columns, Forge-phase
  stage vocabulary, weekly cadence, the one number that matters) + `ledger-template.csv`.
  The **live ledger with the three real brothers stays private, off this public repo** —
  the repo holds only the template. Kevin fills the private copy.
- **Website content curated (2026-09-01):** `website/site-plan.md` is the full page-by-page
  rebuild plan (purpose, structure, exact copy for 6 pages, colors, type, implementation
  priority) from the rebuild-instructions doc (Confidential stamp dropped; it's public-bound
  site copy). `website/copy-audit.md` checks it vs live and canon: strongly aligned, one open
  tension (the About page uses both the 3-stage and 6-stage arc), and a live-page audit that
  needs the Wix login. Step 4 is now an **implementation gap, not a content gap** — the
  plan's "before publishing the video" list is <2 hrs of Wix work. Still to curate: the WBS
  program-of-work and launch copy (Seek Ye First, Marketing/), mined as needed.
- **WP1 partly executed live in Wix (2026-09-03):** the "You knocked." autoresponse is built
  and **ACTIVE** (Automations → "Join Us autoresponse — You knocked", trigger: Application
  Form). The Join Us sorting question was reworded to the plan's version and made required;
  submit button was already "Take the First Step." Remaining WP1 is the canvas work (video
  embed, door/Knock CTA, resequence Program List → The Journey) — tracked with click-paths
  in `website/wix-checklist.md`. Open: confirm the live Join Us page uses the new Application
  Form (there is also one Old Form). Note: never use "sit with" in copy ([[avoid-phrase-sit-with-it]]).
- **Brand curated (2026-09-01):** `brand/assets/` holds the logo vectors
  (primary/transparent/grayscale), favicon, and the canonical `coin-front.png`;
  `brand/brand.md` is the spec (colors `#000000` + GAP blue `#4A73E8` on white). The 3D
  `.glb` (~10.5 MB) and the production library stay in the quarry, linked. Open item: the
  wordmark type is outlined in the SVGs, so the typeface is unconfirmed — needs Kevin.
- **Governance curated (2026-09-01):** constitution/bylaws reconciliation done.
  Canonical = the Leadership-Council Institutional pair v1.0 → `governance/constitution.md`
  and `governance/bylaws.md` (+ `creed.md`, `legal-structure.md`). The 22k-word
  "Constitution and Bylaws (Karnea 1968/2020)" is a **collegiate fraternity's** document,
  not GAP's — archive, do not use. The two `org/…ORGANIZATIONAL STRUCTURE` docs are
  ChatGPT brainstorms, superseded. Remaining governance work is legal, not editorial:
  `legal-structure.md` lists the open questions for counsel (501(c)(10) vs (c)(7); who
  owns the for-profit IP Company / trust layer; entity names; actual filings).

## The critical path to launch

`MVP-WBS.md` is the deltas-to-MVP work breakdown (Step 4). The hull: **WP1 site go-live
(the ~2 hr Wix "before video" list) → WP2 companion Phase-1 deploy → WP3 intake runbook +
WP4 fill the private ledger + WP5 reading-path check.** Most of it is gated only on Kevin's
Wix login and a decision or two. Full-scale org buildout (legal, council, chapters, app,
Layer-4) is explicitly deferred there.

## Immediate next actions

1. Close the rewrites to voice: Father, then Nosce Te Ipsum.
2. Write the Book of the Big Brother from its outline (Father voice, minus the
   hand-holding; peer-operator register).
3. Curate `Fraternity/GAP/` into `companion/` (system prompt, Forge user journey,
   voice references, layer pipelines) as Markdown.
4. Push to a private GitHub remote so the coding friend has it. Needs Kevin's
   account; then wire the remote and push.
5. ~~Stand up the `operations/` ledger.~~ Done — `operations/ledger.md` + `ledger-template.csv`
   (template only; live data private off-repo). Kevin to fill the private copy for the three.

## Surfaced from the cloud GAP project (2026-09-03)

Kevin's claude.ai **GAP** project holds a lot of production the repo never got. Captured raw
in `_inbox/gap-claude-project.md`; the full nested plan is in `WBS.md`. Highlights:
- **Cloud-only, pull them:** `GAP_Project_Record.docx` (the production log), and
  `transmission-forge.skill` + `verifiers.md` (a built transmission-theory framework).
- **New bodies of work not in the repo:** transmission theory (3 laws), the **Threshold
  Reading** (~30–40pp pre-mine entry), the Book of the King, audiobook/video roadmap, Etsy
  product analysis.
- **⚠️ Corpus-state discrepancy:** the cloud Memory (more recent) says the **Field Manual is
  NOT yet rewritten** (it is "next"), while this repo's CLAUDE.md/HANDOFF claim books 1–3 are
  done. **Resolve before trusting the repo's corpus status.**
- **Hard content rules stated there:** zero em/en dashes; ESV scripture only, verbatim.

## The one metric that matters

Does a little brother become a big brother. That is the loop closing. Everything
else is in service of it.

## Not in this repo (on purpose)

- Raw source material: the `Active/Fraternity` folder (see `ARCHIVE.md`).
- The Etsy "Simple Product" / NextLevelState venture is a separate project with its
  own folder and context. It is not part of GAP and does not belong here.
