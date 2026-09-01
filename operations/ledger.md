# The Ledger

The one instrument that answers the one question: **is the loop closing — does a little
brother become a big brother.** Everything else in this repo is in service of that; the
ledger is how you *see* it. It is deliberately a spreadsheet-shaped thing, not an app. A
row per brother, updated when you touch him.

## Privacy — read this first

This repo is public. **The live ledger never goes in it.** Real brothers' names, stages,
and contact history are private formation data. Keep the live ledger in a private sheet
(a local spreadsheet or a private Google Sheet), off this repo. What lives here is the
**template and the method**; `ledger-template.csv` is the importable starting point. The
example rows below are fictional, to show the shape. (Same rule as the instruments: blank
template in the repo, filled copy stays private — `companion/README.md`, job #2.)

## Columns

| Column | Meaning |
|---|---|
| `brother` | Name or handle. **Private** — real values live off-repo. |
| `joined` | Date he crossed in (took the coin). |
| `role` | `Little Brother` → `Brother` → `Big Brother`. The role is the loop; see below. |
| `current_stage` | Where he is in the walk (the Forge phases, below). |
| `big_brother` | Who is walking with him. Every Little Brother has one. |
| `status` | `moving` or `stalled`. This tracks **drift, not worth** — is he still moving, not whether he is "good enough." |
| `last_contact` | Date of the last real touch. The drift alarm: a lengthening gap is the signal. |
| `produced` | The little brothers he has raised. **This is the replication signal.** |
| `notes` | Anything a human needs to remember before the next contact. |

## The stage vocabulary (from `system/forge-journey.md`)

`Echo` → `Interview` → `Coin` → `Mine` → `Drafting Room` → `Walk` → `Declaration` →
`Forge` → `Reach Back`.

Role follows stage: a man becomes a **Little Brother** when he takes the Coin, a **Brother**
at his Declaration, and a **Big Brother** when he reaches back and takes a little brother of
his own. That last transition is the loop closing.

## The one number that matters

Not headcount. Not revenue. **The count of Big Brothers who came up through the walk** —
men who entered as Little Brothers and have now produced (and are walking with) a little
brother of their own. When that number goes from zero to one, the loop is proven. Three
brothers are walking now; the loop is proven when one of them raises the next.

Everything the ledger tracks rolls up to that. `role = Big Brother` **and** a name in
`produced` = one closed loop.

## How to run it (the cadence)

- **Weekly** is the default cadence for the MVP. Once a week, walk the rows.
- For each brother, ask the drift question, not the worth question: **is he still moving?**
  A stalled status or a stale `last_contact` is a prompt for a human to reach out — never a
  judgment on the man. (The gate enforces honesty on its own; the big brother's job is to
  keep a willing man from drifting before the recursion finishes — `system/user-journey.md`.)
- Update `status`, `last_contact`, and `current_stage` as they change. When a man reaches
  back, move his `role` to Big Brother and start a row for the new Little Brother, with this
  man in the new row's `big_brother`.

## Example (fictional — shows the shape)

| brother | joined | role | current_stage | big_brother | status | last_contact | produced | notes |
|---|---|---|---|---|---|---|---|---|
| A. | 2026-03-01 | Big Brother | Reach Back | (founder) | moving | 2026-08-28 | B. | first loop closing — now walking B. |
| B. | 2026-07-15 | Little Brother | Mine | A. | moving | 2026-08-27 | — | deep in the fear work; check in |
| C. | 2026-06-10 | Brother | Forge | (founder) | stalled | 2026-07-30 | — | last_contact stale — reach out |
