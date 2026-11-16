"""Yüzde Problemleri · ŞEKİLLİ paket (10 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
from math import cos,sin,radians
H.KONU='Yüzde Problemleri'
P=Parti('yuzdesek','Yüzde Problemleri','prob|Yüzde Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli yüzde soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body,font='\\small'): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font='+font+']\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def pasta(dilim,r=1.6,tonlar=(15,30,45,60)):
    o=[]; ang=90
    for i,(nm,pc,lab) in enumerate(dilim):
        a1,a2=ang,ang-3.6*pc; mid=radians((a1+a2)/2)
        o.append(f'\\draw[thick,fill=vurgu!{tonlar[i%4]}] (0,0) -- ({r*cos(radians(a1)):.3f},{r*sin(radians(a1)):.3f}) arc[start angle={a1},end angle={a2},radius={r}] -- cycle;')
        ax='west' if cos(mid)>0.1 else 'east' if cos(mid)<-0.1 else 'center'
        o.append(f'\\node[anchor={ax},align=center] at ({(r+0.15)*cos(mid):.3f},{(r+0.3)*sin(mid):.3f}) {{{nm}\\\\{lab}}};'); ang=a2
    return o
def cubuk(vals,ymax,adim,yet,fmt,sx=1.2,sy=None,yaz=''):
    sy=sy or 3.0/ymax; n=len(vals); o=[f'\\draw[-{{Stealth}}] (0,0) -- ({n*sx+0.4:.2f},0); \\draw[-{{Stealth}}] (0,0) -- (0,{ymax*sy+0.4:.2f}) node[above] {{{yaz}}};']
    for t in range(adim,ymax+1,adim):
        o.append(f'\\draw[gray!50,dashed] (0,{t*sy:.2f}) -- ({n*sx+0.2:.2f},{t*sy:.2f}); \\draw (-0.07,{t*sy:.2f}) -- (0.07,{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{{t}}};')
    for i,(nm,v) in enumerate(vals):
        x=(i+0.5)*sx
        o.append(f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] ({x-0.36:.2f},0) rectangle ({x+0.36:.2f},{v*sy:.2f}); \\node[above=1pt] at ({x:.2f},{v*sy:.2f}) {{{fmt(v)}}}; \\node[below=2pt] at ({x:.2f},0) {{{nm}}};')
    return o

IND=B('İndirim','indirim, etiket (liste) fiyatının belirtilen yüzdesi kadar düşülmesidir. Örnek: 500 TL’lik üründe %10 indirim, 500 − 50 = 450 TL öder')
ART=B('Ardışık indirim','ikinci indirim, birinci indirimden sonraki fiyat üzerinden yapılır; çarpımla hesaplanır. Örnek: %50 ve ardından %50 indirim, toplamda %75 indirimdir')
YP=B('Yüzde','bir niceliğin yüzde p’si, niceliğin p/100 katıdır. Örnek: 200 sayısının %15’i 30’dur')
YDG=B('Yüzde değişim','değişim yüzdesi, değişim miktarının başlangıç değerine oranıdır. Örnek: 40’tan 50’ye çıkış (50 − 40) ÷ 40 = %25 artıştır')
PAY=B('Pay ve toplam','bir kesimin sayısı, toplamın o kesimin yüzdesi kadarıdır; yüzdeler toplamı %100’dür. Örnek: 300 kişinin %40’ı 120 kişidir')

kartla('K-YZS-01','İndirim etiketi','Etiketteki liste fiyatından indirimli fiyat bulunur, adetle çarpılır.','İndirim tutarını ödenecek tutar sanmak; yüzdeyi TL gibi çıkarmak; adedi unutmak.','kolay','hikâyeli',3,'yzs-etiket','İndirim etiketi')
kartla('K-YZS-02','Daire grafiği','Bilinmeyen dilimin yüzdesi 100’den bulunur; istenen dilimlerin yüzdeleri toplanıp toplam sayıyla çarpılır.','Yüzdeleri sayı gibi toplamak; dilimi eksik almak.','kolay','grafik',3,'yzs-pasta','Daire grafiği ve yüzdeler')
kartla('K-YZS-03','Fiş tablosu','Birim fiyat × adet ile kalem tutarları, toplamdan da indirim yüzdesi bulunur.','Adedi unutmak; indirimi eklemek; indirim yüzdesini TL gibi çıkarmak.','kolay','tablo',4,'yzs-fis','Fiş tablosu ve indirim')
kartla('K-YZS-04','Sütun grafiği ve ortalama','Sütunlardan ortalama bulunur; yeni değer ortalamadan yüzdeyle hesaplanır, önceki yılla karşılaştırılıp yüzde değişim bulunur.','Yüzdeyi doğrudan artış sanmak; oranı artış yüzdesi yazmak; yanlış yılla karşılaştırmak.','orta','grafik',4,'yzs-sutun','Sütun grafiği ve yüzde artış')
kartla('K-YZS-05','Besin etiketi tablosu','Tablodaki miktar ve günlük değer yüzdesinden günlük değerin kendisi bulunur; porsiyon büyüdükçe miktar orantılı artar.','100 g’ın yüzdesini istenen miktara taşımamak; gramı yüzde yazmak.','orta','tablo',3,'yzs-besin','Besin etiketi ve günlük değer')
kartla('K-YZS-06','Yüzde şeridi','Şeritteki yüzdeler toplanıp kalan yüzde bulunur; kalan para üzerinden pay hesaplanır.','Kalan yerine bütünün yüzdesini almak; şeridin bir parçasını atlamak.','orta','hikâyeli',4,'yzs-serit','Yüzde şeridi ve kalan para')
kartla('K-YZS-07','Oy dağılımı grafiği','Geçerli oylar toplamı geçerli yüzdesinden toplam oya çevrilir; adayın payı toplam oya göre bulunur.','Payı geçerli oylar üzerinden hesaplamak; geçersiz yüzdesini aday yüzdesi sanmak.','orta','grafik',4,'yzs-oy','Oy dağılımı ve geçersiz oy')
kartla('K-YZS-08','Daire grafiği ve değişim','Her dilimin değişimi toplamın yüzdesi olarak bulunur; toplam değişim bunların toplamıdır.','Yüzdeleri doğrudan toplayıp çıkarmak; bir dilimi unutmak; işareti karıştırmak.','orta','hikâyeli',4,'yzs-pasta2','Daire grafiği ve toplam değişim')
kartla('K-YZS-09','İki mağaza etiketi','Birinci etiketteki ardışık indirimler çarpımla uygulanır; ikinci etiketin liste fiyatına göre eşit fiyat için gereken indirim bulunur.','İndirim yüzdelerini toplamak; liste fiyatları farklıyken yüzdeyi doğrudan taşımak.','zor','hikâyeli',4,'yzs-etiket2','Karşılaştırmalı etiketler')
kartla('K-YZS-10','Pazar payı çizgi grafiği','Satış adedi = pay × toplam pazar; pazar büyümesi ve pay değişimi çarpılarak satış değişimi bulunur.','Payın artışını satış artışı sanmak; yüzdeleri toplamak; yüzde puanı yüzde sanmak.','zor','grafik',4,'yzs-pazar','Pazar payı ve satış değişimi')

# ================= 01 kolay · indirim etiketi =================
lf,ip_,adet=1600,35,3; bir=Fr(lf*(100-ip_),100); v=bir*adet
e=[bir,Fr(lf*ip_,100)*adet,adet*(lf-ip_),adet*lf-ip_]
assert bir==1040 and v==3120 and e==[1040,1680,4695,4765] and len({v,*e})==5
o=['\\draw[thick,rounded corners=8pt,fill=vurgu!8] (0,0) rectangle (6.4,3.4); \\draw[thick] (0.55,2.75) circle (0.14);',
   '\\node at (3.4,2.75) {\\large\\textbf{KAMPANYA}};',f'\\node at (3.2,1.7) {{Liste fiyatı: \\textbf{{1\\,600 TL}}}};',
   f'\\node[draw,thick,fill=vurgu!30,rounded corners=3pt,inner sep=5pt] at (3.2,0.75) {{\\large\\textbf{{\\%{ip_} İNDİRİM}}}};']
SK=fig('\n'.join(o),'\\normalsize')
q('0001',tipId='yzs-etiket',tip='İndirim etiketi',z='kolay',alt='İndirim Etiketi',kaz='Etiket üzerindeki liste fiyatı ve indirim yüzdesiyle ödenecek tutarı hesaplar.',kalip='hikâyeli',
 kart='K-YZS-01 (indirim etiketi) · 1 600 TL, %35, 3 adet',
 metin='Bir giyim mağazasında satılan pantolonların hepsinin etiketi şekildeki gibidir ve indirim, etiketteki liste fiyatı üzerinden uygulanmaktadır; mağaza bu kampanya dışında başka bir indirim yapmamaktadır. Aynı pantolondan 3 tane almak isteyen bir müşteri, ürünleri tek seferde kasada öder.\nBuna göre, müşteri kasada toplam kaç TL öder?',
 dogru=v,yan=[(e[0],'Yalnız bir pantolonun indirimli fiyatını bulmuş; 3 ile çarpmayı unutmuş.','dikkat'),(e[1],'Ödenecek tutar yerine indirim tutarını bulmuş: 3 × 560.','dikkat'),(e[2],'%35’i 35 TL gibi düşmüş: 3 × (1600 − 35).','dikkat'),(e[3],'Üç ürünün liste fiyatından yalnız 35 TL düşmüş: 4800 − 35.','dikkat')],
 istenen='Müşterinin ödeyeceği toplam tutar (TL).',ip=['Önce tek bir pantolonun indirimli fiyatını bul; indirim, etiket fiyatının yüzdesidir.'],bilgi=[IND],sekil=SK,
 ad=[A('İndirim tutarı','Liste fiyatının %35’i.','1600 × 35/100 = 560 TL'),A('İndirimli fiyat','Liste fiyatından indirim çıkarılır.','1600 − 560 = 1040 TL'),A('Üç adet','İndirimli fiyat adetle çarpılır.','3 × 1040 = 3120 TL')],
 puf='Ödenecek tutar liste fiyatının %65’idir.')

# ================= 02 kolay · daire grafiği =================
tot=800; dl=[('Roman',35),('Hikâye',25),('Şiir',15)]; den=100-sum(p for _,p in dl); v=(15+den)*tot//100
e=[15+den,15*tot//100,den*tot//100,(35+25)*tot//100]
assert den==25 and v==320 and e==[40,120,200,480] and len({v,*e})==5 and (15+den)*tot%100==0
SK=fig('\n'.join(pasta([('Roman',38,'\\%35'),('Hikâye',23,'\\%25'),('Şiir',17,'\\%15'),('Deneme',22,'?')],r=1.5)))
q('0002',tipId='yzs-pasta',tip='Daire grafiği ve yüzdeler',z='kolay',alt='Daire Grafiği ve Yüzdeler',kaz='Daire grafiğinde bilinmeyen dilimi bulup istenen dilimlerin toplam sayısını hesaplar.',kalip='grafik',
 kart='K-YZS-02 (daire grafiği) · 800 öğrenci; 35, 25, 15, ?',
 metin='Bir okulda 800 öğrenciye en çok okumayı sevdikleri kitap türü sorulmuştur. Her öğrenci yalnız bir tür işaretlemiş ve sonuçlar şekildeki daire grafikte gösterilmiştir; bütün öğrencilerin yanıtı grafiğe dahildir; şekil ölçekli çizilmemiştir. Sonuçlar, okul kütüphanesine alınacak kitapların belirlenmesinde kullanılacaktır.\nBuna göre, şiir ve deneme türünü işaretleyen öğrencilerin sayısı toplam kaçtır?',
 dogru=v,yan=[(e[0],'Yüzdeleri (15 + 25) toplayıp kişi sayısına çevirmeyi unutmuş.','dikkat'),(e[1],'Denemeyi hesaba katmamış: yalnız şiir, 800’ün %15’i.','dikkat'),(e[2],'Şiiri hesaba katmamış: yalnız deneme, 800’ün %25’i.','dikkat'),(e[3],'Şiir ve deneme yerine roman ile hikâyeyi toplamış: 800’ün %60’ı.','dikkat')],
 istenen='Şiir ve deneme türünü işaretleyenlerin toplam sayısı.',ip=['Dilimlerin yüzdeleri toplamı %100’dür; “Deneme”nin yüzdesini bulup iki dilimi birleştir.'],bilgi=[PAY],sekil=SK,
 ad=[A('Deneme dilimi','Yüzdeler toplamı 100 olmalıdır.','100 − (35 + 25 + 15) = 25'),A('İki dilim','Şiir ve deneme yüzdeleri toplanır.','15 + 25 = 40'),A('Kişi sayısı','Toplam öğrenci sayısının %40’ı.','800 × 40/100 = 320')],
 puf='Önce yüzdeleri topla, sonra kişi sayısına çevir.')

# ================= 03 kolay · fiş tablosu =================
kal=[('Peynir',2,150),('Zeytin',3,80),('Reçel',4,65)]; tt=sum(a*b for _,a,b in kal); idy=15; ind=tt*idy//100; v=tt-ind
e=[ind,tt-idy,tt,tt+ind]
assert tt==800 and ind==120 and v==680 and e==[120,785,800,920] and len({v,*e})==5
SK=tablo_svg(['Ürün','Adet','Birim fiyat (TL)'],[[n,str(a),str(b)] for n,a,b in kal])
q('0003',tipId='yzs-fis',tip='Fiş tablosu ve indirim',z='kolay',alt='Fiş Tablosu ve İndirim',kaz='Fişteki birim fiyat ve adetlerden toplam tutarı bulup toplam üzerinden indirim uygular.',kalip='tablo',
 kart='K-YZS-03 (fiş tablosu) · toplam 800 TL, %15 indirim',
 metin='Bir bakkalın kasasında müşterinin sepetindeki ürünlerin adet ve birim fiyatları aşağıdaki tabloda verilmiştir. Kasada, sepetin toplam tutarı üzerinden %15 indirim uygulanmakta ve müşteri indirimli tutarı ödemektedir. Fiyatlara KDV dahildir ve başka bir kampanya uygulanmamaktadır.\nBuna göre, bu müşteri kaç TL öder?',
 dogru=v,yan=[(e[0],'Ödenecek tutar yerine indirim tutarını bulmuş: 800 × 15/100.','dikkat'),(e[1],'%15’i 15 TL gibi çıkarmış: 800 − 15.','dikkat'),(e[2],'İndirimi hiç uygulamamış; toplam tutarı yazmış.','dikkat'),(e[3],'İndirim yerine tutarı artırmış: 800 + 120.','dikkat')],
 istenen='Müşterinin ödeyeceği tutar (TL).',ip=['Her kalemin tutarını birim fiyatı ile adedi çarparak bul; sonra toplam tutarın yüzdesine bak.'],bilgi=[IND],sekil=SK,
 ad=[A('Kalem tutarları','Adet × birim fiyat.','300, 240 ve 260 TL'),A('Toplam','Üç tutar toplanır.','300 + 240 + 260 = 800 TL'),A('İndirim','Toplamın %15’i.','800 × 15/100 = 120 TL'),A('Ödenecek tutar','Toplamdan indirim çıkarılır.','800 − 120 = 680 TL')],
 puf='Her kalem için adet ile birim fiyat çarpılır.')

# ================= 04 orta · sütun grafiği =================
ur=[('2020',90),('2021',120),('2022',150)]; ort=Fr(sum(x for _,x in ur),3); y23=ort*Fr(150,100); v=(y23-150)*100/150
e=[Fr(y23,150)*100,y23-150,50,(y23-90)*100/90]
assert ort==120 and y23==180 and v==20 and e==[120,30,50,100] and len({v,*e})==5
SK=fig('\n'.join(cubuk(ur,180,30,'',str,sx=1.5,yaz='Üretim (bin adet)')))
q('0004',tipId='yzs-sutun',tip='Sütun grafiği ve yüzde artış',z='orta',alt='Sütun Grafiği ve Yüzde Artış',kaz='Sütun grafiğinden ortalamayı bulup yüzdeyle yeni değeri hesaplar ve yüzde artışı bulur.',kalip='grafik',
 kart='K-YZS-04 (sütun grafiği) · 90, 120, 150; ortalamanın %50 fazlası = 180',
 metin='Şekildeki sütun grafikte bir fabrikanın 2020, 2021 ve 2022 yıllarındaki üretim miktarları bin adet cinsinden verilmiştir; fabrika bu yıllarda yalnız bu ürünü üretmiştir. Fabrikanın 2023 yılındaki üretimi, bu üç yılın ortalama üretiminden %50 fazla olmuştur.\nBuna göre, 2023 yılı üretimi, 2022 yılı üretimine göre yüzde kaç artmıştır?',
 dogru=v,yan=[(e[0],'Artış yüzdesi yerine 2023 üretiminin 2022’ye oranını (180/150) yüzde olarak yazmış.','dikkat'),(e[1],'Artış miktarını (30 bin) yüzde sanmış.','dikkat'),(e[2],'Ortalamaya uygulanan %50’yi 2022’ye göre artış yüzdesi sanmış.','dikkat'),(e[3],'2022 yerine 2020 ile karşılaştırmış: (180 − 90) ÷ 90.','dikkat')],
 istenen='2023 üretiminin 2022’ye göre artış yüzdesi.',ip=['Üç sütundan ortalamayı hesapla; 2023 üretimini bulduktan sonra artışı hangi yılın üretimine göre hesaplaman gerektiğine dikkat et.'],bilgi=[YDG],sekil=SK,
 ad=[A('Ortalama','Sütunlardan okunan üç değerin ortalaması.','(90 + 120 + 150) ÷ 3 = 120'),A('2023 üretimi','Ortalamanın %50 fazlası.','120 × 1,5 = 180'),A('Artış miktarı','2022 ile fark.','180 − 150 = 30'),A('Artış yüzdesi','Artış, 2022 üretimine bölünür.','30 ÷ 150 = %20')],
 puf='Yüzde artış, başlangıç olarak sorulan yılın değerine bölünür.')

# ================= 05 orta · besin etiketi =================
bes=[('Protein',8,16),('Yağ',15,25),('Karbonhidrat',65,20)]; gram=200
gd=Fr(15*100,25); alinan=Fr(15*gram,100); v=alinan*100/gd
e=[25,alinan,gd,25+v]
assert gd==60 and alinan==30 and v==50 and e==[25,30,60,75] and len({v,*e})==5 and 8*100/16==50 and 65*100/20==325
SK=tablo_svg(['Besin ögesi','100 g’daki miktar (g)','Günlük değerin yüzdesi'],[[n,str(m),f'%{p}'] for n,m,p in bes])
q('0005',tipId='yzs-besin',tip='Besin etiketi ve günlük değer',z='orta',alt='Besin Etiketi ve Günlük Değer',kaz='Besin etiketindeki miktar ve yüzdeden günlük değeri bulup tüketilen miktarın payını hesaplar.',kalip='tablo',
 kart='K-YZS-05 (besin etiketi) · yağ 15 g = %25; 200 g tüketim',
 metin='Aşağıdaki tabloda, bir bisküvi paketinin besin etiketinde 100 g ürün için verilen miktarlar ve bu miktarların günlük değere oranı yer almaktadır. Bir kişi bu bisküviden 200 g tüketmiş ve gün içinde başka hiçbir kaynaktan yağ almamıştır.\nBuna göre, bu kişi günlük yağ değerinin yüzde kaçını almıştır?',
 dogru=v,yan=[(e[0],'200 g için hesaplama yapmamış; 100 g’ın yüzdesini yazmış.','dikkat'),(e[1],'Aldığı yağ miktarını (30 g) yüzde sanmış.','dikkat'),(e[2],'Günlük yağ değerini (60 g) yüzde sanmış.','dikkat'),(e[3],'100 g’ın yüzdesini (%25) ile 200 g’ın yüzdesini (%50) toplamış.','islem')],
 istenen='Günlük yağ değerinin alınan yüzdesi.',ip=['Tablodaki yağ satırından günlük yağ değerinin kaç gram olduğunu bul; sonra alınan yağı hesapla.'],bilgi=[YP],sekil=SK,
 ad=[A('Günlük yağ değeri','15 g, günlük değerin %25’idir.','15 ÷ 0,25 = 60 g'),A('Alınan yağ','200 g bisküvide, 100 g’ın iki katı.','2 × 15 = 30 g'),A('Yüzde','Alınan yağ, günlük değere bölünür.','30 ÷ 60 = %50')],
 puf='Önce günlük değerin kendisini (gram olarak) bul.')

# ================= 06 orta · yüzde şeridi =================
mas=9000; sg=[('Kira',30),('Market',25),('Fatura',10)]; kalan=100-sum(p for _,p in sg); kal_tl=mas*kalan//100; v=kal_tl*60//100
e=[kal_tl*40//100,mas*(100-sum(p for _,p in sg[:2]))//100*60//100,kal_tl,mas*60//100]
assert kalan==35 and kal_tl==3150 and v==1890 and e==[1260,2430,3150,5400] and len({v,*e})==5
ln=10.4; o=[]; x=0; tonlar=[20,40,60,10]; cz=[28,27,12,33]
for i,(nm,p) in enumerate(sg+[('Kalan',kalan)]):
    w=ln*cz[i]/100; lab='?' if nm=='Kalan' else f'\\%{p}'
    o.append(f'\\draw[thick,fill=vurgu!{tonlar[i]}] ({x:.2f},0) rectangle ({x+w:.2f},1.0); \\node at ({x+w/2:.2f},0.5) {{{lab}}}; \\node[above=2pt] at ({x+w/2:.2f},1.0) {{{nm}}};'); x+=w
o.append(f'\\draw[<->] (0,-0.35) -- ({ln},-0.35); \\node[below=1pt] at ({ln/2},-0.35) {{aylık maaşın tamamı}};')
SK=fig('\n'.join(o))
q('0006',tipId='yzs-serit',tip='Yüzde şeridi ve kalan para',z='orta',alt='Yüzde Şeridi ve Kalan Para',kaz='Yüzde şeridindeki payları toplayıp kalan para üzerinden yüzde pay hesaplar.',kalip='hikâyeli',
 kart='K-YZS-06 (yüzde şeridi) · maaş 9 000 TL; 30+25+10; kalanın %60’ı harçlık',
 metin='Aylık maaşı 9 000 TL olan bir çalışan, maaşını nasıl harcadığını şekildeki şeritle göstermiştir; şeridin tamamı maaşın tamamını temsil etmektedir ve şekil ölçekli çizilmemiştir. Şeritte “Kalan” ile gösterilen para için, çalışan kalan paranın %40’ını tasarruf etmekte, geri kalanını harçlık olarak kullanmaktadır.\nBuna göre, çalışanın harçlığı kaç TL’dir?',
 dogru=v,yan=[(e[0],'Harçlık yerine tasarruf miktarını bulmuş: 3150 × 40/100.','dikkat'),(e[1],'Fatura dilimini şeritten atlamış: kalan %45 = 4050 TL; harçlığı 4050’nin %60’ı sanmış.','dikkat'),(e[2],'Kalan parayı (3150 TL) harçlık sanmış.','dikkat'),(e[3],'Harçlığı maaşın %60’ı sanmış: 9000 × 60/100.','dikkat')],
 istenen='Çalışanın harçlığı (TL).',ip=['Şeritteki üç parçanın yüzdesini topla; “Kalan” parçanın maaştaki yüzdesini ve TL karşılığını bul.'],bilgi=[PAY],sekil=SK,
 ad=[A('Kalan yüzde','Üç harcamanın yüzdeleri toplamı 100’den çıkarılır.','100 − (30 + 25 + 10) = 35'),A('Kalan para','Maaşın %35’i.','9000 × 35/100 = 3150 TL'),A('Harçlık yüzdesi','Tasarruf %40 ise harçlık %60’tır.','100 − 40 = 60'),A('Harçlık','Kalan paranın %60’ı.','3150 × 60/100 = 1890 TL')],
 puf='Kalan paranın tasarruf dışında kalan kısmı harçlıktır.')

# ================= 07 orta · oy dağılımı =================
oy=[('A adayı',540),('B adayı',420),('C adayı',240)]; ge=sum(x for _,x in oy); topl=Fr(ge*100,80); v=Fr(540*100)/topl
e=[20,Fr(540*100,ge),Fr(420*100,topl),80]
assert ge==1200 and topl==1500 and v==36 and e==[20,45,28,80] and len({v,*e})==5
o=[]; sx=0.0095;
o.append(f'\\draw[-{{Stealth}}] (0,0) -- ({600*sx+0.5:.2f},0) node[right] {{Oy sayısı}}; \\draw (0,0) -- (0,-{3*0.9+0.1:.2f});')
for t in range(0,601,60): o.append(f'\\draw[gray!50,dashed] ({t*sx:.3f},0) -- ({t*sx:.3f},-{3*0.9+0.05:.2f}); \\draw ({t*sx:.3f},0.07) -- ({t*sx:.3f},-0.07); \\node[above=1pt] at ({t*sx:.3f},0.05) {{{t if t%120==0 else ""}}};')
for i,(nm,x) in enumerate(oy):
    yy=-0.45-i*0.9
    o.append(f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] (0,{yy-0.3}) rectangle ({x*sx:.3f},{yy+0.3}); \\node[left=3pt] at (0,{yy}) {{{nm}}}; \\node[right=2pt] at ({x*sx:.3f},{yy}) {{{x}}};')
SK=fig('\n'.join(o))
q('0007',tipId='yzs-oy',tip='Oy dağılımı ve geçersiz oy',z='orta',alt='Oy Dağılımı ve Geçersiz Oy',kaz='Oy dağılımı grafiğinden geçerli oyları toplayıp geçersiz oy yüzdesiyle toplam oyu bulur ve adayın payını hesaplar.',kalip='grafik',
 kart='K-YZS-07 (oy dağılımı) · geçerli 1 200; geçersiz %20; A = 540',
 metin='Bir apartman yönetimi seçiminde üç adayın aldığı geçerli oy sayıları şekilde verilmiştir. Sandıktan çıkan oyların %20’si geçersiz sayılmış ve bu oylar grafiğe dahil edilmemiştir; her seçmen yalnız bir oy kullanmış, boş oy çıkmamıştır.\nBuna göre, A adayı sandıktan çıkan toplam oyların yüzde kaçını almıştır?',
 dogru=v,yan=[(e[0],'Geçersiz oyların yüzdesini (%20) A adayının payı sanmış.','dikkat'),(e[1],'A adayının oyunu yalnız geçerli oylara oranlamış: 540 ÷ 1200.','dikkat'),(e[2],'B adayının payını hesaplamış: 420 ÷ 1500.','dikkat'),(e[3],'Geçerli oyların toplam oylara oranını (%80) yazmış.','dikkat')],
 istenen='A adayının toplam oylardaki yüzdesi.',ip=['Grafikten geçerli oyların toplamını bul; bunun toplam oyların yüzde kaçı olduğunu düşünerek toplam oy sayısına ulaş.'],bilgi=[PAY],sekil=SK,
 ad=[A('Geçerli oylar','Üç çubuğun değeri toplanır.','540 + 420 + 240 = 1200'),A('Toplam oy','Geçerli oylar toplamın %80’idir.','1200 ÷ 0,8 = 1500'),A('A’nın payı','A’nın oyu toplam oya bölünür.','540 ÷ 1500 = 0,36'),A('Yüzde','Oranı yüzdeye çevir.','%36')],
 puf='Geçerli oy yüzdesi %80 ise toplam oy, geçerli oyun 1,25 katıdır.')

# ================= 08 zor · daire grafiği, değişim =================
gd=[('Personel',45),('Kira',30),('Reklam',15),('Diğer',10)]; assert sum(p for _,p in gd)==100
v=Fr(45*20-30*10,100); e=[3,9,20-10,Fr(45*20+30*10,100)]
assert v==6 and e==[3,9,10,12] and len({v,*e})==5
SK=fig('\n'.join(pasta([(nm,p,f'\\%{p}') for nm,p in gd],r=1.5)))
q('0008',tipId='yzs-pasta2',tip='Daire grafiği ve toplam değişim',z='orta',alt='Daire Grafiği ve Toplam Değişim',kaz='Daire grafiğindeki payların farklı yüzdelerle değişmesinin toplam gider üzerindeki etkisini bulur.',kalip='hikâyeli',
 kart='K-YZS-08 (daire grafiği) · 45, 30, 15, 10; +%20 ve −%10',
 metin='Bir şirketin aylık giderlerinin dağılımı şekildeki daire grafikte verilmiştir. Gelecek ay personel giderleri %20 artacak, kira giderleri %10 azalacak; reklam ve diğer giderlerde ise bir değişiklik olmayacaktır; şirket bu ay başka bir gider kalemi eklemeyecektir.\nBuna göre, şirketin aylık toplam gideri gelecek ay yüzde kaç artar?',
 dogru=v,yan=[(e[0],'Yalnız kira azalışını hesaplamış: 30’un %10’u.','dikkat'),(e[1],'Yalnız personel artışını hesaplamış: 45’in %20’si.','dikkat'),(e[2],'Yüzdeleri doğrudan toplamış: %20 − %10.','dikkat'),(e[3],'Kira azalışını da artış sanmış: 9 + 3.','dikkat')],
 istenen='Toplam giderdeki artış yüzdesi.',ip=['Her kalemin değişimini, toplam giderin yüzdesi olarak ayrı ayrı bul; sonra işaretlerine dikkat ederek birleştir.'],bilgi=[YDG],sekil=SK,
 ad=[A('Personel','Toplamın %45’i, %20 artıyor.','45 × 20/100 = +9'),A('Kira','Toplamın %30’u, %10 azalıyor.','30 × 10/100 = −3'),A('Net değişim','Toplam giderin yüzdesi olarak.','9 − 3 = +6'),A('Sonuç','Toplam gider %6 artar.','%6')],
 puf='Her kalemin değişimi, toplam giderin yüzdesi cinsinden yazılır.')

# ================= 09 orta · iki mağaza etiketi =================
la,a1,a2=2400,25,20; lb=2000; fa=Fr(la*(100-a1)*(100-a2),10000); x=100-fa*100/lb
e=[34,40,45,48]; assert fa==1440 and x==28 and 100-Fr(la*(100-a1-a2),100)*100/lb==34 and 100-fa*100/la==40 and a1+a2==45 and Fr((la-fa)*100,lb)==48 and len({x,*e})==5
def etk(ox,baslik,satirlar):
    o=[f'\\draw[thick,rounded corners=8pt,fill=vurgu!8] ({ox},0) rectangle ({ox+5.4},3.6); \\draw[thick] ({ox+0.5},3.0) circle (0.13);',f'\\node at ({ox+3.0},3.0) {{\\large\\textbf{{{baslik}}}}};']
    for i,s in enumerate(satirlar): o.append(f'\\node at ({ox+2.7},{2.1-i*0.75:.2f}) {{{s}}};')
    return o
SK=fig('\n'.join(etk(0,'A MAĞAZASI',['Liste fiyatı: \\textbf{2\\,400 TL}','\\%25 indirim','Kasada ek \\%20 indirim'])+etk(5.9,'B MAĞAZASI',['Liste fiyatı: \\textbf{2\\,000 TL}','\\%$x$ indirim'])),'\\normalsize')
q('0009',tipId='yzs-etiket2',tip='Karşılaştırmalı etiketler',z='zor',alt='Karşılaştırmalı Etiketler',kaz='Ardışık indirimli fiyatı bulup başka liste fiyatlı ürünün aynı fiyata inmesi için gereken indirimi hesaplar.',kalip='hikâyeli',
 kart='K-YZS-09 (iki etiket) · 2 400 TL: %25 ve ek %20 = 1 440; B: 2 000 TL, %x',
 metin='Aynı marka bir ürünü satan iki mağazanın etiketleri şekilde verilmiştir. A mağazasında kasadaki ek indirim, etiket indiriminden sonraki fiyat üzerinden uygulanmaktadır. B mağazası ise tek indirim yapmaktadır. Müşteri, ürünü iki mağazadan da aynı fiyata alabilmektedir.\nBuna göre, B mağazasının etiketindeki x kaçtır?',
 dogru=x,yan=[(e[0],'Kasa indirimini de liste fiyatından hesaplamış: A’da ödenecek 1320 TL kabul edip x = 34 bulmuş.','dikkat'),(e[1],'A’nın toplam indirim yüzdesini (%40) B’ye aynen uygulamış; liste fiyatlarının farklı olduğunu unutmuş.','dikkat'),(e[2],'A’daki iki indirimi toplamış: 25 + 20.','dikkat'),(e[3],'A’daki indirim tutarının (960 TL) B’nin liste fiyatına oranını yazmış: 960 ÷ 2000.','dikkat')],
 istenen='B mağazasındaki indirim yüzdesi x.',ip=['A mağazasında ödenecek tutarı iki indirimi sırayla uygulayarak bul; B’de aynı tutarın liste fiyatına oranına bak.'],bilgi=[ART],sekil=SK,
 ad=[A('Etiket indirimi','A’da ilk indirimden sonraki fiyat.','2400 × 75/100 = 1800 TL'),A('Kasa indirimi','Bu fiyatın %20’si düşülür.','1800 × 80/100 = 1440 TL'),A('B’de oran','Ödenecek fiyatın B liste fiyatına oranı.','1440 ÷ 2000 = %72'),A('İndirim yüzdesi','100’den çıkarılır.','100 − 72 = 28')],
 puf='Ardışık indirimler çarpılarak uygulanır; yüzdeler toplanmaz.')

# ================= 10 zor · pazar payı grafiği =================
pay=[('2022',20),('2023',25),('2024',30)]; buy=Fr(120,100); v=(Fr(30)*buy/20-1)*100
e=[30-20,20,Fr(30,20)*100-100,Fr(30,20)*100-100+20]
assert v==80 and e==[10,20,50,70] and len({v,*e})==5
sx,sy=1.5,0.1; o=[f'\\draw[-{{Stealth}}] (0,0) -- ({3*sx+0.4:.2f},0); \\draw[-{{Stealth}}] (0,0) -- (0,{30*sy+0.9:.2f}) node[above] {{Pazar payı (\\%)}};']
for t_ in (10,20,30): o.append(f'\\draw[gray!50,dashed] (0,{t_*sy:.2f}) -- ({3*sx+0.2:.2f},{t_*sy:.2f}); \\draw (-0.07,{t_*sy:.2f}) -- (0.07,{t_*sy:.2f}); \\node[left=2pt] at (0,{t_*sy:.2f}) {{{t_}}};')
pts=[((i+0.5)*sx,p*sy) for i,(_,p) in enumerate(pay)]
o.append('\\draw[thick,vurgu!80!black] '+' -- '.join(f'({x:.2f},{y:.2f})' for x,y in pts)+';')
for (x,y),(nm,p) in zip(pts,pay): o.append(f'\\fill[vurgu] ({x:.2f},{y:.2f}) circle (0.08); \\node[above=3pt] at ({x:.2f},{y:.2f}) {{\\%{p}}}; \\draw ({x:.2f},0.07) -- ({x:.2f},-0.07); \\node[below=2pt] at ({x:.2f},0) {{{nm}}};')
SK=fig('\n'.join(o))
q('0010',tipId='yzs-pazar',tip='Pazar payı ve satış değişimi',z='zor',alt='Pazar Payı ve Satış Değişimi',kaz='Pazar payı çizgi grafiği ile toplam pazar büyümesini birleştirip satış adedindeki yüzde değişimi bulur.',kalip='grafik',
 kart='K-YZS-10 (pazar payı) · pay %20 → %30; pazar %20 büyüme',
 metin='Şekildeki çizgi grafikte, bir markanın bir ülkedeki televizyon pazarındaki payı yıllara göre verilmiştir. Bir markanın “pazar payı”, markanın satış adedinin ülkedeki toplam satış adedine oranıdır. Ülkedeki toplam satış adedi 2022’den 2024’e %20 artmıştır.\nBuna göre, markanın 2024 yılındaki satış adedi 2022 yılındakine göre yüzde kaç artmıştır?',
 dogru=v,yan=[(e[0],'Yüzde puan farkını (30 − 20) artış yüzdesi sanmış.','dikkat'),(e[1],'Yalnız pazarın büyümesini (%20) yazmış.','dikkat'),(e[2],'Yalnız payın artışını hesaplamış: (30 − 20) ÷ 20 = %50.','dikkat'),(e[3],'İki etkiyi toplamış: %50 + %20.','islem')],
 istenen='Satış adedinin 2022’ye göre artış yüzdesi.',ip=['Satış adedini, pay ile toplam pazarın çarpımı olarak yaz.'],bilgi=[YDG],sekil=SK,
 ad=[A('2022 satışı','Toplam pazar 100 birim alınır.','100 × %20 = 20'),A('2024 pazarı','Toplam pazar %20 büyür.','100 × 1,2 = 120'),A('2024 satışı','Yeni pay ile.','120 × %30 = 36'),A('Artış yüzdesi','Satışın değişimi.','(36 − 20) ÷ 20 = %80')],
 puf='Satış = pay × toplam pazar; ikisi de değişince çarpımsal etki oluşur.')

bitir(P,'yuzdesek','prob|Yüzde Problemleri')
