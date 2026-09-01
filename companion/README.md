# companion — the app's brain

Instructions and reference that drive the digital guide (the GAP companion / app):
the system prompt, the Big Brother voice references, and the logic for leading a man
through the walk, handing him tools just in time, and keeping his private record.

Most of this already exists in draft in the old `Fraternity/GAP/` folder
(system prompt, companion architecture, the Forge user-journey drafts, voice
references, the layer pipelines). Those are the first thing to curate in here, as
Markdown, once we do a pass on them.

## The five jobs of the companion (from the design)
1. Lead a man through and hand him tools as he needs them (just-in-time delivery).
2. Become the record of what he accomplished, what he serves, who he is, what he
   wants. His living Nosce Te Ipsum. **Private to him.**
3. Facilitate the big brother's facilitation (give the brother visibility and reach).
4. Communication and accountability. This answers the real failure mode: drift.
5. Meta-data for recursive improvement of the system. Earned once men are walking.

## Non-negotiables (see system/user-journey.md and system/voice.md)
- The companion never adjudicates the crossing. It watches for drift, not for the
  state of a man's soul.
- On heavy ground (despair, crisis), it hands the man to a human brother and, when
  needed, real help. It is scaffolding, not the brother, and never the last line.
- It speaks in the house voice: orient, do not flatter or condemn.
- A brother's introspective answers are private to him by design.

## Build order
Lean first. The leanest companion is this repo plus an assistant reading these
instructions. Record and accountability functions come before the recursive-
improvement engine, which has nothing to learn from until walks are happening.
