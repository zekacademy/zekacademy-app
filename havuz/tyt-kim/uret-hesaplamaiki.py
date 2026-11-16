"""TYT Kimya · Kimyasal Hesaplamalar · ek paket (hesaplamaiki): 22 soru, kardeş yok, ipucu 1.
Şekil verileri Python'da hesaplanır, TikZ bu değerlerden üretilir. Öncüllerin doğru/yanlış değeri tek yerde (d sözlüğü) tanımlanır;
anahtar, adımlar ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,random
GD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,GD)
import _hafif_kim2 as H
from _hafif_kim2 import *
H.KONU='Kimyasal Hesaplamalar'
UK='kim|Kimyasal Hesaplamalar'
P=Parti('hesaplamaiki','Kimyasal Hesaplamalar',UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 10. sınıf Kimyasal Hesaplamalar'
TIP={'mol':'Mol, tanecik ve mol kütlesi','yuzde':'Bileşikte kütlece yüzde','formul':'Basit formül ve molekül formülü','tepkime':'Tepkimede mol–kütle–hacim ilişkisi',
     'sinirlayici':'Sınırlayıcı bileşen ve artan madde','verim':'Tepkime verimi','karisim':'Karışımlarda tepkime'}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad):
    kart(f'K-KMHS2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-hs2-{tipad}',TIP[tipad],KY)
def q(no,ad,tipad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId='km-hs2-'+tipad,tip=TIP[tipad],**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def sc(x): return fm(x)
# ---------- öncüllü yardımcı: hedef harf konumuna göre şık kümeleri ----------
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(d,hedef,olumsuz=False):
    """d: {'I':(bool,açıklama)}; olumsuz=True: kök 'yanlıştır' → hedef küme yanlış öncüller. hedef: doğru şıkkın konumu 0..4."""
    T={k for k,(v,_) in d.items() if v!=olumsuz}
    tn=[n for n in ORD if SETS[n]==T]; assert len(tn)==1,T; tn=tn[0]; i=ORD.index(tn)
    bef=ORD[:i]; aft=ORD[i+1:]; assert hedef<=len(bef) and 4-hedef<=len(aft),(tn,hedef)
    ops=(bef[len(bef)-hedef:] if hedef else [])+[tn]+aft[:4-hedef]; assert len(ops)==5
    yan=[]
    for o in ops:
        if o==tn: continue
        W=SETS[o]; p=[]
        for x in sorted(W-T,key=['I','II','III'].index):
            p.append(f'{x} öncülünü '+('yanlış' if olumsuz else 'doğru')+f' sanmış; oysa {d[x][1]}')
        for x in sorted(T-W,key=['I','II','III'].index):
            p.append(f'{x} öncülünü '+('doğru' if olumsuz else 'yanlış')+f' sanmış; oysa {d[x][1]}')
        yan.append((o,'. '.join(p)+'.','bilgi'))
    return dict(dogru=tn,yan=yan,sira=ops)
def cap(s): return ('İ' if s[0]=='i' else s[0].upper())+s[1:]
def onc_adim(d,olumsuz=False,pre=()):
    ad=list(pre)
    for k,(v,a) in d.items(): ad.append(A(f'{k}. öncülü değerlendir',cap(a)+'.',f'{k}: '+('doğru' if v else 'yanlış')))
    T=[k for k,(v,_) in d.items() if v!=olumsuz]
    lst=T[0] if len(T)==1 else (' ve '.join(T) if len(T)==2 else ', '.join(T[:-1])+' ve '+T[-1])
    ad.append(A('Sonucu yaz','Sorulan türdeki öncüller belirlenir.',(('Yanlış' if olumsuz else 'Doğru')+' olanlar: '+lst)))
    return ad
# ---------- tanecik çizimi ----------
def uzak(p,L,m): return all((p[0]-a)**2+(p[1]-b)**2>=m*m for a,b in L)
def rastgele(n,x1,x2,y1,y2,m,seed):
    rng=random.Random(seed)
    for deneme in range(3000):
        L=[]
        for _ in range(4000):
            p=(rng.uniform(x1,x2),rng.uniform(y1,y2))
            if uzak(p,L,m): L.append(p)
            if len(L)==n: return L
    raise RuntimeError('yerlesmedi')
def molek(x,y,ang,tur):
    """tur 'k': küçük açık (H₂); 'b': büyük dolu (O₂ / N₂)."""
    r,f=(.12,'white') if tur=='k' else (.19,'vurgu!45')
    dx,dy=r*math.cos(ang),r*math.sin(ang)
    return (f'\\draw[thin,fill={f}] ({x-dx:.3f},{y-dy:.3f}) circle ({r});\\draw[thin,fill={f}] ({x+dx:.3f},{y+dy:.3f}) circle ({r});')
def kapdiz(W,Hh,nk,nb,seed,m=.85):
    pts=rastgele(nk+nb,.45,W-.45,.45,Hh-.45,m,seed); rng=random.Random(seed+1)
    s=f'\\draw[thick] (0,{Hh}) -- (0,0) -- ({W},0) -- ({W},{Hh});'
    for i,(x,y) in enumerate(pts): s+=molek(x,y,rng.uniform(0,math.pi),'k' if i<nk else 'b')
    return s
def lejant(x,y,ad_b):
    s=molek(x,y,0,'k')+f'\\node[right,font=\\small] at ({x+.35},{y}) {{{ad_b[0]}}};'
    s+=molek(x,y-.6,0,'b')+f'\\node[right,font=\\small] at ({x+.35},{y-.6}) {{{ad_b[1]}}};'
    return s
HS="H=1, C=12, N=14, O=16, S=32 g/mol"

# ============================================================ KARTLAR (8)
kartla('01','Mol, kütle ve tanecik dönüşümleri','n = m ÷ MA; tanecik sayısı = n × N_A; atom kütlesi mol kütlesinden, mol kütlesi atom sayısına bölünerek bulunur.','Molekül kütlesini atom kütlesi sanmak; n = m × M ya da n = M ÷ m yazmak.','kolay','tablo',3,'mol')
kartla('02','Gaz hacmi, mol ve atom sayısı','NK’da n = V ÷ 22,4; toplam atom sayısı = n × molekül başına atom × N_A.','Molekül ve atom sayısını karıştırmak; 22,4 yerine 11,2 almak.','orta','düz',3,'mol')
kartla('03','Bileşik formülünden kütlece yüzde','Yüzde = (elementin toplam kütlesi ÷ mol kütlesi) × 100; indis atom sayısını verir.','İndisi unutmak; atom sayısıyla kütleyi karıştırmak; O için 32 almak.','kolay','düz',2,'yuzde')
kartla('04','Basit formül ve molekül formülü','Kütleleri mol sayısına çevir, en küçük tam sayı oranına getir; molekül formülü = basit formül × (mol kütlesi ÷ basit formül kütlesi).','Kütle oranını atom oranı sanmak; sadeleştirmemek; basit ile molekül formülünü karıştırmak.','orta','tablo',4,'formul')
kartla('05','Denklemden mol–kütle–hacim','Katsayı oranı mol oranıdır; önce mol, sonra istenen büyüklük hesaplanır.','Katsayıyı kullanmamak; oranı ters kurmak; yanlış maddenin katsayısını almak.','orta','grafik',3,'tepkime')
kartla('06','Sınırlayıcı bileşen ve artan madde','Her maddenin mol sayısı katsayısına bölünür; en küçük olan sınırlayıcıdır, ürünü o belirler.','1 : 1 oranı varsaymak; artanı tepkimeye girenle karıştırmak.','zor','şekilli',4,'sinirlayici')
kartla('07','Yüzde verim','Verim = (gerçek ürün ÷ teorik ürün) × 100; teorik ürün sınırlayıcıdan hesaplanır.','Verimi kayıp sanmak; teorik ürünü katsayısız hesaplamak.','orta','hikâyeli',4,'verim')
kartla('08','Karışımlarda tepkime','Tepkime vermeyen bileşen hesaba girmez; ürün miktarından tepkimeye giren bileşenin kütlesi bulunup karışıma oranlanır.','Karışımın tamamını tepkimeye sokmak; katsayıyı kullanmamak.','orta','hikâyeli',3,'karisim')

# ================= 01 · tablo · mol max · kolay =================
rows=[('N₂',56),('CH₄',24),('CO₂',44),('NH₃',Fr(17,2)),('SO₂',96)]
Mm={'N₂':28,'CH₄':16,'CO₂':44,'NH₃':17,'SO₂':64}
nn={a:Fr(b)/Mm[a] for a,b in rows}; assert nn=={'N₂':2,'CH₄':Fr(3,2),'CO₂':1,'NH₃':Fr(1,2),'SO₂':Fr(3,2)} and max(nn,key=nn.get)=='N₂' and sorted(nn.values())[-2]<2
inv={a:Fr(Mm[a])/Fr(b) for a,b in rows}; assert max(inv,key=inv.get)=='NH₃'
assert max(rows,key=lambda r:r[1])[0]=='SO₂' and min(Mm,key=Mm.get)=='CH₄'
SK=tablo_svg(['Gaz','Kütle (g)'],[[a,sc(b)] for a,b in rows])
S=[a for a,_ in rows]
q('0001',[A('Mol kütlelerini bul','Atom kütlelerinden her gazın mol kütlesi hesaplanır.','N₂: 28 · CH₄: 16 · CO₂: 44 · NH₃: 17 · SO₂: 64'),A('Mol sayılarını hesapla','Mol sayısı, kütlenin mol kütlesine bölünmesiyle bulunur.','n = m ÷ M: N₂ 2 · CH₄ 1,5 · CO₂ 1 · NH₃ 0,5 · SO₂ 1,5'),A('Karşılaştır','Kütlesi en büyük olan örnek mol sayısı en büyük olan değildir.','En büyük mol sayısı: N₂ (2 mol)')],'mol',
 z='kolay',alt='Mol Kavramı',kaz='Kütle ve mol kütlesi verilen maddelerin mol sayılarını karşılaştırır.',kalip='tablo',
 kart='K-KMHS2-01 (mol–kütle dönüşümü) · beş gaz örneği tablosu',sekil=SK,
 metin='Bir öğrenci, laboratuvarda hazırladığı beş ayrı gaz örneğinin kütlelerini hassas terazide tartmış ve sonuçları şekildeki tabloda toplamıştır. Her örnek tek bir saf gazdan oluşmaktadır.\n'+HS+' olduğuna göre bu örneklerden hangisinin mol sayısı en fazladır?',
 dogru='N₂',sira=S,
 yan=[('CH₄','Mol kütlesi en küçük gazın mol sayısının en büyük olacağını sanmış; kütleyi hesaba katmamış.','bilgi'),('CO₂','Mol sayısını 1 bulup diğer örnekleri karşılaştırmadan bırakmış.','dikkat'),('NH₃','Mol sayısını M ÷ m diye ters oranlamış; en büyük değeri NH₃’te (2) bulmuş.','islem'),('SO₂','Kütlesi en büyük örneği mol sayısı en büyük örnek sanmış.','dikkat')],
 istenen='Mol sayısı en fazla olan gaz örneği.',ip=['Kütleler farklı gazlara ait; kütleleri doğrudan karşılaştırmadan önce ortak bir büyüklüğe çevir.'],
 bilgi=[B('Mol sayısı','n = kütle ÷ mol kütlesi. Aynı kütledeki maddelerden mol kütlesi küçük olanın mol sayısı büyüktür. Örnek: 10 g He (4 g/mol) 2,5 mol, 10 g Ne (20 g/mol) 0,5 mol eder')],
 puf='Kütleleri değil mol sayılarını karşılaştır: n = m ÷ M.')

# ================= 02 · akış şeması · atom kütlesi · kolay =================
V2,m2=Fr(56,10),Fr(95,10); n2=V2/Fr(224,10); M2=m2/n2; A2=M2/2
assert n2==Fr(1,4) and M2==38 and A2==19
assert m2/2==Fr(475,100) and m2/Fr(5,10)/2==Fr(95,10) and m2/(V2/Fr(448,10))/2==38 and m2/(V2/Fr(448,10))==76
g='\\foreach \\x/\\t in {0/{5,6 L X$_2$\\\\(NK)},3.7/{$n$ = ? mol\\\\X$_2$},7.4/{9,5 g\\\\X$_2$}}{\\node[draw,rounded corners=3pt,thick,minimum width=2.4cm,minimum height=1.2cm,align=center,font=\\normalsize] at (\\x,0) {\\t};}'
g+=f'\\draw[{ARR},thick] (1.25,0) -- (2.45,0); \\draw[{ARR},thick] (4.95,0) -- (6.15,0);'
g+='\\node[above,font=\\small,align=center] at (1.85,.1) {÷ 22,4\\\\L/mol}; \\node[above,font=\\small,align=center] at (5.55,.1) {× $M$\\\\g/mol};'
SK=tk(g)
q('0002',[A('Mol sayısını bul','NK’da 1 mol gaz 22,4 L hacim kaplar.','n = 5,6 ÷ 22,4 = 0,25 mol'),A('Mol kütlesini bul','Kütle, mol sayısıyla mol kütlesinin çarpımıdır.','M = 9,5 ÷ 0,25 = 38 g/mol'),A('Atom kütlesine geç','X₂ molekülünde iki X atomu vardır.','MA(X) = 38 ÷ 2 = 19 g/mol')],'mol',
 z='kolay',alt='Mol Kavramı',kaz='Gazın hacmi ve kütlesinden mol kütlesini, oradan atom kütlesini hesaplar.',kalip='şekilli',
 kart='K-KMHS2-01 (mol köprüsü) · iki atomlu X₂ gazından atom kütlesi',sekil=SK,
 metin='Bir öğrenci, iki atomlu X₂ gazının normal koşullardaki (NK) hacmini ve kütlesini ölçüp sonuçları şekildeki mol köprüsünün uç kutularına yazmıştır. Orta kutuya ise gazın mol sayısı yazılacaktır.\nNK’da 1 mol gaz 22,4 L hacim kapladığına göre X elementinin mol atom kütlesi kaç g/mol’dür?',
 dogru=19,yan=[(Fr(475,100),'Mol sayısına bölmeden kütleyi yalnızca 2’ye bölmüş (9,5 ÷ 2).','islem'),(Fr(95,10),'1 mol gazı 11,2 L sanıp mol sayısını 0,5 bulmuş; X₂ için 19 g/mol bulup yine 2’ye bölmüş.','bilgi'),(38,'X₂’nin mol kütlesini (38 g/mol) bulmuş; atom kütlesine geçmek için 2’ye bölmemiş.','dikkat'),(76,'1 mol gazı 44,8 L alıp mol sayısını 0,125 bulmuş ve 2’ye bölmemiş.','bilgi')],
 istenen='X elementinin mol atom kütlesi (g/mol).',ip=['Önce mol sayısını, sonra mol kütlesini bul.'],
 bilgi=[B('Atom kütlesi ve mol kütlesi','mol kütlesi, 1 mol maddenin gram cinsinden kütlesidir. İki atomlu bir molekülün mol kütlesi atom kütlesinin 2 katıdır. Örnek: O₂ için 32 g/mol, O atomu için 16 g/mol')],
 puf='Önce gazın mol kütlesini bul, sonra molekül başına atom sayısına böl.')

# ================= 03 · öncüllü mol kavramı · kolay =================
d3={'I':(False,'18 g H₂O 1 mol sudur; her molekülde 3 atom bulunduğundan toplam atom sayısı 3 × 6 × 10²³ = 1,8 × 10²⁴’tür'),
    'II':(True,'atom kütlesi g/mol cinsinden 1 mol atomun kütlesidir; 1 mol Na atomu 23 g gelir'),
    'III':(True,'NK’da 22,4 L CO₂ 1 moldür ve her molekülde 2 O atomu vardır; 2 × 6 × 10²³ = 1,2 × 10²⁴ O atomu bulunur')}
assert Fr(18,18)*3*6==18 and 18!=6 and Fr(224,10)/Fr(224,10)*2*6==12
r=onc(d3,4)
q('0003',onc_adim(d3,pre=[A('Mol bağıntıları','Kütle, hacim ve tanecik sayısı mol üzerinden birbirine bağlanır.','n = m ÷ M = V ÷ 22,4 = tanecik ÷ N_A')]),'mol',
 z='kolay',alt='Mol Kavramı',kaz='Mol, atom sayısı ve gaz hacmi arasındaki dönüşümlere ilişkin yargıları değerlendirir.',kalip='öncüllü',
 kart='K-KMHS2-01 (mol–tanecik–hacim dönüşümleri) · üç yargı',
 metin='Kimya dersinde mol kavramını işleyen öğrenciler, aşağıdaki yargıları tartışıyor.\nI. 18 g H₂O sıvısındaki toplam atom sayısı 6 × 10²³’tür.\nII. 1 mol Na atomunun kütlesi 23 g’dır.\nIII. Normal koşullarda (NK) 22,4 L CO₂ gazında 1,2 × 10²⁴ oksijen atomu bulunur.\nH: 1, C: 12, O: 16, Na: 23 g/mol, N_A = 6 × 10²³ ve NK’da 1 mol gaz 22,4 L olduğuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her yargıda önce maddenin mol sayısını bul; sonra tanecik türüne ve molekül başına atom sayısına bak.'],
 bilgi=[B('Mol ve tanecik sayısı','1 mol = N_A tanecik. Molekül sayısı mol × N_A, atom sayısı ise bunun molekül başına atom sayısıyla çarpımıdır. Örnek: 1 mol NH₃ molekülünde 4 N_A atom bulunur')],
 puf='Atom sayısı = mol × molekül başına atom × N_A.')

# ================= 04 · kütlece yüzde · kolay =================
assert 32+3*16==80 and Fr(32*100,80)==40 and Fr(100,4)==25 and Fr(32*100,64)==50 and Fr(48*100,80)==60
q('0004',[A('Mol kütlesini hesapla','SO₃ molekülünde 1 S ve 3 O atomu vardır.','M = 32 + 3 × 16 = 80 g/mol'),A('S’nin kütlesini yaz','Yüzdeyi hesaplamak için 1 mol bileşikteki kükürt kütlesi alınır.','1 mol SO₃’te 32 g S'),A('Yüzdeyi bul','Elementin kütlesi mol kütlesine bölünüp 100 ile çarpılır.','32 ÷ 80 × 100 = %40')],'yuzde',
 z='kolay',alt='Bileşiklerde Kütlece Yüzde',kaz='Bileşik formülünden bir elementin kütlece yüzdesini hesaplar.',kalip='düz',
 kart='K-KMHS2-03 (kütlece yüzde) · SO₃ içinde kükürt',
 metin='Fosil yakıtların yanması sonucu atmosfere karışan kükürt dioksit gazının bir bölümü ileri aşamada SO₃ bileşiğine yükseltgenir; bu bileşik yağmur suyunda çözünüp asit yağmurlarına neden olur.\nO: 16 g/mol, S: 32 g/mol olduğuna göre saf SO₃ bileşiğinin kütlece yüzde kaçı kükürttür?',
 dogru=40,yan=[(25,'Atom sayısına bakıp 4 atomdan 1’inin S olduğunu düşünerek %25 bulmuş.','bilgi'),(50,'O atom kütlesi yerine O₂’nin mol kütlesini (32) kullanmış: 32 ÷ (32 + 32).','bilgi'),(60,'Oksijenin kütlece yüzdesini (48 ÷ 80) bulmuş.','dikkat'),(80,'Bileşiğin mol kütlesini yüzde olarak yazmış.','dikkat')],
 istenen='SO₃’te kükürdün kütlece yüzdesi.',ip=['Bileşiğin mol kütlesini bul; kükürdün bu kütlenin ne kadarını oluşturduğuna bak.'],
 bilgi=[B('Kütlece yüzde','Elementin yüzdesi = (formüldeki elementin toplam kütlesi ÷ bileşiğin mol kütlesi) × 100. Örnek: CH₄’te C kütlece 12 ÷ 16 × 100 = %75’tir')],
 puf='Yüzde = element kütlesi ÷ bileşik kütlesi × 100; indis, kütleyi o sayıda artırır.')

# ================= 05 · NH₃ gaz hacmi → atom · kolay =================
n5=Fr(672,100)/Fr(224,10); at5=n5*4*6
assert n5==Fr(3,10) and at5==Fr(72,10) and n5*6==Fr(18,10) and n5*3*6==Fr(54,10) and Fr(672,100)/Fr(112,10)*4*6==Fr(144,10) and n5*2*6==Fr(36,10)
s5=['1,8 × 10²³','3,6 × 10²³','5,4 × 10²³','7,2 × 10²³','1,44 × 10²⁴']
q('0005',[A('Mol sayısı','NK’da gazın mol sayısı hacmin 22,4’e bölünmesiyle bulunur.','n = 6,72 ÷ 22,4 = 0,3 mol'),A('Molekül başına atom','Bir NH₃ molekülünde 1 N ve 3 H, toplam 4 atom vardır.','0,3 × 4 = 1,2 mol atom'),A('Atom sayısı','Mol sayısı N_A ile çarpılır.','1,2 × 6 × 10²³ = 7,2 × 10²³')],'mol',
 z='kolay',alt='Gazlarda Mol ve Hacim',kaz='NK’daki gaz hacminden toplam atom sayısını hesaplar.',kalip='düz',
 kart='K-KMHS2-02 (gaz hacmi–mol–atom sayısı) · NH₃ tüpü',
 metin='Bir soğutma sisteminin tüpünde bulunan amonyak (NH₃) gazının hacmi, normal koşullarda (NK) 6,72 L olarak ölçülmüştür.\nN_A = 6 × 10²³ ve NK’da 1 mol gaz 22,4 L olduğuna göre bu gazdaki toplam atom sayısı kaçtır?',
 dogru=s5[3],sira=s5,yan=[(s5[0],'Yalnız molekül sayısını (0,3 mol) bulmuş; atom sayısına geçmemiş.','dikkat'),(s5[1],'Molekül başına atom sayısını 2 almış (0,3 × 2 × 6 × 10²³).','bilgi'),(s5[2],'Yalnız H atomlarının sayısını (0,9 mol) bulmuş.','dikkat'),(s5[4],'1 mol gazı 11,2 L sanıp mol sayısını 0,6 bulmuş.','bilgi')],
 istenen='Gazdaki toplam atom sayısı.',ip=['Önce gazın mol sayısını bul; sonra bir molekülde kaç atom olduğuna bak.'],
 bilgi=[B('Normal koşullarda gaz hacmi','NK’da 1 mol gaz 22,4 L hacim kaplar; mol sayısı n = V ÷ 22,4’tür. Örnek: 44,8 L gaz 2 moldür')],
 puf='Önce hacimden mol, sonra molekül başına atom sayısıyla toplam atom.')

# ================= 06 · tanecik modeli · sınırlayıcı · orta · öncüllü =================
nH,nO=4,3; use=min(nH//2,nO); assert use==2 and nO-use==1 and 2*use==4 and nH+nO==7 and 2*use+(nO-use)==5
g=kapdiz(4.6,3.2,nH,nO,seed=11,m=.9)+'\\node[above] at (2.3,3.25) {Tepkimeden önce};'+lejant(5.3,2.3,['H$_2$','O$_2$'])
SK=tk(g)
d6={'I':(True,'4 H₂ molekülü için 2 O₂ gerekir ve 3 O₂ bulunduğundan 1 O₂ molekülü artar'),
    'II':(False,'2 : 2 oranına göre 4 H₂ molekülünden 4 H₂O molekülü oluşur'),
    'III':(True,'harcanan 2 O₂ molekülü, artan 1 O₂ molekülünün 2 katıdır')}
r=onc(d6,2)
q('0006',onc_adim(d6,pre=[A('Sınırlayıcıyı bul','Tepkime 2 H₂ : 1 O₂ oranında gerçekleşir; 4 H₂ için 2 O₂ yeterlidir.','Şekildeki sayım: 4 H₂ ve 3 O₂ → H₂ sınırlayıcı')]),'sinirlayici',
 z='orta',alt='Sınırlayıcı Bileşen',kaz='Kaptaki tanecik modelinden sınırlayıcı bileşeni belirleyip tepkime sonunu yorumlar.',kalip='şekilli',
 kart='K-KMHS2-06 (sınırlayıcı bileşen) · kapta H₂ ve O₂ molekül modeli',sekil=SK,
 metin='Sert ve kapalı bir kapta bulunan H₂ ve O₂ gazlarının tepkimeden önceki hâli şekildeki gibi modellenmiştir; her çizim bir molekülü göstermektedir. Gazlar, 2H₂ + O₂ → 2H₂O tepkimesine göre sınırlayıcı bileşen tamamen harcanıncaya kadar tepkimeye giriyor ve oluşan H₂O gaz hâlinde kalıyor.\nI. Kapta O₂ molekülü artar.\nII. Tepkimede 3 H₂O molekülü oluşur.\nIII. Harcanan O₂ molekülü sayısı, artan O₂ molekülü sayısının 2 katıdır.\nBuna göre tepkime sona erdiğinde yukarıdaki yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Tepkime sonrası doğru olan yargılar.',ip=['Şekildeki her türden kaç molekül olduğunu say; denklemdeki katsayılara göre hangisinin önce biteceğine bak.'],
 bilgi=[B('Sınırlayıcı bileşen','tepkimede önce tükenen maddedir; ürün miktarını o belirler, diğer reaktiften bir miktar artar. Örnek: 2A + B → ürün tepkimesinde 6 A ve 2 B varsa B tükenir, 2 A artar')],
 puf='Sayım yap, katsayı oranına böl; önce biten madde sınırlayıcıdır.')

# ================= 07 · tablo · N₂+H₂ · orta =================
assert 5-2==3 and (12-3)==3*3 and 2*3==6 and 6*17==102 and 3*17==51 and 9*17==153 and 10*17==170 and 12*17==204 and Fr(12,3)*17==68 and 5*17==85 and 2*17==34
SK=tablo_svg(['Madde','Başlangıç (mol)','Tepkime sonu (mol)'],[['N₂','5','2'],['H₂','12','3'],['NH₃','0','?']])
q('0007',[A('Harcanan N₂','Tepkime sonunda azalan mol sayısı harcananı verir.','5 − 2 = 3 mol N₂'),A('Oluşan NH₃','Katsayılar mol oranıdır: 1 mol N₂’den 2 mol NH₃ oluşur.','3 × 2 = 6 mol NH₃'),A('Kütleye çevir','NH₃’ün mol kütlesi 14 + 3 × 1 = 17 g/mol’dür.','6 × 17 = 102 g')],'tepkime',
 z='orta',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Tablodaki mol değişiminden ürünün kütlesini hesaplar.',kalip='tablo',
 kart='K-KMHS2-05 (denklemden mol–kütle) · N₂ ve H₂ mol tablosu',sekil=SK,
 metin='Amonyak üretiminin laboratuvar modelinde N₂ + 3H₂ → 2NH₃ tepkimesi kapalı bir kapta gerçekleştirilmiş ve kaptaki maddelerin mol sayıları tepkimeden önce ve tepkime tamamlandıktan sonra şekildeki tabloya kaydedilmiştir. Kapta başka madde yoktur.\nH: 1 g/mol, N: 14 g/mol olduğuna göre tepkime sonunda kaptaki NH₃ kaç gram olur?',
 dogru=102,yan=[(34,'Tepkime sonunda kalan N₂ mol sayısını (2) NH₃ mol sayısı almış.','dikkat'),(51,'N₂ ile NH₃’ü 1 : 1 oranında alıp 3 mol NH₃ bulmuş.','bilgi'),(68,'H₂’nin başlangıç mol sayısını (12) 3’e bölüp bunu NH₃ mol sayısı almış; NH₃ katsayısını (2) kullanmamış.','islem'),(85,'Başlangıçtaki N₂ mol sayısını (5) NH₃ mol sayısı almış.','dikkat')],
 istenen='Tepkime sonunda oluşan NH₃’ün kütlesi (g).',ip=['Tabloda mol sayısı değişen maddeyi bul; değişim miktarını denklemdeki katsayı oranıyla NH₃’e bağla.'],
 bilgi=[B('Katsayı ve mol oranı','Denklemdeki katsayılar mol oranını verir. Örnek: 2H₂ + O₂ → 2H₂O tepkimesinde 4 mol H₂ harcanınca 2 mol O₂ harcanır ve 4 mol H₂O oluşur')],
 puf='Tablodaki değişim = harcanan ya da oluşan mol; denklem oranıyla istenen maddeye geç.')

# ================= 08 · öncüllü olumsuz · basit formül · orta =================
nC,nHh=Fr(80,12),Fr(20,1); assert nC/nC==1 and nHh/nC==3
Mb=30; kat=12+3; assert Mb//kat==2 and Mb%kat==0
n6=Fr(6,30); assert n6==Fr(1,5) and n6*8*6==Fr(96,10)
d8={'I':(False,'C : H mol oranı (80 ÷ 12) : (20 ÷ 1) = 1 : 3 olduğundan basit formül CH₃’tür'),
    'II':(True,'basit formül kütlesi 15, mol kütlesi 30 olduğundan molekül formülü (CH₃)₂ yani C₂H₆’dır'),
    'III':(False,'6 g bileşik 0,2 moldür ve C₂H₆ molekülünde 8 atom vardır; 0,2 × 8 × 6 × 10²³ = 9,6 × 10²³ atom bulunur')}
r=onc(d8,3,olumsuz=True)
q('0008',onc_adim(d8,olumsuz=True,pre=[A('Bileşimi mol oranına çevir','100 g bileşikte 80 g C ve 20 g H vardır.','C: 80 ÷ 12 = 20/3 mol · H: 20 ÷ 1 = 20 mol')]),'formul',
 z='orta',alt='Basit Formül ve Molekül Formülü',kaz='Kütlece bileşimden basit ve molekül formülünü bulup çıkarımları değerlendirir.',kalip='öncüllü',
 kart='K-KMHS2-04 (basit–molekül formülü) · kütlece %80 C ve %20 H içeren hidrokarbon',
 metin='Doğal gazın içinde de bulunan, yalnız karbon ve hidrojenden oluşan bir hidrokarbonun analizinde bileşiğin kütlece %80’inin karbon, %20’sinin hidrojen olduğu ve mol kütlesinin 30 g/mol olduğu bulunmuştur. Bileşikle ilgili üç ifade şöyledir:\nI. Basit formülü CH₂’dir.\nII. Molekül formülü C₂H₆’dır.\nIII. 6 g bileşikteki toplam atom sayısı 1,6 × 10²³’tür.\nH: 1 g/mol, C: 12 g/mol ve N_A = 6 × 10²³ olduğuna göre bu ifadelerden hangileri yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifadeler.',ip=['Kütlece yüzdeleri 100 g örnek için mol sayısına çevir; en küçük tam sayı oranını bul.'],
 bilgi=[B('Basit formül ve molekül formülü','basit formül atomların en küçük tam sayı oranını verir; molekül formülü, basit formülün mol kütlesi oranında katıdır. Örnek: basit formülü CH₂O olan ve mol kütlesi 60 g/mol olan bileşik C₂H₄O₂’dir')],
 puf='Kütle → mol → en küçük oran → basit formül; molekül formülü için mol kütlesine oranla.')

# ================= 09 · tablo · iki azot oksit · orta =================
assert Fr(14,14)==1 and Fr(8,16)==Fr(1,2) and Fr(7,14)==Fr(1,2) and Fr(16,16)==1
SK=tablo_svg(['Bileşik','Azot kütlesi (g)','Oksijen kütlesi (g)'],[['I','14','8'],['II','7','16']])
s9=['NO ve NO','NO ve NO₂','NO₂ ve N₂O','NO₂ ve NO₂','N₂O ve NO₂']
q('0009',[A('I. bileşiği mole çevir','Kütleler atom kütlesine bölünür.','N: 14 ÷ 14 = 1 mol · O: 8 ÷ 16 = 0,5 mol'),A('I. bileşiğin formülü','1 : 0,5 oranı 2 : 1 olur.','N : O = 2 : 1 → N₂O'),A('II. bileşiği mole çevir','Aynı işlem II için yapılır.','N: 7 ÷ 14 = 0,5 mol · O: 16 ÷ 16 = 1 mol'),A('II. bileşiğin formülü','0,5 : 1 oranı 1 : 2 olur.','N : O = 1 : 2 → NO₂')],'formul',
 z='orta',alt='Basit Formül ve Molekül Formülü',kaz='Elementlerin kütlelerinden bileşiklerin basit formüllerini bulur.',kalip='tablo',
 kart='K-KMHS2-04 (basit formül) · iki azot oksit örneği',sekil=SK,
 metin='Bir araştırma ekibi, motor egzozundaki iki farklı azot oksit bileşiğinden saf örnekler alıp her birinin bileşimini analiz etmiş ve sonuçları şekildeki tabloya yazmıştır. Her bileşik saftır.\nN: 14 g/mol ve O: 16 g/mol olduğuna göre I. ve II. bileşiklerin basit formülleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru='N₂O ve NO₂',sira=s9,
 yan=[('NO ve NO₂','I. bileşikte oksijen kütlesini 16’ya değil 8’e bölüp N : O = 1 : 1 bulmuş.','islem'),('NO ve NO','Kütleleri mol kütlesine değil kendilerine bölüp her elementi 1 mol bulmuş; iki bileşikte de N : O = 1 : 1 yazmış.','islem'),('NO₂ ve NO₂','I. bileşikte oranı ters kurmuş: 1 mol N ile 0,5 mol O’yu N : O = 1 : 2 yazmış.','islem'),('NO₂ ve N₂O','Mol oranlarını ters yazmış; I için O : N = 2 : 1, II için N : O = 2 : 1 almış.','islem')],
 istenen='I. ve II. bileşiklerin basit formülleri.',ip=['Her elementin kütlesini mol sayısına çevir; sonra oranı en küçük tam sayılara getir.'],
 bilgi=[B('Basit formül','bileşikteki atomların en küçük tam sayı oranıdır. Kütleler atom kütlelerine bölünerek mol oranı bulunur. Örnek: 12 g C ile 32 g O içeren bileşikte C : O = 1 : 2’dir, formül CO₂’dir')],
 puf='Kütleyi atom kütlesine böl, oranı sadeleştir: sayılar indis olur.')

# ================= 10 · grafik · CaCO₃ ısıtma · orta · öncüllü =================
nCa=Fr(25,100); loss=25-14; assert 25==100*nCa and 14==56*nCa and loss==44*nCa and nCa*Fr(224,10)==Fr(56,10) and nCa*2==Fr(1,2)
d10={'I':(True,'0,25 mol CaCO₃ ayrışınca 0,25 mol CO₂ çıkar; bu gaz NK’da 0,25 × 22,4 = 5,6 L hacim kaplar'),
     'II':(True,'kalan katı CaO’dur; 14 g ÷ 56 g/mol = 0,25 mol'),
     'III':(False,'başlangıçtaki 25 g CaCO₃ 25 ÷ 100 = 0,25 moldür')}
r=onc(d10,2)
g='\\begin{axis}[width=7.4cm,height=5.6cm,xmin=0,xmax=9,ymin=0,ymax=30,xtick={0,2,6,9},xticklabels={0,2,6,9},ytick={0,14,25},tick label style={font=\\small},axis lines=left,xlabel={Isıtma süresi (dk)},ylabel={Kaptaki katının kütlesi (g)},xlabel style={font=\\small},ylabel style={font=\\small}]'
g+='\\addplot[thick,vurgu] coordinates {(0,25) (2,25) (6,14) (9,14)};\\draw[dashed,thin] (axis cs:0,14) -- (axis cs:6,14) -- (axis cs:6,0);\\draw[dashed,thin] (axis cs:0,25) -- (axis cs:2,25) -- (axis cs:2,0);\\end{axis}'
SK=tk(g)
q('0010',onc_adim(d10,pre=[A('Grafiği oku','Başlangıç kütlesi 25 g, ayrışma bitince 14 g kalır.','Ayrışan CaCO₃: 25 g · kalan CaO: 14 g')]),'tepkime',
 z='orta',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Kütle–zaman grafiğinden başlangıç ve ürün mol sayılarını ve gaz hacmini hesaplar.',kalip='grafik',
 kart='K-KMHS2-05 (kütle–zaman grafiği) · saf CaCO₃’ın ısıtılarak ayrışması',sekil=SK,
 metin='Saf CaCO₃ katısı, ağzı açık bir kapta ısıtılarak CaCO₃ → CaO + CO₂ tepkimesine göre tamamen ayrıştırılıyor. Çıkan CO₂ gazı kaptan uzaklaşıyor; kapta yalnız CaO katısı kalıyor. Kaptaki katının kütlesinin ısıtma süresiyle değişimi şekildeki grafikte verilmiştir.\nI. Açığa çıkan CO₂ gazı NK’da 5,6 L hacim kaplar.\nII. 6. dakikadan sonra kapta 0,25 mol CaO vardır.\nIII. Isıtmaya başlamadan önce kapta 0,5 mol CaCO₃ bulunur.\nCa: 40, C: 12, O: 16 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Grafikten başlangıç ve son kütleyi oku; her kütleyi uygun mol kütlesiyle mole çevir.'],
 bilgi=[B('Kütle–zaman grafiği','Kaptan gaz çıkan tepkimede katının kütlesi azalır; kütle sabitlendiğinde tepkime bitmiştir. Örnek: ısıtılan bir katının kütlesi azalıp sabitleniyorsa katı tamamen ayrışmış, tepkime tamamlanmıştır')],
 puf='Kütle sabitlenince tepkime biter; kütle farkı çıkan gazın kütlesidir.')

# ================= 11 · akış şeması · KClO₃ ayrışması · orta =================
nO2k=Fr(672,100)/Fr(224,10); nK=nO2k*2/3; mK=nK*Fr(245,2)
assert nO2k==Fr(3,10) and nK==Fr(1,5) and mK==Fr(245,10)
assert nO2k*Fr(245,2)==Fr(3675,100) and Fr(672,100)/Fr(112,10)*Fr(2,3)*Fr(245,2)==49 and nO2k*Fr(3,2)*Fr(245,2)==Fr(55125,1000) and nO2k*2*Fr(245,2)==Fr(735,10)
g='\\foreach \\x/\\t in {0/{6,72 L O$_2$\\\\(NK)},3.1/{$n$(O$_2$)},6.2/{$n$(KClO$_3$)},9.3/{$m$(KClO$_3$)\\\\= ? g}}{\\node[draw,rounded corners=3pt,thick,minimum width=1.9cm,minimum height=1.2cm,align=center,font=\\normalsize] at (\\x,0) {\\t};}'
g+=''.join(f'\\draw[{ARR},thick] ({a},0) -- ({b},0);' for a,b in [(1.0,2.1),(4.1,5.2),(7.2,8.3)])
g+='\\node[above,font=\\small,align=center] at (1.55,.1) {22,4\\\\L/mol}; \\node[above,font=\\small,align=center] at (7.75,.1) {122,5\\\\g/mol};'
SK=tk(g)
s11=[Fr(245,10),Fr(3675,100),Fr(49),Fr(55125,1000),Fr(735,10)]
q('0011',[A('O₂ mol sayısı','NK’da hacim 22,4’e bölünür.','n(O₂) = 6,72 ÷ 22,4 = 0,3 mol'),A('KClO₃ mol sayısı','Denklemden 2 mol KClO₃ için 3 mol O₂ oluşur.','n(KClO₃) = 0,3 × 2 ÷ 3 = 0,2 mol'),A('KClO₃ kütlesi','Mol sayısı mol kütlesiyle çarpılır.','m = 0,2 × 122,5 = 24,5 g')],'tepkime',
 z='orta',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Gaz hacminden denklem oranıyla harcanan katının kütlesini bulur.',kalip='şekilli',
 kart='K-KMHS2-05 (denklemden mol–kütle–hacim) · KClO₃ ayrışması, harcanan katı kütlesi',sekil=SK,
 metin='Bir öğrenci, katalizör varlığında KClO₃ katısını ısıtarak 2KClO₃ → 2KCl + 3O₂ tepkimesini tamamlıyor ve açığa çıkan O₂ gazının hacmini ölçüyor. Hesabını şekildeki akış şemasıyla planlıyor: şemada ölçülen hacim ve işlem basamaklarındaki dönüşüm değerleri verilmiş, ayrışan KClO₃’ün kütlesi ise sorulmuştur.\nBuna göre tepkimede ayrışan KClO₃ kaç gramdır?',
 dogru=s11[0],yan=[(s11[1],'O₂ ile KClO₃ arasında 1 : 1 mol oranı kurmuş; 0,3 mol KClO₃ bulmuş.','bilgi'),(s11[2],'1 mol gazı 11,2 L sanıp O₂’yi 0,6 mol almış.','bilgi'),(s11[3],'Mol oranını ters kurmuş: 0,3 × 3 ÷ 2 = 0,45 mol KClO₃.','islem'),(s11[4],'O₂’nin mol sayısını KClO₃’ün katsayısı olan 2 ile çarpıp 0,6 mol KClO₃ bulmuş.','islem')],
 istenen='Tepkimede ayrışan KClO₃’ün kütlesi (g).',ip=['Şemadaki kutuları hacimden başlayarak sırayla doldur; dönüşümlerden hangisinde çarpma, hangisinde bölme gerektiğine dikkat et.'],
 bilgi=[B('Denklemden oran','Katsayılar mol oranını verir; iki madde arasındaki geçiş mol üzerinden yapılır. Örnek: N₂ + 3H₂ → 2NH₃ tepkimesinde 0,6 mol H₂ için 0,4 mol NH₃ oluşur')],
 puf='Hacim → mol → denklem oranı → mol → kütle: dört kutu, üç dönüşüm.')

# ================= 12 · verim · SO₂ → SO₃ · orta =================
nS=Fr(128,10)/64; th=nS*80; vr=Fr(12)/th*100
assert nS==Fr(1,5) and th==16 and vr==75
assert Fr(16-12,16)*100==25 and Fr(12)/Fr(128,10)*100==Fr(375,4) and Fr(12)/(nS*2*80)*100==Fr(75,2) and Fr(12)/(nS*96)*100==Fr(125,2)
s12=[25,Fr(75,2),Fr(125,2),75,Fr(375,4)]
q('0012',[A('SO₂ mol sayısı','Mol sayısı kütlenin mol kütlesine bölünmesiyle bulunur.','n = 12,8 ÷ 64 = 0,2 mol'),A('Teorik SO₃','2 mol SO₂’den 2 mol SO₃ oluşur; mol sayısı değişmez.','0,2 mol SO₃ → 0,2 × 80 = 16 g'),A('Verimi hesapla','Verim, gerçek ürünün teorik ürüne oranıdır.','12 ÷ 16 × 100 = %75')],'verim',
 z='orta',alt='Tepkime Verimi',kaz='Gerçek ve teorik ürün miktarından yüzde verimi hesaplar.',kalip='hikâyeli',
 kart='K-KMHS2-07 (yüzde verim) · SO₂’nin SO₃’e yükseltgenmesi',
 metin='Sülfürik asit üretiminde SO₂ gazı, 2SO₂ + O₂ → 2SO₃ tepkimesine göre SO₃’e dönüştürülür. Laboratuvar ölçeğinde yapılan bir denemede, yeterli miktarda O₂ içeren kapalı bir kaba 12,8 g SO₂ konuyor ve tepkime sonunda 12 g SO₃ elde ediliyor.\nO: 16 g/mol, S: 32 g/mol olduğuna göre bu tepkimenin yüzde verimi kaçtır?',
 dogru=75,yan=[(25,'Kaybolan miktarı (16 − 12 = 4 g) teorik ürüne oranlayıp bunu verim sanmış.','dikkat'),(Fr(75,2),'Katsayıyı mol sayısıyla çarpıp teorik SO₃’ü 0,4 mol (32 g) bulmuş.','islem'),(Fr(125,2),'SO₃’ün mol kütlesini 96 g/mol alıp teorik ürünü 19,2 g bulmuş.','islem'),(Fr(375,4),'Gerçek ürünü teorik ürüne değil, başlangıçtaki SO₂ kütlesine (12 ÷ 12,8) oranlamış.','dikkat')],
 istenen='Tepkimenin yüzde verimi.',ip=['Sınırlayıcı maddeden en çok kaç g ürün oluşabileceğini düşün.'],
 bilgi=[B('Yüzde verim','Verim = (gerçekte elde edilen ürün ÷ teorik ürün) × 100. Teorik ürün, sınırlayıcı bileşenin tam harcanmasıyla bulunur. Örnek: teorik 40 g, gerçek 30 g ürün %75 verimdir')],
 puf='Önce teorik ürünü hesapla; verim, gerçek ürünün teorik ürüne oranıdır.')

# ================= 13 · karışım · Mg–Cu · orta =================
nMg=Fr(224,100)/Fr(224,10); mMg=nMg*24
assert nMg==Fr(1,10) and mMg==Fr(24,10) and mMg/5*100==48 and (5-mMg)/5*100==52
assert Fr(224,100)/Fr(224,10)/2*24/5*100==24 and Fr(224,100)/Fr(224,10)*2*24/5*100==96 and mMg==Fr(24,10)
q('0013',[A('H₂ mol sayısı','Yalnız Mg tepkime verir; hacimden mol bulunur.','n(H₂) = 2,24 ÷ 22,4 = 0,1 mol'),A('Mg mol sayısı','Denklemde Mg ile H₂’nin katsayıları eşittir.','n(Mg) = 0,1 mol'),A('Mg kütlesi','Mol sayısı mol kütlesiyle çarpılır.','m(Mg) = 0,1 × 24 = 2,4 g'),A('Yüzdeyi bul','Mg kütlesi karışımın kütlesine oranlanır.','2,4 ÷ 5 × 100 = %48')],'karisim',
 z='orta',alt='Karışımlarda Tepkime',kaz='Tepkime veren bileşenin ürününden karışımdaki kütlece yüzdesini bulur.',kalip='hikâyeli',
 kart='K-KMHS2-08 (karışımda tepkime) · Mg–Cu karışımı ve H₂',
 metin='Bir laboratuvarda kütlesi 5 g olan Mg–Cu karışımı, aşırı miktarda HCl çözeltisine atılıyor. Cu, HCl ile tepkime vermezken Mg, Mg + 2HCl → MgCl₂ + H₂ tepkimesine göre tamamen çözünüyor. Tepkime sırasında açığa çıkan H₂ gazı toplanıp hacmi NK’da ölçüldüğünde 2,24 L bulunuyor.\nMg: 24 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre karışımın kütlece yüzde kaçı Mg’dur?',
 dogru=48,yan=[(Fr(24,10),'Mg’nin kütlesini (2,4 g) yüzde olarak yazmış.','dikkat'),(24,'H₂’ye göre Mg’yi yarı mol sayısında (0,05 mol) almış.','bilgi'),(52,'Karışımdaki Cu’nun kütlece yüzdesini bulmuş.','dikkat'),(96,'Mg + 2HCl’deki 2’yi Mg’ye uygulayıp 0,2 mol Mg bulmuş.','bilgi')],
 istenen='Karışımdaki Mg’nin kütlece yüzdesi.',ip=['Tepkimeye yalnız hangi maddenin girdiğini düşün; gazdan o maddenin mol sayısına geç.'],
 bilgi=[B('Karışımda tepkime','Karışımdaki bileşenlerden yalnız biri tepkime veriyorsa ürün miktarı yalnız o bileşene göre hesaplanır; sonra kütlesi karışıma oranlanır. Örnek: karışımdaki 3 g madde ayrışıyorsa ve karışım 12 g ise madde yüzdesi %25’tir')],
 puf='Tepkime vermeyen madde hesaba girmez; tepkime verenin kütlesini karışımın kütlesine oranla.')

# ================= 14 · öncüllü yüzde · orta =================
assert Fr(24*100,40)==60 and Fr(40*100,100)==40 and Fr(48*100,160)==30 and Fr(112*100,160)==70
d14={'I':(False,'MgO’nun mol kütlesi 40 g/mol, Mg’nin payı 24 g olduğundan Mg kütlece %60’tır'),
     'II':(True,'CaCO₃’ın mol kütlesi 100 g/mol, Ca’nın payı 40 g olduğundan Ca kütlece %40’tır'),
     'III':(False,'Fe₂O₃’ün mol kütlesi 160 g/mol, O’nun payı 48 g olduğundan O kütlece %30’dur')}
r=onc(d14,0)
q('0014',onc_adim(d14),'yuzde',
 z='orta',alt='Bileşiklerde Kütlece Yüzde',kaz='Bileşiklerdeki element yüzdelerine ilişkin yargıları hesaplayarak değerlendirir.',kalip='öncüllü',
 kart='K-KMHS2-03 (kütlece yüzde) · MgO, CaCO₃, Fe₂O₃',
 metin='Bir mineral koleksiyonunda bulunan kireç taşı (CaCO₃), pas (Fe₂O₃) ve magnezya (MgO) örnekleri için öğrenciler, element yüzdeleriyle ilgili aşağıdaki yargılarda bulunuyor.\nI. MgO’da Mg kütlece %40’tır.\nII. CaCO₃’ta Ca kütlece %40’tır.\nIII. Fe₂O₃’te O kütlece %70’tir.\nC: 12, O: 16, Mg: 24, Ca: 40, Fe: 56 g/mol olduğuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her bileşiğin mol kütlesini bul; sorulan elementin toplam kütlesine oranla.'],
 bilgi=[B('Bileşikte yüzde','Elementin kütlece yüzdesi, formüldeki toplam kütlesinin bileşiğin mol kütlesine oranıdır; iki elementin yüzdeleri toplamı 100’dür. Örnek: NaCl’de Na (23) ve Cl (35,5) kütlece yaklaşık %39 ve %61’dir')],
 puf='Yüzde = element kütlesi ÷ bileşik kütlesi; indis kütleyi artırır.')

# ================= 15 · hikâyeli mol → atom · orta =================
n15=Fr(22,10)/44; assert n15==Fr(1,20) and n15*6==Fr(3,10) and n15*2*6==Fr(6,10)
s15=['3 × 10²²','6 × 10²²','9 × 10²²','1,2 × 10²³','1,8 × 10²³']
assert n15*6*Fr(1,10)==Fr(3,100) # 3×10²² molekül = 0,3×10²³
assert n15*4*6==Fr(12,10) and n15*3*2*6==Fr(18,10) and n15*3*6==Fr(9,10)
q('0015',[A('CO₂ mol kütlesi','CO₂ molekülünde 1 C ve 2 O atomu vardır.','M = 12 + 2 × 16 = 44 g/mol'),A('Mol sayısı','Kütle mol kütlesine bölünür.','n = 2,2 ÷ 44 = 0,05 mol'),A('O atomu sayısı','Her molekülde 2 O atomu bulunur.','0,05 × 2 × 6 × 10²³ = 6 × 10²²')],'mol',
 z='orta',alt='Mol Kavramı',kaz='Verilen kütlenin içerdiği belirli atomların sayısını hesaplar.',kalip='hikâyeli',
 kart='K-KMHS2-02 (mol–atom sayısı) · içecekte çözünmüş CO₂',
 metin='Gazlı bir içeceğin şişesi açıldığında içeceğin içinde çözünmüş hâlde bulunan CO₂ gazının kabarcıklar hâlinde çıktığı görülür. Bir şişede çözünmüş hâldeki CO₂ gazının kütlesi 2,2 g olarak belirleniyor.\nC: 12 g/mol, O: 16 g/mol ve N_A = 6 × 10²³ olduğuna göre bu CO₂ gazındaki toplam oksijen atomu sayısı kaçtır?',
 dogru=s15[1],sira=s15,yan=[(s15[0],'Oksijen atomu yerine CO₂ molekül sayısını bulmuş.','dikkat'),(s15[2],'Karbon dahil tüm atomları (3 atom) saymış.','dikkat'),(s15[3],'Oksijen indisi yerine molekül başına 4 atom alıp 0,05 × 4 × 6 × 10²³ hesaplamış.','bilgi'),(s15[4],'Toplam atom sayısını (3) bir de oksijen indisiyle (2) çarpmış.','islem')],
 istenen='Gazdaki toplam oksijen atomu sayısı.',ip=['Önce CO₂’nin mol sayısını bul; sonra yalnız oksijen atomlarını say.'],
 bilgi=[B('Belirli atomun sayısı','Aranan atomun sayısı = bileşiğin mol sayısı × formüldeki o atomun indisi × N_A. Örnek: 0,1 mol H₂O’da 0,2 mol H atomu bulunur')],
 puf='Atom sayısı = mol × indis × N_A; sorulan atomun indisini kullan.')

# ================= 16 · öncüllü etilen yanması · orta =================
nE=Fr(56,10)/Fr(224,10); assert nE==Fr(1,4) and nE*3*Fr(224,10)==Fr(168,10) and Fr(14,28)*2*18==18 and 3!=2
d16={'I':(False,'denklemde 1 mol C₂H₄’e karşılık 2 mol CO₂ oluşur; katsayı 3 olan madde O₂’dir'),
     'II':(False,'5,6 L C₂H₄ 0,25 moldür; 3 katı olan 0,75 mol O₂, NK’da 0,75 × 22,4 = 16,8 L hacim kaplar'),
     'III':(True,'14 g C₂H₄ 0,5 moldür; 2 katı olan 1 mol H₂O oluşur ve kütlesi 18 g’dır')}
r=onc(d16,0)
q('0016',onc_adim(d16),'tepkime',
 z='orta',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Yanma denkleminden mol, hacim ve kütle ilişkilerine ait yargıları değerlendirir.',kalip='öncüllü',
 kart='K-KMHS2-05 (denklemden mol–kütle–hacim) · etilen yanması',
 metin='Meyvelerin olgunlaştırılmasında kullanılan etilen (C₂H₄) gazı, yeterli O₂ ile C₂H₄ + 3O₂ → 2CO₂ + 2H₂O tepkimesine göre tamamen yanıyor.\nI. 1 mol C₂H₄ yandığında 3 mol CO₂ oluşur.\nII. NK’da 5,6 L C₂H₄’ün yanması için NK’da 11,2 L O₂ gerekir.\nIII. 14 g C₂H₄ yandığında 18 g H₂O oluşur.\nH: 1 g/mol, C: 12 g/mol, O: 16 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her yargıda verilen maddeyi mole çevir; denklemdeki katsayı oranıyla istenen maddeye geç.'],
 bilgi=[B('Yanma denklemi','Katsayılar mol oranını verir; gazlar için NK’da hacim oranı da mol oranına eşittir. Örnek: CH₄ + 2O₂ → CO₂ + 2H₂O tepkimesinde 1 mol CH₄ için 2 mol O₂ gerekir')],
 puf='Önce verilen maddeyi mole çevir; katsayı oranıyla diğer maddeye geç, sonra kütle ya da hacme çevir.')

# ================= 17 · tanecik modeli · sınırlayıcı · zor =================
nN2,nH2m=3,6; per=Fr(1,2)
mN=nN2*per; mHh=nH2m*per; usedN=min(mN,mHh/3); leftN=mN-usedN; leftH=mHh-3*usedN
assert (mN,mHh)==(Fr(3,2),3) and usedN==1 and leftN==Fr(1,2) and leftN*28==14 and leftH==0 and usedN*2*17==34
assert Fr(3,2)*28==42 and mHh*2==6 and (mHh-mN)*2==3 and 1*28==28   # 1:1 → H₂ 1,5 mol artar (3 g); H₂'nin tamamı 6 g; her molekül 1 mol → 28 g
g=kapdiz(4.9,3.4,nH2m,nN2,seed=5,m=.85)+'\\node[above] at (2.45,3.45) {Tepkimeden önce};'+lejant(5.6,2.4,['H$_2$','N$_2$'])
SK=tk(g)
q('0017',[A('Mol sayıları','Şekildeki her molekül 0,5 mol demektir: 3 N₂ ve 6 H₂.','n(N₂) = 3 × 0,5 = 1,5 mol · n(H₂) = 6 × 0,5 = 3 mol'),A('Sınırlayıcı madde','Her 1 mol N₂ için 3 mol H₂ gerekir; 3 mol H₂ yalnız 1 mol N₂ ile tepkimeye girer.','H₂ sınırlayıcı · harcanan N₂ = 1 mol'),A('Artan N₂','Başlangıç mol sayısından harcanan çıkarılır.','1,5 − 1 = 0,5 mol'),A('Kütleye çevir','N₂’nin mol kütlesi 2 × 14 = 28 g/mol’dür.','0,5 × 28 = 14 g')],'sinirlayici',
 z='zor',alt='Sınırlayıcı Bileşen',kaz='Tanecik modelinden sınırlayıcı bileşeni bulup artan maddenin kütlesini hesaplar.',kalip='şekilli',
 kart='K-KMHS2-06 (sınırlayıcı bileşen ve artan madde) · kapta N₂ ve H₂ modeli, mol ve kütle',sekil=SK,
 metin='Sert ve kapalı bir kapta N₂ ve H₂ gazlarının tepkimeden önceki durumu şekildeki gibi modellenmiştir; çizimdeki her molekül 0,5 mol gazı temsil etmektedir. Gazlar, N₂ + 3H₂ → 2NH₃ tepkimesine göre sınırlayıcı bileşen tamamen harcanıncaya kadar tepkimeye girmektedir.\nH: 1 g/mol, N: 14 g/mol olduğuna göre tepkime sonunda kapta artan gazın kütlesi kaç gramdır?',
 dogru=14,yan=[(3,'N₂ ile H₂’yi 1 : 1 oranında tepkimeye sokup artan H₂’yi (1,5 mol) bulmuş.','bilgi'),(6,'Artan madde olarak H₂’nin başlangıçtaki kütlesini (3 mol) yazmış.','dikkat'),(28,'Her molekülü 1 mol sayıp 3 mol N₂ ile 6 mol H₂’den 1 mol N₂ artırmış.','dikkat'),(42,'N₂’nin tamamının (1,5 mol) artan olduğunu sanmış.','dikkat')],
 istenen='Tepkime sonunda artan gazın kütlesi (g).',ip=['Her türün mol sayısını bul; katsayı oranına göre hangisinin önce biteceğine bak.'],
 bilgi=[B('Sınırlayıcı bileşen','mol sayısı katsayısına bölündüğünde en küçük değeri veren maddedir. Örnek: 2A + B → ürün tepkimesinde 4 mol A (4 ÷ 2 = 2) ve 3 mol B (3 ÷ 1 = 3) varsa A sınırlayıcıdır')],
 puf='Mol sayılarını katsayılara böl; en küçüğü sınırlayıcıdır, artan miktar harcananı çıkararak bulunur.')

# ================= 18 · grafik · Mg + O₂ · orta =================
nMgO=Fr(40,40); nO2=nMgO/2
assert nMgO==1 and nO2*Fr(224,10)==Fr(112,10)
assert nMgO*Fr(224,10)==Fr(224,10) and Fr(40,32)*Fr(224,10)==28 and nMgO*2*Fr(224,10)==Fr(448,10) and nMgO/4*Fr(224,10)==Fr(56,10) and 40-24==16
s18=[Fr(56,10),Fr(112,10),Fr(224,10),28,Fr(448,10)]
g='\\begin{axis}[width=7.4cm,height=5.6cm,xmin=0,xmax=33,ymin=0,ymax=48,xtick={0,6,12,18,24,30},ytick={0,10,20,30,40},tick label style={font=\\small},axis lines=left,xlabel={Eklenen toplam Mg kütlesi (g)},ylabel={Oluşan MgO kütlesi (g)},xlabel style={font=\\small},ylabel style={font=\\small}]'
g+='\\addplot[thick,vurgu] coordinates {(0,0) (24,40) (30,40)};\\draw[dashed,thin] (axis cs:0,40) -- (axis cs:24,40) -- (axis cs:24,0);\\end{axis}'
SK=tk(g)
q('0018',[A('Grafiği oku','Eğri yatay olunca O₂ tükenmiştir; en çok oluşan MgO 40 g’dır.','Plato: m(MgO) = 40 g'),A('MgO mol sayısı','MgO’nun mol kütlesi 24 + 16 = 40 g/mol’dür.','n(MgO) = 40 ÷ 40 = 1 mol'),A('O₂ mol sayısı','2Mg + O₂ → 2MgO denkleminde 2 mol MgO için 1 mol O₂ gerekir.','n(O₂) = 1 ÷ 2 = 0,5 mol'),A('Hacme çevir','NK’da mol sayısı 22,4 ile çarpılır.','V = 0,5 × 22,4 = 11,2 L')],'tepkime',
 z='orta',alt='Kimyasal Tepkimelerde Hesaplamalar',kaz='Kütle–kütle grafiğinden başlangıçtaki gazın NK’daki hacmini hesaplar.',kalip='grafik',
 kart='K-KMHS2-05 (kütle–kütle grafiği) · sabit O₂ üzerine Mg eklenmesi',sekil=SK,
 metin='Sert ve kapalı bir kapta bir miktar O₂ gazı bulunmaktadır. Kaba küçük kısımlar hâlinde Mg parçaları ekleniyor ve her eklemeden sonra 2Mg + O₂ → 2MgO tepkimesi tamamlanıyor. Eklenen toplam Mg kütlesi ile kapta oluşan toplam MgO kütlesi arasındaki ilişki şekildeki grafikte verilmiştir.\nMg: 24 g/mol, O: 16 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre kapta başlangıçta bulunan O₂ gazı NK’da kaç L hacim kaplar?',
 dogru=Fr(112,10),yan=[(s18[0],'MgO’nun mol sayısını (1) katsayılarla iki kez 2’ye bölüp 0,25 mol O₂ bulmuş.','islem'),(s18[2],'MgO ile O₂’yi 1 : 1 oranında alıp 1 mol O₂ bulmuş.','bilgi'),(28,'40 g’ı O₂’nin kütlesi sanıp 40 ÷ 32 = 1,25 mol bulmuş.','dikkat'),(s18[4],'Katsayıları ters kurup 1 mol MgO için 2 mol O₂ bulmuş.','islem')],
 istenen='Başlangıçtaki O₂ gazının NK’daki hacmi (L).',ip=['Mg eklemeye rağmen MgO kütlesinin artmadığı noktayı yorumla.'],
 bilgi=[B('Kütle–kütle grafiği','Reaktiflerden biri tükenince ürün kütlesi artmayı bırakır ve grafik yatay olur; yatay değer o koşulda oluşabilecek en çok üründür. Örnek: 2A + B → C tepkimesinde B tükenince oluşan en çok C, B’nin mol sayısına göre bulunur')],
 puf='Grafikte düzleşme sınırlayıcının bittiğini gösterir; platodaki ürün miktarından sınırlayıcıya geç.')

# ================= 19 · verim + sınırlayıcı · zor =================
n_N=Fr(112,10)/28; n_H=Fr(12,10)/2; th_nh3=min(n_N*2,n_H*2/3); real=th_nh3*Fr(3,4)
assert n_N==Fr(2,5) and n_H==Fr(3,5) and th_nh3==Fr(2,5) and real*17==Fr(51,10)
assert th_nh3*17==Fr(68,10) and n_N*2*17==Fr(136,10) and n_N*2*Fr(3,4)*17==Fr(102,10) and n_H/3*17==Fr(34,10)
q('0019',[A('Mol sayıları','Kütleler mol kütlelerine bölünür (N₂: 28, H₂: 2 g/mol).','n(N₂) = 11,2 ÷ 28 = 0,4 mol · n(H₂) = 1,2 ÷ 2 = 0,6 mol'),A('Sınırlayıcıyı bul','Mol sayıları katsayılara bölünür: N₂ için 0,4 ÷ 1, H₂ için 0,6 ÷ 3.','N₂: 0,4 · H₂: 0,2 → H₂ sınırlayıcı'),A('Teorik NH₃','3 mol H₂’den 2 mol NH₃ oluşur.','0,6 × 2 ÷ 3 = 0,4 mol'),A('Gerçek NH₃','Verim %75 olduğundan teorik ürünün 3/4’ü elde edilir.','0,4 × 0,75 = 0,3 mol · 0,3 × 17 = 5,1 g')],'verim',
 z='zor',alt='Tepkime Verimi',kaz='Sınırlayıcı bileşene göre teorik ürünü bulup yüzde verimle gerçek ürün kütlesini hesaplar.',kalip='düz',
 kart='K-KMHS2-07 (verim ve sınırlayıcı bileşen) · N₂ ve H₂ ile NH₃ sentezi',
 metin='Amonyak sentezinde 11,2 g N₂ gazı ile 1,2 g H₂ gazı, uygun koşullarda kapalı bir kapta N₂ + 3H₂ → 2NH₃ tepkimesine sokuluyor. Tepkimenin yüzde verimi %75 olarak bulunuyor.\nH: 1 g/mol, N: 14 g/mol olduğuna göre tepkime sonunda elde edilen NH₃ kaç gramdır?',
 dogru=Fr(51,10),yan=[(Fr(34,10),'H₂’nin mol sayısını (0,6) yalnız 3’e bölüp 0,2 mol NH₃ bulmuş; NH₃ katsayısını (2) kullanmamış.','bilgi'),(Fr(68,10),'Sınırlayıcıyı bulmuş ama yüzde verimi uygulamamış (teorik ürün).','dikkat'),(Fr(102,10),'N₂’yi sınırlayıcı sanıp verimi uygulamış.','bilgi'),(Fr(136,10),'N₂’yi sınırlayıcı sanmış ve verimi uygulamamış.','bilgi')],
 istenen='Tepkime sonunda elde edilen NH₃’ün kütlesi (g).',ip=['Önce hangi maddenin önce biteceğini bul; yüzde verimi en son uygula.'],
 bilgi=[B('Verim ve sınırlayıcı','Önce sınırlayıcı bileşen bulunur, teorik ürün ona göre hesaplanır; gerçek ürün = teorik ürün × verim. Örnek: teorik 20 g ürün ve %60 verimde 12 g ürün elde edilir')],
 puf='Sıra: mol → sınırlayıcı → teorik ürün → verim çarpanı → kütle.')

# ================= 20 · öncüllü olumsuz · H₂ + Cl₂ · zor =================
nh,nc=Fr(672,100)/Fr(224,10),Fr(448,100)/Fr(224,10); assert nh==Fr(3,10) and nc==Fr(2,10) and nc<nh
lefth=nh-nc; assert lefth*Fr(224,10)==Fr(224,100) and (nh+nc)==(lefth+2*nc) and nc*2*Fr(365,10)==Fr(146,10)
d20={'I':(True,'tepkime 1 : 1 mol oranında gerçekleşir ve 0,2 mol Cl₂ ile 0,3 mol H₂ içinde Cl₂ önce biter'),
     'II':(False,'0,3 − 0,2 = 0,1 mol H₂ artar; bu da NK’da 0,1 × 22,4 = 2,24 L hacim kaplar'),
     'III':(False,'başlangıçta 0,5 mol gaz vardır; sonunda 0,1 mol H₂ ve 0,4 mol HCl olmak üzere yine 0,5 mol gaz bulunur')}
r=onc(d20,3,olumsuz=True)
q('0020',onc_adim(d20,olumsuz=True,pre=[A('Mol sayıları','NK’da hacim 22,4 L/mol’e bölünür.','n(H₂) = 6,72 ÷ 22,4 = 0,3 mol · n(Cl₂) = 4,48 ÷ 22,4 = 0,2 mol')]),'sinirlayici',
 z='zor',alt='Sınırlayıcı Bileşen',kaz='Gaz hacimleri verilen tepkimede sınırlayıcı bileşeni, artan gazı ve toplam mol sayısını değerlendirir.',kalip='öncüllü',
 kart='K-KMHS2-06 (sınırlayıcı bileşen) · H₂ ve Cl₂ ile HCl oluşumu',
 metin='Sert ve kapalı bir kapta, NK’da ölçülen 6,72 L H₂ ve 4,48 L Cl₂ gazı karıştırılıp H₂ + Cl₂ → 2HCl tepkimesine göre sınırlayıcı bileşen tamamen harcanıncaya kadar tepkimeye sokuluyor. Tepkimedeki bütün maddeler gaz hâlindedir.\nI. Cl₂ sınırlayıcı bileşendir.\nII. Tepkime sonunda NK’da 4,48 L H₂ gazı artar.\nIII. Tepkime sonunda kaptaki toplam gaz mol sayısı, başlangıçtakinden azdır.\nNK’da 1 mol gaz 22,4 L olduğuna göre yukarıdaki ifadelerden hangileri yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifadeler.',ip=['Gazların mol sayılarını bul; denklemdeki oranla hangisinin önce biteceğine ve sonunda kaç mol gaz kaldığına bak.'],
 bilgi=[B('Gaz tepkimesinde mol sayısı','Katsayılar gazlar için de mol oranını verir; toplam gaz mol sayısı tepkimede katsayılara bağlı olarak azalabilir, artabilir ya da sabit kalabilir. Örnek: N₂ + 3H₂ → 2NH₃ tepkimesinde toplam gaz mol sayısı azalır (4 mol → 2 mol)')],
 puf='Sınırlayıcıyı bul; artanı ve oluşanı denklem oranıyla yaz, toplam mol sayısını yeniden say.')

# ================= 21 · karışım · eşit mol Mg–Al · zor =================
xe=Fr(51,10)/(24+27); nH21=xe*1+xe*Fr(3,2)
assert xe==Fr(1,10) and nH21==Fr(1,4) and nH21*Fr(224,10)==Fr(56,10)
assert xe*Fr(224,10)==Fr(224,100) and xe*Fr(3,2)*Fr(224,10)==Fr(336,100) and 2*xe*Fr(224,10)==Fr(448,100) and (2*xe+3*xe)*Fr(224,10)==Fr(112,10)
q('0021',[A('Mol sayıları','Mol sayıları eşit olduğundan her metal için x mol yazılır; kütleler toplanır.','24x + 27x = 5,1 → x = 0,1 mol'),A('Mg’den H₂','Denklemde 1 mol Mg 1 mol H₂ verir.','0,1 mol H₂'),A('Al’den H₂','Denklemde 2 mol Al 3 mol H₂ verir.','0,1 × 3 ÷ 2 = 0,15 mol H₂'),A('Hacme çevir','Toplam mol sayısı 22,4 ile çarpılır.','(0,1 + 0,15) × 22,4 = 5,6 L')],'karisim',
 z='zor',alt='Karışımlarda Tepkime',kaz='Mol sayıları eşit iki metal karışımından toplam gaz hacmini hesaplar.',kalip='düz',
 kart='K-KMHS2-08 (karışımda tepkime) · eşit mol Mg–Al karışımı ve H₂ hacmi',
 metin='Mg ve Al metal tozlarından, mol sayıları birbirine eşit olacak biçimde hazırlanmış 5,1 g kütleli bir karışım aşırı miktarda HCl çözeltisine atılıyor. Her iki metal de tamamen çözünüyor. Tepkimeler şöyledir:\nMg + 2HCl → MgCl₂ + H₂\n2Al + 6HCl → 2AlCl₃ + 3H₂\nMg: 24 g/mol, Al: 27 g/mol ve NK’da 1 mol gaz 22,4 L olduğuna göre açığa çıkan H₂ gazı NK’da kaç L hacim kaplar?',
 dogru=Fr(56,10),yan=[(Fr(224,100),'Yalnız Mg’den gelen H₂’yi (0,1 mol) hesaplamış.','dikkat'),(Fr(336,100),'Yalnız Al’den gelen H₂’yi (0,15 mol) hesaplamış.','dikkat'),(Fr(448,100),'Al için de 1 mol metalden 1 mol H₂ çıktığını sanıp 0,2 mol H₂ bulmuş.','bilgi'),(Fr(112,10),'Mg için 2 (HCl katsayısı), Al için 3 (H₂ katsayısı) mol H₂ alıp 0,5 mol bulmuş.','bilgi')],
 istenen='Açığa çıkan H₂ gazının NK’daki hacmi (L).',ip=['Önce karışımda her metalden kaç mol bulunduğunu belirle.'],
 bilgi=[B('Karışımda tepkime','Karışımdaki her bileşenin ürüne katkısı ayrı hesaplanır, sonra toplanır. Örnek: 0,2 mol A’dan 0,4 mol, 0,1 mol B’den 0,3 mol gaz çıkıyorsa toplam gaz 0,7 moldür')],
 puf='Her metalin katkısını denklemden ayrı bul, sonra topla.')

# ================= 22 · grafik · Mg + S · zor · öncüllü =================
nMg0,nS0=Fr(12,24),Fr(24,32); usedMg=nMg0; usedS=usedMg*1; leftS=nS0-usedS; MgS=usedMg*56
assert nMg0==Fr(1,2) and nS0==Fr(3,4) and leftS==Fr(1,4) and leftS*32==8 and MgS==28 and 24-8==16 and 8+28==36 and 12+24==36
d22={'I':(True,'tepkimede 12 g Mg (0,5 mol) ve 16 g S (0,5 mol) harcanır; mol oranı 1 : 1’dir'),
     'II':(True,'artan S 8 g’dır ve 8 ÷ 32 = 0,25 moldür'),
     'III':(True,'oluşan 28 g MgS, 28 ÷ 56 = 0,5 moldür')}
r=onc(d22,4)
g='\\begin{axis}[width=7.6cm,height=5.8cm,xmin=0,xmax=7.6,ymin=0,ymax=30,xtick={0,4},ytick={0,8,12,24,28},tick label style={font=\\small},axis lines=left,xlabel={Zaman (dk)},ylabel={Kütle (g)},xlabel style={font=\\small},ylabel style={font=\\small}]'
g+='\\addplot[thick] coordinates {(0,12) (4,0) (6.2,0)};\\addplot[thick,dashed] coordinates {(0,24) (4,8) (6.2,8)};\\addplot[thick,vurgu] coordinates {(0,0) (4,28) (6.2,28)};'
g+='\\node[anchor=west,font=\\small] at (axis cs:6.3,1.5) {Mg};\\node[anchor=west,font=\\small] at (axis cs:6.3,8) {S};\\node[anchor=west,font=\\small] at (axis cs:6.3,28) {MgS};'
g+='\\draw[dotted,thin] (axis cs:4,0) -- (axis cs:4,28);\\end{axis}'
SK=tk(g)
q('0022',onc_adim(d22,pre=[A('Grafiği oku','Mg tükenir; S ve MgS’nin son değerleri okunur.','Mg: 12 → 0 g; S: 24 → 8 g; MgS: 0 → 28 g')]),'sinirlayici',
 z='orta',alt='Sınırlayıcı Bileşen',kaz='Kütle–zaman grafiğinden harcanan, artan ve oluşan maddelerin mol sayılarını yorumlar.',kalip='grafik',
 kart='K-KMHS2-06 (sınırlayıcı bileşen) · Mg ve S tepkimesinde kütle–zaman grafiği',sekil=SK,
 metin='Kapalı bir kapta Mg ve S katıları, Mg + S → MgS tepkimesine göre tepkimeye giriyor. Kaptaki Mg, S ve MgS kütlelerinin zamanla değişimi şekildeki grafikte verilmiştir; tepkimeye başka madde girmemiştir.\nI. Mg ve S, tepkimede 1 : 1 mol oranında harcanmıştır.\nII. Tepkime sonunda 0,25 mol S artmıştır.\nIII. Tepkimede 0,5 mol MgS oluşmuştur.\nMg: 24 g/mol, S: 32 g/mol olduğuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Eğrilerin başlangıç ve son değerlerini oku; her kütle değişimini ilgili mol kütlesiyle mole çevir.'],
 bilgi=[B('Harcanan ve oluşan','tepkimede azalan madde harcanır, artan madde oluşur; değişim miktarları mol oranına göre belirlenir. Örnek: 2A + B → C tepkimesinde 6 mol A harcanırsa 3 mol B harcanır ve 3 mol C oluşur')],
 puf='Grafikte azalma harcananı, artış oluşanı verir; mole çevirip oranlarına bak.')

bitir(P,'hesaplamaiki',UK)
