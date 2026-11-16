"""TYT Biyoloji · Hücrede Bölünme – Üreme · ek paket (bolunmeiki): 34 soru, kardeş yok, ipucu 1.
Hücre evre çizimleri (kromozom biçimi ve sayısı), DNA miktarı/kromozom sayısı grafikleri ve tablolar Python'da hesaplanan değerlerden TikZ ile çizilir;
her doğru şık ve her çeldirici değeri assert edilir; öncüllerin doğru/yanlış değeri tek yerde (durum sözlüğü) tanımlanır."""
import sys,os,math,random,itertools
GD=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,GD)
import _hafif_bio as H
from _hafif_bio import *
KONU_='Hücrede Bölünme – Üreme'; UK='bio|Hücrede Bölünme – Üreme'
H.KONU=KONU_
P=Parti('bolunmeiki',KONU_,UK,ders='TYT Biyoloji',idon='tytbio')
KY='ÖSYM 2018–2026 TYT Biyoloji dağılımı (yalnız mantık) · MEB 10. sınıf Hücrede Bölünme ve Üreme'
TIPLER={'dongu':'Hücre döngüsü ve interfaz','mitoz':'Mitoz evreleri ve sitokinez','esesiz':'Eşeysiz üreme çeşitleri','mayoz':'Mayoz bölünme ve kalıtsal çeşitlilik',
        'karsilastir':'Mitoz–mayoz ve eşeyli–eşeysiz karşılaştırma','grafik':'DNA miktarı ve kromozom sayısı grafikleri','hesap':'Kromozom, gamet ve hücre sayısı hesapları','insan':'İnsanda üreme ve gelişme'}
def Q(no,tp,z,alt,kaz,kalip,fikir,tuzak,ne,**k):
    assert len(k['ip'])==1 and tp in TIPLER
    kart(f'K-BYBL2-{no}',alt,fikir,tuzak,z,kalip,len(k['ad']),f'by-bl2-{tp}',TIPLER[tp],KY)
    mk(P,'00'+no,tipId=f'by-bl2-{tp}',tip=TIPLER[tp],z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(k['ad']),kart=f'K-BYBL2-{no} ({TIPLER[tp].lower()}) · {ne}',**k)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
