"""Yaş Problemleri · ŞEKİLLİ paket (7 soru): şekil/tablo/grafik çözüm verisini taşır; sayılar Python'da hesaplanır, her doğru ve çeldirici değer assert'lidir. Kardeş yok, ipucu 1."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Yaş Problemleri'
P=Parti('yassek','Yaş Problemleri','prob|Yaş Problemleri')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli/tablolu/grafikli yaş soruları; yalnız mantık) · MEB 8–9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)

ORT=B('Ortalama','aritmetik ortalama, değerlerin toplamının değer sayısına bölünmesidir; n kişi arasında n − 1 aralık vardır. Örnek: 4 kişi arasında 3 aralık bulunur')
YF=B('Yaş farkı','iki kişinin yaş farkı yıllar geçse de değişmez; her kişi her yıl 1 yaş büyür. Örnek: 5 yaş farkı olan iki kişi 10 yıl sonra yine 5 yaş farklıdır')
DY=B('Doğum yılından yaş','bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki farktır. Örnek: 1990’da doğan biri 2000’de 10 yaşındadır')
TY=B('Toplam yaş','n kişinin yaşları toplamı her yıl n artar; bu yüzden farklı kişi sayısına sahip gruplar farklı hızla yaşlanır. Örnek: 3 kişinin toplamı 4 yılda 12 artar')

kartla('K-YSS-01','Sütun grafiği ve toplam yaş','Sütunlardan yaşlar okunur, toplam bulunur; annenin yaşı toplamla ilişkilendirilir ve çocuğun doğduğu yaştaki anne yaşı yaş farkıyla bulunur.','Annenin yaşını sorulan yaş sanmak; toplama 4’ü eklemeyi unutmak; yanlış çocuğu seçmek.','kolay','grafik',4,'yss-grafik','Sütun grafiği ve yaş toplamı')
kartla('K-YSS-02','Soy ağacı ve doğum yılı','Doğum yıllarından yaş bulunur; iki kişinin yaşları toplanır.','Yaş yerine doğum yıllarını işleme sokmak; yanlış kişiyi seçmek.','kolay','hikâyeli',3,'yss-agac','Soy ağacı ve doğum yılı')
kartla('K-YSS-03','Zaman çizelgesi ve yaş farkının katı','Çizelgeden doğum yılları okunur; yıl t için yaşlar t − doğum yılı biçiminde yazılır ve verilen katsayı ilişkisi denklem olur.','Katı yanlış tarafa yazmak; yıl ile yaşı karıştırmak; yaşları toplamak yerine tek çocuğu almak.','orta','hikâyeli',4,'yss-zaman','Zaman çizelgesi ve yaş farkının katı')
kartla('K-YSS-04','Yaş tablosu','Tablodaki yaşlar bugüne çekilir; kişiler aynı hızla büyüdüğünden iki taraf arasındaki fark her yıl bir kapanır ya da açılır.','Tablodaki ham değerleri bugünkü yaş sanmak; farkı yıl başına yanlış hızla bölmek.','orta','tablo',4,'yss-tablo','Geçmiş–gelecek yaş tablosu')
kartla('K-YSS-05','Zaman çizelgesi ve yaş farkı','Çizelgedeki süreler doğumlar arasındaki yaş farkıdır; toplam fark, torun ile dedenin yaş farkını verir ve katı ilişkisi bunu torunun yaşına bağlar.','Farkı dedenin yaşı sanmak; bir yaş farkını yanlış kişiye eklemek.','orta','hikâyeli',4,'yss-fark','Zaman çizelgesi ve yaş farkı')
kartla('K-YSS-06','Farklı yıllarda verilmiş yaşlar','Bütün yaşlar aynı yıla çekilir; toplam yaşlar her yıl kişi sayısı kadar artar ve eşitlik denklemi kurulur.','Yaşları güncellemeden toplamak; çocuk sayısını yanlış almak; yılı yaş sanmak.','zor','tablo',5,'yss-yillar','Farklı yıllara ait yaşlar')
kartla('K-YSS-07','Aile şeması ve yaş farkları','Yol boyunca yaş farkları toplanır; iki torunun dede ile farkı eşit çıkar, böylece yaşları eşittir; toplamdan her birinin yaşı ve dedenin yaşı bulunur.','Farkı yaş sanmak; torunların eşit yaşta olduğunu görmeyip tek bir farkı kullanmak.','zor','hikâyeli',4,'yss-sema','Aile şeması ve yaş farkları')

# ================= 01 kolay · sütun grafiği =================
yaslar=[('Ada',5),('Bora',8),('Can',12),('Defne',15)]; top=sum(v for _,v in yaslar); anne=top+4; v=anne-5
e=[anne-15,anne-12,anne-8,anne]
assert top==40 and anne==44 and v==39 and e==[29,32,36,44] and len({v,*e})==5
o=[]; sx,sy=1.25,0.2
o.append(f'\\draw[-{{Stealth}}] (0,0) -- ({4*sx+0.4},0); \\draw[-{{Stealth}}] (0,0) -- (0,{17*sy:.2f}) node[above] {{Yaş}};')
for t in (5,10,15):
    o.append(f'\\draw[gray!50,dashed] (0,{t*sy:.2f}) -- ({4*sx+0.2},{t*sy:.2f}); \\draw (-0.07,{t*sy:.2f}) -- (0.07,{t*sy:.2f}); \\node[left=2pt] at (0,{t*sy:.2f}) {{{t}}};')
for i,(n,yy) in enumerate(yaslar):
    x=(i+0.5)*sx
    o.append(f'\\filldraw[fill=vurgu!25,draw=vurgu!80!black] ({x-0.38:.2f},0) rectangle ({x+0.38:.2f},{yy*sy:.2f}); \\node[above=1pt] at ({x:.2f},{yy*sy:.2f}) {{{yy}}}; \\node[below=2pt] at ({x:.2f},0) {{{n}}};')
SK=fig('\n'.join(o))
q('0001',tipId='yss-grafik',tip='Sütun grafiği ve yaş toplamı',z='kolay',alt='Sütun Grafiği ve Yaş Toplamı',kaz='Sütun grafiğinden yaşları okuyup toplam ve yaş farkı ilişkisiyle bir olayın yaşını bulur.',kalip='grafik',
 kart='K-YSS-01 (sütun grafiği) · toplam 40, anne 44, en küçük 5, en büyük 15',
 metin='Bir ailedeki dört kardeşin bugünkü yaşları şekildeki sütun grafikte verilmiştir. Bu kardeşlerin annesinin bugünkü yaşı, dört kardeşin yaşları toplamından 4 fazladır; kardeşler arasında ikiz yoktur.\nBuna göre, anne en küçük çocuğunu dünyaya getirdiğinde kaç yaşındaydı?',
 dogru=v,yan=[(e[0],'En büyük çocuğu (Defne) esas almış: 44 − 15.','dikkat'),(e[1],'Can’ı en küçük çocuk sanmış: 44 − 12.','dikkat'),(e[2],'Bora’yı en küçük çocuk sanmış: 44 − 8.','dikkat'),(e[3],'Annenin bugünkü yaşını (44) yazmış.','dikkat')],
 istenen='Anne, en küçük çocuğu doğurduğunda kaç yaşındaydı?',ip=['Önce sütunlardan dört kardeşin yaşlarını toplayıp annenin yaşını belirle; sonra en küçük çocuğun yaşını ayıkla.'],bilgi=[YF],sekil=SK,
 ad=[A('Yaşlar toplamı','Dört sütunun yüksekliği toplanır.','5 + 8 + 12 + 15 = 40'),A('Annenin yaşı','Toplamdan 4 fazladır.','40 + 4 = 44'),A('En küçük çocuk','Sütunlardan en küçük yaş okunur.','5 yaş'),A('Doğum anındaki yaş','Anne yaşından çocuğun yaşı çıkarılır; yaş farkı sabittir.','44 − 5 = 39')],
 puf='Annenin yaşı ile çocuğun yaşı arasındaki fark sabit kalır.')

# ================= 02 kolay · soy ağacı, kuşak aralığı (yeni nesil) =================
yn,ya,yt=1958,1984,2012; g1,g2=ya-yn,yt-ya; v=Fr(g1+g2,2)
e=[g1,g2,g1+g2,Fr(g1+g2,3)]
assert (g1,g2)==(26,28) and v==27 and e==[26,28,54,18] and len({v,*e})==5
o=[]
for i,(nm,yl) in enumerate([('Nine',yn),('Anne',ya),('Torun',yt)]):
    y0=-i*1.7
    o.append(f'\\node[draw,rounded corners=3pt,minimum width=3.4cm,minimum height=1.05cm,align=center,fill=vurgu!10] (n{i}) at (0,{y0}) {{\\textbf{{{nm}}}\\\\doğum yılı: {yl}}};')
o.append('\\draw[-{Stealth},thick] (n0.south) -- (n1.north); \\draw[-{Stealth},thick] (n1.south) -- (n2.north);')
SK=fig('\n'.join(o))
q('0002',tipId='yss-agac',tip='Soy ağacı ve doğum yılı',z='kolay',alt='Soy Ağacı ve Kuşak Aralığı',kaz='Soy ağacındaki doğum yıllarından kuşak aralıklarını bulup tanımlı ortalamayı hesaplar.',kalip='yeni nesil',
 kart='K-YSS-02 (soy ağacı) · 1958, 1984, 2012; kuşak aralığı ortalaması',
 metin='Bir ailedeki ardışık iki kuşağın bireylerinin doğum yılları arasındaki farka “kuşak aralığı”, bu aralıkların aritmetik ortalamasına da ailenin “ortalama kuşak aralığı” denir. Şekildeki soy ağacında bir ailenin nine, anne ve torununun doğum yılları verilmiştir.\nBuna göre, bu ailenin ortalama kuşak aralığı kaç yıldır?',
 dogru=v,yan=[(e[0],'Yalnız ilk kuşak aralığını (nine–anne) yazmış: 1984 − 1958.','dikkat'),(e[1],'Yalnız ikinci kuşak aralığını (anne–torun) yazmış: 2012 − 1984.','dikkat'),(e[2],'Aralıkların toplamını (54) ortalama sanmış.','dikkat'),(e[3],'Toplamı aralık sayısı (2) yerine kişi sayısına (3) bölmüş: 54 ÷ 3.','dikkat')],
 istenen='Ortalama kuşak aralığı (yıl).',ip=['Ağaçtaki iki ok, iki ayrı kuşak aralığına karşılık gelir; her birini doğum yıllarından bul.'],bilgi=[ORT],sekil=SK,
 ad=[A('Birinci aralık','Nine ile anne.','1984 − 1958 = 26'),A('İkinci aralık','Anne ile torun.','2012 − 1984 = 28'),A('Ortalama','İki aralığın ortalaması alınır.','(26 + 28) ÷ 2 = 27')],
 puf='Üç kişi arasında iki aralık vardır.')

# ================= 03 orta · zaman çizelgesi, yaş farkının katı =================
a,b,c=1980,2014,2018; fk=c-b; kat=12; t=a+kat*fk; v=t-b
assert fk==4 and t==2028 and v==14 and t-c==10
e=[fk,t-c,2026-b,t-a]
assert e==[4,10,12,48] and len({v,*e})==5
sc=0.165; X=lambda yy:(yy-1975)*sc
o=[f'\\draw[-{{Stealth}},thick] (-0.2,0) -- ({X(2024)+0.2:.2f},0) node[below right] {{yıl}};']
for nm,yy,pos in [('Anne doğdu',a,'above'),('Kız doğdu',b,'above'),('Oğul doğdu',c,'below')]:
    o.append(f'\\fill[vurgu] ({X(yy):.2f},0) circle (0.09); \\draw[thin] ({X(yy):.2f},0) -- ({X(yy):.2f},{0.55 if pos=="above" else -0.55});')
    o.append(f'\\node[{pos}=5pt,align=center] at ({X(yy):.2f},{0.5 if pos=="above" else -0.5}) {{{nm}\\\\\\textbf{{{yy}}}}};')
SK=fig('\n'.join(o))
q('0003',tipId='yss-zaman',tip='Zaman çizelgesi ve yaş farkının katı',z='orta',alt='Zaman Çizelgesi ve Yaş Farkı',kaz='Zaman çizelgesindeki doğum yıllarından çocukların yaş farkını bulup bu farkın katı olan anne yaşından ilgili yılı ve yaşı hesaplar.',kalip='hikâyeli',
 kart='K-YSS-03 (zaman çizelgesi) · 1980, 2014, 2018; anne = 12 × çocukların yaş farkı',
 metin='Şekildeki zaman çizelgesinde bir annenin ve iki çocuğunun doğum yılları işaretlenmiştir. Bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki fark olarak alınmaktadır. İleride bir yılda annenin yaşı, iki çocuğun o yıldaki yaşları arasındaki farkın tam 12 katı olacaktır.\nBuna göre, o yıl kız kaç yaşında olacaktır?',
 dogru=v,yan=[(e[0],'Çocukların yaş farkını (4) kızın yaşı sanmış.','dikkat'),(e[1],'Kız yerine oğulun o yıldaki yaşını bulmuş: 2028 − 2018.','dikkat'),(e[2],'Kızın 2026’daki yaşını yazmış: 2026 − 2014.','dikkat'),(e[3],'Annenin o yıldaki yaşını (48) yazmış.','dikkat')],
 istenen='O yıl kızın yaşı.',ip=['Çocukların yaş farkı yıllar geçse de değişmez; önce bu farkı doğum yıllarından bul.'],bilgi=[YF],sekil=SK,
 ad=[A('Yaş farkı','Çocukların doğum yılları farkı.','2018 − 2014 = 4'),A('Annenin yaşı','Fark 12 katı olacak.','12 × 4 = 48'),A('Yıl','Annenin doğum yılına yaşı eklenir.','1980 + 48 = 2028'),A('Kızın yaşı','Yıldan kızın doğum yılı çıkarılır.','2028 − 2014 = 14')],
 puf='İki kişinin yaş farkı hiçbir zaman değişmez.')

# ================= 04 orta · yaş tablosu, kat ilişkisi =================
an5,ki7=31,15; anne=an5+5; kiz=ki7-7; v=anne-2*kiz
assert (anne,kiz,v)==(36,8,20) and anne+v==2*(kiz+v)
e=[anne-2*ki7,an5-2*kiz,anne-kiz,anne]
assert e==[6,15,28,36] and len({v,*e})==5
SK=tablo_svg(['Kişi','5 yıl önceki yaşı','7 yıl sonraki yaşı'],[['Anne',str(an5),'—'],['Kız','—',str(ki7)]])
q('0004',tipId='yss-tablo',tip='Geçmiş–gelecek yaş tablosu',z='orta',alt='Geçmiş–Gelecek Yaş Tablosu',kaz='Farklı zamanlara ait tablo verilerini bugüne taşıyıp bir yaşın diğerinin katı olacağı süreyi bulur.',kalip='tablo',
 kart='K-YSS-04 (yaş tablosu) · anne 31 (5 yıl önce); kız 15 (7 yıl sonra)',
 metin='Aşağıdaki tabloda bir annenin ve kızının farklı zamanlardaki yaşlarından bazıları verilmiştir; “—” işareti bilginin verilmediği anlamına gelmektedir. Tablodaki “5 yıl önceki” ve “7 yıl sonraki” ifadeleri bugüne göredir ve herkes her yıl bir yaş büyümektedir.\nBuna göre, kaç yıl sonra annenin yaşı kızının yaşının 2 katı olur?',
 dogru=v,yan=[(e[0],'Kızın yaşını güncellememiş (15), anneyi güncellemiş: 36 + t = 2(15 + t).','dikkat'),(e[1],'Annenin yaşını güncellememiş (31), kızı güncellemiş: 31 + t = 2(8 + t).','dikkat'),(e[2],'Bugünkü yaş farkını (28) süre sanmış.','dikkat'),(e[3],'Annenin bugünkü yaşını (36) süre sanmış.','dikkat')],
 istenen='Koşulun sağlandığı süre (yıl).',ip=['Tablodaki iki değeri de bugüne taşı; t yıl sonra iki yaşı t cinsinden yazıp katı koşulunu denklem yap.'],bilgi=[TY],sekil=SK,
 ad=[A('Bugünkü yaşlar','Anne 5 yıl ileri, kız 7 yıl geri taşınır.','anne 36, kız 8'),A('Denklem','t yıl sonra anne = 2 × kız.','36 + t = 2(8 + t)'),A('Çöz','t yalnız bırakılır.','36 − 16 = t'),A('Süre','Sonuç.','t = 20 yıl')],
 puf='Önce herkesi bugüne taşı; sonra t yıl sonraki yaşları yaz.')

# ================= 05 orta · zaman çizelgesi, yaş farkı =================
f1,f2=26,34; fark=f1+f2; k=6; tor=Fr(fark,k-1); baba=tor+f2; dede=tor*k
assert tor==12 and baba==46 and dede==72 and dede-tor==60
v=baba; e=[tor+f1, Fr(fark,k)+f2, fark, dede]
assert e==[38,44,60,72] and len({v,*e})==5
sc=0.11; o=[f'\\draw[-{{Stealth}},thick] (-0.3,0) -- ({(f1+f2)*sc+0.7:.2f},0) node[above right] {{zaman}};']
for nm,x in [('Dede doğdu',0),('Baba doğdu',f1*sc),('Torun doğdu',(f1+f2)*sc)]:
    o.append(f'\\fill[vurgu] ({x:.2f},0) circle (0.1); \\node[below=5pt,align=center] at ({x:.2f},0) {{{nm}}};')
o.append(f'\\draw[<->] (0,0.5) -- ({f1*sc:.2f},0.5) node[midway,above] {{{f1} yıl}}; \\draw[<->] ({f1*sc:.2f},0.5) -- ({(f1+f2)*sc:.2f},0.5) node[midway,above] {{{f2} yıl}};')
SK=fig('\n'.join(o))
q('0005',tipId='yss-fark',tip='Zaman çizelgesi ve yaş farkı',z='orta',alt='Zaman Çizelgesi ve Yaş Farkı',kaz='Zaman çizelgesindeki doğum aralıklarını yaş farkı olarak toplayıp katı ilişkisiyle yaşları bulur.',kalip='hikâyeli',
 kart='K-YSS-05 (zaman çizelgesi) · 26 ve 34 yıl; dede = 6 × torun',
 metin='Bir aile, aile albümü için şekildeki zaman çizelgesini hazırlamıştır; çizelgede dede, baba ve torunun doğumları arasında geçen süreler gösterilmiştir. Bugün dedenin yaşı, torunun yaşının 6 katıdır.\nBuna göre, baba bugün kaç yaşındadır?',
 dogru=v,yan=[(e[0],'Torunun yaşına dede ile baba arasındaki farkı eklemiş: 12 + 26.','dikkat'),(e[1],'Dede–torun farkını 6’ya bölüp baba–torun farkını eklemiş: 60 ÷ 6 + 34.','islem'),(e[2],'Dede ile torun arasındaki yaş farkını (60) babanın yaşı sanmış.','dikkat'),(e[3],'Dedenin yaşını (72) yazmış.','dikkat')],
 istenen='Babanın bugünkü yaşı.',ip=['Dede ile torunun yaş farkını iki süreyi toplayarak bul; dedenin yaşı torunun kaç katı?'],bilgi=[YF],sekil=SK,
 ad=[A('Dede–torun farkı','İki süre toplanır.','26 + 34 = 60 yıl'),A('Torunun yaşı','Dede = 6 × torun ise fark torunun 5 katıdır.','5 × torun = 60 ⇒ torun = 12'),A('Baba–torun farkı','Çizelgeden okunur.','34 yıl'),A('Babanın yaşı','Torunun yaşına bu fark eklenir.','12 + 34 = 46')],
 puf='Katı ilişkisi bilinen bir fark ile yaşı birbirine bağlar.')

# ================= 06 zor · farklı yıllarda verilmiş yaşlar =================
PA=[('Anne',38,2020),('Baba',42,2018)]; KD=[('Ece',12,2024),('Mert',9,2022),('Zeynep',2,2022)]
def g(l,eski=()): return sum(a+(0 if n in eski else 2026-y) for n,a,y in l)
p0,k0=g(PA),g(KD); assert (p0,k0)==(94,33) and (p0-2*k0)%4==0
x=(p0-2*k0)//4; assert x==7; v=2026+x
def yil(eski_p=(),eski_k=(),nk=3):
    pp=g(PA,eski_p); kk=g(KD,eski_k)
    return pp,kk
pp,kk=g(PA,('Baba',)),k0; xb=Fr(pp-2*kk,4); assert xb==5
pp,kk=p0,g(KD,('Ece',)); xe=Fr(pp-2*kk,4); assert xe==8
kk=g(KD,('Ece','Mert','Zeynep')); xh=Fr(p0-2*kk,4); assert xh==12
kk=33-6; xz=Fr(p0-2*kk,4); assert xz==10
e=[2026+xb,2026+xe,2026+xz,2026+xh]; assert e==[2031,2034,2036,2038]
SK=tablo_svg(['Kişi','Yaşı','Yaşın verildiği yıl'],[[n,str(a),str(y)] for n,a,y in PA+KD])
q('0006',tipId='yss-yillar',tip='Farklı yıllara ait yaşlar',z='zor',alt='Farklı Yıllara Ait Yaşlar',kaz='Farklı yıllarda verilmiş yaşları ortak yıla çekip toplam yaşlar arasındaki katı ilişkisinin sağlandığı yılı bulur.',kalip='tablo',
 kart='K-YSS-06 (farklı yıllarda yaşlar) · 2026’da ebeveynler 94, çocuklar 33',
 metin='Bir ailenin bireylerinin yaşları, farklı yıllarda öğrenilmiş ve aşağıdaki tabloda verilmiştir. Bir kişinin yaşı, bulunulan yıl ile doğum yılı arasındaki fark olarak alınmaktadır. 2026 yılında anne ile babanın yaşları toplamı, üç çocuğun yaşları toplamının 2 katından fazladır; ancak ileride bir yıl bu toplam tam 2 katına eşit olacaktır.\nBuna göre, bu eşitlik hangi yılda sağlanır?',
 dogru=v,yan=[(e[0],'Babanın yaşını 2026’ya taşımamış (42): 86 + 2x = 2(33 + 3x) ⇒ x = 5.','dikkat'),(e[1],'Ece’nin yaşını güncellememiş (12): çocukların toplamı 31 çıkmış ve x = 8 bulmuş.','dikkat'),(e[2],'Zeynep’i başlangıç toplamından çıkarmış (27) ama yıllık artışı yine 3 almış: 94 + 2x = 2(27 + 3x) ⇒ x = 10.','dikkat'),(e[3],'Çocukların yaşlarını güncellememiş (12 + 9 + 2 = 23): x = 12.','dikkat')],
 istenen='Eşitliğin sağlandığı yıl.',ip=['Tüm yaşları aynı yıla taşıdıktan sonra iki grubun toplamlarının yılda ne kadar arttığını karşılaştır.'],bilgi=[TY],sekil=SK,
 ad=[A('Yaşları 2026’ya taşı','Her yaşa, verildiği yıldan 2026’ya geçen süre eklenir.','anne 44, baba 50, Ece 14, Mert 13, Zeynep 6'),A('Toplamlar','Ebeveynler ve çocuklar ayrı toplanır.','94 ve 33'),A('Yıllık artış','Ebeveyn toplamı yılda 2, çocuk toplamı yılda 3 artar.','94 + 2x = 2(33 + 3x)'),A('Çöz','Denklemden x bulunur.','28 = 4x ⇒ x = 7'),A('Yılı yaz','2026’ya eklenir.','2026 + 7 = 2033')],
 puf='Toplam yaş, kişi sayısı kadar hızla artar; ortak yıla çekmeden toplama yapma.')

# ================= 07 zor · aile şeması =================
d1,d2,s1,s2=29,33,31,27; assert d1+s1==d2+s2==60; ec=38//2; v=ec+60
assert v==79 and ec==19
e=[ec+d1,ec+s1,60,38]; assert e==[48,50,60,38]
o=[]
N={'D':(0,0,'Dede'),'B':(-2.5,-2.0,'Baba'),'A':(2.5,-2.0,'Amca'),'E':(-2.5,-4.0,'Elif'),'C':(2.5,-4.0,'Can')}
for kx,(x,y,nm) in N.items(): o.append(f'\\node[draw,rounded corners=3pt,minimum width=1.7cm,minimum height=0.7cm,fill=vurgu!10] ({kx}) at ({x},{y}) {{{nm}}};')
for a_,b_,val,side in [('D','B',d1,'left'),('D','A',d2,'right'),('B','E',s1,'left'),('A','C',s2,'right')]:
    o.append(f'\\draw[-{{Stealth}},thick] ({a_}.south) -- ({b_}.north) node[midway,above {side}=1pt,inner sep=2pt] {{{val}}};')
SK=fig('\n'.join(o))
q('0007',tipId='yss-sema',tip='Aile şeması ve yaş farkları',z='zor',alt='Aile Şeması ve Yaş Farkları',kaz='Aile şemasındaki yaş farklarını toplayarak iki kişinin yaşlarının eşit olduğunu görüp dedenin yaşını bulur.',kalip='hikâyeli',
 kart='K-YSS-07 (aile şeması) · 29+31 = 33+27 = 60; Elif + Can = 38',
 metin='Şekildeki aile şemasında dedenin iki oğlu ve bu oğulların birer çocuğu gösterilmiştir. Bir okun üzerindeki sayı, ok başındaki kişinin ok ucundaki kişiden kaç yaş büyük olduğunu göstermektedir. Elif ile Can’ın bugünkü yaşları toplamı 38’dir.\nBuna göre, dede bugün kaç yaşındadır?',
 dogru=v,yan=[(e[0],'Elif’e yalnız dede ile baba arasındaki farkı eklemiş: 19 + 29.','dikkat'),(e[1],'Babanın yaşını (19 + 31) dedenin yaşı sanmış.','dikkat'),(e[3],'Elif ile Can’ın yaşları toplamını (38) dedenin yaşı sanmış.','dikkat'),(e[2],'Dede ile torun arasındaki farkı (60) dedenin yaşı sanmış.','dikkat')],
 istenen='Dedenin bugünkü yaşı.',ip=['Dededen Elif’e ve dededen Can’a giden yollardaki yaş farklarını ayrı ayrı topla.'],bilgi=[YF],sekil=SK,
 ad=[A('Dede–Elif farkı','Baba üzerinden iki fark toplanır.','29 + 31 = 60'),A('Dede–Can farkı','Amca üzerinden iki fark toplanır.','33 + 27 = 60'),A('Elif ile Can','Farklar eşit olduğundan yaşları eşittir.','2 × Elif = 38 ⇒ Elif = 19'),A('Dedenin yaşı','Elif’in yaşına 60 eklenir.','19 + 60 = 79')],
 puf='Aynı kişiden iki farklı yolla ulaşan farklar eşit çıkabilir.')

bitir(P,'yassek','prob|Yaş Problemleri')
