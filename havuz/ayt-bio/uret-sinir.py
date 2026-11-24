"""AYT Biyoloji · Sinir Sistemi · 20 soru. Kardeş yok, ipucu 1.
Şekiller TikZ/pgfplots; iletim hızları, grafik tepe noktaları, öncül ve hasta tabloları Python'da tek yerde tanımlanır, assert edilir."""
import sys,os,math,json,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONU_AD='Sinir Sistemi'; KEY='abio|Sinir Sistemi'
P=Parti('sinir',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KY='ÖSYM AYT 2018–2026 Biyoloji sinir sistemi soruları (yalnız mantık) · MEB 11. sınıf Denetleyici ve Düzenleyici Sistemler'
TIP={'noron':('sn-noron','Nöron yapısı ve miyelin kılıf'),'impuls':('sn-impuls','İmpuls oluşumu ve iletimi'),'sinaps':('sn-sinaps','Sinaps ve nörotransmitterler'),
     'refleks':('sn-refleks','Refleks yayı'),'mss':('sn-mss','Merkezi ve çevresel sinir sistemi'),'beyin':('sn-beyin','Beyin bölümleri ve görevleri'),
     'deney':('sn-deney','Vaka ve deney yorumlama')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kart(f'K-ABSNR-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KY)
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABSNR-{no[-2:]} ({ozet})',**k)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKS='-{Stealth[length=2.3mm,width=1.9mm]}'
def lab(t,x,y,x2,y2,gap=.0):
    """numara etiketi (x,y) ve ok ucu (x2,y2)"""
    a=math.atan2(y2-y,x2-x); sx=x+.28*math.cos(a); sy=y+.28*math.sin(a)
    return f'\\node[font=\\normalsize\\bfseries] at ({x},{y}) {{{t}}};\\draw[{OKS},line width=.8pt] ({sx:.2f},{sy:.2f})--({x2},{y2});'
# ---------- seçenek yardımcıları ----------
KOMB=[('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]
def adk(c): return ('Yalnız '+c[0]) if len(c)==1 else (' ve '.join(c) if len(c)==2 else ', '.join(c[:-1])+' ve '+c[-1])
def onc(d,h,hedef=True):
    """d: {'I':(bool,açıklama)}; hedef=True doğru öncüller, False yanlış öncüller aranır; doğru kümeyi h. harfe (0=A) yerleştirir."""
    T=tuple(k for k in ('I','II','III') if d[k][0]==hedef); i=KOMB.index(T); bas=i-h; assert 0<=bas<=2,('uygun degil',T,h)
    ops=KOMB[bas:bas+5]; assert ops[h]==T and len(ops)==5
    yan=[]
    for o in ops:
        if o==T: continue
        p=[]
        for x in o:
            if x not in T: p.append(f'{x} öncülünü '+('doğru' if hedef else 'yanlış')+f' sanmış; oysa '+('yanlıştır' if hedef else 'doğrudur')+f': {d[x][1]}')
        for x in T:
            if x not in o: p.append(f'{x} öncülünü '+('yanlış' if hedef else 'doğru')+f' sanmış; oysa '+('doğrudur' if hedef else 'yanlıştır')+f': {d[x][1]}')
        yan.append((adk(o),'. '.join(p)+'.','bilgi'))
    return dict(dogru=adk(T),yan=yan,sira=[adk(o) for o in ops])
def tek(dogru,yanlislar,h,hedef=True):
    """dogru=(metin,neden); yanlislar=[(metin,neden)]*4; h: doğru şık konumu. hedef=True: doğru ifade aranır; False: yanlış ifade aranır."""
    assert len(yanlislar)==4
    sira=[m for m,_ in yanlislar]; sira.insert(h,dogru[0])
    yan=[(m,(f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}.' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}.'),'bilgi') for m,n in yanlislar]
    return dict(dogru=dogru[0],yan=yan,sira=sira)
def dizi(dogru,digerleri,h,aciklamalar):
    """dizi/sıra seçenekleri: digerleri=[(metin,hata açıklaması)]"""
    sira=[m for m,_ in digerleri]; sira.insert(h,dogru)
    return dict(dogru=dogru,yan=[(m,a,'bilgi') for m,a in digerleri],sira=sira)

# ======================= ŞEKİLLER =======================
def f_noron(L):
    """L: gov,dend,aks,miy,ran -> numara"""
    b=[]
    for ln in ['(1.65,.2)--(1.0,.55)--(.35,.75)','(1.0,.55)--(.4,.35)','(1.62,-.2)--(1.0,-.55)--(.35,-.8)','(1.0,-.55)--(.45,-.3)','(1.95,.55)--(1.45,1.1)--(.95,1.4)','(1.45,1.1)--(1.05,.95)']:
        b.append(f'\\draw[line width=1.1pt] {ln};')
    b.append('\\draw[line width=1.4pt,fill=black,fill opacity=.10] (2.2,0) circle (.62);\\draw[line width=1.4pt] (2.2,0) circle (.62);\\draw[line width=1pt,fill=black,fill opacity=.35] (2.2,0) circle (.2);')
    b.append('\\draw[line width=1.3pt] (2.82,0)--(8.6,0);')
    for a in (3.5,5.3,7.1):
        b.append(f'\\draw[rounded corners=5pt,line width=1.1pt,fill=black,fill opacity=.15] ({a},-.3) rectangle ({a+1.5},.3);\\draw[rounded corners=5pt,line width=1.1pt] ({a},-.3) rectangle ({a+1.5},.3);')
    b.append('\\draw[line width=1.2pt] (8.6,0)--(9.25,.55) (8.6,0)--(9.3,0) (8.6,0)--(9.25,-.55);\\draw[fill=black,fill opacity=.4] (9.25,.55) circle (.13) (9.3,0) circle (.13) (9.25,-.55) circle (.13);')
    b.append(lab(L['dend'],.4,1.9,1.0,.6)); b.append(lab(L['gov'],2.2,-1.6,2.2,-.68)); b.append(lab(L['aks'],3.15,1.4,3.15,.1))
    b.append(lab(L['miy'],4.25,-1.4,4.25,-.34)); b.append(lab(L['ran'],5.15,1.4,5.15,.1))
    return tk('\n'.join(b),.85)
def f_beyin(L):
    """L: buyuk,beyincik,omsogan,ara,orta"""
    b=[]
    b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.08,smooth cycle] plot coordinates {(.3,1.4) (.25,2.3) (.8,3.2) (1.9,3.7) (3.2,3.75) (4.4,3.3) (5.0,2.4) (5.0,1.5) (4.5,.85) (3.6,.75) (2.9,.9) (2.2,.8) (1.4,.7) (.7,.95)};')
    b.append('\\draw[line width=1.3pt,smooth cycle] plot coordinates {(.3,1.4) (.25,2.3) (.8,3.2) (1.9,3.7) (3.2,3.75) (4.4,3.3) (5.0,2.4) (5.0,1.5) (4.5,.85) (3.6,.75) (2.9,.9) (2.2,.8) (1.4,.7) (.7,.95)};')
    b.append('\\draw[line width=.6pt] (1.0,2.6) .. controls (1.6,3.0) and (2.0,2.2) .. (2.6,2.7) .. controls (3.2,3.1) and (3.6,2.3) .. (4.2,2.7);')
    b.append('\\draw[line width=1.2pt,fill=black,fill opacity=.30] (2.5,1.45) ellipse (.72 and .4);\\draw[line width=1.2pt] (2.5,1.45) ellipse (.72 and .4);')
    b.append('\\draw[line width=1.2pt,fill=black,fill opacity=.18,rounded corners=3pt] (2.15,.82)--(2.9,.82)--(2.85,.15)--(2.2,.15)--cycle;\\draw[line width=1.2pt,rounded corners=3pt] (2.15,.82)--(2.9,.82)--(2.85,.15)--(2.2,.15)--cycle;')
    b.append('\\draw[line width=1.2pt,fill=black,fill opacity=.10,rounded corners=4pt] (2.0,.15)--(3.1,.15)--(3.0,-.45)--(2.1,-.45)--cycle;\\draw[line width=1.2pt,rounded corners=4pt] (2.0,.15)--(3.1,.15)--(3.0,-.45)--(2.1,-.45)--cycle;')
    b.append('\\draw[line width=1.2pt,fill=black,fill opacity=.25,rounded corners=3pt] (2.15,-.45)--(2.95,-.45)--(2.85,-1.45)--(2.3,-1.45)--cycle;\\draw[line width=1.2pt,rounded corners=3pt] (2.15,-.45)--(2.95,-.45)--(2.85,-1.45)--(2.3,-1.45)--cycle;')
    b.append('\\draw[line width=1.2pt] (2.3,-1.45)--(2.35,-2.5) (2.85,-1.45)--(2.8,-2.5);')
    b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.15] (4.0,.1) ellipse (1.0 and .55);\\draw[line width=1.3pt] (4.0,.1) ellipse (1.0 and .55);')
    b.append('\\draw[line width=.6pt] (3.2,.3) .. controls (3.8,.45) and (4.2,.45) .. (4.8,.3) (3.1,.1) .. controls (3.8,.25) and (4.2,.25) .. (4.9,.1) (3.2,-.1) .. controls (3.8,.05) and (4.2,.05) .. (4.75,-.1);')
    b.append(lab(L['buyuk'],1.0,4.5,1.5,3.35)); b.append(lab(L['ara'],-.4,1.5,1.75,1.5)); b.append(lab(L['orta'],-.4,.45,2.18,.45))
    b.append(lab(L['beyincik'],5.9,-.55,4.85,-.15)); b.append(lab(L['omsogan'],5.0,-1.5,2.9,-1.0))
    return tk('\n'.join(b),.85)
def f_omurilik(L,refleks=False):
    """L: dict gri,beyaz,arka,on,dugum (numara) ya da refleks için resp,duyu,ara,motor,efek"""
    b=[]
    b.append('\\draw[line width=1.4pt,fill=black,fill opacity=.06] (4,3) ellipse (2.6 and 2.5);\\draw[line width=1.4pt] (4,3) ellipse (2.6 and 2.5);')
    pts=[(4,3.4),(3.45,4.25),(3.0,4.3),(2.9,3.8),(3.2,3.35),(2.6,3.0),(2.2,2.5),(2.35,1.85),(2.85,1.7),(3.4,2.2),(3.75,2.55),(4,2.6)]
    full=pts+[(8-x,y) for x,y in reversed(pts[1:-1])]
    co=' '.join(f'({x:.2f},{y:.2f})' for x,y in full)
    b.append(f'\\draw[line width=1.2pt,fill=black,fill opacity=.30,smooth cycle] plot coordinates {{{co}}};\\draw[line width=1.2pt,smooth cycle] plot coordinates {{{co}}};')
    if not refleks: b.append('\\draw[line width=.9pt] (4,3) circle (.14);')
    # kökler (sol)
    b.append('\\draw[line width=1.5pt] (3.0,4.3)--(2.9,5.35)--(2.75,6.25);\\draw[line width=1.2pt,fill=black,fill opacity=.35] (2.7,6.5) ellipse (.42 and .28);\\draw[line width=1.2pt] (2.7,6.5) ellipse (.42 and .28);')
    b.append('\\draw[line width=1.5pt] (2.55,6.78)--(2.0,7.5);\\draw[line width=1.5pt] (2.45,1.85)--(2.35,1.05)--(2.0,.2);')
    if refleks:
        b=[x for x in b if 'line width=.9pt] (4,3)' not in x]
        b.append('\\draw[line width=1.5pt] (2.0,7.5)--(.7,7.5);\\draw[line width=1.2pt] (.45,7.5) circle (.28);\\draw[line width=.8pt,fill=black] (.45,7.5) circle (.1);')
        b.append('\\draw[line width=1.5pt] (2.0,.2)--(1.0,-.4);\\draw[line width=1.2pt] (.1,-.4) .. controls (.5,-.1) and (.9,-.1) .. (1.3,-.4) .. controls (.9,-.7) and (.5,-.7) .. (.1,-.4);\\draw[line width=.7pt] (.3,-.4)--(1.1,-.4);')
        # duyu nöronu gri maddede biter; ara nöron; motor nöron gövdesi
        b.append('\\draw[line width=1.5pt] (3.0,4.3)--(3.3,3.55);\\draw[line width=1.5pt] (3.3,3.55)--(3.7,3.2);')
        b.append('\\draw[line width=1.2pt] (3.85,3.1) circle (.17);\\draw[line width=1.5pt] (3.8,2.95)--(3.5,2.45)--(3.1,2.25);')
        b.append('\\draw[line width=1.2pt] (2.9,2.2) circle (.17);\\draw[line width=1.5pt] (2.75,2.12)--(2.55,1.95)--(2.45,1.85);')
        b.append(lab(L['resp'],-.3,6.5,.4,7.25)); b.append(lab(L['duyu'],1.1,6.0,2.5,5.8)); b.append(lab(L['ara'],6.2,3.1,4.05,3.1))
        b.append(lab(L['motor'],1.1,1.5,2.4,1.35)); b.append(lab(L['efek'],1.5,-1.3,.7,-.62))
        return tk('\n'.join(b),.62)
    b.append(lab(L['gri'],7.4,3.6,4.9,3.3)); b.append(lab(L['beyaz'],6.9,5.2,5.9,4.5)); b.append(lab(L['arka'],4.3,5.8,2.95,5.5))
    b.append(lab(L['on'],1.0,1.25,2.2,1.3)); b.append(lab(L['dugum'],1.1,6.5,2.2,6.5))
    return tk('\n'.join(b),.62)
def f_sinaps(L):
    """L: ves,aralik,resp,pre"""
    b=[]
    b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.08,rounded corners=18pt] (1.0,2.4) rectangle (5.0,4.5);\\draw[line width=1.3pt,rounded corners=18pt] (1.0,2.4) rectangle (5.0,4.5);')
    b.append('\\draw[line width=1.3pt] (2.4,4.5)--(2.4,5.4) (3.6,4.5)--(3.6,5.4);')
    for (x,y) in [(1.9,3.2),(2.5,3.0),(3.2,3.25),(3.9,3.0),(4.4,3.3),(2.2,3.8),(3.0,3.9),(3.8,3.8)]:
        b.append(f'\\draw[line width=.9pt,fill=black,fill opacity=.2] ({x},{y}) circle (.2);\\fill ({x-.06},{y}) circle (.035) ({x+.06},{y+.05}) circle (.035);')
    b.append('\\draw[line width=1.3pt,fill=black,fill opacity=.08,rounded corners=18pt] (.4,-.2) rectangle (5.6,1.5);\\draw[line width=1.3pt,rounded corners=18pt] (.4,-.2) rectangle (5.6,1.5);')
    for x in (1.6,2.8,4.0):
        b.append(f'\\draw[line width=1.4pt] ({x-.3},1.5)--({x-.12},1.2)--({x-.12},1.0) ({x+.3},1.5)--({x+.12},1.2)--({x+.12},1.0);')
    b.append(lab(L['ves'],6.6,3.8,4.45,3.3)); b.append(lab(L['aralik'],-.4,2.0,1.6,2.0)); b.append(lab(L['resp'],6.6,1.0,4.2,1.25))
    b.append(lab(L['pre'],-.2,4.0,1.0,3.9))
    return tk('\n'.join(b),.62)
def f_zincir(P_):
    b=[]
    def noron(x0,tag):
        o=f'\\draw[line width=1.3pt,fill=black,fill opacity=.10] ({x0},0) circle (.38);\\draw[line width=1.3pt] ({x0},0) circle (.38);'
        o+=f'\\draw[line width=1.1pt] ({x0-.36},.1)--({x0-.85},.35) ({x0-.38},0)--({x0-.9},0) ({x0-.36},-.1)--({x0-.85},-.35);'
        o+=f'\\draw[line width=1.3pt] ({x0+.38},0)--({x0+2.75},0);\\draw[line width=1.2pt,fill=black,fill opacity=.4] ({x0+2.88},0) circle (.13);'
        o+=f'\\node[font=\\normalsize\\bfseries] at ({x0},-.85) {{{tag}}};'
        return o
    for x0,t in ((1.0,'A'),(5.0,'B'),(9.0,'C')): b.append(noron(x0,t))
    for x,t in P_.items(): b.append(f'\\fill ({x[0]},0) circle (.1);\\node[font=\\normalsize\\bfseries] at ({x[0]},.5) {{{t}}};')
    b.append(f'\\draw[{OKS},line width=1pt] (5.0,1.5)--(5.0,.45);\\node[font=\\small\\bfseries] at (5.0,1.8) {{Uyarı}};')
    return tk('\n'.join(b),.78)
# ---- aksiyon potansiyeli ----
def ap(t,tp,s=1.0):
    """tepe zamanı tp; yükselme s, düşme s, ters taraf 1.6s"""
    u=t-(tp-s)
    if u<=0: return -70.0
    if u<=s: return -70+105*(1-math.cos(math.pi*u/s))/2
    if u<=2*s: return 35-105*(1-math.cos(math.pi*(u-s)/s))/2
    if u<=3.6*s: return -70-10*math.sin(math.pi*(u-2*s)/(1.6*s))
    return -70.0
def pgf(pts): return ' '.join(f'({x:.2f},{y:.1f})' for x,y in pts)

# ======================= 01 · Nöron (kolay, şekilli) =======================
SK1=f_noron(dict(gov='I',aks='II',dend='III',miy='IV',ran='V'))
NOR=B('Nöronun yapısı','nöron; hücre gövdesi, dendritler ve akson uzantılarından oluşur · Aksonu saran miyelin kılıf yer yer kesintiye uğrar, bu noktalara Ranvier boğumu denir')
Q('0001','noron','kolay','şekilli','Nöronun yapısı','Şematik nöronda dendriti belirleyip görevini bilir.','Dendrit uyarıyı alıp gövdeye doğru taşır; akson gövdeden uzağa iletir.','Dendriti akson ile karıştırmak; miyelin kılıfı uyarıyı alan yapı sanmak.','nöron yapısı',
 [A('Şekli oku','Şekilde nöronun gövdesi, kısa dallanan uzantıları, uzun ve kılıfla sarılı uzantısı vardır.','Dallanan kısa uzantı · uzun uzantı · kılıf'),
  A('Görevi eşleştir','Hücreye uyarıyı getiren uzantı, gövdeye doğru taşıma yapan kısa ve çok dallı olandır.','Gövdeye doğru taşıyan: dendrit'),
  A('Numarayı bul','Dendrit, gövdenin uyarıyı alan tarafındaki dallanmış uzantıdır.','Dendrit: III numaralı yapı')],
 metin='Şekilde bir motor nöronun yapısı gösterilmiş ve bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, başka nöronlardan gelen uyarıları alarak bunları hücre gövdesine doğru ileten yapı numaralı bölümlerden hangisidir?',
 sekil=SK1,sira=['I','II','III','IV','V'],dogru='III',
 yan=[('I','I numaralı yapı hücre gövdesidir; impulsu yalnız aldığı için dendritle karıştırılmış, oysa gövde uyarıyı kendisine ulaşan uzantılardan alır.','bilgi'),
      ('II','II numaralı yapı aksondur; akson impulsu gövdeden uzaklaştırır, gövdeye doğru taşımaz.','bilgi'),
      ('IV','IV numaralı yapı miyelin kılıftır; aksonu yalıtır ve iletimi hızlandırır, uyarı almaz.','bilgi'),
      ('V','V numaralı yapı Ranvier boğumudur; kılıfın kesintiye uğradığı noktadır, uyarı alan bir uzantı değildir.','bilgi')],
 istenen='Uyarıyı alıp hücre gövdesine doğru ileten yapı',ip=['Gövdeye doğru mu, gövdeden uzağa mı taşıma yapıldığına bak.'],bilgi=[NOR],puf='Dendrit gövdeye getirir, akson gövdeden götürür.')

# ======================= 02 · Beyin bölümleri (kolay, şekilli) =======================
SK2=f_beyin(dict(omsogan='I',buyuk='II',beyincik='III',ara='IV',orta='V'))
BEY=B('Beyin bölümleri','beyin; büyük beyin, ara beyin, orta beyin, beyincik ve omurilik soğanından oluşur · Orta beyin, köprü ve omurilik soğanı birlikte beyin sapını kurar ve beyin sapı omurilikle birleşir')
Q('0002','beyin','kolay','şekilli','Beyin bölümleri','Beyin bölümlerinin görevlerini şekil üzerinde eşleştirir.','Beyin bölümlerinin görevleri şekil üzerinde eşleştirilir.','Kalp ve solunumu büyük beyin ya da hipotalamusla ilişkilendirmek.','kalp–solunum merkezi',
 [A('Şekli oku','Şekilde büyük beyin, beyincik ve beyin sapının bölümleri numaralandırılmıştır.','Beyin sapı: omurilikle birleşen sap'),
  A('Görevi hatırla','Kalp atışı ve solunum gibi yaşamsal olaylar, omuriliğe bağlanan sap bölümünün alt ucundaki merkezlerce denetlenir.','Yaşamsal merkez: omurilik soğanı'),
  A('Numarayı bul','Omurilik soğanı beyin sapının omuriliğe en yakın bölümüdür.','Omurilik soğanı: I numaralı yapı')],
 metin='Şekilde insan beyninin yandan kesit görünümü verilmiş ve bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır.\nBir kaza sonucunda kalp atışı ve solunum hızının düzenlenmesi bozulan bir kişide, hasar görmüş olması en olası yapı numaralı bölümlerden hangisidir?',
 sekil=SK2,sira=['I','II','III','IV','V'],dogru='I',
 yan=[('II','II numaralı yapı büyük beyindir; bilinçli düşünme ve istemli hareketleri yönetir, yaşamsal olayları denetlemez.','bilgi'),
      ('III','III numaralı yapı beyinciktir; denge ve kas koordinasyonundan sorumludur.','bilgi'),
      ('IV','IV numaralı yapı ara beyindir; vücut ısısı, açlık ve susuzluk gibi dengeleri düzenler, kalp ve solunum merkezi değildir.','bilgi'),
      ('V','V numaralı yapı orta beyindir; göz hareketleri ve bazı refleksleri denetler.','bilgi')],
 istenen='Kalp atışı ve solunumu denetleyen merkez',ip=['Yaşamsal olayları denetleyen merkezin bulunduğu beyin bölümünü düşün.'],bilgi=[BEY],puf='Yaşamsal merkez omurilik soğanındadır.')

# ======================= 03 · MSS / ÇSS (kolay) =======================
Q('0003','mss','kolay','düz','Merkezi ve çevresel sinir sistemi','Merkezi ve çevresel sinir sistemi yapılarını ayırt eder.','Omurilik merkezi, kranyal ve spinal sinirler çevresel sinir sistemindedir.','Omuriliği çevresel sinirle karıştırmak.','MSS–ÇSS ayrımı',
 [A('Sınıflandırmayı hatırla','Merkezi sinir sistemini beyin ve omurilik oluşturur; bunlara bağlanan sinirler çevresel sistemdedir.','MSS: beyin + omurilik'),
  A('Şıkları ele','Kranyal ve spinal sinirler ile otonom sinirler MSS dışında kalır.','Çevresel: kranyal, spinal, otonom'),
  A('Dışarıda kalanı bul','Omurilik, beyinle birlikte merkezi sinir sistemini kurar.','Çevresel olmayan: omurilik')],
 metin='İnsanda sinir sistemi, merkezi sinir sistemi ve çevresel sinir sistemi olmak üzere iki bölümde incelenir. Çevresel sinir sistemi, merkezi sinir sistemini vücudun diğer bölgelerindeki reseptör ve efektörlere bağlayan sinirlerden oluşur.\nBuna göre, aşağıdakilerden hangisi çevresel sinir sisteminin bir parçası değildir?',
 **tek(('Omurilik','omurilik beyinle birlikte merkezi sinir sistemini oluşturur'),
       [('Spinal sinirler','spinal sinirler omurilikten çıkan sinirlerdir ve çevresel sinir sisteminde yer alır'),('Kranyal sinirler','kranyal sinirler beyinden çıkar ve çevresel sinir sistemine aittir'),
        ('Sempatik sinirler','sempatik sinirler otonom sinir sisteminin bir koludur ve çevresel sistemdedir'),('Parasempatik sinirler','parasempatik sinirler otonom sinir sisteminin bir koludur ve çevresel sistemdedir')],0,hedef=False),
 istenen='Çevresel sinir sistemine ait olmayan yapı',ip=['Beyne ve omuriliğe bağlanan sinirlerle beyin ve omuriliğin kendisini ayır.'],
 bilgi=[B('Sinir sisteminin bölümleri','merkezi sinir sistemi beyin ve omurilikten oluşur · Çevresel sinir sistemi kranyal ve spinal sinirlerden, işleyiş bakımından da somatik ve otonom kısımlardan oluşur')],puf='Beyin ve omurilik merkezi, onlardan çıkan sinirler çevreseldir.')

# ======================= 04 · Miyelin kaybı (orta, hikâyeli) =======================
Q('0004','noron','orta','hikâyeli','Miyelin kılıf ve iletim','Miyelin kılıfın iletim hızına etkisini yorumlar.','Miyelin kılıf kaybolunca sıçramalı iletim yerine kesintisiz iletim olur ve hız düşer.','Kılıf kaybını impuls oluşumunun tamamen durmasıyla ya da genliğin değişmesiyle karıştırmak.','miyelin kaybı',
 [A('Durumu çöz','Hastalıkta aksonun kılıfı parçalanıyor; akson artık yalıtılmamıştır.','Kılıf yok · akson yalıtımsız'),
  A('İletim türünü belirle','Kılıflı aksonda impuls boğumdan boğuma sıçrar; kılıf yoksa impuls aksonun her noktasında sırayla oluşur.','Sıçramalı iletim yok · kesintisiz iletim'),
  A('Hızı yorumla','Kesintisiz iletim, sıçramalı iletimden yavaştır; impuls oluşumu ve genliği ise değişmez.','İletim hızı azalır')],
 metin='Multipl skleroz gibi bazı hastalıklarda sinir hücrelerinin akson çevresindeki miyelin kılıf zarar görür ve aksonun bazı bölümleri kılıfsız kalır. Bir hastanın duyu nöronunun aksonunda kılıf tamamen kaybolmuştur. Bu akson eşik değerin üzerindeki bir uyarıyla uyarılmaktadır.\nBuna göre, bu aksonda aşağıdakilerden hangisinin gerçekleşmesi beklenir?',
 **tek(('İmpulsun sıçramalı iletim yerine kesintisiz iletimle ilerlemesi ve hızının azalması',''),
       [('Aksonda impuls oluşumunun durması ve iletim hızının azalması','impuls oluşumu için kılıf gerekmez; kılıfsız akson da impuls üretir ve yalnız iletim hızı azalır'),
        ('İmpuls genliğinin küçülmesi ve iletim hızının artması','hep-hiç yasası nedeniyle impuls genliği değişmez; kılıf kaybı hızı artırmaz, azaltır'),
        ('Na⁺–K⁺ pompasının ATP harcamaması ve iletim hızının azalması','pompa her zaman ATP harcar ve kılıf kaybı iletimi hızlandırmaz'),
        ('İmpulsun akson ucuna ulaşamaması ve iletim hızının artması','kılıfsız akson ucuna da impuls ulaşır ve kılıf kaybı hızı artırmaz')],4),
 istenen='Kılıfı kaybolan aksonda beklenen sonuç',ip=['Kılıfın hangi iletim türünü sağladığını düşün; impulsun oluşup oluşmayacağı ile hızı ayır.'],
 bilgi=[B('Miyelin kılıf','miyelin kılıf akson çevresinde yalıtkan bir örtüdür ve Ranvier boğumlarında kesintiye uğrar · Sinir hücrelerinde impuls iletimi, impulsun akson boyunca ilerlemesidir')],puf='Kılıf hızı belirler; impulsun oluşup oluşmayacağını belirlemez.')

# ======================= 05 · Aksiyon potansiyeli (orta, grafik) =======================
tt=[i/20 for i in range(0,121)]
pts5=[(t,ap(t,2.0,1.0)) for t in tt]
assert max(v for _,v in pts5)==35 and abs(min(v for _,v in pts5)+80)<0.2 and ap(0.5,2.0)==-70 and ap(5.5,2.0)==-70
assert ap(1.5,2.0)>-70 and ap(1.5,2.0)<35 and ap(2.5,2.0)<35 and ap(2.5,2.0)>-70 and ap(3.8,2.0)<-70
b5=['\\begin{axis}[width=8.4cm,height=6cm,xmin=0,xmax=6,ymin=-100,ymax=55,xtick=\\empty,ytick={-70,0,35},axis lines=left,xlabel={Zaman},ylabel={Zar potansiyeli (mV)},tick label style={font=\\small},label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
    f'\\addplot[black] coordinates {{{pgf(pts5)}}};',
    '\\node[font=\\normalsize\\bfseries] at (axis cs:.5,-58) {I};\\node[font=\\normalsize\\bfseries] at (axis cs:1.0,-12) {II};\\node[font=\\normalsize\\bfseries] at (axis cs:3.05,-12) {III};',
    '\\node[font=\\normalsize\\bfseries] at (axis cs:3.8,-92) {IV};\\node[font=\\normalsize\\bfseries] at (axis cs:5.3,-58) {V};','\\end{axis}']
SK5=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(b5)+'\n\\end{tikzpicture}')
Q('0005','impuls','orta','grafik','Aksiyon potansiyeli','Aksiyon potansiyeli grafiğinde iyon hareketlerini evrelerle eşleştirir.','Yükselme evresinde Na⁺ kanalları açılır; düşüşte K⁺ kanalları açılıp K⁺ dışarı çıkar.','Düşüş evresinde de Na⁺ girişi sürer sanmak; dinlenme evresini Na⁺ girişi evresiyle karıştırmak.','aksiyon potansiyeli evreleri',
 [A('Grafiği oku','Zar potansiyeli dinlenme düzeyinden yükselip tepe yapar, sonra düşerek dinlenme düzeyine döner.','Yükselme · tepe · düşüş · dinlenme'),
  A('Evreleri adlandır','Potansiyelin pozitife doğru yükseldiği bölüm depolarizasyon, düştüğü bölüm repolarizasyondur.','Yükselme: depolarizasyon'),
  A('İyon hareketini eşleştir','Depolarizasyonda Na⁺ kanalları açılır ve Na⁺ difüzyonla hızla hücre içine girer; düşüşte K⁺ dışarı çıkar.','Na⁺ girişi: yükselme bölümü'),
  A('Numarayı bul','Yükselen eğri II numaralı aralıktır.','II numaralı aralık')],
 metin='Grafikte bir nöronun akson zarında, eşik değerin üzerinde bir uyarı verildiğinde kaydedilen zar potansiyeli değişimi gösterilmiştir. Eğrinin bazı aralıkları I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, numaralı aralıklardan hangisinde zardaki Na⁺ kanalları açık olduğundan Na⁺ iyonları derişim farkı doğrultusunda hücre içine hızla girmektedir?',
 sekil=SK5,sira=['I','II','III','IV','V'],dogru='II',
 yan=[('I','I numaralı aralık dinlenme düzeyidir; Na⁺ kanalları kapalıdır ve Na⁺ pompayla dışarı taşınır.','bilgi'),
      ('III','III numaralı aralıkta K⁺ kanalları açıktır ve K⁺ hücre dışına çıkar; Na⁺ girişi sona ermiştir.','bilgi'),
      ('IV','IV numaralı aralık dinlenme düzeyinin altındadır; K⁺ çıkışı sürmektedir ve Na⁺ kanalları kapalıdır.','bilgi'),
      ('V','V numaralı aralık dinlenme düzeyine dönüşüdür; iyon dağılımı pompayla düzeltilir, Na⁺ girişi yoktur.','bilgi')],
 istenen='Na⁺ girişinin hızlı olduğu aralık',ip=['Potansiyelin hangi yönde değiştiği, hangi iyonun hangi yöne hareket ettiğini gösterir.'],
 bilgi=[B('İmpuls oluşumu','dinlenmede hücre içi dışına göre negatiftir · Uyarılan nöronun zar potansiyeli önce depolarizasyon, sonra repolarizasyon evrelerinden geçer; iyonlar kanallardan ve pompadan geçer')],puf='Grafikte potansiyelin yönü, iyonun hangi yöne hareket ettiğini gösterir.')