ST=['I','II','III']
OPS=[('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]
def adla(s): return ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
def onc(durum,hedef=True,harf=None,seed=1):
    """durum {'I':(ifade,bool,gerçek,başlık)}; hedef True: doğru olanlar istenir, False: yanlış olanlar. harf: doğru şıkkın harfi."""
    T=tuple(k for k in ST if durum[k][1]==hedef); assert T in OPS,T
    p=OPS.index(T); rnd=random.Random(seed+len(T)*7+p)
    onceki=OPS[:p]; sonraki=OPS[p+1:]
    if harf is None:
        for h in range(1,6):
            if h-1<=len(onceki) and 5-h<=len(sonraki): harf=h; break
    h=harf; assert h-1<=len(onceki) and 5-h<=len(sonraki),(T,h)
    sec=sorted(rnd.sample(range(len(onceki)),h-1))+[p]+sorted(p+1+i for i in rnd.sample(range(len(sonraki)),5-h))
    ops=[OPS[i] for i in sec]; yan=[]
    for o in ops:
        if o==T: continue
        c=[]
        for x in ST:
            if (x in o)!=(x in T):
                if hedef: c.append(f'{x} öncülünü '+('doğru' if x in o else 'yanlış')+f' sanmış; oysa {durum[x][2].rstrip(".")}')
                else: c.append(f'{x} öncülünü '+('yanlış' if x in o else 'doğru')+f' sanmış; oysa {durum[x][2].rstrip(".")}')
        yan.append((adla(o),'. '.join(c)+'.','bilgi'))
    kelime='doğru' if hedef else 'yanlış'
    ad=[A(durum[x][3],durum[x][2],f'{x}: '+('doğru' if durum[x][1] else 'yanlış')) for x in ST]
    ad.append(A('Sonucu yaz',f'{kelime.capitalize()} olan öncüller aranıyor.',adla(T)))
    return dict(dogru=adla(T),yan=yan,sira=[adla(o) for o in ops],ad=ad)
def tek(sec,hedef=True,harf=None,tur='bilgi'):
    """sec: [(ifade,bool,gerçek)]; tek bir ifade bool==hedef; harf: doğru şıkkın harfi."""
    h=[s for s in sec if s[1]==hedef]; assert len(h)==1,[s[0] for s in sec if s[1]==hedef]
    diger=[s for s in sec if s[1]!=hedef]; assert len(diger)==4
    harf=harf or 1; sira=diger[:harf-1]+h+diger[harf-1:]
    yan=[(m,(f'Bu ifadeyi doğru sanmış; oysa {n}' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}'),tur) for m,b,n in diger]
    return dict(dogru=h[0][0],yan=yan,sira=[s[0] for s in sira],gercek=h[0][2])
def sayi_sik(degerler,dogru):
    return degerler
# ---------------- çizim yardımcıları ----------------
REN={'k':'black','g':'vurgu'}; AD_={'L':(.12,.32),'M':(.105,.26),'S':(.09,.2)}
def kr(t,boy,renk,x,y,ang=0): return (t,boy,renk,x,y,ang)
def kromozom(cx,cy,c):
    t,boy,renk,x,y,ang=c; X=cx+x; Y=cy+y; col=REN[renk]
    if t=='D':
        a,bb=AD_[boy]
        return (f'\\begin{{scope}}[shift={{({X:.3f},{Y:.3f})}},rotate={ang}]\\draw[{col},line width=1.7pt] ({-a},{-bb})--({a},{bb});\\draw[{col},line width=1.7pt] ({-a},{bb})--({a},{-bb});\\end{{scope}}')
    dx,bb={'L':(.17,.30),'M':(.15,.25),'S':(.12,.2)}[boy]; s=-1 if x<0 else 1
    return f'\\draw[{col},line width=1.7pt] ({X-s*dx:.3f},{Y-bb:.3f})--({X:.3f},{Y:.3f})--({X-s*dx:.3f},{Y+bb:.3f});'
def hucre(cx,cy,krl,asama,rx=1.55,ry=1.2,et=None,cent=False):
    o=[f'\\draw[line width=.9pt] ({cx},{cy}) ellipse ({rx} and {ry});']
    for s in (-1,1):
        px=cx+s*(rx-.23)
        if asama=='plak':
            for c in krl: o.append(f'\\draw[gray,line width=.6pt] ({px:.2f},{cy}) -- ({cx+c[3]:.3f},{cy+c[4]:.3f});')
        elif asama=='kutup':
            for c in krl:
                if (c[3]<0)==(s<0): o.append(f'\\draw[gray,line width=.6pt] ({px:.2f},{cy}) -- ({cx+c[3]:.3f},{cy+c[4]:.3f});')
        if asama in ('plak','kutup'):
            if cent: o.append(sentriyol(px,cy))
            else: o.append(f'\\fill ({px:.2f},{cy}) circle (.055);')
    for c in krl: o.append(kromozom(cx,cy,c))
    if et: o.append(f'\\node[font=\\normalsize\\bfseries] at ({cx},{cy-ry-.35}) {{{et}}};')
    return '\n'.join(o)
def cekirdek(x,y,r=.42):
    return (f'\\draw[line width=.8pt] ({x},{y}) circle ({r});'
            f'\\draw[line width=1pt] ({x-.22*r/.42:.2f},{y+.12}) .. controls ({x-.05},{y+.34}) and ({x+.05},{y-.34}) .. ({x+.22*r/.42:.2f},{y-.1});'
            f'\\draw[line width=1pt] ({x-.2*r/.42:.2f},{y-.16}) .. controls ({x-.05},{y+.06}) and ({x+.06},{y-.1}) .. ({x+.2*r/.42:.2f},{y+.16});')
def sentriyol(x,y,a=0):  # tek sembol: birbirine dik iki kısa çubuk
    return (f'\\begin{{scope}}[shift={{({x:.3f},{y:.3f})}},rotate={a}]\\draw[line width=1.8pt] (-.13,0)--(.13,0);\\draw[line width=1.8pt] (0,.03)--(0,.26);\\end{{scope}}')
def hayvan_tel(cx,cy,rx=.95,ry=1.05,d=.85,cent=True):
    """hayvan hücresi telofaz: iki yavru çekirdek, hücre zarı içe boğumlanmış"""
    th0=math.acos(-d/rx); n=70; o=[]
    for s in (-1,1):
        pts=[(s*(d+rx*math.cos(-th0+2*th0*i/n)),ry*math.sin(-th0+2*th0*i/n)) for i in range(n+1)]
        o.append('\\draw[line width=.9pt] '+' -- '.join(f'({cx+x:.3f},{cy+y:.3f})' for x,y in pts)+';')
        o.append(cekirdek(cx+s*d,cy+.1,.4))
        if cent: o.append(sentriyol(cx+s*(d+.62),cy-.62,0 if s<0 else 0))
    return '\n'.join(o)
def bitki_tel(cx,cy,w=3.2,h=2.2):
    o=[f'\\draw[line width=1.4pt,rounded corners=6pt] ({cx-w/2},{cy-h/2}) rectangle ({cx+w/2},{cy+h/2});',
       f'\\draw[line width=.7pt,rounded corners=5pt] ({cx-w/2+.12},{cy-h/2+.12}) rectangle ({cx+w/2-.12},{cy+h/2-.12});',
       f'\\draw[line width=1.6pt,dash pattern=on 3pt off 2pt] ({cx},{cy-h/2+.12}) -- ({cx},{cy+h/2-.12});']
    for s in (-1,1): o.append(cekirdek(cx+s*.85,cy,.4))
    return '\n'.join(o)
def interfaz(cx,cy,rx=1.55,ry=1.2,et=None):
    o=[f'\\draw[line width=.9pt] ({cx},{cy}) ellipse ({rx} and {ry});',cekirdek(cx,cy,.62),f'\\fill ({cx+.18},{cy-.2}) circle (.07);']
    if et: o.append(f'\\node[font=\\normalsize\\bfseries] at ({cx},{cy-ry-.35}) {{{et}}};')
    return '\n'.join(o)
def profaz(cx,cy,krl,rx=1.55,ry=1.2,et=None):
    o=[sentriyol(cx-1.32,cy),sentriyol(cx+1.32,cy),f'\\draw[line width=.9pt] ({cx},{cy}) ellipse ({rx} and {ry});',f'\\draw[line width=.6pt,dash pattern=on 2pt off 2pt] ({cx},{cy}) circle (.98);']
    for c in krl: o.append(kromozom(cx,cy,c))
    if et: o.append(f'\\node[font=\\normalsize\\bfseries] at ({cx},{cy-ry-.35}) {{{et}}};')
    return '\n'.join(o)
def etiket(cx,cy,t,ry=1.2): return f'\\node[font=\\normalsize\\bfseries] at ({cx},{cy-ry-.35}) {{{t}}};'
# ---- tablo/grafik ----
def F(pts,x):
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        if x0<=x<=x1: return y0 if x1==x0 else y0+(y1-y0)*(x-x0)/(x1-x0)
    raise ValueError(x)
def eksen(pts,yt,xmax,ymax,bolge=None,w=6.6,h=4.3,ylab='DNA miktarı (birim)',xlab='Zaman',at=None,etik=None,ytl=None,title=None):
    """pgfplots ekseni; bolge: (sınırlar listesi, etiket listesi) — aralık numaraları üstte."""
    a=f',at={{({at})}}' if at else ''
    if title: a+=f',title={{\\bfseries\\normalsize {title}}}'
    yts=','.join(str(v) for v in yt)
    b=[f'\\begin{{axis}}[width={w}cm,height={h}cm,xmin=0,xmax={xmax},ymin=0,ymax={ymax},xtick=\\empty,ytick={{{yts}}},axis lines=left,xlabel={{{xlab}}},ylabel={{{ylab}}},'
       f'tick label style={{font=\\small}},label style={{font=\\small}},every axis plot/.append style={{line width=1.6pt}}{a}]'.replace('\\\\','\\')]
    b.append('\\addplot[black] coordinates {'+' '.join(f'({x},{y})' for x,y in pts)+'};')
    if bolge:
        sn,et=bolge
        for x in sn[1:-1]: b.append(f'\\draw[gray,dashed] (axis cs:{x},0) -- (axis cs:{x},{ymax*.93});')
        for i,e in enumerate(et): b.append(f'\\node[font=\\normalsize\\bfseries] at (axis cs:{(sn[i]+sn[i+1])/2},{ymax*.97}) {{{e}}};')
    b.append('\\end{axis}')
    return '\n'.join(b)
def oncm(giris,durum,kok): return giris+'\n'+'\n'.join(f'{k}. {durum[k][0]}' for k in ST)+'\n'+kok
def tabl(bas,sat):
    n=len(bas); assert all(len(r)==n for r in sat)
    gen=[max(56,round(7.4*max(len(str(x)) for x in [bas[j]]+[r[j] for r in sat])+22)) for j in range(n)]
    W=sum(gen)+4; assert W<=580,W; h=30; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,t in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+5,str(t),size=13,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,t in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+5,str(t),size=13,bold=(j==0)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    return G._svg(W,Hh,''.join(b))
# kromozom takımları (2n = 4: iki homolog çift, biri uzun biri kısa)
MIT4=[kr('D','L','k',-.4,.55,20),kr('D','L','g',.45,.6,-30),kr('D','S','k',-.45,-.5,70),kr('D','S','g',.5,-.45,0)]
MET4=[kr('D','L','k',0,.75),kr('D','L','g',0,.25),kr('D','S','k',0,-.25),kr('D','S','g',0,-.75)]
ANA4=[kr('T','L','k',-1.0,.5),kr('T','L','g',-.7,.5),kr('T','S','k',-1.0,-.5),kr('T','S','g',-.7,-.5),kr('T','L','k',1.0,.5),kr('T','L','g',.7,.5),kr('T','S','k',1.0,-.5),kr('T','S','g',.7,-.5)]
# ================= 01 · hücre döngüsü dairesi =================
SEKT=[('I',150,'G1'),('II',110,'S'),('III',70,'G2'),('IV',30,'M')]; assert sum(x[1] for x in SEKT)==360
def daire():
    o=[]; a0=90; r1,r2=1.05,1.95
    for i,(n,sp,_) in enumerate(SEKT):
        a1=a0-sp; c=math.radians
        fill='fill=vurgu!18,' if i%2==0 else ''
        o.append(f'\\path[draw,line width=.9pt,{fill}] ({r1*math.cos(c(a0)):.3f},{r1*math.sin(c(a0)):.3f}) -- ({r2*math.cos(c(a0)):.3f},{r2*math.sin(c(a0)):.3f}) arc[start angle={a0},end angle={a1},radius={r2}] -- ({r1*math.cos(c(a1)):.3f},{r1*math.sin(c(a1)):.3f}) arc[start angle={a1},end angle={a0},radius={r1}] -- cycle;')
        m=c((a0+a1)/2); o.append(f'\\node[font=\\large\\bfseries] at ({1.5*math.cos(m):.3f},{1.5*math.sin(m):.3f}) {{{n}}};')
        a0=a1
    o.append('\\draw[-{Stealth[length=2.6mm,width=2.2mm]},line width=1.1pt] (35:2.35) arc[start angle=35,end angle=-25,radius=2.35];')
    o.append('\\node[font=\\small,align=center] at (0,0) {Hücre\\\\döngüsü};')
    return tk('\n'.join(o),.95)
SK1=daire()
d1={'I':('II numaralı evrede DNA eşlenir ve DNA miktarı iki katına çıkar.',True,'S evresinde DNA eşlenir, bu evre II numaralıdır.','S evresi: DNA eşlenmesi'),
    'II':('IV numaralı evre, hücre döngüsünün en uzun evresidir.',False,'en uzun evre interfazdır; IV numaralı evre mitozdur ve en kısa evredir','Mitozun süresi'),
    'III':('I, II ve III numaralı evrelerde hücre bölünme geçirmez.',True,'G1, S ve G2 interfazı oluşturur; bölünme yalnız IV numaralı evrededir','İnterfaz evreleri')}
assert [x[2] for x in SEKT]==['G1','S','G2','M'] and max(x[1] for x in SEKT)==SEKT[0][1] and min(x[1] for x in SEKT)==SEKT[3][1]
o=onc(d1,True,harf=5)
Q('01','dongu','kolay','Hücre döngüsü','Hücre döngüsünün evrelerini ve her evrede olanları şemadan ilişkilendirir.','öncüllü',
  'Hücre döngüsünün evre sırası ve her evrenin işlevi şemadaki numaralarla eşleştirilir.','Mitozu hücre döngüsünün en uzun evresi sanmak.','Hücre döngüsü şemasına göre doğru ifadeler.',
  metin=oncm('Şekilde, bölünebilen bir hayvan hücresinin hücre döngüsü evreleri I, II, III ve IV ile gösterilmiştir. Oklar döngünün yönünü, I numaralı evre ise bir önceki bölünmenin hemen ardından başlayan evreyi göstermektedir.',d1,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',sekil=SK1,ad=o['ad'],
  ip=['Bölünmeden hemen sonra başlayan evreden başlayıp okların yönünde ilerleyerek her evrenin adını belirle.'],
  bilgi=[B('Hücre döngüsü','Hücre döngüsü interfaz (G1 → S → G2) ve mitoz (M) evrelerinden oluşur · G1: hücre büyür ve organel sayısı artar · S: DNA eşlenir · G2: hücre mitoza hazırlanır')],
  puf='Bölünmeden sonra sırayla G1, S, G2 ve mitoz gelir; DNA eşlenmesi her zaman S evresindedir.')
# ================= 02 · tablo: hücre sayısı =================
SUR={'G1':10,'S':6,'G2':3,'Mitoz':1}; TUR=sum(SUR.values()); ZAMAN=90; bol=ZAMAN//TUR; assert (TUR,bol,2**bol)==(20,4,16)
SK2=tabl(['Evre','Süre (saat)'],[[k,str(v)] for k,v in SUR.items()])
assert 2**(bol+1)==32 and 2**(ZAMAN//(TUR-SUR['S']))==64 and 2**(bol-1)==8
Q('02','hesap','orta','Hücre sayısı','Hücre döngüsü süresinden bölünme sayısını ve hücre sayısını hesaplar.','tablo',
  'Evre süreleri toplanıp döngü süresi bulunur; tam tamamlanan döngü sayısından hücre sayısı (2 üzeri bölünme sayısı) hesaplanır.','Bölünme sayısı ile hücre sayısını karıştırmak ya da tamamlanmamış bölünmeyi saymak.','Belirli sürede oluşan hücre sayısı.',
  metin='Bir hayvan hücresinin hücre döngüsünün evreleri ve her evrede geçen süre tabloda verilmiştir. Besin ortamına, G1 evresinin başındaki tek bir hücre bırakılmıştır. Oluşan her yavru hücre G1 evresinden başlayarak döngüsünü aynı sürelerle tamamlamakta, hiçbir hücre ölmemekte ve hücreler eş zamanlı bölünmektedir.\nBuna göre, ortama bırakılan hücreden 90 saat sonra ortamdaki hücre sayısı kaçtır?',
  dogru=16,yan=[(4,'Bölünme sayısını (4) hücre sayısı sanmak.','bilgi'),(8,'Dördüncü bölünmeyi saymayıp 2 üzeri 3 almak.','islem'),(32,'90 ÷ 20 = 4,5 değerini 5’e yuvarlayıp tamamlanmamış bölünmeyi saymak.','dikkat'),(64,'S evresini unutup 10 + 3 + 1 = 14 saat bulmak ve 90 ÷ 14 işleminden 6 bölünme saymak.','islem')],
  istenen='90 saat sonundaki hücre sayısı.',sekil=SK2,
  ad=[A('Döngü süresini bul','Bir tam döngü, tüm evrelerin süresinin toplamıdır.','10 + 6 + 3 + 1 = 20 saat'),A('Bölünme sayısını bul','Yalnız tamamlanan döngüler hücre sayısını artırır; yarım kalan bölünme sayılmaz.','90 ÷ 20 = 4,5 → 4 tam döngü'),A('Hücre sayısını hesapla','Her bölünmede hücre sayısı iki katına çıkar.','2 üzeri 4 = 16')],
  ip=['Bir hücrenin yeniden bölünebilmesi için tüm evrelerin tamamlanması gerekir.'],
  bilgi=[B('Bölünme ve hücre sayısı','Her mitoz bölünmede hücre sayısı iki katına çıkar · n bölünme sonunda 1 hücreden 2 üzeri n hücre oluşur')],
  puf='Önce döngü süresini toplayıp kaç tam döngü tamamlandığını bul; hücre sayısı 2’nin o kuvvetidir.')
# ================= 03 · mitoz evre sıralaması =================
def mit_sira():
    h=[('II','profaz'),('IV','metafaz'),('I','anafaz'),('III','telofaz')]
    return h
KAR={'I':'anafaz','II':'profaz','III':'telofaz','IV':'metafaz'}; SIRAM=[x for x in ['profaz','metafaz','anafaz','telofaz']]
dog3=' – '.join(next(k for k,v in KAR.items() if v==e) for e in SIRAM); assert dog3=='II – IV – I – III'
b=hucre(0,0,ANA4,'kutup',cent=True)+etiket(0,0,'I')+profaz(3.6,0,MIT4,et='II')+hayvan_tel(0,-3.3,cent=True)+etiket(0,-3.3,'III',1.05)+hucre(3.6,-3.3,MET4,'plak',cent=True)+etiket(3.6,-3.3,'IV')
SK3=tk(b,.9)
Q('03','mitoz','kolay','Mitoz evreleri','Mitoz bölünmenin evrelerini kromozom görünümüne göre sıralar.','şekilli',
  'Kromozomların dağılımına bakarak mitoz evreleri doğru sıraya dizilir.','Anafaz ile telofazı ya da profaz ile metafazı karıştırmak.','Mitoz evrelerinin gerçekleşme sırası.',
  metin='Şekilde, 2n = 4 kromozomlu bir hayvan hücresinin interfazı tamamlandıktan sonra geçirdiği mitoz bölünmenin evreleri karışık sırada gösterilmiştir.\nBuna göre, bu hücrelerin mitoz sırasında gerçekleşme sırası aşağıdakilerden hangisinde doğru verilmiştir?',
  dogru=dog3,yan=[('II – I – IV – III','Metafaz ile anafaz evrelerinin sırasını karıştırmak.','bilgi'),('IV – II – I – III','Profaz ile metafazı karıştırmak; kromozomlar önce belirginleşir, sonra ekvatora dizilir.','bilgi'),('II – IV – III – I','Telofazı anafazdan önce sanmak; kromatitler ayrıldıktan sonra çekirdekler oluşur.','bilgi'),('IV – I – II – III','Profazı metafazdan sonraya koymak; kromozomlar ancak profazda belirginleşir.','bilgi')],
  sira=[dog3,'II – I – IV – III','IV – II – I – III','II – IV – III – I','IV – I – II – III'],
  istenen='Evrelerin doğru sırası.',sekil=SK3,
  ad=[A('Hücreleri tanı','Çekirdek zarı belirsiz ve kromozomlar dağınıksa profaz; ekvatorda dizilmişse metafaz; her kutba tek kromatitli kromozomlar gidiyorsa anafaz; hücre boğumlanmış, çekirdekler oluşmuşsa telofazdır.','II: profaz · IV: metafaz · I: anafaz · III: telofaz'),A('Çekirdek ve iğ durumuna bak','Profazda kromozomlar kısalıp belirginleşir, metafazda ekvatora dizilir; bu iki evre kromatitlerin ayrılmasından önce gelir.','II ve IV: kromatitler ayrılmamış'),A('Evre sırasını yaz','Mitoz sırası profaz, metafaz, anafaz ve telofazdır.','II – IV – I – III')],
  ip=['Kromozomların hücredeki konumuna ve kromatitlerin ayrılıp ayrılmadığına bak.'],
  bilgi=[B('Mitozun evreleri','Profaz: kromozomlar belirginleşir · Metafaz: kromozomlar ekvatorda dizilir · Anafaz: kardeş kromatitler kutuplara çekilir · Telofaz: çekirdekler oluşur, hücre bölünür')],
  puf='Kromozom konumunu izle: dağınık, ekvatorda, kutuplara giden, iki çekirdek.')
# ================= 04 · sitokinez: hayvan–bitki =================
b=hayvan_tel(0,0,cent=True)+'\\node[font=\\normalsize\\bfseries] at (0,-1.45) {X};'+bitki_tel(4.6,0)+'\\node[font=\\normalsize\\bfseries] at (4.6,-1.45) {Y};'
SK4=tk(b,.95)
d4={'I':('X hücresinde sitoplazma, hücre zarının içe doğru boğumlanmasıyla ikiye ayrılır.',True,'hayvan hücrelerinde sitoplazma hücre zarının içe boğumlanmasıyla bölünür','Hayvan hücresi sitokinezi'),
    'II':('Y hücresinde ortada oluşan hücre plağından yeni hücre duvarı meydana gelir.',True,'bitki hücrelerinde ortada hücre plağı oluşur ve yeni hücre duvarının yapısına katılır','Bitki hücresi sitokinezi'),
    'III':('X ve Y hücrelerinde sitoplazma bölünmesi aynı mekanizmayla gerçekleşir.',False,'hayvan hücresinde boğumlanma, bitki hücresinde hücre plağı oluşumu görülür; mekanizmalar farklıdır','İki hücrenin karşılaştırması')}
o=onc(d4,False,harf=1)
Q('04','mitoz','orta','Sitokinez','Hayvan ve bitki hücrelerinde sitoplazma bölünmesinin farkını şekilden yorumlar.','öncüllü',
  'Telofaz sonunda sitoplazmanın bölünme biçimi hayvan ve bitkide farklıdır.','Her hücre tipinde sitokinezin boğumlanmayla olduğunu sanmak.','Yanlış ifadelerin belirlenmesi.',
  metin=oncm('Şekilde, mitoz bölünmenin son evresindeki iki hücre gösterilmiştir. X ve Y hücrelerinden biri hayvan, diğeri bitki hücresidir.',d4,'Buna göre, yukarıdaki ifadelerden hangileri yanlıştır?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Yanlış ifadelerin belirlenmesi.',sekil=SK4,ad=o['ad'],
  ip=['Hücre duvarının ve hücre zarının şekline bakarak hangi hücrenin hayvan, hangisinin bitki hücresi olduğunu belirle.'],
  bilgi=[B('Sitokinez','Sitokinez, çekirdek bölünmesinden sonra sitoplazmanın ikiye ayrılmasıdır; hayvan ve bitki hücrelerinde farklı biçimlerde gerçekleşir')],
  puf='Boğumlanma hayvan hücresinin, hücre plağı bitki hücresinin sitokinez işaretidir.')
# ================= 05 · mitozun önemi (olumsuz) =================
t5=[('Çok hücreli canlıların büyümesi ve gelişmesi için gerekli olan hücre sayısı artışını sağlar.',True,'mitozla hücre sayısı artar ve canlı büyür'),
    ('Yaralanan ya da yıpranan dokularda hücrelerin yenilenmesini sağlar.',True,'doku onarımı mitozla olur'),
    ('Tek hücreli bazı canlılarda eşeysiz üremeyi sağlar.',True,'amip gibi canlılar mitozla üreyebilir'),
    ('Yavru hücrelerin kromozom sayısını ana hücreyle aynı tutar.',True,'mitozda kromozom sayısı değişmez (2n → 2n)'),
    ('Her bölünmede ana hücreden farklı gen kombinasyonları oluşturarak kalıtsal çeşitliliği artırır.',False,'çeşitlilik mayozdaki krossing-over ve rastgele dağılımdan gelir; mitozda yavru hücreler ana hücreyle aynıdır')]
r=tek(t5,hedef=False,harf=1)
Q('05','mitoz','kolay','Mitozun önemi','Mitoz bölünmenin canlılar için önemini ve sınırlarını ayırt eder.','düz',
  'Mitoz büyüme, onarım ve eşeysiz üremeyi sağlar; kalıtsal çeşitlilik sağlamaz.','Mitozla kalıtsal çeşitlilik oluştuğunu sanmak.','Mitozla ilgili yanlış ifade.',
  metin='Bir öğrenci, mitoz bölünmenin canlılar için önemini anlatan bir poster hazırlamaktadır. Posterde mitozun sonuçlarıyla ilgili beş ifadeye yer vermiş, ancak bunlardan biri yanlış bilgi içermektedir.\nBuna göre, mitoz bölünmeyle ilgili aşağıdakilerden hangisi yanlıştır?',
  dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Mitozla ilgili yanlış ifade.',
  ad=[A('Mitozun sonuçlarını hatırla','Mitozda 2n kromozomlu ana hücreden 2n kromozomlu iki yavru hücre oluşur; yavru hücreler ana hücreyle aynı kalıtsal yapıdadır.','Ana hücre = yavru hücreler'),A('İfadeleri ele','Büyüme, onarım ve tek hücrelilerde üreme mitozla olur.','Dört ifade doğru'),A('Yanlışı bul','Gen kombinasyonu çeşitliliği mitozda oluşmaz; mutasyon dışında yavru hücreler ana hücreyle aynıdır.','Yanlış: çeşitliliği artırma ifadesi')],
  ip=['Yavru hücreler ana hücreyle karşılaştırıldığında kalıtsal yapının değişip değişmediğini düşün.'],
  bilgi=[B('Mitozun önemi','Büyüme · doku onarımı ve yenilenme · tek hücrelilerde üreme · kromozom sayısını ve kalıtsal yapıyı korur')],
  puf='Mitoz “aynısını kopyalar”: çeşitlilik gördüğün yerde mayoz ya da döllenme vardır.')
# ================= 06 · mitoz sayımı (kök ucu) =================
n2=14; metk=2*n2; yav=n2; assert metk+yav==42 and n2+yav==28 and metk+n2//2==35 and n2//2+yav==21 and metk+metk==56
Q('06','hesap','orta','Mitozda kromozom ve kromatit sayısı','Mitozun evrelerinde kromozom ve kromatit sayılarını hesaplar.','hikâyeli',
  'Metafazdaki kromatit sayısı kromozom sayısının iki katıdır; yavru hücre ana hücreyle aynı kromozom sayısındadır.','Kromozom sayısı ile kromatit sayısını karıştırmak; yavru hücrede sayının yarıya indiğini sanmak.','Kromatit ve kromozom sayılarının toplamı.',
  metin='Bir araştırmacı, 2n = 14 kromozomlu bir bitkinin kök ucu hücrelerinde mitoz bölünmeyi incelemektedir. Mikroskopta metafaz evresindeki bir hücreyi seçmiştir.\nBuna göre, bu hücredeki toplam kromatit sayısı ile mitoz bölünme tamamlandığında oluşan yavru hücrelerden birindeki kromozom sayısının toplamı kaçtır?',
  dogru=42,yan=[(21,'Yavru hücrede kromozom sayısının yarıya indiğini sanmak (14 + 7).','bilgi'),(28,'Metafazdaki kromatit sayısını kromozom sayısı (14) sanmak.','bilgi'),(35,'Yavru hücredeki kromozom sayısını yarıya indirmek (28 + 7).','bilgi'),(56,'Yavru hücredeki kromozomları da çift kromatitli sayarak 28 + 28 işlemi yapmak.','bilgi')],
  istenen='Kromatit ve kromozom sayısı toplamı.',
  ad=[A('Metafazdaki kromatit sayısı','DNA eşlenmiştir; her kromozom iki kardeş kromatitten oluşur.','14 × 2 = 28 kromatit'),A('Yavru hücredeki kromozom','Mitozda kromozom sayısı yarıya inmez; yavru hücreler 2n kromozomludur.','14 kromozom'),A('Toplamı bul','Kromatit sayısı ile yavru hücredeki kromozom sayısı toplanır.','28 + 14 = 42')],
  ip=['Metafazdaki her kromozomun kaç kromatitten oluştuğunu ve mitozda kromozom sayısının değişip değişmediğini düşün.'],
  bilgi=[B('Kromozom ve kromatit','DNA eşlendikten sonra her kromozom, sentromerle bağlı iki kardeş kromatitten oluşur · Mitozda yavru hücrelerin kromozom sayısı ana hücreyle aynıdır')],
  puf='Eşlenmiş kromozom = 2 kromatit; mitoz sonunda her yavru hücre ana hücreyle aynı sayıda kromozom alır.')
# ================= 07 · mitoz DNA grafiği =================
P7=[(0,2),(3,2),(5.5,4),(7.5,4),(9.4,4),(10,2),(12,2)]; SN7=[0,3,5.5,7.5,10,12]
def v7(x): return F(P7,x)
assert v7(1.5)==2 and v7(4)>2 and v7(4)<4 and v7(6.5)==4 and v7(8)==4 and v7(11)==2 and v7(7.5)==4 and v7(10)==2
SK7=tk(eksen(P7,[2,4],12,4.9,(SN7,['1','2','3','4','5']),w=7.0,h=4.4,ylab='DNA miktarı (birim)',xlab='Zaman'),1.05)
d7={'I':('1. aralıktaki hücrelerde DNA eşlenmesi tamamlanmıştır.',False,'DNA eşlenmesi 2. aralıkta (S evresi) gerçekleşir; 1. aralıkta DNA henüz eşlenmemiştir','1. aralık: G1'),
    'II':('2. aralıkta DNA miktarındaki artış, DNA eşlenmesinden kaynaklanır.',True,'S evresinde DNA eşlenir ve miktarı iki katına çıkar','2. aralık: S evresi'),
    'III':('4. aralığın sonunda hücre başına DNA miktarının azalması, sitoplazmanın bölünmesiyle gerçekleşir.',True,'mitoz sonunda hücre ikiye bölününce her yavru hücre DNA’nın yarısını alır','4. aralığın sonu')}
o=onc(d7,True,harf=4)
Q('07','grafik','orta','DNA miktarı grafiği','Mitoz döngüsünde hücre başına DNA miktarı grafiğini yorumlar.','grafik',
  'DNA miktarı S evresinde iki katına çıkar, mitoz sonunda hücre bölününce yarıya iner.','DNA eşlenmesinin hangi aralıkta olduğunu karıştırmak.','Grafiğe göre doğru ifadeler.',
  metin=oncm('Grafikte, bir hayvan hücresinin hücre döngüsü boyunca hücre başına DNA miktarının zamanla değişimi verilmiştir. Hücre, 1. aralığın başında önceki bölünmesini yeni tamamlamıştır ve 4. aralıkta mitoz bölünme geçirmektedir.',d7,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',sekil=SK7,ad=o['ad'],
  ip=['Grafikte DNA miktarının arttığı aralık ile azaldığı noktanın hücre döngüsünde hangi olaylara denk geldiğini düşün.'],
  bilgi=[B('DNA miktarı–zaman','Hücre başına DNA miktarı hücre döngüsünün evrelerine göre değişir; eşlenme ve bölünme bu değişimin nedenleridir')],
  puf='Grafikte artış = DNA eşlenmesi (S), düşüş = hücrenin bölünmesi.')
# ================= 08 · tablo: eşeysiz üreme eşleştirme =================
SAT8=[('Hidra','Tomurcuklanma',True),('Patates','Sporla üreme',False),('Planarya','Rejenerasyon',True),('Eğrelti otu','Sporla üreme',True),('Amip','İkiye bölünme',True)]
ROM=['I','II','III','IV','V']; yi=[i for i,x in enumerate(SAT8) if not x[2]]; assert yi==[1]; yi=yi[0]
SK8=tabl(['Satır','Canlı','Üreme biçimi'],[[r_,c,u] for r_,(c,u,_) in zip(ROM,SAT8)])
Q('08','esesiz','kolay','Eşeysiz üreme çeşitleri','Canlıların eşeysiz üreme biçimlerini doğru eşleştirir.','tablo',
  'Hidra tomurcuklanır, planarya rejenerasyonla çoğalabilir, eğrelti otu sporla, amip ikiye bölünmeyle, patates vejetatif (yumruyla) ürer.','Vejetatif üremeyi sporla üreme sanmak.','Yanlış eşleştirilmiş satır.',
  metin='Tabloda, bazı canlılar ile bu canlılarda görülen eşeysiz üreme biçimleri eşleştirilmiştir.\nBuna göre, numaralı satırlardan hangisindeki eşleştirme yanlıştır?',
  dogru=ROM[yi],yan=[(ROM[i],{'Hidra':'Hidranın vücudundan tomurcuk ayrılarak ürediğini bilmemek; bu eşleştirme doğrudur.','Planarya':'Planaryanın parçalarından yeni birey oluşturabildiğini (rejenerasyon) bilmemek; bu eşleştirme doğrudur.','Eğrelti otu':'Eğrelti otunun sporla ürediğini bilmemek; bu eşleştirme doğrudur.','Amip':'Amibin ikiye bölünerek ürediğini bilmemek; bu eşleştirme doğrudur.'}[c],'bilgi') for i,(c,u,_) in enumerate(SAT8) if i!=yi],
  sira=['I','II','III','IV','V'],istenen='Yanlış eşleştirilmiş satır.',sekil=SK8,
  ad=[A('Üreme biçimlerini hatırla','Hidra tomurcuklanır; planarya parçalarından yeni birey (rejenerasyon) oluşturur; eğrelti otu sporla; amip ikiye bölünerek ürer.','Hidra, planarya, eğrelti otu, amip: doğru'),A('Patatesi ele','Patates yumrusundaki gözlerden yeni bitki gelişir; bu vejetatif üremedir, sporla üreme değildir.','Patates satırı yanlış'),A('Sonucu yaz','Yanlış eşleştirme II numaralı satırdadır.','Cevap: II')],
  ip=['Her satırdaki canlının hangi yapısıyla ya da parçasıyla yeni birey oluşturduğunu düşün.'],
  bilgi=[B('Eşeysiz üreme türleri','İkiye bölünme (amip), tomurcuklanma (hidra, maya mantarı), sporla üreme (eğrelti otu, mantarlar), rejenerasyon (planarya), vejetatif üreme (bitkilerde kök, gövde ve yaprak parçalarıyla), partenogenez (döllenmemiş yumurtadan gelişme)')],
  puf='Bitkinin kök, gövde ya da yaprak parçasından yeni bitki oluşuyorsa üreme vejetatiftir.')
# ================= 09 · eşeysiz üreme özellikleri (olumsuz) =================
d9={'I':('Eşeysiz üremede tek bir ana canlı, yeni bireylerin oluşması için yeterlidir.',True,'eşeysiz üremede tek ebeveyn yeterlidir','Ebeveyn sayısı'),
    'II':('Eşeysiz üremeyle oluşan bireyler arasında mayoz ve krossing-over nedeniyle kalıtsal çeşitlilik yüksektir.',False,'eşeysiz üremede mayoz ve krossing-over görülmez; bireyler ana canlıyla aynı kalıtsal yapıdadır','Kalıtsal çeşitlilik'),
    'III':('Eşeysiz üremede döllenme gerçekleşmez.',True,'yeni birey gametlerin birleşmesiyle değil, vücut parçasının ya da hücrenin ayrılmasıyla oluşur','Döllenme')}
o=onc(d9,False,harf=1)
Q('09','esesiz','orta','Eşeysiz üremenin özellikleri','Eşeysiz üremenin kalıtsal sonuçlarını ve koşullarını değerlendirir.','öncüllü',
  'Eşeysiz üremede tek ebeveyn yeterlidir, döllenme yoktur ve yavrular ana canlıyla aynı kalıtsal yapıdadır.','Eşeysiz üremede de kalıtsal çeşitlilik oluştuğunu sanmak.','Eşeysiz üremeyle ilgili yanlış ifadeler.',
  metin=oncm('Bir araştırmacı, besin ortamında tomurcuklanarak çoğalan bir maya mantarı kültürü ile bahçede stolonlarla yayılan bir çilek bitkisini karşılaştırarak eşeysiz üreme hakkında notlar almıştır. Notlarında şu ifadelere yer vermiştir:',d9,'Buna göre, bu ifadelerden hangileri yanlıştır?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Yanlış ifadelerin belirlenmesi.',ad=o['ad'],
  ip=['Eşeysiz üremede yeni birey hangi tür hücrelerden ve kaç ebeveynden oluşur?'],
  bilgi=[B('Eşeysiz üreme','Eşeysiz üreme, gametlerin birleşmesi olmadan bir canlıdan yeni birey oluşmasıdır; çok hücrelilerde ve tek hücrelilerde farklı biçimleri vardır')],
  puf='Eşeysiz üremede “kopyalama” vardır: çeşitlilik yok, döllenme yok, tek ebeveyn yeterli.')
# ================= 10 · planarya rejenerasyon =================
d10={'I':('Bu olay, rejenerasyonla gerçekleşen bir eşeysiz üremedir.',True,'planaryada parçalardan yeni birey oluşumu rejenerasyondur','Olayın adı'),
     'II':('Parçaların yeni bireye dönüşürken hücre sayısı mitoz bölünmeyle artar.',True,'büyüme ve eksik kısımların tamamlanması mitozla olur','Hücre bölünmesi'),
     'III':('Oluşan üç birey, ana bireyden ve birbirinden kalıtsal olarak farklıdır.',False,'mitozla oluşan hücrelerin kalıtsal yapısı aynıdır; bireyler birbirinin kalıtsal kopyasıdır','Kalıtsal yapı')}
o=onc(d10,True,harf=2)
Q('10','esesiz','orta','Rejenerasyon','Rejenerasyonla üremenin mekanizmasını ve kalıtsal sonucunu yorumlar.','öncüllü',
  'Planarya parçalarının mitozla yeni bireye dönüşmesi rejenerasyondur; bireyler kalıtsal olarak aynıdır.','Rejenerasyonla oluşan bireylerde çeşitlilik beklemek.','Doğru ifadelerin belirlenmesi.',
  metin=oncm('Bir araştırmacı, bir planarya (yassı solucan) bireyini enine üç parçaya ayırıp besleyici bir ortamda bekletmiştir. Zamanla her parçanın eksik kısımlarını tamamlayarak ayrı bir bireye dönüştüğünü gözlemlemiştir.',d10,'Buna göre, bu gözlemle ilgili yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',ad=o['ad'],
  ip=['Parçaların kendini tamamlaması sırasında hangi tür hücre bölünmesinin görev yaptığını düşün.'],
  bilgi=[B('Rejenerasyon','Bazı canlılar (planarya, denizyıldızı) vücut parçalarından eksik kısımları tamamlayarak yeni birey oluşturabilir · Bu süreçte hücreler mitozla çoğalır')],
  puf='Parçadan yeni birey = mitoz; mitozla oluşan bireyler ana canlıyla aynı kalıtsal yapıdadır.')
# ================= 11 · amip hücre sayısı grafiği =================
PT=[(0,1),(40,2),(80,4),(120,8),(160,16)]; bol11=320//40; assert bol11==8 and 2**bol11==256 and 2**(bol11-1)==128 and 2**(bol11+1)==512 and bol11+1==9 and PT[-1][1]==16
assert all(PT[i+1][1]==2*PT[i][1] and PT[i+1][0]-PT[i][0]==40 for i in range(4))
g=['\\begin{axis}[width=6.8cm,height=5cm,xmin=0,xmax=175,ymin=0,ymax=18,xtick={0,40,80,120,160},ytick={2,4,8,16},axis lines=left,xlabel={Zaman (dakika)},ylabel={Amip sayısı},tick label style={font=\\small},label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
   '\\addplot[black,mark=*,mark size=2.2pt] coordinates {'+' '.join(f'({x},{y})' for x,y in PT)+'};','\\end{axis}']
SK11=tk('\n'.join(g),.9)
Q('11','esesiz','orta','İkiye bölünme','İkiye bölünmeyle üreyen bir populasyonun büyümesini grafikten yorumlar.','grafik',
  'Grafikten bölünme süresi bulunur; her bölünme süresinde amip sayısı iki katına çıkar.','Artışı doğrusal sanmak ya da grafikteki son değeri cevap almak.','Belirli bir andaki amip sayısı.',
  metin='Besin bakımından zengin bir ortama tek bir amip bırakılmış ve amiplerin sayısı zamana göre izlenerek grafikte gösterilmiştir. Amipler yalnız ikiye bölünmeyle üremektedir ve ortamda besin ile yer sınırlayıcı değildir. Ayrıca hiçbir amip ölmemekte ve bölünme süresi sabit kalmaktadır.\nBuna göre, 320. dakikada ortamdaki amip sayısı kaç olur?',
  dogru=256,yan=[(9,'Her bölünme süresinde yalnız bir amip eklendiğini sanmak (doğrusal artış).','bilgi'),(16,'Grafikteki son değeri (160. dakika) sorulan zamana ait sanmak.','dikkat'),(128,'8 bölünmeyi 7 saymak (ilk bölünmeyi atlamak).','islem'),(512,'0. dakikayı da bölünme sayarak 9 bölünme hesaplamak.','islem')],
  istenen='320. dakikadaki amip sayısı.',sekil=SK11,
  ad=[A('Bölünme süresini oku','Grafikte amip sayısı her 40 dakikada iki katına çıkıyor.','Bölünme süresi 40 dakika'),A('Bölünme sayısını bul','320 dakikada kaç kez bölünüleceğini hesapla.','320 ÷ 40 = 8 bölünme'),A('Amip sayısını hesapla','Her bölünmede sayı iki katına çıkar.','2 üzeri 8 = 256')],
  ip=['Grafikteki noktalar arasında sayının ve sürenin nasıl değiştiğine bak.'],
  bilgi=[B('İkiye bölünme','Amip, paramesyum gibi tek hücrelilerde hücre mitozla ikiye bölünür · n bölünme sonunda 1 hücreden 2 üzeri n hücre oluşur')],
  puf='Sayı her bölünme süresinde ikiye katlanır: önce süreyi, sonra bölünme sayısını bul.')
# ================= 12 · eşeysiz ve eşeyli üreme karşılaştırması (olumsuz) =================
d12={'I':('Eşeyli üremede yavru birey, iki ebeveynden gelen kalıtsal materyali taşır.',True,'zigot, sperm ve yumurtanın kalıtsal materyalini birleştirir','Eşeyli üremede yavru'),
     'II':('İnsanda gametler mitoz bölünmeyle oluşur ve kromozom sayısı bu sayede nesiller boyunca sabit kalır.',False,'insanda gametler mayozla oluşur; mayoz kromozom sayısını yarıya indirir, döllenme eski sayıyı geri getirir','Gamet oluşumu'),
     'III':('Eşeysiz üremede yeni birey, iki gametin birleşmesiyle oluşan zigottan gelişir.',False,'eşeysiz üremede döllenme ve zigot oluşumu yoktur','Eşeysiz üremede zigot')}
o=onc(d12,False,harf=5)
Q('12','karsilastir','orta','Eşeyli ve eşeysiz üreme','Eşeyli ve eşeysiz üremenin temel farklarını değerlendirir.','öncüllü',
  'Eşeyli üremede gametler mayozla oluşur ve döllenmeyle zigot meydana gelir; eşeysiz üremede ikisi de yoktur.','Gametlerin mitozla oluştuğunu sanmak; eşeysiz üremede de zigot oluştuğunu sanmak.','Yanlış ifadelerin belirlenmesi.',
  metin=oncm('Bir biyoloji öğretmeni, eşeyli ve eşeysiz üremeyi karşılaştıran bir etkinlikte öğrencilerden aşağıdaki ifadeleri değerlendirmelerini istemiştir:',d12,'Buna göre, bu ifadelerden hangileri yanlıştır?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Yanlış ifadelerin belirlenmesi.',ad=o['ad'],
  ip=['Gametlerin hangi bölünmeyle oluştuğunu ve eşeysiz üremede döllenme olup olmadığını düşün.'],
  bilgi=[B('Eşeyli üreme','Gametler mayozla oluşur (n) · sperm ile yumurtanın birleşmesiyle zigot (2n) meydana gelir · yavrular iki ebeveynden gelen genlerle çeşitlilik gösterir')],
  puf='Gamet = mayoz, zigot = döllenme; eşeysiz üremede ikisi de yoktur.')
# ================= 13 · mayoz I anafaz (2n = 6) =================
ANAI=[kr('D','L','k',-1.0,.75),kr('D','M','g',-1.0,0),kr('D','S','k',-1.0,-.75),kr('D','L','g',1.0,.75),kr('D','M','k',1.0,0),kr('D','S','g',1.0,-.75)]
assert len(ANAI)==6 and sum(2 for c in ANAI if c[3]<0)==6
SK13=tk(hucre(0,0,ANAI,'kutup',rx=1.9,ry=1.3,cent=True),1.0)
def kk(k,c): return f'{k} kromozom, {c} kromatit'
dog13=kk(3,6); assert (6//2,6//2*2)==(3,6)
Q('13','mayoz','kolay','Mayoz I','Mayoz I anafazındaki hücrenin bölünme sonundaki kromozom ve kromatit sayısını bulur.','şekilli',
  'Anafaz I’de homologlar ayrılır; her yavru hücre n kromozomlu ve çift kromatitlidir.','Tüm hücredeki sayıyı yavru hücreye yazmak; kromatitlerin mayoz I’de ayrıldığını sanmak.','Yavru hücredeki kromozom ve kromatit sayısı.',
  metin='Şekilde, 2n = 6 kromozomlu bir hayvanın üreme ana hücresi, mayoz bölünmenin bir evresinde gösterilmiştir. Hücre, gösterilen evreden sonra içinde bulunduğu bölünmeyi tamamlamaktadır.\nBuna göre, hücrenin bu bölünmesi tamamlandığında oluşan hücrelerin her birinde kaç kromozom ve kaç kromatit bulunur?',
  dogru=dog13,yan=[(kk(3,3),'Kardeş kromatitlerin mayoz I’de ayrıldığını sanmak; ayrılan homologlardır, kromatitler mayoz II’de ayrılır.','bilgi'),(kk(3,12),'Kromatit sayısını tüm hücredeki değerle (12) karıştırmak.','dikkat'),(kk(6,6),'Mayoz I’de kromozom sayısının yarıya indiğini atlayıp kromatit sayısını kromozom sayısına eşitlemek.','bilgi'),(kk(6,12),'Tüm hücredeki değerleri her yavru hücre için yazmak; mayoz I’de homologlar ayrılır, sayı yarıya iner.','dikkat')],
  sira=[kk(3,3),dog13,kk(3,12),kk(6,6),kk(6,12)],istenen='Yavru hücrelerdeki kromozom ve kromatit sayısı.',sekil=SK13,
  ad=[A('Evreyi belirle','Kromozomlar çift kromatitli ve homolog çiftlerin üyeleri zıt kutuplara gitmektedir; bu mayoz I’in anafazıdır.','Her kutupta 3 kromozom'),A('Bölünme sonunu yaz','Mayoz I sonunda her hücre n kromozomlu olur; kromozomlar hâlâ çift kromatitlidir.','3 kromozom'),A('Kromatit sayısını bul','Her kromozom iki kromatitten oluşur.','3 × 2 = 6 kromatit')],
  ip=['Anafazda ayrılan yapıların kardeş kromatitler mi, homolog kromozomlar mı olduğuna ve ayrılan yapıların nasıl göründüğüne bak.'],
  bilgi=[B('Mayoz I','Anafaz I’de homolog kromozomlar kutuplara ayrılır · mayoz I sonunda hücreler n kromozomludur, kromozomlar çift kromatitlidir (kardeş kromatitler mayoz II’de ayrılır)')],
  puf='Mayoz I homologları, mayoz II kardeş kromatitleri ayırır.')
# ================= 14 · krossing-over şekli =================
def tetrat():
    o=[]; xs=[-1.15,-.65,.65,1.15]
    # alt kısım (y -2 .. .9): kromatitler; üst kısım (1.3 .. 2.2) çaprazlama sonrası yer değiştirmiş
    o.append(f'\\draw[line width=2.2pt] ({xs[0]},-2) -- ({xs[0]},2.2);\\draw[vurgu,line width=2.2pt] ({xs[3]},-2) -- ({xs[3]},2.2);')
    o.append(f'\\draw[line width=2.2pt] ({xs[1]},-2) -- ({xs[1]},.9) -- ({xs[2]},1.3) -- ({xs[2]},2.2);')
    o.append(f'\\draw[vurgu,line width=2.2pt] ({xs[2]},-2) -- ({xs[2]},.9) -- ({xs[1]},1.3) -- ({xs[1]},2.2);')
    o.append(f'\\fill (-.9,0) circle (.14);\\fill (.9,0) circle (.14);')
    return '\n'.join(o)
SK14=tk(tetrat(),1.1)
d14={'I':('Krossing-over, homolog kromozomların kardeş olmayan kromatitleri arasında gerçekleşmiştir.',True,'şekilde yer değiştiren parçalar farklı kromozomlara ait iç kromatitlerdir','Çaprazlamanın yeri'),
     'II':('Bu olay, mayoz I’in profazında gerçekleşir.',True,'homologlar eşleşip tetrat oluşturduğunda krossing-over mayoz I profazında olur','Olayın evresi'),
     'III':('Mayoz sonunda oluşan dört hücrenin kromozomlarının tümü, ana hücredeki homologlarla birebir aynıdır.',False,'iç kromatitler parça değiştirdiği için bu kromatitlerden oluşan kromozomlar yeni gen birleşimleri taşır','Oluşan hücrelerin kromozomları')}
o=onc(d14,True,harf=4)
Q('14','mayoz','orta','Krossing-over','Krossing-over olayını şekilden tanır ve sonuçlarını yorumlar.','öncüllü',
  'Krossing-over homolog kromozomların kardeş olmayan kromatitleri arasında parça değişimidir ve yeni gen birleşimleri oluşturur.','Parça değişiminin kardeş kromatitler arasında olduğunu sanmak.','Doğru ifadelerin belirlenmesi.',
  metin=oncm('Şekilde, mayoz bölünme geçiren bir hücredeki bir homolog kromozom çifti, her kromozomu iki kromatitli olarak gösterilmiştir. Siyah ve yeşil renkler kromozomların hangi ebeveynden geldiğini belirtmektedir.',d14,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',sekil=SK14,ad=o['ad'],
  ip=['Renklerin değiştiği noktada hangi kromatitlerin birbirine dolandığına bak.'],
  bilgi=[B('Krossing-over','Mayoz I profazında homolog kromozomlar eşleşir (tetrat) · kardeş olmayan kromatitler arasında parça değişimi olur · sonuçta yeni gen birleşimleri ve kalıtsal çeşitlilik oluşur')],
  puf='Parça değişimi yalnız homologlar arasında ve mayoz I profazında olur.')
# ================= 15 · mayoz II (olumsuz) =================
t15=[('Mayoz II’nin başlangıcında hücrelerdeki kromozom sayısı n’dir.',True,'mayoz I sonunda kromozom sayısı yarıya inmiştir'),
     ('Mayoz II’den önce DNA eşlenmesi gerçekleşmez.',True,'DNA yalnız mayoz I öncesindeki interfazda bir kez eşlenir'),
     ('Mayoz II’nin anafazında kardeş kromatitler birbirinden ayrılır.',True,'mayoz II, kardeş kromatitlerin ayrılmasıyla gerçekleşen mitoza benzer bir bölünmedir'),
     ('Mayoz II sonunda oluşan hücrelerin DNA miktarı, mayoz II’nin başlangıcındaki hücrelerin yarısı kadardır.',True,'kromatitler ayrılınca hücre başına DNA miktarı yarıya iner'),
     ('Mayoz II’nin anafazında homolog kromozomlar birbirinden ayrılır.',False,'homologlar mayoz I’de ayrılmıştır; mayoz II’de ayrılan yapılar kardeş kromatitlerdir')]
r=tek(t15,hedef=False,harf=1)
Q('15','mayoz','orta','Mayoz II','Mayoz II’de gerçekleşen olayları mayoz I ile ayırt eder.','düz',
  'Mayoz II’de DNA eşlenmez; kardeş kromatitler ayrılır, homologlar değil.','Homologların mayoz II’de ayrıldığını sanmak.','Mayoz II ile ilgili yanlış ifade.',
  metin='Kromozom sayısı 2n = 8 olan bir hayvanın testisindeki sperm ana hücrelerinden biri mayoz bölünme geçirmektedir. Bu hücrenin mayoz I’i tamamlayarak oluşturduğu hücrelerde mayoz II evresi başlamıştır.\nBuna göre, mayoz II ile ilgili aşağıdakilerden hangisi yanlıştır?',
  dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Mayoz II ile ilgili yanlış ifade.',
  ad=[A('Mayoz I sonucunu hatırla','Mayoz I’de homolog kromozomlar ayrılmış, hücreler n kromozomlu ve çift kromatitli olmuştur.','2n = 8 → n = 4'),A('Mayoz II’yi tanımla','DNA yeniden eşlenmeden, kardeş kromatitler ayrılır ve hücre başına DNA yarıya iner.','Mayoz II ≈ mitoza benzer'),A('İfadeleri ele','Homologların ayrılması mayoz I’e aittir; mayoz II için yanlıştır.','Yanlış: homologların ayrılması')],
  ip=['Homologların ve kardeş kromatitlerin hangi bölünmede ayrıldığını ayrı ayrı düşün.'],
  bilgi=[B('Mayoz I ve II','Mayoz I: homolog kromozomlar ayrılır, kromozom sayısı yarıya iner · Mayoz II: DNA eşlenmeden kardeş kromatitler ayrılır, kromozom sayısı n olarak kalır')],
  puf='Mayoz II’yi “mitoz gibi” düşün: kardeş kromatitler ayrılır, kromozom sayısı değişmez.')
# ================= 16 · mayozun önemi =================
d16={'I':('Mayoz I’de homolog kromozom çiftlerinin kutuplara rastgele dağılması.',True,'her çiftin hangi üyesinin hangi kutba gideceği tesadüfidir ve gamet çeşidini artırır','Rastgele dağılım'),
     'II':('Mayoz I’in profazında homolog kromozomlar arasında krossing-over gerçekleşmesi.',True,'parça değişimi yeni gen birleşimleri oluşturur','Krossing-over'),
     'III':('Döllenmede sperm ve yumurtanın rastgele birleşmesi.',True,'hangi spermin hangi yumurtayla birleşeceği tesadüfidir ve zigot çeşidini artırır','Rastgele döllenme')}
o=onc(d16,True,harf=5)
Q('16','mayoz','kolay','Mayozun önemi','Eşeyli üremede kalıtsal çeşitliliği artıran olayları belirler.','öncüllü',
  'Rastgele dağılım, krossing-over ve rastgele döllenme kalıtsal çeşitliliği artırır.','Çeşitliliğin yalnız krossing-over’dan kaynaklandığını sanmak.','Çeşitliliğe katkı sağlayan olaylar.',
  metin=oncm('Aynı ebeveynlerin çocukları ya da aynı türden bireyler arasında kalıtsal özellikler bakımından büyük çeşitlilik görülür. Bu çeşitliliğin oluşumuyla ilgili olarak,',d16,'olaylarından hangileri, eşeyli üreyen canlılarda kalıtsal çeşitliliğin artmasına katkı sağlar?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Kalıtsal çeşitliliğe katkı sağlayan olaylar.',ad=o['ad'],
  ip=['Gamet oluşumu sırasında ve gametler birleşirken hangi olayların tesadüfe bağlı olduğunu düşün.'],
  bilgi=[B('Kalıtsal çeşitlilik','Mayoz sırasında krossing-over ve homologların rastgele dağılımı, ardından döllenmede gametlerin rastgele birleşmesi kalıtsal çeşitliliği artırır')],
  puf='Çeşitliliğin üç kaynağı: krossing-over, homologların rastgele dağılımı, rastgele döllenme.')
# ================= 17 · gamet olasılığı =================
assert Fr(1,2)**4==Fr(1,16) and 2*Fr(1,2)**4==Fr(1,8) and Fr(1,2)**8==Fr(1,256) and Fr(1,2)**2*2==Fr(1,2)
Q('17','hesap','zor','Gamet çeşitliliği ve olasılık','Homolog çiftlerinin gametlere rastgele dağılımından iki durumlu olasılık hesaplar.','yeni nesil',
  'Her homolog çiftinde anneden ya da babadan gelen üye gamete 1/2 olasılıkla geçer; çiftler bağımsızdır ve iki ayrı durum toplanır.','Yalnız bir durumu hesaplayıp diğerini atlamak; kromozom sayısı ile çift sayısını karıştırmak.','Gametin tüm kromozomlarının aynı ebeveynden gelme olasılığı.',
  metin='2n = 8 kromozomlu bir hayvanın her homolog çiftinde, kromozomlardan biri anneden, diğeri babadan gelmiştir. Bu hayvan, krossing-over olmadan mayoz bölünmeyle gamet oluşturmaktadır. Her homolog çiftinin üyelerinin gametlere dağılması birbirinden bağımsız ve eşit olasılıklıdır.\nBuna göre, bu hayvanın oluşturduğu bir gametteki tüm kromozomların aynı ebeveynden (ya hepsi anneden ya da hepsi babadan) gelmiş olma olasılığı kaçtır?',
  dogru='1/8',yan=[('1/256','8 kromozomun her birini bağımsız sayıp (1/2) üzeri 8 hesaplamak; oysa dağılım homolog çiftleri üzerinden yapılır.','islem'),('1/16','Yalnız hepsinin anneden gelme durumunu hesaplayıp babadan gelme durumunu atlamak.','dikkat'),('1/4','Homolog çifti sayısını 2 sanmak.','bilgi'),('1/2','Yalnız tek bir homolog çiftinin olasılığını almak.','dikkat')],
  sira=['1/256','1/16','1/8','1/4','1/2'],istenen='Tüm kromozomların aynı ebeveynden gelme olasılığı.',
  ad=[A('Homolog çifti sayısını bul','Her çiftin bir üyesi gamete gider; çift sayısı 2n’nin yarısıdır.','2n = 8 → 4 çift'),A('Bir durumun olasılığı','Hepsinin anneden gelmesi için her çiftte anne üyesi seçilmelidir; çiftler bağımsızdır.','(1/2) üzeri 4 = 1/16'),A('Diğer durumu ekle','Hepsinin babadan gelmesi de aynı olasılığa sahiptir ve ayrı bir durumdur.','1/16 + 1/16'),A('Sonucu yaz','İki ayrı durumun olasılıkları toplanır.','2/16 = 1/8')],
  ip=['Gamete her homolog çiftinden kaç üyenin geçtiğini ve “aynı ebeveynden” koşulunun kaç ayrı durumu kapsadığını düşün.'],
  bilgi=[B('Gametlere dağılım','Mayoz I’de her homolog çiftinin üyeleri kutuplara bağımsız ve rastgele dağılır · Bağımsız olayların olasılıkları çarpılır, birbirini dışlayan durumların olasılıkları toplanır')],
  puf='Olasılık = durum sayısı × (1/2) üzeri homolog çifti sayısı.')
# ================= 18 · tablo: mayozda kromozom/kromatit/DNA =================
X18,Y18,Z18=4,8,6; assert (8//2,(8//2)*2,12//2)==(X18,Y18,Z18) and 4*1==4 and 12//4==3
SK18=tabl(['Hücre / evre','Kromozom','Kromatit','DNA (birim)'],[['Mayoz I metafaz','8','16','12'],['Mayoz I sonu (bir hücre)','X','Y','Z'],['Mayoz II sonu (bir hücre)','4','4','3']])
def xyz(a,b,c): return f'{a} – {b} – {c}'
dog18=xyz(4,8,6)
Q('18','mayoz','orta','Mayozda kromozom, kromatit ve DNA','Mayoz evrelerinde kromozom, kromatit ve DNA miktarının birlikte değişimini yorumlar.','tablo',
  'Mayoz I sonunda kromozom sayısı ve DNA yarıya iner ama kromozomlar çift kromatitli kalır.','Mayoz I sonunda kromatitlerin de ayrıldığını sanmak.','Tablodaki X, Y ve Z değerleri.',
  metin='Tabloda, 2n = 8 kromozomlu bir hayvanın mayoz bölünme geçiren bir hücresinin bazı evrelerindeki kromozom, kromatit ve DNA miktarı (birim) değerleri verilmiştir. DNA miktarı hücre başına verilmiştir.\nBuna göre, tablodaki X, Y ve Z değerleri sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
  dogru=dog18,yan=[(xyz(4,4,3),'Mayoz I sonunda kardeş kromatitlerin de ayrıldığını sanmak; oysa kromatitler mayoz II’de ayrılır.','bilgi'),(xyz(4,8,12),'DNA miktarının mayoz I sonunda yarıya indiğini unutmak.','bilgi'),(xyz(8,8,6),'Mayoz I’de kromozom sayısının yarıya indiğini atlayıp kromatit sayısını kromozom sayısına eşitlemek.','bilgi'),(xyz(8,16,12),'Metafaz I değerlerini mayoz I sonundaki hücreye de yazmak.','dikkat')],
  sira=[xyz(4,4,3),dog18,xyz(4,8,12),xyz(8,8,6),xyz(8,16,12)],istenen='X, Y ve Z değerleri.',sekil=SK18,
  ad=[A('Mayoz I’in sonucunu belirle','Homolog kromozomlar ayrılır; her hücrede kromozom sayısı yarıya iner.','X = 8 ÷ 2 = 4'),A('Kromatit sayısını bul','Mayoz I sonunda kromozomlar çift kromatitlidir; kromatit sayısı kromozom sayısının iki katıdır.','Y = 4 × 2 = 8'),A('DNA miktarını bul','Hücre başına DNA miktarı mayoz I sonunda yarıya iner.','Z = 12 ÷ 2 = 6'),A('Tutarlılığı sına','Mayoz II sonunda DNA bir daha yarıya iner: 6 → 3, tablodaki değerle uyumludur.','Doğru: X = 4, Y = 8, Z = 6')],
  ip=['Mayoz I’de ve mayoz II’de hangi yapıların ayrıldığını ve DNA miktarının bu ayrılmalarda nasıl değiştiğini düşün.'],
  bilgi=[B('Mayozda sayılar','Mayoz I sonunda kromozom sayısı ve hücre başına DNA yarıya iner, kromozomlar çift kromatitli kalır · Mayoz II sonunda kromatitler ayrıldığı için hücre başına DNA bir daha yarıya iner')],
  puf='Mayoz I kromozom sayısını, mayoz II kromatit sayısını yarıya indirir; DNA her iki ayrılmada da yarıya iner.')
# ================= 19 · tablo: mitoz–mayoz (olumsuz) =================
SAT19=[('Oluşan hücre sayısı','2','4',True),('Yavru hücre kromozomu','2n','n',True),('Krossing-over','Görülür','Görülmez',False),('Görüldüğü hücreler','Vücut hücreleri','Üreme ana hücreleri',True),('Bölünme sayısı','1','2',True)]
YS19=2  # yanlış satır (0 tabanlı): III
SAT19=[x for x in SAT19 if x[3]]+[x for x in SAT19 if not x[3]]
SAT19.insert(YS19,SAT19.pop()); assert [i for i,x in enumerate(SAT19) if not x[3]]==[YS19]
SK19=tabl(['Satır','Özellik','Mitoz','Mayoz'],[[r,a,b,c] for r,(a,b,c,_) in zip(['I','II','III','IV','V'],SAT19)])
dog19='III'; ROM19=['I','II','III','IV','V']
Q('19','karsilastir','kolay','Mitoz ve mayoz karşılaştırması','Mitoz ve mayozun temel özelliklerini tablo üzerinde karşılaştırır.','tablo',
  'Krossing-over yalnız mayozda görülür; hücre sayısı, kromozom sayısı ve bölünme sayısı iki bölünmeyi ayırır.','Krossing-over’ın mitozda da görüldüğünü sanmak.','Yanlış bilgi içeren satır.',
  metin='Tabloda, 2n kromozomlu bir hayvanda görülen mitoz ve mayoz bölünmenin bazı özellikleri karşılaştırılmıştır. Satırlardan birinde mitoz ve mayoz sütunlarındaki bilgiler yanlış yazılmıştır.\nBuna göre, numaralı satırlardan hangisindeki bilgi yanlıştır?',
  dogru=dog19,yan=[(r_,f'“{a_}” satırındaki bilginin doğru olduğunu bilmemek; bu satır doğrudur.','bilgi') for r_,(a_,_,_,ok_) in zip(ROM19,SAT19) if ok_],
  sira=['I','II','III','IV','V'],istenen='Yanlış bilgi içeren satır.',sekil=SK19,
  ad=[A('Mitozu hatırla','Mitozda tek bölünmeyle 2 yavru hücre oluşur; kromozom sayısı 2n kalır; vücut hücrelerinde görülür.','Mitoz: 1 bölünme, 2 hücre, 2n'),A('Mayozu hatırla','Mayozda iki bölünmeyle 4 hücre oluşur; kromozom sayısı n’ye iner; üreme ana hücrelerinde görülür. Krossing-over yalnız mayozda olur.','Mayoz: 2 bölünme, 4 hücre, n, krossing-over var'),A('Satırları karşılaştır','Krossing-over satırında sütunlar ters yazılmıştır; diğer satırlar doğrudur.','III yanlış')],
  ip=['Satırları tek tek mitoz ve mayoz bilgilerine göre sına.'],
  bilgi=[B('Mitoz–mayoz','Mitoz ve mayoz, farklı hücre türlerinde gerçekleşir ve farklı sayıda hücre ile farklı kromozom sayıları oluşturur')],
  puf='Krossing-over yalnız mayoza özgüdür; “eşleşen homologlar” görürsen mayoz de.')
# ================= 20 · iki grafik: hangisi mayoz =================
P20a=[(0,2),(2,2),(4,4),(8,4),(8.6,2),(10.4,2),(11,1),(12.4,1)]   # I: mayoz
P20b=[(0,2),(2,2),(4,4),(8,4),(8.6,2),(12.4,2)]                    # II: mitoz
assert F(P20a,12)==1 and F(P20b,12)==2 and F(P20a,1)==F(P20b,1)==2 and F(P20a,6)==F(P20b,6)==4
g20=[eksen(P20a,[1,2,4],12.4,4.8,w=5.0,h=4.0,ylab='DNA miktarı',xlab='Zaman',at='0,0',title='I'),eksen(P20b,[1,2,4],12.4,4.8,w=5.0,h=4.0,ylab='DNA miktarı',xlab='Zaman',at='6.4cm,0',title='II')]
SK20=tk('\n'.join(g20),1.0)
t20=[('I numaralı grafik mayoza aittir; çünkü DNA miktarı eşlenmeden sonra iki kez yarıya inmiştir.',True,'mayozda iki ardışık bölünme vardır ve DNA miktarı eşlenmeden sonra iki kez yarıya iner'),
     ('II numaralı grafik mayoza aittir; çünkü bölünme sonunda DNA miktarı, eşlenme öncesinin yarısına inmiştir.',False,'II numaralı grafikte bölünme sonunda DNA miktarı eşlenme öncesindeki değerine (2 birim) döner; bu mitozun işaretidir'),
     ('I numaralı grafik mitoza aittir; çünkü DNA miktarı yalnız bir kez iki katına çıkmıştır.',False,'DNA miktarı her iki bölünmede de yalnız bir kez (S evresinde) iki katına çıkar; ayırt edici olan yarıya inme sayısıdır'),
     ('Her iki grafikte de bölünme sonunda hücrelerdeki DNA miktarı, G1 evresindeki DNA miktarına eşittir.',False,'yalnız mitozda sonuç G1’deki değere eşittir; mayozda hücreler G1’deki hücrenin yarısı kadar DNA içerir'),
     ('II numaralı grafikteki DNA azalması, homolog kromozomların birbirinden ayrılmasıyla gerçekleşmiştir.',False,'mitozda homologlar eşleşmez; DNA miktarındaki azalma sitoplazmanın bölünmesiyle olur ve kardeş kromatitler ayrılmıştır')]
r=tek(t20,hedef=True,harf=1)
Q('20','grafik','kolay','Mitoz ve mayoz grafikleri','İki bölünmenin DNA miktarı grafiklerini yarıya inme sayısına göre ayırt eder.','grafik',
  'Mayozda DNA eşlenmeden sonra iki kez, mitozda bir kez yarıya iner.','Her iki bölünmede de DNA’nın G1 düzeyine döndüğünü sanmak.','Grafiklerle ilgili doğru ifade.',
  metin='I ve II numaralı grafiklerden biri mitoz, diğeri mayoz bölünme geçiren bir hayvan hücresinin hücre başına DNA miktarındaki değişimini göstermektedir. Her iki hücrenin G1 evresindeki DNA miktarı eşittir ve DNA, yalnız S evresinde eşlenmektedir.\nBuna göre, bu grafiklerle ilgili aşağıdakilerden hangisi doğrudur?',
  dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Grafiklerle ilgili doğru ifade.',sekil=SK20,
  ad=[A('Grafikleri oku','Her iki grafikte DNA miktarı S evresinde 2 birimden 4 birime çıkıyor. I numaralıda 4 → 2 → 1, II numaralıda 4 → 2 düşüşü var.','I: iki yarılanma · II: bir yarılanma'),A('Bölünme türünü belirle','İki ardışık bölünme (iki yarılanma) mayoza, tek bölünme mitoza aittir.','I mayoz, II mitoz'),A('İfadeleri ele','Mayozda hücrelerin DNA miktarı G1’dekinin yarısına inerken mitozda G1 düzeyine döner. Doğru ifade I’i mayoz sayandır.','Doğru: I mayoza aittir')],
  ip=['Eşlenmeden sonra DNA miktarının kaç kez yarıya indiğini her grafikte say.'],
  bilgi=[B('DNA grafikleri','S evresinde DNA iki katına çıkar; hücre bölünmeleri hücre başına DNA miktarını azaltır')],
  puf='Eşlenmeden sonra bir düşüş varsa mitoz, iki düşüş varsa mayoz.')
# ================= 21 · eşeyli üreme (insan) =================
d21={'I':('İnsanda gametler, mayoz bölünmeyle oluşur.',True,'gametler mayozla n kromozomlu olarak oluşur','Gamet oluşumu'),
     'II':('Gametlerin kromozom sayısı, vücut hücrelerinin kromozom sayısıyla aynıdır.',False,'gametler n kromozomludur, vücut hücreleri 2n’dir; insanda gametlerde 23, vücut hücrelerinde 46 kromozom bulunur','Kromozom sayıları'),
     'III':('Zigot, sperm ile yumurtanın birleşmesiyle oluşur.',True,'döllenmede sperm ve yumurta birleşerek 2n kromozomlu zigotu oluşturur','Zigot')}
o=onc(d21,True,harf=4)
Q('21','karsilastir','kolay','Eşeyli üreme ve döllenme','Gamet oluşumu, döllenme ve zigotla ilgili ifadeleri değerlendirir.','öncüllü',
  'Gametler mayozla n kromozomlu oluşur; döllenmeyle 2n kromozomlu zigot meydana gelir.','Gametlerin de vücut hücreleri gibi 2n kromozomlu olduğunu sanmak.','Doğru ifadelerin belirlenmesi.',
  metin=oncm('İnsanda eşeyli üremeyle ilgili bir ders notunda,',d21,'ifadelerine yer verilmiştir. Buna göre, bu ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',ad=o['ad'],
  ip=['İnsanda vücut hücreleri 46 kromozomlu iken gametlerin kaç kromozomlu olması gerektiğini düşün.'],
  bilgi=[B('Eşeyli üreme','Gametler mayozla n kromozomlu oluşur · Döllenmede iki gamet birleşir ve 2n kromozomlu zigot meydana gelir · Böylece tür kromozom sayısını korur')],
  puf='Mayoz sayıyı yarıya indirir, döllenme eski sayıyı geri getirir.')
# ================= 22 · gamet ve kutup hücresi sayısı (ters hesap) =================
sp=20*4; yum=(140-sp)//1; kut=yum*3; assert (yum,kut)==(60,180) and sp+yum==140 and 140*3==420 and yum*2==120 and yum*4==240
Q('22','hesap','zor','Gamet sayısı','Toplam gamet sayısından yumurta ana hücresi sayısını bulup kutup hücresi sayısını hesaplar.','hikâyeli',
  'Sperm ana hücresi 4 sperm, yumurta ana hücresi 1 yumurta ve 3 kutup hücresi verir; toplam gametten yumurta sayısı, ondan da kutup hücresi sayısı bulunur.','Yumurta ana hücresi sayısını bulmadan kutup hücrelerini hesaplamak; kutup hücresi sayısını yanlış almak.','Gamet olmayan hücre sayısı.',
  metin='Bir hayvanın testislerinde 20 sperm ana hücresi, yumurtalıklarında ise bir miktar yumurta ana hücresi mayoz bölünme geçirmektedir. Tüm bölünmeler eksiksiz tamamlanmış ve bu bölünmeler sonunda toplam 140 gamet (sperm ve yumurta) oluşmuştur. Yumurta oluşumu sırasında oluşan kutup hücreleri gamet sayılmamaktadır.\nBuna göre, bu bölünmeler sonunda oluşan, gamet olmayan hücre sayısı kaçtır?',
  dogru=180,yan=[(60,'Gamet olmayan hücre sayısını yumurta ana hücresi sayısı sanmak.','dikkat'),(120,'Her yumurta ana hücresinden 2 kutup hücresi oluştuğunu sanmak.','bilgi'),(240,'Her yumurta ana hücresinden 4 hücre atıldığını sanmak.','bilgi'),(420,'Toplam gamet sayısını 3 ile çarpmak.','islem')],
  istenen='Gamet olmayan hücre sayısı.',
  ad=[A('Sperm sayısını bul','Her sperm ana hücresi mayozla 4 sperm oluşturur.','20 × 4 = 80 sperm'),A('Yumurta sayısını bul','Toplam gametten sperm sayısı çıkarılır; her yumurta ana hücresi 1 yumurta verir.','140 − 80 = 60 yumurta = 60 yumurta ana hücresi'),A('Kutup hücrelerini hesapla','Her yumurta ana hücresi ayrıca 3 kutup hücresi oluşturur.','60 × 3 = 180')],
  ip=['Önce spermlerin sayısını, sonra toplam gametten yola çıkarak yumurta ana hücresi sayısını bul.'],
  bilgi=[B('Gamet oluşumu','Sperm ana hücresi ve yumurta ana hücresi mayoz sonunda farklı sayıda hücre oluşturur; bunların hepsi gamet değildir')],
  puf='Yumurta ana hücresinden 1 gamet ve 3 kutup hücresi oluşur; önce gamet sayısından yumurta ana hücresini bul.')
# ================= 23 · mayoz DNA grafiği (aralıklar) =================
P23=[(0,8),(3,8),(5,16),(8.2,16),(8.6,8),(11.6,8),(12,4),(14,4)]; SN23=[0,3,5,8.6,12,14]
assert F(P23,1)==8 and F(P23,4)==12 and F(P23,6)==16 and F(P23,10)==8 and F(P23,13)==4
SK23=tk(eksen(P23,[4,8,16],14,19.5,(SN23,['1','2','3','4','5']),w=7.2,h=4.6,ylab='DNA miktarı (birim)',xlab='Zaman'),1.05)
d23={'I':('2. aralıkta DNA miktarındaki artışa paralel olarak hücredeki kromozom sayısı da iki katına çıkar.',False,'S evresinde DNA eşlenir ama kromozom sayısı değişmez; eşlenen kromatitler sentromerle bağlı kalır','2. aralık: DNA eşlenmesi'),
     'II':('4. aralıkta kardeş kromatitlerin birbirinden ayrıldığı bir evre bulunur.',True,'mayoz II’de kardeş kromatitler ayrılır ve hücre başına DNA yarıya iner','4. aralık: mayoz II'),
     'III':('5. aralıktaki hücrelerde DNA miktarı, 1. aralıktaki hücrelerin yarısı kadardır.',True,'mayoz sonunda hücreler G1’deki hücrenin DNA miktarının yarısına sahiptir (8 → 4)','5. aralık: DNA miktarı')}
o=onc(d23,True,harf=4)
Q('23','grafik','zor','Mayozda DNA miktarı','Mayoz sürecinde hücre başına DNA miktarı grafiğini kromozom ve kromatit olaylarıyla ilişkilendirir.','grafik',
  'DNA miktarı S evresinde artar, mayoz I ve II sonunda ikişer kez yarıya iner; kromozom sayısı yalnız mayoz I’de yarıya iner.','DNA miktarındaki değişimi kromozom sayısındaki değişimle karıştırmak.','Grafiğe göre doğru ifadeler.',
  metin=oncm('Grafikte, bir hayvanın üreme ana hücresinde mayoz bölünme boyunca hücre başına DNA miktarının değişimi verilmiştir. 1. aralık G1 evresini, 3. aralık mayoz I’i, 4. aralık mayoz II’yi göstermektedir.',d23,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',sekil=SK23,ad=o['ad'],
  ip=['DNA miktarının değiştiği her noktada kromozom sayısının da değişip değişmediğini ayrı ayrı düşün.'],
  bilgi=[B('DNA ve kromozom','DNA eşlenmesi kromozom sayısını değiştirmez, kromozomları çift kromatitli yapar · Mayoz I’de homologlar ayrılınca kromozom sayısı ve DNA yarıya iner')],
  puf='DNA miktarı ile kromozom sayısını ayrı ayrı izle: eşlenme yalnız DNA’yı artırır.')
# ================= 24 · kromozom sayısı grafiği (mitoz) =================
P24=[(0,8),(4.3,8),(4.6,16),(6.4,16),(6.7,8),(9,8)]; SN24=[0,4.3,6.7,9]
assert F(P24,2)==8 and F(P24,5)==16 and F(P24,8)==8
SK24=tk(eksen(P24,[8,16],9,19.5,(SN24,['1','2','3']),w=6.6,h=4.4,ylab='Kromozom sayısı',xlab='Zaman'),1.05)
n24=8//2; kro24=8*2; assert kro24+n24==20 and 8+n24==12 and 8+8==16 and kro24+8==24 and 16*2+0==32
Q('24','grafik','zor','Mitozda kromozom sayısı grafiği','Mitoz sırasında hücredeki kromozom sayısı grafiğini kromatit ve gamet sayısıyla ilişkilendirir.','grafik',
  'Anafazda kardeş kromatitler ayrılınca hücredeki kromozom sayısı geçici olarak iki katına çıkar; 2n değeri 1. aralıktan okunur.','Kromozom sayısı ile kromatit sayısını karıştırmak; gametin n kromozomlu olduğunu unutmak.','Kromatit ve kromozom sayılarının toplamı.',
  metin='Grafikte, bir hayvanın vücut hücresinin mitoz bölünme boyunca hücredeki kromozom sayısının değişimi gösterilmiştir. 1. aralık, interfaz ile metafaz evresinin sonuna kadar olan süreyi, 2. aralık anafazdan sitoplazma bölünmesine kadar olan süreyi, 3. aralık ise oluşan yavru hücrelerin interfazını göstermektedir.\nBuna göre, 1. aralığın son evresindeki bu hücrede bulunan toplam kromatit sayısı ile aynı hayvanın bir sperm hücresindeki kromozom sayısının toplamı kaçtır?',
  dogru=20,yan=[(12,'Metafazdaki kromatit sayısını kromozom sayısıyla (8) bir tutmak: 8 + 4.','bilgi'),(16,'Kromatit sayısını 8 alıp spermi de 2n kromozomlu sanmak: 8 + 8.','bilgi'),(24,'Sperm hücresinin kromozom sayısını 2n (8) sanmak: 16 + 8.','bilgi'),(32,'Anafazdaki 16 kromozomu çift kromatitli sayıp (32) spermi hesaba katmamak.','dikkat')],
  istenen='Kromatit ve kromozom sayısı toplamı.',sekil=SK24,
  ad=[A('2n değerini oku','1. aralıkta hücredeki kromozom sayısı 8’dir; hayvanın vücut hücresi 2n = 8’dir.','2n = 8'),A('Metafazdaki kromatit sayısı','Metafazda DNA eşlenmiştir; her kromozom iki kromatitlidir.','8 × 2 = 16 kromatit'),A('Spermdeki kromozom sayısı','Sperm mayozla oluşur ve n kromozomludur.','n = 4'),A('Toplamı bul','Kromatit sayısı ile sperm kromozom sayısı toplanır.','16 + 4 = 20')],
  ip=['Grafikteki ilk düzeyden hayvanın vücut hücresindeki kromozom sayısını bul; gametlerin kromozom sayısını nasıl belirleyeceğini düşün.'],
  bilgi=[B('Kromozom ve kromatit','Eşlenmiş kromozom iki kromatitlidir · Anafazda kromatitler ayrılınca her biri ayrı kromozom sayılır ve hücredeki kromozom sayısı geçici olarak iki katına çıkar'),B('Gamet','Gametler mayozla oluşur ve n kromozomludur')],
  puf='2n değeri grafikte anafaz öncesindeki düzeydir; metafazda kromatit sayısı bunun iki katıdır.')
# ================= 25 · tablo: G2 ile sperm DNA farkı =================
D25=[('G1',6),('G2',12),('Mitoz sonunda oluşan yavru hücre',6)]
assert D25[1][1]-D25[0][1]//2==9 and D25[0][1]//2==3 and 12+3==15 and D25[1][1]-D25[0][1]==6
SK25=tabl(['Evre','DNA miktarı (birim)'],[[a,str(b)] for a,b in D25])
Q('25','hesap','orta','DNA miktarı ve gamet','Vücut hücresinin evrelere göre DNA miktarından gametin DNA miktarını çıkarır.','tablo',
  'Gamet n kromozomlu olduğundan DNA miktarı, G1’deki vücut hücresinin yarısıdır.','Spermin DNA miktarını G1’deki hücreyle ya da G2’deki hücreyle aynı sanmak.','G2’deki DNA miktarı ile spermdeki DNA miktarı arasındaki fark.',
  metin='Tabloda, 2n kromozomlu bir hayvanın vücut hücresinde hücre döngüsünün bazı evrelerindeki hücre başına DNA miktarı verilmiştir.\nBuna göre, hücrenin G2 evresindeki DNA miktarı ile aynı hayvanın olgun bir sperm hücresindeki DNA miktarı arasındaki fark kaç birimdir?',
  dogru=9,yan=[(3,'Fark yerine yalnız sperm hücresinin DNA miktarını vermek.','dikkat'),(6,'Spermin DNA miktarını G1’deki vücut hücresiyle aynı sanmak (12 − 6).','bilgi'),(12,'G2’deki DNA miktarını fark sanmak; spermi atlamak.','dikkat'),(15,'G2 ile sperm DNA miktarını çıkarmak yerine toplamak.','islem')],
  istenen='DNA miktarı farkı.',sekil=SK25,
  ad=[A('G2 evresindeki DNA','Tablodan G2 evresinin değeri okunur.','12 birim'),A('Spermdeki DNA','Sperm vücut hücresinin G1’indeki kromozom sayısının yarısını taşır; DNA miktarı da buna orantılıdır.','6 ÷ 2 = 3 birim'),A('Farkı bul','G2’deki değerden spermdeki değer çıkarılır.','12 − 3 = 9')],
  ip=['Spermin kromozom sayısının vücut hücresindeki kromozom sayısıyla ilişkisini düşün.'],
  bilgi=[B('DNA ve kromozom sayısı','Hücre başına DNA miktarı, hücrenin kromozom sayısıyla orantılıdır')],
  puf='Gametin DNA miktarı, aynı canlının G1’deki vücut hücresinin yarısıdır.')
# ================= 26 · hücre popülasyonu DNA dağılımı =================
D26=[('2 birim',540),('2 ile 4 birim arasında',300),('4 birim',160)]; N26=sum(x[1] for x in D26); assert N26==1000
assert 300/N26==.30 and 540/N26==.54 and 540/N26!=.70
SK26=tabl(['Hücre başına DNA miktarı','Hücre sayısı'],[[a,str(b)] for a,b in D26])
d26={'I':('Hücrelerin %30’u DNA eşlenmesi evresindedir.',True,'DNA miktarı 2 ile 4 birim arasında olan hücreler S evresindedir ve toplamın %30’udur (300 ÷ 1000)','S evresindeki hücreler'),
     'II':('DNA miktarı 4 birim olan hücrelerin tümü mitoz bölünme geçirmektedir.',False,'4 birim DNA, G2 evresindeki hücrelerde de vardır; bu hücrelerin tümü mitozda değildir','4 birim DNA’lı hücreler'),
     'III':('Hücrelerin %70’inin DNA miktarı, eşlenmeden önceki düzeydedir.',False,'DNA miktarı eşlenmeden önceki düzeyde (2 birim) olan hücreler %54’tür (540 ÷ 1000)','2 birim DNA’lı hücreler')}
o=onc(d26,True,harf=1)
Q('26','dongu','orta','Hücre döngüsünde DNA dağılımı','Bir hücre popülasyonunun DNA miktarı dağılımından hücrelerin evrelerini yorumlar.','tablo',
  'DNA miktarı 2 birim olan hücreler G1’de, 2–4 arası olanlar S’de, 4 birim olanlar G2 ya da mitozdadır.','4 birim DNA’lı hücrelerin hepsini mitozda sanmak.','Tabloya göre doğru ifadeler.',
  metin=oncm('Bir hayvan doku kültüründeki 1000 hücrenin hücre başına DNA miktarı ölçülmüş ve sonuçlar tabloda verilmiştir. Hücreler eş zamanlı olmayan biçimde mitozla bölünmektedir ve hücreler döngünün farklı evrelerindedir. Bölünmeyi yeni tamamlamış hücrelerin DNA miktarı 2 birimdir.',d26,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',sekil=SK26,ad=o['ad'],
  ip=['2 birimden 4 birime geçen DNA miktarının hücre döngüsünün hangi evresine karşılık geldiğini düşün.'],
  bilgi=[B('Evre – DNA miktarı','G1: eşlenmemiş DNA (en az düzey) · S: DNA eşlenirken ara değerler · G2 ve mitoz: eşlenmiş DNA (en yüksek düzey)')],
  puf='En düşük DNA düzeyi G1, ara değerler S, en yüksek düzey G2 ve mitoz hücreleridir.')
# ================= 27 · sperm ana hücresinden oluşan spermler =================
assert 4*(16//2)==32 and 16//4==4 and 16//2==8 and 2*(16//2)==16 and 3*(16//2)==24
Q('27','hesap','kolay','Mayozda gamet kromozomları','Bir ana hücreden oluşan gametlerdeki toplam kromozom sayısını hesaplar.','düz',
  'Bir sperm ana hücresi 4 sperm verir ve her sperm n kromozomludur.','Yalnız bir spermi saymak ya da gametlerin 2n kromozomlu olduğunu sanmak.','Dört spermdeki toplam kromozom sayısı.',
  metin='Kromozom sayısı 2n = 16 olan bir hayvanın testisindeki sperm ana hücrelerinden biri, krossing-over dahil tüm mayoz evrelerini eksiksiz tamamlamıştır.\nBuna göre, bu ana hücreden oluşan spermlerdeki toplam kromozom sayısı kaçtır?',
  dogru=32,yan=[(4,'2n değerini dörde bölmek.','islem'),(8,'Yalnız bir spermin kromozom sayısını (n = 8) vermek.','dikkat'),(16,'Spermleri 2 sanmak ya da bir spermi 2n kromozomlu saymak.','bilgi'),(24,'Üç sperm oluştuğunu sanmak (3 × 8).','bilgi')],
  istenen='Spermlerdeki toplam kromozom sayısı.',
  ad=[A('Bir spermin kromozomu','Mayozla oluşan gametler n kromozomludur.','n = 16 ÷ 2 = 8'),A('Sperm sayısını bul','Bir sperm ana hücresi mayozla 4 sperm oluşturur.','4 sperm'),A('Toplamı hesapla','Spermlerin kromozom sayıları toplanır.','4 × 8 = 32')],
  ip=['Bir ana hücreden kaç sperm oluştuğunu ve her spermin kromozom sayısını ayrı ayrı bul.'],
  bilgi=[B('Sperm oluşumu','Sperm ana hücresi mayozla bölünerek spermleri oluşturur; spermlerin kromozom sayısı ana hücreden farklıdır')],
  puf='Toplam kromozom = sperm sayısı × n.')
# ================= 28 · AaBbDd hücre başına gamet =================
def gamet_turleri(secimler):
    s=set()
    for a,b,d in secimler:
        s.add((a,b,d)); s.add((1-a,1-b,1-d))
    return s
tum=list(itertools.product((0,1),repeat=3)); en_cok=max(len(gamet_turleri(c)) for c in itertools.product(tum,repeat=3)); en_az=min(len(gamet_turleri(c)) for c in itertools.product(tum,repeat=3))
assert (en_cok,en_az)==(6,2) and len(gamet_turleri(tum))==8
Q('28','hesap','zor','Mayozla oluşan gamet çeşidi','Sınırlı sayıda ana hücreden oluşabilecek gamet çeşidi sayısını hesaplar.','yeni nesil',
  'Bir ana hücre mayozla yalnız 2 çeşit gamet verir; birden çok ana hücrede çeşit sayısı tüm olası gamet çeşidiyle sınırlıdır.','Bir ana hücreden tüm olası gamet çeşitlerinin oluşacağını sanmak.','En çok kaç farklı gamet genotipi.',
  metin='Genotipi AaBbDd olan ve bu genlerin ayrı homolog kromozom çiftlerinde bulunduğu bir hayvanın testisinde, üç sperm ana hücresi krossing-over olmaksızın mayoz bölünme geçirmektedir.\nBuna göre, bu üç hücreden oluşan toplam 12 sperm arasında en çok kaç farklı genotipte sperm bulunabilir?',
  dogru=6,yan=[(2,'Bir ana hücreden oluşan çeşit sayısını üç hücre için de geçerli saymak.','bilgi'),(3,'Çeşit sayısını ana hücre sayısına eşitlemek.','dikkat'),(8,'Her ana hücreden tüm olası gamet çeşitlerinin (2 üzeri 3) oluşabileceğini sanmak.','bilgi'),(12,'Sperm sayısını çeşit sayısı sanmak.','dikkat')],
  istenen='En çok farklı sperm genotipi sayısı.',
  ad=[A('Bir hücrenin vereceği çeşit','Bir sperm ana hücresi mayozla 4 sperm verir; bunlar yalnız 2 çeşittir (ikişer tane).','1 hücre → en çok 2 çeşit'),A('Üç hücreyi birleştir','Her hücre farklı çeşitler verecek biçimde bölünürse çeşitler toplanır.','3 × 2 = 6 çeşit'),A('Üst sınırı sına','Üç çift gen için toplam olası sperm çeşidi 2 × 2 × 2 = 8’dir; 6 bu sınırı aşmaz.','6 ≤ 8')],
  ip=['Tek bir sperm ana hücresinin kaç çeşit sperm verebileceğini bul, sonra hücreler arası çakışmayı düşün.'],
  bilgi=[B('Gamet çeşidi','Bir ana hücre mayozla 4 gamet oluşturur ve bunlar ikişer ikişer aynıdır · Genler ayrı kromozomlardaysa her hücrede homologların kutuplara dağılımı farklı olabilir')],
  puf='Bir ana hücre en çok 2 çeşit gamet verir; birden çok hücrede çeşit sayısı bunların toplamıyla ve tüm olası çeşitlerle sınırlıdır.')
# ================= 29 · insan zigotu mitoz =================
assert 8*46==368 and 46*3==138 and 8*23==184 and 46*6==276 and 16*46==736
Q('29','insan','orta','Zigotun bölünmesi','Döllenmeden sonra zigotun mitozla bölünmesiyle oluşan toplam kromozom sayısını hesaplar.','hikâyeli',
  'Zigot mitozla bölünür; her hücre 46 kromozomlu kalır ve hücre sayısı her bölünmede ikiye katlanır.','Bölünme sayısıyla hücre sayısını karıştırmak; zigotun kromozom sayısını yanlış almak.','Embriyodaki toplam kromozom sayısı.',
  metin='İnsanda döllenmeyle oluşan zigot, yumurta kanalında ilerlerken eş zamanlı olarak mitoz bölünmeyle çoğalmaya başlar. Bir embriyoda bu bölünmelerden ardışık üçünün tamamlandığı ve hiçbir hücrenin ölmediği bir anda hücreler sayılmıştır.\nBuna göre, bu embriyodaki hücrelerde bulunan toplam kromozom sayısı kaçtır?',
  dogru=368,yan=[(138,'Bölünme sayısını (3) kromozom sayısıyla çarpmak.','bilgi'),(184,'Zigotun 23 kromozomlu olduğunu sanıp 8 hücreyle çarpmak.','bilgi'),(276,'Her bölünmede hücre sayısını 2 artırıp 3 × 2 = 6 hücre saymak.','islem'),(736,'Dördüncü bölünmeyi de sayarak 16 hücre almak.','dikkat')],
  istenen='Toplam kromozom sayısı.',
  ad=[A('Zigotun kromozom sayısı','Zigot, sperm (23) ile yumurtanın (23) birleşmesiyle oluşur ve 2n kromozomludur.','23 + 23 = 46'),A('Hücre sayısını bul','Her mitoz bölünmede hücre sayısı iki katına çıkar.','2 üzeri 3 = 8 hücre'),A('Toplamı hesapla','Mitozda her hücre 46 kromozomlu kalır.','8 × 46 = 368')],
  ip=['Zigotun kromozom sayısını gametlerin kromozom sayılarından yola çıkarak bul.'],
  bilgi=[B('Zigot ve mitoz','Zigot, iki gametin birleşmesiyle 2n kromozomlu oluşur ve mitozla bölünerek embriyoyu oluşturur · Mitozda hücre sayısı her bölünmede ikiye katlanır, her hücre ana hücreyle aynı kromozom sayısını taşır')],
  puf='Önce hücre sayısını (2 üzeri bölünme sayısı), sonra her hücredeki 46 kromozomu çarp.')
# ================= 30 · dişi üreme sistemi şeması =================
def bez(p0,p1,p2,p3,t): return tuple((1-t)**3*a+3*(1-t)**2*t*b+3*(1-t)*t**2*c+t**3*d for a,b,c,d in zip(p0,p1,p2,p3))
def ureme():
    o=[]
    o.append('\\draw[line width=1.1pt] (-.8,1.3) .. controls (-.9,.4) and (-.4,.0) .. (-.25,-.5) -- (.25,-.5) .. controls (.4,.0) and (.9,.4) .. (.8,1.3) .. controls (.4,1.6) and (-.4,1.6) .. (-.8,1.3);')
    o.append('\\draw[line width=1.1pt] (-.25,-.5) -- (-.3,-1.7);\\draw[line width=1.1pt] (.25,-.5) -- (.3,-1.7);')
    for s in (-1,1):
        P0=(s*.75,1.28);P1=(s*1.6,1.95);P2=(s*2.3,1.75);P3=(s*2.7,1.25)
        Q0=(s*.78,1.08);Q1=(s*1.6,1.6);Q2=(s*2.2,1.45);Q3=(s*2.55,1.0)
        o.append(f'\\draw[line width=1.1pt] {P0} .. controls {P1} and {P2} .. {P3};'.replace('(-','(-'))
        o.append(f'\\draw[line width=1.1pt] {Q0} .. controls {Q1} and {Q2} .. {Q3};')
        o.append(f'\\draw[line width=1.1pt] (' f'{s*2.7:.2f},1.25) -- ({s*2.9:.2f},1.1);\\draw[line width=1.1pt] ({s*2.55:.2f},1.0) -- ({s*2.75:.2f},.85);')
        o.append(f'\\draw[line width=1.1pt] ({s*2.95:.2f},.55) ellipse (.5 and .33);')
    # etiketler
    t=bez((-.75,1.28),(-1.6,1.95),(-2.3,1.75),(-2.7,1.25),.5)
    o.append(f'\\node[font=\\normalsize\\bfseries] at (0,.6) {{1}};')
    o.append(f'\\node[font=\\normalsize\\bfseries] at ({t[0]:.2f},2.75) {{2}};\\draw[line width=.7pt] ({t[0]:.2f},2.5) -- ({t[0]:.2f},{t[1]+.03:.2f});')
    o.append('\\node[font=\\normalsize\\bfseries] at (-2.95,-.4) {3};\\draw[line width=.7pt] (-2.95,-.15) -- (-2.95,.22);')
    o.append('\\node[font=\\normalsize\\bfseries] at (1.0,-1.1) {4};\\draw[line width=.7pt] (.8,-1.1) -- (.34,-1.1);')
    return '\n'.join(o)
SK30=tk(ureme(),1.15)
t30=[('Döllenme genellikle 2 numaralı yapıda gerçekleşir.',True,'döllenme yumurta kanalında olur'),
     ('Yumurta ana hücrelerinin mayoz bölünme geçirdiği yapı 1 numaralı yapıdır.',False,'yumurta ana hücreleri yumurtalıkta (3 numaralı yapı) mayoz geçirir'),
     ('Zigotun bölünerek oluşturduğu embriyo, 3 numaralı yapıya tutunarak gelişir.',False,'embriyo rahime (1 numaralı yapı) tutunur; 3 numaralı yapı yumurtalıktır'),
     ('Doğum sırasında bebek, 2 numaralı yapıdan geçerek dışarı çıkar.',False,'doğum yolu vajinadır (4 numaralı yapı); 2 numaralı yapı yumurta kanalıdır'),
     ('4 numaralı yapıda yumurta hücresi oluşur.',False,'yumurta hücreleri yumurtalıkta (3 numaralı yapı) oluşur')]
r=tek(t30,hedef=True,harf=2)
Q('30','insan','kolay','Kadın üreme sistemi','Kadın üreme sisteminin yapılarını şematik çizimde tanır ve görevleriyle eşleştirir.','şekilli',
  'Yumurta yumurtalıkta oluşur, döllenme yumurta kanalında, gelişme rahimde olur; doğum yolu vajinadır.','Döllenmenin rahimde olduğunu sanmak.','Şekle göre doğru ifade.',
  metin='Şekilde, insanda kadın üreme sisteminin bazı yapıları 1, 2, 3 ve 4 numaralarıyla gösterilmiştir. Bu yapılar gamet oluşumu, döllenme ve embriyonun gelişimi gibi farklı olaylarda görev yapmaktadır.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
  dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Şekle göre doğru ifade.',sekil=SK30,
  ad=[A('Yapıları tanı','Ortadaki armut biçimli yapı rahim, iki yanındaki ince borular yumurta kanalı, uçlardaki oval yapılar yumurtalık, alttaki kanal vajinadır.','1: rahim · 2: yumurta kanalı · 3: yumurtalık · 4: vajina'),A('Görevleri hatırla','Yumurta yumurtalıkta oluşur; döllenme yumurta kanalında olur; embriyo rahime tutunur; doğum vajinadan gerçekleşir.','Döllenme: 2 numaralı yapı'),A('İfadeleri ele','Yalnız döllenmenin yeri doğru verilmiştir; diğer ifadelerde yapılar karıştırılmıştır.','Doğru ifade: döllenme 2’de')],
  ip=['Önce numaralı yapıların adlarını şekilden belirle, sonra her olayın hangi yapıda gerçekleştiğini düşün.'],
  bilgi=[B('Kadın üreme sistemi','Yumurtalık: yumurta oluşumu · Yumurta kanalı: döllenme yeri · Rahim: embriyonun tutunup geliştiği yer · Vajina: doğum yolu')],
  puf='Yumurtalıkta oluşur, kanalda döllenir, rahimde gelişir, vajinadan doğar.')
# ================= 31 · sperm/yumurta oluşumu (olumsuz) =================
t31=[('Bir sperm ana hücresinden mayoz bölünmeyle dört işlevsel sperm oluşur.',True,'sperm ana hücresi mayozla 4 sperm verir'),
     ('Bir yumurta ana hücresinden mayoz bölünmeyle bir olgun yumurta oluşur.',True,'yumurta ana hücresi 1 yumurta ve 3 kutup hücresi verir'),
     ('Sperm hücreleri yumurtaya göre çok daha küçük ve hareketlidir.',True,'sperm kamçısı ile hareket eder; yumurta besin deposu nedeniyle büyüktür'),
     ('Yumurta oluşumunda ortaya çıkan kutup hücreleri döllenmede görev almaz.',True,'kutup hücreleri gamet olarak kullanılmaz'),
     ('Sperm ve yumurta oluşumu sırasında kromozom sayısı mitoz bölünmeyle yarıya indirilir.',False,'kromozom sayısını yarıya indiren bölünme mayozdur; mitozda kromozom sayısı değişmez')]
r=tek(t31,hedef=False,harf=2)
Q('31','insan','orta','Sperm ve yumurta oluşumu','Gamet oluşumunda sperm ve yumurta farklarını ve mayozun rolünü değerlendirir.','düz',
  'Sperm ve yumurta mayozla oluşur; sperm ana hücresi 4 sperm, yumurta ana hücresi 1 yumurta verir.','Gamet oluşumunda kromozom sayısını mitozun yarıya indirdiğini sanmak.','Gamet oluşumuyla ilgili söylenemeyecek ifade.',
  metin='İnsanda erkeklerde testislerde, kadınlarda ise yumurtalıklarda gamet oluşumu gerçekleşir. Bu gametlerin oluşumu ile ilgili bir biyoloji öğretmeni beş ifade yazmış, ancak bunlardan birinin bilimsel olarak doğru olmadığını belirtmiştir.\nBuna göre, gamet oluşumu ile ilgili aşağıdakilerden hangisi söylenemez?',
  dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Söylenemeyecek ifade.',
  ad=[A('Gamet oluşumunu hatırla','Gametler, üreme ana hücrelerinin mayoz bölünmesiyle oluşur; kromozom sayısını yarıya indiren bölünme mayozdur.','Gamet: mayoz, n kromozom'),A('Sperm ve yumurtayı karşılaştır','Sperm ana hücresi 4 sperm, yumurta ana hücresi 1 yumurta ve 3 kutup hücresi verir; sperm küçük ve hareketlidir.','Dört ifade doğru'),A('Yanlışı bul','Kromozom sayısının mitozla yarıya indirildiğini söyleyen ifade bilimsel olarak yanlıştır.','Söylenemez: mitozla yarıya inme')],
  ip=['Kromozom sayısını yarıya indiren bölünmenin hangisi olduğunu düşün.'],
  bilgi=[B('Sperm ve yumurta','Sperm ana hücresi ve yumurta ana hücresi, mayoz sonunda farklı sayıda gamet ve farklı büyüklükte hücreler oluşturur')],
  puf='Gamet = mayoz; kromozom sayısını yarıya indiren tek bölünme mayozdur.')
# ================= 32 · embriyonun gelişimi (insan) =================
d32={'I':('Zigotun embriyoya dönüşürken hücre sayısı mayoz bölünmeyle artar.',False,'zigot ve embriyonun hücre sayısı artışı mitozla olur; mayoz yalnız gamet oluşumunda görülür','Hücre sayısının artışı'),
     'II':('Embriyonun beslenmesi ve gaz alışverişi, plasenta ve göbek bağı aracılığıyla gerçekleşir.',True,'madde alışverişi plasentada annenin ve embriyonun kan damarları arasında, göbek bağı yoluyla olur','Beslenme ve gaz alışverişi'),
     'III':('Anne ve embriyonun kanları plasentada birbirine karışmaz.',True,'maddeler damar duvarlarından geçerek alışveriş yapar; iki kan birbirine karışmaz','Kanların durumu')}
o=onc(d32,True,harf=5)
Q('32','insan','orta','Embriyonun gelişimi','Döllenme sonrası embriyonun gelişimi ve beslenmesiyle ilgili ifadeleri değerlendirir.','öncüllü',
  'Zigot mitozla bölünür; embriyo plasenta ve göbek bağıyla beslenir, anne ve bebek kanları karışmaz.','Embriyonun gelişiminde mayozun görev aldığını sanmak; anne ve bebek kanlarının karıştığını sanmak.','Doğru ifadelerin belirlenmesi.',
  metin=oncm('İnsanda döllenmeden sonra zigot, yumurta kanalından rahime doğru ilerleyerek gelişmeye devam eder. Embriyonun gelişimiyle ilgili olarak,',d32,'ifadelerine yer verilmiştir. Buna göre, bu ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',ad=o['ad'],
  ip=['Zigotun hücre sayısını artıran bölünmenin türünü ve embriyo ile annenin madde alışverişinin nasıl olduğunu düşün.'],
  bilgi=[B('Embriyonik gelişim','Zigot mitozla bölünerek embriyoyu oluşturur · Embriyo rahime tutunur · Plasenta ve göbek bağı madde alışverişini sağlar, kanlar karışmaz')],
  puf='Zigottan sonra yalnız mitoz vardır; madde alışverişi kan karışmadan plasentada olur.')
# ================= 33 · spermatogenez diyagramı =================
def sperm_sema():
    o=[]; R=.5
    def c(x,y,t): return f'\\draw[line width=.9pt] ({x},{y}) circle ({R});\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};'
    def kenar(x1,y1,x2,y2):
        d=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/d,(y2-y1)/d
        return f'\\draw[-Stealth,line width=1pt] ({x1+ux*(R+.05):.2f},{y1+uy*(R+.05):.2f}) -- ({x2-ux*(R+.07):.2f},{y2-uy*(R+.07):.2f});'
    o.append(c(0,0,'I'))
    for y in (1.6,-1.6):
        o.append(c(3.4,y,'II')); o.append(kenar(0,0,3.4,y))
        for dy in (1.0,-1.0):
            o.append(c(7.0,y+dy,'III')); o.append(kenar(3.4,y,7.0,y+dy))
    o.append('\\node[font=\\normalsize] at (1.1,1.35) {Mayoz I};\\node[font=\\normalsize] at (5.2,0) {Mayoz II};')
    return '\n'.join(o)
SK33=tk(sperm_sema(),.9)
assert 46*2//2==46 and 23*1==23 and 46+23==69 and 23+23==46 and 46+46==92 and 92+23==115 and 92+46==138
Q('33','insan','zor','Spermatogenez','Sperm oluşumu aşamalarında kromatit sayısını hesaplar.','şekilli',
  'Mayoz I sonunda hücreler n kromozomlu ve çift kromatitli, mayoz II sonunda n kromozomlu ve tek kromatitlidir.','Mayoz I sonundaki hücreleri tek kromatitli saymak; kromozom ve kromatit sayısını karıştırmak.','Kromatit sayıları toplamı.',
  metin='Şekilde, insanda bir sperm ana hücresinden sperm oluşumunun aşamaları gösterilmiştir. I numaralı hücre DNA eşlenmesini tamamlamıştır ve 46 kromozom içermektedir. III numaralı hücrelerin her biri mayoz II sonunda oluşmuştur.\nBuna göre, II numaralı hücrelerden birindeki kromatit sayısı ile III numaralı hücrelerden birindeki kromatit sayısının toplamı kaçtır?',
  dogru=69,yan=[(46,'Kromatit sayısını kromozom sayısıyla bir tutmak (23 + 23).','bilgi'),(92,'III numaralı hücreyi de çift kromatitli saymak (46 + 46).','bilgi'),(115,'II numaralı hücreyi I numaralı hücre gibi saymak (92 + 23).','bilgi'),(138,'II numaralı hücreyi I gibi (92), III numaralı hücreyi 46 kromatitli sayıp 92 + 46 işlemini yapmak.','islem')],
  istenen='Kromatit sayıları toplamı.',sekil=SK33,
  ad=[A('II numaralı hücre','Mayoz I’de homologlar ayrılır; hücreler 23 kromozomlu olur ve kromozomlar çift kromatitlidir.','23 × 2 = 46 kromatit'),A('III numaralı hücre','Mayoz II’de kardeş kromatitler ayrılır; her hücre 23 kromozomlu ve tek kromatitlidir.','23 kromatit'),A('Toplamı bul','İki hücredeki kromatit sayıları toplanır.','46 + 23 = 69')],
  ip=['Mayoz I’de ve mayoz II’de hangi yapıların ayrıldığını ve her aşamada kromozomların kaç kromatitli olduğunu düşün.'],
  bilgi=[B('Sperm oluşumu','1 sperm ana hücresi → mayoz I → 2 hücre → mayoz II → 4 hücre · Mayoz I’de homologlar, mayoz II’de kardeş kromatitler ayrılır')],
  puf='Mayoz I sonunda kromozomlar çift, mayoz II sonunda tek kromatitlidir.')
# ================= 34 · hayvan hücresi mitozu: yapılar =================
def yapilar():
    o=[hucre(0,0,MET4,'plak',rx=1.9,ry=1.3,cent=True)]
    px=-1.67
    o.append(f'\\node[font=\\normalsize\\bfseries] at (-2.55,.75) {{1}};\\draw[line width=.7pt] (-2.4,.62) -- ({px-.06},.08);')
    mx,my=(px+0)/2,(0+.75)/2   # sol kutuptan ilk kromozoma giden lif ortası
    o.append(f'\\node[font=\\normalsize\\bfseries] at (-1.0,1.65) {{2}};\\draw[line width=.7pt] (-1.0,1.4) -- ({mx*1.0:.2f},{my+0.04:.2f});')
    return '\n'.join(o)
SK34=tk(yapilar(),1.3)
d34={'I':('1 numaralı yapılar, iğ ipliklerinin oluşumunda görev alır.',True,'sentriyoller iğ ipliklerinin oluşumuna katılır','1 numaralı yapılar'),
     'II':('2 numaralı yapılar, telofazda kardeş kromatitlerin birbirinden ayrılmasını sağlar.',False,'kardeş kromatitler anafazda ayrılır; telofazda çekirdekler oluşur','2 numaralı yapılar'),
     'III':('Hayvan hücrelerinde 1 numaralı yapılar interfazda eşlenir.',True,'sentriyoller bölünmeye hazırlık olarak interfazda eşlenir','Sentriyol eşlenmesi')}
o=onc(d34,True,harf=5)
Q('34','mitoz','orta','Mitozda hücre yapıları','Hayvan hücresindeki sentriyol ve iğ ipliklerinin mitozdaki görevlerini yorumlar.','öncüllü',
  'Sentriyoller interfazda eşlenir ve iğ ipliklerinin oluşumuna katılır; iğ iplikleri anafazda kromatitleri kutuplara çeker.','İğ ipliklerinin görevini telofaza kaydırmak.','Doğru ifadelerin belirlenmesi.',
  metin=oncm('Şekilde, mitoz bölünmenin bir evresindeki hayvan hücresi ve bazı yapılar 1 ve 2 numaralarıyla gösterilmiştir.',d34,'Buna göre, yukarıdaki ifadelerden hangileri doğrudur?'),
  dogru=o['dogru'],yan=o['yan'],sira=o['sira'],istenen='Doğru ifadelerin belirlenmesi.',sekil=SK34,ad=o['ad'],
  ip=['Kutuplardaki yapılar ile bunlardan kromozomlara uzanan liflerin görevlerini ayrı ayrı düşün.'],
  bilgi=[B('Mitozda yapılar','Sentriyoller (hayvan hücresi) interfazda eşlenir, iğ ipliklerinin oluşumuna katılır · İğ iplikleri kromozomların sentromerine bağlanır ve anafazda kardeş kromatitleri kutuplara çeker')],
  puf='Sentriyol: iğ ipliği kurucusu; iğ ipliği: anafazda kromatitleri çekici.')
bitir(P,'bolunmeiki',UK)
