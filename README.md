# Palette Algorithm

A single-file, zero-dependency color-palette tool. Drop in one hex; the page returns a coherent primary + accents + status colors + neutral "paper" surfaces, plus a 100–900 ramp per color and a WCAG accessibility check.

Everything runs in the browser — no build step, no backend. `index.html` is the whole app.

---

## Try it

Open `index.html` in any modern browser, or host the file on GitHub Pages / Netlify / Vercel / any static host.

```bash
# Local preview
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Features

- **Four generation methods** — switch between OKLCH-Scored (weighted scorer with sliders), HSL Math (classic schemes), Material Library (curated premium colors), and Hybrid (HSL with material safety net).
- **Tag your project** — pick topic + feel tags (corporate, playful, vintage, etc.) and the tool retunes the candidate pool and method options to match.
- **Color grades** — toggle a Tailwind-style 100–900 ramp under every swatch. In Line view, grades stack vertically per color column at readable size.
- **Paper neutrals** — seven swatches tinted toward the primary hue (Bg, Surface, Layout, Border, Muted, Body, Heading). Tune the tint strength, hue offset, bg lightness, and text darkness with sliders.
- **Compatibility breakdown** — every color pair scored on Hue / Chroma / Lightness / Accessibility / Modernity, plus a paper-readability section showing contrast against page surfaces.
- **WCAG minimum** — toggle A / AA / AAA. The selected level filters the color generator so picked accents and statuses meet the threshold against the primary; out-of-reach colors get a red `!` overlay.
- **Locks** — pin any swatch by clicking the lock icon. Locked colors survive "Try another" and keep their name stable across regenerations.
- **Two views** — Grid (each color in its own card) or Line (palette + status in one continuous row).
- **Exports** — PNG, PDF, CSS variables, Tailwind config, JSON, plain text.
- **Share links** — every interaction encodes the state into the URL hash. Reloading the page intentionally starts with a fresh random color; clicking a shared link still restores the encoded state.

## Hosting on GitHub Pages

1. Create a new repository.
2. Drop these files in.
3. Settings → Pages → set the source to `main` branch, root folder.
4. Your tool will be live at `https://<username>.github.io/<repo>/` within a minute.

## Tech notes

- OKLCH color math is computed directly from sRGB hex; no external color libraries.
- WCAG 2.1 relative-luminance contrast for accessibility checks.
- View prefs (grid/line, grades on/off, WCAG min) persist in `localStorage`.
- ~250 KB total, single file — no fonts, no third-party scripts.

## License

MIT — see `LICENSE`.