# ======================= 06 · Na–K pompası (orta, öncüllü) =======================
d6={'I':(True,'dinlenmede Na⁺–K⁺ pompası ATP harcayarak Na⁺ iyonlarını dışarı, K⁺ iyonlarını içeri taşır'),
    'II':(False,'dinlenme hâlinde hücre içi, hücre dışına göre negatif yüklüdür'),
    'III':(True,'depolarizasyonda Na⁺ iyonları kanallardan derişim farkıyla girer ve bu girişte ATP harcanmaz')}
r6=onc(d6,3)
Q('0006','impuls','orta','öncüllü','Dinlenme potansiyeli ve pompa','Dinlenme potansiyeli ve Na⁺–K⁺ pompasıyla ilgili yargıları değerlendirir.','Pompa ATP harcar, kanallardan difüzyon ATP harcamaz; dinlenmede hücre içi negatiftir.','Her iyon hareketinin ATP gerektirdiğini sanmak; hücre içinin dinlenmede pozitif olduğunu düşünmek.','Na–K pompası öncülleri',
 [A('Dinlenmeyi hatırla','Dinlenmedeki nöronun içi dışına göre negatif, dışı pozitiftir; iyon dağılımı pompayla korunur.','İçi negatif · dışı pozitif'),
  A('Taşıma türlerini ayır','Derişim farkına karşı taşıma ATP ister; kanaldan difüzyon ATP istemez.','Pompa: ATP var · kanal: ATP yok'),
  A('Öncülleri değerlendir','Pompa tanımı doğru, yük dağılımı ters verilmiş, depolarizasyonda ATP harcanmadan Na⁺ girişi doğrudur.','I: doğru · II: yanlış · III: doğru')],
 metin='İnsan sinir sisteminde bir nöronun zarında Na⁺–K⁺ pompası ve iyon kanalları bulunur. Bu yapılar sayesinde nöron dinlenme hâlindeyken zarın iki yanı arasında bir potansiyel farkı korunur ve uyarılınca impuls oluşur.\nBu nöronla ilgili,\nI. Dinlenme hâlinde Na⁺–K⁺ pompası, ATP harcayarak Na⁺ iyonlarını hücre dışına, K⁺ iyonlarını hücre içine taşır.\nII. Dinlenme hâlinde hücre içi, hücre dışına göre pozitif yüklüdür.\nIII. Depolarizasyon sırasında Na⁺ iyonlarının hücre içine girişi ATP harcanmadan gerçekleşir.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüller',ip=['Her iyon hareketinde derişim farkına karşı mı, yoksa derişim farkı yönünde mi taşıma yapıldığına bak.'],
 bilgi=[B('Zardan madde geçişi','derişim farkı yönünde geçiş (difüzyon) enerji gerektirmez; derişim farkına karşı taşıma (aktif taşıma) ATP harcar. Örnek: glikozun kolaylaştırılmış difüzyonla girişi ATP gerektirmez')],puf='Pompa ATP ister, kanaldan geçiş ister değil.',**r6)

