# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Joel Oranen's personal site, published by GitHub Pages from `main` at https://jtnoranen.github.io/. Plain HTML and CSS with no build step or framework, and one inline script; GitHub Pages' Jekyll copies the files as they are. Anything that is not part of the site (notes, scripts) must be listed under `exclude` in `_config.yml`, or it gets published.

Site copy is English (`lang="en"`), written in the first person for data engineering recruiters; the CVs come in Finnish and English. CSS comments are Finnish. The class names of `index.html` are short English ones taken over from the prototype the design came from (`.sharp`, `.ghost`, `.ques`); the CVs use Finnish BEM-style names.

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

Work history, education and projects appear in `index.html` (the Projects and Experience sides), `cv/cv-fi.html` and `cv/cv-en.html`. The site is deliberately shorter than the CVs: some projects (betting odds, companion planting, Crown Bridges, bachelor's thesis) appear only in the CVs. A content change usually touches all three, followed by a PDF rebuild. Each CV must stay on one A4 page: check the page count of the generated PDFs (for example with pypdf) and tighten the text if a second page appears.

The CVs list only email, LinkedIn, GitHub and the site. Do not add a phone number, home address or birth date; the old Canva CV that used to be published here exposed them.

`cv.html` and `portfolio.html` are meta-refresh redirects to `index.html#experience` and `#projects`, kept so that old links keep working. The CVs link to `#projects`. The script also maps the old hashes `#home`, `#me`, `#questions`, `#background` and `#cv` to the right side.

## Styling

The design came from a single-file prototype (Claude design handoff, 2026-11-11) and is kept as it was. Do not redesign; fix things within this design language.

- Light only, "architectonic but light", like a modern art museum. Colours: ink `#1E2026`, soft text `#5E6066`, halo `#F7F8FA`, page a radial gradient `#FFF` to `#EFF1F4`, body `#F3F4F6`. Type: Cormorant Garamond 300 for statements and questions, Jost 400 for small text, both from Google Fonts with `display=swap`.
- The page is one three-sided CSS 3D structure (`.cube`, a triangular prism: sides 120° apart, each set back by `--a`, the inradius `--w` × 0.2887) that rolls left or right: Joel Oranen (statement and bio, centred vertically with `.mid`), Projects (each project as a question), and Experience (work on the left; education with certifications under it on the right; the minor jobs are only in the CVs). A fourth side, Questions (eight open questions, for a while bent over a turning sphere), was removed on 2026-11-20; that version is kept on the branch `kysymykset`. The sides behind show through as fogged glass. Under the tabs, outside the structure, a row of contact links (`.contact`: email, LinkedIn, GitHub, "CV (en)" and "CV (fi)", both with the `download` attribute) shows on every side. Navigation: the tabs below, arrow keys, the mouse wheel (one roll per wheel gesture, after the side has scrolled to its end), drag or swipe (1.5× gain, commits after 14°), shortest-path rolling and hashes `#projects`, `#experience`, `#energy`.
- Opening the energy project turns the structure "through itself" onto a table plane (`rotateX(-78deg)`) with three frosted glass sheets holding charts (`img/energy/*.webp`, crops of the report and health screenshots in the energy-data-platform repo's `docs/images`, 640 px wide); clicking a sheet brings it to the front and zooms it to nearly fill the table (another click, Escape or a click elsewhere puts it back). The sheets are laid out at the full zoom size (616 × 414) and scaled down with `--s`; scaling a small sheet up looked blurry. The table's text sits in its own scrolling column (`.txt`) so it stays inside the structure and off the tabs; on phones `.txt` is `display: contents` and `.inner` scrolls instead. Its facts come from that repo's README: the platform ran on Azure 2026-10-20 to 2026-11-03 and was then torn down. Leave with "Back to projects", Escape, tapping empty space or a swipe.
- A side that does not fit scrolls inside itself (hidden scrollbar); this happens on phones. On Experience each job and degree is a `<details>` and only the current job is open.
- Performance rules, do not undo: never animate `filter: blur` (the blur is a pre-made `.ghost` copy of each side, rebuilt by the script when a `<details>` toggles, and only `opacity` fades); hidden layers use `opacity: .001`, not 0; no `will-change: transform` on big layers; `.scene`, `.sway` and `.cube` have `pointer-events: none` and only the front side's `.sharp` is interactive; `.inner` keeps `touch-action: pan-y`. Timings: roll 1.3 s `cubic-bezier(.3,.7,.2,1)`, turn onto the table 1.9 s `cubic-bezier(.5,0,.15,1)`.
- Inactive sides are `inert`, focus is visible and `prefers-reduced-motion` stops the sway and shortens the transitions. Without JavaScript only the first side shows. Not yet tested on a real iPhone or in Safari.
- The constant sway makes Playwright call elements "not stable"; click with `force=True` in tests.
- `cv/cv.css` is separate from `style.css`. It is light-only and sized in mm for A4 printing. The CVs still use Space Grotesk.

Design decisions to keep:
- Sentence case everywhere, with no all-caps labels.
- Site copy is in the active first person ("I designed …"), but sentences must not all start with "I": open with the context instead ("For KONE's strategy teams, I …", "Alongside client work, I …"). The job texts on Experience are short paragraphs in ink colour, not one soft-grey block.
- No `A · B · C` meta strings; write lists of tools as a sentence, for example "Built with Terraform, Azure, Databricks, dbt and GitHub Actions."
- No arrows appended to links, no numbered markers, no gradient cards, no fade-up on every section, no single accented word in headlines.
- Plain labels such as "Back to projects".
- The first side holds the waving video on a small frosted glass pane (`.pane`, twisted in 3D with `perspective(600px) rotateY(-24deg) rotateX(6deg) rotateZ(-1.5deg)`), small (96 px tall, 66 px on phones) in the lower right corner, positioned absolutely so it never pushes the text. Joel chose it on 2026-11-11 although the handoff said no face. Its ghost copy uses the pre-blurred, soft-edged `img/joel-vilkuttaa-sumu.png` instead of a second video; the video pauses when its side is not in front, and reduced motion shows the poster instead. Rejected ideas: a particle man and a particle 3D head made from his selfie.

## Images

The images in `img/` were made from the original photo `img/joel-oranen.jpg` with Pillow, and the repo has no image pipeline:
- 640 px wide JPEG and WebP versions (no longer used on the page)
- `og-image.jpg` (1200×630), referenced by absolute URL in the Open Graph tags
- `joel-oranen-cv.jpg`, a square crop used by the CVs

`joel-vilkuttaa.*` was cut from a 1280×720 webcam clip with ffmpeg (`pip install imageio-ffmpeg`): source 1.2–7.4 s whose last second cross-fades into 0.2–1.2 s, so the loop only plays forward and has no visible jump (playing it in reverse looked uncanny), a 960×720 crop at x=60 scaled to 480×360 at 20 fps, without audio, H.264 and VP9. The poster is the frame at 3.8 s.

`favicon.svg` and `apple-touch-icon.png` draw the same "Jo" monogram.
