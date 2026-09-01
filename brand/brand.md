# Brand spec

The concrete visual identity: the marks, the colors, the coin. Enough for a collaborator
to build the site and the next print piece without eyedropping a PNG. Sources live in
`assets/`; the heavy production library stays in the quarry (`Fraternity/Coin/`).

## Colors

| Role | Hex | Notes |
|---|---|---|
| Ink / black | `#000000` | Primary logo color; text. |
| GAP blue | `#4A73E8` | The one accent. Cornflower/royal blue. It is the blue of the coin's segment ring. |
| Paper / white | `#FFFFFF` | Ground for the primary logo. |

The flat logo is a two-color mark (black + GAP blue on white). The **physical coin** is
antique gold relief with the GAP blue picking out the segment ring; gold is a material, not
a brand ink, so the palette above is the digital standard and gold appears only as the coin.

## Logo files (`assets/`)

- `logo-primary.svg` — black + GAP blue on white. Default.
- `logo-transparent.svg` — same mark, transparent background (for placing on color).
- `logo-grayscale.svg` — single-color/greyscale version (one-color print, watermarks).
- `favicon.ico` — transparent favicon for the site.

All are vector (paths). The mark is the torch/chalice-and-hourglass with ΓΑΠ, the same
device at the center of the coin's triangle.

## The coin

- `assets/coin-front.png` — the canonical front render (rev3): the gold coin, the triangle
  of **Strength / Vision / Love**, the ΓΑΠ hourglass and torch, the compass rose (cardinal
  points plus the symbolic directions), the seasons, and the blue segment ring. This ring is
  the "Living Coin" the companion and corpus reference (`companion/reference/living-coin.md`):
  fifty segments, forty-five visible, five obscured by the triangle and compass points.
- **3D source:** `Fraternity/Coin/The raod/Coin rev 3 3d.glb` (~10.5 MB). Left in the quarry
  by design to keep this lane light; pull it into `assets/` only if a collaborator is
  actually working the 3D model. The coin back and alternate renders are also in the quarry.

## Type

The wordmark in the logo SVGs is **outlined to paths**, so no typeface name is embedded and
none is recoverable from the files. **Open item:** confirm the display and body typefaces
GAP uses (and get the actual font files) before setting site or print type; until then the
logo stands on its own and body copy has no canonical face. Note the coin sets its wordmark
in Greek majuscule (ΓΑΠ) — decorative, not a text face.

## What stays in the quarry (not brand sources)

The Fiverr kit's generic guides ("Get the most out of your logo guide", "The roadmap to a
strong business") are the seller's boilerplate, not a GAP brand book. The social-media kit
(Etsy/Facebook/Instagram/etc. banners), the `.psd`/`.indd` working files, and the hundreds
of coin photos and spin videos are production assets. Mine a specific file when a specific
need calls for it; do not bulk-import.
