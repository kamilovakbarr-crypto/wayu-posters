body = """🇷🇺 <b>ROSSIYADA 1-YANVARDAN DAROMADI KÖRSATILMAGAN MIGRANTLARGA PATENT VA IŞ RUXSATNOMASI BERILMAYDI</b>

Rossiyada 2027-yil 1-yanvardan çet el fuqarosi daromadi haqida ma’lumot bölmasa, iş ruxsatnomasi va patent berilmaydi. Ilgari berilgan hujjatlar ham bekor qilinişi mümkin.

📌 Tekşiriş tartibi:

🔹 Soliq xizmati ma’lumotlarni 1-oktyabrdan, Ijtimoiy suğurta jamğarmasi 25-oktyabrdan IIVga uzatmoqda.

🔹 Qaror suğurta badallari hisobotiga asoslanadi: yilning 3, 6, 9 va 12 oyi uçun. Hisobotda tölov körsatilmagan bölsa, rad etiladi.

🔹 Patent bekor qilinsa, egasi va voyaga yetmagan bolalari 15 kun içida çiqişi lozim.

❗️ Muhim: rasmiy hisobotsiz tölanadigan ish haqi patentni xavf ostiga qöyadi. Qismen ma’lumot bölgan holatlar tartibi hali tuşuntirilmagan.

✅ Ish beruvçidan badallar tölanayotganini tekşirib turiş tavsiya etiladi.

"""
footer = """<b>🌐Telegram sahifamizga obuna böling -  @wayuuz</b>

<b>🌐<a href="https://instagram.com/wayu.uz?igshid=YmMyMTA2M2Y=">Instagram</a> |  🌐<a href="http://www.facebook.com/wayu.uz">Facebook</a> |  🌐<a href="https://www.youtube.com/channel/UC9deez4fWZYs-q5O0YkAapw">YouTube</a> | 🌐<a href="https://www.linkedin.com/company/wayuuz">LinkedIn</a></b>

<b>www.wayu.uz</b>"""
body = body.replace("ish haqi","iş haqi")
import re
t = body+footer
plain = re.sub(r'<[^>]+>','',t)
print(len(plain.encode('utf-16-le'))//2)
open('cap-nov19.txt','w').write(t)