# ======================= 07 · Eşik ve hep-hiç (orta, grafik, olumsuz) =======================
pts7=[]
for i in range(0,601):
    t=i/20
    v=ap(t,13.8,.5)+ap(t,23.8,.5)+70
    v=v+(-70 if False else 0)
    # eşik altı uyarı: küçük yerel sapma
    v+=6*math.exp(-((t-3.5)/.9)**2)
    pts7.append((t,v))
assert max(v for t,v in pts7 if t<8)<-60 and abs(max(v for t,v in pts7 if 10<t<17)-35)<.5 and abs(max(v for t,v in pts7 if 20<t<27)-35)<.5
assert abs(max(v for t,v in pts7 if 10<t<17)-max(v for t,v in pts7 if 20<t<27))<1e-9
b7=['\\begin{axis}[width=8.6cm,height=5.4cm,xmin=0,xmax=30,ymin=-85,ymax=100,xtick={0,5,10,15,20,25,30},ytick={-70,0,35},axis lines=left,xlabel={Zaman (ms)},ylabel={Zar potansiyeli (mV)},tick label style={font=\\small},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
    f'\\addplot[black] coordinates {{{pgf(pts7)}}};']
for t0,s,nm in ((3.0,10,1),(13.0,20,2),(23.0,40,3)):
    b7.append(f'\\draw[{OKS},line width=.9pt] (axis cs:{t0},60)--(axis cs:{t0},-55);\\node[font=\\small,align=center,anchor=south] at (axis cs:{t0+.2},62) {{{nm}. uyarı\\\\{s} birim}};')
