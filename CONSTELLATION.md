# Constellation Map

The mining index for Gamma Alpha Pi. `ARCHIVE.md` says *where* the raw quarry is;
this says *what is in it, what it maps to, and whether it is in the repo yet.* It is
the working map for **Step 1 (scaffold) → Step 2 (find the gaps)**. It is a map, not
a manifest of imports — nothing moves into the repo except on purpose, converted to
Markdown, per the intake rule in `README.md` and `_inbox/README.md`.

**Read this with `README.md` (what the repo is) and `HANDOFF.md` (what's in flight).**

Status legend:

- ✅ **in repo** — canonical object already lives here, in readable/diffable form
- 🟡 **partial** — a version is here but it's draft / incomplete / not to voice yet
- 🔴 **gap** — exists only in the quarry (or nowhere); needs curating in
- 📦 **archive-only** — stays in the quarry by design (media, source scholarship, old revisions); pull a piece only when a specific need calls for it

---

## The three sources

| Source | Where | How to pull from it | Notes |
|---|---|---|---|
| **The quarry (on-disk)** | `Active/Fraternity/` | Curate straight into structured folders (converted to `.md`), or stage via `_inbox/`. No bulk import. | 4,416 files. Substance is ~260 docs (192 `.docx`, 47 `.pdf`, 16 `.xlsx`, 5 `.pptx`); the other ~4,150 are media/design assets. |
| **Web chats & other projects** | Claude projects, other assistants | Cannot be read from disk — **export/paste the useful parts into `_inbox/` manually**, then refine. | The one seam that needs your hands. Name each file by source + topic. |
| **The live public surfaces** | `gammaalphapi.com` + Wix editor (backend), YouTube, TikTok, Facebook, Discord | Public pages/channels are viewable now (though social platforms resist automated reading); the Wix editor and any channel backend are behind Kevin's login — **manual seams**. Registered in `website/channels.md`. | Storefront + channels already live (see Website lane). |

---

## The map, by destination lane

### 1. Corpus — `corpus/` (the six books)

The repo already holds canonical `.md` for books 1–5; the quarry holds the `.docx`
authoring originals plus a long tail of old revisions.

| Book | In repo | Authoring original in quarry | Status |
|---|---|---|---|
| 1 · Coin | `corpus/coin/book-of-the-coin.md` | `Books/The Book of the Coin.docx`, `GAP/Book of The Coin Rev 1.docx` (+ revoicing directions) | ✅ rewrite complete |
| 2 · Brother | `corpus/brother-philosophy/book-of-the-brother.md` | `Books/The Book of the Brother.docx` (+ Rev 1, additions, Old versions) | ✅ rewrite complete |
| 3 · Field Manual | `corpus/brother-fieldmanual/brothers-field-manual.md` | `Books/The Brothers Field Manual.docx` (+ Rev 1) | ✅ rewrite complete |
| 4 · Nosce Te Ipsum | `corpus/nosce-te-ipsum/nosce-te-ipsum.md` | `Books/Nosce Te Ipsum.docx` / `.pdf` | 🟡 first draft |
| 5 · Father | `corpus/father/book-of-the-father.md` | `Books/THE BOOK OF THE FATHER.docx`, `Books/Old versions/BOOK OF THE FATHER.docx` | 🟡 first draft (voice standard) |
| 6 · Big Brother | `corpus/big-brother/OUTLINE.md` | *(none — not written)* | 🔴 outline only |

Feeder / satellite corpus material in the quarry (candidates to fold into a book or
a workbook, not standalone books): `Books/Admonition to Men`, `Rites of Passage`,
`Shuhari`, `basic tenets of change`, `The Calling`, `Love Strength and Vision Outline`,
`From Laborer to Leader`, `Books/Old versions/10 degrees Workbook`, `The Law of Success`.
→ 🔴 unmapped; decide per piece in Step 2.

### 2. System / design — `system/`

How the thing operates. Repo has the two load-bearing docs; the quarry has more.

| Object | In repo | Quarry source | Status |
|---|---|---|---|
| User journey | `system/user-journey.md` | `GAP/The_Forge_Master_User_Journey_v3_Updated.docx` (+ v1, v2, v3) | ✅ / 🟡 reconcile against latest Forge draft |
| Voice standard | `system/voice.md` | `GAP/GAP_Voice_Reference.docx` | ✅ |
| Big Brother outline | `system/` ← `corpus/big-brother/OUTLINE.md` | — | ✅ outline |
| Movement architecture | — | `GAP/Movement Architecture Conversation Document May 2026.docx` | 🔴 gap |
| The four-problem spine, control map | — | `GAP/90-Second Control Map.docx`, `GAP/three questions.docx` | 🔴 gap |
| Journey metaphors | — | `GAP/Valley Meadow Mountain.docx`, `images/Hero's journey.docx` | 🔴 gap |
| Rituals / rites / degrees | — | `Books/rituals.docx`, `Rites of Passage.docx`, `Books/chapter list.docx` | 🔴 gap |

### 3. Companion — `companion/` (the app's brain)

**Was the richest seam and the emptiest lane; the brain is now curated in.** The
load-bearing companion docs are filed; the voice/narrative tail remains.

| Object | In repo | Quarry source | Status |
|---|---|---|---|
| Runtime system prompt (+ coin & I AM sections) | `companion/system-prompt.md` | `GAP/GAP_Companion_Phase1_Deploy_Now.docx` + both addenda | ✅ curated |
| Phase-1 deploy guide | `companion/deployment.md` | `GAP/GAP_Companion_Phase1_Deploy_Now.docx` | ✅ curated |
| AI conduct constitution | `companion/ai-conduct.md` | `GAP/GAP_AI_Governance_Codex.docx` Part I | ✅ curated |
| Living Coin map / symbolism | `companion/reference/living-coin.md` | `GAP/GAP_Companion_Architecture.docx` + addenda | ✅ curated |
| Layer-4 vision (intelligence/finance/tools) | `companion/reference/layer4-intelligence.md` | Codex Parts II–IV + 3 `REFERENCE_GAP_Layer4_*.docx` | ✅ curated as **deferred** |
| `GAP_System_Prompt.docx` | `tools/` (belongs there) | `GAP/GAP_System_Prompt.docx` | 🔴 misfiled name — it's the **book-rewriting** prompt, an authoring tool, not the companion brain |
| Voice-reference exemplars | — | `GAP/Voice_Reference_The_Extension_Cord.docx`, `..._The_Hill_With_The_Ashes.docx`, `GAP/Seek_Ye_First_Master.docx` | 🔴 gap (voice corpus for authoring + guide) |
| Narrative / calling pieces | — | `GAP/{I was lost, II want to walk with you, Im tired, From breaking point to purpose, So here to fore, What do you serve, Whats your story, The Founding Call, The general Calling}.docx` | 🔴 gap (companion openings / entry scripts) |
| Forge user-journey (v1–v3+updated) | reconcile → `system/user-journey.md` | `GAP/The_Forge_Master_User_Journey_v3_Updated.docx` | 🟡 reconcile |

### 4. Operations & instruments — `operations/` + a new tools lane

Repo has the operations doctrine (intake, pairing, ledger) but **no ledger and no
instruments filed.** The quarry holds the actual worksheets a man fills in.

| Object | Quarry source | Destination | Status |
|---|---|---|---|
| The ledger | — | `operations/` (spreadsheet, HANDOFF #5) | 🔴 gap — not created |
| Self-assessment | `Books/GAP Self Assessment.xlsx` | instruments | 🔴 gap |
| Allostatic Audit | `GAP/The Allostatic Audit Worksheet.docx` / `.pdf` | instruments | 🔴 gap |
| "Where I want to be" | `Books/Old versions/Where I want to be *.xlsx` | instruments | 🔴 gap |
| Gratitude journal, Community map | `Books/Gratitude Journal.docx`, `Books/Getting to Know Your Community.docx` | instruments | 🔴 gap |
| 90-Minute Mission / Mission Blueprint | `90 minute mission/*` (workbook, PDFs, Lulu print template) | instrument / product | 🔴 gap |
| 3-Day Reset | `Books/3 day/*` (book, workbook, challenge) | instrument / product | 🔴 gap |
| Modular Meal System | `Books/Nutritian/*` | instrument / product (peripheral) | 📦 likely archive |

### 5. Governance & legal — new lane (no home in repo yet)

A collaborator and any nonprofit/chapter work will need these. There is no
`governance/` folder yet.

| Object | Quarry source | Status |
|---|---|---|
| Creed | `Creed.docx` (canonical creed already in `README.md`) | 🟡 text is in README; source doc not filed |
| Constitution & bylaws | `CONSTITUTION AND BYLAWS OF GAMMA ALPHA PI FRATERNITY.docx`, `Research/constitution-and-bylaws.pdf`, `GAP/GAP_Institutional_Constitution.docx`, `GAP/GAP_Institutional_Bylaws.docx` | 🔴 gap (multiple versions — reconcile) |
| Chapter bylaws template | `Research/Chapter-Bylaws-Template.pdf` | 🔴 gap |
| Org structure | `org/CORE ORGANIZATIONAL STRUCTURE.docx`, `org/ORGANIZATIONAL STRUCTURE.docx` | 🔴 gap |
| Nonprofit path | `Marketing/Making Gamma Alpha Pi a nonprofit.docx` | 🔴 gap |

### 6. Website & go-to-market — new lane (no home in repo yet)

Directly serves **Step 4 (public launch threshold)** and **Step 5 (scale)**. The
storefront is already live; the *spec* and *funnel* thinking lives in the quarry.

| Object | Quarry source | Status |
|---|---|---|
| Live public surfaces | site + YouTube + TikTok + Facebook + Discord — registered in `website/channels.md` | ✅ live; ✅ registered; copy/content audit pending |
| Site rebuild spec | `GAP/GAP_Website_Rebuild_Instructions.docx`, `website and app.docx` | 🔴 gap |
| Program of work / WBS | `WBS for creating a global fraternity.docx`, `Research/How to Start a Fraternity.docx` | 🔴 gap |
| Marketing engine | `Marketing/*` (~40 docs: funnels, 100 hooks, archetypes, pricing, objections, founder's story, acquisition roadmap, hero's journey) | 📦 mostly archive; mine specific pieces for launch copy |
| Meetings / strategy | `meetings/{Avatar and marketing strategy, Meeting Structure}.docx` | 🔴 gap |
| Presentations | `Presentations/*.pptx` (5: Intro, Brotherhood, Love, Strength, Vision) | 📦 archive; source for site/deck copy |

### 7. Brand & design assets — decide: `brand/` vs archive

Text-canonical repo, but a collaborator building the site needs the logo and marks.
Worth pulling the **vector source + brand guide** into a small `brand/` lane; leave
the thousands of renders/photos in the quarry.

| Object | Quarry source | Recommendation |
|---|---|---|
| Logo (vector + kit) | `Coin/Fiverr Premium Kit/` (SVG, PNG, favicon, social kit, brand guide PDF) | 🔴 pull SVG + guide into `brand/` |
| Coin renders / 3D | `Coin/` (renders, `Coin rev 3 3d.glb`, spin videos, proofs) | 📦 archive; link the canonical render |
| Symbols & meanings | `Coin/Symbol explinations.xlsx`, `Coin/Symbol explanations`, `Research/Symbols.docx`, `Research/The Torch as a Symbol.docx` | 🔴 gap (symbol canon — belongs with corpus/companion) |
| Video / ambience / quotes | `Videos/` (~2,000 mp4), campfire footage, `quotes/` | 📦 archive (production assets) |

### 8. AI tooling & prompts — `tools/`

| Object | Quarry source | Status |
|---|---|---|
| docx → md converter | `tools/docx_to_md.py` | ✅ in repo |
| Authoring / chapter prompts | `MASTER CHAPTER Prompt BOTF.docx`, `Prompts.docx`, `Prompts 7 short video.docx`, `GAP/Book_of_the_Coin_Revoicing_Directions.docx` | 🔴 gap (curate the reusable ones into `tools/` or `companion/`) |

### 9. Source scholarship — 📦 archive/reference

`Research/` (Delphic maxims, Phi, civilizations, empire table, verses, names of man,
values & principles, top-10 commonalities, torch symbolism, etc.) and `ideation/`
(How to Sell/Market Like Jesus, The Measure of a Man, Beauty and the Beast). This is
the reading behind the corpus — mine a citation when a book needs it; do not import
wholesale.

---

## What Step 2 inherits from this map

The gap picture in one glance:

- **Corpus:** 3 of 6 books to voice; **Father + Nosce** to finish; **Big Brother** to write. (Known; HANDOFF #1–2.)
- **Companion:** whole brain drafted in `GAP/`, **zero curated into `companion/`.** Biggest single lift, highest leverage for a lean launch.
- **Operations:** doctrine exists, **ledger + instruments don't.** Cheapest lift, and it's what proves the loop.
- **Governance, Website-spec, Brand, Symbol-canon:** **four lanes with no home in the repo.** Collaboration-blocking — a coding partner can't act on what isn't filed.
- **Web chats:** unknown volume, **only source that needs your manual export.**

Decisions settled (2026-09-01):

1. **New lanes — scaffolded.** `governance/`, `website/`, `brand/`, and
   `operations/instruments/` now exist as README-stub lanes, empty by design and
   ready to fill. The framework is set; the material gets filled in on purpose.
2. **Remote — live.** Repo is public at `github.com/kehaughey-cyber/gamma-alpha-pi`;
   the collaborator can already see it. Public means no private data ever curates in.
3. **First curation lane — homeless lanes**, to unblock a collaborator, then the
   **companion brain** (`Fraternity/GAP/` → `companion/`) as the highest-leverage lift.

---

## Intake rule (non-negotiable, from `README.md`)

> `_inbox/` is raw, everything else is curated. Capture messy, file clean. Nothing
> enters `corpus/`, `system/`, `companion/`, or `operations/` except converted to
> Markdown and refined on purpose. The quarry (`Active/Fraternity/`) is never bulk-imported.
