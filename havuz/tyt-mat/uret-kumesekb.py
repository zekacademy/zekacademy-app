"""Kümeler ve Kartezyen Çarpım · ŞEKİLLİ ek paket (kumesekb): 10 soru (Venn, kesişim/birleşim); şekil veri taşır; her doğru ve çeldirici değer Python'da hesaplanıp assert edilir. Kardeş yok, ipucu 1."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import _hafif_mat as H
from _hafif_mat import *
from cizim import tikz_svg
H.KONU='Kümeler ve Kartezyen Çarpım'
P=Parti('kumesekb','Kümeler ve Kartezyen Çarpım','matd|Kümeler-Kartezyen Çarpım')
KY='ÖSYM 2018–2026 TYT Matematik (şekilli Venn ve küme problemleri; yalnız mantık) · MEB 9. sınıf'
def q(no,ad,**k): mk(P,no,ad=ad,adim=len(ad),**k)
def fig(body): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'+body+'\n\\end{tikzpicture}')
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def tx(x,y,t,st=''): return f'\\node[{st}] at ({x:.3f},{y:.3f}) {{{t}}};'
def ln(x1,y1,x2,y2,st=''): return f'\\draw[{st}] ({x1:.3f},{y1:.3f}) -- ({x2:.3f},{y2:.3f});'

KES=B('Kesir ve eleman sayısı','evrensel kümenin elemanları bölgelere ayrıldığında bölgelerin kesirleri toplamı 1’dir; bir bölgenin eleman sayısı, kesri ile evrensel kümenin eleman sayısının çarpımıdır. Örnek: 40 kişilik grupta 1/4’lük bölgede 10 kişi vardır')
IIC=B('İç içe kümeler','A ⊂ B ise A’nın tüm elemanları B’dedir; B \\ A, B’de olup A’da olmayan elemanlardır ve s(B \\ A) = s(B) − s(A)’dır. Örnek: s(A) = 3, s(B) = 8 ise s(B \\ A) = 5’tir')
UCV=B('Üç kümeli Venn','her bölgenin eleman sayıları toplanınca evrensel kümenin eleman sayısı bulunur; bir kümenin eleman sayısı, o dairenin içindeki dört bölgenin toplamıdır. Örnek: yalnız A 3, A ∩ B (yalnız) 2, A ∩ C (yalnız) 4, üçü birden 1 ise s(A) = 3 + 2 + 4 + 1 = 10’dur')
SER=B('Şerit modelde kesişim','iki kümenin şeritleri ortak kutular üzerinde üst üste çizilir; ortak kutular kesişimi gösterir ve birleşimdeki kutu sayısı, iki şeridin kutu sayısının toplamından ortak kutuların bir kez çıkarılmasıyla bulunur. Örnek: 5 ve 4 kutu, 2 ortak kutu ise birleşim 7 kutudur')
BIR=B('Birleşim ve kesişim','s(A ∪ B) = s(A) + s(B) − s(A ∩ B); yalnız bir kümede bulunanlar s(A ∪ B) − s(A ∩ B) kadardır. Örnek: s(A) = 6, s(B) = 5, s(A ∪ B) = 9 ise s(A ∩ B) = 2’dir')
DEG=B('Üyelik değişimi','bir kişi bir kümeden ayrılıp başka kümeye katılınca yalnız o iki bölgenin sayıları değişir; kişi bölge değiştirir, toplam öğrenci sayısı değişmez. Örnek: yalnız A’daki bir kişi B’ye de katılırsa “yalnız A” bölgesi 1 azalır, “A ve B” bölgesi 1 artar')
TOP=B('Daire toplamları','bir dairenin toplamı, içindeki dört bölgenin toplamıdır; yalnız o kümeye ait bölge, daire toplamından diğer üç bölgenin çıkarılmasıyla bulunur. Örnek: A’nın toplamı 10, A ∩ B (yalnız) 2, A ∩ C (yalnız) 3, üçü birden 1 ise yalnız A 10 − 2 − 3 − 1 = 4’tür')
YUZ=B('Yüzde ve Venn','iki kümenin yüzdeleri toplamından birleşimin yüzdesi çıkarılırsa kesişimin yüzdesi bulunur; bir yüzdenin eleman sayısı, yüzde ile evrensel kümenin çarpımıdır. Örnek: %60 ve %50 üye, hiçbirine üye olmayan %10 ise ikisine de üye olan %60 + %50 − %90 = %20’dir')
BIRL=B('Kümelerin birleştirilmesi','iki ayrı grup birleşince aynı bölgelerin sayıları toplanır. Örnek: bir grupta “hiçbirine üye değil” bölgesi 3, ötekinde 5 ise birleşik grupta bu bölge 8’dir')

kartla('K-KVB-01','Kesirli Venn bölgeleri','Bölgelerin kesirleri toplamı 1’dir; boş kalan bölgenin kesri bulunup evrensel kümeyle çarpılır.','Kesirleri toplamayı unutmak; birleşimi hesaplayıp dışarıyı almamak.','kolay','şekilli',3,'kvb-kesir','Kesirli Venn bölgeleri')
kartla('K-KVB-02','İç içe kümeler','İç içe dairelerde farklar alınarak halkalardaki sayılar bulunur.','Halka yerine dairenin tamamını almak.','kolay','şekilli',3,'kvb-ic','İç içe kümeler ve farklar')
kartla('K-KVB-03','Üç kümeli Venn ve bilinmeyen','Bölgelerdeki ifadeler toplamı evrensel kümeyi verir; denklemden x bulunup istenen bölgeler toplanır.','Bir bölgeyi iki kez saymak; dışarıdaki bölgeyi unutmak.','orta','şekilli',4,'kvb-uc','Üç kümeli Venn’de cebirsel bölgeler')
kartla('K-KVB-04','Şerit modelde kesişim','Ortak kutu sayısı kesişimi, birleşimdeki kutu sayısı toplam kişi sayısını verir; bir kutunun değeri bulunur.','Ortak kutuları iki kez saymak; kutu değerini bulmadan sayıları yazmak.','orta','şekilli',4,'kvb-serit','Şerit modelde kesişim ve birleşim')
kartla('K-KVB-05','Sütun grafiğinden küme sayıları','Sütunlardan s(A), s(B), s(A ∪ B) okunur; kesişim bulunup yalnız bir kümedekiler hesaplanır.','Birleşimi toplam sanmak; kesişimi iki kez çıkarmak.','orta','grafik',4,'kvb-sutun','Sütun grafiğinden kesişim ve yalnız bir küme')
kartla('K-KVB-06','İsimli Venn ve üyelik değişimi','İsimler sayılarak bölge sayıları bulunur; kişilerin geçişleri bölge sayılarını değiştirir.','Geçişi yalnız bir bölgede işlemek; kişiyi iki kez saymak.','orta','şekilli',4,'kvb-isim','İsimli Venn ve üyelik değişimi')
kartla('K-KVB-07','Daire toplamlı üç kümeli Venn','Dairelerin toplamları ve ikili bölgelerden yalnız bir kümedekiler ile üçlü kesişim denklemle bulunur.','Üçlü kesişimi sıfır sanmak; ikili bölgeleri iki kez saymak.','zor','şekilli',5,'kvb-toplam','Daire toplamları ve üçlü kesişim')
kartla('K-KVB-08','Yüzdeli Venn','Yüzdelerden kesişim ve yalnız bölgeler bulunur; evrensel kümeyle çarpılıp kesirle çarpılır.','Yüzdeleri toplam sanmak; kesişimi çıkarmamak.','orta','şekilli',5,'kvb-yuzde','Yüzdeli Venn ve kesirli alt grup')
kartla('K-KVB-09','İki bilinmeyenli Venn','Toplam ve bir dairenin toplamı için iki denklem yazılır, x ve y bulunur, istenen küme toplanır.','Bir denklemi eksik yazmak; üçlü kesişimi atlamak.','zor','şekilli',5,'kvb-iki','İki bilinmeyenli üç kümeli Venn')
kartla('K-KVB-10','İki Venn şemasını birleştirme','Her sınıftaki bölgeler bulunur, aynı bölgeler toplanır; istenen bölge birleşik gruptan okunur.','Sınıfların bölgelerini karıştırmak; tamamlayıcı bölgeyi seçmek.','zor','şekilli',5,'kvb-birles','İki Venn şemasını birleştirme')

# çizim yardımcıları
def venn2(a,ab,b,out,ra=1.1,dx=.7,w=4.4,h=2.7,fs='\\small',na='A',nb='B',ya=None,yb=None):
    o=[f'\\draw[line width=1.1pt] (-{w/2},-{h/2}) rectangle ({w/2},{h/2});',f'\\draw[line width=1.1pt] (-{dx},0) circle ({ra});',f'\\draw[line width=1.1pt] ({dx},0) circle ({ra});']
    o+=[tx(-dx-.55,0,a),tx(0,0,ab),tx(dx+.55,0,b),tx(w/2-.4,-h/2+.3,out),tx(-dx-.3,ra+.28,f'\\textbf{{{na}}}'),tx(dx+.3,ra+.28,f'\\textbf{{{nb}}}')]
    return o
def venn3(vals,ra=1.15,names=('A','B','C'),w=5.0,h=4.2,fs='',koşe=False):
    # vals: dict aa,bb,cc,ab,ac,bc,abc,out
    cA=(-.65,.45); cB=(.65,.45); cC=(0,-.65)
    o=[f'\\draw[line width=1.1pt] (-{w/2},-{h/2}) rectangle ({w/2},{h/2});']
    for c in (cA,cB,cC): o.append(f'\\draw[line width=1.1pt] ({c[0]},{c[1]}) circle ({ra});')
    pos={'aa':(-1.2,.8),'bb':(1.2,.8),'cc':(0,-1.35),'ab':(0,1.0),'ac':(-.62,-.15),'bc':(.62,-.15),'abc':(0,.2),'out':(w/2-.45,-h/2+.3)}
    for k,(x,y) in pos.items():
        if k in vals: o.append(tx(x,y,str(vals[k])))
    o+=[tx(cA[0]-.85,cA[1]+1.0,f'\\textbf{{{names[0]}}}'),tx(cB[0]+.85,cB[1]+1.0,f'\\textbf{{{names[1]}}}'),tx(cC[0]+1.05,cC[1]-.95,f'\\textbf{{{names[2]}}}')]
    if koşe: o[-3:]=[tx(-w/2+.85,h/2-.35,f'\\textbf{{{names[0]}}}'),tx(w/2-.85,h/2-.35,f'\\textbf{{{names[1]}}}'),tx(-w/2+.85,-h/2+.35,f'\\textbf{{{names[2]}}}')]
    return o

# ---------- 01 kesirli Venn ----------
E1=60; fa,fab,fb=Fr(1,5),Fr(1,10),Fr(3,10); fo=1-fa-fab-fb; d1=fo*E1; assert (fo,d1)==(Fr(2,5),24)
e1=[fa*E1,fab*E1,fb*E1,(fa+fab+fb)*E1]; assert e1==[12,6,18,36] and len({d1,*e1})==5
SK=fig('\n'.join(venn2('$\\frac{1}{5}$','$\\frac{1}{10}$','$\\frac{3}{10}$','?',ra=1.1,dx=.7,w=4.8,h=3.4,na='Satranç',nb='Bulmaca')))
q('0001',tipId='kvb-kesir',tip='Kesirli Venn bölgeleri',z='kolay',alt='Venn Şeması',kaz='Venn şemasında bölgelerin kesirlerinden boş kalan bölgenin kesrini bulup evrensel kümenin eleman sayısıyla çarpar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-01 (kesirli Venn) · 60 öğrenci; dışarısı 2/5',
 metin='Bir okulda satranç ve bulmaca kulüplerine üye olan öğrencilerin, tüm öğrencilere oranları yukarıdaki Venn şemasında kesirlerle gösterilmiştir. Şemadaki evrensel küme 60 kişilik bir öğrenci grubudur; kesirler bu gruba oranlanmıştır ve dışarıdaki bölgenin oranı verilmemiştir.\nBuna göre kulüplerin hiçbirine üye olmayan öğrenci kaç kişidir?',
 dogru=int(d1),yan=[(6,'Yalnızca iki kulübe birden üye olanların sayısını (60 × 1/10) yazmış.','dikkat'),(12,'Yalnız satranç kulübüne üye olanların sayısını (60 × 1/5) yazmış.','dikkat'),(18,'Yalnız bulmaca kulübüne üye olanların sayısını (60 × 3/10) yazmış.','dikkat'),(36,'Kulüplerden en az birine üye olanların sayısını (60 × 6/10) bulup dışarıyı almamış.','dikkat')],
 istenen='Hiçbir kulübe üye olmayan öğrenci sayısı.',
 ip=['Şemadaki üç bölgenin kesirlerini topla; bütünün 1 olduğunu kullan.'],
 bilgi=[KES],
 ad=[A('Kesirleri topla','Şemadaki üç bölgenin kesirleri toplanır.','1/5 + 1/10 + 3/10 = 6/10'),A('Dışarıyı bul','Bütün 1 olduğundan dışarıdaki bölgenin kesri kalan kısımdır.','1 − 6/10 = 4/10 = 2/5'),A('Kişi sayısı','Kesir, evrensel kümenin eleman sayısıyla çarpılır.','60 × 2/5 = 24')],
 puf='Bütün gruba oranlar toplamı 1 olacak biçimde dışarıdaki bölgenin kesrini bul; kişi sayısına çevir.')

# ---------- 02 iç içe kümeler ----------
sA,sB,sC=8,20,35; d2=(sB-sA)+(sC-sB); assert d2==27
e2=[sB-sA,sC-sB,sC,sB+sC]; assert e2==[12,15,35,55] and len({d2,*e2})==5
o=['\\draw[line width=1.1pt] (-2.7,-2.2) rectangle (2.7,2.2);']
for (r,y,n,v,ty) in [(1.9,0,'C',sC,1.45),(1.3,-.6,'B',sB,.25),(.7,-1.2,'A',sA,-1.2)]:
    o.append(f'\\draw[line width=1.1pt] (0,{y}) circle ({r});'); o.append(tx(0,ty,f'$s({n})={v}$','font=\\footnotesize'))
SK=fig('\n'.join(o))
q('0002',tipId='kvb-ic',tip='İç içe kümeler ve farklar',z='kolay',alt='Venn Şeması',kaz='İç içe kümelerin eleman sayılarının farklarıyla halkalardaki eleman sayılarını bulur.',kalip='şekilli',sekil=SK,
 kart='K-KVB-02 (iç içe kümeler) · s(A)=8, s(B)=20, s(C)=35',
 metin='Bir müzik okulunda piyano çalanlar A, herhangi bir müzik aleti çalanlar B, müzik kulübüne üye olanlar C kümesiyle gösterilmiş; kümelerin eleman sayıları yukarıdaki şemada verilmiştir. Piyano çalan herkes bir müzik aleti çalmakta, müzik aleti çalan herkes de kulübe üyedir.\nBuna göre müzik aleti çalıp piyano çalmayanların sayısı ile kulübe üye olup hiçbir müzik aleti çalmayanların sayısının toplamı kaçtır?',
 dogru=d2,yan=[(12,'Yalnızca müzik aleti çalıp piyano çalmayanların sayısını (20 − 8) bulmuş.','dikkat'),(15,'Yalnızca kulübe üye olup müzik aleti çalmayanların sayısını (35 − 20) bulmuş.','dikkat'),(35,'Kulübün tamamını, yani C kümesinin eleman sayısını yazmış.','dikkat'),(55,'İki dairenin toplam eleman sayılarını toplamış: 20 + 35.','islem')],
 istenen='İki halkadaki öğrenci sayılarının toplamı.',
 ip=['İç içe dairelerde her halkanın eleman sayısını, büyük dairenin sayısından küçüğünü çıkararak bul.'],
 bilgi=[IIC],
 ad=[A('B halkası','B’de olup A’da olmayanlar.','20 − 8 = 12'),A('C halkası','C’de olup B’de olmayanlar.','35 − 20 = 15'),A('Topla','İki halkadaki öğrenciler toplanır.','12 + 15 = 27')],
 puf='Her halka, büyük dairenin eleman sayısından içindeki dairenin eleman sayısı çıkarılarak bulunur.')

# ---------- 03 üç kümeli Venn, bilinmeyen ----------
E3=40; xs=Fr(E3-20,4); assert xs==5
v3=dict(aa=xs,bb=xs+2,cc=2*xs,ab=4,ac=3,bc=5,abc=2,out=4); assert sum(v3.values())==E3
d3=v3['aa']+v3['bb']+v3['ab']+v3['ac']+v3['bc']+v3['abc']; assert d3==26
sa=v3['aa']+v3['ab']+v3['ac']+v3['abc']; sb=v3['bb']+v3['ab']+v3['bc']+v3['abc']
x6=Fr(E3-16,4); v6=dict(v3,aa=x6,bb=x6+2,cc=2*x6); e3a=v6['aa']+v6['bb']+v6['ab']+v6['ac']+v6['bc']+v6['abc']
e3=[e3a,sa+sb,v3['aa']+v3['bb']+v3['ab'],E3-v3['cc']]; assert e3==[28,32,16,30] and len({d3,*e3})==5
SK=fig('\n'.join(venn3(dict(aa='$x$',bb='$x+2$',cc='$2x$',ab=4,ac=3,bc=5,abc=2,out=4))))
q('0003',tipId='kvb-uc',tip='Üç kümeli Venn’de cebirsel bölgeler',z='orta',alt='Venn Şeması',kaz='Üç kümeli Venn şemasında bölgelerin toplamından bilinmeyeni bulup istenen bölgelerin toplamını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-03 (üç kümeli Venn) · x, x+2, 2x; E=40; s(A∪B)=26',
 metin='Bir okulda 40 öğrencinin A, B ve C kulüplerine üyeliği yukarıdaki Venn şemasında gösterilmiştir; her bölgedeki sayı, o bölgede bulunan öğrenci sayısıdır. Şemada üç kulüpten hiçbirine üye olmayanlar da bulunmaktadır.\nBuna göre A veya B kulübüne üye olan öğrenci sayısı kaçtır?',
 dogru=int(d3),yan=[(28,'Dışarıdaki bölgeyi toplama katmayıp x = 6 bulmuş.','dikkat'),(32,'s(A) ile s(B)’yi toplamış; ortak bölgeleri iki kez saymış.','dikkat'),(16,'Yalnız A, yalnız B ve yalnız A ∩ B bölgelerini toplamış.','dikkat'),(30,'Toplamdan yalnız C bölgesini (40 − 10) çıkarmış; hiçbirine üye olanları da saymış.','dikkat')],
 istenen='A veya B kulübüne üye olan öğrenci sayısı.',
 ip=['Bütün bölgelerin toplamı 40’tır; dışarıdaki bölgeyi de say.'],
 bilgi=[UCV],
 ad=[A('Denklem','Tüm bölgelerin toplamı evrensel kümeyi verir.','x + (x + 2) + 2x + 4 + 3 + 5 + 2 + 4 = 40'),A('x bul','Toplam sadeleştirilir.','4x + 20 = 40 → x = 5'),A('Bölgeler','Yalnız A 5, yalnız B 7, yalnız C 10.','5; 7; 10'),A('A ∪ B','C’ye ait olmayan bölgeler ve C ile kesişen kısımlar toplanır.','5 + 7 + 4 + 3 + 5 + 2 = 26')],
 puf='C’de olmayıp dışarıdan da ayrı tutulan bölgeleri çıkar; A ∪ B’ye giren altı bölgeyi topla.')

# ---------- 04 şerit model ----------
nA,nB,nO=7,5,2; blok=nA+nB-nO; U=120; v=Fr(U,blok); assert blok==10 and v==12
d4=(nA-nO+nB-nO)*v; assert d4==96
e4=[nA*v,nB*v,(nA-nO+nB-nO)*Fr(U,nA+nB),nO*v]; assert e4==[84,60,80,24] and len({d4,*e4})==5
cw=.55; o=[]
for i in range(nA): o.append(f'\\filldraw[fill={"vurgu!35" if i>=5 else "white"},line width=.9pt] ({i*cw},.65) rectangle ({i*cw+cw},{.65+cw});')
for i in range(5,5+nB): o.append(f'\\filldraw[fill={"vurgu!35" if i<7 else "white"},line width=.9pt] ({i*cw},0) rectangle ({i*cw+cw},{cw});')
o+=[tx(-.5,.65+cw/2,'\\textbf{A}'),tx(-.5,cw/2,'\\textbf{B}'),tx(5.5*cw+cw/2+.0,1.45,'\\footnotesize ortak kutular')]
SK=fig('\n'.join(o))
q('0004',tipId='kvb-serit',tip='Şerit modelde kesişim ve birleşim',z='orta',alt='Venn Şeması',kaz='Şerit modelde ortak kutulardan birleşimin kutu sayısını bulup bir kutunun değeri üzerinden yalnız bir kümedekileri hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-04 (şerit model) · A 7, B 5, ortak 2 kutu; birleşim 120',
 metin='Bir sitede satranç kulübüne üye olanlar A, bilmece kulübüne üye olanlar B şeridiyle gösterilmiştir; her kutu aynı sayıda üyeyi temsil etmekte ve ortak kutular iki kulübe de üye olanları göstermektedir. Kulüplerin en az birine üye olan kişi sayısı 120’dir.\nBuna göre yalnız bir kulübe üye olan kişi sayısı kaçtır?',
 dogru=int(d4),yan=[(84,'Yalnız A şeridinin tamamını (7 kutu) yazmış.','dikkat'),(60,'Yalnız B şeridinin tamamını (5 kutu) yazmış.','dikkat'),(80,'Ortak kutuları iki kez sayıp bir kutuyu 10 kişi bulmuş.','dikkat'),(24,'Yalnızca ortak kutuların değerini (2 kutu) yazmış.','dikkat')],
 istenen='Yalnız bir kulübe üye olan kişi sayısı.',
 ip=['Birleşimde kaç kutu olduğunu sayarken ortak kutuları bir kez say.'],
 bilgi=[SER],
 ad=[A('Birleşim','Ortak kutular bir kez sayılarak toplam kutu bulunur.','7 + 5 − 2 = 10 kutu'),A('Bir kutu','120 kişi 10 kutuya bölünür.','120 ÷ 10 = 12 kişi'),A('Yalnız kutular','Ortak kutular dışındaki kutular sayılır.','(7 − 2) + (5 − 2) = 8 kutu'),A('Kişi sayısı','Kutu sayısı bir kutunun değeriyle çarpılır.','8 × 12 = 96')],
 puf='Önce birleşimdeki kutu sayısını ortak kutuları tek say; sonra yalnız bir kümedeki kutuları ayır.')

# ---------- 05 sütun grafiği ----------
nA5,nB5,nU5,nE5=34,27,50,60; ks=nA5+nB5-nU5; hc=nE5-nU5; d5=ks+hc; assert (ks,hc,d5)==(11,10,21)
e5=[nU5-ks,nA5+nB5,nU5,nE5]; assert e5==[39,61,50,60] and len({d5,*e5})==5
sy=.045; o=[]
for t in range(0,61,10): o.append(ln(0,t*sy,4.3,t*sy,'black!12,line width=.4pt')); o.append(tx(-.3,t*sy,f'\\footnotesize {t}'))
o+=[ln(0,0,0,63*sy,'line width=1pt'),ln(0,0,4.3,0,'line width=1.2pt'),tx(.5,63*sy+.3,'\\footnotesize Öğrenci sayısı')]
for i,(nm,val) in enumerate([('$A$',nA5),('$B$',nB5),('$A\\cup B$',nU5),('$E$',nE5)]):
    x=.2+i*1.0; o.append(f'\\fill[vurgu!45] ({x:.2f},0) rectangle ({x+.6:.2f},{val*sy:.3f});'); o.append(tx(x+.3,-.35,f'\\footnotesize {nm}')); o.append(tx(x+.3,val*sy+.25,f'\\footnotesize {val}'))
SK=fig('\n'.join(o))
q('0005',tipId='kvb-sutun',tip='Sütun grafiğinden kesişim ve yalnız bir küme',z='orta',alt='Venn Şeması',kaz='Sütun grafiğinden küme eleman sayılarını okuyup kesişimi ve dışarıdaki bölgeyi bularak istenen toplamı hesaplar.',kalip='grafik',sekil=SK,
 kart='K-KVB-05 (sütun grafiği) · 34, 27, 50, 60',
 metin='Bir okulda tüm öğrencilerin kümesi E, A ve B kulüplerine üye olan öğrencilerin kümeleri A ve B ile gösterilmiştir. Bu kümelerin ve A ile B kümelerinin birleşiminin eleman sayıları yukarıdaki sütun grafiğinde verilmiştir.\nBuna göre her iki kulübe de üye olan öğrenci sayısı ile hiçbir kulübe üye olmayan öğrenci sayısının toplamı kaçtır?',
 dogru=int(d5),yan=[(39,'Yalnız bir kulübe üye olanların sayısını (50 − 11) yazmış.','dikkat'),(50,'Birleşimin eleman sayısını yazmış.','dikkat'),(60,'Tüm öğrenci sayısını yazmış.','dikkat'),(61,'s(A) ile s(B)’yi toplamış: 34 + 27.','islem')],
 istenen='Kesişimdeki ve dışarıdaki öğrencilerin toplamı.',
 ip=['Grafikten s(A), s(B), s(A ∪ B) ve s(E) değerlerini oku; kesişim için birleşim formülünü kullan.'],
 bilgi=[BIR],
 ad=[A('Değerleri oku','Dört sütunun yüksekliği okunur.','s(A) = 34; s(B) = 27; s(A ∪ B) = 50; s(E) = 60'),A('Kesişim','s(A ∩ B) = s(A) + s(B) − s(A ∪ B).','34 + 27 − 50 = 11'),A('Dışarısı','Evrensel kümeden birleşim çıkarılır.','60 − 50 = 10'),A('Topla','İki bölge toplanır.','11 + 10 = 21')],
 puf='Önce kesişimi birleşim formülüyle bul; dışarıyı evrensel kümeden birleşimi çıkararak elde et.')

# ---------- 06 isimli Venn, üyelik değişimi ----------
A0=['Ali','Bora','Cem']; AB0=['Deniz','Ece']; B0=['Fatma','Gül','Hakan','İpek']; N0=['Jale','Kaan']
st={n:(True,False) for n in A0}; st.update({n:(True,True) for n in AB0}); st.update({n:(False,True) for n in B0}); st.update({n:(False,False) for n in N0})
def bir(s): return sum(1 for a,b in s.values() if a!=b)
def uygula(s,atla=(),cem_gec=False):
    s=dict(s); 
    if 'Bora' not in atla: s['Bora']=(False,True)
    if 'Cem' not in atla: s['Cem']=(False,True) if cem_gec else (s['Cem'][0],True)
    if 'Deniz' not in atla: s['Deniz']=(True,False)
    if 'Ece' not in atla: s['Ece']=(False,True)
    if 'Jale' not in atla: s['Jale']=(True,False)
    return s
d6=bir(uygula(st)); assert d6==9
sonB=sum(1 for a,b in uygula(st).values() if b and not a)
e6=[bir(st),bir(uygula(st,atla=('Jale',))),bir(uygula(st,cem_gec=True)),sonB]; assert e6==[7,8,10,6] and len({d6,*e6})==5
def kl(l): return '\\\\'.join(l)
o=[f'\\draw[line width=1.1pt] (-3.3,-2.0) rectangle (3.3,2.0);','\\draw[line width=1.1pt] (-.8,0) circle (1.55);','\\draw[line width=1.1pt] (.8,0) circle (1.55);',
 tx(-1.5,0,kl(A0),'align=center,font=\\footnotesize'),tx(0,0,kl(AB0),'align=center,font=\\footnotesize'),tx(1.5,0,kl(B0),'align=center,font=\\footnotesize'),
 tx(2.45,-1.45,kl(N0),'align=center,font=\\footnotesize'),tx(-1.3,1.8,'\\textbf{Tiyatro}'),tx(1.3,1.8,'\\textbf{Müzik}')]
SK=fig('\n'.join(o))
q('0006',tipId='kvb-isim',tip='İsimli Venn ve üyelik değişimi',z='orta',alt='Venn Şeması',kaz='İsimli Venn şemasında kişilerin kulüp değişikliklerini bölgelere işleyip yalnız bir kulübe üye olanların sayısını bulur.',kalip='şekilli',sekil=SK,
 kart='K-KVB-06 (isimli Venn) · 5 üyelik değişikliği',
 metin='Bir okulda tiyatro ve müzik kulüplerine üye öğrenciler ile hiçbirine üye olmayanlar yukarıdaki şemada adlarıyla gösterilmiştir. Yeni dönemde Bora tiyatrodan ayrılıp müzik kulübüne katılmış, Cem müzik kulübüne de üye olmuş, Deniz müzikten, Ece tiyatrodan ayrılmış, Jale tiyatro kulübüne katılmıştır; başka değişiklik olmamıştır.\nBuna göre yeni dönemde yalnız bir kulübe üye olan öğrenci sayısı kaçtır?',
 dogru=d6,yan=[(7,'Değişiklikleri işlemeyip ilk şemadaki yalnız bir kulübe üyeleri saymış.','dikkat'),(8,'Jale’nin tiyatro kulübüne katılmasını işlememiş.','dikkat'),(10,'Cem’in müziğe de üye olduğunu, tiyatrodan müziğe geçmiş gibi işlemiş.','dikkat'),(6,'Yalnız müzik kulübüne üye olanların sayısını yazmış.','dikkat')],
 istenen='Yalnız bir kulübe üye olan öğrenci sayısı.',
 ip=['Her kişiyi yeni bölgesine yerleştir; sonra tek kulübe üye olanları say.'],
 bilgi=[DEG],
 ad=[A('İlk durum','Şemadan bölgeler sayılır.','yalnız tiyatro 3; ikisi 2; yalnız müzik 4; dışarısı 2'),A('Geçişler','Bora yalnız müziğe, Cem ikisine, Deniz yalnız tiyatroya, Ece yalnız müziğe, Jale yalnız tiyatroya geçer.','Bora; Cem; Deniz; Ece; Jale'),A('Yeni bölgeler','Yalnız tiyatro: Ali, Deniz, Jale. Yalnız müzik: Bora, Ece, Fatma, Gül, Hakan, İpek. İkisi: Cem.','3; 6; 1'),A('Topla','Yalnız bir kulübe üye olanlar.','3 + 6 = 9')],
 puf='Her öğrencinin yeni kulüp durumunu tek tek yaz, sonra yalnız bir kulübü olanları say.')

# ---------- 07 daire toplamlı üç kümeli Venn ----------
tA,tB,tC=21,18,15; pab,pac,pbc=5,4,3; none7=7; E7=45
t=Fr(sum([pab,pac,pbc])+sum([]),1)  # yer tutucu
# sum = (tA-pab-pac)+(tB-pab-pbc)+(tC-pac-pbc)+pab+pac+pbc+3*0 ... çöz
base=(tA+tB+tC)-2*(pab+pac+pbc)+(pab+pac+pbc)+none7  # t=0 iken toplam: yalnızlar + ikililer + dışarısı
# toplam(t)=base-3t+t = base-2t
t7=Fr(base-E7,2); assert t7==2
aa7,bb7,cc7=tA-pab-pac-t7,tB-pab-pbc-t7,tC-pac-pbc-t7; assert (aa7,bb7,cc7)==(10,8,6)
d7=int(aa7+bb7+cc7); assert d7==24 and aa7+bb7+cc7+pab+pac+pbc+t7+none7==E7
e7=[(tA-pab-pac)+(tB-pab-pbc)+(tC-pac-pbc),pab+pac+pbc,pab+pac+pbc+t7,E7-none7]; assert e7==[30,12,14,38] and len({d7,*e7})==5
SK=fig('\n'.join(venn3(dict(ab=pab,ac=pac,bc=pbc,out=none7),names=('$s(A)=21$','$s(B)=18$','$s(C)=15$'),w=5.6,h=4.4,koşe=True)))
q('0007',tipId='kvb-toplam',tip='Daire toplamları ve üçlü kesişim',z='zor',alt='Venn Şeması',kaz='Üç kümeli Venn’de daire toplamlarını ve ikili bölgeleri kullanarak üçlü kesişimi bulup yalnız bir kümedekileri hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-07 (daire toplamları) · 45 üye; üçlü kesişim 2',
 metin='Bir spor salonunda 45 üyenin A, B ve C branşlarına kayıtları yukarıdaki Venn şemasında gösterilmiştir; dairelerin yanındaki ifadeler o branştaki toplam üye sayısını, iki dairenin ortak bölgesindeki sayılar ise yalnız o iki branşa kayıtlı üye sayısını göstermektedir. Dikdörtgenin köşesindeki sayı hiçbir branşa kayıtlı olmayan üyeleri gösterir; yalnız bir daireye ait bölgelerde ve üç dairenin ortak bölgesinde sayı yazılmamıştır.\nBuna göre yalnız bir branşa kayıtlı üye sayısı kaçtır?',
 dogru=d7,yan=[(30,'Üçlü kesişimi 0 alıp yalnız bölgeleri toplamış.','dikkat'),(12,'İkili bölgelerin toplamını (5 + 4 + 3) yazmış.','dikkat'),(14,'İkili bölgelerle üçlü kesişimin toplamını yazmış.','dikkat'),(38,'Dışarıdaki 7’yi çıkarıp en az bir branşa kayıtlı olanları yazmış.','dikkat')],
 istenen='Yalnız bir branşa kayıtlı üye sayısı.',
 ip=['Üçlü kesişime t de; her dairenin toplamından yalnız bölgeyi t cinsinden yaz.'],
 bilgi=[TOP],
 ad=[A('Yalnız bölgeler','Daire toplamından diğer üç bölge çıkarılır; üçlü kesişim t olsun.','A: 21 − 5 − 4 − t = 12 − t; B: 18 − 5 − 3 − t = 10 − t; C: 15 − 4 − 3 − t = 8 − t'),A('Toplam denklemi','Tüm bölgeler toplanır.','(12 − t) + (10 − t) + (8 − t) + 5 + 4 + 3 + t + 7 = 45'),A('t bul','Sadeleştirilir.','49 − 2t = 45 → t = 2'),A('Yalnız bölgeler','Her biri hesaplanır.','10; 8; 6'),A('Topla','Yalnız bir branşa kayıtlılar.','10 + 8 + 6 = 24')],
 puf='Önce üçlü kesişime bir harf ver; her dairenin toplamı o dairedeki dört bölgenin toplamıdır.')

# ---------- 08 yüzdeli Venn ----------
E8=250; pA,pB,pO=62,48,8; pk=pA+pB-(100-pO); ya=pA-pk; assert (pk,ya)==(18,44)
cnt=Fr(E8*ya,100); d8=cnt*Fr(3,5); assert (cnt,d8)==(110,66)
e8=[Fr(E8*pA,100)*Fr(3,5),Fr(E8*(100-pO),100)*Fr(3,5),Fr(E8*3,5),cnt]; assert e8==[93,138,150,110] and len({d8,*e8})==5
SK=fig('\n'.join(venn2('','','','\\%8',ra=1.1,dx=.7,w=4.8,h=3.4,na='A: \\%62',nb='B: \\%48')))
q('0008',tipId='kvb-yuzde',tip='Yüzdeli Venn ve kesirli alt grup',z='orta',alt='Venn Şeması',kaz='Yüzdelerle verilen Venn şemasında kesişimi ve yalnız bir kümedeki payı bulup kesirli alt grubun sayısını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-08 (yüzdeli Venn) · 250 öğrenci; %62, %48, %8',
 metin='Bir okulda 250 öğrenciye hangi kulüplere üye oldukları sorulmuştur. A kulübüne, B kulübüne ve hiçbir kulübe üye olanların tüm öğrencilere oranları yukarıdaki Venn şemasında yüzdelerle gösterilmiştir.\nA kulübüne (ikisine de üye olanlar dâhil) üye olanların oranı yüzde olarak verilmiştir. Yalnız A kulübüne üye olan öğrencilerin 3/5’i kız olduğuna göre bu kız öğrenciler kaç kişidir?',
 dogru=int(d8),yan=[(93,'A kulübünün tamamını (%62 ile 155 kişi) alıp 3/5’ini bulmuş.','dikkat'),(138,'Kulüplerden en az birine üye olanların (230 kişi) 3/5’ini bulmuş.','dikkat'),(150,'Tüm öğrencilerin 3/5’ini bulmuş.','dikkat'),(110,'Yalnız A’dakileri doğru bulup 3/5 ile çarpmayı unutmuş.','dikkat')],
 istenen='Yalnız A kulübüne üye kız öğrenci sayısı.',
 ip=['Hiçbirine üye olmayanları çıkararak birleşimin yüzdesini bul.'],
 bilgi=[YUZ],
 ad=[A('Birleşim','Dışarıdaki %8 çıkarılır.','100 − 8 = %92'),A('Kesişim','Yüzdeler toplamından birleşim çıkarılır.','62 + 48 − 92 = %18'),A('Yalnız A','A’nın yüzdesinden kesişim çıkarılır.','62 − 18 = %44'),A('Kişi sayısı','Yüzde evrensel kümeyle çarpılır.','250 × 44 / 100 = 110'),A('Kız öğrenci','3/5’i alınır.','110 × 3/5 = 66')],
 puf='Yalnız A’nın yüzdesini bulmak için kesişimi A’dan çıkar; sonra kişi sayısına çevirip kesri uygula.')

# ---------- 09 iki bilinmeyenli Venn ----------
E9,sA9=60,30; ac9,bc9,abc9,cc9,out9=3,2,1,8,5
# 2x+y+ac+abc=sA ; 2x+(x+4)+cc+y+ac+bc+abc+out=E
# 2x+y=26 ; 3x+y=37
x9=(E9-(4+cc9+ac9+bc9+abc9+out9))-(sA9-ac9-abc9); y9=(sA9-ac9-abc9)-2*x9; assert (x9,y9)==(11,4)
aa9,bb9,ab9=2*x9,x9+4,y9; assert aa9+ab9+ac9+abc9==sA9 and aa9+bb9+cc9+ab9+ac9+bc9+abc9+out9==E9
d9=bb9+ab9+bc9+abc9; assert d9==22
# hatalı: abc'yi A denkleminde atla: 2x+y=27, 3x+y=37 -> x=10,y=7
xh=37-27; yh=27-2*xh; e9a=xh+4+yh+bc9+abc9; assert (xh,yh,e9a)==(10,7,24)
e9=[e9a,bb9+ab9+bc9,sA9,E9-d9]; assert e9==[24,21,30,38] and len({d9,*e9})==5
SK=fig('\n'.join(venn3(dict(aa='$2x$',bb='$x+4$',cc=8,ab='$y$',ac=3,bc=2,abc=1,out=5))))
q('0009',tipId='kvb-iki',tip='İki bilinmeyenli üç kümeli Venn',z='zor',alt='Venn Şeması',kaz='İki bilinmeyenli üç kümeli Venn’de iki denklem kurup bilinmeyenleri bulur ve istenen kümenin eleman sayısını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-09 (iki bilinmeyen) · E=60, s(A)=30; x=11, y=4',
 metin='Bir okulda 60 öğrencinin A, B ve C kulüplerine üyeliği yukarıdaki Venn şemasında gösterilmiş; her bölgedeki ifade, o bölgedeki öğrenci sayısını göstermektedir. A kulübünün eleman sayısı 30’dur.\nBuna göre B kulübüne üye olan öğrenci sayısı kaçtır?',
 dogru=d9,yan=[(24,'A kulübü denkleminde üçlü kesişimi atlayıp 2x + y = 27 yazmış.','dikkat'),(21,'s(B)’yi hesaplarken üçlü kesişim bölgesini (1) katmamış.','dikkat'),(30,'Soruda verilen A kulübünün eleman sayısını yazmış.','dikkat'),(38,'B kulübünün dışındaki öğrencileri (60 − 22) yazmış.','dikkat')],
 istenen='B kulübüne üye olan öğrenci sayısı.',
 ip=['Verilen iki bilginin her biri hangi bölgeleri kapsıyor?'],
 bilgi=[UCV],
 ad=[A('A denklemi','A dairesindeki dört bölge toplanır.','2x + y + 3 + 1 = 30 → 2x + y = 26'),A('Toplam denklemi','Tüm bölgeler toplanır.','2x + (x + 4) + 8 + y + 3 + 2 + 1 + 5 = 60 → 3x + y = 37'),A('Çöz','İki denklem çıkarılır.','x = 11; y = 26 − 22 = 4'),A('B bölgeleri','Yalnız B, A ∩ B, B ∩ C ve üçlü kesişim.','15; 4; 2; 1'),A('Topla','B dairesindeki bölgeler toplanır.','15 + 4 + 2 + 1 = 22')],
 puf='A dairesinin toplamı ile tüm bölgelerin toplamı iki ayrı denklem verir; ikisini çıkarınca x bulunur.')

# ---------- 10 iki Venn şemasını birleştirme ----------
X=dict(a=9,ab=6,b=8,n=7); nX=sum(X.values()); assert nX==30
tAY,tBY,nY,nnY=20,15,38,8; abY=tAY+tBY-(nY-nnY); aY,bY=tAY-abY,tBY-abY; assert (abY,aY,bY)==(5,15,10) and nnY+abY+aY+bY==nY
d10=X['n']+X['ab']+nnY+abY; assert d10==26
e10=[X['ab']+abY,X['n']+X['ab'],X['n']+nnY,X['a']+X['b']]; assert e10==[11,13,15,17] and len({d10,*e10})==5
o=['\\begin{scope}[shift={(-2.7,0)}]']+venn2(9,6,8,7,ra=.95,dx=.6,w=4.2,h=3.2,na='A',nb='B')+[tx(0,1.9,'\\textbf{X sınıfı: 30 kişi}'),'\\end{scope}']
o+=['\\begin{scope}[shift={(2.7,0)}]']+venn2('','','',8,ra=.95,dx=.6,w=4.2,h=3.2,na='A: 20',nb='B: 15')+[tx(0,1.9,'\\textbf{Y sınıfı: 38 kişi}'),'\\end{scope}']
SK=fig('\n'.join(o))
q('0010',tipId='kvb-birles',tip='İki Venn şemasını birleştirme',z='zor',alt='Venn Şeması',kaz='İki sınıfın Venn şemalarından bölgeleri bulup birleştirerek tamamlayıcı iki bölgenin toplamını hesaplar.',kalip='şekilli',sekil=SK,
 kart='K-KVB-10 (iki sınıf) · X 30 kişi, Y 38 kişi; yanıt 26',
 metin='X ve Y sınıflarında satranç (A) ve bulmaca (B) kulüplerine üyelik yukarıdaki şemalarda gösterilmiştir; X sınıfında bölgelerdeki sayılar kişi sayısını, Y sınıfında dairelerin yanındaki sayılar kulüplerin toplam üye sayısını göstermektedir. İki sınıf birleştirilerek tek bir sınıf oluşturulmuştur.\nBuna göre birleşik sınıfta ya hiçbir kulübe üye olmayan ya da iki kulübe birden üye olan öğrenci sayısı kaçtır?',
 dogru=d10,yan=[(11,'Yalnız iki kulübe birden üye olanları (6 + 5) yazmış.','dikkat'),(13,'Yalnız X sınıfındaki dışarı ve ortak bölgeleri (7 + 6) toplamış.','dikkat'),(15,'Yalnız hiçbir kulübe üye olmayanları (7 + 8) yazmış.','dikkat'),(17,'X sınıfında yalnız bir kulübe üye olanları (9 + 8) yazmış.','dikkat')],
 istenen='Birleşik sınıfta dışarıdaki ve ortak bölgedeki öğrenci sayısı.',
 ip=['Y sınıfında kesişimi ve dışarıdaki bölgeyi dairelerin toplamlarından bul.'],
 bilgi=[BIRL,BIR],
 ad=[A('Y kesişimi','Y’de kulüplerden en az birine üye olanlar 38 − 8 = 30’dur.','20 + 15 − 30 = 5'),A('Y dışarısı','Şemada verilmiştir.','8'),A('X bölgeleri','Şemadan okunur.','kesişim 6; dışarısı 7'),A('Birleştir','Aynı bölgeler toplanır.','kesişim: 6 + 5 = 11; dışarısı: 7 + 8 = 15'),A('Topla','İstenen iki bölge.','11 + 15 = 26')],
 puf='İki sınıfın kesişim ve dışarı bölgelerini ayrı ayrı bul, sonra aynı bölgeleri topla.')

bitir(P,'kumesekb','matd|Kümeler-Kartezyen Çarpım')