b7.append('\\end{axis}')
SK7=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(b7)+'\n\\end{tikzpicture}')
Q('0007','impuls','orta','grafik','Eşik değer ve hep-hiç','Eşik değer ve "ya hep ya hiç" ilkesini grafikten yorumlar.','Eşik altı uyarı impuls oluşturmaz; eşik üzerindeki her uyarı aynı büyüklükte impuls verir.','Uyarı şiddeti arttıkça impuls genliğinin de arttığını sanmak.','eşik ve hep-hiç',
 [A('Kaydı oku','Üç uyarıdan yalnız ikincisi ve üçüncüsü tepe noktalı impuls oluşturmuştur.','1. uyarı: impuls yok · 2. ve 3.: impuls var'),
  A('Eşik değeri çıkar','10 birimde impuls yok, 20 birimde var; eşik değer bu iki değer arasındadır.','10 < eşik ≤ 20'),
  A('İfadeleri sına','İkinci ve üçüncü impulsların tepe noktası eşittir; şiddet arttığında genlik değişmemiştir.','Genlikler eşit'),
  A('Söylenemeyeni seç','Üçüncü uyarının daha büyük bir impuls oluşturduğu grafikten çıkarılamaz.','Söylenemeyen: daha büyük genlik')],
 metin='Bir nöronun aksonuna art arda farklı şiddette üç uyarı uygulanmış ve akson zarındaki potansiyel değişimi kaydedilmiştir. Kayıt grafikte verilmiştir; uyarı şiddetleri grafikte ilgili anlarda gösterilmiştir.\nBu kayda göre, aşağıdaki ifadelerden hangisi söylenemez?',
 sekil=SK7,
 **tek(('3. uyarıyla oluşan impuls, 2. uyarıyla oluşandan daha büyük genliklidir.','2. ve 3. impulsların tepe noktaları aynıdır'),
       [('1. uyarının şiddeti, nöronun eşik değerinin altındadır.','1. uyarı impuls oluşturmamıştır, bu nedenle eşik altındadır'),
        ('Nöronun eşik değeri 10 birimden büyüktür.','10 birimlik uyarı impuls oluşturmamıştır'),
        ('2. ve 3. uyarılara nöron aynı büyüklükte impulsla yanıt vermiştir.','iki impulsun tepe noktası aynıdır'),
        ('2. uyarının şiddeti, nöronun eşik değerine eşit veya eşik değerinden büyüktür.','2. uyarı impuls oluşturmuştur')],1,hedef=False),
 istenen='Kayıttan çıkarılamayan ifade',ip=['Her şıkkı, grafikteki üç tepkiyle tek tek karşılaştır.'],
 bilgi=[B('Eşik değer','impuls oluşturabilen en küçük uyarı şiddetine eşik değer denir · Zar potansiyelindeki değişim grafikle izlenir')],puf='Şiddet impulsun büyüklüğünü değil, sıklığını etkiler.')

# ======================= 08 · İletim hızı (zor, grafik, öncüllü) =======================
MESAFE_CM=12; TX=30; TY=2   # ms
vx=Fr(MESAFE_CM,100)/Fr(TX,1000); vy=Fr(MESAFE_CM,100)/Fr(TY,1000)
assert vx==4 and vy==60 and vy/vx==15
ptX=[(i/10,ap(i/10,TX,.6)) for i in range(0,401)]; ptY=[(i/10,ap(i/10,TY,.6)) for i in range(0,401)]
assert max(v for t,v in ptX)==35 and abs([t for t,v in ptX if v==35][0]-TX)<1e-9 and abs([t for t,v in ptY if v==35][0]-TY)<1e-9
b8=['\\draw[line width=1.6pt] (0,3.0)--(7.2,3.0);\\draw[line width=1.6pt] (0,1.7)--(7.2,1.7);',
    '\\node[font=\\normalsize\\bfseries] at (-.5,3.0) {X};\\node[font=\\normalsize\\bfseries] at (-.5,1.7) {Y};',
    '\\foreach \\y in {3.0,1.7}{\\draw[line width=1.4pt,fill=black] (0,\\y-.15) rectangle (.16,\\y+.15);\\draw[line width=1.4pt,fill=black] (7.2,\\y) -- (7.45,\\y+.18) -- (7.45,\\y-.18) -- cycle;}',
    '\\node[font=\\small] at (.1,.95) {Uyarı};\\node[font=\\small] at (7.2,.95) {Kayıt};',
    '\\draw[<->,line width=.8pt] (0,3.75)--(7.2,3.75);\\node[font=\\small] at (3.6,4.1) {12 cm};',
    '\\begin{axis}[at={(1.2cm,-.6cm)},anchor=north west,width=7.6cm,height=4.6cm,xmin=0,xmax=40,ymin=-85,ymax=55,xtick={0,10,20,30,40},ytick={-70,0,35},axis lines=left,xlabel={Uyarıdan sonra geçen zaman (ms)},ylabel={Kayıt (mV)},tick label style={font=\\small},label style={font=\\small},every axis plot/.append style={line width=1.4pt}]',
    f'\\addplot[black] coordinates {{{pgf(ptX)}}};\\addplot[vurgu] coordinates {{{pgf(ptY)}}};',
    '\\node[font=\\normalsize\\bfseries] at (axis cs:33.5,35) {X};\\node[font=\\normalsize\\bfseries,vurgu] at (axis cs:5.2,35) {Y};','\\end{axis}']
