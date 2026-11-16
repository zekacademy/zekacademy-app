"""TYT Fizik · Manyetizma (ikinci paket) · 14 soru (kardeş yok, ipucu 1). Şekiller TikZ (cizim.tikz_svg); alan çizgileri ve alan şiddetleri Python'da hesaplanır.
Öncüllü sorularda her öncülün doğruluğu TEK yerde (onc() girdisi) tanımlanır; anahtar, adımlar ve çeldirici açıklamaları oradan üretilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,GD); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
from math import sin,cos,radians,pi,sqrt
H.KONU='Manyetizma'
P=Parti('manyetizmaiki','Manyetizma','fiz|Manyetizma',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 TYT Fizik manyetizma soruları (yalnız mantık) · MEB 10. sınıf fizik'
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
MARK='postaction={decorate,decoration={markings,mark=at position .5 with {\\arrow{Stealth[length=1.9mm,width=1.7mm]}}}}'
def p2(x,y): return f'({x:.3f},{y:.3f})'

def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    kart(f'K-FZMN2-{no}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    mk(P,no,ad=ad,adim=len(ad),**k)

# ---------- öncüllü yardımcı ----------
ETK={'I':'I’i','II':'II’yi','III':'III’ü'}
OPT={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
CAN=list(OPT)
def onc(stmts,sira,intro,outro='yargılarından hangileri doğrudur?'):
    """stmts: [dict(t=öncül, v=doğru mu, ok=adım açıklaması (doğru kavram), inc=yanlış öncülü doğru sanma nedeni, exc=doğru öncülü yanlış sanma nedeni)]"""
    assert [CAN.index(s) for s in sira]==sorted(CAN.index(s) for s in sira) and len(sira)==5
    T={i for i,s in enumerate(stmts) if s['v']}
    dogru=[s for s in sira if OPT[s]==T]; assert len(dogru)==1,('doğru küme şıklarda yok',T)
    lab=['I','II','III']
    metin=intro+'\n'+'\n'.join(f'{lab[i]}. {s["t"]}' for i,s in enumerate(stmts))+'\n'+outro
    yan=[]
    for o in sira:
        if o==dogru[0]: continue
        S=OPT[o]; why=[]
        for i in sorted(S^T):
            why.append(stmts[i]['inc'] if i in S else stmts[i]['exc'])
        yan.append((o,' '.join(why),'bilgi'))
    steps=[A(f'{ETK[lab[i]]} değerlendir',s['ok'],f'{lab[i]} {"doğru" if s["v"] else "yanlış"}') for i,s in enumerate(stmts)]
    return dict(metin=metin,dogru=dogru[0],sira=list(sira),yan=yan),steps

# ---------- şekil yardımcıları ----------
def magnet(x,y,w,h,labs=('N','S'),nfill=True,nleft=True,size=''):
    """Yatay çubuk mıknatıs; sol yarı labs[0], sağ yarı labs[1]; N yarısı gri."""
    o=[]
    for k,(xx,lb) in enumerate([(x,labs[0]),(x+w/2,labs[1])]):
        isN=(lb=='N')
        fill='gray!40' if (isN and nfill) else 'white'
        o.append(f'\\draw[thick,fill={fill}] ({xx:.3f},{y:.3f}) rectangle ({xx+w/2:.3f},{y+h:.3f});')
        if lb: o.append(f'\\node[font=\\small\\bfseries] at ({xx+w/4:.3f},{y+h/2:.3f}) {{{lb}}};')
    return '\n'.join(o)
def compass(x,y,lab,r=.3,below=True):
    s=f'\\draw[thick,fill=white] ({x:.3f},{y:.3f}) circle ({r});\n'
    s+=f'\\node[font=\\small\\bfseries] at ({x:.3f},{y-r-.28 if below else y+r+.28:.3f}) {{{lab}}};'
    return s
def dot(x,y,lab,dx=.28,dy=.28):
    return f'\\fill ({x:.3f},{y:.3f}) circle (2.2pt);\n\\node[font=\\small\\bfseries] at ({x+dx:.3f},{y+dy:.3f}) {{{lab}}};'
def pole_field(x,y,d=.8):
    """N kutbu (d,0), S kutbu (-d,0) olan iki tekil kutup modeli; (x,y)'deki alan vektörü."""
    ex=ey=0
    for qq,px in ((1,d),(-1,-d)):
        rx,ry=x-px,y; r3=(rx*rx+ry*ry)**1.5; ex+=qq*rx/r3; ey+=qq*ry/r3
    return ex,ey
def field_lines(nl=14,d=.8,box=(3.9,2.9)):
    out=[]
    for k in range(nl):
        f=(k+.5)*2*pi/nl; x,y=d+.18*cos(f),.18*sin(f); pts=[(x,y)]
        for _ in range(4000):
            def u(a,b):
                ex,ey=pole_field(a,b,d); m=sqrt(ex*ex+ey*ey); return ex/m,ey/m
            h=.04; k1=u(x,y); k2=u(x+h/2*k1[0],y+h/2*k1[1]); k3=u(x+h/2*k2[0],y+h/2*k2[1]); k4=u(x+h*k3[0],y+h*k3[1])
            x+=h/6*(k1[0]+2*k2[0]+2*k3[0]+k4[0]); y+=h/6*(k1[1]+2*k2[1]+2*k3[1]+k4[1]); pts.append((x,y))
            if (x+d)**2+y**2<.16**2 or abs(x)>box[0] or abs(y)>box[1]: break
        out.append(pts[::5]+[pts[-1]])
    return out
def coil(x0,n,R,p,d,plus_left):
    """Önden geçen sarımlar kalın '/' çizgiler; akım + uçtan girer. Döndürür (tikz, sol_uç_x, sağ_uç_x, N_uç ('sol'|'sağ'))."""
    o=[];xe=x0+(n-1)*p+d
    for i in range(n):
        xi=x0+i*p
        o.append(f'\\draw[very thick] {p2(xi,-R)} -- {p2(xi+d,R)};')
        if i<n-1: o.append(f'\\draw[gray,thin,dashed] {p2(xi+d,R)} -- {p2(xi+p,-R)};')
    yb=-R-1.3; yt=R+.9; xr=xe+2.3; bx=(x0+xr)/2
    o.append(f'\\draw[thick] {p2(x0,-R)} -- {p2(x0,yb)} -- {p2(x0+.9-.35,yb)};\\draw[thick] {p2(x0+.9+.35,yb)} -- {p2(bx-.14,yb)};')
    o.append(f'\\draw[thick] {p2(bx+.14,yb)} -- {p2(xr,yb)} -- {p2(xr,yt)} -- {p2(xe,yt)} -- {p2(xe,R)};')
    sx=x0+.9; o.append(f'\\draw[thick,fill=white] {p2(sx-.35,yb)} circle (1.5pt);\\draw[thick,fill=white] {p2(sx+.35,yb)} circle (1.5pt);\\draw[thick] {p2(sx-.35,yb)} -- {p2(sx+.3,yb+.3)};')
    Lh,Sh=.30,.16
    lp,sp=(bx-.14,bx+.14) if plus_left else (bx+.14,bx-.14)
    o.append(f'\\draw[thick] {p2(lp,yb-Lh)} -- {p2(lp,yb+Lh)};\\draw[thick] {p2(sp,yb-Sh)} -- {p2(sp,yb+Sh)};')
    pl,mn=(bx-.14-.3,bx+.14+.3) if plus_left else (bx+.14+.3,bx-.14-.3)
    o.append(f'\\node at {p2(pl,yb+.42)} {{$+$}};\\node at {p2(mn,yb+.42)} {{$-$}};')
    # akım + uçtan girer. Sol uçtan giriyorsa ön tellerde akım yukarı => B = -x (N sol).
    N='sol' if plus_left else 'sağ'
    return '\n'.join(o),x0,xe,N

