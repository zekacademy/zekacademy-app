import json,sys
from itertools import product,permutations
from math import factorial as F
sys.path.insert(0,'/home/claude/zekacademy-app/havuz/tyt-mat')
H='/home/claude/zekacademy-app/havuz/tyt-mat/'
Q={q['id']:q for f in ('sayi-kumeleri-parti1.json','sayi-kumeleri-parti2.json') for q in json.load(open(H+f))}
OSYM={'sk-ardisik':[2019,2025],'sk-basamak':[2020,2021,2023,2024,2026],'sk-faktoriyel':[2021],'sk-gosterge':[2019,2020,2024],'sk-isaret':[2019],'sk-kesir':[2018,2021,2022,2023,2024,2025,2026],'sk-ondalik':[2021,2022,2023,2026],'sk-oruntu':[2023],'sk-tanimli':[2018,2019,2022,2023,2024,2025],'sk-tek-cift':[2018,2020,2021,2022,2024,2025],'sk-yerlestirme':[2018,2019,2020,2022,2025,2026]}
B=lambda a,i:dict(ad=a,ifade=i)
TEK=B('Tek-çift kuralları','tek + tek = çift · çift + çift = çift · tek + çift = tek'); CARP=B('Çarpımda tek-çift','çarpanlardan biri çiftse çarpım çifttir; hepsi tekse çarpım tektir')
ASAL=B('Asal sayı','1’den büyük, yalnızca 1’e ve kendisine bölünen sayı: 2, 3, 5, 7, 11, 13, … 2 tek çift asal sayıdır')
FAK=B('Faktöriyel','n! = 1 × 2 × … × n. Örnek: 4! = 24. Ayrıca 7! = 7 × 6 × 5! gibi yazılabilir')
A=lambda b,a,i:dict(baslik=b,aciklama=a,islem=i)
def K(id,tip,z,metin,siklar,sik,cel,bilgi,adimlar,puf,kisa):
    o=Q[id]; return dict(id=id+'k',ana=id,tipId=o['tipId'],tip=o['tip'],k=o['k'],zorluk=z,metin=metin,siklar=dict(zip('ABCDE',siklar)),cevap=dict(sik=sik,deger=dict(zip('ABCDE',siklar))[sik]),celdiriciler=cel,bilgi=bilgi,adimlar=adimlar,puf=puf,kisaYol=kisa,istenen='')