SK8=tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+'\n'.join(b8)+'\n\\end{tikzpicture}')
d8={'I':(True,'hız = 12 cm / 30 ms = 4 m/sn ve 12 cm / 2 ms = 60 m/sn olarak bulunur'),
    'II':(True,'Y aksonunda 3 cm yol 0,03 m / 60 m/sn = 0,0005 sn = 0,5 ms sürer'),
    'III':(False,'X aksonunda 3 cm yol 0,03 m / 4 m/sn = 0,0075 sn = 7,5 ms sürer, 5 ms değil')}
assert Fr(3,100)/vy==Fr(5,10000) and Fr(3,100)/vx==Fr(75,10000)
r8=onc(d8,2)
Q('0008','impuls','zor','grafik','İmpuls iletim hızı','Kayıt grafiğinden iletim hızını hesaplayıp miyelin kılıfla ilişkilendirir.','Hız = yol / süre; hızlı iletim miyelin kılıf ve sıçramalı iletimle açıklanır.','Süre farkını hız oranıyla ters yorumlamak; hızı hesaplarken cm ve ms birimlerini karıştırmak.','iletim hızı öncülleri',
 [A('Verileri oku','İki akson için uyarı ve kayıt elektrotları arası yol 12 cm; impulsun kayıt noktasına ulaşma zamanı grafikten okunur.','X: 30 ms · Y: 2 ms · yol: 12 cm = 0,12 m'),
  A('Hızları hesapla','Hız, yolun süreye bölünmesiyle bulunur; süreler saniyeye çevrilir.','X: 0,12 / 0,03 = 4 m/sn · Y: 0,12 / 0,002 = 60 m/sn'),
  A('3 cm için süre bul','Süre, yolun hıza bölünmesiyle bulunur.','Y: 0,03 / 60 = 0,0005 sn = 0,5 ms · X: 0,03 / 4 = 0,0075 sn = 7,5 ms'),
  A('Öncülleri değerlendir','İlk iki öncül doğrudur, üçüncüde X için süre 7,5 ms bulunur.','I: doğru · II: doğru · III: yanlış')],
 metin='Aynı uzunlukta iki sinir lifinde (X ve Y) iletim hızını ölçmek için düzenek şekildeki gibi kurulmuştur. Her aksonun bir ucundan eşik değerin üzerinde uyarı verilmiş, uyarı anından itibaren aksonların diğer ucuna yerleştirilen elektrottaki potansiyel değişimi kaydedilmiştir. Elektrotlar arası uzaklık her iki akson için 12 cm’dir.\nBu düzenek ve kayıtla ilgili,\nI. X aksonunda impuls 4 m/s, Y aksonunda 60 m/s hızla iletilmiştir.\nII. Y aksonunda impuls, uyarı noktasından 3 cm uzaklığa 0,5 ms’de ulaşır.\nIII. X aksonunda impuls, uyarı noktasından 3 cm uzaklığa 5 ms’de ulaşır.\nifadelerinden hangileri doğrudur?',
 sekil=SK8,istenen='Doğru olan öncüller',ip=['Grafikten okuduğun süreleri yola oranlamadan önce birimleri kontrol et.'],
 bilgi=[B('Hız','hız, alınan yolun geçen süreye oranıdır · Hesapta uzunluk ve zaman birimleri aynı sisteme çevrilir')],puf='Önce birimleri eşitle, sonra yolu süreye böl.',**r8)

# ======================= 09 · Sinaps (orta, şekilli) =======================
SK9=f_sinaps(dict(ves='I',aralik='II',resp='III',pre='IV'))
Q('0009','sinaps','orta','şekilli','Sinaps yapısı','Sinapstaki yapıların görevlerini yorumlar.','Nörotransmitter veziküllerden ekzositozla salınır ve postsinaptik zardaki reseptöre bağlanır.','Nörotransmitterin difüzyonla salındığını, impulsun sinapsta çift yönlü iletildiğini sanmak.','sinaps yapıları',
 [A('Şekli çöz','Üstteki nöronun akson ucunda veziküller, alttaki nöronun zarında ise reseptörler görülür.','I: vezikül · II: sinaptik aralık · III: reseptör · IV: presinaptik akson ucu'),
  A('Salınımı hatırla','Veziküllerdeki nörotransmitterler, zarla kaynaşma yoluyla ekzositozla aralığa bırakılır.','Salınım: ekzositoz'),
  A('İletimi yorumla','Nörotransmitter aralığı geçip reseptöre bağlanınca postsinaptik zarda impuls oluşabilir; iletim tek yönlüdür.','Presinaptik → postsinaptik'),
  A('Şıkları sına','Reseptörü ve bağlanma sonucunu doğru anlatan ifade seçilir.','III: reseptör, bağlanma → impuls')],
 metin='Şekilde iki nöron arasındaki bir sinaps gösterilmiş ve bazı yapılar I, II, III ve IV ile numaralandırılmıştır. Üstteki nöronun akson ucuna bir impuls ulaşmıştır.\nBuna göre, bu sinapsta gerçekleşen olaylarla ilgili aşağıdakilerden hangisi doğrudur?',
 sekil=SK9,
 **tek(('III numaralı yapılara nörotransmitter bağlandığında alttaki nöronun zarında impuls oluşumu başlayabilir.',''),
       [('I numaralı yapılar, nörotransmitterleri aktif taşımayla doğrudan III numaralı yapıların içine aktarır.','nörotransmitterler veziküllerden ekzositozla aralığa bırakılır ve III numaralı yapıların içine aktarılmaz'),
        ('II numaralı bölgede impuls elektriksel olarak aktarıldığından nörotransmitter gerekmez.','sinaptik aralıkta iletim kimyasaldır, nörotransmitterle sağlanır'),
        ('Alttaki nöronda oluşan impuls IV numaralı yapıya geri iletilerek üstteki nöronu uyarabilir.','sinapsta iletim tek yönlüdür, presinaptik nörondan postsinaptik nörona doğrudur'),
        ('Nörotransmitter III numaralı yapılara bağlandıktan sonra hücre zarından geçip alttaki nöronun sitoplazmasında impuls başlatır.','nörotransmitter reseptöre bağlanır, zardan geçip hücreye girmez')],3),
 istenen='Sinapsla ilgili doğru ifade',ip=['Nörotransmitterin nereden salındığına, nereye bağlandığına ve iletimin yönüne bak.'],
 bilgi=[B('Sinaps','iki nöron ya da nöron ile efektör arasındaki bağlantı bölgesidir · İmpulsu gönderen nöron presinaptik, alan nöron postsinaptik nöron olarak adlandırılır')],puf='Sinapsta iletim kimyasal ve tek yönlüdür.')
# dogru metni ve neden: tek() 'neden' yalnız yanlışlarda kullanılır

# ======================= 10 · İlaç etkisi (zor, tablo) =======================
SK10=tablo_svg(['İlaç','Sinaptik aralıkta nörotransmitter','Postsinaptik nöron'],[['Kontrol','Normal','Uyarıya bağlı impuls'],['X','Normalden çok','Sürekli impuls'],['Y','Normalden az','İmpuls oluşmaz'],['Z','Normal','İmpuls oluşmaz']])
Q('0010','sinaps','zor','tablo','Sinaps ve ilaç etkisi','Tablodan ilaçların etki basamağını çıkarıp ilaçların birlikte etkisini öngörür.','Nörotransmitter miktarı ve impuls durumu ilacın hangi basamağı etkilediğini gösterir; birlikte etkide salınmayan nörotransmitter yıkım engelinden etkilenmez.','İlaçların basamaklarını belirlemeden birlikte etkiyi tahmin etmeye çalışmak.','ilaçların birlikte etkisi',
 [A('Kontrolü oku','Normal sinapsta nörotransmitter normal miktardadır ve her uyarıda kısa süreli impuls oluşur.','Kontrol: normal · uyarıya bağlı impuls'),
  A('X ve Y ilaçlarını çöz','X’te nörotransmitter fazla ve impuls sürekli: yıkım engellenmiştir. Y’de nörotransmitter az ve impuls yok: salınım engellenmiştir.','X: yıkım engeli · Y: salınım engeli'),
  A('Birlikte etkiyi öngör','Salınım engellendiğinden aralığa az nörotransmitter geçer; yıkımın engellenmesi olmayan nörotransmitteri çoğaltmaz.','Aralıkta az nörotransmitter'),
  A('Sonucu yaz','Aralıkta az nörotransmitter olduğundan postsinaptik nöronda impuls oluşmaz.','Az nörotransmitter · impuls yok')],
 metin='Bir araştırmacı, aynı tür sinapslara sahip üç sinaps preparatına X, Y ve Z ilaçlarını ayrı ayrı uygulamıştır. Her preparatta presinaptik nöron aynı şiddette uyarılmış; sinaptik aralıktaki nörotransmitter miktarı ve postsinaptik nörondaki impuls durumu kontrol grubuyla birlikte tabloda verilmiştir. İlaçlardan her biri nörotransmitterin salınmasını, yıkımını ya da reseptörlere bağlanmasını etkilemektedir.\nBuna göre, X ve Y ilaçları aynı preparata birlikte uygulanıp presinaptik nöron uyarıldığında, aşağıdakilerden hangisi gözlenir?',
 sekil=SK10,sira=['Aralıkta nörotransmitter normalden çok, postsinaptik nöronda sürekli impuls','Aralıkta nörotransmitter normalden az, postsinaptik nöronda impuls yok','Aralıkta nörotransmitter normal, postsinaptik nöronda impuls yok','Aralıkta nörotransmitter normalden çok, postsinaptik nöronda impuls yok','Aralıkta nörotransmitter normalden az, postsinaptik nöronda sürekli impuls'],
 dogru='Aralıkta nörotransmitter normalden az, postsinaptik nöronda impuls yok',
 yan=[('Aralıkta nörotransmitter normalden çok, postsinaptik nöronda sürekli impuls','Yalnız X ilacının etkisini yazmış; oysa Y ilacı nörotransmitter salınmasını engellediğinden aralıkta fazla nörotransmitter birikmez.','bilgi'),
      ('Aralıkta nörotransmitter normal, postsinaptik nöronda impuls yok','Z ilacının etkisini yazmış; oysa Z uygulanmamıştır ve salınım engellendiğinden nörotransmitter normal miktarda olamaz.','bilgi'),
      ('Aralıkta nörotransmitter normalden çok, postsinaptik nöronda impuls yok','Yıkımın engellenmesinin nörotransmitteri artıracağını sanmış; oysa salınmayan nörotransmitter yıkım engeliyle çoğalmaz.','bilgi'),
      ('Aralıkta nörotransmitter normalden az, postsinaptik nöronda sürekli impuls','Yıkım engelinin sürekli impuls oluşturacağını sanmış; oysa aralıkta bol nörotransmitter olmadığı için sürekli impuls oluşmaz.','bilgi')],
 istenen='X ve Y ilaçlarının birlikte etkisi',ip=['Önce her ilacın hangi basamağı etkilediğini tablodan çıkar.'],
 bilgi=[B('Sinapsta kimyasal iletim','sinapsta iletimi nörotransmitter denilen kimyasal maddeler sağlar · Nörotransmitter etki gösterdikten sonra ortamdan uzaklaştırılır ve iletim sona erer')],puf='Önce her ilacın basamağını bul, sonra birlikte etkiyi düşün.')