# =================== 01 · bölünme · kolay ===================
kartla('01','Mıknatısın bölünmesi','Kesilen her parça ilk mıknatısla aynı yönde kutuplanır: her parçanın sol ucu N, sağ ucu S kutbudur; tek kutuplu parça olmaz.','Parçalardan birinin yalnız N ya da yalnız S kutbu olacağını sanmak; kesilen yüzeylerde kutup oluşmadığını düşünmek.','kolay','öncüllü',3,'fz-mn2-bolunme','Mıknatısın bölünmesi')
o=[]
o.append('\\draw[thick] (0,0) rectangle (6,.9);')
o.append('\\node[font=\\small\\bfseries] at (-.35,.45) {N};\\node[font=\\small\\bfseries] at (6.35,.45) {S};')
for x in (2,4): o.append(f'\\draw[dashed,thick] ({x},-.25) -- ({x},1.15);')
for i,x in enumerate((1,3,5)): o.append(f'\\node at ({x},1.45) {{{i+1}}};')
SK1=tikz_svg(HEAD+'\n'.join(o)+TAIL)
ic,ad=onc([
 dict(t='2 numaralı parçanın sol ucu N, sağ ucu S kutbudur.',v=True,ok='Kesilen her parça ilk mıknatısla aynı yönde kutuplanır; her parçada sol uç N, sağ uç S olur.',exc='Ortadaki parçanın kutupsuz kalacağını ya da kutuplarının farklı olacağını sanmış.'),
 dict(t='1 numaralı parçanın sağ ucu ile 3 numaralı parçanın sol ucu aynı cins kutuplardır.',v=False,ok='1 numaralı parçanın sağ ucu S, 3 numaralı parçanın sol ucu N kutbudur; farklı cinstirler.',inc='Kesilen yüzeylerde aynı cins kutupların oluştuğunu sanmış; oysa her parçanın sağ ucu S, sol ucu N olur.'),
 dict(t='3 numaralı parçanın sağ ucu N kutbudur.',v=False,ok='3 numaralı parçanın sağ ucu ilk mıknatısın S kutbudur; kesme kutupları değiştirmez.',inc='Kesmenin uçlardaki kutupları değiştireceğini sanmış; oysa sağ uç ilk mıknatısın S kutbudur.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 'Bir fizik öğretmeni, kutupları şekilde gösterilen uzun bir çubuk mıknatısı kesikli çizgilerin bulunduğu yerlerden, boyuna dik olacak biçimde keserek 1, 2 ve 3 numaralı üç eşit parçaya ayırıyor. Parçaların hiçbiri döndürülmeden masaya, ilk mıknatıstaki sıralarıyla diziliyor. Öğretmen öğrencilerden küçük bir pusula ve demir tozuyla parçaların kutuplarını ve birbirlerine etkilerini yorumlamalarını istiyor.\nBuna göre,')
q('0001',ad+[A('Sonuç','Yalnız I doğrudur.','Yalnız I')],tipId='fz-mn2-bolunme',tip='Mıknatısın bölünmesi',z='kolay',alt='Mıknatıs ve Manyetik Alan',kaz='Bölünen mıknatısın parçalarında oluşan kutupları ve parçaların birbirine etkisini belirler.',kalip='öncüllü',
 kart='K-FZMN2-01 (mıknatısın bölünmesi) · üç parça, kesilen yüzeylerdeki kutuplar',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Kesilen her parçanın uçlarında hangi kutupların oluşacağını ilk mıknatısın şeklinden yola çıkarak düşün.'],
 bilgi=[B('Mıknatısın bölünmesi','bir mıknatıs kesildiğinde her parça yine N ve S kutbu olan bir mıknatıs olur ve ilk mıknatısla aynı yönde kutuplanır. Örnek: soldan sağa N–S olan bir mıknatısın her parçası da soldan sağa N–S dizilir')],
 puf='Mıknatıs kırılınca tek kutuplu parça oluşmaz; her parça ilk mıknatısla aynı yönde N ve S kutbu kazanır.',sekil=SK1,**ic)

# =================== 02 · alan şiddeti · kolay ===================
kartla('02','Manyetik alan çizgileri ve alan şiddeti','Alan çizgilerinin sık olduğu yer alanın güçlü, seyrek olduğu yer zayıf olduğu yerdir; kutuplara yakın bölgede alan en büyüktür.','Alan şiddetini mıknatısın ortasında en büyük sanmak; çizgilerin dışında kalan yerde de alan şiddetini aynı almak.','kolay','şekilli',3,'fz-mn2-sikalan','Alan çizgilerinin sıklığı ve alan şiddeti')
dk=(1.3,.12); dl=(0,2.05); dm=(0,3.7)
bk,bl,bm=[sqrt(sum(c*c for c in pole_field(*pp))) for pp in (dk,dl,dm)]
assert bk>bl>bm and bk/bl>5 and bl/bm>1.8
o=[]
FL=field_lines()
for pts in list(FL)+[[(-x,y) for x,y in reversed(pts)] for pts in FL if (pts[-1][0]+.8)**2+pts[-1][1]**2>.2]:
    o.append(f'\\draw[line width=.55pt,{MARK}] '+' -- '.join(p2(*a) for a in pts)+';')
o.append(magnet(-1,-.3,2,.6,labs=('S','N')))
o.append(dot(*dk,'K',.05,.3)+dot(*dl,'L',.3,0)+dot(*dm,'M',.3,0))
SK2=tikz_svg(HEAD+'\n'.join(o)+TAIL)
q('0002',[A('Çizgi sıklığını incele','Alan çizgilerinin sık olduğu yerde alan şiddeti büyüktür.','sık → güçlü alan'),
 A('K noktası','K, N kutbunun hemen yanındadır; çizgiler burada en sıktır.','B_K en büyük'),
 A('L noktası','L iki halka arasındaki geniş aralıktadır; çizgiler seyrektir.','B_L orta'),
 A('M noktası','M en dıştaki çizginin de dışında, çizgilerin en seyrek olduğu bölgededir.','B_M en küçük'),
 A('Sonuç','Büyükten küçüğe sırala.','B_K > B_L > B_M')],
 tipId='fz-mn2-sikalan',tip='Alan çizgilerinin sıklığı ve alan şiddeti',z='kolay',alt='Mıknatıs ve Manyetik Alan',kaz='Manyetik alan çizgilerinin sıklığından alan şiddetlerini karşılaştırır.',kalip='şekilli',
 kart='K-FZMN2-02 (alan çizgisi sıklığı) · kutba yakın, yanda ve uzak üç nokta',
 metin='Fizik dersinde öğretmen, çubuk mıknatısın üzerine yerleştirdiği şeffaf levhaya demir tozu serpiyor ve tozların dizilişine bakarak manyetik alan çizgilerini şekildeki gibi çiziyor; çizgilerin yönünü de oklarla gösteriyor. Ardından öğrencilerden levha üzerindeki K, L ve M noktalarında manyetik alanın şiddetini (B_K, B_L, B_M) karşılaştırmalarını istiyor. Noktalar levha üzerindedir ve ortamda başka mıknatıs bulunmamaktadır.\nBuna göre, B_K, B_L ve B_M arasındaki ilişki aşağıdakilerden hangisidir?',
 sekil=SK2,dogru='B_K > B_L > B_M',sira=['B_K > B_L > B_M','B_M > B_L > B_K','B_L > B_K > B_M','B_K > B_M > B_L','B_K = B_L = B_M'],
 yan=[('B_M > B_L > B_K','Mıknatısın kutuplarından uzaklaştıkça alanın güçleneceğini sanmış; oysa alan çizgileri uzakta seyrektir.','bilgi'),
  ('B_L > B_K > B_M','Alanın mıknatısın orta bölgesinde en şiddetli olduğunu sanmış; alan kutuplara yakın yerlerde daha şiddetlidir.','bilgi'),
  ('B_K > B_M > B_L','Çizgilerin sıklığını okurken M noktasını L’den yoğun almış; M çizgilerin en seyrek olduğu yerdedir.','dikkat'),
  ('B_K = B_L = B_M','Alanın her noktada aynı olduğunu sanmış; çizgi sıklığının alan şiddetini gösterdiğini atlamış.','bilgi')],
 istenen='K, L ve M noktalarındaki alan şiddetlerinin sıralaması.',ip=['Alan çizgilerinin her bir noktanın çevresinde ne kadar sık ya da seyrek geçtiğine bak.'],
 bilgi=[B('Alan çizgilerinin sıklığı','manyetik alan çizgileri kutuplarda sıktır ve uzaklaştıkça seyrekleşir; çizgilerin sık olduğu yerde alan şiddeti büyüktür. Örnek: çizgilerin birbirine yakın olduğu bölge, aralıklı olduğu bölgeden daha güçlü bir alana sahiptir')],
 puf='Alan çizgileri ne kadar sıksa manyetik alan o kadar şiddetlidir; en şiddetli alan kutuplara yakındır.')

# =================== 03 · asılı mıknatıslar · zor ===================
kartla('03','İpe asılı mıknatıslar ve denge','İtme gören mıknatıslar birbirinden uzağa sapar: bakışan uçlar aynı cinstir; etki-tepki gereği kuvvetler eşit büyüklüktedir; mıknatıs ters çevrilirse itme çekmeye döner.','Güçlü mıknatısın daha büyük kuvvet uyguladığını sanmak; bakışan uçların farklı cins olduğunu düşünmek.','orta','öncüllü',4,'fz-mn2-asili','İpe asılı mıknatıslar')
LL=2.4; sh=.6; hw=.8
o=['\\draw[thick] (-4.6,3.0) -- (4.6,3.0);']
for c0,s_ in ((-2.2,-sh),(2.2,sh)):
    cx=c0+s_; y=3.0-sqrt(LL**2-sh**2)
    for dx in (-.55,.55): o.append(f'\\draw[thick] {p2(c0+dx,3.0)} -- {p2(cx+dx,y+.25)};')
    o.append(None)
    # mıknatıs
    if c0<0: o[-1]=magnet(cx-hw,y-.25,2*hw,.5)
    else: o[-1]=magnet(cx-hw,y-.25,2*hw,.5,labs=('',''))+f'\n\\draw[thick] ({cx:.3f},{y-.25:.3f}) -- ({cx:.3f},{y+.25:.3f});\n\\node[font=\\small\\bfseries] at ({cx+hw+.3:.3f},{y:.3f}) {{K}};'
SK3=tikz_svg(HEAD+'\n'.join(o)+TAIL)
ic,ad=onc([
 dict(t='K ucu N kutbudur.',v=True,ok='İki mıknatıs birbirini itiyor; bakışan uçlar aynı cinstir. Sol mıknatısın sağ ucu S olduğundan sağ mıknatısın sol ucu da S, K ucu ise N kutbudur.',exc='İtmeyi görmesine karşın bakışan uçların farklı cins olduğunu varsaymış ve K ucunu S sanmış.'),
 dict(t='Sağ mıknatıs soldakinden daha güçlü olsaydı, sağ mıknatısa etki eden itme kuvveti soldakine etki edenden büyük olurdu.',v=False,ok='İki mıknatısın birbirine uyguladığı kuvvetler etki–tepki çiftidir; mıknatısların güçleri farklı olsa da kuvvetlerin büyüklükleri eşittir.',inc='Güçlü mıknatısın daha büyük kuvvet uyguladığını sanmış; etki–tepki kuvvetlerinin eşit büyüklükte olduğunu atlamış.'),
 dict(t='Sağ mıknatıs uçları yer değiştirecek biçimde ters çevrilip yeniden asılsaydı, mıknatıslar birbirine doğru yaklaşırdı.',v=True,ok='Ters çevrilince bakışan uçlar farklı cins olur; mıknatıslar birbirini çeker ve ipler birbirine doğru sapar.',exc='Ters çevirmenin kuvvetin yönünü değiştirmeyeceğini, mıknatısların yine uzaklaşacağını sanmış.')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],
 'Şekildeki gibi, eşit uzunlukta iplerle tavandan yatay olarak asılan iki özdeş görünümlü çubuk mıknatıs birbirine dokunmadan dengede durmaktadır. Soldaki mıknatısın kutupları şekilde gösterilmiştir; sağdaki mıknatısın yalnız sağ ucu K ile işaretlenmiştir. İplerin düşeyle yaptığı açılar, mıknatıslar arasındaki etkileşmenin sonucudur. Ortamda başka mıknatıs ya da demir yoktur ve Yer’in manyetik alanı ihmal edilmektedir.\nBuna göre,')
q('0003',ad+[A('Sonuç','I ve III doğrudur.','I ve III')],tipId='fz-mn2-asili',tip='İpe asılı mıknatıslar',z='orta',alt='Mıknatıs ve Manyetik Alan',kaz='İpe asılı mıknatısların dengedeki konumundan kutup cinslerini ve kuvvetlerin özelliklerini yorumlar.',kalip='öncüllü',
 kart='K-FZMN2-03 (ipe asılı mıknatıslar) · itme, etki–tepki, ters çevirme',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Mıknatısların birbirine uyguladığı kuvvetin yönünü şekildeki duruma bakarak belirle.'],
 bilgi=[B('Mıknatısların birbirine etkisi','aynı cins kutuplar birbirini iter, farklı cins kutuplar çeker; iki mıknatıs birbirine eşit büyüklükte ve zıt yönlü kuvvet uygular. Örnek: iki mıknatısın N uçları karşılıklı getirilirse ikisi de birbirinden uzaklaşmaya çalışır')],
 puf='Mıknatıslar birbirine eşit büyüklükte ve zıt yönlü kuvvet uygular; itme aynı cins, çekme farklı cins kutupların bakışmasıyla olur.',sekil=SK3,**ic)

# =================== 04 · geçici mıknatıslanma · orta ===================
kartla('04','Geçici mıknatıslanma','Mıknatısa değen yumuşak demir mıknatıslanır; mıknatısa değen ucu karşıt kutup olur ve mıknatıs uzaklaşınca özelliğini kaybeder; çelik ise mıknatıslığını korur.','Mıknatıslanan çivinin mıknatısa değen ucunu aynı cins kutup sanmak; yumuşak demirin de kalıcı mıknatıs olacağını düşünmek.','orta','öncüllü',4,'fz-mn2-gecici','Geçici mıknatıslanma')
o=[]
o.append('\\draw[thick] (-1,5.0) -- (1,5.0);')
o.append('\\draw[thick] (0,5.0) -- (0,4.4);')
o.append('\\draw[thick,fill=gray!40] (-.4,3.5) rectangle (.4,4.4);\\draw[thick] (-.4,2.6) rectangle (.4,3.5);')
o.append('\\node[font=\\small\\bfseries] at (0,3.95) {N};\\node[font=\\small\\bfseries] at (0,3.05) {S};')
o.append('\\draw[thick,fill=gray!65] (-.12,1.2) rectangle (.12,2.6);\\draw[thick,fill=gray!65] (-.12,1.2) -- (0,.95) -- (.12,1.2) -- cycle;')
for i in range(3):
    yy=.35-i*.38
    o.append(f'\\draw[thick,rounded corners=1.5pt,fill=white] (-.25,{yy-.42:.2f}) rectangle (.25,{yy+.42:.2f});')
o[-3:]=[]  # sade: tek bir zincir yerine üç toplu iğne
for yy in (.95,.5,.05):
    o.append(f'\\draw[thick] (0,{yy:.2f}) -- (0,{yy-.42:.2f});\\fill (0,{yy:.2f}) circle (2.6pt);')
o.append('\\node[anchor=west,font=\\small] at (.7,1.95) {demir çivi};\\node[anchor=west,font=\\small] at (.7,-.4) {toplu iğneler};')
SK4=tikz_svg(HEAD+'\n'.join(o)+TAIL)
ic,ad=onc([
 dict(t='Çivinin mıknatısa değen ucu N, alt ucu S kutbu özelliği kazanır.',v=True,ok='Mıknatısın S kutbuna değen uç karşıt kutba, yani N kutbuna dönüşür; çivinin diğer ucu S olur.',exc='Çivinin mıknatıslanmayacağını ya da kutuplarının ters oluşacağını (mıknatısa değen ucun S olacağını) sanmış.'),
 dict(t='Mıknatıs çividen uzaklaştırılırsa çivi mıknatıslığını büyük ölçüde yitirir ve toplu iğneler düşer.',v=True,ok='Yumuşak demir geçici mıknatıs gibi davranır; mıknatıs uzaklaşınca özelliğini büyük ölçüde kaybeder ve iğneler düşer.',exc='Yumuşak demirin de mıknatıslığını kalıcı olarak koruyacağını sanmış.'),
 dict(t='Çivi yerine aynı boyutta çelik bir çubuk kullanılsaydı, mıknatıs uzaklaştırıldıktan sonra çubuk uzun süre mıknatıslığını korurdu.',v=True,ok='Çelik kalıcı mıknatıs olabilen bir maddedir; mıknatıslanınca özelliğini uzun süre korur.',exc='Her demirli maddenin mıknatıs uzaklaşınca aynı biçimde özelliğini yitireceğini sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III'],
 'Bir öğrenci şekildeki düzenekte, tavana asılmış çubuk mıknatısın alt ucuna yumuşak demirden yapılmış bir çivinin üst ucunu değdiriyor; çivinin alt ucuna da küçük demir toplu iğneler birbirine tutunarak asılı kalıyor. Öğrenci, çivinin ve toplu iğnelerin davranışını mıknatısın yanındayken ve mıknatıs uzaklaştırıldığında yorumlamak istiyor. Ortamda başka mıknatıs yoktur.\nBuna göre,')
q('0004',[A('Geçici mıknatıslanmayı hatırla','Mıknatısa yaklaşan demir mıknatıslanır; mıknatısa yakın uç karşıt kutup olur.','demir → mıknatıslanır')]+ad+[A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],tipId='fz-mn2-gecici',tip='Geçici mıknatıslanma',z='orta',alt='Mıknatıs ve Manyetik Alan',kaz='Mıknatısa değen demirin geçici mıknatıslanmasını ve çelikle farkını değerlendirir.',kalip='öncüllü',
 kart='K-FZMN2-04 (geçici mıknatıslanma) · çivi, toplu iğne ve çelik çubuk',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Mıknatısın S kutbuna değen demirin o ucunda hangi kutup oluştuğunu ve mıknatıs gidince ne olacağını düşün.'],
 bilgi=[B('Mıknatıslanma','demir, nikel, kobalt ve bunların alaşımları mıknatıs tarafından çekilir ve mıknatıslanabilir; yumuşak demir geçici, çelik kalıcı olarak mıknatıslanır. Örnek: yumuşak demir bir çubuk mıknatıs uzaklaşınca toplu iğneleri tutamaz')],
 puf='Mıknatısa değen demirin o ucunda karşıt kutup oluşur; yumuşak demir özelliğini kaybeder, çelik korur.',sekil=SK4,**ic)

# =================== 05 · maddeler tablosu · orta ===================
kartla('05','Manyetik maddeler','Mıknatıs değerken iğne çeken ama uzaklaşınca çekmeyen madde yumuşak demirdir (geçici); her iki durumda çeken çeliktir (kalıcı); hiç çekmeyen madde manyetik değildir.','Çekmeyen maddeyi bile mıknatıslanabilir sanmak; geçici ve kalıcı mıknatıslanmayı karıştırmak.','orta','tablo',3,'fz-mn2-maddeler','Manyetik maddeler')
SK5=tablo_svg(['Çubuk','Mıknatıs değerken','Mıknatıs uzaklaştırılınca'],[['K','İğne çekiyor','İğne çekmiyor'],['L','İğne çekiyor','İğne çekiyor'],['M','İğne çekmiyor','İğne çekmiyor']])
q('0005',[A('M çubuğunu belirle','Mıknatıs değse bile iğne çekmeyen madde manyetik madde değildir.','M → bakır'),
 A('K çubuğunu belirle','K yalnız mıknatıs değerken iğne çeker; özelliği geçicidir.','K → yumuşak demir'),
 A('L çubuğunu belirle','L mıknatıs uzaklaşınca da iğne çeker; mıknatıslığı kalıcıdır.','L → çelik'),
 A('Sonuç','Sıra K, L, M.','Yumuşak demir – çelik – bakır')],
 tipId='fz-mn2-maddeler',tip='Manyetik maddeler',z='orta',alt='Mıknatıs ve Manyetik Alan',kaz='Geçici ve kalıcı mıknatıslanan maddelerle manyetik olmayan maddeleri gözleme dayanarak ayırt eder.',kalip='tablo',
 kart='K-FZMN2-05 (manyetik maddeler) · yumuşak demir, çelik, bakır',
 metin='Bir öğrenci, aynı boyutlardaki K, L ve M çubuklarının hangi maddeden yapıldığını bulmaya çalışıyor. Çubuklar yumuşak demir, çelik ve bakırdır; ancak hangisinin hangisi olduğu bilinmiyor. Öğrenci her çubuğun bir ucuna güçlü bir mıknatısın kutbunu değdiriyor ve çubuğun diğer ucunun toplu iğne çekip çekmediğine bakıyor. Sonra mıknatısı çubuktan uzaklaştırıp aynı gözlemi yineliyor. Gözlemler tabloda verilmiştir.\nBuna göre, K, L ve M çubukları sırasıyla aşağıdakilerden hangisi olabilir?',
 sekil=SK5,dogru='Yumuşak demir – çelik – bakır',sira=['Çelik – yumuşak demir – bakır','Yumuşak demir – bakır – çelik','Yumuşak demir – çelik – bakır','Bakır – yumuşak demir – çelik','Çelik – bakır – yumuşak demir'],
 yan=[('Çelik – yumuşak demir – bakır','Geçici ve kalıcı mıknatıslanmayı ters yorumlamış: mıknatıs uzaklaşınca iğne çekmeyen K’yi çelik, çekmeye devam eden L’yi yumuşak demir sanmış.','bilgi'),
  ('Yumuşak demir – bakır – çelik','L her iki durumda da iğne çektiği hâlde L’yi bakır, hiç çekmeyen M’yi çelik sanmış.','dikkat'),
  ('Bakır – yumuşak demir – çelik','Mıknatıs değerken iğne çeken K’yi bakır sanmış; bakır mıknatıslanmadığından iğne çekmez.','bilgi'),
  ('Çelik – bakır – yumuşak demir','Hiçbir durumda iğne çekmeyen M’yi yumuşak demir, her iki durumda çeken L’yi bakır sanmış.','bilgi')],
 istenen='K, L ve M çubuklarının hangi maddeden yapılmış olabileceği.',ip=['Hangi çubuğun mıknatıs uzaklaşınca da özelliğini koruduğuna ve hangisinin hiç mıknatıslanmadığına bak.'],
 bilgi=[B('Geçici ve kalıcı mıknatıs','yumuşak demir mıknatısın yanındayken mıknatıslanır, uzaklaşınca özelliğini yitirir (geçici); çelik mıknatıslığını uzun süre korur (kalıcı); bakır ve alüminyum gibi maddeler mıknatıslanmaz. Örnek: çelik makas bir mıknatısa sürtülünce toplu iğne çekebilir')],
 puf='Mıknatıs gidince de çeken madde kalıcı mıknatıstır (çelik), yalnızca mıknatıs yanındayken çeken madde geçicidir (yumuşak demir), hiç çekmeyen madde manyetik değildir.')

# =================== 06 · Dünya'nın manyetik alanı · orta ===================
kartla('06','Dünya’nın manyetik alanı','Dünya büyük bir mıknatıs gibidir; coğrafi kuzeye yakın manyetik kutup mıknatıs olarak S kutbudur; manyetik eksenin coğrafi eksenle çakışmaması pusulada sapma açısı doğurur.','Coğrafi kuzeye yakın kutbu N kutbu sanmak; pusula iğnesinin tam coğrafi kuzeyi gösterdiğini düşünmek.','orta','öncüllü',4,'fz-mn2-dunya','Dünya’nın manyetik alanı')
Re=1.5; al=radians(11); a=(-sin(al),cos(al)); nv=(cos(al),sin(al))
o=[]
o.append(f'\\draw[dashed,gray] (0,-2.35) -- (0,2.35);')
for c in (2.6,3.4,4.4):
    for sg in (1,-1):
        th=[radians(t) for t in range(180,0,-2)]; pts=[]
        for t in th:
            r=c*sin(t)**2
            if r>Re+.04 and sin(t)>0: pts.append((r*(cos(t)*a[0]+sg*sin(t)*nv[0]),r*(cos(t)*a[1]+sg*sin(t)*nv[1])))
        # yönlendir: güneyden kuzeye (θ azalır) → liste zaten θ=180°→0°
        o.append(f'\\draw[line width=.55pt,{MARK}] '+' -- '.join(p2(*pp) for pp in pts)+';')
o.append(f'\\draw[thick,fill=white] (0,0) circle ({Re});')
o.append(f'\\draw[line width=7pt,gray!55,line cap=butt] {p2(-.95*a[0],-.95*a[1])} -- {p2(.95*a[0],.95*a[1])};')
o.append('\\node[font=\\small] at (0,2.65) {Coğrafi kuzey};\\node[font=\\small] at (0,-2.65) {Coğrafi güney};')
pa=radians(15); o.append(f'\\fill ({Re*sin(pa):.3f},{Re*cos(pa):.3f}) circle (2.4pt);\\node[font=\\small\\bfseries] at ({(Re+.3)*sin(pa):.3f},{(Re+.3)*cos(pa):.3f}) {{P}};')
o.append('\\node[font=\\footnotesize,align=center] at (.85,-.15) {çubuk\\\\mıknatıs};')
SK6=tikz_svg(HEAD+'\n'.join(o)+TAIL)
ic,ad=onc([
 dict(t='Coğrafi kuzey kutbuna yakın manyetik kutup, mıknatıs kutbu olarak S kutbudur.',v=True,ok='Alan çizgileri mıknatısın dışında N kutbundan S kutbuna gider; çizgiler coğrafi kuzeye doğru ilerleyip oraya girdiğinden kuzeye yakın manyetik kutup S kutbudur.',exc='Coğrafi kuzeye yakın manyetik kutbun N kutbu olduğunu sanmış; oysa pusulanın N ucunu çeken bu kutup S kutbudur.'),
 dict(t='Pusulanın gösterdiği yön ile coğrafi kuzey arasındaki açı, manyetik eksenin coğrafi eksenle çakışmamasından kaynaklanır.',v=True,ok='Manyetik kutuplar coğrafi kutuplarla çakışmadığından pusulanın gösterdiği yön coğrafi kuzeyden bir miktar sapar.',exc='Pusulanın her yerde tam coğrafi kuzeyi göstereceğini, açının başka bir nedenle oluştuğunu sanmış.'),
 dict(t='Pusulanın S ucu, coğrafi kuzey kutbuna yakın olan manyetik kutba doğru yönelir.',v=False,ok='Pusulanın N ucu, kuzeye yakın manyetik kutba (S kutbuna) yönelir; S ucu güneyi gösterir.',inc='Pusulanın S ucunun kuzeye döneceğini sanmış; oysa kuzeyi gösteren uç iğnenin N ucudur.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],
 'Şekilde, Dünya’nın manyetik alanını açıklamak için kullanılan çubuk mıknatıs modeli ve çevresindeki manyetik alan çizgileri verilmiştir; çubuğun kutupları işaretlenmemiştir. Yer yüzeyindeki P noktasında bulunan bir öğrenci, serbestçe dönebilen küçük bir pusulanın N ucunun yaklaşık olarak coğrafi kuzeyi gösterdiğini, ancak gösterilen yön ile coğrafi kuzey arasında küçük bir açı kaldığını görüyor.\nBuna göre,')
q('0006',ad+[A('Sonuç','I ve II doğrudur.','I ve II')],tipId='fz-mn2-dunya',tip='Dünya’nın manyetik alanı',z='orta',alt='Pusula ve Dünya’nın Manyetik Alanı',kaz='Dünya’nın manyetik alanında coğrafi ve manyetik kutupları ve pusulanın sapmasını yorumlar.',kalip='öncüllü',
 kart='K-FZMN2-06 (Dünya’nın manyetik alanı) · eğik manyetik eksen, pusulanın sapması',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Şekildeki alan çizgilerinin okunun yönüne bakarak coğrafi kuzeye yakın manyetik kutbun mıknatıs kutbu olarak hangisi olduğunu bul.'],
 bilgi=[B('Dünya’nın manyetik alanı','Dünya büyük bir çubuk mıknatıs gibidir; coğrafi kuzeye yakın manyetik kutup mıknatıs olarak S, coğrafi güneye yakın olan N kutbudur. Manyetik ve coğrafi kutuplar çakışmaz; aradaki açıya sapma denir. Örnek: iki mıknatısın zıt kutupları birbirini çeker')],
 puf='Pusulanın N ucu Dünya’nın kuzeye yakın manyetik (S) kutbunu gösterir; kutupların çakışmaması sapma açısını doğurur.',sekil=SK6,**ic)

# =================== 07 · Oersted · zor ===================
kartla('07','Akım taşıyan telin pusulaya etkisi','Pusulanın üstünden ve altından geçen telde alan zıt yönlere doğrudur; akım yönü değişince sapma yönü değişir; akım artarsa sapma artar.','Akım yönüne bakmadan sapma yönünü tahmin etmek; telin üstünde ve altında aynı yönde sapma olacağını sanmak.','zor','öncüllü',4,'fz-mn2-oersted','Akım taşıyan telin pusulaya etkisi')
o=[]
o.append('\\draw[thick,fill=white] (0,0) circle (.85);')
o.append('\\draw[thick,fill=gray!60] (-.14,0) -- (0,.7) -- (.14,0) -- cycle;\\draw[thick,fill=white] (-.14,0) -- (0,-.7) -- (.14,0) -- cycle;')
o.append('\\draw[line width=2.2pt,gray!80] (0,-2.0) -- (0,2.1);')
o.append('\\draw[-{Stealth[length=3mm,width=2.6mm]},line width=1.6pt,vurgu] (0,1.2) -- (0,1.95);\\node[vurgu,font=\\small\\bfseries] at (.4,1.7) {$I$};')
o.append('\\node[font=\\footnotesize\\bfseries] at (.38,.48) {N};\\node[font=\\small,anchor=west] at (.3,-1.4) {tel};\\node[font=\\small] at (-1.55,-.7) {pusula};\\draw (-1.2,-.55) -- (-.7,-.15);')
o.append('\\draw[-{Stealth[length=2mm]},thick] (2.3,-1.0) -- (2.3,.0);\\draw[-{Stealth[length=2mm]},thick] (2.3,-1.0) -- (3.3,-1.0);\\node[font=\\small] at (2.3,.3) {Kuzey};\\node[font=\\small] at (3.75,-1.0) {Doğu};')
SK7=tikz_svg(HEAD+'\n'.join(o)+TAIL)
ic,ad=onc([
 dict(t='Akım yönü ters çevrilirse iğnenin N ucu, ilk sapmanın tersi yönünde, doğuya doğru sapar.',v=True,ok='Tel pusulanın üstünde ve akım kuzeye doğrudur: sağ el kuralıyla telin altında alan batıya yöneliktir, N ucu batıya sapar. Akım ters çevrilince alan doğuya döner ve N ucu doğuya sapar.',exc='Akım yönünün değişmesinin alanın ve iğnenin sapma yönünü ters çevirdiğini atlamış.'),
 dict(t='Akım yönü değiştirilmeden tel pusulanın altından geçirilirse iğnenin N ucu yine batıya doğru sapar.',v=False,ok='Telin üstünde ve altında alan zıt yönlerdedir; tel pusulanın altından geçerse iğnenin N ucu batıya değil doğuya sapar.',inc='Telin hangi tarafta olduğunun alan yönünü değiştirmediğini sanmış; telin altında ve üstünde alan zıt yönlüdür.'),
 dict(t='Telden geçen akımın şiddeti artırılırsa iğnenin sapma miktarı artar.',v=True,ok='Akım arttıkça telin pusula bulunduğu yerde oluşturduğu alan güçlenir ve iğne Yer’in alanına göre daha çok sapar.',exc='Akım şiddetinin sapma miktarını etkilemediğini, yalnızca akımın yönüne bağlı olduğunu sanmış.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],
 'Bir öğrenci, Yer’in manyetik alanında serbestçe dönebilen küçük bir pusulanın N ucunun (şekilde koyu uç) kuzeyi gösterdiğini gözlüyor. Sonra uzun bir bakır teli kuzey–güney doğrultusunda, pusulanın hemen üstünden ve iğneye paralel olacak biçimde gerip bir üretece bağlıyor. Şekil, düzeneğin yukarıdan görünüşüdür. Telden şekildeki yönde akım geçince iğne başlangıç konumundan sapıyor. Pusula ile tel arasındaki uzaklık değiştirilmiyor ve Yer’in manyetik alanı ihmal edilmiyor.\nBuna göre,')
q('0007',[A('Sağ el kuralını uygula','Başparmak kuzeyi gösterirken parmaklar telin altında batı yönüne kıvrılır.','altta alan batıya')]+ad+[A('Sonuç','I ve III doğrudur.','I ve III')],tipId='fz-mn2-oersted',tip='Akım taşıyan telin pusulaya etkisi',z='zor',alt='Akım ve Manyetik Alan',kaz='Akım taşıyan telin pusula iğnesini saptırmasını akım yönü, tel konumu ve akım şiddetiyle ilişkilendirir.',kalip='öncüllü',
 kart='K-FZMN2-07 (Oersted deneyi) · telin üstü, altı, akım yönü ve şiddeti',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Telin pusulaya göre üstte mi altta mı olduğunu ve akımın yönünü sağ el kuralıyla alanın yönüne çevir.'],
 bilgi=[B('Akımın manyetik etkisi','akım taşıyan telin çevresinde manyetik alan oluşur; sağ elin başparmağı akım yönünü gösterirse kıvrılan parmaklar alanın yönünü gösterir. Akım yönü değişince alan yönü değişir, akım arttıkça alan güçlenir. Örnek: akım artarsa pusula iğnesindeki sapma da büyür')],
 puf='Telin üstünde ve altında alan zıt yönlüdür; akım yönü alan yönünü, akım şiddeti sapma miktarını belirler.',sekil=SK7,**ic)

# =================== 08 · bobinin kutupları · orta ===================
kartla('08','Akım geçen bobinin kutupları','Sağ el kuralıyla bobinin hangi ucu N ise oradan alan çizgileri çıkar; bobinin dışında eksen üzerinde alan çizgileri N’den S’ye gider.','Eksen üzerinde bobinin iki yanında pusulaların zıt yön göstereceğini sanmak; akımın yönünü ters uygulamak.','orta','şekilli',4,'fz-mn2-bobin','Akım geçen bobinin kutupları')
n8,R8,p8,d8=5,.7,.55,.4
ct,xl,xr,Nuc=coil(0,n8,R8,p8,d8,True); assert Nuc=='sol'
kx=-1.2; lx=xr+1.15
o=[ct,compass(kx,0,'K'),compass(lx,0,'L')]
SK8=tikz_svg(HEAD+'\n'.join(o)+TAIL)
q('0008',[A('Bobinin kutuplarını bul','Pilin + ucu sol taraftadır; önden geçen kalın sarımlarda akım yukarı yönlüdür. Sağ el kuralında parmaklar akım yönünde kıvrılınca başparmak sola bakar.','sol uç N, sağ uç S'),
 A('K noktasındaki alan','K, N kutbunun solundadır; dışarıda alan N kutbundan uzağa doğrudur.','K: ←'),
 A('L noktasındaki alan','L, S kutbunun sağındadır; alan çizgileri S kutbuna girer, yani sola doğrudur.','L: ←'),
 A('Sonuç','İki pusulanın N uçları da sola bakar.','K: ←, L: ←')],
 tipId='fz-mn2-bobin',tip='Akım geçen bobinin kutupları',z='orta',alt='Akım ve Manyetik Alan',kaz='Akım geçen bobinin kutuplarını sağ el kuralıyla belirleyip eksendeki pusulaların yönünü bulur.',kalip='şekilli',
 kart='K-FZMN2-08 (bobinin kutupları) · eksen üzerinde iki pusula',
 metin='Bir öğrenci, yalıtkan telle sarılmış bir bobini şekildeki gibi bir pile bağlıyor; pilin uzun çizgisi artı (+) kutbunu gösterir. Bobinin önden geçen sarımları kalın, arkadan geçenler ince kesikli çizgilerle çizilmiştir. Devre kapatıldıktan sonra bobinin eksenindeki K ve L noktalarına küçük birer pusula konuyor ve iğneler dengeye geliyor. Yer’in manyetik alanı ihmal edilmektedir.\nBuna göre, pusulaların N uçları K ve L noktalarında sayfa düzleminde hangi yönü gösterir?',
 sekil=SK8,dogru='K: ←, L: ←',sira=['K: →, L: →','K: ←, L: ←','K: →, L: ←','K: ←, L: →','K: ↑, L: ↓'],
 yan=[('K: →, L: →','Akımın yönünü ters uygulayıp bobinin sol ucunu S sanmış; iki pusulayı da bu kutba göre döndürmüş.','bilgi'),
  ('K: →, L: ←','Bobinin uçlarını doğru bulmuş; ancak K’de N ucunun N kutbuna doğru döneceğini sanmış (aynı cins çeker).','bilgi'),
  ('K: ←, L: →','N ucunun yakın olduğu kutuptan hep uzağa döneceğini sanmış; oysa L’de N ucu S kutbuna doğru (sola) döner.','bilgi'),
  ('K: ↑, L: ↓','Bobin ekseni üzerindeki noktalarda alanı eksene dik sanmış; eksen üzerinde alan eksen doğrultusundadır.','dikkat')],
 istenen='K ve L noktalarındaki pusula iğnelerinin N uçlarının yönü.',ip=['Bobinin hangi ucunun N olduğunu akım yönünden bul.'],
 bilgi=[B('Bobinin kutupları','sağ elin parmakları bobinde akım yönünde kıvrılınca başparmak bobinin N kutbunu gösterir. Mıknatısın dışında alan çizgileri N’den S’ye gider. Örnek: N ucu sağda olan bir bobinin sağındaki pusulanın N ucu sağa bakar')],
 puf='Bobinin N ucunu sağ el kuralı verir; eksen üzerinde bobinin dışında alan çizgileri N’den S’ye doğrudur.')

# =================== 09 · elektromıknatıs gücü · orta ===================
kartla('09','Elektromıknatısın gücü','Akım şiddeti eşitken sarım sayısı fazla olan ve demir çekirdekli elektromıknatıs daha çok toplu iğne çeker.','Çekirdeğin ya da sarım sayısının etkisini atlamak; akım eşitse hepsinin aynı gücte olacağını sanmak.','orta','şekilli',3,'fz-mn2-elgucu','Elektromıknatısın gücü')
o=[]
def elm(x,n,core,lab):
    s=''
    if core: s+=f'\\draw[thick,fill=gray!55] ({x-.15:.2f},0) rectangle ({x+.15:.2f},2.2);\n'
    y0=1.1-(n*.2)/2+.1
    for i in range(n): s+=f'\\draw[thick] ({x-.34:.2f},{y0+i*.2:.2f}) -- ({x+.34:.2f},{y0+i*.2+.12:.2f});\n'
    s+=f'\\node[font=\\small\\bfseries] at ({x:.2f},-.4) {{{lab}}};'
    return s
o.append(elm(0,4,True,'K')+elm(2.6,8,True,'L')+elm(5.2,4,False,'M'))
SK9=tikz_svg(HEAD+'\n'.join(o)+TAIL)
q('0009',[A('K ile M’yi karşılaştır','Sarım sayısı ve akım eşit; yalnız K’de demir çekirdek var. Demir çekirdek alanı güçlendirir.','n_K > n_M'),
 A('K ile L’yi karşılaştır','İkisinde de çekirdek demirdir, akım eşittir; L’nin sarım sayısı fazladır.','n_L > n_K'),
 A('Sonuç','Çekilen toplu iğne sayıları sıralanır.','n_L > n_K > n_M')],
 tipId='fz-mn2-elgucu',tip='Elektromıknatısın gücü',z='orta',alt='Akım ve Manyetik Alan',kaz='Elektromıknatısın gücünü sarım sayısı ve çekirdek yönünden karşılaştırır.',kalip='şekilli',
 kart='K-FZMN2-09 (elektromıknatısın gücü) · sarım sayısı ve demir çekirdek',
 metin='Üç öğrenci, aynı kalınlıkta yalıtkan telle K, L ve M elektromıknatıslarını yapıyor; sarım sayıları ve çekirdekleri şekilde görülmektedir (çekirdek varsa demir çubuktur). Her elektromıknatıs, bir reosta yardımıyla akım şiddeti 1 A’e ayarlanmış ayrı bir devreye bağlanıyor. Ardından elektromıknatısların her biri, aynı büyüklükteki çok sayıda toplu iğnenin bulunduğu kaba ayrı ayrı yaklaştırılıyor ve çektiği toplu iğne sayıları (n_K, n_L, n_M) sayılıyor.\nBuna göre, n_K, n_L ve n_M arasındaki ilişki aşağıdakilerden hangisidir?',
 sekil=SK9,dogru='n_L > n_K > n_M',sira=['n_K > n_L > n_M','n_L > n_M > n_K','n_K = n_L > n_M','n_L > n_K > n_M','n_K = n_L = n_M'],
 yan=[('n_K > n_L > n_M','Sarım sayısı arttıkça alanın zayıflayacağını sanmış; oysa sarım sayısı arttıkça elektromıknatıs güçlenir.','bilgi'),
  ('n_L > n_M > n_K','Demir çekirdeğin alanı zayıflattığını sanmış; çekirdeksiz M’yi çekirdekli K’den güçlü almış.','bilgi'),
  ('n_K = n_L > n_M','Akım eşit olduğundan sarım sayısının önemsiz olduğunu sanmış; yalnız çekirdeğin etkisini görmüş.','bilgi'),
  ('n_K = n_L = n_M','Akım şiddetleri eşit olduğu için üç elektromıknatısın da eşit güçte olacağını sanmış; sarım sayısı ve çekirdeği atlamış.','dikkat')],
 istenen='Çekilen toplu iğne sayılarının karşılaştırması.',ip=['Akım eşitken elektromıknatısın gücünü hangi iki etkenin değiştirdiğini düşün ve şekilde bu etkenleri karşılaştır.'],
 bilgi=[B('Elektromıknatısın gücü','akım şiddeti, sarım sayısı ve demir çekirdek elektromıknatısın gücünü artırır. Örnek: akım ve sarım sayısı aynı olan iki bobinden demir çekirdekli olanı daha çok çivi çeker')],
 puf='Akım eşitken elektromıknatısın gücü sarım sayısı ve demir çekirdekle artar.')

# =================== 10 · vinç · kolay ===================
kartla('10','Elektromıknatıslı vinç','Elektromıknatıs yalnızca manyetik maddeleri (demir, nikel, kobalt) çeker; akım kesilince mıknatıslığı yitirir ve cisimler düşer.','Her metalin mıknatıs tarafından çekileceğini sanmak; akım kesilince de çekimin sürdüğünü düşünmek.','kolay','şekilli',3,'fz-mn2-vinc','Elektromıknatıslı vinç')
o=[]
o.append('\\draw[thick] (-1.9,4.6) -- (8.1,4.6);')
o.append('\\draw[thick] (3.1,4.6) -- (3.1,3.9);\\draw[thick,fill=gray!40] (1.6,3.0) rectangle (4.6,3.9);\\node[font=\\small] at (3.1,3.45) {elektromıknatıs};')
o.append('\\draw[thick] (-1.9,0) -- (8.1,0);')
xs=[-.9,1.1,3.1,5.1,7.1]
o.append(f'\\draw[thick,fill=gray!65] ({xs[0]-.12:.2f},.12) rectangle ({xs[0]+.12:.2f},1.15);\\draw[thick,fill=gray!65] ({xs[0]-.25:.2f},1.15) rectangle ({xs[0]+.25:.2f},1.3);')
o.append(f'\\draw[thick,fill=gray!65] ({xs[1]:.2f},.4) circle (.32);\\draw[thick,fill=white] ({xs[1]:.2f},.4) circle (.12);')
o.append(f'\\draw[thick,fill=gray!8] ({xs[2]-.35:.2f},.1) rectangle ({xs[2]+.35:.2f},.95);\\draw[thick,fill=gray!8] ({xs[2]:.2f},.95) ellipse (.35 and .09);')
o.append(f'\\draw[thick,decorate,decoration={{snake,amplitude=1.2mm,segment length=4mm}}] ({xs[3]-.55:.2f},.5) -- ({xs[3]+.55:.2f},.5);')
o.append(f'\\draw[thick,fill=white] ({xs[4]:.2f},.4) circle (.3);')
for x_,lb in zip(xs,['demir çivi','demir somun','alüminyum kutu','bakır tel','cam bilye']):
    o.append(f'\\node[font=\\footnotesize] at ({x_:.2f},-.4) {{{lb}}};')
SK10=tikz_svg(HEAD+'\n'.join(o)+TAIL)
q('0010',[A('Çekilen cisimleri bul','Elektromıknatıs yalnız manyetik maddeleri çeker; çivi ve somun demirdendir.','demir çivi, demir somun'),
 A('Alüminyum, bakır ve cam','Bunlar manyetik madde değildir; çekilmez.','çekilmezler'),
 A('Anahtar açılınca','Akım kesilince elektromıknatıs özelliğini kaybeder; çekilen cisimler düşer.','ikisi de düşer'),
 A('Sonuç','Doğru seçenek belirlenir.','Demir çivi ve demir somun; ikisi de düşer')],
 tipId='fz-mn2-vinc',tip='Elektromıknatıslı vinç',z='kolay',alt='Manyetizmanın Uygulamaları',kaz='Elektromıknatıslı vincin hangi cisimleri kaldırdığını ve anahtar açılınca ne olduğunu açıklar.',kalip='şekilli',
 kart='K-FZMN2-10 (elektromıknatıslı vinç) · manyetik olan ve olmayan cisimler',
 metin='Bir hurda tesisinde, elektromıknatıslı bir vinç şekildeki gibi karışık hurda yığınının üzerine getiriliyor. Vincin elektromıknatısı, anahtar kapatıldığında akım geçen, yumuşak demir çekirdekli büyük bir bobindir ve akım kesilince mıknatıslığını yitirir. Operatör anahtarı kapatıp elektromıknatısı yığına indiriyor, kaldırıp taşıma alanına getiriyor ve orada anahtarı açıyor. Yığındaki cisimler şekilde adlarıyla gösterilmiştir; cisimlerin hiçbiri önceden mıknatıslanmış değildir.\nBuna göre, anahtar kapatıldığında elektromıknatıs hangi cisimleri kaldırır ve anahtar açıldığında bu cisimlere ne olur?',
 sekil=SK10,dogru='Demir çivi ve demir somun; ikisi de düşer',sira=['Demir çivi ve demir somun; ikisi de düşer','Demir çivi, demir somun ve alüminyum kutu; hepsi düşer','Bakır tel ve alüminyum kutu; ikisi de düşer','Demir çivi ve demir somun; ikisi de havada kalır','Bütün cisimler kalkar; hepsi düşer'],
 yan=[('Demir çivi, demir somun ve alüminyum kutu; hepsi düşer','Alüminyum gibi metallerin de mıknatıs tarafından çekileceğini sanmış; yalnız demir, nikel ve kobalt çekilir.','bilgi'),
  ('Bakır tel ve alüminyum kutu; ikisi de düşer','Elektriği ileten metallerin mıknatıs tarafından çekildiğini, demirin ise çekilmediğini sanmış.','bilgi'),
  ('Demir çivi ve demir somun; ikisi de havada kalır','Akım kesilince de elektromıknatısın özelliğini koruyacağını sanmış; oysa anahtar açılınca elektromıknatıs mıknatıslığını kaybeder.','bilgi'),
  ('Bütün cisimler kalkar; hepsi düşer','Mıknatısın her cismi çektiğini sanmış; alüminyum, bakır ve camı da kaldırılacak saymış.','bilgi')],
 istenen='Kaldırılan cisimler ve anahtar açıldığında olan durum.',ip=['Elektromıknatısın hangi tür maddeleri çektiğini ve akım kesilince ne olacağını düşün.'],
 bilgi=[B('Manyetik maddeler','demir, nikel ve kobalt mıknatıs tarafından çekilir; bakır, alüminyum, cam ve plastik çekilmez. Elektromıknatıs akım geçtiği sürece mıknatıs gibi davranır. Örnek: çelik bir toplu iğne mıknatısa yapışır, alüminyum folyo yapışmaz')],
 puf='Elektromıknatıs yalnız demir, nikel, kobalt gibi manyetik maddeleri çeker ve akım kesilince etkisini yitirir.')

# =================== 11 · maglev · orta ===================
kartla('11','Manyetik havada asılı tren','Havada asılı tren, ray ve tren mıknatıslarının bakışan aynı cins kutuplarının itmesiyle dengede durur; itme kuvveti ağırlığa eşittir; kutuplar çekmeye dönerse tren raya düşer.','Trenin raya çekimle yükseldiğini sanmak; yük artınca itme kuvvetinin değişmeyeceğini düşünmek.','zor','öncüllü',5,'fz-mn2-maglev','Manyetik havada asılı tren')
o=[]
for x in (-2.7,-.9,.9,2.7):
    o.append(f'\\draw[thick,fill=gray!12] ({x-.7:.2f},-.9) rectangle ({x+.7:.2f},0);\\draw[thick] ({x-.7:.2f},-.45) -- ({x+.7:.2f},-.45);\\node[font=\\small\\bfseries] at ({x:.2f},-.22) {{N}};\\node[font=\\small\\bfseries] at ({x:.2f},-.67) {{S}};')
o.append('\\draw[thick,rounded corners=6pt,fill=white] (-3.1,1.2) rectangle (3.1,2.4);')
for x in (-2.0,-.7,.7,2.0): o.append(f'\\draw[thick] ({x:.2f},1.8) circle (.22);')
for x in (-1.8,1.8):
    o.append(f'\\draw[thick,fill=gray!12] ({x-.6:.2f},.3) rectangle ({x+.6:.2f},1.2);\\draw[thick] ({x-.6:.2f},.75) -- ({x+.6:.2f},.75);\\node[font=\\small\\bfseries] at ({x:.2f},.52) {{K}};')
o.append('\\node[font=\\small,anchor=west] at (3.75,-.45) {ray};\\node[font=\\small,anchor=west] at (3.35,1.8) {tren};')
SK11=tikz_svg(HEAD+'\n'.join(o)+TAIL)
ic,ad=onc([
 dict(t='K kutbu N kutbudur.',v=True,ok='Tren ray ile temas etmeden havada duruyor; bu ancak itme ile mümkündür. Rayın üst yüzeyi N olduğundan bakışan K kutbu da N olmalıdır.',exc='Havada kalmayı çekme kuvvetine bağlayıp K kutbunun rayın üst kutbundan farklı (S) olduğunu sanmış.'),
 dict(t='Yolcular bindikten sonra tren yeniden durgun hâle geldiğinde, ray mıknatıslarının trene uyguladığı itme kuvveti yolcular binmeden öncekinden büyüktür.',v=True,ok='Durgun trende net kuvvet sıfırdır: itme kuvveti ağırlığa eşittir. Yolcularla ağırlık arttığından yeni dengede itme kuvveti de daha büyük olur (tren raya biraz yaklaşır).',exc='Dengede itme kuvvetinin ağırlıktan bağımsız olduğunu, yolcuların itme kuvvetini değiştirmeyeceğini sanmış.'),
 dict(t='Rayın mıknatısları ters çevrilerek üst yüzeyleri S yapılırsa tren havada durmaya devam eder.',v=False,ok='Rayın üst yüzeyi S olursa trenin N olan alt kutbuyla farklı cins kutuplar bakışır; çekme kuvveti oluşur ve tren raya düşer.',inc='Kutupları değiştirmenin trenin havada kalmasını etkilemeyeceğini sanmış; farklı cins kutuplar çeker, tren raya iner.')],
 ['Yalnız III','I ve II','I ve III','II ve III','I, II ve III'],
 'Bir manyetik havada asılı (maglev) tren modelinde, rayın içine yerleştirilmiş mıknatısların üst yüzeyleri şekildeki gibi aynı kutuptadır. Trenin altındaki iki özdeş mıknatısın ray yönüne bakan yüzeylerinin kutbu K ile gösterilmiştir. Tren hareketsizken ray ile temas etmeden, sabit yükseklikte havada durmaktadır; yolcular bindiğinde ise tren biraz alçalıp yeniden hareketsiz hâle gelmektedir. Ortamda başka mıknatıs yoktur ve havanın etkisi ihmal edilmektedir.\nBuna göre,')
q('0011',ad+[A('Sonuç','I ve II doğrudur.','I ve II')],tipId='fz-mn2-maglev',tip='Manyetik havada asılı tren',z='zor',alt='Manyetizmanın Uygulamaları',kaz='Manyetik havada asılı trenin dengede kalmasını mıknatıslar arasındaki itme kuvvetiyle açıklar.',kalip='öncüllü',
 kart='K-FZMN2-11 (maglev) · itme, denge, yük artışı, kutupların değişmesi',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Trenin havada hareketsiz kalmasının hangi tür kuvvetle ve hangi kutup durumuyla mümkün olduğunu düşün.'],
 bilgi=[B('Manyetik havada asılı tren','tren ile ray arasında aynı cins kutuplar bakıştığında oluşan itme kuvveti trenin ağırlığını dengeler ve tren raya değmeden havada kalır; sürtünme çok azalır. Örnek: iki mıknatısın N uçlarını birbirine yaklaştırınca elde hissedilen itme')],
 puf='Havada duran trende yukarı yönlü itme kuvveti ağırlığa eşittir; bakışan kutuplar aynı cinstir.',sekil=SK11,**ic)

# =================== 12 · elektrik zili · orta ===================
kartla('12','Elektrik zili','Zilde elektromıknatıs şeridi çekince devre açılır, akım kesilir, şerit esneyip geri döner ve devre yeniden kapanır; demir çekirdek çekme kuvvetini artırır.','Akımın şerit çekildiğinde de sürdüğünü sanmak; demir çekirdeğin etkisiz olduğunu düşünmek.','orta','öncüllü',4,'fz-mn2-zil','Elektrik zili')
ic,ad=onc([
 dict(t='Şerit kaseye vurduğu anda bobinden akım geçmeye devam eder ve elektromıknatıs şeridi kasede tutar.',v=False,ok='Şerit çekilince kontak vidasıyla teması kesilir; devre açılır, akım geçmez ve elektromıknatıs şeridi tutamaz.',inc='Şerit çekilirken de devrenin kapalı kaldığını sanmış; oysa şerit çekilince kontak açılır.'),
 dict(t='Şerit çekilip kontak vidasıyla teması kesildiğinde bobinden akım geçmez ve elektromıknatıs etkisini kaybeder.',v=True,ok='Temas kesilince devre açılır; akım geçmediği için elektromıknatıs şeridi bırakır ve şerit esneyerek geri döner.',exc='Temas kesilince de akımın sürdüğünü, elektromıknatısın etkisinin devam ettiğini sanmış.'),
 dict(t='Demir çekirdek çıkarılırsa elektromıknatısın şeridi çekme kuvveti azalır.',v=True,ok='Demir çekirdek bobinin manyetik alanını güçlendirir; çıkarılırsa alan ve şeridi çekme kuvveti azalır.',exc='Demir çekirdeğin elektromıknatısın gücüne katkısı olmadığını sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III'],
 'Elektrikli bir kapı zilinde; demir çekirdekli bir elektromıknatıs, ucunda çekiç bulunan esnek bir demir şerit, şeridin dayandığı bir kontak vidası ve bir zil kasesi vardır. Pil, düğme, bobin, şerit ve kontak vidası şekildeki gibi seri bağlıdır; şeridin ucunda çekiç vardır ve şerit, dinlenme konumunda kontak vidasına dayanır. Düğmeye basılı tutulduğunda zil kesintisiz çalmaktadır.\nBuna göre,')
o=[]
o.append('\\draw[thick,fill=gray!55] (.8,.3) rectangle (1.4,2.0);')
for i in range(6): o.append(f'\\draw[thick] (.6,{.45+i*.27:.2f}) -- (1.6,{.57+i*.27:.2f});')
o.append('\\draw[thick,fill=gray!30] (1.9,2.3) rectangle (2.3,2.5);\\draw[line width=1.6pt] (2.1,2.3) -- (2.1,.5);\\fill (2.1,.4) circle (.13);')
o.append('\\draw[thick] (2.7,0) arc (180:0:.45);\\draw[thick] (2.7,0) -- (3.6,0);')
o.append('\\draw[thick,fill=gray!30] (3.0,1.05) rectangle (3.5,1.35);\\draw[thick] (3.0,1.2) -- (2.15,1.2);')
o.append('\\draw[thick] (.6,.45) -- (.6,-.8) -- (1.5,-.8);\\draw[thick] (1.7,-.8) -- (2.5,-.8);\\draw[thick] (3.3,-.8) -- (4.2,-.8) -- (4.2,1.2) -- (3.5,1.2);')
o.append('\\draw[thick] (1.5,-.5) -- (1.5,-1.1);\\draw[thick] (1.7,-.65) -- (1.7,-.95);')
o.append('\\draw[thick,fill=white] (2.5,-.8) circle (1.5pt);\\draw[thick,fill=white] (3.3,-.8) circle (1.5pt);\\draw[thick] (2.5,-.8) -- (3.25,-.5);')
o.append('\\draw[thick] (1.6,1.83) -- (1.6,2.9) -- (2.1,2.9) -- (2.1,2.5);')
for t,(x,y),an in (('demir çekirdek',(-1.3,2.5),'east'),('bobin',(.5,.7),'east'),('şerit',(2.5,2.45),'west'),('çekiç',(2.1,.2),'north'),('kontak vidası',(3.25,1.45),'south'),('zil kasesi',(3.15,.55),'south'),('düğme',(2.9,-1.0),'north'),('pil',(1.6,-1.2),'north')):
    o.append(f'\\node[font=\\footnotesize,anchor={an}] at ({x},{y}) {{{t}}};')
o.append('\\draw[-{Stealth[length=1.5mm]}] (-1.25,2.5) -- (.85,1.85);')
SK12=tikz_svg(HEAD+'\n'.join(o)+TAIL)
q('0012',[A('Zilin çalışmasını çöz','Elektromıknatıs şeridi çekerse şerit kontak vidasından ayrılır ve devre açılır.','çekilince devre açılır')]+ad+[A('Sonuç','II ve III doğrudur.','II ve III')],tipId='fz-mn2-zil',tip='Elektrik zili',z='orta',alt='Manyetizmanın Uygulamaları',kaz='Elektrik zilinin çalışmasını elektromıknatısın akımla kontak arasındaki ilişkiyle açıklar.',kalip='öncüllü',
 kart='K-FZMN2-12 (elektrik zili) · kontak, devrenin açılıp kapanması, çekirdek',
 istenen='Doğru yargıların hangileri olduğu.',ip=['Şerit elektromıknatıs tarafından çekildiği anda devrenin açık mı kapalı mı olduğunu düşün.'],
 bilgi=[B('Elektrik zili','zilde elektromıknatıs, devre kapalıyken demir şeridi çeker; şerit çekilince devre açılır, akım kesilir ve şerit esneyerek geri döner. Böylece şerit hızla ileri geri gider. Örnek: düğmeye basılı kaldıkça çekiç kaseye tekrar tekrar vurur')],
 puf='Zilde şerit çekilince devre açılır, akım kesilir; şerit geri dönünce devre kapanır ve olay tekrarlanır.',sekil=SK12,**ic)

# =================== 13 · hoparlör · kolay ===================
kartla('13','Hoparlörün çalışması','Hoparlörde yönü değişen akım bobinin kutuplarını değiştirir; bobin sabit mıknatısla dönüşümlü itişip çekişir ve zarı titreştirir.','Hoparlörde mıknatısın kutuplarının değiştiğini ya da ısınmanın sesi oluşturduğunu sanmak.','kolay','düz',3,'fz-mn2-hoparlor','Hoparlörün çalışması')
q('0013',[A('Bobinden geçen akımı incele','Ses akımının yönü ve şiddeti sürekli değişir.','akım yönü değişir'),
 A('Bobinin kutuplarını yorumla','Akım yönü değişince bobinin N ve S kutupları yer değiştirir.','kutuplar değişir'),
 A('Sabit mıknatısla etkileşimi bul','Bobin sabit mıknatısı dönüşümlü iter ve çeker; zar ileri geri titreşir.','itme–çekme → titreşim')],
 tipId='fz-mn2-hoparlor',tip='Hoparlörün çalışması',z='kolay',alt='Manyetizmanın Uygulamaları',kaz='Hoparlörün zarının titreşmesini bobin ve sabit mıknatıs etkileşimiyle açıklar.',kalip='düz',
 kart='K-FZMN2-13 (hoparlör) · değişken akım, bobin ve sabit mıknatıs',
 metin='Bir hoparlörde, sabit bir mıknatıs ile mıknatısın alanı içinde bulunan, hareket edebilen ve hoparlör zarına bağlı bir bobin vardır. Ses kaynağından gelen akım, yönü ve şiddeti sürekli değişerek bobinden geçer. Bu sırada zar ileri geri titreşir ve ortama ses yayılır.\nBuna göre, hoparlörde zarın titreşmesini sağlayan olay aşağıdakilerden hangisidir?',
 dogru='Bobinin kutuplarının akımla değişip sabit mıknatısla itişip çekişmesi',sira=['Sabit mıknatısın alanının akımla sürekli güçlenip zayıflaması','Bobinin kutuplarının akımla değişip sabit mıknatısla itişip çekişmesi','Bobinin hep aynı kutuplu kalıp sabit mıknatısı sürekli itmesi','Bobindeki akımın zarı elektrik yüküyle doğrudan çekmesi','Sabit mıknatısın bobindeki demir çekirdeği kalıcı mıknatıslaması'],
 yan=[('Sabit mıknatısın alanının akımla sürekli güçlenip zayıflaması','Sabit mıknatısın alanının akımla değiştiğini sanmış; sabit mıknatısın alanı sabittir, değişen bobinin alanıdır.','bilgi'),
  ('Bobinin hep aynı kutuplu kalıp sabit mıknatısı sürekli itmesi','Akımın bobine hep aynı kutbu verdiğini sanmış; öyle olsaydı zar bir yana itilip sabit kalırdı, titreşmezdi.','bilgi'),
  ('Bobindeki akımın zarı elektrik yüküyle doğrudan çekmesi','Akımın zarı doğrudan çektiğini sanmış; zarı hareket ettiren bobin ile mıknatıs arasındaki manyetik kuvvettir.','bilgi'),
  ('Sabit mıknatısın bobindeki demir çekirdeği kalıcı mıknatıslaması','Kalıcı mıknatıslanmanın zarı titreştireceğini sanmış; kalıcı mıknatıslanma yönü sürekli değişen bir hareket vermez.','bilgi')],
 istenen='Zarın titreşmesini sağlayan olay.',ip=['Hoparlörde bobinin ve sabit mıknatısın birbirine nasıl etki ettiğini düşün.'],
 bilgi=[B('Hoparlör','akım geçen bobin elektromıknatıs gibi davranır; akımın yönü değişince N ve S kutupları yer değiştirir. Hareketli bobin ile sabit mıknatıs dönüşümlü itişip çekişir, zar ileri geri titreşir. Örnek: bobinin N ucu sabit mıknatısın N kutbuna bakarken bobin itilir'),],
 puf='Hoparlörde yönü değişen akım bobinin kutuplarını değiştirir; bobinin sabit mıknatısla itişip çekişmesi zarı titreştirir.')

# =================== 14 · bobin ve asılı mıknatıs · zor ===================
kartla('14','Elektromıknatıs ve asılı mıknatıs','Bobinin kutbu sağ el kuralıyla bulunur; karşısındaki mıknatısın bakışan ucu farklı cinsse çekilir, aynı cinsse itilir; pil ters çevrilince bobinin kutupları değişir ve etki tersine döner.','Pil ters çevrilince etkinin ortadan kalktığını sanmak; bobin kutbunu ters bulmak.','orta','şekilli',5,'fz-mn2-asilibobin','Elektromıknatıs ve asılı mıknatıs')
n14,R14=5,.7
ct,xl,xr,Nuc=coil(0,n14,R14,.55,.4,False); assert Nuc=='sağ'
o=[ct]
cy=0; mw=1.6; mx=xl-.7-mw/2       # mıknatıs merkezi
o.append('\\draw[thick] (-5.3,2.3) -- (-.6,2.3);')
for dx in (-.55,.55): o.append(f'\\draw[thick] {p2(mx+dx,2.3)} -- {p2(mx+dx,cy+.25)};')
o.append(magnet(mx-mw/2,cy-.25,mw,.5,labs=('N','S'),nfill=True))
SK14=tikz_svg(HEAD+'\n'.join(o)+TAIL)
q('0014',[A('Bobinin kutuplarını bul','Pilin + ucu sağdadır; akım bobine sağdan girer ve önden geçen sarımlarda aşağı yönlüdür. Sağ el kuralıyla başparmak sağa bakar: sağ uç N, sol uç S.','sol uç S'),
 A('İlk durumu yorumla','Mıknatısın bobine bakan ucu S, bobinin sol ucu da S’dir; aynı cins kutuplar birbirini iter.','bobinden uzaklaşır'),
 A('Pili ters çevir','Akım yönü değişince bobinin kutupları yer değiştirir; sol uç N olur.','sol uç N'),
 A('İkinci durumu yorumla','Mıknatısın bobine bakan ucu S, bobinin sol ucu N; farklı cins kutuplar birbirini çeker.','bobine yaklaşır'),
 A('Sonuç','Hareketler sırasıyla belirlenir.','uzaklaşır – yaklaşır')],
 tipId='fz-mn2-asilibobin',tip='Elektromıknatıs ve asılı mıknatıs',z='orta',alt='Akım ve Manyetik Alan',kaz='Bobinin kutuplarını sağ el kuralıyla bulup pil ters çevrilmeden önce ve sonra asılı mıknatısın hareketini yorumlar.',kalip='şekilli',
 kart='K-FZMN2-14 (bobin ve asılı mıknatıs) · pil ters çevrilir, asılı mıknatıs',
 metin='Şekildeki düzenekte bir bobin, bir pil ve bir anahtar seri bağlanmıştır (anahtar şekilde çizilmiştir); bobinin önden geçen sarımları kalın, arkadan geçenler ince kesikli çizgilerle gösterilmiştir. Bobinin sol yanında, ipleriyle tavana asılmış bir çubuk mıknatıs bobinin eksenine hizalı ve durgun hâldedir. Anahtar kapatılınca mıknatısın ilk hareketi gözleniyor. Sonra anahtar açılıyor, mıknatıs ilk konumunda durgun hâle gelince pilin bağlantı uçları yer değiştirilip anahtar yeniden kapatılıyor ve mıknatısın ilk hareketi bir kez daha gözleniyor.\nBuna göre, mıknatısın bobine göre ilk hareketleri sırasıyla aşağıdakilerden hangisidir?',
 sekil=SK14,dogru='Bobinden uzaklaşır – bobine yaklaşır',sira=['Bobine yaklaşır – bobine yaklaşır','Bobine yaklaşır – bobinden uzaklaşır','Bobinden uzaklaşır – bobine yaklaşır','Bobinden uzaklaşır – bobinden uzaklaşır','Hareket etmez – hareket etmez'],
 yan=[('Bobine yaklaşır – bobine yaklaşır','Pil ters çevrilince bile etkinin değişmediğini sanmış ve ilk durumda bobinin sol ucunu N bulmuş.','bilgi'),
  ('Bobine yaklaşır – bobinden uzaklaşır','Sağ el kuralını ters uygulayıp bobinin sol ucunu N sanmış; pilin ters çevrilmesini de doğru yorumlamış.','islem'),
  ('Bobinden uzaklaşır – bobinden uzaklaşır','İlk durumu doğru bulmuş; pil ters çevrilince bobinin kutuplarının değiştiğini atlamış.','dikkat'),
  ('Hareket etmez – hareket etmez','Akım geçen bobinin mıknatısa kuvvet uygulamayacağını sanmış; bobin elektromıknatıs gibi davranır.','bilgi')],
 istenen='Mıknatısın pil ters çevrilmeden önceki ve sonraki ilk hareketi.',ip=['Akım yönünü kullanarak bobinin mıknatısa bakan ucunun kutbunu bul; pil ters çevrilince bu uçta ne değişir?'],
 bilgi=[B('Bobin ve mıknatıs','sağ elin parmakları bobinde akım yönünde kıvrılınca başparmak bobinin N ucunu gösterir; pil ters çevrilince kutuplar yer değiştirir. Bobinin ucu ile mıknatısın bakışan ucu aynı cinsse itme, farklı cinsse çekme olur. Örnek: N ucu bakışan bobin ile N ucu bakışan mıknatıs birbirini iter')],
 puf='Pil ters çevrilince bobinin kutupları yer değiştirir; aynı cins kutuplar iter, farklı cins kutuplar çeker.')

bitir(P,'manyetizmaiki','fiz|Manyetizma')
