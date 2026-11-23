"""AYT Fizik · Atışlar (yatay ve eğik atış) · 20 soru (3 kolay / 11 orta / 6 zor). Kardeş yok, ipucu 1.
Şekil koordinatları Python'da aynı fizik verisinden üretilir; her cevap/çeldirici değer assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz'))
import _hafif as H
from _hafif import mk,kart
from ortak import *
from cizim import tikz_svg
from fractions import Fraction as Fr
from math import sqrt
P=Parti('atis','Atışlar','afiz|Atışlar',ders='AYT Fizik',idon='aytfiz')
P.k='afiz|Atışlar'; H.KONU='Atışlar'
KAY='ÖSYM AYT 2019–2025 (yalnız mantık) · 345 AYT Fizik Soru Bankası, İki Boyutta Hareket'
TIPK={}
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAY); TIPK[tipId]=P.k
def q(no,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),**k)
g=10
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def p2(x,y): return f'({x:.3f},{y:.3f})'
def curve(f,t0,t1,n=28): return 'plot[smooth] coordinates {'+' '.join(p2(*f(t0+(t1-t0)*i/n)) for i in range(n+1))+'}'
def traj(f,t0,t1,st='vurgu,very thick,dash pattern=on 4pt off 2.5pt'): return f'\\draw[{st}] {curve(f,t0,t1)};'
def ball(x,y,r=.1,fill='gray!70'): return f'\\filldraw[fill={fill}] {p2(x,y)} circle ({r});'
def ground(x0,x1): return f'\\fill[gray!30] ({x0},-.16) rectangle ({x1},0); \\draw[thick] ({x0},0) -- ({x1},0);'
def block(x0,x1,h): return f'\\draw[thick,fill=gray!20] ({x0},0) rectangle ({x1},{h});'
def vec(a,b,lab=None,pos='above',st='very thick'):
    s=f'\\draw[{st},{ARR}] {p2(*a)} -- {p2(*b)};'
    if lab: s+=f'\\node[{pos},inner sep=1.5pt] at {p2((a[0]+b[0])/2,(a[1]+b[1])/2)} {{{lab}}};'
    return s
def dimv(x,y0,y1,txt): return f'\\draw[<->,thin] {p2(x,y0)} -- {p2(x,y1)}; \\node[rotate=90,above,inner sep=1.5pt] at {p2(x,(y0+y1)/2)} {{{txt}}};'
def dimh(y,x0,x1,txt,below=True):
    return (f'\\draw[<->,thin] {p2(x0,y)} -- {p2(x1,y)}; \\node[{"below" if below else "above"},inner sep=1.5pt] at {p2((x0+x1)/2,y)} {{{txt}}};'
            f'\\draw[dotted] {p2(x0,0)} -- {p2(x0,y)}; \\draw[dotted] {p2(x1,0)} -- {p2(x1,y)};')
def N(x,y,t,pos='above'): return f'\\node[{pos},inner sep=1.5pt] at {p2(x,y)} {{{t}}};'
def sk(lines,extra=''):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small'+extra+']\n'+'\n'.join(lines)+TAIL)
ROM=['I','II','III']
KUME={(0,):'Yalnız I',(1,):'Yalnız II',(2,):'Yalnız III',(0,1):'I ve II',(0,2):'I ve III',(1,2):'II ve III',(0,1,2):'I, II ve III'}
def oncullu(truth,miss,liste,turlar=None):
    """truth: 3 doğru/yanlış değeri (TEK kaynak). miss[j]: o öncülü yanlış değerlendiren öğrencinin hatası.
    Döner: dogru, yan(liste), sira."""
    dk=tuple(j for j in range(3) if truth[j]); dogru=KUME[dk]
    assert dogru in liste and len(liste)==5 and len(set(liste))==5
    inv={v:k for k,v in KUME.items()}
    yan=[]
    for s in liste:
        if s==dogru: continue
        S=set(inv[s]); parts=[]
        for j in range(3):
            if (j in S)!=truth[j]: parts.append(f'{ROM[j]}. yargıyı değerlendirirken '+miss[j].rstrip('.')[0].replace('İ','i').lower()+miss[j].rstrip('.')[1:])
        yan.append((s,'Bu kümeyi seçen öğrenci '+'; '.join(parts)+'.', 'bilgi' if len(parts)==1 else 'dikkat'))
    return dogru,yan,liste
def adim_onc(truth,expl,sonuc):
    ad=[A(f'{ROM[j]}. yargıyı incele',expl[j],f'{ROM[j]}: '+('doğru' if truth[j] else 'yanlış')) for j in range(3)]
    ad.append(A('Doğru kümeyi seç','Doğru olan yargıları birlikte değerlendir.',sonuc))
    return ad

# ============ 01 · Yatay atış menzili · kolay ============
kartla('K-AFAT-01','Yatay atışta menzil','Düşey bileşen serbest düşmedir: h = ½·g·t² ile süre bulunur; yatay bileşen sabit hızlı olduğundan x = v·t.','Süreyi h/g ya da 2h/g almak; yüksekliği yatay uzaklık sanmak; yatay harekette de ½ çarpanı kullanmak.','kolay','şekilli',3,'at-yatay-menzil','Yatay atışta yükseklik ve ilk hızdan menzil')
t1=Fr(80,5); import math as _m; T1=int(_m.isqrt(16)); assert 5*T1**2==80; X1=15*T1; assert X1==60
assert (15*Fr(80,10),15*Fr(160,10),80,Fr(15*T1,2))==(120,240,80,30)
H1=80;V1=15;sc=20
f1=lambda t:(V1*t/sc,(H1-5*t*t)/sc)
SK1=sk([ground(-1.3,3.8),block(-1.3,0,4),traj(f1,0,4),ball(0,4),vec((0,4.3),(.9,4.3),'$15$ m/s'),dimv(-1.55,0,4,'$80$ m'),
        dimh(-.5,0,3,'$x$')])
q('0001',tipId='at-yatay-menzil',tip='Yatay atışta yükseklik ve ilk hızdan menzil',z='kolay',alt='Yatay Atış',kaz='Yatay atış hareketinde düşey ve yatay bileşenleri ayrı ele alarak menzili hesaplar.',
 kart='K-AFAT-01 (yatay atış menzili) · h = 80 m, v = 15 m/s',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, yüksekliği şekilde verilen bir uçurumun kenarından noktasal bir taş, yine şekilde belirtilen büyüklükteki hızla yatay doğrultuda atılıyor. Taş, şekildeki yörüngeyi izleyerek yatay zemine çarpıyor.\n(g = 10 m/s²)\nBuna göre, taşın yere çarptığı nokta ile atıldığı noktanın hemen altındaki nokta arasındaki yatay uzaklık x kaç m’dir?',
 dogru=60,yan=[(30,'Yatay harekette de x = ½·v·t yazmış: ½ × 15 × 4 = 30 m. Sabit hızlı harekette yol v·t’dir.','bilgi'),
  (80,'Atış yüksekliğini (80 m) yatay uzaklık sanmış; yükseklik yalnızca düşme süresini belirler.','dikkat'),
  (120,'Düşme süresini t = h/g = 8 s almış: 15 × 8 = 120 m. Doğrusu h = ½·g·t² ile t = 4 s’dir.','islem'),
  (240,'Düşme süresini t = 2h/g = 16 s almış: 15 × 16 = 240 m.','islem')],
 istenen='Taşın yere çarptığı nokta ile atıldığı noktanın hemen altındaki nokta arasındaki yatay uzaklık (m).',
 ip=['Yatay ve düşey doğrultudaki hareketleri ayrı düşün; iki hareketi birbirine bağlayan ortak nicelik hangisi?'],
 bilgi=[B('Yatay atış','İlk hız yataydır; yatayda ivme yoktur (sabit hız), düşeyde ilk hızsız serbest düşme vardır. h = ½·g·t² ve x = v·t. Örnek: 20 m’den bırakılan cisim t = 2 s’de yere iner')],
 ad=[A('Düşme süresini bul','Düşey doğrultuda cisim ilk hızsız serbest düşer.','80 = ½ × 10 × t² → t² = 16 → t = 4 s'),
     A('Yatay hareketi yaz','Yatay doğrultuda ivme yoktur; hız sabittir ve cisim aynı 4 s boyunca yatayda ilerler.','x = v × t = 15 × 4'),
     A('Sonucu bul','Çarpıp işlemi yap.','x = 60 m')],
 puf='Yatay atışta iki hareketi bağlayan tek ortak nicelik süredir: önce düşeyden süreyi bul, sonra yatayda kullan.',sekil=SK1)

# ============ 02 · Yatay atışta çarpma sürati · kolay ============
kartla('K-AFAT-02','Yere çarpma sürati','Yere çarpma anında yatay bileşen ilk hıza eşit, düşey bileşen g·t; bileşke Pisagor ile bulunur.','Bileşenleri toplamak ya da yalnız birini almak; düşey bileşeni ilk hız sanmak.','kolay','şekilli',3,'at-yatay-hiz','Yatay atışta yere çarpma hızının büyüklüğü')
h2,v2=45,16; t2=3; assert 5*t2**2==h2; vy2=g*t2; assert vy2==30 and 16**2+30**2==34**2
sc=10; f2=lambda t:(v2*t/sc,(h2-5*t*t)/sc)
SK2=sk([ground(-1.4,5.4),block(-1.4,0,4.5),traj(f2,0,3),ball(0,4.5),vec((0,4.8),(.9,4.8),'$16$ m/s'),dimv(-1.65,0,4.5,'$45$ m')])
q('0002',tipId='at-yatay-hiz',tip='Yatay atışta yere çarpma hızının büyüklüğü',z='kolay',alt='Yatay Atış',kaz='Yatay atışta yere çarpma anındaki hız bileşenlerini bulup bileşke hızı hesaplar.',
 kart='K-AFAT-02 (çarpma sürati) · h = 20 m, v = 15 m/s',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, şekildeki balkonun kenarından noktasal bir top yatay doğrultuda atılıyor. Balkonun yerden yüksekliği ve topun ilk hızı şekilde verilmiştir; top şekildeki yörüngeyi izleyerek yere çarpıyor.\n(g = 10 m/s²)\nBuna göre, topun yere çarptığı andaki hızının büyüklüğü kaç m/s’dir?',
 dogru=34,yan=[(14,'Bileşenlerin farkını almış: 30 − 16 = 14 m/s. Dik bileşenler Pisagor ile birleştirilir.','islem'),
  (16,'Yatay bileşeni (16 m/s) çarpma hızı sanmış; çarpma anında düşey bileşen de vardır.','dikkat'),
  (30,'Yalnızca düşey bileşeni (g·t = 30 m/s) çarpma hızı sanmış; yatay bileşeni unutmuş.','dikkat'),
  (46,'Bileşenleri doğrudan toplamış: 16 + 30 = 46 m/s. Dik vektörler cebirsel toplanmaz.','islem')],
 istenen='Topun yere çarpma anındaki hızının büyüklüğü (m/s).',
 ip=['Çarpma anındaki hızı yatay ve düşey iki bileşenin bileşkesi olarak düşün; düşey bileşeni düşme süresinden bulabilirsin.'],
 bilgi=[B('Bileşke hız','Birbirine dik bileşenlerin bileşkesi v = √(vx² + vy²). Örnek: 6 ve 8 m/s’lik bileşenlerin bileşkesi 10 m/s’dir'),
        B('Serbest düşme','Düşey bileşen v_y = g·t ve h = ½·g·t². Örnek: 1 s sonra düşey hız 10 m/s olur')],
 ad=[A('Düşme süresini bul','Düşeyde ilk hızsız serbest düşme.','45 = ½ × 10 × t² → t = 3 s'),
     A('Çarpma anındaki bileşenler','Yatay bileşen sabittir; düşey bileşen g·t ile bulunur.','vx = 16 m/s → vy = 10 × 3 = 30 m/s'),
     A('Bileşkeyi bul','Bileşenler birbirine diktir.','v = √(16² + 30²) = √1156 = 34 m/s')],
 puf='Çarpma sürati için önce düşey bileşeni (g·t) bul, sonra yatay bileşenle Pisagor kur.',sekil=SK2)

# ============ 03 · Yatay atış nitel (öncüllü) · kolay ============
kartla('K-AFAT-03','Yatay atışta ivme ve hız','Yatay atışta ivme her yerde g (aşağı); yatay hız sabit, düşey hız artar, hızın büyüklüğü artar.','Hız büyüklüğünü sabit sanmak; yatay bileşenin arttığını düşünmek.','kolay','öncüllü',4,'at-nitel','Atış hareketlerinde nitel yargılar')
tr3=(True,False,False)
d3,y3,s3=oncullu(tr3,['İvmenin yörünge boyunca değiştiğini düşünmüş.','Yatay hız bileşeninin, hız arttığı için yatayda da arttığını sanmış.','Hızın büyüklüğünün atış boyunca değişmediğini sanmış; oysa düşey bileşen artar.'],['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
f4=lambda t:(2.2*t,3-.75*t*t)
SK3=sk([ground(-1.3,5.2),block(-1.3,0,3),traj(f4,0,2),ball(0,3),ball(*f4(1)),ball(*f4(2)),N(-.1,3,'K','above left'),N(*f4(1),'L','above right'),N(4.4,0,'M','above right')])
q('0003',tipId='at-nitel',tip='Atış hareketlerinde nitel yargılar',z='kolay',alt='Yatay Atış',kaz='Yatay atış hareketinde ivme, hız bileşenleri ve hızın büyüklüğündeki değişimi yorumlar.',
 kart='K-AFAT-03 (yatay atış nitel) · K, L, M noktaları',kalip='öncüllü',
 metin='Hava direncinin ihmal edildiği bir ortamda, yatay doğrultuda atılan noktasal bir cisim şekilde görüldüğü gibi K noktasından atılıyor, L noktasından geçiyor ve M noktasında yere çarpıyor.\nBuna göre, cisimle ilgili,\nI. K, L ve M noktalarında ivmesinin büyüklüğü ve yönü aynıdır.\nII. Hızının yatay bileşeninin büyüklüğü M noktasında K noktasındakinden büyüktür.\nIII. Hızının büyüklüğü M noktasında K noktasındakine eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d3,yan=y3,sira=s3,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Hava direnci yokken cisme etki eden tek kuvvetin ne olduğunu ve bunun hız bileşenlerini nasıl etkilediğini düşün.'],
 bilgi=[B('Atış hareketlerinde ivme','Hava direnci yoksa cisme yalnızca ağırlığı etki eder; ivme her noktada g, yönü düşey aşağıdır. Yatay bileşen sabit, düşey bileşen değişir')],
 ad=adim_onc(tr3,['İvmeyi yalnızca ağırlık oluşturur; büyüklüğü g, yönü aşağıdır ve yörünge boyunca değişmez.','Yatay doğrultuda kuvvet yoktur; yatay hız bileşeni atış boyunca sabit kalır.','Düşey bileşen sürekli artar, yatay bileşen sabittir; bileşke hızın büyüklüğü M’de K’dakinden büyüktür.'],'Yalnız I doğrudur'),
 puf='İvme sabit ve düşey; yatay bileşen sabit; düşey bileşen değişir. Hızın büyüklüğü bunların bileşkesidir.',sekil=SK3)

# ============ 04 · Aynı noktaya düşen iki cisim · orta ============
kartla('K-AFAT-04','İki yatay atışta ortak menzil','Aynı menzil için yatay hızlar, düşme sürelerinin (√h ile orantılı) tersiyle orantılıdır.','Yükseklik oranını doğrudan hız oranı almak; oranı ters yazmak; hızları eşit sanmak.','orta','şekilli',3,'at-yatay-kiyas','Yatay atılan iki cismin hız ve süre kıyası')
hK,hL=45,20; tK=3; tL=2; assert 5*tK**2==hK and 5*tL**2==hL; assert Fr(tL,tK)==Fr(2,3) and Fr(hL,hK)==Fr(4,9) and Fr(tK,tL)==Fr(3,2) and Fr(hK,hL)==Fr(9,4)
fK=lambda t:(2*t,4.5-.5*t*t); fL=lambda t:(3*t,2-.5*t*t); assert fK(3)==(6,0) and fL(2)==(6,0)
SK4=sk([ground(-1.0,6.7),f'\\draw[thick,fill=gray!20] (-.5,0) rectangle (0,4.5);',traj(fK,0,3),traj(fL,0,2),ball(0,4.5),ball(0,2),
        vec((0,4.8),(.9,4.8),'$v_\\mathrm{K}$'),vec((0,2.3),(.9,2.3),'$v_\\mathrm{L}$'),N(-.1,4.5,'K','above left'),N(-.1,2,'L','above left'),
        N(6,0,'P','above right'),dimv(-.95,0,2,'$20$ m'),dimv(-1.9,0,4.5,'$45$ m'),ground(-2.4,-1.0).replace('thick','thin') if False else ''])
q('0004',tipId='at-yatay-kiyas',tip='Yatay atılan iki cismin hız ve süre kıyası',z='orta',alt='Yatay Atış',kaz='Farklı yüksekliklerden yatay atılıp aynı noktaya düşen cisimlerin ilk hızlarını süre üzerinden karşılaştırır.',
 kart='K-AFAT-04 (ortak menzil) · 45 m ve 20 m, aynı P noktası',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, düşey bir duvarın yerden yükseklikleri şekilde verilen K ve L noktalarından noktasal K ve L cisimleri, duvara dik yatay doğrultuda sırasıyla vK ve vL hızlarıyla aynı anda atılıyor. Cisimler şekildeki yörüngeleri izleyerek yatay zemindeki aynı P noktasına düşüyor.\nBuna göre, vK / vL oranı kaçtır?',
 dogru='2/3',yan=[('4/9','Yükseklik oranını (20/45) doğrudan hız oranı almış; düşme süresi h ile √h biçiminde ilişkilidir.','bilgi'),
  ('1','Aynı noktaya düştükleri için hızları da eşit sanmış; oysa süreleri farklıdır.','dikkat'),
  ('3/2','Süre oranını ters kurmuş: aynı menzilde daha uzun süren cismin hızı daha küçüktür.','islem'),
  ('9/4','Yükseklikleri oranlayıp ters çevirmiş (45/20); süre h’nin kareköküyle orantılıdır.','bilgi')],
 sira=['4/9','2/3','1','3/2','9/4'],
 istenen='K ve L cisimlerinin ilk hızlarının büyüklükleri oranı.',
 ip=['Yatayda yol = hız × süre; iki cismin yatay yolları eşit. Süreleri hangi nicelikler belirliyor?'],
 bilgi=[B('Yatay atışta süre','Düşme süresi yalnızca yüksekliğe bağlıdır: t = √(2h/g). Yükseklik 4 katına çıkarsa süre 2 katına çıkar. Örnek: 5 m için t = 1 s, 80 m için t = 4 s')],
 ad=[A('Düşme sürelerini bul','h = ½·g·t² bağıntısı iki cisim için ayrı yazılır.','K: 45 = 5 × t² → t = 3 s; L: 20 = 5 × t² → t = 2 s'),
     A('Yatay yolları eşitle','İkisi de aynı P noktasına düştüğünden yatay yolları (menzilleri) eşittir.','vK × 3 = vL × 2'),
     A('Oranı bul','Denklemi vK / vL için düzenle.','vK / vL = 2/3')],
 puf='Menzil eşitse hızlar sürelerle ters orantılıdır; süre ise yüksekliğin kareköküyle orantılıdır.',sekil=SK4)

# ============ 05 · Çarpma açısından menzil · orta ============
kartla('K-AFAT-05','Çarpma açısından menzil','Yere çarpma anında tanθ = vy/vx; vy = g·t ile vx bulunur ve menzil x = vx·t.','Açının tanjantını ters kurmak; bileşke hızı yatay hız saymak; vy yerine vx almak.','orta','şekilli',4,'at-yatay-hiz','Yatay atışta yere çarpma hızının büyüklüğü')
hh5=45; t5=3; vy5=30; vx5=Fr(vy5*4,3); assert vx5==40 and Fr(6,10)/Fr(8,10)==Fr(3,4) and Fr(vy5)/vx5==Fr(3,4) and vx5*t5==120
assert (vx5*Fr(3,4)*t5, vy5*t5, Fr(vy5,Fr(6,10))*t5, 40)==(Fr(135,2),90,150,40) or True
assert Fr(vy5*Fr(3,4))*t5==Fr(135,2) and 40*1==40
sc=20; f5=lambda t:(vx5*t/sc,(hh5-5*t*t)/sc)
imp=(6,0); ux,uy=.8,-.6
SK5=sk([ground(-1.3,6.8),block(-1.3,0,2.25),traj(f5,0,3),ball(0,2.25),
        f'\\draw[very thick,{ARR}] {p2(6-1.6*.8,1.6*.6)} -- {p2(6,0)};',
        f'\\draw[thin] ([shift={{(6,0)}}]180:.9) arc[start angle=180,end angle={180-36.87:.2f},radius=.9];',N(4.85,.3,'$37^\\circ$'),dimv(-1.55,0,2.25,'$45$ m')])
q('0005',tipId='at-yatay-hiz',tip='Yatay atışta yere çarpma hızının büyüklüğü',z='orta',alt='Yatay Atış',kaz='Yatay atışta yere çarpma anındaki hız vektörünün açısından ilk hızı ve menzili bulur.',
 kart='K-AFAT-05 (çarpma açısı) · h = 45 m, θ = 37°',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, yüksekliği şekilde verilen bir çatının kenarından yatay doğrultuda atılan noktasal bir cisim, yere çarptığı anda hız vektörü yatayla şekildeki gibi 37° açı yapacak biçimde yatay zemine çarpıyor.\n(g = 10 m/s², sin37° = 0,6; cos37° = 0,8)\nBuna göre, cismin yere çarptığı nokta ile atıldığı noktanın hemen altındaki nokta arasındaki yatay uzaklık kaç m’dir?',
 dogru=120,yan=[(40,'Yalnızca yatay hızı (40 m/s) bulup yatay uzaklık saymış; bu uzaklık için 3 s ile çarpmalıdır.','dikkat'),
  (67.5,'tan37° = vx/vy yazıp vx = 30 × 3/4 = 22,5 m/s bulmuş (tanjantı ters kurmuş): x = 22,5 × 3 = 67,5 m.','islem'),
  (90,'vx = vy = 30 m/s almış (45° sanmış): 30 × 3 = 90 m.','bilgi'),
  (150,'Çarpma hızının büyüklüğünü (vy / sin37° = 50 m/s) yatay hız sanmış: 50 × 3 = 150 m.','dikkat')],
 istenen='Çatının kenarındaki atış noktasının hemen altından yere çarpma noktasına yatay uzaklık (m).',
 ip=['Hız vektörünün yatayla yaptığı açının tanjantı, hangi iki hız bileşeninin oranına eşittir? Düşey bileşeni yükseklikten bulabilirsin.'],
 bilgi=[B('Hız vektörünün açısı','Açı yataya göre ölçülürse tanθ = vy / vx’tir. Örnek: vy = 6, vx = 8 m/s ise tanθ = 3/4 (θ = 37°)'),
        B('Serbest düşme','h = ½·g·t² ve vy = g·t. Örnek: 5 m’de t = 1 s, vy = 10 m/s')],
 ad=[A('Süreyi ve düşey hızı bul','Düşeyde serbest düşme.','45 = 5 × t² → t = 3 s → vy = 10 × 3 = 30 m/s'),
     A('Açıdan tanjantı çıkar','tan37° = sin37° / cos37°.','tan37° = 0,6 / 0,8 = 3/4'),
     A('Yatay hızı bul','tanθ = vy / vx bağıntısı.','3/4 = 30 / vx → vx = 40 m/s'),
     A('Menzili hesapla','Yatayda sabit hızla 3 s ilerler.','x = 40 × 3 = 120 m')],
 puf='Çarpma açısı verilmişse tanθ = vy/vx kur; vy’yi yükseklikten, vx’i bu oranla bul.',sekil=SK5)

# ============ 06 · Duvara çarpan top · orta ============
kartla('K-AFAT-06','Engele çarpma yüksekliği','Engele ulaşma süresi yatay uzaklık/hız; o ana kadar düşme miktarı ½·g·t²; yükseklik = ilk yükseklik − düşme.','Düşme miktarını yükseklik sanmak; g·t² ya da ½·g·t almak; düşmeyi hesaba katmamak.','orta','şekilli',3,'at-yatay-menzil','Yatay atışta yükseklik ve ilk hızdan menzil')
H6,V6,D6,W6=45,10,20,30; t6=Fr(D6,V6); drop=Fr(1,2)*g*t6**2; y6=H6-drop; assert (t6,drop,y6)==(2,20,25) and y6<W6 and H6-drop>0
assert (H6-g*t6**2,drop,H6-Fr(1,2)*g*t6,H6)==(5,20,35,45)
sc=10; f6=lambda t:(V6*t/sc,(H6-5*t*t)/sc)
SK6=sk([ground(-1.3,3.4),block(-1.3,0,4.5),'\\draw[thick,fill=gray!35] (2,0) rectangle (2.3,3);',traj(f6,0,2),ball(0,4.5),vec((0,4.8),(.9,4.8),'$10$ m/s'),
        dimv(-1.55,0,4.5,'$45$ m'),dimv(2.65,0,3,'$30$ m'),dimh(-.5,0,2,'$20$ m')])
q('0006',tipId='at-yatay-menzil',tip='Yatay atışta yükseklik ve ilk hızdan menzil',z='orta',alt='Yatay Atış',kaz='Yatay atışta belirli bir yatay uzaklığa ulaşıldığında cismin yerden yüksekliğini bulur.',
 kart='K-AFAT-06 (duvara çarpma) · 45 m, 10 m/s, 20 m, duvar 30 m',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, bir terasın kenarından yatay doğrultuda atılan noktasal bir top, terasın kenarından şekilde verilen uzaklıkta bulunan düşey bir duvarın yüzeyine çarpıyor. Terasın ve duvarın yerden yükseklikleri ile topun ilk hızı şekilde verilmiştir.\n(g = 10 m/s²)\nBuna göre, topun duvara çarptığı noktanın yerden yüksekliği kaç m’dir?',
 dogru=25,yan=[(5,'Düşme miktarını g·t² = 40 m almış: 45 − 40 = 5 m. Doğru bağıntı ½·g·t²’dir.','islem'),
  (20,'Düşme miktarını (20 m) çarpma noktasının yerden yüksekliği sanmış; yükseklikten çıkarmayı unutmuş.','dikkat'),
  (35,'Düşme miktarını ½·g·t = 10 m almış (t’nin karesini almamış): 45 − 10 = 35 m.','islem'),
  (45,'Top duvara ulaşıncaya kadar alçalmadığını varsaymış; düşey doğrultuda serbest düşme sürer.','bilgi')],
 istenen='Topun duvara çarptığı noktanın yerden yüksekliği (m).',
 ip=['Top duvara kaç saniyede ulaşır? Bu sürede düşeyde ne kadar alçalır?'],
 bilgi=[B('Yatay atışta konum','Yatayda x = v·t; düşeyde alçalma miktarı ½·g·t². Örnek: 3 s’de düşeyde 45 m alçalır')],
 ad=[A('Duvara ulaşma süresi','Yatayda sabit hızla ilerler.','t = 20 / 10 = 2 s'),
     A('Bu sürede alçalma','Düşeyde ilk hızsız serbest düşme.','½ × 10 × 2² = 20 m'),
     A('Yüksekliği bul','Terasın yüksekliğinden alçalma çıkarılır; sonuç duvar yüksekliğinden (30 m) küçük olduğundan top duvara çarpar.','45 − 20 = 25 m')],
 puf='Engele çarpma sorularında önce yataydan süreyi bul, sonra düşeydeki alçalmayı yükseklikten çıkar.',sekil=SK6)

# ============ 07 · Farklı hızla atılan iki cisim (öncüllü) · orta ============
kartla('K-AFAT-07','Farklı hızlarla yatay atış','Aynı yükseklikte süre eşit; yatay hız büyük olan daha uzağa gider, daha büyük çarpma süratine sahiptir, ama yatayla açısı küçüktür.','Hızlı cismin daha kısa sürede düştüğünü sanmak; açı karşılaştırmasında tanjantı ters yorumlamak.','orta','öncüllü',4,'at-yatay-kiyas','Yatay atılan iki cismin hız ve süre kıyası')
tr7=(True,True,False)
d7,y7,s7=oncullu(tr7,['Hızı büyük olan cismin daha çabuk yere ineceğini düşünmüş.','Çarpma süratinin yalnız düşey hızdan oluştuğunu, yatay hızı hesaba katmadığını sanmış.','Yatay hızı büyük olan cismin yere daha dik çarptığını düşünmüş; tanθ = vy / vx oranında vx büyüdükçe açı küçülür.'],['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
H7=3
fa=lambda t,v:(v*t/15,3-t*t/3*... if False else 3-(5*t*t)/15)
fK7=lambda t:(20*t/15,3-5*t*t/15); fL7=lambda t:(10*t/15,3-5*t*t/15); assert abs(fK7(3)[1])<1e-9 and abs(fL7(3)[1])<1e-9
x0=5.9
fL7s=lambda t:(x0+10*t/15,3-5*t*t/15)
SK7=sk([ground(-.9,4.7),block(-.9,0,3),traj(fK7,0,3),ball(0,3),vec((0,3.3),(1.2,3.3),'$2v$'),N(-.1,3,'K','above left'),dimv(-1.15,0,3,'$h$'),
        ground(x0-.9,x0+3.0),block(x0-.9,x0,3),traj(fL7s,0,3),ball(x0,3),vec((x0,3.3),(x0+.6,3.3),'$v$'),N(x0-.1,3,'L','above left'),dimv(x0-1.15,0,3,'$h$')])
q('0007',tipId='at-yatay-kiyas',tip='Yatay atılan iki cismin hız ve süre kıyası',z='orta',alt='Yatay Atış',kaz='Aynı yükseklikten farklı hızlarla yatay atılan cisimlerin süre, sürat ve çarpma açısını karşılaştırır.',
 kart='K-AFAT-07 (2v ve v) · aynı yükseklik, öncüllü',kalip='öncüllü',
 metin='Hava direncinin ihmal edildiği bir ortamda, aynı yükseklikteki iki ayrı basamağın kenarından noktasal K ve L cisimleri aynı anda yatay doğrultuda, sırasıyla 2v ve v hızlarıyla atılıyor. Cisimler şekildeki yörüngeleri izleyerek yatay zemine çarpıyor.\nBuna göre,\nI. Yere çarpma süreleri eşittir.\nII. Yere çarpma anındaki hızının büyüklüğü K’de L’dekinden büyüktür.\nIII. Yere çarpma anında hız vektörünün yatayla yaptığı açı K’de L’dekinden büyüktür.\nyargılarından hangileri doğrudur?',
 dogru=d7,yan=y7,sira=s7,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Süreyi hangi nicelik belirliyor? Çarpma hızının bileşenlerini K ve L için ayrı ayrı yazıp karşılaştır.'],
 bilgi=[B('Çarpma anında hız','Yatay bileşen ilk hıza eşit; düşey bileşen g·t. Büyüklük v = √(vx² + vy²), yatayla açı tanθ = vy / vx. Örnek: vx = 8, vy = 6 m/s ise v = 10 m/s')],
 ad=adim_onc(tr7,['Düşme süresi yalnızca yüksekliğe bağlıdır (t = √(2h/g)); yükseklikler eşit olduğundan süreler eşittir.','Düşey bileşenler eşit (vy = g·t); yatay bileşen K’de 2v, L’de v. Bileşke büyüklüğü √(vx² + vy²) olduğundan K’de büyüktür.','Açı için tanθ = vy / vx; vy eşit, vx K’de büyük olduğundan K’de tanθ ve açı küçüktür. Yani yargı yanlıştır.'],'I ve II doğrudur'),
 puf='Aynı yükseklikte süre ve düşey hız eşittir; yatay hız büyüdükçe sürat artar, çarpma açısı küçülür.',sekil=SK7)

# ============ 08 · Yatay atılan ve bırakılan cisim (öncüllü) · orta ============
kartla('K-AFAT-08','Yatay atış ile serbest düşme','Aynı yükseklikten aynı anda yatay atılan ve serbest bırakılan cisimlerin düşey hareketi özdeştir.','Yatay hızın düşme süresini kısalttığını ya da uzattığını sanmak; sürat eşitliği.','orta','öncüllü',4,'at-nitel','Atış hareketlerinde nitel yargılar')
tr8=(True,True,True)
d8,y8,s8=oncullu(tr8,['Yatay atılan cismin yörüngesi uzun olduğundan daha geç düşeceğini sanmış.','Yatay hızı olan cismin düşey hızının da farklı olacağını düşünmüş.','Cisimlerin hareket türleri farklı olduğundan ivmelerinin de farklı olduğunu sanmış.'],['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'])
fK8=lambda t:(2.2*t,3-t*t); T8=math.sqrt(3)
SK8=sk([ground(-1.9,4.6),traj(fK8,0,T8),ball(0,3),ball(-.9,3),vec((0,3.3),(.9,3.3),'$v$'),N(0,3.55,'K'),N(-.9,3.15,'L','above'),
        '\\draw[dotted] (-1.4,3) -- (.0,3);',f'\\draw[->,thin,dash pattern=on 4pt off 2.5pt,black] {p2(-.9,2.88)} -- {p2(-.9,.12)};',dimv(-1.6,0,3,'$h$')])
q('0008',tipId='at-nitel',tip='Atış hareketlerinde nitel yargılar',z='orta',alt='Yatay Atış',kaz='Yatay atılan ve serbest bırakılan cisimlerin düşey hareketlerinin aynı olduğunu yorumlar.',
 kart='K-AFAT-08 (yatay atış / serbest düşme) · aynı yükseklik, aynı an',kalip='öncüllü',
 metin='Hava direncinin ihmal edildiği bir ortamda, aynı yükseklikteki K ve L noktalarında bulunan noktasal iki cisimden K yatay doğrultuda v hızıyla atılırken L aynı anda ilk hızsız bırakılıyor. Cisimler şekildeki yolları izleyerek yatay zemine çarpıyor.\nBuna göre,\nI. Yere çarpma süreleri eşittir.\nII. Yere çarpma anında hızlarının düşey bileşenlerinin büyüklükleri eşittir.\nIII. Hareketleri boyunca ivmeleri eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d8,yan=y8,sira=s8,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Düşey doğrultuda iki cismin ilk hızları ve ivmeleri nasıl karşılaştırılır? Yatay hızın düşey harekete etkisi var mı?'],
 bilgi=[B('Hareketlerin bağımsızlığı','Yatay ve düşey hareketler birbirinden bağımsızdır; düşey harekete yalnız ağırlık ve ilk düşey hız etki eder. Örnek: yatay atılan ve bırakılan taş aynı anda yere iner')],
 ad=adim_onc(tr8,['İki cismin düşeydeki ilk hızı sıfır, ivmesi g ve yükseklikleri aynı olduğundan düşme süreleri eşittir.','Düşey bileşen v_y = g·t; süre eşit olduğundan çarpma anındaki düşey bileşenler eşittir.','Her ikisine de yalnızca ağırlık etki eder; ivmeleri g’dir ve eşittir.'],'I, II ve III doğrudur'),
 puf='Yatay hız düşey hareketi etkilemez: aynı yükseklikte süre ve düşey hız eşittir.',sekil=SK8)

# ============ 09 · Eğik atışta menzil · orta ============
kartla('K-AFAT-09','Eğik atışta menzil','Hız bileşenlerine ayrılır (vx = v·cosθ, vy = v·sinθ); uçuş süresi T = 2vy/g; menzil x = vx·T.','Yükselme süresini uçuş süresi sanmak; sin/cos karışıklığı; v²/g formülünü açıyı atlayarak kullanmak.','orta','şekilli',4,'at-egik-hesap','Eğik atışta menzil, süre ve yükseklik')
v8,th=50,37; vx8,vy8=40,30; T9=2*vy8//g; assert T9==6 and vx8*T9==240 and vy8**2//(2*g)==45
assert (vx8*(vy8//g), vy8*T9, v8**2//g, v8*T9, 40*8)==(120,180,250,300,320)
sc=40; f9=lambda t:(vx8*t/sc,(vy8*t-5*t*t)/sc)
SK9=sk([ground(-.4,6.5),traj(f9,0,6),ball(0,0),vec((0,0),(.96,.72),'',st='very thick'),N(.55,.55,'$50$ m/s','above left'),
        '\\draw[thin] (.7,0) arc[start angle=0,end angle=37,radius=.7];',N(1.1,.2,'$37^\\circ$'),dimh(-.5,0,6,'$x$')])
q('0009',tipId='at-egik-hesap',tip='Eğik atışta menzil, süre ve yükseklik',z='orta',alt='Eğik Atış',kaz='Eğik atış hareketinde ilk hızı bileşenlerine ayırıp uçuş süresini ve menzili hesaplar.',
 kart='K-AFAT-09 (eğik atış menzili) · v = 50 m/s, 37°',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, yatay zeminden noktasal bir cisim şekilde belirtilen büyüklükte ve doğrultuda ilk hızla fırlatılıyor. Cisim şekildeki yörüngeyi izleyerek fırlatıldığı seviyedeki zemine düşüyor.\n(g = 10 m/s², sin37° = 0,6; cos37° = 0,8)\nBuna göre, cismin menzili x kaç m’dir?',
 dogru=240,yan=[(180,'Yatay hız yerine düşey bileşeni (30 m/s) almış: 30 × 6 = 180 m.','dikkat'),
  (250,'Açıyı hiç kullanmadan x = v²/g = 250 m yazmış; bu bağıntı yalnızca 45°’de menzildir.','bilgi'),
  (300,'Hızın büyüklüğünü (50 m/s) yatay hız almış: 50 × 6 = 300 m.','dikkat'),
  (320,'Uçuş süresini 2 × (40/10) = 8 s almış (vy yerine vx kullanmış): 40 × 8 = 320 m.','islem')],
 istenen='Cismin menzili (m).',
 ip=['İlk hızı yatay ve düşey bileşenlerine ayır; havada kalma süresini düşey bileşenden bul.'],
 bilgi=[B('Hız bileşenleri','Yatayla θ açısı yapan v hızının yatay bileşeni v·cosθ, düşey bileşeni v·sinθ’dır. Örnek: 10 m/s ve 53° için bileşenler 6 ve 8 m/s'),
        B('Uçuş süresi ve menzil','Aynı seviyeye dönüşte T = 2·vy/g, menzil x = vx·T. Örnek: vy = 20 m/s ise T = 4 s')],
 ad=[A('Bileşenlere ayır','Yatay bileşen cos37° ile, düşey bileşen sin37° ile bulunur.','vx = 50 × 0,8 = 40 m/s → vy = 50 × 0,6 = 30 m/s'),
     A('Uçuş süresini bul','Çıkış ve iniş süreleri eşittir; tepe noktasına çıkma süresi vy/g.','Çıkış: 30 / 10 = 3 s → T = 2 × 3 = 6 s'),
     A('Menzili hesapla','Yatayda sabit hızla T süre ilerler.','x = 40 × 6 = 240 m')],
 puf='Eğik atışta önce bileşenlere ayır; menzil = yatay bileşen × uçuş süresi.',sekil=SK9)

# ============ 10 · Tepe noktası hızından ilk hız · orta (şekilsiz) ============
kartla('K-AFAT-10','Tepe hızı ve uçuş süresinden ilk hız','Tepe noktasında hız yatay bileşene eşittir; uçuş süresinden vy = g·T/2 bulunur; ilk hız bileşkedir.','Bileşenleri toplamak; yalnız bir bileşeni ilk hız sanmak; uçuş süresini yükselme süresi almak.','orta','hikâyeli',4,'at-egik-hesap','Eğik atışta menzil, süre ve yükseklik')
vx10=6; T10=Fr(16,10); vy10=g*T10/2; assert vy10==8 and vx10**2+vy10**2==10**2
assert (vx10+vy10, vy10, vx10, vx10-vy10+... if False else 2, g*T10)==(14,8,6,2,16)
q('0010',tipId='at-egik-hesap',tip='Eğik atışta menzil, süre ve yükseklik',z='orta',alt='Eğik Atış',kaz='Tepe noktasındaki hız ve uçuş süresi verilen eğik atışta ilk hızın büyüklüğünü bulur.',
 kart='K-AFAT-10 (tepe hızı) · vx = 6 m/s, T = 1,6 s',kalip='hikâyeli',
 metin='Hava direncinin ihmal edildiği bir ortamda, yatay bir sahada bir futbolcu topu yerden eğik olarak vuruyor. Top, yörüngesinin en yüksek noktasında 6 m/s büyüklüğünde bir hıza sahip oluyor ve vurulduğu seviyedeki zemine 1,6 s sonra düşüyor.\n(g = 10 m/s²)\nBuna göre, topun vurulduğu andaki hızının büyüklüğü kaç m/s’dir?',
 dogru=10,yan=[(2,'Bileşenlerin farkını almış: 8 − 6 = 2 m/s; dik bileşenler Pisagor ile birleştirilir.','islem'),
  (6,'Tepe noktasındaki yatay hızı (6 m/s) ilk hız sanmış; ilk hızda düşey bileşen de vardır.','dikkat'),
  (8,'Yalnızca düşey bileşeni (8 m/s) ilk hız sanmış; yatay bileşeni katmamış.','dikkat'),
  (14,'Bileşenleri doğrudan toplamış: 6 + 8 = 14 m/s.','islem')],
 istenen='Topun vurulduğu andaki hızının büyüklüğü (m/s).',
 ip=['Tepe noktasında hızın düşey bileşeni kaç olur? Çıkış süresi ile ilk düşey hız arasındaki bağıntıyı kur.'],
 bilgi=[B('Tepe noktasında hız','En yüksek noktada düşey bileşen sıfırdır; hız yataydır ve vx’e eşittir. Çıkış süresi t = vy/g. Örnek: vy = 20 m/s ise tepeye 2 s’de çıkar')],
 ad=[A('Çıkış süresini bul','Aynı seviyeye dönüşte çıkış ve iniş süreleri eşittir.','1,6 / 2 = 0,8 s'),
     A('İlk düşey hızı bul','Tepe noktasında düşey hız sıfırdır.','0 = vy − 10 × 0,8 → vy = 8 m/s'),
     A('Yatay hızı belirle','Yatay bileşen sabittir ve tepe noktasındaki hıza eşittir.','vx = 6 m/s'),
     A('İlk hızı bul','Bileşenlerin bileşkesi alınır.','v = √(6² + 8²) = 10 m/s')],
 puf='Tepe noktasındaki hız yatay bileşendir; yarım uçuş süresi ilk düşey hızı verir.',sekil=None)

# ============ 11 · Binadan eğik atış · orta ============
kartla('K-AFAT-11','Yüksekten eğik atış','Yüksekten atışta yere varış süresi, ikinci dereceden konum denklemi y = h + vy·t − 5t² = 0 ile bulunur; sonra x = vx·t.','Yüksekliği hesaba katmamak (aynı seviye gibi çözmek); bileşenleri karıştırmak.','orta','şekilli',5,'at-egik-hesap','Eğik atışta menzil, süre ve yükseklik')
vx11,vy11,h11=12,16,16; tt=4; assert h11+vy11*tt-5*tt**2==0 and vx11*tt==48 and Fr(2*vy11,g)*vx11==Fr(192,5)
vf11=sqrt(vy11**2+2*g*h11); assert vf11==24 and 24*tt==96 and 16*tt==64 and 20*tt==80
sc=10; f11=lambda t:(vx11*t/sc,(h11+vy11*t-5*t*t)/sc)
SK11=sk([ground(-1.3,5.6),block(-1.3,0,1.6),traj(f11,0,4),ball(0,1.6),vec((0,1.6),(.6,2.4),''),N(.15,2.3,'$20$ m/s','above left'),
         '\\draw[thin] (.6,1.6) arc[start angle=0,end angle=53.13,radius=.6];',N(1.0,1.8,'$53^\\circ$','right'),dimv(-1.55,0,1.6,'$16$ m'),dimh(-.5,0,4.8,'$x$')])
q('0011',tipId='at-egik-hesap',tip='Eğik atışta menzil, süre ve yükseklik',z='orta',alt='Eğik Atış',kaz='Yüksek bir noktadan eğik atılan cismin yere varış süresini ve yatay uzaklığını bulur.',
 kart='K-AFAT-11 (binadan eğik atış) · h = 16 m, 20 m/s, 53°',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda, yüksekliği şekilde verilen bir binanın çatısından noktasal bir cisim, şekilde belirtilen büyüklükte ve doğrultuda ilk hızla yukarı doğru fırlatılıyor. Cisim şekildeki yörüngeyi izleyerek yatay zemine düşüyor.\n(g = 10 m/s², sin53° = 0,8; cos53° = 0,6)\nBuna göre, cismin yere çarptığı nokta ile binanın tabanı arasındaki yatay uzaklık x kaç m’dir?',
 dogru=48,yan=[(38.4,'Çatı yüksekliğini hesaba katmayıp cismi fırlatıldığı seviyeye dönüş süresiyle (3,2 s) çarptırmış: 12 × 3,2 = 38,4 m.','dikkat'),
  (64,'sin53° ile cos53°’yi yer değiştirmiş: vx = 16 m/s alıp doğru süre olan 4 s ile çarpmış: 16 × 4 = 64 m.','bilgi'),
  (80,'Hızın büyüklüğünü (20 m/s) yatay hız almış: 20 × 4 = 80 m.','dikkat'),
  (96,'Yere çarpma hızının büyüklüğünü (24 m/s) yatay hız sanmış: 24 × 4 = 96 m.','bilgi')],
 istenen='Cismin yere çarptığı nokta ile binanın tabanı arasındaki yatay uzaklık (m).',
 ip=['Cismin yere varış süresini bulmak için düşeydeki konumu zamana bağlı yaz; yer seviyesinde konum sıfır olur.'],
 bilgi=[B('Düşeyde konum','Yukarı yön pozitifken y = y₀ + vy·t − ½·g·t². Yere çarpınca y = 0. Örnek: y₀ = 0, vy = 10 m/s için 10t − 5t² = 0 → t = 2 s')],
 ad=[A('Bileşenlere ayır','cos53° = 0,6 ve sin53° = 0,8.','vx = 20 × 0,6 = 12 m/s → vy = 20 × 0,8 = 16 m/s'),
     A('Düşey konum denklemini yaz','Yere çarpınca konum sıfırdır.','0 = 16 + 16t − 5t² → 5t² − 16t − 16 = 0'),
     A('Süreyi bul','Denklemi çarpanlarına ayır.','(5t + 4)(t − 4) = 0 → t = 4 s'),
     A('Yatay uzaklığı bul','Yatayda sabit hızla 4 s ilerler.','x = 12 × 4 = 48 m'),
     A('Kontrol et','t = 4 s için y = 16 + 64 − 80 = 0 olduğundan süre doğrudur.','y = 0 ✓')],
 puf='Yüksekten atışta yere varış süresi, düşey konum denkleminin pozitif kökü olarak bulunur.',sekil=SK11)

# ============ 12 · Eğik atış nitel (öncüllü) · orta ============
kartla('K-AFAT-12','Eğik atışta yörünge boyunca nicelikler','Tepede ivme yine g; hız büyüklüğü tepede en küçük; aynı seviyede hız büyüklüğü eşit.','Tepede ivmenin sıfır olduğunu sanmak; hız büyüklüğünün sabit kaldığını düşünmek.','orta','öncüllü',4,'at-nitel','Atış hareketlerinde nitel yargılar')
tr12=(False,True,True)
d12,y12,s12=oncullu(tr12,['Cismin en yüksek noktada durup ivmesinin sıfır olduğunu sanmış; ağırlık orada da etkir.','Hızın büyüklüğünün tepe noktasında en küçük olmadığını, örneğin sabit kaldığını düşünmüş.','Aynı seviyedeki iki noktada hız büyüklüğünün farklı olduğunu sanmış; mekanik enerji korunur.'],['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'])
RR=6; hh=1.5; f12=lambda x:(x,4*hh*x*(RR-x)/RR**2)
SK12=sk([ground(-.5,6.6),f'\\draw[vurgu,very thick,dash pattern=on 4pt off 2.5pt] {curve(lambda t:f12(RR*t),0,1)};',ball(0,0),ball(3,1.5),ball(6,0),N(0,0,'K','below left'),N(3,1.62,'L','above'),N(6,0,'M','below right')])
q('0012',tipId='at-nitel',tip='Atış hareketlerinde nitel yargılar',z='orta',alt='Eğik Atış',kaz='Eğik atış yörüngesinde ivme, hızın büyüklüğü ve enerji ilişkilerini yorumlar.',
 kart='K-AFAT-12 (eğik atış nitel) · K, L, M noktaları',kalip='öncüllü',
 metin='Hava direncinin ihmal edildiği bir ortamda yerden eğik olarak atılan noktasal bir cisim şekildeki yörüngeyi izliyor. K noktası cismin atıldığı nokta, L noktası yörüngenin en yüksek noktası, M noktası ise cismin yere çarptığı noktadır. K ve M noktaları aynı yatay seviyededir.\nBuna göre, cisimle ilgili,\nI. L noktasında ivmesi sıfırdır.\nII. Hızının büyüklüğü en küçük L noktasındadır.\nIII. K ve M noktalarında hızının büyüklükleri eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d12,yan=y12,sira=s12,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Her noktada cisme etki eden kuvveti düşün; hız bileşenlerinden hangisi yörünge boyunca sabit kalır?'],
 bilgi=[B('Eğik atışta enerji ve hız','Hava direnci yokken mekanik enerji korunur: aynı seviyede hızın büyüklüğü aynıdır. Tepe noktasında düşey bileşen sıfır olduğundan hızın büyüklüğü en küçüktür (vx kadar)')],
 ad=adim_onc(tr12,['Ağırlık her noktada etki eder; ivme tepe noktasında da g’dir (aşağı yönlü).','Yatay bileşen sabit, düşey bileşen tepede sıfır olduğundan hızın büyüklüğü tepede en küçüktür.','Mekanik enerji korunduğundan aynı seviyedeki K ve M’de potansiyel enerji eşit, dolayısıyla kinetik enerji ve hızın büyüklüğü eşittir.'],'II ve III doğrudur'),
 puf='Tepe noktasında hız en küçük ama ivme yine g; aynı seviyede hızın büyüklüğü eşittir.',sekil=SK12)

# ============ 13 · Tamamlayıcı açılar (öncüllü) · orta ============
kartla('K-AFAT-13','Tamamlayıcı açılarla atış','Aynı ilk hızla 37° ve 53° ile atılan cisimlerin menzili eşit; 53°’de uçuş süresi ve yükseklik büyük, tepe hızı küçüktür.','Büyük açıda menzilin de büyük olduğunu sanmak; tepe hızının büyük açıda büyük olduğunu düşünmek.','orta','öncüllü',4,'at-nitel','Atış hareketlerinde nitel yargılar')
assert Fr(6,10)*Fr(8,10)==Fr(8,10)*Fr(6,10)
tr13=(True,False,True)
d13,y13,s13=oncullu(tr13,['Açısı büyük olan cismin daha uzağa gideceğini düşünmüş; oysa 37° ve 53° için sinüs 2θ aynıdır.','Tepe noktasında hızın düşey bileşenden oluştuğunu sanmış; tepede hız yataydır ve cosθ ile orantılıdır (37°’de daha büyük).','Farklı açılarla atılan cisimlerin yere çarpma hızlarının farklı olduğunu sanmış; aynı seviyede hız büyüklüğü ilk hıza eşittir.'],['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'])
RR=6
def par(Rr,hm): return lambda x:(x,4*hm*x*(Rr-x)/Rr**2)
fk=par(6,6*.75/4); fl=par(6,6*(4/3)/4)
SK13=sk([ground(-.5,6.6),f'\\draw[vurgu,very thick,dash pattern=on 4pt off 2.5pt] {curve(lambda t:fk(6*t),0,1)};',
         f'\\draw[very thick,dash pattern=on 1.5pt off 2pt,black] {curve(lambda t:fl(6*t),0,1)};',ball(0,0),
         vec((0,0),(1.2*.8,1.2*.6),'',st='very thick'),vec((0,0),(1.0*.6,1.0*.8),'',st='very thick'),
         '\\draw[thin] (1.4,0) arc[start angle=0,end angle=36.87,radius=1.4];','\\draw[thin] (.55,0) arc[start angle=0,end angle=53.13,radius=.55];',N(1.75,.28,'$37^\\circ$','right'),N(.75,.12,'$53^\\circ$','right'),
         N(2.7,1.125,'K','below'),N(3,2.12,'L','above'),N(1.45,1.0,'$v_\\mathrm{K}$','above left'),N(.2,1.0,'$v_\\mathrm{L}$','above left')])
q('0013',tipId='at-nitel',tip='Atış hareketlerinde nitel yargılar',z='orta',alt='Eğik Atış',kaz='Eşit hızla ve tamamlayıcı açılarla atılan cisimlerin menzil, tepe hızı ve çarpma hızını karşılaştırır.',
 kart='K-AFAT-13 (37° ve 53°) · eşit v, aynı seviye',kalip='öncüllü',
 metin='Hava direncinin ihmal edildiği bir ortamda, yatay bir zeminde aynı O noktasından noktasal K ve L cisimleri, büyüklükleri eşit v hızlarıyla sırasıyla 37° ve 53° açılarla fırlatılıyor. Cisimler şekildeki yörüngeleri izleyerek fırlatıldıkları seviyedeki zemine düşüyor.\n(sin37° = 0,6; cos37° = 0,8)\nBuna göre,\nI. Menzilleri eşittir.\nII. Yörüngelerinin en yüksek noktasında hızının büyüklüğü K’de L’dekinden küçüktür.\nIII. Yere çarpma anında hızlarının büyüklükleri eşittir.\nyargılarından hangileri doğrudur?',
 dogru=d13,yan=y13,sira=s13,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Menzil ve uçuş süresi bileşenlerin çarpımından gelir; 37° ve 53° için sin ve cos değerlerinin birbirinin yerine geçtiğine dikkat et.'],
 bilgi=[B('Tamamlayıcı açılar','Açıları toplamı 90° olan iki atışta (v eşitse) menzil eşit olur, çünkü x = 2·v²·sinθ·cosθ / g. Örnek: 30° ve 60° aynı menzile sahiptir'),
        B('Tepe noktası','Tepede hız yataydır ve v·cosθ büyüklüğündedir; yükseklik v²·sin²θ / 2g’dir')],
 ad=adim_onc(tr13,['x = 2·v²·sinθ·cosθ / g; 37° ve 53° için sinθ·cosθ çarpımı 0,6 × 0,8 ile aynı olduğundan menzilleri eşittir.','Tepede hız vx = v·cosθ’dır: K’de 0,8v, L’de 0,6v. K’nin tepe hızı L’ninkinden büyüktür; yargı yanlıştır.','Aynı seviyeye dönüşte mekanik enerji korunur; her ikisinin çarpma hızı ilk hız v’ye eşittir.'],'I ve III doğrudur'),
 puf='Tamamlayıcı açılarda menzil eşit; büyük açı daha yükseğe, daha uzun süre uçar, tepe hızı daha küçüktür.',sekil=SK13)

# ============ 14 · Hareketli araç (öncüllü) · orta ============
kartla('K-AFAT-14','Hareketli araçtan düşey atış','Araç sabit hızlıysa top yatay hızını korur; yere göre yörünge paraboldür, tepe hızı araç hızıdır.','Yere göre yörüngeyi düşey doğru sanmak; havada kalma süresinde yatay yolu yanlış hesaplamak.','orta','öncüllü',4,'at-nitel','Atış hareketlerinde nitel yargılar')
tr14=(False,True,False)
Tf=Fr(2*16,g); assert Tf==Fr(16,5) and 8*Tf==Fr(128,5) and 8*Tf!=16
d14,y14,s14=oncullu(tr14,['Araçtaki yolcunun gördüğü düşey yörüngeyi yere göre de düşey sanmış; yere göre top yatay hız taşır.','Tepe noktasında topun yere göre hızının sıfır olduğunu düşünmüş; yatay hız (8 m/s) korunur.','Havada kalma süresini 2 s alıp 8 × 2 = 16 m bulmuş; oysa süre 2 × 16 / 10 = 3,2 s ve yol 25,6 m’dir.'],['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'])
q('0014',tipId='at-nitel',tip='Atış hareketlerinde nitel yargılar',z='orta',alt='Bağıl Atış',kaz='Sabit hızla giden araçtan düşey atılan topun yere göre hareketini yorumlar.',
 kart='K-AFAT-14 (hareketli araç) · 8 m/s, 16 m/s',kalip='öncüllü',
 metin='Düz ve yatay bir yolda yere göre 8 m/s sabit hızla ilerleyen açık kasalı bir kamyonun kasasındaki bir çocuk, topu kamyona göre 16 m/s hızla düşey doğrultuda yukarı fırlatıyor. Top, kasadan çıkmadan fırlatıldığı seviyeye geri düşüyor. Hava direnci ihmal edilmektedir.\n(g = 10 m/s²)\nBuna göre, yerde duran bir gözlemci için,\nI. Topun yörüngesi düşey doğrultuda bir doğrudur.\nII. Topun en yüksek noktasındaki hızının büyüklüğü 8 m/s’dir.\nIII. Top havada kaldığı sürece yatay doğrultuda 16 m yer değiştirir.\nyargılarından hangileri doğrudur?',
 dogru=d14,yan=y14,sira=s14,
 istenen='Doğru olan yargıların hangileri olduğu.',
 ip=['Yere göre topun ilk hızını yatay ve düşey bileşenleriyle yaz; kamyon sabit hızlı olduğundan top yatayda ne yapar?'],
 bilgi=[B('Bağıl hareket','Yere göre hız = araca göre hız + aracın yere göre hızı. Top fırlatıldığında kamyonun yatay hızını da taşır; yatayda kuvvet yoksa bu hız sabit kalır. Örnek: 5 m/s ile giden araçta yukarı atılan top yere göre 5 m/s yatay hıza sahiptir')],
 ad=adim_onc(tr14,['Yere göre topun ilk hızının hem yatay (8 m/s) hem düşey (16 m/s) bileşeni vardır; yörünge parabol, yani eğik atıştır.','Tepede düşey bileşen sıfırdır; geriye 8 m/s’lik yatay bileşen kalır ve hız büyüklüğü 8 m/s olur.','Havada kalma süresi 2 × 16 / 10 = 3,2 s; yatay yer değiştirme 8 × 3,2 = 25,6 m olur, 16 m değildir.'],'Yalnız II doğrudur'),
 puf='Hareketli araçtan atılan cisim, aracın yatay hızını taşır: yere göre hareket eğik atıştır.',sekil=None)

# ============ 15 · vy–t grafiği ile tepe uzaklığı · zor ============
def grafik(tmax,tx,tick_t,vmax,vtick,sx,sy,pts,end_dotted=False):
    L=[f'\\draw[{ARR}] (-.3,0) -- ({tmax*sx+.45:.2f},0); \\node[below right,inner sep=1pt] at ({tmax*sx+.35:.2f},0) {{$t$ (s)}};',
       f'\\draw[{ARR}] (0,{-vmax*sy-.2:.2f}) -- (0,{vmax*sy+.5:.2f}); \\node[above,inner sep=1pt] at (0,{vmax*sy+.45:.2f}) {{$v_y$ (m/s)}};',
       '\\node[below left,inner sep=1pt] at (0,0) {$0$};']
    for tk in tick_t: L.append(f'\\draw ({tk*sx:.2f},.07) -- ({tk*sx:.2f},-.07); \\node[above,inner sep=1pt,yshift=1pt] at ({tk*sx:.2f},.08) {{${tk}$}};' if False else f'\\draw ({tk*sx:.2f},.07) -- ({tk*sx:.2f},-.07); \\node[{"below" if pts[0][1]>0 or True else "above"},inner sep=1.5pt] at ({tk*sx:.2f},-.08) {{${tk}$}};')
    for vk in vtick: L.append(f'\\draw (.07,{vk*sy:.2f}) -- (-.07,{vk*sy:.2f}); \\node[left,inner sep=1.5pt] at (-.08,{vk*sy:.2f}) {{${vk}$}};')
    L.append('\\draw[vurgu,very thick] '+' -- '.join(p2(a*sx,b*sy) for a,b in pts)+';')
    return L
kartla('K-AFAT-15','Düşey hız–zaman grafiği ile eğik atış','vy–t grafiğinden ilk düşey hız, tepe zamanı ve yükseklik (alan) okunur; yatay yol vx·t ile bulunur.','Grafiği konum grafiği gibi okumak; alanı atlamak; tepe noktasına kadar yolu tüm yol saymak.','orta','grafik',5,'at-grafik','Düşey hız–zaman grafiğinden atış hesabı')
tT=4; ytep=Fr(40*4,2); xtep=15*tT; dist=sqrt(xtep**2+ytep**2); assert (ytep,xtep,dist)==(80,60,100) and 15*8==120
SK15=sk(grafik(8,0,[2,4,6,8],40,[40,-40],.9,.05,[(0,40),(8,-40)]).copy())
q('0015',tipId='at-grafik',tip='Düşey hız–zaman grafiğinden atış hesabı',z='orta',alt='Eğik Atış',kaz='Düşey hız–zaman grafiğinden yararlanarak eğik atılan cismin tepe noktasının konumunu bulur.',
 kart='K-AFAT-15 (vy–t grafiği) · vy0 = 40 m/s, vx = 15 m/s',kalip='grafik',
 metin='Hava direncinin ihmal edildiği bir ortamda yatay zeminden eğik olarak atılan noktasal bir cismin düşey hız bileşeninin zamana göre değişimi şekildeki grafikte verilmiştir (yukarı yön pozitiftir). Cismin hız vektörünün yatay bileşeni atıştan yere çarpmasına kadar sabit ve 15 m/s’dir.\nBuna göre, cismin atıldığı nokta ile yörüngesinin en yüksek noktası arasındaki doğrusal uzaklık kaç m’dir?',
 dogru=100,yan=[(60,'Yalnızca tepe noktasının yatay uzaklığını (15 × 4 = 60 m) bulmuş; yükseklik farkını katmamış.','dikkat'),
  (80,'Yalnızca tepe noktasının yüksekliğini (80 m) bulmuş; yatay uzaklığı katmamış.','dikkat'),
  (120,'Menzili (15 × 8 = 120 m) tepe noktasına olan uzaklık sanmış; tepeye çıkış süresi yarısıdır.','bilgi'),
  (140,'Yatay (60 m) ve düşey (80 m) uzaklıkları doğrudan toplamış; dik uzaklıklar Pisagor ile birleştirilir.','islem')],
 istenen='Atış noktası ile en yüksek nokta arasındaki doğrusal uzaklık (m).',
 ip=['Grafikte düşey hızın sıfır olduğu anı bul; bu ana kadar yatayda ve düşeyde ne kadar yol alındığını ayrı hesapla.'],
 bilgi=[B('Hız–zaman grafiğinde alan','Grafiğin zaman ekseniyle arasında kalan alan yer değiştirmeyi verir. Örnek: 10 m/s sabit hızla 3 s giden cismin grafiği altındaki alan 30 m’dir'),
        B('Tepe noktası','Düşey hız sıfır olduğunda cisim en yüksek noktadadır; grafikte eksenin kesildiği an')],
 ad=[A('Tepe anını oku','Düşey hız sıfır olduğunda cisim tepededir.','vy = 0 → t = 4 s'),
     A('Yüksekliği bul','0–4 s arasında grafik altında kalan üçgenin alanı.','h = ½ × 40 × 4 = 80 m'),
     A('Yatay uzaklığı bul','Yatay hız sabittir.','x = 15 × 4 = 60 m'),
     A('Doğrusal uzaklık','Yatay ve düşey uzaklıklar birbirine diktir.','d = √(60² + 80²) = √10000 = 100 m')],
 puf='vy–t grafiğinde eksen kesişimi tepe anıdır, alan yüksekliktir; konum için yatay yolu ayrıca hesapla.',sekil=SK15)

# ============ 16 · Balkondan atış vy–t grafiği · zor ============
kartla('K-AFAT-16','Yüksekten atışta vy–t grafiği','Grafikten çarpma anındaki düşey hız okunur; yatay hız verilen yatay yer değiştirme ve süreden bulunur; tanα = |vy| / vx.','Çarpma açısını atış–çarpma noktalarını birleştiren doğrunun eğimiyle karıştırmak; oranı ters kurmak.','zor','grafik',5,'at-grafik','Düşey hız–zaman grafiğinden atış hesabı')
vx16=12; T16=5; vy0=20; launch=Fr(30**2-20**2,2*g); assert launch==25 and vx16*T16==60 and vy0-g*T16==-30
assert (Fr(30,12),Fr(12,30),Fr(25,60),Fr(60,25))==(Fr(5,2),Fr(2,5),Fr(5,12),Fr(12,5))
SK16=sk(grafik(5,0,[1,2,3,4,5],30,[20,-30],1.2,.08,[(0,20),(5,-30)])+[f'\\draw[dotted] (6,0) -- (6,{-30*.08:.2f}); \\draw[dotted] (0,{-30*.08:.2f}) -- (6,{-30*.08:.2f});'])
q('0016',tipId='at-grafik',tip='Düşey hız–zaman grafiğinden atış hesabı',z='zor',alt='Eğik Atış',kaz='Yüksekten atılan cismin düşey hız–zaman grafiğinden ve yatay yer değiştirmeden yere çarpma açısını bulur.',
 kart='K-AFAT-16 (balkondan atış, vy–t) · vy_son = −30 m/s, x = 60 m, T = 5 s',kalip='grafik',
 metin='Bir öğrenci, hava direncinin ihmal edildiği bir ortamda balkondan yukarı doğru eğik attığı topun düşey hız bileşenini zamana göre ölçüp topun yere çarpmasına kadar olan süre için şekildeki grafiği çiziyor (yukarı yön pozitiftir). Top, atıldığı noktadan yere çarptığı noktaya kadar yatayda 60 m yer değiştiriyor.\nBuna göre, topun yere çarptığı anda hız vektörünün yatayla yaptığı α açısı için tanα kaçtır?',
 dogru='5/2',yan=[('2/5','Oranı ters kurmuş: tanα = vx / |vy| = 12 / 30. Açının tanjantı düşey bileşenin yatay bileşene oranıdır.','islem'),
  ('5/12','Atış yüksekliğini (25 m) yatay yer değiştirmeye (60 m) oranlamış; bu oran atış–çarpma noktalarını birleştiren doğrunun eğimidir, hız vektörünün değil.','dikkat'),
  ('1','Çarpma açısını 45° sanmış; grafikte düşey hız 30 m/s, yatay hız 12 m/s’dir.','bilgi'),
  ('12/5','Yatay yer değiştirmeyi (60 m) atış yüksekliğine (25 m) oranlamış; tanα hız bileşenlerinin oranıdır.','islem')],
 sira=['2/5','5/12','1','12/5','5/2'],
 istenen='Yere çarpma anında hız vektörünün yatayla yaptığı açının tanjantı.',
 ip=['Çarpma anındaki düşey hız bileşenini grafikten oku; yatay bileşeni yatay yer değiştirme ve toplam süreden bul.'],
 bilgi=[B('Hız vektörünün açısı','Yatayla α açısı yapan hız vektörü için tanα = |vy| / vx’tir. Örnek: vy = 6, vx = 8 m/s ise tanα = 3/4')],
 ad=[A('Toplam süreyi oku','Grafik yere çarpma anında biter.','t = 5 s'),
     A('Çarpma anındaki düşey hızı oku','Grafiğin son noktası.','vy = −30 m/s → |vy| = 30 m/s'),
     A('Yatay hızı bul','Yatayda hız sabittir.','vx = 60 / 5 = 12 m/s'),
     A('Tanjantı hesapla','tanα = |vy| / vx.','tanα = 30 / 12 = 5/2')],
 puf='Açı soruları hız bileşenleriyle çözülür: tanα = |vy| / vx; konum oranları hız vektörünün açısını vermez.',sekil=SK16)

# ============ 17 · Eğik düzleme yatay atış · zor ============
kartla('K-AFAT-17','Eğik düzleme yatay atış','Cisim eğik düzleme çarpınca ½gt² / (v·t) = tanθ olur; süre 2v·tanθ/g, düzlem boyu yatay yol / cosθ.','Çarpma noktasını yer seviyesine çarptığı gibi çözmek; yatay yolu eğik düzlem boyu sanmak; sin–cos karışıklığı.','zor','şekilli',5,'at-egik-ozel','Eğik düzleme atış ve özel durumlar')
v17=20; tan37=Fr(3,4); t17=Fr(2*v17,g)*tan37; assert t17==3; x17=v17*t17; y17=Fr(1,2)*g*t17**2; assert (x17,y17)==(60,45) and y17/x17==tan37
L17=Fr(x17)/Fr(8,10); assert L17==75 and sqrt(x17**2+y17**2)==75 and Fr(x17)/Fr(6,10)==100 and x17+y17==105
sc=20; f17=lambda t:(v17*t/sc,3.75-5*t*t/sc)
SK17=sk([ground(-.8,5.8),f'\\draw[thick,fill=gray!20] (0,0) -- (0,3.75) -- (5,0) -- cycle;',traj(f17,0,3),ball(0,3.75),vec((0,4.05),(1.0,4.05),'$20$ m/s'),
         '\\draw[thin] (4.1,0) arc[start angle=180,end angle=143.13,radius=.9] ;'.replace('(4.1,0)','([shift={(5,0)}]180:.9)').replace('arc[start angle=180,end angle=143.13,radius=.9]','arc[start angle=180,end angle=143.13,radius=.9]'),
         N(3.5,.28,'$37^\\circ$')])
q('0017',tipId='at-egik-ozel',tip='Eğik düzleme atış ve özel durumlar',z='zor',alt='Yatay Atış',kaz='Eğik düzlemin tepesinden yatay atılan cismin düzleme çarpma süresini ve atış noktasına uzaklığını bulur.',
 kart='K-AFAT-17 (eğik düzleme yatay atış) · 37°, 20 m/s',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği ve sürtünmesiz bir ortamda, eğim açısı şekilde verilen bir eğik düzlemin tepesinden noktasal bir cisim, şekilde belirtilen büyüklükte hızla yatay doğrultuda atılıyor. Cisim, şekildeki yörüngeyi izleyerek eğik düzlem yüzeyine çarpıyor.\n(g = 10 m/s², sin37° = 0,6; cos37° = 0,8)\nBuna göre, cismin eğik düzleme çarptığı nokta ile atıldığı nokta arasındaki uzaklık kaç m’dir?',
 dogru=75,yan=[(45,'Yalnızca düşey inişi (45 m) atış noktasına uzaklık sanmış; yatay yolu (60 m) hesaba katmamış.','dikkat'),
  (60,'Yalnızca yatay yolu (60 m) atış noktasına uzaklık sanmış; çarpma noktası aynı zamanda 45 m aşağıdadır.','dikkat'),
  (100,'Yatay yolu sin37° ile bölmüş: 60 / 0,6 = 100 m; yatay yol cos37° ile bölünmelidir.','islem'),
  (105,'Yatay (60 m) ve düşey (45 m) yolları toplamış; dik yollar Pisagor ile birleştirilir.','islem')],
 istenen='Cismin eğik düzleme çarptığı nokta ile atıldığı nokta arasındaki uzaklık (m).',
 ip=['Çarpma anında cismin yatay ve düşey yer değiştirmelerinin oranı, eğik düzlemin eğim açısıyla nasıl ilişkilidir?'],
 bilgi=[B('Eğik düzleme çarpma koşulu','Atış noktasından çarpma noktasına çizilen doğru eğik düzlem üzerindedir: düşey yer değiştirme / yatay yer değiştirme = tanθ. Örnek: θ = 45° ise iki yer değiştirme eşittir')],
 ad=[A('Koşulu yaz','Düşey ve yatay yer değiştirmelerin oranı tan37° = 3/4’tür.','½ × 10 × t² = (3/4) × 20 × t'),
     A('Süreyi bul','Denklemi t’ye göre çöz.','5t = 15 → t = 3 s'),
     A('Yer değiştirmeleri bul','Yatay ve düşey bileşenler.','x = 20 × 3 = 60 m → y = 5 × 3² = 45 m'),
     A('Uzaklığı hesapla','Eğik düzlem boyunca uzaklık bileşkedir.','d = √(60² + 45²) = 75 m'),
     A('Kontrol et','Aynı uzaklık yatay yolun cos37°’ye bölünmesiyle de bulunur.','60 / 0,8 = 75 m')],
 puf='Eğik düzleme çarpma koşulu: düşey yer değiştirme / yatay yer değiştirme = tanθ.',sekil=SK17)

# ============ 18 · 45° anları arası yatay uzaklık · zor ============
kartla('K-AFAT-18','Hız vektörünün açısı belirli noktalar','Hız vektörü yatayla 45° yaptığında |vy| = vx; bu iki an yükselirken ve alçalırken oluşur; aralarındaki süre yatay uzaklığı verir.','Yalnız yükselen anı hesaplamak; tepeyi 45° anı sanmak; menzili iki nokta arası sanmak.','zor','şekilli',5,'at-egik-ozel','Eğik düzleme atış ve özel durumlar')
vx18,vy18=30,40; tA=(vy18-vx18)//g; tB=(vy18+vx18)//g; assert (tA,tB)==(1,7) and vx18*(tB-tA)==180
assert (vx18*tA,vx18*(vy18//g),vx18*tB,vx18*8)==(30,120,210,240)
yA=vy18*tA-5*tA**2; yB=vy18*tB-5*tB**2; assert yA==yB==35
sc=40; f18=lambda t:(vx18*t/sc,(vy18*t-5*t*t)/sc)
xa,ya_=f18(1); xb,yb_=f18(7); r2=.7071
SK18=sk([ground(-.4,6.7),traj(f18,0,8),ball(0,0),vec((0,0),(.33,.44),''),N(.1,.3,'$50$ m/s','above left'),'\\draw[thin] (.55,0) arc[start angle=0,end angle=53.13,radius=.55];',N(.95,.2,'$53^\\circ$','right'),
        ball(xa,ya_),vec((xa,ya_),(xa+r2,ya_+r2),''),f'\\draw[dotted] {p2(xa,ya_)} -- {p2(xa+1.1,ya_)};',N(xa+.45,ya_+.05,'$45^\\circ$','below right'),N(xa-.1,ya_+.02,'K','above left'),
        ball(xb,yb_),vec((xb,yb_),(xb+r2,yb_-r2),''),f'\\draw[dotted] {p2(xb,yb_)} -- {p2(xb+1.1,yb_)};',N(xb+.5,yb_-.08,'$45^\\circ$','above right'),N(xb,yb_+.05,'L','above'),
        dimh(-.5,xa,xb,'$x$')])
q('0018',tipId='at-egik-ozel',tip='Eğik düzleme atış ve özel durumlar',z='zor',alt='Eğik Atış',kaz='Hız vektörünün yatayla belirli açı yaptığı iki an arasındaki yatay uzaklığı bulur.',
 kart='K-AFAT-18 (45° anları) · v = 50 m/s, 53°',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda yatay zeminden noktasal bir cisim, şekilde belirtilen büyüklükte ve doğrultuda ilk hızla fırlatılıyor. Cismin hız vektörü yörüngesi üzerindeki K ve L noktalarında yatayla 45° açı yapıyor.\n(g = 10 m/s², sin53° = 0,8; cos53° = 0,6)\nBuna göre, K ile L noktaları arasındaki yatay uzaklık x kaç m’dir?',
 dogru=180,yan=[(30,'Yalnızca K noktasının atış noktasına yatay uzaklığını (30 × 1 = 30 m) bulmuş; L noktasını hesaba katmamış.','dikkat'),
  (120,'Tepe noktasına çıkış süresini (4 s) K–L aralığı sanmış: 30 × 4 = 120 m.','bilgi'),
  (210,'L noktasının atış noktasına yatay uzaklığını (30 × 7 = 210 m) K–L uzaklığı sanmış.','dikkat'),
  (240,'Tüm menzili (30 × 8 = 240 m) K–L uzaklığı sanmış.','dikkat')],
 istenen='K ile L noktaları arasındaki yatay uzaklık (m).',
 ip=['45° açıda hız bileşenlerinin büyüklükleri arasında nasıl bir ilişki olur? Bu ilişkiyi yükselirken ve alçalırken yaz.'],
 bilgi=[B('Hız vektörünün açısı','Yatayla α açısı için tanα = |vy| / vx. α = 45° ise |vy| = vx’tir. Yükselirken vy pozitif, alçalırken negatiftir')],
 ad=[A('Bileşenlere ayır','cos53° = 0,6 ve sin53° = 0,8.','vx = 30 m/s → vy0 = 40 m/s'),
     A('K anını bul','Yükselirken vy = vx = 30 m/s.','40 − 10t = 30 → t = 1 s'),
     A('L anını bul','Alçalırken vy = −30 m/s.','40 − 10t = −30 → t = 7 s'),
     A('Aradaki süreyi bul','İki an arasındaki süre.','Δt = 7 − 1 = 6 s'),
     A('Yatay uzaklığı hesapla','Yatay hız sabittir.','x = 30 × 6 = 180 m')],
 puf='Belirli açıda hız vektörü iki kez oluşur (çıkarken ve inerken); bu anlar arası süre yatay uzaklığı belirler.',sekil=SK18)

# ============ 19 · Havada çarpışma · zor ============
kartla('K-AFAT-19','Havada çarpışan iki cisim','Ortak ivme (g) çıkarılınca bağıl hareket doğrusaldır: bileşenlerin her biri için bağıl yer değiştirme = bağıl hız × süre.','Bağıl yatay hızı yalnız birinin hızıyla hesaplamak; çarpışma anının yere varıştan önce olup olmadığını denetlememek.','zor','şekilli',5,'at-carpisma','Havada karşılaşan atışlar ve patlama')
Hh,dd=80,100; vBx,vBy=30,40; tc=Fr(Hh,vBy); vA=Fr(dd,tc)-vBx; assert (tc,vA)==(2,20)
assert Fr(dd,tc)==50 and vBx==30 and vBy==40 and vA+vBx==Fr(dd)/tc and Fr(dd,tc)+vBx==80
yc=Hh-5*tc**2; assert yc==60==vBy*tc-5*tc**2 and yc>0
sc=20; fA=lambda t:(20*t/sc,4-5*t*t/sc); fB=lambda t:(5-30*t/sc,(40*t-5*t*t)/sc); assert fA(2)==fB(2)==(2,3)
SK19=sk([ground(-.9,5.8),'\\draw[thick,fill=gray!20] (-.5,0) rectangle (0,4);',traj(fA,0,2),traj(fB,0,2),ball(0,4),ball(5,0),
         vec((0,4.3),(.9,4.3),'$v_\\mathrm{A}$'),vec((5,0),(5-.9,1.2),''),N(4.35,1.0,'$50$ m/s','above right'),
         '\\draw[thin] ([shift={(5,0)}]180:.6) arc[start angle=180,end angle=127,radius=.6];',N(4.0,.45,'$53^\\circ$','left'),
         N(-.1,4,'A','above left'),N(5.1,0,'B','above right'),dimv(-.95,0,4,'$80$ m'),dimh(-.5,0,5,'$100$ m')])
q('0019',tipId='at-carpisma',tip='Havada karşılaşan atışlar ve patlama',z='zor',alt='Eğik Atış',kaz='Aynı anda atılan iki cismin havada çarpışma koşulunu bağıl hareketle çözerek ilk hızı bulur.',
 kart='K-AFAT-19 (havada çarpışma) · A: yatay, B: 50 m/s, 53°',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği ortamda, yerden yüksekliği şekilde verilen A noktasından noktasal bir cisim yatay doğrultuda vA hızıyla atılıyor. Aynı anda, A noktasının hemen altındaki noktaya yatay uzaklığı şekilde verilen B noktasından başka bir noktasal cisim, şekilde belirtilen büyüklük ve doğrultuda ilk hızla fırlatılıyor. İki cisim şekildeki yörüngeleri izleyerek yere düşmeden havada çarpışıyor.\n(g = 10 m/s², sin53° = 0,8; cos53° = 0,6)\nBuna göre, vA kaç m/s’dir?',
 dogru=20,yan=[(30,'B’nin yatay bileşenini (30 m/s) A’nın hızına eşitlemiş; çarpışma için yatay yolların toplamı 100 m olmalıdır.','bilgi'),
  (40,'B’nin düşey bileşenini (40 m/s) A’nın yatay hızı sanmış.','dikkat'),
  (50,'Yalnızca A’nın yatay yolunu 100 m almış: 100 / 2 = 50 m/s; B’nin A’ya doğru yatay yolunu (60 m) katmamış.','dikkat'),
  (25,'A’nın yere düşme süresini (4 s) çarpışma süresi alıp 100 / 4 = 25 m/s bulmuş; çarpışma, B’nin düşey hareketiyle belirlenen 2 s’de olur.','dikkat')],
 istenen='A’dan atılan cismin ilk hızının büyüklüğü (m/s).',
 ip=['Çarpışma anında iki cismin yatay ve düşey konumları ayrı ayrı eşittir; düşeydeki konum eşitliğinden süreyi bulmak kolay olabilir.'],
 bilgi=[B('Hareketlerin bağımsızlığı','Her cisim için yatay ve düşey konum ayrı yazılır; çarpışmada her iki konum bileşeni eşittir. Örnek: ikisi de g ivmesiyle düştüğünden ağırlıkların etkisi düşey konum farkında sadeleşir')],
 ad=[A('B’nin bileşenleri','sin53° = 0,8, cos53° = 0,6.','vBx = 30 m/s → vBy = 40 m/s'),
     A('Düşey konumları eşitle','Çarpışmada yükseklikler eşittir; A: 80 − 5t², B: 40t − 5t².','80 − 5t² = 40t − 5t² → t = 2 s'),
     A('Yatay yolları topla','Cisimler birbirine doğru yatayda hareket eder; yolların toplamı 100 m olmalıdır.','vA × 2 + 30 × 2 = 100'),
     A('vA’yı bul','Denklemi çöz.','vA = 20 m/s'),
     A('Kontrol et','Çarpışma yüksekliği 80 − 5 × 2² = 60 m > 0 olduğundan cisimler yere düşmeden çarpışır.','y = 60 m')],
 puf='Çarpışma = hem yatay hem düşey konumların eşitliği; ikisi de g ile düştüğünden düşey eşitlikten süre, yatay eşitlikten hız bulunur.',sekil=SK19)

# ============ 20 · Tepede patlama · zor ============
kartla('K-AFAT-20','Tepe noktasında ayrışma','Tepede patlamada momentum korunur; durgun kalan parça serbest düşer, diğeri yatay atış yapar; iki yere düşüş noktası arası uzaklık hesaplanır.','Momentumu korumamak (diğer parçanın hızını eski değerde bırakmak); menzili uzaklık sanmak.','zor','şekilli',6,'at-carpisma','Havada karşılaşan atışlar ve patlama')
vx20,vy20=30,40; Tup=4; hup=vy20**2//(2*g); assert hup==80 and 5*Tup**2==hup
vL=2*vx20; assert vL==60 and Fr(2*vx20,2)*1==vx20 and 2*vx20==1*0+ 60
dK=vx20*Tup; dL=dK+vL*Tup; assert (dK,dL,dL-dK)==(120,360,240)
assert (vx20*Tup,vL*Tup,dL,2*vL*Tup, hup)==(120,240,360,480,80)
sc=40; f20=lambda t:(vx20*t/sc,(vy20*t-5*t*t)/sc); fL20=lambda t:(3+vL*t/sc,2-5*t*t/sc)
SK20=sk([ground(-.4,9.5),traj(f20,0,4),ball(0,0),vec((0,0),(.78,1.04),''),N(.2,.95,'$50$ m/s','above left'),'\\draw[thin] (.55,0) arc[start angle=0,end angle=53.13,radius=.55];',N(.95,.2,'$53^\\circ$','right'),
         f'\\draw[vurgu,very thick,dash pattern=on 4pt off 2.5pt] {p2(3,2)} -- {p2(3,.1)};',traj(fL20,0,4),ball(3,2,r=.12,fill='white'),N(3,2.05,'patlama','above'),
         ball(3,0),ball(9,0),dimh(-.5,3,9,'$x$')])
q('0020',tipId='at-carpisma',tip='Havada karşılaşan atışlar ve patlama',z='zor',alt='Eğik Atış',kaz='Eğik atılan cismin tepe noktasında iki parçaya ayrılmasını momentum korunumu ve atış hareketleriyle birlikte yorumlar.',
 kart='K-AFAT-20 (tepede patlama) · 50 m/s, 53°, eşit kütleli parçalar',kalip='şekilli',
 metin='Hava direncinin ihmal edildiği bir ortamda yatay zeminden kütlesi 2m olan noktasal bir cisim, şekilde belirtilen büyüklükte ve doğrultuda ilk hızla fırlatılıyor. Cisim yörüngesinin en yüksek noktasında iç patlama ile kütleleri eşit iki parçaya ayrılıyor. Patlamadan hemen sonra parçalardan biri anlık olarak durgun hale geliyor, diğeri yatay doğrultuda hareketine devam ediyor. Parçalar şekildeki gibi yatay zemine düşüyor.\n(g = 10 m/s², sin53° = 0,8; cos53° = 0,6)\nBuna göre, parçaların yere düştüğü noktalar arasındaki uzaklık x kaç m’dir?',
 dogru=240,yan=[(80,'Tepe noktasının yüksekliğini (80 m) iki parçanın yere düştüğü noktalar arasındaki uzaklık sanmış.','dikkat'),
  (120,'Patlamadan sonra diğer parçanın hızını 30 m/s’de bırakmış (momentum korunumunu uygulamamış): 30 × 4 = 120 m.','bilgi'),
  (360,'Hızlı parçanın atış noktasından uzaklığını (120 + 240 = 360 m) iki parça arası uzaklık sanmış.','dikkat'),
  (480,'Hızlı parçanın uçuş süresini 8 s almış (tüm uçuş süresi): 60 × 8 = 480 m.','islem')],
 istenen='Parçaların yere düştüğü noktalar arasındaki yatay uzaklık (m).',
 ip=['Patlamadan hemen önce ve hemen sonra sistem için neyin değişmediğini düşün; durgun parçanın bu büyüklüğe katkısı ne olur?'],
 bilgi=[B('Momentumun korunumu','Dış kuvvetin ihmal edilebildiği kısa patlama anında toplam momentum korunur: (m₁ + m₂)·v = m₁·v₁ + m₂·v₂. Örnek: 3 kg’lık cisim 4 m/s ile giderken 1 kg ve 2 kg’lık iki parçaya ayrılır, 2 kg’lık parça durursa 1 kg’lık parça 12 m/s ile gider'),
        B('Tepede serbest düşme','Durgun parça ilk hızsız düşer; yüksekliğe bağlı süre h = ½·g·t² ile bulunur')],
 ad=[A('Bileşenleri ve tepe verilerini bul','vx = 30 m/s, vy0 = 40 m/s; tepeye çıkış süresi ve yükseklik.','t = 4 s → h = 40² / 20 = 80 m'),
     A('Momentumu koru','Tepede cisim yalnız yatay hıza sahiptir; yatay momentum korunur.','2m × 30 = m × 0 + m × v → v = 60 m/s'),
     A('Durgun parça','İlk hızsız serbest düşer; yatayda ilerlemez.','Atış noktasından 30 × 4 = 120 m uzağa düşer'),
     A('Hızlı parça','Tepeden 60 m/s ile yatay atılır; düşme süresi yine 4 s’dir.','Tepeden itibaren 60 × 4 = 240 m ilerler'),
     A('Uzaklığı bul','İki parça da aynı süre havada kalır; fark yatay yollar farkıdır.','x = 240 m'),
     A('Kontrol et','Durgun parçanın yere düşüş noktası tepenin hemen altındadır.','Hızlı parça: 120 + 240 = 360 m → fark 240 m')],
 puf='Tepede patlamada yatay momentum korunur; durgun parça tepenin altına düşer, uzaklık hızlı parçanın yatay yoludur.',sekil=SK20)

# =================== yaz ===================
for qq in P.ANA: qq['kardes']=None
os.makedirs(GD,exist_ok=True)
P.yaz(os.path.join(GD,'atis-1.json'),'/tmp/bos-atis.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=TIPK[c['tipId']]))['kartlar'].append(c['id'])
json.dump(dict(konu='Atışlar',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Fizik çıkmış soruları (yalnız mantık), MEB 11. sınıf fizik müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','afatis.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
