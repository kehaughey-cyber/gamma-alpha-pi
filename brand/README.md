# brand — the visual identity

The marks a man recognizes: the logo, the coin, the color and type that carry the house
across the site, the books, and the coin itself. This repo is text-canonical, so this
lane stays **deliberately small** — the *source* files a collaborator actually needs to
build with, not the thousands of renders and photos. Those stay in the quarry.

## What belongs here (pull the sources; leave the rest in the quarry)
- **Logo, vector** — `Coin/Fiverr Premium Kit/SVG Vector Files/*.svg` (the real source;
  PNGs are exports of it). Pull the SVG(s).
- **Brand guide** — `Coin/Fiverr Premium Kit/` guide PDF, plus favicon and the social kit.
- **Canonical coin render** — link the one true render (and `Coin/The raod/Coin rev 3 3d.glb`
  for the 3D). Do not pull the dozens of proofs and spin videos; link the one that ships.
- **Color & type** — capture the actual hex values and typefaces in a short `brand.md`
  so a collaborator is not eyedropping a PNG.

## What does NOT belong here
- The ~2,000 videos, ambience footage, photo shoots, old proofs (`Coin/`, `Videos/`,
  `quotes/`) — 📦 archive. Production assets, not brand sources.
- **Symbol canon** — the *meanings* of the coin's symbols (`Coin/Symbol explinations.xlsx`,
  `Research/The Torch as a Symbol.docx`) are corpus/companion content, not a brand asset.
  They belong with the Book of the Coin and the companion's coin-symbolism addendum;
  cross-reference from here, do not duplicate.

## Non-negotiable
Keep this lane a **handful of source files**, not a media library. The test: could a
collaborator build the site and the next coin from only what is in here? If yes, it is
complete; if it is growing past that, the extra belongs in the quarry.
