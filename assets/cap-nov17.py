import html
head = "🇷🇺 <b>ROSSIYAGA İŞ UÇUN KIRGAN ÇET ELLIKLAR ORASIDA ÖZBEKISTONLIKLAR BIRINÇI ÖRINDA</b>"
main = """2026-yil yanvar-sentyabr oylarida iş maqsadida Rossiyaga kirgan özbekistonliklar soni 1 535 026 nafarni taşkil etdi. Bu çet el fuqarolari orasida eng yuqori körsatkiç.

Ikkinçi örinda Tojikiston (665 892), üçinçi örinda Qirğiziston (289 061) turibdi.

📌 Şu davrda Rossiyada barça çet el fuqarolariga nisbatan:

🔹 taxminan 1,8 mln ta ma’muriy protokol rasmiylaştirilgan;

🔹 143,1 ming ta çiqarib yuboriş qarori qabul qilingan.

❗️ Muhim: bu raqamlarda Özbekiston fuqarolari alohida ajratilmagan, ular barça çet el fuqarolari böyiça keltirilgan.

✅ Rossiyada iş qilayotgan yoki bormoqçi bölganlarga hujjatlar muddatini oldindan tekşiriş tavsiya etiladi."""
foot = """<b>🌐Telegram sahifamizga obuna böling -  @wayuuz</b>

<b>🌐<a href="https://instagram.com/wayu.uz?igshid=YmMyMTA2M2Y=">Instagram</a> |  🌐<a href="http://www.facebook.com/wayu.uz">Facebook</a> |  🌐<a href="https://www.youtube.com/channel/UC9deez4fWZYs-q5O0YkAapw">YouTube</a> | 🌐<a href="https://www.linkedin.com/company/wayuuz">LinkedIn</a></b>

<b>www.wayu.uz</b>"""
import re
# plain-text length
cap = head + "\n\n" + main + "\n\n" + foot
plain = re.sub(r"<[^>]+>", "", cap)
print(len(plain.encode("utf-16-le"))//2)
for bad in ("o‘","g‘","sh","ch"):
    pass
open("/home/claude/wayu-posters/assets/cap-nov17.txt","w").write(cap)
