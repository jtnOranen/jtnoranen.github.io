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
- Four Google Fonts, loaded in `index.html`'s `<head>`: Fraunces (headings), Inter (body), JetBrains Mono (small uppercase labels, tags, dates) and Caveat (handwriting).
- Handwriting is used in exactly two places: the "Hey, I'm Joel" greeting and the "the one people ACTUALLY care about" note in the pipeline diagram. Do not add more.
- The hero diagram is an inline SVG of Joel as a pipeline (learning, doing, iterating, coffee → me → pipelines, dashboards, decisions). It is animated with CSS only (`.flow`, `.light`, `.cursor`), and every animation sits inside `@media (prefers-reduced-motion: no-preference)`.
- Layouts are flex rows with `flex-wrap` and flex-basis in rem, so everything stacks on phones without breakpoints. Check that the page has no horizontal scroll at 390 px.
- `cv/cv.css` is separate from `style.css`. It is light-only and sized in mm for A4 printing.

## Images

The images in `img/` were made from the original photo `img/joel-oranen.jpg` with Pillow, and the repo has no image pipeline:
- 640 px wide JPEG and WebP versions (used by the old full-width hero; not referenced by the current page)
- `og-image.jpg` (1200×630), referenced by absolute URL in the Open Graph tags
- `joel-oranen-cv.jpg`, a square crop used by the CVs and the hero avatar

`favicon.svg` and `apple-touch-icon.png` draw the same "Jo" monogram. The hero avatar reuses `joel-oranen-cv.jpg`; a short muted looping video ("live photo") is planned to replace it, with the still image kept as the poster and reduced-motion fallback.