# ======================= 11 · Nöron zinciri (zor, şekilli, öncüllü) =======================
SK11=f_zincir({(2.0,):'I',(7.5,):'II',(11.5,):'III'})
d11={'I':(False,'sinapsta iletim tek yönlüdür; B’den A’ya geri iletim olmaz, A nöronunun aksonunda impuls oluşmaz'),
     'II':(True,'B nöronunun gövdesinde eşik üstü uyarı, B aksonu boyunca ilerleyen impuls oluşturur'),
     'III':(True,'B’nin akson ucundaki sinapstan salınan uyarıcı nörotransmitter C nöronunda impuls başlatır ve impuls C aksonunda ilerler')}
r11=onc(d11,3)
Q('0011','sinaps','zor','şekilli','Sinaps yönü ve eşik','Eşik değer ve sinapsta tek yönlü iletimi birleştirerek zincir boyunca impuls yayılımını belirler.','Eşik altı uyarı impuls oluşturmaz; impuls sinapsta yalnızca presinaptikten postsinaptiğe geçer.','Sinapsta çift yönlü iletim sanmak; eşik altı uyarının da zincirde yayıldığını düşünmek.','nöron zinciri',
 [A('Zinciri oku','A nöronunun aksonu B’ye, B nöronunun aksonu C’ye sinaps yapar; uyarı B’nin gövdesine verilir.','A → B → C'),
  A('Eşiği uygula','Birinci uyarı eşik altıdır, hiçbir noktada impuls oluşturmaz; yalnız ikinci uyarı impuls oluşturur.','1. uyarı: impuls yok · 2. uyarı: impuls var'),
  A('İletim yönünü belirle','Sinapsta iletim tek yönlü olduğundan impuls B’nin aksonundan C’ye ilerler, A’ya geri dönmez.','B → C: evet · B → A: hayır'),
  A('Öncülleri değerlendir','II ve III noktalarında impuls kaydedilir, I noktasında kaydedilmez.','I: yanlış · II: doğru · III: doğru')],
 metin='Şekilde A, B ve C nöronları arasındaki sinapslar gösterilmiştir; sinapslar uyarıcıdır ve B’nin akson ucundan salınan nörotransmitter, C nöronunu eşik değerin üzerinde uyarmaktadır. B nöronunun hücre gövdesine sırayla iki uyarı verilmiştir: birinci uyarı B nöronunun eşik değerinin altında, ikinci uyarı ise eşik değerinin üzerindedir. Aksonlar üzerindeki I, II ve III noktalarından impuls kaydı alınmıştır.\nBuna göre, bu noktalardan hangilerinde impuls yalnızca ikinci uyarıdan sonra kaydedilir?',
 sekil=SK11,istenen='Yalnızca ikinci uyarıdan sonra impuls kaydedilen noktalar',ip=['Eşik altı uyarıdan sonra impuls olup olmadığına ve sinapsın iletim yönüne bak.'],
 bilgi=[B('Sinaps ve iletim','sinaps, presinaptik akson ucu ile postsinaptik hücre arasındaki bağlantı bölgesidir · Zincirdeki her nöron, eşik değerin üzerinde uyarıldığında impuls oluşturur')],puf='Zincirde impuls yalnız ileri yönde geçer.',**r11)

# ======================= 12 · Refleks yolu (orta, şekilli) =======================
SK12=f_omurilik(dict(resp='IV',duyu='II',ara='V',motor='I',efek='III'),refleks=True)
dz='IV – II – V – I – III'
dg12=[('I – II – V – IV – III','Motor nöronu uyarının başlangıcı sanmış; oysa yanıt motor nöronla biter, duyu nöronu ise uyarıyı reseptörden omuriliğe getirir.'),
      ('IV – V – II – I – III','Ara nöronu duyu nöronundan önce yerleştirmiş; oysa reseptörden gelen uyarıyı önce duyu nöronu omuriliğe taşır.'),
      ('IV – II – I – V – III','Motor nöronu ara nörondan önce yerleştirmiş; oysa duyu nöronundan gelen impuls ara nörondan geçip motor nörona ulaşır.'),
      ('III – I – V – II – IV','Sırayı tamamen ters yazmış; oysa impuls reseptörden efektöre doğru ilerler.')]
r12=dizi(dz,dg12,0,None)
Q('0012','refleks','orta','şekilli','Refleks yayı','Refleks yayını oluşturan yapıların impuls yolunu şekilde sıralar.','Reseptör → duyu nöronu → ara nöron → motor nöron → efektör.','Ara nöronu atlamak; duyu ve motor nöronun yerlerini karıştırmak.','refleks yayı sırası',
 [A('Yapıları tanı','Şekilde deri reseptörü, omuriliğe girip çıkan nöronlar ve kas görülür.','Reseptör · nöronlar · kas'),
  A('Nöronları ayır','Omuriliğe arka kökle giren nöron duyu nöronu, ön kökle çıkan nöron motor nörondur; gri maddedeki kısa nöron ara nörondur.','Duyu: arka kök · motor: ön kök'),
  A('Yolu sırala','İmpuls reseptörden başlayıp önce duyu nöronuna, sonra ara nörona, motor nörona ve efektöre geçer.','Reseptör → duyu → ara → motor → efektör'),
  A('Numaraları yaz','Numaralar bu sırayla okunur.','IV → II → V → I → III')],
 metin='Şekilde, parmağı iğneye değen bir kişide kolun geri çekilmesini sağlayan refleks yayı şematik olarak gösterilmiştir. Yayı oluşturan yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, bu refleksin gerçekleşmesi sırasında impulsun izlediği yol numaralarla aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=SK12,istenen='İmpulsun izlediği yol',ip=['Uyarıyı alan yapıdan başlayıp yanıtı oluşturan yapıda biten sırayı kur.'],
 bilgi=[B('Refleks yayı','refleks, uyarıya karşı istem dışı oluşan hızlı yanıttır · Refleks yayını reseptör, duyu nöronu, motor nöron, ara nöron ve efektör kurar')],puf='Reseptörden efektöre: duyu, ara, motor.',**r12)

# ======================= 13 · Refleks öncülleri (orta) =======================
d13={'I':(True,'refleks istem dışı bir yanıttır ve aynı uyarıya karşı her seferinde benzer biçimde oluşur'),
     'II':(True,'ara nöronlardan beyne giden yollarla duyu bilgisi beyne de iletilir, kişi uyarıyı sonradan fark eder'),
     'III':(False,'ara nöronlar omurilikte, yani merkezi sinir sisteminde bulunur')}
r13=onc(d13,1)
Q('0013','refleks','orta','öncüllü','Refleks ve ara nöron','Refleks yayının çalışma özelliklerini değerlendirir.','Refleks istem dışıdır; ara nöron MSS içindedir.','Bütün refleks yayı nöronlarını çevresel sinir sistemine ait saymak; refleks için beyin gerektiğini düşünmek.','refleks öncülleri',
 [A('Refleksi tanımla','Refleks, uyarıya karşı hızlı ve istem dışı oluşan yanıttır.','Hızlı · istem dışı'),
  A('Birinci ve ikinci öncülü sına','Yanıt istem dışı ve kalıplaşmıştır; duyu bilgisi ise beyne de gider ve fark etme sonradan olur.','I: doğru · II: doğru'),
  A('Üçüncü öncülü sına','Ara nöron omurilikte bulunur; omurilik merkezi sinir sistemindedir.','III: yanlış')],
 metin='Sıcak bir cisme dokunan kişi elini, sıcaklığı fark etmeden hemen önce geri çeker. Bu tepki bir refleks örneğidir.\nBu refleksle ilgili,\nI. Yanıt istem dışı oluşur ve aynı uyarı karşısında her seferinde benzer biçimde gerçekleşir.\nII. Duyu bilgisi omurilikten beyne de iletilir ve kişi sıcaklığı sonradan fark eder.\nIII. Refleks yayını oluşturan bütün nöronlar çevresel sinir sisteminde yer alır.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüller',ip=['Her öncülde sözü edilen nöronun omurilik içinde mi, dışında mı bulunduğuna bak.'],
 bilgi=[B('Refleks yayı','refleks, uyarıya karşı istem dışı oluşan hızlı yanıttır · Nöronlar, bulundukları yere göre merkezi ya da çevresel sinir sistemine ait sayılır')],puf='Nöronların bulunduğu yer, hangi sisteme ait olduğunu belirler.',**r13)

