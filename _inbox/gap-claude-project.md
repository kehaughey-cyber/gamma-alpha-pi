# Raw capture: the claude.ai "GAP" project (unmigrated production)

Captured 2026-09-03 from Kevin's claude.ai **GAP** project
(`claude.ai/project/019e2d2a-2da9-70c8-b955-08ec20c27759`). This is the "quite a bit
produced that never got migrated." Raw, per `_inbox` doctrine — mine into the right
lanes on purpose. The single richest piece is the **project Memory** (below), which is a
current, synthesized state document.

## Cloud-only artifacts (NOT on disk, not in repo — pull these)

These exist only in the claude.ai project's knowledge; they are not in the `Fraternity`
quarry:

- **`GAP_Project_Record.docx`** (21.8 kB) — the project's own production record. "Stored as
  a plain markdown-formatted text file with a .docx extension; read as plain text, edit the
  working copy, then build a Word doc via a Node.js script (`build_doc.js`)." **Download and
  curate — likely the best single map of what has been produced.**
- **`transmission-forge.skill`** + **`verifiers.md`** — functional skill files for the
  transmission-theory framework (five-stage generation with adversarial self-gating,
  selfish-teller deformation test, domain-truth verifier). Real, working IP. → `tools/` or a
  `skills/` lane when pulled.

Everything else in the project's knowledge (Book of the Coin, Brother, Forge journeys
v1–v3, Institutional docs, Layer-4 refs, companion addenda, Seek Ye First, 3-Day Reset,
Father, NTI, Rites of Passage, voice references) is already in the quarry and mostly
curated. Note the project holds **Book of the Brother Rev 1** and **Book of the Coin Rev 1**
(the newer revoiced versions) — reconcile against the repo's corpus (see the corpus-state
flag in the WBS).

## The chats (production that lives only as conversations)

Titles only — each may hold drafts/decisions worth mining:
Failure as a tool for narrowing possibility · Parallel product examples and offerings (×3) ·
Self-improvement workbook resources · Men's purpose and discipline workbook · Book of the
Brother part 1 rewrite finished · Adapting to the Book of the Brother rewrite · Adding 1
Corinthians 16:13-14 to book · Christ and Moses as life archetypes · Book of the brother
re-write considerations · Book of the brother revision · Giving a coin and finding purpose ·
Reading time for book series · GAP 5-2026 · Designing a fraternal handshake with symbolic
meaning · Understanding the coin's symbology · Spiral growth and the Phi logo · Building an
AI companion · (+ more under "Show more"). Sidebar also lists: Building a system for lifetime
agency · Field manual portion of the book · AI as human augmentation not replacement ·
Creating digital products by finding [needs] · Personal insight journal instructions ·
Optimizing systems instead of abandoning · SPINE proof evaluation.

## New items surfaced here that the repo does not have yet

- **Transmission theory** — a formal model of how ideas/stories propagate across generations;
  three laws: **propulsion** (double emotional payment, to teller and receiver, on the spot),
  **the weld** (cargo fused into events so a selfish teller cannot strip it without breaking
  the story), **seating** (cargo lodged in universal human material, not local context that
  sheds in transit). Myths = the partial-failure specimen (fly on propulsion, arrive empty).
- **The Threshold Reading** — a curated ~30–40 page pre-mine reading list drawn from the Book
  of the Coin and Book of the Brother; the intended entry point before the full corpus.
  (Directly an MVP entry artifact.)
- **Three foundational questions** — What do you serve? Who are you? What do you want?
- **Book of the King** (planned) — where the "full GAP north star statement" is placed.
- **Production roadmap** — audiobook via ElevenLabs with Kevin's cloned voice (Brother last
  due to size); video series (each Threshold "why this" doubles as a directorial brief).
- **Etsy competitive analysis** — men's-dev PDF workbooks are the commodity end; only the
  3-Day Reset and Field Manual excerpts productize to that format without breaking the
  sequenced-revelation architecture.

## Hard rules stated here the repo should adopt

- **Zero em dashes, zero en dashes** in all GAP content.
- **ESV scripture only**, verbatim wording verified.
- GAP_Project_Record workflow: markdown source → `build_doc.js` → .docx.

## Corpus-state discrepancy to resolve (flagged in the WBS)

The Memory (updated ~2026-09-01) says the revoicing state is: **Book of the Coin Rev 1
complete** (voice benchmark); **Book of the Brother Part 1 (Philosophy) complete** (~66,700
words, mechanical audit passed); **Field Manual is NEXT (not yet written)**; then NTI,
Father, King. The repo's `CLAUDE.md`/`HANDOFF.md` claim the **Field Manual is already
rewritten**. These conflict — the cloud Memory is more recent. Reconcile before trusting the
repo's corpus status.

---

## The project Memory, verbatim

