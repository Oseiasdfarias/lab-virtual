#!/usr/bin/env python3
"""Rasteriza os SVGs da marca com Chrome headless (antialiasing muito superior ao ImageMagick)."""
import os
import sys
from playwright.sync_api import sync_playwright

BRAND = "/home/osfarias/workspace/workspace_mestrado/Projeto_Tcc_Oseias_Oficial/brand"

# (svg, png, largura_alvo)
JOBS = [
    ("icone.svg", "icone-1024.png", 1024),
    ("icone.svg", "icone-512.png", 512),
    ("icone.svg", "icone-256.png", 256),
    ("icone.svg", "icone-128.png", 128),
    ("icone.svg", "icone-64.png", 64),
    ("icone-reduzido.svg", "icone-reduzido-256.png", 256),
    ("icone-solido.svg", "icone-solido-512.png", 512),
    ("icone-solido-branco.svg", "icone-solido-branco-512.png", 512),
    ("favicon.svg", "favicon-180.png", 180),
    ("favicon.svg", "favicon-64.png", 64),
    ("favicon.svg", "favicon-32.png", 32),
    ("favicon.svg", "favicon-16.png", 16),
    ("favicon-contorno.svg", "favicon-contorno-180.png", 180),
    ("favicon-contorno.svg", "favicon-contorno-32.png", 32),
    ("logo-horizontal.svg", "logo-horizontal-1600.png", 1600),
    ("logo-horizontal.svg", "logo-horizontal-800.png", 800),
    ("logo-horizontal-solido.svg", "logo-horizontal-solido-800.png", 800),
    ("logo-vertical.svg", "logo-vertical-800.png", 800),
    ("logo-vertical-solido.svg", "logo-vertical-solido-800.png", 800),
]


def viewbox(svg_text):
    import re
    m = re.search(r'viewBox="([\d.\s-]+)"', svg_text)
    _, _, w, h = [float(v) for v in m.group(1).split()]
    return w, h


def main():
    os.makedirs(f"{BRAND}/png", exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for svg_name, png_name, target in JOBS:
            src = f"{BRAND}/svg/{svg_name}"
            with open(src, encoding="utf-8") as f:
                svg = f.read()
            vw, vh = viewbox(svg)
            th = round(target * vh / vw)
            # remove width/height fixos para o CSS controlar
            import re
            svg = re.sub(r'\swidth="[\d.]+"\s+height="[\d.]+"', "", svg, count=1)
            html = (
                "<!doctype html><meta charset='utf-8'>"
                "<style>html,body{margin:0;padding:0;background:transparent}"
                f"svg{{display:block;width:{target}px;height:{th}px;"
                "shape-rendering:geometricPrecision;}}</style>" + svg
            )
            page = browser.new_page(viewport={"width": target, "height": th},
                                    device_scale_factor=1)
            page.set_content(html)
            page.screenshot(path=f"{BRAND}/png/{png_name}", omit_background=True)
            page.close()
            print(f"  -> png/{png_name} ({target}x{th})")
        browser.close()


if __name__ == "__main__":
    main()