# ======================= 14 · Hasta tablosu (zor, tablo) =======================
YAPI={'I':'Motor nöron','II':'Büyük beyindeki hareket merkezi','III':'Duyu nöronu','IV':'Omurilik ile beyin arasındaki yollar'}
HST={'K':('Yok','Yok','Var','III'),'L':('Var','Yok','Yok','I'),'M':('Var','Var','Yok','II'),'N':('Yok','Var','Yok','IV')}
dog14=' – '.join(HST[k][3] for k in 'KLMN'); assert dog14=='III – I – II – IV'
SK14=tablo_svg(['Hasta','Dokunmayı hissetme','Refleks yanıtı','İstemli hareket'],[[k,*HST[k][:3]] for k in 'KLMN'])
dg14=[('I – III – II – IV','K ile L’yi karıştırmış; oysa K’de refleks de yoktur ama istemli hareket vardır, bu duyu nöronu hasarını gösterir, motor nöron hasarında istemli hareket de olmaz.'),
      ('III – I – IV – II','M ile N’yi karıştırmış; oysa M’de dokunma hissedilir ve refleks sürer, yollar kesilseydi dokunma hissedilmezdi.'),
      ('III – II – I – IV','L’de hasarı beyin hareket merkezine yazmış; oysa L’de refleks yoktur, refleks yayının motor kolu bozulmuştur.'),
      ('IV – I – II – III','K’de hasarı yollara yazmış; oysa yollar hasarlıysa refleks yayı çalışmaya devam ederdi, K’de ise refleks yoktur.')]
r14=dizi(dog14,dg14,4,None)
Q('0014','deney','zor','tablo','Hasar yeri belirleme','Refleks, duyu ve istemli hareket bulgularından hasarlı sinir yapısını belirler.','Duyu, refleks ve istemli hareket bulgularının birlikte yorumlanması hasar yerini belirler.','Refleksin yalnız beyin tarafından gerçekleştiğini düşünmek.','hasar yeri',
 [A('Yolları ayır','Refleks omurilikte, dokunmayı fark etme ve istemli hareket ise beyinde gerçekleşir.','Refleks: omurilik · duyu ve istemli hareket: beyin'),
  A('K ve L hastalarını çöz','K’de duyu ve refleks yoktur, istemli hareket sürer: duyu kolu bozuktur. L’de duyu sürer, refleks ve istemli hareket yoktur: motor kol bozuktur.','K: duyu nöronu · L: motor nöron'),
  A('M ve N hastalarını çöz','M’de duyu ve refleks sürer, istemli hareket yoktur: hareket merkezi bozuktur. N’de duyu yoktur ama refleks sürer: yollar kesilmiştir.','M: hareket merkezi · N: yollar'),
  A('Sırayı yaz','Hastalar K, L, M, N sırasıyla yazılır.','III – I – II – IV')],
 metin='Dört hastada (K, L, M ve N) uzuvlardan birine yapılan dokunma uyarısına karşı dokunmanın hissedilmesi, refleks yanıtı ve o uzvun istemli hareketi incelenmiş, sonuçlar tabloda verilmiştir. Her hastada tek bir yapı hasar görmüştür. Hasar görmüş olabilecek yapılar şunlardır:\nI. Motor nöron\nII. Büyük beyindeki hareket merkezi\nIII. Duyu nöronu\nIV. Omurilik ile beyin arasındaki yollar\nBuna göre, K, L, M ve N hastalarında hasar gören yapılar sırasıyla aşağıdakilerin hangisinde doğru verilmiştir?',
 sekil=SK14,istenen='K, L, M ve N hastalarındaki hasarlı yapılar',ip=['Refleksin çalışıp çalışmadığı hasarın omurilik dışındaki yollarla mı, refleks yayıyla mı ilgili olduğunu gösterir.'],
 bilgi=[B('Duyu ve hareket','duyu bilgisi reseptörlerden sinirlerle merkezi sinir sistemine iletilir · Kaslardaki yanıtı motor nöronlar oluşturur')],puf='Önce refleksi, sonra duyu ve istemli hareketi sına.',**r14)

# ======================= 15 · Omurilik kesiti (orta, şekilli, olumsuz) =======================
SK15=f_omurilik(dict(gri='I',beyaz='II',arka='III',on='IV',dugum='V'))
Q('0015','mss','orta','şekilli','Omurilik yapısı','Omurilik enine kesitinde yapıları ve görevlerini eşleştirir.','Gri madde gövdelerden, beyaz madde miyelinli aksonlardan oluşur; duyu nöron gövdeleri omurilik dışındaki sinir düğümündedir.','Sinir düğümünü motor nöron gövdelerinin bulunduğu yer sanmak.','omurilik kesiti',
 [A('Kesiti çöz','Ortadaki kelebek biçimli bölge gri madde, çevresi beyaz maddedir; kökler omurilikten çıkar.','I: gri madde · II: beyaz madde · III: arka kök · IV: ön kök · V: sinir düğümü'),
  A('Şıkları tek tek sına','Gri madde gövdeleri, beyaz madde aksonları içerir; arka kök duyuyu getirir, ön kök motor impulsu taşır.','Dört ifade doğru'),
  A('Yanlışı bul','Arka kök üzerindeki düğüm duyu nöronlarının gövdelerini içerir, motor nöron gövdelerini değil.','Yanlış: sinir düğümü motor gövde')],
 metin='Şekilde omuriliğin enine kesiti ve ona bağlanan kökler gösterilmiş, bazı yapılar I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre, bu yapılarla ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK15,
 **tek(('V numaralı yapı, motor nöronların hücre gövdelerini içerir.','V numaralı yapı sinir düğümüdür ve duyu nöronlarının hücre gövdelerini içerir'),
       [('I numaralı bölgede nöronların hücre gövdeleri yoğundur.','I numaralı gri madde nöron gövdeleri ve dendritlerden oluşur'),
        ('II numaralı bölge, miyelinli aksonlardan oluşur ve omurilik ile beyin arasında impuls taşır.','II numaralı beyaz madde miyelinli aksonlar içerir ve yukarı ile aşağı yollarla beyne bağlanır'),
        ('III numaralı kök, duyu nöronlarının aksonlarını omuriliğe getirir.','III numaralı arka kök duyu bilgisini omuriliğe taşır'),
        ('IV numaralı kökten motor nöronların aksonları omurilikten çıkar.','IV numaralı ön kök motor aksonları omurilikten kas ve bezlere götürür')],2,hedef=False),
 istenen='Yanlış olan ifade',ip=['Her numarayı gri madde, beyaz madde ya da kök olarak adlandırıp görevini ayrı sına.'],
 bilgi=[B('Omurilik','kelebek biçimli gri madde nöron gövdelerinden, çevresindeki beyaz madde miyelinli aksonlardan oluşur · Duyu nöronları omuriliğe arka kökten girer, motor nöronlar ön kökten çıkar')],puf='Arka kök duyu, ön kök motor; duyu gövdesi düğümdedir.')

# ======================= 16 · Otonom sinir sistemi (orta, tablo, olumsuz) =======================
SK16=tablo_svg(['Organ ya da olay','X uyarıldığında','Y uyarıldığında'],[['Kalp atış hızı','Artar','Azalır'],['Göz bebeği','Genişler','Daralır'],['Bronşlar','Genişler','Daralır'],['Sindirim kanalı hareketleri','Yavaşlar','Hızlanır']])
Q('0016','mss','orta','tablo','Otonom sinir sistemi','Sempatik ve parasempatik sistemin etkilerini tablodan yorumlar.','Sempatik sistem tehlikede hazırlık, parasempatik sistem dinlenmede düzen sağlar; ikisi de istem dışıdır.','Otonom sistemin iskelet kaslarını istemli denetlediğini sanmak.','otonom sinir sistemi',
 [A('Tabloyu oku','X uyarıldığında kalp hızlanıyor, göz bebeği ve bronşlar genişliyor, sindirim yavaşlıyor; Y bunun tersini yapıyor.','X: sempatik · Y: parasempatik'),
  A('Şıkları sına','Sempatik sistem tehlike ve stres anında, parasempatik sistem dinlenmede baskındır; ikisi zıt etki yapar.','Dört ifade tabloyla uyumlu'),
  A('Yanlışı bul','Otonom sistem iç organları istem dışı denetler; iskelet kaslarını istemli denetlemez, bunu somatik sistem yapar.','Yanlış: istemli denetim')],
 metin='Otonom sinir sisteminin iki kolu olan X ve Y, aynı organlara zıt yönde etki eder. Aşağıdaki tabloda bu kollardan her biri uyarıldığında bazı organ ve olaylarda görülen değişimler verilmiştir.\nBuna göre, X ve Y sistemleriyle ilgili aşağıdakilerden hangisi yanlıştır?',
 sekil=SK16,
 **tek(('X ve Y sistemlerinin motor nöronları iskelet kaslarını istemli olarak denetler.','otonom sistem iç organları, düz kasları, kalp kasını ve bezleri istem dışı denetler; iskelet kaslarının istemli denetimi somatik sinir sistemindedir'),
       [('X sistemi sempatik sistemdir ve tehlike anında baskın hâle gelir.','tabloda X’in kalbi hızlandırması ve göz bebeğini genişletmesi sempatik sistemin özelliğidir'),
        ('Y sistemi vücudu dinlenme durumuna yönlendiren etkiler yapar.','Y’nin kalbi yavaşlatması ve sindirimi hızlandırması parasempatik sistemin etkisidir'),
        ('X ve Y, bir organa zıt yönde etki ederek iç dengenin korunmasına katkı sağlar.','tabloda her organa X ve Y zıt yönde etki etmiştir'),
        ('Y sistemi uyarıldığında sindirim kanalındaki hareketler hızlanır.','tabloda Y uyarıldığında sindirim kanalı hareketleri hızlanmıştır')],3,hedef=False),
 istenen='Yanlış olan ifade',ip=['Her ifadeyi tabloyla ve otonom sistemin görevleriyle karşılaştır.'],
 bilgi=[B('Otonom sinir sistemi','otonom sinir sistemi sempatik ve parasempatik olmak üzere iki koldan oluşur · Bu kollar çevresel sinir sisteminin parçasıdır')],puf='Tablodaki zıt etkiler hangi kolun hangisi olduğunu gösterir.')

# ======================= 17 · Beyin öncülleri (orta, şekilli, öncüllü) =======================
SK17=f_beyin(dict(buyuk='I',beyincik='II',ara='III',omsogan='IV',orta='V'))
d17={'I':(True,'büyük beyin yarım kürelerinin istemli hareket merkezleri vücudun karşı tarafını denetler'),
     'II':(True,'beyincik denge ve kas hareketlerinin koordinasyonunu sağlar'),
     'III':(True,'ara beyindeki hipotalamus açlık, susuzluk ve vücut sıcaklığı gibi dengeleri düzenler')}
