"""TYT Coğrafya · Basınç ve Rüzgârlar: 4 ana soru (hafif mod)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_a import *
KY='ÖSYM 2018–2026 (basınç kuşakları, rüzgârlar) · MEB 9. sınıf coğrafya'
KARTLAR={
 'K-RZG-01':dict(alt='Basınç kuşakları',fikir='Ekvator ve kutuplar termik, 30° ve 60° enlemleri dinamik basınç alanıdır.',tuzak='60° enlemini yüksek basınç sanmak.',zorluk='kolay',kalip='düz',adim=2,tipId='cg-rzg-kusak',kaynak=KY),
 'K-RZG-02':dict(alt='Basınç farkı ve rüzgâr hızı',fikir='Rüzgâr yüksekten alçak basınca eser; hız birim uzaklıktaki basınç farkıyla (basınç gradyanı) artar.',tuzak='Yalnız toplam basınç farkına bakmak, uzaklığı unutmak.',zorluk='orta',kalip='tablo',adim=3,tipId='cg-rzg-hiz',kaynak=KY),
 'K-RZG-03':dict(alt='Yerel rüzgârlar',fikir='Kara ve denizin ısınma farkı meltemi doğurur; gündüz denizden karaya, gece karadan denize eser.',tuzak='Gündüz karada yüksek basınç oluştuğunu sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='cg-rzg-yerel',kaynak=KY),
 'K-RZG-04':dict(alt='Dünya’nın dönmesi ve rüzgâr yönü',fikir='Rüzgâr Kuzey Yarım Küre’de sağa, Güney Yarım Küre’de sola sapar; kuşaklar arası rüzgârların yönü buradan bulunur.',tuzak='Sapmayı unutup rüzgârı düz kuzey-güney sanmak.',zorluk='zor',kalip='yeni nesil',adim=5,tipId='cg-rzg-sapma',kaynak=KY),
}
TIPLER={'cg-rzg-kusak':'Basınç kuşaklarının türleri','cg-rzg-hiz':'Basınç farkı ve rüzgâr hızı','cg-rzg-yerel':'Yerel rüzgârlar (meltem)','cg-rzg-sapma':'Sürekli rüzgârların yönü ve sapma'}
Q=Konu('ruzgar','Basınç ve Rüzgârlar','cog|Basınç ve Rüzgarlar',4,KARTLAR,TIPLER,{'kolay':1,'orta':2,'zor':1})

# 0001 kolay · D
Q.soru('0001','K-RZG-01','kolay','Basınç kuşaklarını termik ve dinamik, alçak ve yüksek olarak ayırt eder.',2,'düz',
 'Aşağıdaki basınç alanlarından hangisi dinamik (hava hareketine bağlı) alçak basınç alanıdır?',
 [('Kutup noktaları çevresi','termik-yuksek','Kutuplarda aşırı soğuma nedeniyle oluşan termik yüksek basınç alanıdır; dinamik değil.','bilgi'),
  ('Ekvator çevresi','termik-alcak','Ekvator’da aşırı ısınma sonucu oluşan termik alçak basınç alanıdır; dinamik değil.','bilgi'),
  ('30° enlemleri çevresi','dinamik-yuksek','Havanın alçalmasıyla oluşan dinamik alanıdır ama yüksek basınçlıdır.','dikkat'),
  ('60° enlemleri çevresi','dinamik-alcak','',''),
  ('Kışın Sibirya çevresi','termik-yuksek','Kışın soğuyan kara üzerinde oluşan termik yüksek basınç alanıdır; dinamik değildir.','bilgi')],
 'D',lambda t:t=='dinamik-alcak','Dinamik alçak basınç alanı.',
 'Sıcaklık değil de hava hareketi yüzünden oluşan alçak basınç hangi enlemdedir?',
 [B('Basınç kuşakları','Ekvator: termik alçak (ısınma) · 30° enlemleri: dinamik yüksek (hava alçalır) · 60° enlemleri: dinamik alçak (hava yükselir) · Kutuplar: termik yüksek (soğuma)')],
 [A('Sınıflandırmayı hatırla','Isınma ve soğumayla oluşanlar termik, hava hareketiyle oluşanlar dinamik basınçtır.','termik: ekvator, kutup · dinamik: 30°, 60°'),
  A('Alçak olanı seç','Dinamik kuşaklardan 30° yüksek, 60° alçak basınçlıdır.','30°: yüksek · 60°: alçak'),
  A('Sonuç','Dinamik alçak basınç alanı 60° enlemleri çevresidir.','60° enlemleri')],
 'Ekvator–30°–60°–kutup sırasında basınç alçak, yüksek, alçak, yüksek diye gider.')

# 0002 orta · B
TB={'K':1016,'L':1004,'M':1012,'N':1000,'R':1024,'S':1008,'P':1020,'T':1000}
CF=[('K','L',200),('M','N',300),('R','S',200),('P','T',500)]
gr={a+b:Fr(abs(TB[a]-TB[b]),d) for a,b,d in CF}
en=max(gr,key=gr.get); assert en=='RS' and sorted(gr.values())[-1]>sorted(gr.values())[-2]
assert max(CF,key=lambda c:abs(TB[c[0]]-TB[c[1]]))[:2]==('P','T')
def yon(a,b): return (a,b) if TB[a]>TB[b] else (b,a)
Q.soru('0002','K-RZG-02','orta','Basınç farkı ve uzaklıktan rüzgâr hızı ile yönünü belirler.',3,'tablo',
 'Aynı yükseltideki sekiz noktanın basınç değerleri ve ikili noktalar arasındaki uzaklıklar aşağıda verilmiştir.\nK: 1016 hPa, L: 1004 hPa (K–L arası 200 km)\nM: 1012 hPa, N: 1000 hPa (M–N arası 300 km)\nR: 1024 hPa, S: 1008 hPa (R–S arası 200 km)\nP: 1020 hPa, T: 1000 hPa (P–T arası 500 km)\nBu ikililer arasında rüzgârın hızının en fazla olduğu yer ve rüzgârın yönü aşağıdakilerin hangisinde doğru verilmiştir?',
 [('P–T arasında, P’den T’ye',('PT',('P','T')),'Basınç farkı en büyük olan çift P–T’dir (20 hPa) ama uzaklık 500 km olduğu için 100 km’deki fark 4 hPa kalır; en hızlı rüzgâr burada değildir.','dikkat'),
  ('R–S arasında, R’den S’ye',('RS',('R','S')),'',''),
  ('R–S arasında, S’den R’ye',('RS',('S','R')),'Çift doğru ama yön ters: rüzgâr yüksek basınçtan (R, 1024) alçak basınca (S, 1008) eser.','bilgi'),
  ('K–L arasında, K’den L’ye',('KL',('K','L')),'K–L’de 100 km’deki fark 6 hPa’dır; R–S’deki 8 hPa’dan azdır.','islem'),
  ('M–N arasında, N’den M’ye',('MN',('N','M')),'M–N’de 100 km’deki fark 4 hPa’dır; hem hız azdır hem de yön yüksek basınçtan alçağa doğru değildir.','bilgi')],
 'B',lambda t:t[0]==en and t[1]==yon(*en),'Rüzgârın hızının en fazla olduğu ikili ve rüzgârın yönü.',
 'Rüzgâr hızı, 100 km’ye düşen basınç farkıyla artar.',
 [B('Rüzgâr hızı','basınç farkı ne kadar büyük ve uzaklık ne kadar kısaysa rüzgâr o kadar hızlıdır · hız ∼ basınç farkı ÷ uzaklık (ör. 12 hPa ÷ 200 km = 6 hPa / 100 km)'),B('Rüzgâr yönü','yüksek basınçtan alçak basınca doğru eser')],
 [A('100 km’ye düşen farkı hesapla','Farkı uzaklığa böl, 100 ile çarp ya da doğrudan oranla.','K–L: 12 ÷ 2 = 6 · M–N: 12 ÷ 3 = 4 · R–S: 16 ÷ 2 = 8 · P–T: 20 ÷ 5 = 4 (hPa / 100 km)'),
  A('En büyüğü seç','En çok hPa / 100 km değeri en hızlı rüzgârı verir. Toplam fark en büyük olan P–T değildir.','en büyük: R–S (8)'),
  A('Yönü bul','R’de 1024, S’de 1008 hPa vardır. Rüzgâr R’den S’ye eser.','R (yüksek) → S (alçak)')],
 'Rüzgâr hızı için toplam basınç farkına değil, birim uzaklıktaki farka bak.')

# 0003 orta · E
Q.oncul('0003','K-RZG-03','orta','Meltemin oluşum nedenini ve yönünü değerlendirir.',3,
 'Kıyı kesimlerde deniz ve kara meltemi görülür.',
 [('Gündüz karalar denizden daha hızlı ısındığı için kara üzerinde yüksek basınç oluşur.',False,'Gündüz hızlı ısınan kara üzerinde alçak basınç oluşur; rüzgâr denizden karaya eser.'),
  ('Gece rüzgâr karadan denize doğru eser.',True,'Gece kara hızlı soğur, kara üzerinde yüksek basınç oluşur; rüzgâr karadan denize eser.'),
  ('Meltemlerin oluşmasında kara ile denizin ısınma hızlarının farklı olması etkilidir.',True,'Kara çabuk ısınıp çabuk soğur, deniz geç ısınıp geç soğur; basınç farkı bu yüzden doğar.')],
 'Bu ifadelerden hangileri doğrudur?',
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'E',True,'Doğru olan ifadeler.',
 'Gündüz kara mı deniz mi daha sıcak olur? Basıncı buna göre düşün.',
 [B('Meltem','kara ve denizin farklı ısınmasıyla oluşan yerel rüzgâr · gündüz: deniz → kara (kara sıcak, alçak basınç) · gece: kara → deniz (kara soğuk, yüksek basınç)')],
 [A('Isınma farkını hatırla','Kara çabuk ısınır ve çabuk soğur. Deniz ise geç ısınır ve geç soğur.','gündüz: kara sıcak · gece: kara soğuk'),
  A('Basıncı ve yönü bul','Gündüz kara üzerinde alçak, gece yüksek basınç oluşur. Rüzgâr yüksekten alçağa eser.','gündüz: deniz → kara · gece: kara → deniz'),
  A('İfadeleri ele','I’de basınç türü yanlıştır. II ve III doğrudur.','I: yanlış · II: doğru · III: doğru')],
 'Meltem sorularında önce kara ile denizin hangisinin sıcak olduğunu belirle.')

# 0004 zor · A
YON={45:'kuzeydoğu',135:'güneydoğu',225:'güneybatı',315:'kuzeybatı'}
ABL={'kuzeydoğu':'kuzeydoğudan','güneydoğu':'güneydoğudan','güneybatı':'güneybatıdan','kuzeybatı':'kuzeybatıdan'}
def kaynak(yarim,ekvatora):
    hed=(180 if yarim=='K' else 0) if ekvatora else (0 if yarim=='K' else 180)
    hed=(hed+45)%360 if yarim=='K' else (hed-45)%360   # K: sağa, G: sola sapma
    return YON[(hed+180)%360]
assert kaynak('K',True)=='kuzeydoğu' and kaynak('G',True)=='güneydoğu' and kaynak('K',False)=='güneybatı' and kaynak('G',False)=='kuzeybatı'
IDD=[('Kuzey','K','30° enlemlerinden 60° enlemlerine',False,'güneybatı'),
     ('Güney','G','30° enlemlerinden Ekvator’a',True,'kuzeydoğu'),
     ('Kuzey','K','kutup noktalarından 60° enlemlerine',True,'güneydoğu'),
     ('Güney','G','30° enlemlerinden 60° enlemlerine',False,'güneybatı'),
     ('Kuzey','K','30° enlemlerinden Ekvator’a',True,'güneydoğu')]
GER={0:'Batı rüzgârları: Kuzey Yarım Küre’de güneybatıdan eser.',1:'Güneydoğu alizeleri: Güney Yarım Küre’de güneydoğudan eser.',2:'Kutup doğu rüzgârları: Kuzey Yarım Küre’de kuzeydoğudan eser.',3:'Güney Yarım Küre’de bu yöndeki rüzgâr kuzeybatıdan eser (sola sapma).',4:'Kuzey Yarım Küre’de bu yöndeki rüzgâr kuzeydoğudan eser (kuzeydoğu alizeleri).'}
opts=[]
for i,(hem,h,yol,ekv,iddia) in enumerate(IDD):
    gercek=kaynak(h,ekv); dogru=(gercek==iddia)
    opts.append((f'{hem} Yarım Küre’de {yol} esen rüzgâr {ABL[iddia]} eser.',dogru,'' if dogru else GER[i],'' if dogru else ('dikkat' if i in (1,3) else 'bilgi')))
assert [o[1] for o in opts]==[True,False,False,False,False]
Q.soru('0004','K-RZG-04','zor','Dünya’nın dönmesinin etkisiyle kuşaklar arasında esen rüzgârların yönünü belirler.',5,'yeni nesil',
 'Bir coğrafya öğretmeni, yeryüzünde basınç kuşakları arasında esen sürekli rüzgârların yönünü Dünya’nın dönmesinin etkisini de hesaba katarak (rüzgârlar Kuzey Yarım Küre’de sağa, Güney Yarım Küre’de sola sapar) öğrencilerinden bulmalarını istiyor.\nBuna göre aşağıdaki yön bilgilerinden hangisi doğrudur?',
 opts,'A',lambda t:t is True,'Sapma dikkate alındığında doğru olan rüzgâr yönü bilgisi.',
 'Önce rüzgârın ekvatora mı kutba mı yöneldiğini, sonra hangi yarım kürede saptığını düşün.',
 [B('Rüzgâr nereye esiyor?','yüksek basınçtan alçak basınca · 30° → Ekvator: ekvatora doğru · 30° → 60°: kutba doğru · kutup → 60°: ekvatora doğru'),B('Sapma','Kuzey Yarım Küre’de rüzgâr gittiği yönün sağına, Güney Yarım Küre’de soluna sapar · rüzgâr yönü, estiği (geldiği) yerle adlandırılır'),B('Örnek','Kuzey’de ekvatora doğru güneye esen rüzgâr batıya sapar: kuzeydoğudan eser (kuzeydoğu alizeleri)')],
 [A('Esiş yönünü belirle','Yüksek basınç kuşağından alçak basınç kuşağına doğru esen rüzgârın düz yönü bulunur.','30° → 60°: kutba doğru (K yarım kürede kuzeye)'),
  A('Sapmayı uygula','Kuzey Yarım Küre’de sağa sapılır. Kuzeye giden rüzgâr doğuya doğru kayar.','kuzey + sağa → kuzeydoğuya gider'),
  A('Estiği yeri adlandır','Rüzgâr, geldiği yönle anılır. Kuzeydoğuya giden rüzgâr güneybatıdan eser.','güneybatıdan eser (batı rüzgârları)'),
  A('Diğer şıkları sına','Güney’de 30°–Ekvator rüzgârı güneydoğudan, Kuzey’de 30°–Ekvator ve kutup–60° rüzgârları kuzeydoğudan, Güney’de 30°–60° rüzgârı kuzeybatıdan eser.','B, C, D, E: yön yanlış'),
  A('Sonucu bul','Yalnız A şıkkı sapma hesabıyla uyuşur.','A')],
 'Önce “nereye”, sonra sapma yönü, en son “nereden” diye üç adımda ilerle.')
Q.bitir()
