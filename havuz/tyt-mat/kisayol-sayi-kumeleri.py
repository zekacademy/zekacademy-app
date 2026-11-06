"""Ana sorulara kısa yol + kardeş bağlantısı (yalnızca gerçekten hızlı olanlarda kisaYol)."""
import json,os
H=os.path.dirname(os.path.abspath(__file__))
KISA={
'0001':'Rakamlardan biri mutlaka 1 olmalı (hepsi 2 ve üstüyse çarpım büyük kalır); 1 + b + c = bc ⇒ (b − 1)(c − 1) = 2 ⇒ {1, 2, 3}, sıralanışı 3! = 6.',
'0002':'a’yı tek varsay: ikinci koşuldan b ve c tek çıkar, birinci koşul bozulur. Tek denemede a çift bulunur.',
'0003':'k. nesnenin yeri = (k − 1) × aralık: 3 × 0,6 = 1,8 ve 5 × 0,4 = 2,0; fark 0,2.',
'0006':'A + B = 11 ve A − B = 3 olunca: A = (11 + 3) ÷ 2 = 7, B = (11 − 3) ÷ 2 = 4.',
'0007':'Şıkların hepsi ilk koşulu sağlıyor; yalnızca ikinci koşulu dene: ⟨99⟩ = 18 ve [18] = 8. Diğer şıklarda rakam toplamı 17, 11, 14.',
'0008':'Ortadaki sayı yöntemi: beş ardışık çift sayının toplamı = 5 × ortadaki. 5m = 6(m − 4) ⇒ m = 24, en büyük 24 + 4 = 28.',
'0009':'Şıklar 120’li; sınırları da 120’liye çevir (48, 50, ≈51,4). Tek yanlış için sayı 48 ile 50 arasında olmalı: 49.',
'0011':'12,40 × 2,5 = 124 ÷ 4 = 31 (× 2,5 = × 10 ÷ 4); 18,60 × 1,5 = 18,60 + 9,30.',
'0012':'15 dakika = 900 sn = 12 tam tur; kalan 2 dk 20 sn = 140 sn = 75 + 65. Turun 65. saniyesi: kırmızının 20. saniyesi.',
'0019':'Önce z = 2’yi dene: 3 × 7 + 2 = 23 ⇒ toplam 12. x = 2 durumunda z ≥ 13 ya da 17 olduğu için toplam daha büyük kalır.',
'0021':'Sayı ver: a = 1, b = −1, c = −2 koşulları sağlar. Şıkları bu değerlerle hesapla; yalnızca a · b · c = 2 pozitif.',
'0024':'6!/4! = 6 × 5: üstteki sayıdan başlayıp alttakine kadar (dahil değil) çarp.',
'0026':'k = 1, e = 2 koy: k · e = 2, k + e = 3, 2k + e = 4, k · e + e = 4, e² = 4. Tek olan yalnızca k + e.',
}
KAR={'0001','0002','0003','0004','0005','0006','0007','0008','0009','0010','0011','0012','0019','0024'}
for f in ('sayi-kumeleri-parti1.json','sayi-kumeleri-parti2.json'):
    p=os.path.join(H,f); Q=json.load(open(p))
    for q in Q:
        n=q['id'][-4:]; q['kisaYol']=KISA.get(n)
        if n in KAR: q['kardes']=q['id']+'k'
        else: q.pop('kardes',None)
    json.dump(Q,open(p,'w'),ensure_ascii=False,indent=1)
print('ok',len(KISA))