r17=onc(d17,4)
Q('0017','beyin','orta','şekilli','Beyin bölümlerinin görevleri','Şekildeki beyin bölümlerinin görevlerini değerlendirir.','Büyük beyin karşı tarafı denetler, beyincik koordinasyon, hipotalamus iç denge sağlar.','Çaprazlanmayı bilmemek; beyincik ile hipotalamusun görevlerini karıştırmak.','beyin öncülleri',
 [A('Yapıları tanı','I büyük beyin, II beyincik, III ara beyin olarak tanınır.','I: büyük beyin · II: beyincik · III: ara beyin'),
  A('Büyük beyni sına','Bir yarım kürenin hareket merkezi vücudun karşı yanındaki kasları denetler.','I: doğru'),
  A('Diğerlerini sına','Beyincik denge ve koordinasyonu, ara beyin iç dengeleri düzenler.','II: doğru · III: doğru')],
 metin='Şekilde insan beyninin yandan kesit görünümü verilmiş ve bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır.\nBuna göre,\nI. I numaralı yapının sağ yarım küresindeki hareket merkezi, vücudun sol tarafındaki kasların istemli hareketini denetler.\nII. II numaralı yapı, vücudun dengesinin sağlanmasında ve kas hareketlerinin koordinasyonunda görev alır.\nIII. III numaralı yapıda bulunan merkezler, açlık, susuzluk ve vücut sıcaklığı gibi iç dengelerin düzenlenmesinde rol oynar.\nifadelerinden hangileri doğrudur?',
 sekil=SK17,istenen='Doğru olan öncüller',ip=['Önce numaralı yapıları adlandır, sonra her birinin görevini ayrı ayrı sına.'],
 bilgi=[B('Beyin bölümleri','beyin; büyük beyin, ara beyin, orta beyin, beyincik ve omurilik soğanından oluşur · Büyük beyin sağ ve sol yarım küreden oluşur')],puf='Önce yapıyı adlandır, sonra görevi sına.',**r17)

# ======================= 18 · İnme vakası (zor, öncüllü) =======================
d18={'I':(False,'sol yarım küre hasarında vücudun sağ tarafı etkilenir; sol tarafın felci sağ yarım küre hasarını düşündürür'),
     'II':(True,'sol kol ve bacaktaki istemli hareket kaybı, sağ yarım küredeki hareket merkezinin hasarıyla açıklanabilir'),
     'III':(True,'diz kapağı refleksi omurilik düzeyinde gerçekleştiği için beyindeki hasar bu refleksi bozmaz')}
r18=onc(d18,4)
Q('0018','deney','orta','öncüllü','İnme sonrası bulgular','Çaprazlanmayı ve refleksin omurilik merkezli olduğunu bir vakada birleştirir.','Beyin yarım küreleri karşı tarafı denetler; refleks omurilikte gerçekleşir.','Hasarı aynı taraftaki yarım küreye yazmak; refleksin de bozulmasını beklemek.','inme vakası',
 [A('Bulguları ayır','Sol kol ve bacak istemli hareket etmiyor; dokunma, refleks, solunum ve kalp normal.','İstemli hareket yok · refleks var · yaşamsal olaylar normal'),
  A('Çaprazlanmayı uygula','Vücudun sol tarafını sağ yarım küre denetler; bu nedenle sol yanın felci sağ yarım küre hasarını düşündürür.','I: yanlış · II: doğru'),
  A('Refleksi yorumla','Diz kapağı refleksinin sürmesi, refleks merkezinin omurilikte olduğunu gösterir.','III: doğru')],
 metin='Beyninde kanama geçiren bir hastanın sol kolunu ve sol bacağını istemli olarak hareket ettiremediği saptanmıştır. Hastanın dokunma duyusu ve diz kapağı refleksi normaldir; kalp atışı ve solunumunda da bir sorun yoktur.\nBu hastayla ilgili,\nI. Hasar, beynin sol yarım küresindeki hareket merkezindedir.\nII. Hasar, beynin sağ yarım küresindeki hareket merkezinde olabilir.\nIII. Diz kapağı refleksinin sürmesi, bu refleksin omurilik düzeyinde gerçekleşmesiyle açıklanabilir.\nifadelerinden hangileri doğrudur?',
 istenen='Doğru olan öncüller',ip=['Yarım kürelerin vücudun hangi yanını denetlediğini ve refleksin nerede merkezlendiğini düşün.'],
 bilgi=[B('Beyin ve omurilik','büyük beyin sağ ve sol yarım küreden oluşur · Omurilik beyne bağlanır ve onunla birlikte merkezi sinir sistemini oluşturur')],puf='Felç hasarın karşı yarım küresini işaret eder.',**r18)

# ======================= 19 · Kurbağa deneyi (zor, öncüllü) =======================
d19={'I':(True,'beyni tahrip edilmiş kurbağada bacağın çekilmesi, refleks için beynin gerekmediğini gösterir'),
     'II':(True,'arka kök ve ön kök kesilen gruplarda yanıt olmadığından her ikisinin de refleks yayı için gerekli olduğu sonucuna varılır'),
     'III':(False,'arka kökün duyu, ön kökün motor görevli olduğu bu sonuçlardan kesin olarak çıkarılamaz, bu bilgi ek gözlem gerektirir')}
r19=onc(d19,2)
Q('0019','deney','zor','öncüllü','Refleks deneyi yorumlama','Refleks deneyinin sonuçlarından kesin çıkarımları ayırt eder.','Deney yalnız gözlenen sonuçları kanıtlar; görev atamak ek gözlem ister.','Bilinen bilgiyi deney sonucundan çıkarılmış sanmak.','kurbağa deneyi',
 [A('Gruplara bak','Dört grupta bacağın çekilip çekilmediğine bakılmıştır.','Sağlam: çeker · arka kök kesik: çekmez · ön kök kesik: çekmez · beyinsiz: çeker'),
  A('Birinci öncülü sına','Beyni tahrip edilmiş grup yanıt verdiğine göre refleks için beyin gerekmez.','I: doğru'),
  A('İkinci öncülü sına','Her iki kök kesildiğinde de yanıt kaybolur; iki kök de yayın parçasıdır.','II: doğru'),
  A('Üçüncü öncülü sına','Hangi kökün duyu, hangisinin motor olduğu bu gözlemlerden çıkmaz; duyu ve hareket ayrıca incelenmelidir.','III: yanlış')],
 metin='Bir araştırmacı, aynı türden kurbağaları dört gruba ayırarak arka bacağın derisine asit emdirilmiş pamuk temas ettirmiş ve bacağın çekilip çekilmediğini gözlemiştir.\n1. grup: Sağlam kurbağalar; bacak çekilmiştir.\n2. grup: Arka kökler kesilmiştir; bacak çekilmemiştir.\n3. grup: Ön kökler kesilmiştir; bacak çekilmemiştir.\n4. grup: Beyni tahrip edilmiş, omuriliği sağlam kurbağalar; bacak çekilmiştir.\nBu deneyin sonuçlarına bakılarak,\nI. Bacağı çekme refleksinin gerçekleşmesi için beynin sağlam olması gerekmez.\nII. Hem arka kökler hem de ön kökler refleksin gerçekleşmesi için gereklidir.\nIII. Arka kökler duyu nöronlarının, ön kökler motor nöronların aksonlarını taşır.\nifadelerinden hangilerine kesin olarak ulaşılabilir?',
 istenen='Deney sonuçlarından kesin çıkarılabilen öncüller',ip=['Her öncülün, dört grubun gözlemlerinden doğrudan çıkıp çıkmadığına bak.'],
 bilgi=[B('Deney sonucu yorumlama','bir deneyden çıkarılacak sonuçlar yalnız gözlemlenen verilere dayanır')],puf='Sonuç, gözlemin gösterdiğinden fazlasını söylemez.',**r19)

# ======================= 20 · Zarlar ve BOS (orta, öncüllü, olumsuz) =======================
d20={'I':(False,'beyin-omurilik sıvısı hem beyin boşluklarında hem omurilik kanalında bulunur'),
     'II':(True,'beyin-omurilik sıvısı merkezi sinir sistemini darbelere karşı korur'),
     'III':(True,'merkezi sinir sistemi, meninks adı verilen üç katlı zarla örtülüdür')}
r20=onc(d20,0,hedef=False)
Q('0020','mss','orta','öncüllü','Merkezi sinir sisteminin korunması','Beyin ve omuriliği koruyan yapıları ayırt eder.','Beyin kafatasıyla, omurilik omurgayla korunur; zarlar ve BOS ek koruma sağlar.','Sıvının yalnız beyinde bulunduğunu sanmak.','MSS koruması',
 [A('Koruma katmanlarını sırala','Merkezi sinir sistemi kemik, zar ve sıvıyla korunur.','Kemik · meninks · beyin-omurilik sıvısı'),
  A('Birinci öncülü sına','Beyin-omurilik sıvısı beyin boşluklarında ve omurilik kanalında bulunur.','I: yanlış'),
  A('Diğerlerini sına','Meninks üç katlı zardır; sıvı darbeyi sönümler.','II: doğru · III: doğru')],
 metin='Merkezi sinir sistemi, hayati önemi nedeniyle birden fazla yapı tarafından korunur. Beyin ve omurilik çevrelerindeki kemik yapıların içinde yer alır, ayrıca zarlar ve sıvıyla da sarılmıştır.\nBu korumayla ilgili,\nI. Beyin-omurilik sıvısı yalnız beyin boşluklarında bulunur, omurilik kanalında bulunmaz.\nII. Beyin-omurilik sıvısı, merkezi sinir sistemini darbelere karşı korur.\nIII. Merkezi sinir sistemi, meninks adı verilen üç katlı zarla örtülüdür.\nifadelerinden hangileri yanlıştır?',
 istenen='Yanlış olan öncül',ip=['Beyin ve omuriliğin hangi kemik yapılarla korunduğunu ayır.'],
 bilgi=[B('Merkezi sinir sistemi','merkezi sinir sistemi beyin ve omurilikten oluşur · Bu yapıların korunmasında kemik, zar ve sıvı rol alır')],puf='Sıvı, beyin ve omurilik için ortak koruyucudur.',**r20)

# ======================= bitiş =======================
for q in P.ANA: q['kardes']=None
P.yaz(os.path.join(GD,'sinir-1.json'),os.path.join('/tmp','bos-sinir.json'))
tipler={}
for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji, MEB 11. sınıf.',kartlar=KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','absinir.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
