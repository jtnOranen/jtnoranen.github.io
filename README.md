# jtnoranen.github.io

Joel Orasen kotisivu: https://jtnoranen.github.io/

Sivusto on puhdasta HTML:ää ja CSS:ää ilman build-vaihetta. GitHub Pages julkaisee `main`-haaran sellaisenaan.

## Rakenne

- `index.html` ja `style.css`: koko sivusto yhdellä sivulla
- `img/`: valokuva JPEG- ja WebP-muodossa, jakokuva `og-image.jpg` ja CV-kuva
- `cv/`: CV:iden lähdesivut, joista PDF:t tulostetaan
- `cv_Suomi.pdf` ja `cv_English.pdf`: ladattavat CV:t
- `cv.html` ja `portfolio.html`: vanhojen osoitteiden uudelleenohjaukset

## Esikatselu

```
python -m http.server 8000
```

Avaa sitten http://localhost:8000.

## CV:n päivittäminen

Muokkaa tiedostoja `cv/cv-fi.html` ja `cv/cv-en.html` ja tulosta PDF:t uudelleen:

```
python -m pip install playwright
python -m playwright install chromium
python tools/build_cv_pdfs.py
```

Tarkista lopuksi, että kumpikin PDF mahtuu yhdelle sivulle.
