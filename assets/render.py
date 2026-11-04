import sys, os
from playwright.sync_api import sync_playwright
# usage: python3 render.py <html_file> <out_png>   (html must reference logo_mark.png and fonts/ relative to its folder)
html, out = os.path.abspath(sys.argv[1]), sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1080, 'height': 1080}, device_scale_factor=2)
    pg.goto('file://' + html); pg.wait_for_timeout(800)
    pg.screenshot(path=out); b.close()