# --- doğrulamalar
cs=[(a,b,c) for a,b,c in product([0,1],repeat=3) if (a+b*c)%2==1 and (a*c+b)%2==0]; assert cs==[(1,0,0)]
L={p[6] for p in permutations([3,4,5,6,7,11,12]) if p[0]*p[1]==p[2] and p[3]+p[4]==p[5]}; assert L=={7}
x=[x for x in range(1,99,2) if 4*x+12==5*x-3]; assert x==[15]
P=[p for p in range(2,40) if all(p%d for d in range(2,int(p**.5)+1))]
s=[(a,b,c) for a in P for b in P for c in P if a<b and a*b+c==29]; assert min(map(sum,s))==18 and sorted(map(sum,s))==[18,20,26,28]
assert F(7)//F(5)+F(4)==66
KD=[
K('tytmat-sayilar-0002','sk-tek-cift','orta','a, b ve c pozitif tam sayılar olmak üzere\na + b × c bir tek sayı,\na × c + b bir çift sayıdır.\nBuna göre\nI. a + c\nII. b × c\nIII. a + b + c\nifadelerinden hangileri her zaman tek sayıdır?',
 ['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],'D',dict(A='III de her zaman tek: a tek, b ve c çift.',B='I de her zaman tek: tek + çift = tek.',C='b × c çift; II olamaz.',E='b × c çifttir; II her zaman tek değil.'),[TEK,CARP],
 [A('a çift olsaydı?','a × c çift olur; a × c + b çift olduğundan b de çift olur. O zaman a + b × c = çift + çift = **çift** çıkar, ama tek olmalıydı.','çelişki ⇒ a tek'),
  A('b’yi bul','a × c + b çift. a tek; c tekse a × c tek olur ve b tek olmalı, o zaman b × c tek ve a + b × c çift çıkar ✗. O hâlde **c çift**, a × c çift, **b çift**.','c çift · b çift'),
  A('İfadeleri dene','a tek, b çift, c çift: a + c tek, b × c çift, a + b + c tek.','I ve III tek')],
 '“Biri tek mi?” sorularında bir harfi varsayıp çelişki aramak en hızlı yoldur.','a’yı çift varsay, çelişki çıkınca a tek; sonra c’yi dene. İki deneme yeter.'),
K('tytmat-sayilar-0005','sk-yerlestirme','orta','3, 4, 5, 6, 7, 11 ve 12 sayılarından altısı, her kutuya farklı bir sayı gelecek şekilde aşağıdaki kutulara yazılıyor ve iki eşitlik de sağlanıyor.\n□ × □ = □\n□ + □ = □\nBuna göre kutulara yazılmayan sayı kaçtır?',
 ['5','6','7','11','12'],'C',dict(A='5, 5 + 6 = 11 eşitliğinde kullanılıyor.',B='6, 5 + 6 = 11 eşitliğinde kullanılıyor.',D='11, 5 + 6 = 11 eşitliğinin sonucu.',E='12, 3 × 4 = 12 eşitliğinin sonucu.'),[],
 [A('Çarpmayı dene','Sonucu da listede olan çarpım: 3 × 4 = 12 (diğerleri, ör. 3 × 5 = 15, listede yok).','3 × 4 = 12'),
  A('Kalanları yaz','3, 4 ve 12 kullanıldı.','kalanlar: 5, 6, 7, 11'),
  A('Toplamayı dene','5 + 6 = 11 uyuyor.','5 + 6 = 11 ⇒ dışarıda 7')],
 'En sıkı kısıt çarpmadadır; önce onu yerleştir.','Çarpımı listede olan tek ikiliyi bul; kalan dört sayıdan toplamı bulmak saniyeler sürer.'),
K('tytmat-sayilar-0008','sk-ardisik','kolay','Ardışık dört tek doğal sayının toplamı, bu sayıların en küçüğünün 5 katından 3 eksiktir.\nBuna göre bu sayıların en büyüğü kaçtır?',
 ['13','15','17','19','21'],'E',dict(A='13 hiçbir koşulu sağlamıyor; denklemi yeniden kur.',B='15 en küçük sayı; soru en büyüğü soruyor.',C='17 ikinci sayı; en büyük sayı x + 6.',D='19 üçüncü sayı; en büyük sayı x + 6.'),[B('Ardışık tek sayılar','2’şer artar: 15, 17, 19, …')],
 [A('En küçüğe x de','Dört sayı 2’şer artar.','x, x + 2, x + 4, x + 6'),A('Topla','x’ler ve sayılar ayrı toplanır.','4x + 12'),A('Denklemi kur','Toplam, 5x’ten 3 eksik. İki taraftan 4x çıkar, 3 ekle.','4x + 12 = 5x − 3 ⇒ x = 15'),A('En büyüğü bul','En büyük sayı x + 6.','15 + 6 = 21')],
 'Soru en büyüğü soruyorsa x’i bulunca durma.','Ortalama yöntemi: dört ardışık tek sayının toplamı = 4 × (en küçük + 3).'),
K('tytmat-sayilar-0019','sk-asal','orta','x, y ve z asal sayılar ve x < y olmak üzere\nx · y + z = 29\nolduğuna göre x + y + z toplamı en az kaçtır?',
 ['18','20','26','28','30'],'A',dict(B='20, x = 2, y = 11, z = 7 durumu; daha küçük toplam var.',C='26, x = 2, y = 5, z = 19 durumu; daha küçük toplam var.',D='28, x = 2, y = 3, z = 23 durumu; daha küçük toplam var.',E='30 veren bir asal üçlü yok.'),[ASAL,TEK],
 [A('Tek-çift dengesi','29 tek; x · y ve z’den biri çift olmalı. Çift asal yalnızca 2.','z = 2 veya x = 2'),
  A('z = 2 durumu','x · y = 27 olmalı; 27 = 3 × 9 ve 9 asal değil. Bu durum olmaz.','z ≠ 2'),
  A('x = 2 durumu','2y + z = 29: y = 3 ⇒ 23, y = 5 ⇒ 19, y = 11 ⇒ 7, y = 13 ⇒ 3 (hepsi asal).','toplamlar 28, 26, 20, 18'),
  A('En küçüğü seç','En küçük toplam 2 + 13 + 3.','18')],
 'Toplam tekse içlerinden biri 2’dir; sonra durumları tek tek yaz.','x = 2 iken toplam = 2 + y + (29 − 2y) = 31 − y; y en büyük olunca toplam en küçük olur: y = 13 ⇒ 18.'),
K('tytmat-sayilar-0024','sk-faktoriyel','kolay','7!/5! + 4!\nişleminin sonucu kaçtır?',
 ['42','46','66','84','840'],'C',dict(A='42, yalnızca 7!/5!; 4!’i eklemeyi unutmuşsun.',B='4! yerine 4 eklemişsin; 4! = 24.',D='7!/5!’i iki kez saymışsın: 7 × 6 = 42.',E='840 = 7 × 6 × 5 × 4; 5! sadeleşince yalnızca 7 × 6 kalır.'),[FAK],
 [A('7!/5!','7! = 7 × 6 × 5! olduğundan 5! sadeleşir.','7!/5! = 7 × 6 = 42'),A('4!','4 faktöriyel.','4! = 1 × 2 × 3 × 4 = 24'),A('Topla','İki sonucu topla.','42 + 24 = 66')],
 'Faktöriyel bölmesinde büyük faktöriyeli küçüğe kadar aç.','7!/5! = 7 × 6: üstteki sayıdan başlayıp alttakine kadar (dahil değil) çarp.'),
]
KISA={'tytmat-sayilar-0002':'a’yı tek varsay: ikinci koşuldan b ve c tek çıkar, birinci koşul bozulur. Tek denemede a çift bulunur.',
'tytmat-sayilar-0008':'Ortadaki sayı yöntemi: beş ardışık çift sayının toplamı = 5 × ortadaki. 5m = 6(m − 4) ⇒ m = 24, en büyük 24 + 4 = 28.',
'tytmat-sayilar-0019':'Toplam tek ⇒ içlerinden biri 2. Önce z = 2’yi dene: 3 × 7 + 2 = 23 ⇒ toplam 12; diğer durumlarda y ≥ 3 ve z büyük olduğundan toplam daha büyük.',
'tytmat-sayilar-0024':'6!/4! = 6 × 5: üstteki sayıdan başlayıp alttakine kadar (dahil değil) çarp.'}
sec=['tytmat-sayilar-0002','tytmat-sayilar-0005','tytmat-sayilar-0008','tytmat-sayilar-0019','tytmat-sayilar-0024']
out=[]
for i in sec:
    q=dict(Q[i]); q['kisaYol']=KISA.get(i); q['kardes']=i+'k'; out.append(q)
json.dump(dict(test=out,kardes={k['id']:k for k in KD},osym=OSYM),open('veri.json','w'),ensure_ascii=False)
print('ok',len(out),len(KD))
