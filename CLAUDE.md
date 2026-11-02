# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Joel Oranen's personal site, published by GitHub Pages from `main` at https://jtnoranen.github.io/. Plain HTML and CSS with no build step or framework, and one small inline script; GitHub Pages' Jekyll copies the files as they are. Anything that is not part of the site (notes, scripts) must be listed under `exclude` in `_config.yml`, or it gets published.

Site copy is English (`lang="en"`), written in the first person for data engineering recruiters; the CVs come in Finnish and English. Class names and CSS comments are Finnish, BEM-style (`.paneeli__sisus`, `.linkit--hiljainen`).

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

Work history, education and projects appear in `index.html` (`#projects` and `#experience`; `#cv` only links the two PDFs), `cv/cv-fi.html` and `cv/cv-en.html`. The site is deliberately shorter than the CVs: some projects (betting odds, companion planting, Crown Bridges, bachelor's thesis) appear only in the CVs. A content change usually touches all three, followed by a PDF rebuild. Each CV must stay on one A4 page: check the page count of the generated PDFs (for example with pypdf) and tighten the text if a second page appears.

The CVs list only email, LinkedIn, GitHub and the site. Do not add a phone number, home address or birth date; the old Canva CV that used to be published here exposed them.

`cv.html` and `portfolio.html` are meta-refresh redirects to `index.html#experience` and `#projects`, kept so that old links keep working. The CVs link to `#projects`. The navigation links in `index.html` must match the section ids.

## Styling

- All colours come from custom properties on `:root` in `style.css`, and the dark palette is a full override in `@media (prefers-color-scheme: dark)`. A new colour needs a value in both. The teal accent (`--korostus`, `#2c7873` light and `#6cc1ba` dark) is the only accent colour, and the palette was checked for WCAG AA contrast.
- Inter is the typeface of `index.html`, loaded from Google Fonts in its `<head>`. The CVs still use Space Grotesk.
- The look follows https://1chooo.com/: small grey text in one column of at most `42rem`, headings the same size as body text, and plain underlined links.
- The page is a row of full-screen panels (`#home`, `#projects`, `#experience`, `#cv`) in `.paneelit`, a horizontal scroll-snap container. Anchor links scroll the row sideways, and each panel scrolls vertically on its own, so `body` never scrolls. The inline script at the end of `index.html` maps a vertical mouse wheel to panel changes (only when the current panel has no room left to scroll, and at most once per wheel gesture) and adds left/right arrow keys. The page must keep working without it: links and swiping need no JavaScript. Every panel except `#home` starts with the same section links (`.ylapalkki`: "me", "projects", "experience", "cv", lower case on purpose), a row at the top on narrow screens and a column centred vertically in the left margin from `64rem` up. The current panel's link has `aria-current` and is bold.
- The aim is that a panel fits the screen without scrolling. The content panels keep their `h2` for screen readers but hide it (`.piilotettu`). On `#experience` each job and degree is a `<details>` whose summary is the title line, and only the current job is open; "Other work" and "Character-building work" open as whole lists. Spacing tightens on short or narrow screens.
- `#home` holds only the name, the waving video and the links. The video is a small (`17rem`, 4:3) muted loop (`img/joel-vilkuttaa.webm`/`.mp4`, poster `.jpg`) seen through a rounded torn hole in the page. An inline SVG (viewBox `0 0 120 90`) over it draws, bottom to top, a shadow, the torn fibre edge (inner hole) and the paper in the page background colour (slightly larger outer hole), both cut out with even-odd fills. The two hole paths were generated with a seeded Python script (harmonic wobble, random jag and a few cracks) and are roughened with `feTurbulence`/`feDisplacementMap`. The filters use `color-interpolation-filters="sRGB"`; without it the paper's colour shifts in dark mode and a box shows around the video. With `prefers-reduced-motion: reduce` the CSS hides the video and shows the poster as an image instead.
- `cv/cv.css` is separate from `style.css`. It is light-only and sized in mm for A4 printing.

Design decisions to keep:
- Sentence case everywhere, with no all-caps labels. The exception is the lower-case section links.
- `#home` is finished; Joel does not want it changed.
- No `A · B · C` meta strings; write lists of tools as a sentence, for example "Tekniikat: Python ja Streamlit."
- No arrows appended to links.
- No cards, shadows or entrance animations.
- No buttons or hero; actions are plain links laid out in a row.

## Images

The images in `img/` were made from the original photo `img/joel-oranen.jpg` with Pillow, and the repo has no image pipeline:
- 640 px wide JPEG and WebP versions (no longer used on the page)
- `og-image.jpg` (1200×630), referenced by absolute URL in the Open Graph tags
- `joel-oranen-cv.jpg`, a square crop used by the CVs

`joel-vilkuttaa.*` was cut from a 1280×720 webcam clip with ffmpeg (`pip install imageio-ffmpeg`): source 1.2–7.4 s whose last second cross-fades into 0.2–1.2 s, so the loop only plays forward and has no visible jump (playing it in reverse looked uncanny), a 960×720 crop at x=60 scaled to 480×360 at 20 fps, without audio, H.264 and VP9. The poster is the frame at 3.8 s.

`favicon.svg` and `apple-touch-icon.png` draw the same "Jo" monogram.
