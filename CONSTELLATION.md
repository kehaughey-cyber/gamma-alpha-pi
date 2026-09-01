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
| Voice-reference exemplars | `system/voice-references/` | `GAP/Voice_Reference_The_Extension_Cord.docx`, `..._The_Hill_With_The_Ashes.docx` | ✅ curated (Kevin cleared publish): the concrete companions to `system/voice.md`. |
| `Seek_Ye_First_Master.docx` | belongs in Website/GTM lane, not companion | `GAP/GAP_Seek_Ye_First_Master.docx` | ↪️ reclassified: it's a **Master Content Document** (sermon + TikTok series + The Calling + The Founding Call + verse reference), finished rescue-voice funnel content. See the Website & GTM lane. |
| Narrative / calling pieces | stays in quarry | `GAP/{I was lost, II want to walk with you, Im tired, From breaking point to purpose, So here to fore, What do you serve, Whats your story, The Founding Call, The general Calling}.docx` | 📦 raw capture per Kevin — stream-of-consciousness brain dumps, possible future video seed. Preserved in quarry, **not imported** (do not reframe as designed scripts). |
| Forge Master User Journey (the "BIOS") | `system/forge-journey.md` | `GAP/The_Forge_Master_User_Journey_v3_Updated.docx` (v3) | ✅ curated in full (Kevin cleared publish): the **phased choreography** (10 phases, ceremonies, the Walk, the Forge) that instantiates the abstract `system/user-journey.md`; a companion layer, not a merge. Open reconciliations noted in the file: 6-stage life arc vs 3-stage in README; new vocabulary (Forge/Mine/Bloom, Wounded Lion / Excuse Maker). |

### 4. Operations & instruments — `operations/` + a new tools lane

Repo has the operations doctrine (intake, pairing, ledger) but **no ledger and no
instruments filed.** The quarry holds the actual worksheets a man fills in.

| Object | Quarry source | Destination | Status |
|---|---|---|---|
| The ledger | 🔴 gap — not created | `operations/` (spreadsheet, HANDOFF #5) | the one remaining operations gap |
| NTI self-assessment (45 aspects) | ✅ `operations/instruments/self-assessment.md` | `Books/GAP Self Assessment.xlsx` (`Where I want to be.xlsx` = older, superseded) | curated; flagship instrument |
| Allostatic Audit | ✅ `operations/instruments/allostatic-audit.md` | `GAP/The Allostatic Audit Worksheet.docx` | curated |
| Community map | ✅ `operations/instruments/community-map.md` | `Books/Getting to Know Your Community.docx` | curated (worksheet only; event/safety/waiver routed out) |
| Gratitude journal | 📦 product (not an instrument) | `Books/Gratitude Journal.docx` (~35k words) | full journal product; don't curate as worksheet |
| 90-Minute Mission, 3-Day Reset | 🔴 product-curricula | `90 minute mission/*`, `Books/3 day/*` | curate with product/website lane (3-Day = entry experience) |
| Modular Meal System | 📦 archive | `Books/Nutritian/*` | peripheral product |
| Liability waiver / event safety plan | 🔴 → operations/governance | bundled in `Books/Getting to Know Your Community.docx` | legal/operational, not a personal instrument |

### 5. Governance & legal — `governance/` (constitution/bylaws reconciled)

The versions were sorted into three generations; the canonical pair is curated in, the
rest classified. Remaining core work is legal, not editorial.

| Object | In repo | Quarry source | Status |
|---|---|---|---|
| Institutional Constitution v1.0 | `governance/constitution.md` | `GAP/GAP_Institutional_Constitution.docx` | ✅ canonical, curated |
| Institutional Bylaws v1.0 | `governance/bylaws.md` | `GAP/GAP_Institutional_Bylaws.docx` | ✅ canonical, curated |
| Creed (+ affirmation form) | `governance/creed.md` | `Creed.docx` + Constitution §1.4 | ✅ curated |
| Legal structure + open questions | `governance/legal-structure.md` | synthesis | ✅ curated; flags 501(c)(10) vs (c)(7), IP-Company ownership / trust layer, naming, filings — for counsel |
| Collegiate "Constitution and Bylaws" (1968/2020) | archive — **not GAP's** | `CONSTITUTION AND BYLAWS OF GAMMA ALPHA PI FRATERNITY.docx` | 📦 a collegiate fraternity's doc (Karnea/Arch Chapter); do not use as ours |
| Org-structure ideation | stays in quarry | `org/{CORE ,}ORGANIZATIONAL STRUCTURE.docx` | 📦 ChatGPT brainstorm transcripts; superseded |
| Chapter formation kit | — | `Research/Chapter-Bylaws-Template.pdf`, `Research/How to Start a Fraternity.docx` | 🔴 gap (curate when live) |
| Nonprofit path | — | `Marketing/Making Gamma Alpha Pi a nonprofit.docx` | 🔴 gap |

### 6. Website & go-to-market — new lane (no home in repo yet)

Directly serves **Step 4 (public launch threshold)** and **Step 5 (scale)**. The
storefront is already live; the *spec* and *funnel* thinking lives in the quarry.

| Object | Quarry source | Status |
|---|---|---|
| Live public surfaces | site + YouTube + TikTok + Facebook + Discord — registered in `website/channels.md` | ✅ live; ✅ registered; copy/content audit pending |
| Site rebuild spec | `GAP/GAP_Website_Rebuild_Instructions.docx`, `website and app.docx` | 🔴 gap |
| Program of work / WBS | `WBS for creating a global fraternity.docx`, `Research/How to Start a Fraternity.docx` | 🔴 gap |
| Flagship content master | `GAP/GAP_Seek_Ye_First_Master.docx` — sermon + TikTok series + The Calling + The Founding Call, one finished rescue-voice piece | 🔴 notable; candidate to curate when the content/copy lane is worked |
| Marketing engine | `Marketing/*` (~40 docs: funnels, 100 hooks, archetypes, pricing, objections, founder's story, acquisition roadmap, hero's journey) | 📦 mostly archive; mine specific pieces for launch copy |
| Meetings / strategy | `meetings/{Avatar and marketing strategy, Meeting Structure}.docx` | 🔴 gap |
| Presentations | `Presentations/*.pptx` (5: Intro, Brotherhood, Love, Strength, Vision) | 📦 archive; source for site/deck copy |

### 7. Brand & design assets — decide: `brand/` vs archive

Text-canonical repo, but a collaborator building the site needs the logo and marks.
Worth pulling the **vector source + brand guide** into a small `brand/` lane; leave
the thousands of renders/photos in the quarry.

| Object | Quarry source | Recommendation |
|---|---|---|
| Logo (vector) | `brand/assets/logo-*.svg`, `brand/assets/favicon.ico` | ✅ pulled from `Coin/Fiverr Premium Kit/`; spec in `brand/brand.md` (colors `#000000` + `#4A73E8`) |
| Coin render | `brand/assets/coin-front.png` | ✅ canonical front render curated; 3D `.glb` (~10.5 MB) left in quarry, linked |
| Coin 3D / alt renders | `Coin/The raod/Coin rev 3 3d.glb`, other renders/spin videos/proofs | 📦 archive; linked from `brand/brand.md` |
| Type / typeface | — | 🔴 open: wordmark outlined in SVG, typeface unconfirmed (flagged in `brand/brand.md`) |
| Symbols & meanings | `Coin/Symbol explinations.xlsx`, `Research/Symbols.docx`, `Research/The Torch as a Symbol.docx` | 🔴 gap (symbol canon — belongs with corpus/companion; cross-ref `companion/reference/living-coin.md`) |
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