> **Purpose & context.** Kevin Haughey is the founder and architect of Gamma Alpha Pi (GAP),
> a Christian men's fraternal brotherhood organization built around purpose discovery,
> servant leadership, and intergenerational mentorship. GAP's philosophical core is fractal —
> the same failure and growth mechanisms operate at the individual, family, community, and
> civilizational level — and its three foundational questions are: What do you serve? Who are
> you? What do you want? The organization is structured around a life-stage progression (Son,
> Brother, Husband, Father, King, Elder), an initiatory brotherhood model with earned trust as
> the gatekeeping mechanism, and a physical coin artifact carrying layered theological and
> cosmological symbolism. GAP's growth model is a spiral, not a linear ascent — men revisit
> core territory (identity, purpose, fear, relationships) at progressively higher levels. Phi
> (the golden ratio) serves as GAP's logo, encoding this pattern mathematically. Kevin carries
> approximately thirty years of experience walking men through personal transformation, which
> forms the empirical foundation of the framework. He describes GAP as a calling rather than a
> project, grounded explicitly in Christ's model of servant leadership. The framework does not
> announce itself — men are meant to arrive at its full architecture through the process, not
> by direct delivery.
>
> **Current state.** The primary active work is the Revoicing Project: rewriting GAP's
> multi-volume book series in a unified "Big Brother" voice — grounded, earned authority,
> elevation rather than rescue — modeled on the narrator register established in the completed
> Book of the Coin (Rev 1). The book corpus: Book of the Coin (Rev 1 — complete, voice
> benchmark); Book of the Brother, Part 1: Philosophy (Rev 1 rewrite complete at ~66,700
> words; mechanical audit passed; flagged: a heading markup artifact, the Epic of Gilgamesh
> pending inclusion, a 1 Corinthians 16:13-14 epigraph placement question, a Carl Sandburg
> quote requiring copyright clearance before audiobook/print); Book of the Brother: Field
> Manual (next in sequence); Nosce Te Ipsum; Book of the Father; Book of the King (planned).
> Sequencing decision: complete the Field Manual first, then assess whether a Philosophy
> volume rebalance (v1.1) is needed, then edit all volumes together as a set before
> formatting. Demote-candidate mechanics from Philosophy seed corresponding Field Manual
> sections; monitor duplication. A transmission theory framework was developed (three laws:
> propulsion, the weld, seating); a functional `transmission-forge.skill` and `verifiers.md`
> were built (selfish-teller deformation test, domain-truth verifier). Kevin assessed AI
> output here as ~80% requiring human polish; the skill makes that seam explicit. GAP's
> institutional and governance architecture is documented (three-entity legal structure,
> nine-member Leadership Council with Founder advisory seat, AI Governance Codex). The Living
> Coin maps forty-five visible segments to the NTI self-assessment across three tenets, with
> five segments intentionally obscured (no man fully completes his work).
>
> **On the horizon.** Drafting the Field Manual (immediate next volume); audiobook production
> via ElevenLabs using Kevin's cloned voice (Brother last due to size); video series (each
> Threshold "why this" doubles as directorial brief); the Threshold Reading (~30–40 page
> pre-mine reading list) as the entry point before the full corpus; the Book of the King
> (planned) carrying the full GAP north star statement; Etsy competitive analysis logged
> (only the 3-Day Reset and Field Manual excerpts productize to instant-download format
> without violating sequenced revelation).
>
> **Key learnings & principles.** Every stage must prepare the man for the next; the
> transition involves genuine loss and grief that must not be bypassed — the tunnel is a real
> death, and men are lost at transitions for lack of a map/guide/framework to distinguish
> metaphorical from physical death. GAP is a metaskill, not a container — owned, carried,
> unable to be taken away. The brother ahead is guide and proof; the brother behind creates
> the teaching pressure that forces full synthesis (you do not own something until you can
> give it away). You cannot pour a gallon into a cup — the full architecture cannot be
> delivered at the door; truth must be architected for the audience's receivability at each
> stage. Transmission: emotional exchange is the engine at the human level, structural depth
> the engine of durability; the rare object satisfying both under tension flies and stays
> loaded. Selfish-teller test is the primary quality gate. AI can be fluent in vocabulary
> without reliable assembly knowledge (domain-truth verifier catches this). Productizing
> deeper layers to instant-download would flatten sequenced revelation. The coin's three
> back-face elements are distinct and must never be conflated: words for "man" across
> civilizations; the open right hand (honesty, integrity, transparency, help); the scriptural
> frame (Isaiah 41:10, Ezekiel 22:30, Isaiah 6:8).
>
> **Approach & patterns.** Systems thinking before execution; frameworks understood
> completely before build; thinks in vectors and root causality. Stop theoretical exploration
> at diminishing returns; redirect to architecture and build. Direct, economical
> communication; Kevin corrects verbosity and abstraction without payoff. Modular,
> purpose-specific documents over combined files. Collaborative line-by-line refinement, not
> wholesale rewrites. Kevin uses Claude as a muse that catalyzes connections to ideas already
> present — not co-creator or authority ("do not praise the hammer for the work of the
> carpenter"). GAP does not announce itself. Sycophantic output slows the work.
>
> **Tools & standards.** ElevenLabs (voice cloning) for audiobook; claude.ai Projects as the
> primary environment; GAP Project Record stored as markdown-in-.docx, built via `build_doc.js`;
> `transmission-forge.skill` + `verifiers.md`; **ESV translation only**; **zero em dashes,
> zero en dashes**, ESV-only scripture verbatim-verified.
