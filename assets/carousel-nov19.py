import os, html
from playwright.sync_api import sync_playwright
from PIL import Image
OUT = '/home/claude/wayu-posters/posters/2026-11-19-mehnat-huquqlari'
os.makedirs(OUT, exist_ok=True)
TOTAL = 7
CSS = open('germany-nov18.html', encoding='utf-8').read().split('<style>')[1].split('</style>')[0]
CSS = CSS.replace('width:1080px;height:1080px', 'width:1080px;height:1350px')
CSS += """
.wrap{padding:60px 66px 104px;display:flex;flex-direction:column}
.tag{align-self:flex-start;margin-top:34px;display:inline-block;background:var(--navy);color:#fff;font-weight:800;font-size:27px;letter-spacing:2px;padding:10px 24px;border-radius:999px}
h2{font-family:AntonX,Impact,sans-serif;font-weight:400;font-size:80px;line-height:1.06;margin-top:24px;letter-spacing:.5px}
h2 span{color:var(--orange)}
ul.l{list-style:none;margin-top:30px;display:flex;flex-direction:column;gap:14px;flex:1}
ul.l li{flex:1;max-height:150px;display:flex;gap:22px;align-items:center;background:#fff;border-radius:24px;padding:12px 26px;font-weight:800;font-size:37px;line-height:1.15;box-shadow:0 2px 10px rgba(12,36,71,.08)}
ul.l li i{flex:none;width:58px;height:58px;border-radius:50%;background:var(--blue);color:#fff;font-style:normal;font-family:AntonX,Impact,sans-serif;font-size:34px;display:flex;align-items:center;justify-content:center}
ul.red li i{background:var(--orange)}
.note{margin-top:22px;background:var(--orange);color:#fff;border-radius:24px;padding:24px 30px;font-weight:800;font-size:34px;line-height:1.2}
.note.b{background:var(--blue)}
.pg{position:absolute;left:66px;bottom:34px;font-weight:800;font-size:25px;color:#5b4690}
.sw{position:absolute;right:66px;bottom:34px;font-weight:800;font-size:25px;color:var(--navy);letter-spacing:1px}
.cover h1{font-size:170px;margin-top:70px;line-height:1.02;white-space:normal}
.cover .sub{font-size:48px;margin-top:50px!important}
"""
HEAD = '<div class="head"><img class="logo" src="logo_mark.png"><span class="div"></span><div class="org">Özbekiston<br>Yoşlari Umumjahon<em>Assotsiatsiyasi</em></div></div>'
def li(items, red=False):
    return '<ul class="l%s">' % (' red' if red else '') + ''.join('<li><i>%d</i><span>%s</span></li>' % (n, html.escape(t)) for n, t in enumerate(items, 1)) + '</ul>'
def page(i, body, last=False):
    foot = '<div class="pg">%d / %d</div>' % (i, TOTAL) + ('<div class="sw">WAYU.UZ</div>' if last else '<div class="sw">SURIŞTIRING →</div>')
    return '<!doctype html><html lang="uz"><head><meta charset="utf-8"><style>%s</style></head><body><div class="rings"><i></i><i></i><i></i></div><div class="wrap">%s%s</div>%s</body></html>' % (CSS, HEAD, body, foot)
S = []
S.append(page(1, '<div class="cover"><h1>MEHNAT <span>HUQUQINI</span> BILING</h1><div class="sub">Xorijga işga ketmoqçimisiz? Şartnoma imzolaşdan avval nimalarni bilişingiz kerak</div><div class="chips" style="margin-top:50px"><span class="chip">Şartnoma</span><span class="chip">Şaroit</span><span class="chip">Huquq</span><span class="chip">Himoya</span></div></div>'))
S.append(page(2, '<div class="tag">1 · MEHNAT ŞARTNOMASI</div><h2>IMZO QÖYIŞDAN AVVAL <span>TEKŞIRING</span></h2>' + li([
 'Ish beruvchining nomi va manzili', 'Lavozim va ish vazifalari', 'Maoş va uning berilış muddati', 'Ish vaqti va dam olış kunlari',
 'Şartnomaning amal qilış muddati', 'Turar joy, ovqat va transport xarajatini kim qoplaydi', 'Şartnomani bekor qilış şartlari']) +
 '<div class="note b">Tuşunarsiz bandga imzo qöymang. Bir nusxasini özingizda saqlang.</div>'))
