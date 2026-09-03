# Gamma Alpha Pi

A lifelong, non-collegiate brotherhood for men 18+. It forms a man through a
sequenced body of work, a big brother who walks beside him, and the fraternity
around them, then equips that formed man to do the same for the next.

**Creed:** *I am a servant of God, to my family, and my community. With love,
strength, and vision, I will act with integrity, grow personally, and uplift,
support, and protect my family and my community. This is my duty, my privilege,
my honor, and my legacy. I am with Brothers.*

Arc of a man: **son → brother → father.** Virtues: **love, strength, vision.**

---

## What this repo is

The canonical foundation for the GAP system: the corpus in plain text, the
design of how it operates, and the instructions for the tools built on top
(the companion / app, the forward-facing site). It is meant to be shared, forked,
and built on. If it is not in here in a readable, diffable form, it is not yet
part of the system.

Raw source material (years of drafts, media, research) stays in the separate
`Active/Fraternity` folder. See `ARCHIVE.md`. This repo holds only the current,
canonical objects.

## The system in one paragraph

Every man is stopped by the same four things regardless of the arena: **fear,
not starting, not finishing, and missing information.** The corpus supplies the
information. The physical coin, the fraternity, the big brother, the little
brother, and the app answer starting and finishing. Fear is answered by a big
brother who recognizes it, mirrors it back without shame, and is living proof it
can be crossed. The gates in the work are **self-enforcing**: an honest answer
moves a man forward, a dishonest one stalls him, and no one can force the honesty.
The big brother's job is not to judge the crossing but to keep a willing man from
drifting before the recursion does its work. See `system/user-journey.md`.

## The corpus (read in order)

| # | Book | Role | Status |
|---|------|------|--------|
| 1 | The Book of the Coin | Orient in the world (external) | rewrite complete |
| 2 | The Book of the Brother | Formation, know thyself (internal) | rewrite complete |
| 3 | The Brother's Field Manual | Tools, converted to motion | rewrite complete |
| 4 | Nosce Te Ipsum (workbook) | Build your actual life | first draft |
| 5 | The Book of the Father | Fatherhood, the long view | first draft (voice standard) |
| 6 | The Book of the Big Brother | Run the walk for another (guide manual) | not written; outline in `corpus/big-brother/OUTLINE.md` |

The `.md` files are the source of truth. The `.docx` originals are edited in Word,
then regenerated with `tools/docx_to_md.py` (see that file's header). Books 1-3
carry the intended voice; 4 and 5 are being brought up to it; the Father already
has the voice and is the standard (`system/voice.md`).

## Layout

```
corpus/        the six books, canonical Markdown
system/        how it operates: user journey (design logic) + the Forge journey
  (phased walk), voice + voice-references, the Big Brother outline
companion/     operator / AI-companion instructions (the app's brain)
operations/    intake, pairing, cadence, the ledger of who is where
  instruments/ the worksheets/assessments a man fills in on the walk
governance/    creed, constitution, bylaws, org structure, chapter formation
website/       the public site: spec, launch copy, the door onto the walk
brand/         the visual identity sources: logo, coin, color, type
tools/         scripts (docx -> md, etc.)
_inbox/        raw capture from chats and old projects, to be refined (see below)
CONSTELLATION.md  the mining index: what's in the quarry, what it maps to, what's a gap
MVP-WBS.md     the deltas to a proven loop: the critical path to launch (Step 4)
WBS.md         the full 11-section WBS with the MVP nested + outstanding tasks across both
ARCHIVE.md     pointer to the raw Fraternity source folder
```

Lanes carry a `README.md` that says what belongs in them and what does not. Several
are freshly scaffolded and mostly empty by design — the framework is set so the
material can be filled in on purpose. See `CONSTELLATION.md` for the gap picture.

## Migrating in old material

Useful content from other chats and projects lands in `_inbox/` first, raw. It
gets refined from there into the canonical `system/` and `companion/` docs. The
rule that keeps this repo clean: **`_inbox/` is raw, everything else is curated.**
Capture messy, file clean.
