# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Joel Oranen's personal site, published by GitHub Pages from `main` at https://jtnoranen.github.io/. Plain HTML and CSS with no build step, framework or JavaScript; GitHub Pages' Jekyll copies the files as they are. Anything that is not part of the site (notes, scripts) must be listed under `exclude` in `_config.yml`, or it gets published.

The main page is in English, written in the first person for data engineering recruiters and collaborators. Its sections are Now (current work, projects and an experience list, `#now` and `#experience`), Next (`#next`, what Joel is learning or building), Someday (`#someday`, futures-studies questions) and Contact (`#contact`). The CVs stay bilingual (`cv_English.pdf`, `cv_Suomi.pdf`).

## Commands

```
python -m http.server 8000          # preview at http://localhost:8000
python tools/build_cv_pdfs.py       # regenerate cv_Suomi.pdf and cv_English.pdf
```

`build_cv_pdfs.py` needs `python -m pip install playwright` and `python -m playwright install chromium`. Validate HTML with the W3C checker, which should return nothing:

```
curl -s -H "Content-Type: text/html; charset=utf-8" --data-binary @index.html "https://validator.w3.org/nu/?out=gnu"
```

## Content lives in three places

Work history, education and projects appear in `index.html` (project cards and `#experience` in `#now`, the current job also in the hero and the `#now` intro), `cv/cv-fi.html` and `cv/cv-en.html`. A content change usually touches all three, followed by a PDF rebuild. Each CV must stay on one A4 page: check the page count of the generated PDFs (for example with pypdf) and tighten the text if a second page appears.

The CVs list only email, LinkedIn, GitHub and the site. Do not add a phone number, home address or birth date; the old Canva CV that used to be published here exposed them.

`cv.html` and `portfolio.html` are meta-refresh redirects to `index.html#experience` and `#now`, kept so that old links keep working. The navigation links in `index.html` must match the section ids.

## Styling

- All colours are custom properties on `:root` in `style.css`. The page is light only (warm paper `#F6F2EA`, ink `#1E2A3A`); the Someday band is the one dark surface. Amber `#C8822E` is for graphics (lines, dots, outlines) and `#8A500E` for accent text, which passes WCAG AA on paper, cards and the Next band.
- Three Google Fonts, loaded in `index.html`'s `<head>`: Fraunces (headings), Inter (body text, small uppercase labels, tags, dates and the diagram) and Caveat (the handwritten notes only). Do not add a fourth; a monospace font was tried and removed as too busy.
- Handwriting is used in exactly three places: the "Hey, I'm Joel" greeting, the "the one people ACTUALLY care about" note in the pipeline diagram and the "Get a cup of coffee maybe?" note next to "Let's talk data." Do not add more unless Joel asks.
- The hero diagram is an inline SVG of Joel as a pipeline (learning, doing, iterating, coffee → me → pipelines, dashboards, decisions). It is animated with CSS only (`.flow`, `.light`, `.cursor`), and every animation sits inside `@media (prefers-reduced-motion: no-preference)`.
- Layouts are flex rows with `flex-wrap` and flex-basis in rem, so everything stacks on phones without breakpoints. Check that the page has no horizontal scroll at 390 px.
- `cv/cv.css` is separate from `style.css`. It is light-only and sized in mm for A4 printing.

## Images

The images in `img/` were made from the original photo `img/joel-oranen.jpg` with Pillow, and the repo has no image pipeline:
- 640 px wide JPEG and WebP versions (used by the old full-width hero; not referenced by the current page)
- `og-image.jpg` (1200×630), referenced by absolute URL in the Open Graph tags
- `joel-oranen-cv.jpg`, a square crop used by the CVs

`favicon.svg` and `apple-touch-icon.png` draw the same "Jo" monogram.

The hero avatar is a "live photo": `img/joel-live.mp4`, a 320×320, 5.4 s, muted H.264 loop of Joel waving (about 75 KB), made with ffmpeg from a webcam clip: seconds 1.0–6.45 of the clip, a 720×720 crop at x=160 (the full frame height, set left of the face so the waving hand stays inside the circle), a slight warm grade, and the last 0.4 s cross-faded with the 0.4 s just before the start so the loop has no jump. `img/joel-live-poster.jpg` is its first frame (shown while it loads) and `img/joel-live-still.jpg` a smiling frame shown instead of the video when the visitor prefers reduced motion. Autoplay needs `muted` and `playsinline`; the accessible name sits on the wrapping `span role="img"`, and the video and still are hidden from assistive tech.
