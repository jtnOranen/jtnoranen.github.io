# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Joel Oranen's personal site, published by GitHub Pages from `main` at https://jtnoranen.github.io/. Plain HTML and CSS with no build step, framework or JavaScript; GitHub Pages' Jekyll copies the files as they are. Anything that is not part of the site (notes, scripts) must be listed under `exclude` in `_config.yml`, or it gets published.

Site copy is Finnish, written in the first person for data engineering recruiters. The only English on the main page is the `#in-english` section (`lang="en"`). Class names are Finnish, BEM-style (`.ylapalkki__nimi`, `.nappi--ensisijainen`).

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

Work history, education and projects appear in `index.html` (`#projektit`, `#kokemus`, and the current job in `#mina` and `#in-english`), `cv/cv-fi.html` and `cv/cv-en.html`. A content change usually touches all three, followed by a PDF rebuild. Each CV must stay on one A4 page: check the page count of the generated PDFs (for example with pypdf) and tighten the text if a second page appears.

The CVs list only email, LinkedIn, GitHub and the site. Do not add a phone number, home address or birth date; the old Canva CV that used to be published here exposed them.

`cv.html` and `portfolio.html` are meta-refresh redirects to `index.html#kokemus` and `#projektit`, kept so that old links keep working. The navigation links in `index.html` must match the section ids.

## Styling

- All colours come from custom properties on `:root` in `style.css`, and the dark palette is a full override in `@media (prefers-color-scheme: dark)`. A new colour needs a value in both. The teal accent (`--korostus`, `#2c7873` light and `#6cc1ba` dark) is the only accent colour, and the palette was checked for WCAG AA contrast.
- Space Grotesk is the only typeface, loaded from Google Fonts in each page's `<head>`.
- The hero has two layouts. Below `56rem` the photo and the text are stacked. From `56rem` up they share one grid cell, with the text over a dark gradient on the left side of the photo. The grid row must stay `minmax(0, 1fr)`, or the row grows to the image's natural height and pushes the text down.
- The only photo is 1260×840 and no larger version exists. The hero is therefore capped at `100rem` and anchored to the top (`object-position: 65% 0%`) because the head is close to the top edge.
- `cv/cv.css` is separate from `style.css`. It is light-only and sized in mm for A4 printing.

Design decisions to keep:
- Sentence case everywhere, with no all-caps labels.
- No `A · B · C` meta strings; write lists of tools as a sentence, for example "Tekniikat: Python ja Streamlit."
- No arrows appended to links.
- No cards, shadows or entrance animations.
- The dashed line at the top of the work timeline (`.aikajana--jatkuu`) and the filled dot (`li.nyt`) mark the current job.

## Images

The images in `img/` were made from the original photo `img/joel-oranen.jpg` with Pillow, and the repo has no image pipeline:
- 640 px wide JPEG and WebP versions for the hero's `srcset`
- `og-image.jpg` (1200×630), referenced by absolute URL in the Open Graph tags
- `joel-oranen-cv.jpg`, a square crop used by the CVs

`favicon.svg` and `apple-touch-icon.png` draw the same "Jo" monogram.
