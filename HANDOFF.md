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
- Open reconciliations surfaced by the Forge doc: life arc is 3-stage (son→brother→
  father) in README vs 6-stage (Son/Brother/Husband/Father/King/Elder) in the Forge;
  new vocabulary to adopt or not (Forge/Mine/Bloom metallurgy, Wounded Lion / Excuse
  Maker). `GAP_Seek_Ye_First_Master.docx` reclassified as funnel content (Website/GTM).
- **Governance curated (2026-09-01):** constitution/bylaws reconciliation done.
  Canonical = the Leadership-Council Institutional pair v1.0 → `governance/constitution.md`
  and `governance/bylaws.md` (+ `creed.md`, `legal-structure.md`). The 22k-word
  "Constitution and Bylaws (Karnea 1968/2020)" is a **collegiate fraternity's** document,
  not GAP's — archive, do not use. The two `org/…ORGANIZATIONAL STRUCTURE` docs are
  ChatGPT brainstorms, superseded. Remaining governance work is legal, not editorial:
  `legal-structure.md` lists the open questions for counsel (501(c)(10) vs (c)(7); who
  owns the for-profit IP Company / trust layer; entity names; actual filings).

## Immediate next actions

1. Close the rewrites to voice: Father, then Nosce Te Ipsum.
2. Write the Book of the Big Brother from its outline (Father voice, minus the
   hand-holding; peer-operator register).
3. Curate `Fraternity/GAP/` into `companion/` (system prompt, Forge user journey,
   voice references, layer pipelines) as Markdown.
4. Push to a private GitHub remote so the coding friend has it. Needs Kevin's
   account; then wire the remote and push.
5. Stand up the `operations/` ledger (a spreadsheet) for the three brothers.

## The one metric that matters

Does a little brother become a big brother. That is the loop closing. Everything
else is in service of it.

## Not in this repo (on purpose)

- Raw source material: the `Active/Fraternity` folder (see `ARCHIVE.md`).
- The Etsy "Simple Product" / NextLevelState venture is a separate project with its
  own folder and context. It is not part of GAP and does not belong here.
