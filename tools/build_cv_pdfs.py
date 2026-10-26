"""Tulostaa CV-sivut PDF-tiedostoiksi.

    python -m pip install playwright
    python -m playwright install chromium
    python tools/build_cv_pdfs.py
"""

import functools
import http.server
import threading
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
TARGETS = {
    "cv/cv-fi.html": "cv_Suomi.pdf",
    "cv/cv-en.html": "cv_English.pdf",
}


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def main():
    handler = functools.partial(QuietHandler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        threading.Thread(target=server.serve_forever, daemon=True).start()
        base_url = f"http://127.0.0.1:{server.server_address[1]}"

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            for source, output in TARGETS.items():
                page.goto(f"{base_url}/{source}", wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                page.pdf(path=str(ROOT / output), prefer_css_page_size=True, print_background=True)
                print(f"{source} -> {output}")
            browser.close()

        server.shutdown()


if __name__ == "__main__":
    main()