S.append(page(3, '<div class="tag">2 · ISH ŞAROITLARI</div><h2>MAOŞDAN TAŞQARI <span>NIMANI SURIŞTIRASIZ?</span></h2>' + li([
 'Ish kuni necha soat, haftada necha kun?', 'Qöşimça ish uçun haq töylanadimi?', 'Ta’til va dam olış kunlari qanday?',
 'Xavfsizlik qoidalari va himoya vositalari bormi?', 'Kasallik yoki baxtsiz hodisada kim yordam beradi?', 'Yaşaş joyining şaroiti qanday?']) +
 '<div class="note">Qurilış, işlab çiqariş, qişloq xöjaligi va xizmat körsatişda xavfsizlikka alohida e’tibor bering.</div>'))
S.append(page(4, '<div class="tag">3 · SIZNING HUQUQLARINGIZ</div><h2>MUHOJIR BÖLIŞ — <span>HUQUQSIZLIK EMAS</span></h2>' + li([
 'Kelişilgan maoşni vaqtida va töliq olış', 'Xavfsiz mehnat şaroiti', 'Belgilangan ish vaqti va dam olış kunlari',
 'Qonunda nazarda tutilgan haq töylanadigan ta’til', 'Kamsitiş va majburiy mehnatdan himoya', 'Huquq buzilsa — vakolatli tashkilotga murojaat']) +
 '<div class="note b">Huquqlaringiz mezbon mamlakat qonunçiligi va şartnoma şartlariga muvofiq amalga oşiriladi.</div>'))
S.append(page(5, '<div class="tag">4 · HUQUQ BUZILSA</div><h2>BEFARQ BÖLMANG: <span>5 QADAM</span></h2>' + li([
 'Şartnoma, tölov hujjatlari va yozişmalarni saqlang', 'Muammoni ish beruvçi bilan yozma qayd eting', 'Mehnat inspeksiyasi yoki vakolatli tashkilotga murojaat qiling',
 'Özbekistonning elçixonasi yoki konsulligi bilan boğlaning', 'Huquqşunos yoki migrantlarni qöllab-quvvatlovçi tashkilotdan yordam sörang']) +
 '<div class="note">Pasportni olib qöyiş va tahdid — qonunbuzarlik. Hayotingizga xavf bölsa, avval xavfsiz joyga çiqing va favqulodda xizmatga qöngiroq qiling.</div>'.replace('ı','i')))
S.append(page(6, '<div class="tag">5 · KETIŞDAN OLDIN</div><h2>HUJJATLARNI <span>TAYYORLANG</span></h2>' + li([
 'Muddati yetarli xorijga çiqiş pasporti', 'Viza va işlaş ruxsatnomasi (mamlakat talabiga köra)', 'Mehnat şartnomasi',
 'Ish beruvchining aloqa ma’lumotlari', 'Yaşaş manzili va favqulodda vaziyatda bog‘lanadigan raqamlar'.replace('bog‘lanadigan','boğlanadigan'), 'Muhim hujjatlarning elektron va qoğoz nusxalari'])))
S.append(page(7, '<div class="tag">OGOHLANTIRIŞ BELGILARI</div><h2>BUNDAY TAKLIFDAN <span>EHTIYOT BÖLING</span></h2>' + li([
 'Oldindan katta pul talab qilinadi', 'Şartnomasiz işga taklif qilinadi', 'Haddan taşqari yuqori maoş va’da qilinadi', 'Vositaçining qonuniy faoliyati tasdiqlanmagan'], red=True) +
 '<div class="note b">Xavfsizlik va huquqiy himoya ish boşlaşdan oldin boşlanadi. Huquqlaringizni biling, hujjatlaringizni saqlang.</div><div class="chips" style="margin-top:26px"><span class="chip">Telegram: @wayuuz</span></div>', last=True))
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width':1080,'height':1350}, device_scale_factor=1)
    for i, h in enumerate(S, 1):
        f = 'slide%d.html' % i
        open(f, 'w', encoding='utf-8').write(h)
        pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(700)
        pg.screenshot(path='/tmp/s%d.png' % i)
        Image.open('/tmp/s%d.png' % i).convert('RGB').save('%s/%d.jpg' % (OUT, i), quality=93)
        os.remove(f)
    b.close()
