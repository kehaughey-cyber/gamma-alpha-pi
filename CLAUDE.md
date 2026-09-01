# CLAUDE.md — Gamma Alpha Pi

Standing context for any AI session working in this repo. Read this first, then
`HANDOFF.md` for current state and next actions.

## What this is

The foundation for the Gamma Alpha Pi system: a men's fraternity that forms a man
through a corpus + a big brother + the brotherhood, then equips him to form the
next man. This repo holds the canonical corpus (plain-text Markdown), the system
design, and the instructions for tools built on top (companion/app, website).

Operator: Kevin. He is the author of the corpus and the architect of the system.
A friend who codes is helping build the forward-facing pieces, so **everything
here must read clearly to a smart collaborator who was not in the room.**

## How to work here

- **Voice is law.** The house voice is defined in `system/voice.md`. Its thesis:
  *not here to flatter you or condemn you, here to orient you.* The Book of the
  Father is the voice standard. When you draft or edit corpus text, match it, and
  hunt the failure mode: wherever the man disappears and a list appears, the voice
  has dropped.
- **Orient, don't flatter or condemn — including toward Kevin.** He has explicitly
  asked not to be agreed with reflexively and not to be argued with for sport.
  Push where he is likely wrong, yield where he is right, do not manufacture
  resistance to prove you are not a yes-man. Calibration, both directions.
- **The gates are self-enforcing. Do not rebuild a judge.** The system works
  because an honest answer moves a man and a dishonest one stalls him; no guide
  adjudicates the crossing. Never propose "assessment tools" that judge whether a
  man is truly honest or truly set. The guide watches for *drift* (is he still
  moving), never for the state of his soul. See `system/user-journey.md`.
- **Ship the hull, not more keels.** The failure mode of this project historically
  is building elaborate systems before a working loop runs. There are three real
  brothers walking now. Bias every recommendation toward what gets a man through
  the loop, and toward the smallest thing that could work.

## The build doctrine (Kevin's, hold him to it)

Value first: money is a fraction of value returned. Start at a **delta** you have
the talent to close. **Why you, why yours** must be a real, hard-to-copy advantage,
or it is noise added to a solved problem. Quality delivered reliably compounds into
**reputation**, which is what builds an enterprise. This repo is exactly that bet:
it is made of Kevin's hard-to-copy talent (rigorous systematized transmission), and
a brotherhood is a reputation-and-referral engine by nature.

## The corpus and its order

Coin (orient) → Brother (form) → Field Manual (tools) → Nosce Te Ipsum (build your
life) → Father (the long view) → Big Brother (run the walk for another). The `.md`
in `corpus/` is canonical; regenerate from the Word originals with
`tools/docx_to_md.py`. Books 1-3 are rewritten to voice; 4-5 are first draft; 6 is
outlined only (`corpus/big-brother/OUTLINE.md`).

## Current state (as of 2026-09-01)

- Corpus: books 1-3 rewritten to the new voice; Father and Nosce Te Ipsum still
  first draft; the Big Brother book is outlined, not written.
- Next writing: close the rewrites, then write the Book of the Big Brother from the
  outline, in the Father's voice minus the hand-holding (peer-operator register).
- The app is deferred by design, not cut: walk the first men in the lean form
  first; the app's record and accountability functions come first, its
  recursive-improvement data is earned by actual walks. The leanest form of the
  app is this repo plus a companion driven by `companion/` instructions.

## Session end

This is a normal git repo. Commit changed files with clear messages. Keep the
corpus `.md` in sync with the `.docx` originals via the converter when books change.
