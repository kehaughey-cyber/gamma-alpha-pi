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
