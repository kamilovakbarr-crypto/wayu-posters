import sys, datetime, re
# usage: python3 recolor.py <in.html> <out.html> [palette_index]   (default: rotates by day of year)
PAL = [
 dict(navy="#0c2447", blue="#2060c4", acc="#f26b21", b1="#f3f9ff", b2="#dcecfc", b3="#cfe4fa", mute="#2c4a78"),  # blue/orange (base)
 dict(navy="#0b3b2e", blue="#0f8b6d", acc="#f2a900", b1="#f2fbf6", b2="#d9f1e5", b3="#c6e8d8", mute="#2f6352"),  # green/amber
 dict(navy="#2a1456", blue="#6a3fd0", acc="#ff5a7a", b1="#f7f2ff", b2="#e6dcfb", b3="#d9cbf6", mute="#5b4690"),  # violet/coral
 dict(navy="#3a0d14", blue="#b5242f", acc="#f58a07", b1="#fff5f0", b2="#fbe0d4", b3="#f5cfc0", mute="#7a3a40"),  # crimson/orange
 dict(navy="#063a47", blue="#0a7e9c", acc="#ff6b4a", b1="#f0fafc", b2="#d3eef4", b3="#bfe5ee", mute="#2c6473"),  # teal/coral
]
src, dst = sys.argv[1], sys.argv[2]
i = int(sys.argv[3]) if len(sys.argv) > 3 else datetime.date.today().timetuple().tm_yday % len(PAL)
p, base = PAL[i], PAL[0]
h = open(src, encoding="utf-8").read()
for k in ("navy","blue"): h = h.replace(f"--{k}:{base[k]}", f"--{k}:{p[k]}")
h = h.replace(f"--orange:{base['acc']}", f"--orange:{p['acc']}")
h = h.replace(f"#f3f9ff 0%,#dcecfc 55%,#cfe4fa 100%", f"{p['b1']} 0%,{p['b2']} 55%,{p['b3']} 100%")
h = h.replace("#2c4a78", p["mute"]).replace("rgba(32,96,196,.10)", "rgba(0,0,0,.07)")
open(dst, "w", encoding="utf-8").write(h)
print("palette", i)
