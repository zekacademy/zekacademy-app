"""AYT Biyoloji · Hücresel Solunum · 20 soru (kardeş yok, ipucu 1). Şekiller TikZ; tüm sayısal değerler modelden hesaplanıp assert edilir."""
import sys,os,math,json
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
from fractions import Fraction as Fr
from collections import Counter
KONU_AD='Hücresel Solunum'; KK='abio|Hücresel Solunum'
P=Parti('hucresolunum',KONU_AD,KK,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KY='ÖSYM 2018–2026 AYT Biyoloji dağılımı · MEB 12. sınıf biyoloji'
TIPK={}
TIPAD={'hs-yer':'Hücresel solunumun gerçekleştiği yerler','hs-basamak':'Solunum basamakları ve ürünleri','hs-ets':'Elektron taşıma sistemi ve kemiozmoz','hs-ferm':'Fermantasyon','hs-atp':'ATP ve taşıyıcı hesapları','hs-deney':'Solunum deney düzenekleri','hs-grafik':'Solunum grafikleri','hs-karsilastir':'Solunum türlerinin karşılaştırılması'}
def kartla(no,alt,fikir,tuzak,z,kalip,adim,tipId,tip):
    tip=TIPAD[tipId]
    kart(f'K-ABHS-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY); return f'K-ABHS-{no:02d}'

# ===================== MODEL (tek veri kaynağı) =====================
GL=dict(harcanan=2,uretilen=4,net=2,NADH=2,piruvat=2,CO2=0)          # 1 glikoz, glikoliz
PO=dict(NADH=2,CO2=2,asetil=2)                                        # 1 glikozdan 2 pirüvat → piruvat oksidasyonu
KT=dict(NADH=3,FADH2=1,ATP=1,CO2=2)                                   # Krebs döngüsünün 1 turu (1 asetil CoA)
KG=dict(NADH=KT['NADH']*PO['asetil'],FADH2=KT['FADH2']*PO['asetil'],ATP=KT['ATP']*PO['asetil'],CO2=KT['CO2']*PO['asetil'])  # 1 glikoz
assert GL['uretilen']-GL['harcanan']==GL['net']==2
assert PO['CO2']+KG['CO2']==6 and KG==dict(NADH=6,FADH2=2,ATP=2,CO2=4)
ETS_N,ETS_F=3,2                                                       # soruda verilen dönüşüm katsayıları (NADH→3, FADH2→2)
FERM=dict(laktik=dict(laktat=2,CO2=0),alkol=dict(etanol=2,CO2=2))     # 1 glikoz
OKS_CO2=6

def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKS='-{Stealth[length=2.2mm,width=1.8mm]}'
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)); return sira
def q(no,ad,**k):
    k['tip']=TIPAD[k['tipId']]; mk(P,no,ad=ad,adim=len(ad),**k)

# ---- öncüllü yardımcıları ----
ONC7=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def etiket(s,canon,rom):
    s=sorted(s,key=rom.index)
    if len(s)==1: return 'Yalnız '+s[0]
    if len(s)==len(rom): return ', '.join(s[:-1])+' ve '+s[-1]
    return ' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1]
def kume_of(lbl,rom):
    if lbl.startswith('Yalnız '): return {lbl[7:]}
    return {x for x in lbl.replace(' ve ',', ').split(', ')}
def onc_sec(T,harf,rom=('I','II','III'),canon=None):
    canon=canon or ONC7
    d=etiket(T,canon,list(rom)); p=canon.index(d); i='ABCDE'.index(harf)
    assert p-i>=0 and len(canon[p+1:p+5-i])==4-i,(d,harf)
    sira=canon[p-i:p]+[d]+canon[p+1:p+5-i]; assert len(sira)==5
    return d,sira
def onc_cel(T,sira,d,n,rom=('I','II','III'),olumsuz=False):
    U=set(rom); yan=[]
    for o in sira:
        if o==d: continue
        S=kume_of(o,rom); ex=sorted(S-T,key=rom.index); ms=sorted(T-S,key=rom.index); pr=[]
        for e in ex: pr.append(f'{e} öncülü kökteki koşulu sağlamadığı hâlde seçilmiş: {n[e]}')
        for e in ms: pr.append(f'{e} öncülü kökteki koşulu sağladığı hâlde dışarıda bırakılmış: {n[e]}')
        tur='dikkat' if (olumsuz and S==U-T) else 'bilgi'
        txt=' '.join(x if x.endswith('.') else x+'.' for x in pr)
        if tur=='dikkat': txt='Kökteki olumsuzluğu gözden kaçırıp tersini seçmek. '+txt
        yan.append((o,txt,tur))
    return yan
def onc_adim(T,n,rom=('I','II','III'),koşul='koşulu sağlar'):
    ad=[]
    for e in rom: ad.append(A(f'{e}. öncülü değerlendir',n[e],f'{e}: '+('koşulu sağlar' if e in T else 'koşulu sağlamaz')))
    return ad

# ===================== ŞEKİL YARDIMCILARI =====================
def grafik(egriler,xmax,ymax,xt,yt,xlab,ylab,W=6.0,Hh=3.4,etik=(),kes=(),ytlab=None):
    sx=W/xmax; sy=Hh/ymax; b=[]
    b.append(f'\\draw[{OKS},line width=1pt] (0,0)--({W+.35},0);\\draw[{OKS},line width=1pt] (0,0)--(0,{Hh+.35});')
    for x in xt: b.append(f'\\draw (%.3f,0)--(%.3f,-.09) node[below,font=\\footnotesize] {{{x}}};'%(x*sx,x*sx))
    for y in yt:
        lab=(ytlab or {}).get(y,y); b.append(f'\\draw (0,%.3f)--(-.09,%.3f) node[left,font=\\footnotesize] {{{lab}}};'%(y*sy,y*sy))
    b.append(f'\\node[font=\\small] at ({W/2},-.85) {{{xlab}}};\\node[font=\\small,rotate=90] at (-1.0,{Hh/2}) {{{ylab}}};')
    for pts,stil in egriler:
        c=' -- '.join('(%.3f,%.3f)'%(x*sx,y*sy) for x,y in pts); b.append(f'\\draw[{stil}] {c};')
    for x0,y0,s in kes:  # kesikli kılavuz çizgileri (x, y)
        if y0 is None: b.append('\\draw[dashed,line width=.6pt] (%.3f,0)--(%.3f,%.3f);'%(x0*sx,x0*sx,Hh))
        else: b.append('\\draw[dashed,line width=.6pt] (0,%.3f)--(%.3f,%.3f);'%(y0*sy,x0*sx,y0*sy))
    for x,y,t,pos in etik: b.append('\\node[font=\\small\\bfseries,%s] at (%.3f,%.3f) {%s};'%(pos,x*sx,y*sy,t))
    return '\n'.join(b)

def sise(x,y,ad,kap_ad,kap_tur,damla,boy=2.0):
    """Respirometre: kapalı şişe (içinde çimlenen tohum + küçük kap) ve kılcal boru. (x,y) şişenin sol alt köşesi."""
    b=[]
    w=2.0; h=boy
    b.append(f'\\draw[line width=1.3pt,rounded corners=6pt] ({x},{y+h}) -- ({x},{y}) -- ({x+w},{y}) -- ({x+w},{y+h});')
    b.append(f'\\draw[line width=1.3pt] ({x},{y+h}) -- ({x+.35},{y+h}) ;\\draw[line width=1.3pt] ({x+w-.35},{y+h}) -- ({x+w},{y+h});')
    # tıpa
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15] ({x+.3},{y+h}) rectangle ({x+w-.3},{y+h+.28});')
    # tohumlar
    for i,(tx,ty) in enumerate([(.35,.18),(.7,.22),(1.05,.17),(1.4,.23),(1.7,.17),(.55,.5),(1.2,.5),(1.55,.5)]):
        b.append(f'\\draw[line width=.7pt,fill=black,fill opacity=.18] ({x+tx},{y+ty}) ellipse (.15 and .09);')
    # kap
    kx=x+.7; ky=y+.78
    b.append(f'\\draw[line width=1pt] ({kx},{ky+.45})--({kx},{ky})--({kx+.6},{ky})--({kx+.6},{ky+.45});')
    b.append(f'\\draw[line width=.6pt,fill=black,fill opacity=.10] ({kx+.02},{ky+.02}) rectangle ({kx+.58},{ky+.26});')
    b.append(f'\\node[font=\\small,anchor=west] at ({x+w+.15},{y+.45}) {{{kap_ad}}};')
    b.append(f'\\draw[line width=.5pt] ({x+w+.12},{y+.45}) -- ({kx+.62},{ky+.15});')
    # kılcal boru
    ty=y+h+.14; L=3.4
    b.append(f'\\draw[line width=1pt] ({x+w/2},{y+h+.28}) -- ({x+w/2},{ty}) -- ({x+w/2+L+.6},{ty});')
    b.append(f'\\draw[line width=1pt] ({x+w/2},{ty-.16}) -- ({x+w/2+L+.6},{ty-.16});')
    b.append(f'\\draw[line width=1pt] ({x+w/2},{y+h+.28})--({x+w/2},{ty-.16});')
    for k in range(0,8): b.append(f'\\draw[line width=.5pt] ({x+w/2+.9+.4*k},{ty-.16}) -- ({x+w/2+.9+.4*k},{ty-.28});')
    b.append(f'\\draw[line width=.5pt,fill=black,fill opacity=.6] ({x+w/2+.9+.4*damla},{ty-.08}) ellipse (.14 and .09);')
    b.append(f'\\node[font=\\normalsize\\bfseries] at ({x-.45},{y+h/2}) {{{ad}}};')
    return '\n'.join(b)

def erlen(x,y,sivi,yag,ad,alt_yazi,kire_bulanik):
    """Erlenmayer + tıpa + çıkış borusu + kireç suyu kabı. (x,y)= taban orta."""
    b=[]; wb=1.0; wn=.3; hb=1.15; hn=.65
    b.append(f'\\draw[line width=1.2pt] ({x-wb},{y})--({x+wb},{y})--({x+wn},{y+hb})--({x+wn},{y+hb+hn});')
    b.append(f'\\draw[line width=1.2pt] ({x-wb},{y})--({x-wn},{y+hb})--({x-wn},{y+hb+hn});')
    sy=y+.85; ww=wb-(wb-wn)*(.85/hb)
    b.append(f'\\fill[black,fill opacity=.10] ({x-wb},{y})--({x+wb},{y})--({x+ww},{sy})--({x-ww},{sy})--cycle;')
    if yag: b.append(f'\\fill[black,fill opacity=.38] ({x-ww},{sy})--({x+ww},{sy})--({x+ww-.03},{sy+.13})--({x-ww+.03},{sy+.13})--cycle;')
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.18] ({x-wn-.05},{y+hb+hn-.02}) rectangle ({x+wn+.05},{y+hb+hn+.22});')
    # boru: tıpadan yukarı, sağa, kireç suyu kabına
    ty=y+hb+hn+.12
    b.append(f'\\draw[line width=1pt] ({x},{ty}) -- ({x},{ty+.45}) -- ({x+1.35},{ty+.45}) -- ({x+1.35},{y+.55});')
    kx=x+1.35
    b.append(f'\\draw[line width=1.1pt] ({kx-.42},{y+.9})--({kx-.42},{y})--({kx+.42},{y})--({kx+.42},{y+.9});')
    b.append(f'\\fill[black,fill opacity={.38 if kire_bulanik else .06}] ({kx-.40},{y+.02}) rectangle ({kx+.40},{y+.62});')
    b.append(f'\\node[font=\\normalsize\\bfseries] at ({x-.1},{y-.35}) {{{ad}}};')
    b.append(f'\\node[font=\\footnotesize,text width=3.1cm,align=center,anchor=north] at ({x},{y-.7}) {{{alt_yazi}}};')
    return '\n'.join(b)

# ===================== SORULAR =====================
SIRA={}   # no → soru  (kimlik numarası, yazım sırası değil)

# -------- N1 · Mitokondri bölümleri · kolay · şekil (şema)
k1=kartla(1,'Mitokondri bölümleri ve Krebs yeri','Mitokondrinin matriks, iç zar ve zarlar arası boşluk bölümleri biçimle ayırt edilir; matrikste çözünmüş enzimlerle yürüyen basamaklar ile zarda gerçekleşen basamaklar farklı yerlerdedir.','Krebs döngüsünü zar yapılarıyla ya da dış zarla ilişkilendirmek; DNA’yı gösteren numarayı bölge sanmak.','kolay','şekilli',2,'hs-yer','Mitokondri bölümleri ve hücresel solunum yeri')
def mito():
    a,b_=2.55,1.35
    def yt(x): return b_*math.sqrt(1-(x/a)**2)
    top=[-1.55,0.3,1.7]; bot=[-0.9,0.9]; hw=.14
    def seg(x0,x1,n=3): return [(x0+(x1-x0)*i/n,yt(x0+(x1-x0)*i/n)) for i in range(n+1)]
    cur=-2.5; path=[(-a,0.0),(-2.5,yt(-2.5))]
    for f in top:
        for p in seg(cur,f-hw,3)[1:]: path.append(p)
        path+= [(f-hw,-.2),(f+hw,-.2),(f+hw,yt(f+hw))]; cur=f+hw
    for p in seg(cur,2.5,3)[1:]: path.append(p)
    path.append((a,0.0)); path.append((2.5,-yt(2.5)))
    cur=2.5
    for f in sorted(bot,reverse=True):
        for p in seg(cur,f+hw,3)[1:]: path.append((p[0],-p[1]))
        path+= [(f+hw,.2),(f-hw,.2),(f-hw,-yt(f-hw))]; cur=f-hw
    for p in seg(cur,-2.5,3)[1:]: path.append((p[0],-p[1]))
    return path
MP=mito()
def mito_svg(num):
    """num: sözlük {'matriks':'I','dis':'II','arasi':'III','ic':'IV','dna':'V'}"""
    b=[]
    b.append('\\draw[line width=1.6pt] (0,0) ellipse (3 and 1.75);')
    b.append('\\draw[line width=1.6pt,rounded corners=2.5pt] '+' -- '.join('(%.3f,%.3f)'%p for p in MP)+' -- cycle;')
    b.append('\\draw[line width=1pt] (-.3,-.62) circle (.2);\\fill (-.5,-.55) circle (.04);\\fill (-.1,-.7) circle (.04);\\fill (-.27,-.35) circle (.04);')
    for (rx,ry) in [(.9,.6),(1.2,.35),(-1.9,.2),(-2.1,-.2),(.1,-.85)]: b.append(f'\\fill ({rx},{ry}) circle (.035);')
    def lab(t,tx,ty,ex,ey): return f'\\node[font=\\normalsize\\bfseries] at ({tx},{ty}) {{{t}}};\\draw[{OKS},line width=.8pt] ({tx+(ex-tx)*.12:.3f},{ty+(ey-ty)*.12:.3f})--({ex},{ey});'
    # dış zar
    th=math.radians(165); b.append(lab(num['dis'],-4.1,1.6,3*math.cos(th),1.75*math.sin(th)))
    # zarlar arası boşluk (üst-sağ)
    th=math.radians(52); b.append(lab(num['arasi'],3.6,2.4,2.775*math.cos(th),1.55*math.sin(th)))
    # iç zar (alt-sol, düz kısım)
    th=math.radians(205); b.append(lab(num['ic'],-3.9,-1.9,2.55*math.cos(th),1.35*math.sin(th)))
    # matriks
    b.append(lab(num['matriks'],1.2,2.55,1.0,.55))
    # DNA
    b.append(lab(num['dna'],1.9,-2.4,-.14,-.78))
    return tk('\n'.join(b),.85)
NUM1=dict(matriks='I',dis='II',arasi='III',ic='IV',dna='V')
SK1=mito_svg(NUM1)
MIT=B('Mitokondrinin bölümleri','çift zarlı organeldir: düz dış zar ile kıvrımlar (krista) yapan iç zar bulunur · İç zarın çevrelediği sıvı bölgeye matriks, iki zar arasındaki aralığa zarlar arası boşluk denir · Matriksteki halkasal DNA ve ribozomlar mitokondrinin kendi proteinlerini yapmasını sağlar')
q('0001',tipId='hs-yer',tip='Mitokondri bölümleri ve hücresel solunum yeri',z='kolay',alt='Solunumun gerçekleştiği yerler',kaz='Mitokondri şemasında bölümleri tanıyıp Krebs döngüsünün yerini belirler.',kalip='şekilli',
 kart=f'{k1} (mitokondri bölümleri) · numaralı şemada Krebs yeri',
 metin='Şekilde bir mitokondrinin yapısı şematik olarak gösterilmiş ve bazı bölümleri I, II, III, IV ve V ile numaralandırılmıştır. Glikozdan oluşan pirüvik asit mitokondriye girer, asetil CoA’ya dönüşür ve bu madde hücresel solunumun bir sonraki basamağında yıkılır.\nBuna göre, Krebs döngüsü tepkimelerinin gerçekleştiği bölüm numaralandırılmış yerlerden hangisidir?',
 dogru='I',sira=['I','II','III','IV','V'],
 yan=[('II','II numaralı yapı dış zardır; madde geçişini denetler, Krebs tepkimelerinin yeri değildir.','bilgi'),
      ('III','III numaralı bölge zarlar arası boşluktur; burada protonlar birikir ama Krebs tepkimeleri gerçekleşmez.','bilgi'),
      ('IV','IV numaralı yapı iç zardır; elektron taşıma sistemi bu zarda bulunur, Krebs döngüsü ise zarda değil sıvı bölgede yürür.','bilgi'),
      ('V','V numaralı yapı halkasal mitokondri DNA’sıdır; bir bölge değil bir kalıtım materyalidir ve Krebs tepkimelerinin yeri sayılmaz.','bilgi')],
 istenen='Krebs döngüsünün gerçekleştiği bölümün numarası.',
 ip=['Şemadaki zarları ve zarların çevrelediği bölgeleri biçimlerinden tanı; hangi bölgede çözünmüş hâlde enzimlerin bulunabileceğini düşün.'],
 bilgi=[MIT],
 ad=[A('Bölümleri tanı','Dıştaki düz zar dış zar, kıvrımlı zar iç zar, iki zar arası boşluk zarlar arası boşluktur. İç zarın içindeki sıvı matrikstir.','II: dış zar · III: zarlar arası boşluk · IV: iç zar · I: matriks · V: DNA'),
     A('Krebs yerini hatırla','Krebs döngüsü enzimleri matriks sıvısında çözünmüş hâlde bulunur; zara gömülü değildir.','Krebs → matriks'),
     A('Numarayı eşle','Matriks şemada I ile gösterilmiştir.','Cevap: I')],
 puf='Zara gömülü basamaklar (ETS) zarda, çözünmüş enzimle yürüyenler (Krebs) mitokondri sıvısında gerçekleşir.',sekil=SK1)
SIRA[1]=1

# -------- N2 · Glikoliz yanlıştır · kolay
k2=kartla(2,'Glikolizin genel özellikleri','Glikoliz sitoplazmada, oksijensiz ortamda da yürüyen ve substrat düzeyinde ATP üreten ilk basamaktır; oksijen gerektirdiğini sanmak sık yanılgıdır.','Glikolizi mitokondri ya da oksijenle ilişkilendirmek; net ve brüt ATP’yi karıştırmak.','kolay','düz',2,'hs-basamak','Glikolizin özellikleri')
GLB=B('Glikoliz','glikozun, üç karbonlu iki pirüvik asit molekülüne yıkıldığı ilk basamaktır · Tüm canlı hücrelerde bulunur · Bu sırada ATP harcanır, ATP üretilir ve NAD⁺ indirgenir')
q('0002',tipId='hs-basamak',tip='Glikolizin özellikleri',z='kolay',alt='Glikoliz',kaz='Glikolizin yeri, koşulu ve ürünleriyle ilgili yanlış ifadeyi belirler.',kalip='düz',
 kart=f'{k2} (glikoliz özellikleri) · yanlış ifadeyi bulma',
 metin='Hücresel solunum, glikozun hücre içinde basamaklar hâlinde yıkılarak ATP elde edilmesidir. Bu basamaklardan ilki olan glikoliz, hem oksijenli solunum yapan hem de fermantasyon yapan hücrelerde ortak olarak görülür.\nBuna göre, glikolizle ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru='Glikozun yıkılabilmesi için ortamda oksijen bulunması gerekir.',
 sira=yer('C','Glikozun yıkılabilmesi için ortamda oksijen bulunması gerekir.',['Sitoplazmada gerçekleşir.','Bir glikozdan iki pirüvik asit molekülü oluşur.','ATP, substrat düzeyinde fosforilasyonla sentezlenir.','NAD⁺ indirgenerek NADH’a dönüşür.']),
 yan=[('Sitoplazmada gerçekleşir.','Kökün yanlış ifadeyi istediğini gözden kaçırıp doğru bir ifadeyi seçmek; glikoliz gerçekten sitoplazmada gerçekleşir.','dikkat'),
      ('Bir glikozdan iki pirüvik asit molekülü oluşur.','Doğru bir ifadeyi seçmek; üç karbonlu glikozun yıkımıyla iki pirüvik asit oluşur, bu da ortak bir bilgidir.','dikkat'),
      ('ATP, substrat düzeyinde fosforilasyonla sentezlenir.','Doğru bir ifadeyi yanlış sanmak; glikolizde ATP, fosfat grubunun bir bileşikten doğrudan ADP’ye aktarılmasıyla yapılır.','bilgi'),
      ('NAD⁺ indirgenerek NADH’a dönüşür.','Doğru bir ifadeyi yanlış sanmak; glikolizde glikozdan alınan hidrojenler NAD⁺’yı NADH’a indirger.','bilgi')],
 istenen='Glikolizle ilgili yanlış ifade.',
 ip=['Kök yanlış ifadeyi istiyor; glikolizin fermantasyon yapan hücrelerde de gerçekleştiğini hatırlayarak ifadeleri tek tek sına.'],
 bilgi=[GLB],
 ad=[A('Kökü oku','Yanlış ifade isteniyor; doğru olanlar tek tek elenecek.','Aranan: yanlış ifade'),
     A('Doğruları ele','Glikoliz sitoplazmada yürür, bir glikozdan iki pirüvik asit verir, ATP’yi substrat düzeyinde üretir ve NAD⁺’yı indirger.','4 ifade doğru'),
     A('Koşulu sına','Glikoliz fermantasyonda da gerçekleşir; fermantasyon oksijensiz ortamda olduğundan glikoliz oksijen gerektirmez.','Oksijen şartı yanlış'),
     A('Sonuç','Yanlış olan, oksijen gerektiğini söyleyen ifadedir.','Yanlış: oksijen şartı')],
 puf='Hem oksijenli solunumda hem fermantasyonda ortak olan basamak, oksijen gerektirmeyen glikolizdir.')
SIRA[2]=2

# -------- N3 · Kültür tablosu · kolay · öncüllü (tablo)
k3=kartla(3,'Ürünlerden solunum türünü çıkarma','Ortamda biriken ürün, hücrenin NADH’ı hangi yolla yükseltgediğini gösterir: H₂O oksijenli solunumu (ETS), laktik asit ve etil alkol fermantasyonu işaret eder.','Her ürünü oksijenli solunumla ilişkilendirmek; fermantasyonda NAD⁺’nın yenilenmediğini sanmak.','kolay','öncüllü',3,'hs-karsilastir','Ürünlerden solunum türünü belirleme')
T3={'I':False,'II':True,'III':True}
N3={'I':'X kültüründe CO₂ ve H₂O birikmiştir; bu oksijenli solunumdur ve NAD⁺, NADH’ın elektronlarını ETS yoluyla oksijene aktarmasıyla yenilenir, fermantasyon basamağı yoktur.',
    'II':'Y kültüründe etil alkol ve CO₂ birikmiştir; alkol fermantasyonunda NADH, pirüvattan türeyen asetaldehiti etil alkole indirger ve NAD⁺ yenilenir.',
    'III':'Z kültüründe laktik asit birikmiştir; laktik asit fermantasyonunda NADH, pirüvatı laktik aside indirger ve NAD⁺ yenilenir.'}
d3,s3=onc_sec({k for k,v in T3.items() if v},'E')
SK3=tablo_svg(['Kültür','Ortamda biriken ürünler'],[['X','CO₂ ve H₂O'],['Y','Etil alkol ve CO₂'],['Z','Laktik asit']])
q('0003',tipId='hs-karsilastir',tip='Ürünlerden solunum türünü belirleme',z='kolay',alt='Oksijenli solunum ve fermantasyon',kaz='Ortamdaki ürünlerden fermantasyon yapan kültürleri belirler.',kalip='tablo',
 kart=f'{k3} (ürünlerden tür) · X, Y, Z kültürleri',
 metin='Aynı miktarda glikoz verilen üç hücre kültürüne ait ortamlarda bir süre sonra biriken ürünler tabloda verilmiştir.\nI. X\nII. Y\nIII. Z\nBuna göre, yukarıdaki kültürlerden hangilerinde glikolizde oluşan NADH’ın NAD⁺’ya yükseltgenmesi fermantasyon basamağında gerçekleşmiştir?',
 dogru=d3,sira=s3,yan=onc_cel({k for k,v in T3.items() if v},s3,d3,N3),
 istenen='NAD⁺’nın fermantasyonla yenilendiği kültürler.',
 ip=['Her ürünün hangi solunum türünün sonunda ortaya çıktığını düşün; ürün H₂O mu, yoksa pirüvattan türeyen bir madde mi?'],
 bilgi=[B('NAD⁺’nın yenilenmesi','glikolizin sürmesi için NADH’ın yeniden NAD⁺’ya yükseltgenmesi gerekir · Oksijenli solunumda bu iş ETS’de, fermantasyonda ise pirüvat (ya da türevi) indirgenerek yapılır')],
 ad=onc_adim({k for k,v in T3.items() if v},N3)+[A('Sonuç','Fermantasyonla NAD⁺ yenileyenler Y ve Z kültürleridir.','Doğru: II ve III')],
 puf='Ortamda H₂O oluşuyorsa ETS çalışmıştır; laktik asit ya da etil alkol varsa NAD⁺ fermantasyonla yenilenmiştir.',sekil=SK3)
SIRA[3]=3

# -------- N4 · ETS yanlış öncüller · orta · öncüllü + olumsuz
k4=kartla(4,'Elektron taşıma sistemi (ETS) ve kemiozmoz','NADH ve FADH₂ elektronlarını ETS elemanlarına verir; elektronlar zincirde taşınırken pompalanan H⁺’lar ATP sentazdan geçerken ATP üretilir ve son elektron alıcısı O₂’dir.','Elektronların doğrudan oksijene aktarıldığını sanmak; ETS’de substrat düzeyinde ATP üretildiğini düşünmek.','orta','öncüllü',3,'hs-ets','Elektron taşıma sistemi ve kemiozmoz')
T4={'I':True,'II':False,'III':False}   # kökte "yanlış" aranıyor → koşulu sağlayan = yanlış olan
N4={'I':'NADH ve FADH₂ elektronlarını oksijene doğrudan vermez; elektronlar ETS elemanları üzerinden sırayla taşınır ve en sonda oksijene aktarılır.',
    'II':'Elektronlar taşınırken açığa çıkan enerji H⁺’ları matriksten zarlar arası boşluğa pompalar; bu ifade doğrudur.',
    'III':'ATP sentaz, H⁺’ların zarlar arası boşluktan matrikse geçişinden yararlanarak ATP sentezler; bu ifade doğrudur.'}
d4,s4=onc_sec({k for k,v in T4.items() if v},'A')
q('0004',tipId='hs-ets',tip='Elektron taşıma sistemi ve kemiozmoz',z='orta',alt='ETS ve kemiozmoz',kaz='ETS’deki elektron akışı, proton pompalanması ve ATP sentezi ile ilgili yanlış öncülü ayırt eder.',kalip='öncüllü',
 kart=f'{k4} (ETS, kemiozmoz) · yanlış öncülü bulma',
 metin='Oksijenli solunumun son basamağı, mitokondrinin iç zarında gerçekleşen elektron taşıma sistemidir (ETS). Bu basamakta NADH ve FADH₂’den gelen elektronlar zardaki taşıyıcılar üzerinden ilerler ve en sonunda bir son elektron alıcısına aktarılır.\nI. NADH ve FADH₂ elektronlarını doğrudan oksijene aktarır.\nII. Elektronlar taşınırken açığa çıkan enerjiyle H⁺’lar matriksten zarlar arası boşluğa pompalanır.\nIII. ATP sentezi, H⁺’ların ATP sentaz aracılığıyla zarlar arası boşluktan matrikse geçişiyle gerçekleşir.\nBuna göre, ETS ile ilgili yukarıdaki ifadelerden hangileri yanlıştır?',
 dogru=d4,sira=s4,yan=onc_cel({k for k,v in T4.items() if v},s4,d4,N4,olumsuz=True),
 istenen='ETS ile ilgili yanlış olan öncüller.',
 ip=['Elektronların NADH’tan oksijene kadar izlediği yolu aşama aşama düşün ve her öncülü bu yolla karşılaştır.'],
 bilgi=[B('Kemiozmotik ATP sentezi','elektronların taşıyıcılarda ilerlemesiyle H⁺’lar zarın bir yanına pompalanır; derişim farkına uyarak geri akan H⁺’ların enerjisi ATP sentaz enzimiyle ATP’ye dönüştürülür')],
 ad=onc_adim({k for k,v in T4.items() if v},N4)+[A('Sonuç','Kökte yanlış olanlar istendiğinden yalnız ilk öncül seçilir.','Yanlış olan: I')],
 puf='Elektronlar taşıyıcıdan taşıyıcıya geçer; oksijen yalnız zincirin sonunda elektron alır ve suya indirgenir.')
SIRA[4]=4

# -------- N5 · Basamak akış şeması · orta · öncüllü + olumsuz · şema
k5=kartla(5,'Basamaklarda CO₂ çıkışı','CO₂, oksijenli solunumda yalnız pirüvatın asetil CoA’ya dönüşümünde ve Krebs döngüsünde açığa çıkar; glikolizde ve ETS’de CO₂ oluşmaz.','Glikolizde CO₂ çıktığını sanmak; ETS’yi CO₂ üreten basamak saymak.','orta','şekilli',3,'hs-basamak','Basamaklardaki ürünler')
def akis():
    b=[]
    yer_={'Glikoz':(0,1.5),'Pirüvat':(3.6,1.5),'Asetil CoA':(7.2,1.5),'NADH ve\\\\FADH$_2$':(7.2,-.5),'H$_2$O':(3.6,-.5)}
    for t,(x,y) in yer_.items():
        b.append(f'\\node[draw,line width=1pt,rounded corners=3pt,minimum width=2.1cm,minimum height=1.05cm,align=center] at ({x},{y}) {{{t}}};')
    b.append(f'\\draw[{OKS},line width=1pt] (1.05,1.5)--(2.55,1.5);\\node[font=\\normalsize\\bfseries] at (1.8,1.9) {{I}};')
    b.append(f'\\draw[{OKS},line width=1pt] (4.65,1.5)--(6.15,1.5);\\node[font=\\normalsize\\bfseries] at (5.4,1.9) {{II}};')
    b.append(f'\\draw[{OKS},line width=1pt] (7.2,.95)--(7.2,0.05);\\node[font=\\normalsize\\bfseries] at (7.65,.5) {{III}};')
    b.append(f'\\draw[{OKS},line width=1pt] (6.15,-.5)--(4.65,-.5);\\node[font=\\normalsize\\bfseries] at (5.4,-.1) {{IV}};')
    return tk('\n'.join(b),.95)
SK5=akis()
T5={'I':True,'II':False,'III':False,'IV':True}   # CO₂ çıkmayan basamaklar
ROM4=('I','II','III','IV')
CAN5=['Yalnız I','I ve II','II ve III','II ve IV','I ve IV']
N5={'I':'I numaralı basamak glikolizdir; glikoz, karbonlarının tamamını koruyarak iki pirüvata ayrılır ve CO₂ oluşmaz.',
    'II':'II numaralı basamakta pirüvattan asetil CoA oluşurken bir karbon CO₂ olarak ayrılır; bu yüzden CO₂ çıkar.',
    'III':'III numaralı basamak Krebs döngüsüdür; asetil CoA’nın karbonları CO₂ olarak ayrılır, bu yüzden CO₂ çıkar.',
    'IV':'IV numaralı basamak ETS’dir; elektronlar oksijene aktarılıp su oluşur, CO₂ oluşmaz.'}
d5='I ve IV'; assert d5==etiket({'I','IV'},CAN5,list(ROM4))
yan5=[]
for o in CAN5[:-1]:
    S=kume_of(o,ROM4); T=set(k for k,v in T5.items() if v); ex=sorted(S-T,key=ROM4.index); ms=sorted(T-S,key=ROM4.index)
    pr=[f'{e} numaralı basamakta CO₂ çıktığı hâlde bu basamak CO₂ çıkmayanlar arasında sayılmış: {N5[e]}' for e in ex]+[f'{e} numaralı basamakta CO₂ çıkmadığı hâlde bu basamak dışarıda bırakılmış: {N5[e]}' for e in ms]
    yan5.append((o,' '.join(pr),'bilgi'))
q('0005',tipId='hs-basamak',tip='Basamaklardaki ürünler',z='orta',alt='Basamaklar ve ürünler',kaz='Oksijenli solunum basamaklarının hangilerinde CO₂ çıkmadığını belirler.',kalip='şekilli',
 kart=f'{k5} (CO₂ çıkışı) · şematik basamaklar',
 metin='Şekilde, bir glikozun oksijenli solunumla tamamen yıkılması sırasındaki ardışık dönüşümler I, II, III ve IV ile numaralandırılmış oklarla gösterilmiştir.\nBuna göre, numaralandırılmış dönüşümlerin hangilerinde CO₂ açığa çıkması beklenmez?',
 dogru=d5,sira=CAN5,yan=yan5,
 istenen='CO₂ çıkışı gerçekleşmeyen dönüşümler.',
 ip=['Her okun hangi basamağa karşılık geldiğini madde adlarından bulup o basamakta karbon atomlarının akıbetine bak.'],
 bilgi=[B('Karbonların akıbeti','glikozun altı karbonu oksijenli solunumda tamamen CO₂’ye dönüşür · CO₂ üreten basamaklarda bir karbonlu parça organik molekülden ayrılır')],
 ad=[A('Okları adlandır','Glikozdan pirüvata glikoliz, pirüvattan asetil CoA’ya dönüşüm, asetil CoA’dan taşıyıcılara Krebs döngüsü, taşıyıcılardan suya ETS gerçekleşir.','I: glikoliz · II: pirüvat → asetil CoA · III: Krebs · IV: ETS'),
     A('CO₂ çıkışını sına','Karbon kaybı yalnız pirüvatın dönüşümünde ve Krebs döngüsünde olur.','CO₂ var: II, III'),
     A('Kökü uygula','Kökte CO₂ çıkmayanlar istenir; glikoliz ve ETS CO₂ üretmez.','CO₂ çıkmaz: I, IV'),
     A('Sonuç','CO₂ çıkmayan dönüşümler I ve IV’tür.','Doğru: I ve IV')],
 puf='Glikoz sonunda tamamen CO₂’ye dönüştüğü hâlde CO₂ yalnız asetil CoA oluşumunda ve Krebs döngüsünde çıkar; ilk ve son basamak CO₂ üretmez.',sekil=SK5)
SIRA[5]=5

# -------- N6 · Respirometre (KOH) · orta · düzenek
k6=kartla(6,'KOH’lu solunum düzeneği','KOH CO₂’yi tutar; oksijen tüketimi gaz hacmini azaltır. Karbonhidratın oksijenli solunumunda tüketilen O₂ ile üretilen CO₂ hacmi eşittir.','KOH’un görevini bilmemek; CO₂ çıkışının gaz hacmini artıracağını düşünmek.','orta','şekilli',3,'hs-deney','KOH’lu solunum düzeneği')
sk6=tk(sise(0,2.9,'K','KOH çözeltisi','',3)+'\n'+sise(0,-.4,'L','Saf su','',3),.8)
SK6=sk6
A6='K’de damla şişeye doğru hareket eder, L’de yerinde kalır.'
q('0006',tipId='hs-deney',tip='KOH’lu solunum düzeneği',z='orta',alt='Solunum deneyi',kaz='KOH’lu ve KOH’suz düzeneklerde gaz hacmi değişimini yorumlar.',kalip='şekilli',
 kart=f'{k6} (KOH’lu düzenek) · iki düzenek karşılaştırması',
 metin='Şekildeki K ve L düzeneklerinde, aynı miktarda çimlenmekte olan nişastalı tohumlar kapalı şişelere konmuştur. Her şişeye, içinde sıvı bulunan küçük bir kap yerleştirilmiş ve kılcal boruda başlangıç konumuna bir damla boyalı sıvı konmuştur. Sıcaklık sabit tutulmuş, tohumların yalnızca karbonhidratı oksijenli solunumla yıkadığı ve damlanın yalnız şişedeki gaz hacmi değişimiyle hareket ettiği kabul edilmiştir.\nBir süre sonra damlalar için aşağıdakilerden hangisi beklenir?',
 dogru=A6,
 sira=yer('B',A6,['K’de damla şişeye doğru hareket eder, L’de şişeden uzağa hareket eder.','K’de ve L’de damla yerinde kalır.','K’de damla şişeden uzağa hareket eder, L’de yerinde kalır.','K’de damla yerinde kalır, L’de şişeye doğru hareket eder.']),
 yan=[('K’de damla şişeye doğru hareket eder, L’de şişeden uzağa hareket eder.','L’de CO₂ üretiminin O₂ tüketiminden fazla olduğunu sanmak; oysa karbonhidratın yıkımında tüketilen O₂ ile üretilen CO₂ hacmi eşittir.','bilgi'),
      ('K’de ve L’de damla yerinde kalır.','KOH’un CO₂’yi tuttuğunu görmeden, solunumun gaz hacmini hiç değiştirmediğini sanmak.','bilgi'),
      ('K’de damla şişeden uzağa hareket eder, L’de yerinde kalır.','KOH’lu düzende CO₂ çıkışının hacmi artırdığını sanmak; oysa KOH CO₂’yi tutar ve geriye yalnız O₂ tüketimi kalır.','bilgi'),
      ('K’de damla yerinde kalır, L’de şişeye doğru hareket eder.','Suyun CO₂’yi tuttuğunu düşünüp işlevleri ters eşleştirmek; KOH’lu kapta gaz azalır, sulu kapta hacim değişmez.','bilgi')],
 istenen='K ve L düzeneklerindeki damlaların hareketi.',
 ip=['Her şişede tüketilen ve üretilen gazları ayrı ayrı yaz; kaptaki sıvının hangi gazı tuttuğunu hatırla.'],
 bilgi=[B('Gaz alışverişi ve KOH','oksijenli solunumda O₂ tüketilir, CO₂ üretilir · KOH çözeltisi ortamdaki CO₂’yi bağlar · Kapalı kapta gaz hacmi azalırsa ucu açık boruda sıvı kapalı kaba doğru çekilir')],
 ad=[A('Denklemi yaz','Glikozun oksijenli yıkımında 6 O₂ tüketilir, 6 CO₂ oluşur.','O₂ tüketimi = CO₂ üretimi'),
     A('K düzeneğini incele','KOH, oluşan CO₂’yi tutar; yalnız O₂ tüketimi gaz hacmini azaltır.','K’de hacim azalır'),
     A('L düzeneğini incele','Su CO₂’yi tutmaz; tüketilen O₂ kadar CO₂ oluştuğundan hacim değişmez.','L’de hacim sabit'),
     A('Damlayı yorumla','Hacmi azalan K şişesine damla çekilir; L’de damla yerinde kalır.','K: şişeye doğru · L: yerinde')],
 puf='KOH’lu düzende damlanın yer değiştirmesi doğrudan tüketilen O₂ miktarını gösterir.',sekil=SK6)
SIRA[6]=6

# -------- N7 · O₂ tüketimi ve laktik asit grafiği · orta · öncüllü
k7=kartla(7,'Egzersizde laktik asit birikimi grafiği','O₂ tüketimi sürerken laktik asit de artıyorsa hücrede oksijenli solunum ve laktik asit fermantasyonu birlikte yürür.','O₂ tüketim eğrisi yatay diye solunumun durduğunu sanmak; laktik asit artışını oksijenli solunumun bittiği anlamına getirmek.','orta','grafik',3,'hs-grafik','Egzersizde solunum grafiği')
SK7=tk(grafik([([(0,1),(3,6),(6,9.5),(30,9.5)],'line width=1.8pt'),([(0,1),(10,1),(14,3.2),(20,7.5),(30,9.5)],'line width=1.8pt,dash pattern=on 5pt off 3pt')],30,10.5,[0,5,10,15,20,25,30],[],'Zaman (dk)','Göreli değer',W=6.2,Hh=3.2,etik=[(24,10.1,'O$_2$ tüketim hızı','above'),(21.5,6.2,'Laktik asit derişimi','below right')]),.85)
T7={'I':True,'II':False,'III':True}
N7={'I':'Laktik asit derişimi artmaktadır; bu, pirüvatın laktik aside indirgendiğini, yani laktik asit fermantasyonunun gerçekleştiğini gösterir.',
    'II':'O₂ tüketim hızı sıfırdan büyük ve sabit kaldığına göre oksijenli solunum durmamıştır, sürmektedir.',
    'III':'O₂ tüketildiğine göre mitokondride ETS çalışmaktadır ve NADH yükseltgenmeye devam eder.'}
d7,s7=onc_sec({k for k,v in T7.items() if v},'E')
q('0007',tipId='hs-grafik',tip='Egzersizde solunum grafiği',z='orta',alt='Oksijenli solunum ve fermantasyon',kaz='O₂ tüketimi ve laktik asit eğrilerinden hücredeki solunum olaylarını çıkarır.',kalip='grafik',
 kart=f'{k7} (laktik asit grafiği) · 10–20. dakika yorumu',
 metin='Bir sporcunun iskelet kası hücrelerinde, yoğun egzersiz sırasında O₂ tüketim hızı ve laktik asit derişimindeki değişimler grafikte gösterilmiştir.\nI. Pirüvik asidin bir kısmı laktik aside indirgenmektedir.\nII. Oksijenli solunum durmuştur.\nIII. Mitokondride NADH’ın yükseltgenmesi sürmektedir.\nBuna göre, 10. ile 20. dakikalar arasında bu hücrelerle ilgili yukarıdakilerden hangileri söylenebilir?',
 dogru=d7,sira=s7,yan=onc_cel({k for k,v in T7.items() if v},s7,d7,N7),
 istenen='Grafikten 10–20. dakikalar için çıkarılabilecek yargılar.',
 ip=['İki eğriyi aynı zaman aralığında ayrı ayrı oku: biri sabit ve sıfırdan büyük, diğeri artıyor; bunların hangi olaylara karşılık geldiğini düşün.'],
 bilgi=[B('Laktik asit fermantasyonu','pirüvik asit NADH ile laktik aside indirgenir ve NAD⁺ yenilenir · İskelet kasında oksijen yetersiz kaldığında ya da ATP gereksinimi arttığında oksijenli solunumla birlikte görülebilir')],
 ad=onc_adim({k for k,v in T7.items() if v},N7)+[A('Sonuç','Grafikten çıkarılabilecek yargılar I ve III’tür.','Doğru: I ve III')],
 puf='Laktik asit birikmesi oksijenli solunumun bittiğini göstermez; O₂ tüketimi sürüyorsa ETS de çalışır.',sekil=SK7)
SIRA[7]=7

# -------- N8 · Krebs + ETS ATP hesabı · orta · tablo
k8=kartla(8,'Krebs kaynaklı taşıyıcılardan ATP hesabı','1 glikoz 2 asetil CoA verir; her asetil CoA Krebs’in bir turunu işletir. Taşıyıcıların ETS’deki ATP verimleri ve substrat düzeyi ATP toplanır.','Glikozun tek asetil CoA verdiğini sanmak; substrat düzeyi ATP’yi ya da FADH₂ katkısını unutmak.','orta','tablo',4,'hs-atp','Krebs ve ETS kaynaklı ATP hesabı')
n_glk=2; asetil=PO['asetil']*n_glk; tur=asetil
N_=KT['NADH']*tur; F_=KT['FADH2']*tur; S_=KT['ATP']*tur
c8=N_*ETS_N+F_*ETS_F+S_; assert (N_,F_,S_,c8)==(12,4,4,48)
y8=[(24,'2 glikozdan oluşan asetil CoA sayısını yarıya indirip yalnız tek glikoz için hesaplamak.'),
    (N_*ETS_N+F_*0+S_,'FADH₂’nin ETS’deki katkısını hesaba katmamak.'),
    (N_*ETS_N+F_*ETS_F,'Krebs’te substrat düzeyinde üretilen ATP’yi toplama eklememek.'),
    (N_*ETS_N+F_*ETS_N+S_,'FADH₂ başına da 3 ATP hesaplamak.')]
assert [v for v,_ in y8]==[24,40,44,52]
y8=[(v,t,'islem') for v,t in y8]
SK8=tablo_svg(['Olay','Sonuç'],[['Krebs döngüsünün 1 turu','3 NADH + 1 FADH₂ + 1 ATP'],['ETS’de 1 NADH’ın yükseltgenmesi','3 ATP'],['ETS’de 1 FADH₂’nin yükseltgenmesi','2 ATP']])
q('0008',tipId='hs-atp',tip='Krebs ve ETS kaynaklı ATP hesabı',z='orta',alt='ATP hesapları',kaz='Krebs döngüsü ürünlerinden ETS dahil toplam ATP miktarını hesaplar.',kalip='tablo',
 kart=f'{k8} (Krebs+ETS ATP) · 2 glikoz',
 metin='Krebs döngüsünün bir turunda oluşan ürünler ile ETS’de taşıyıcıların yükseltgenmesiyle elde edilen ATP miktarları tabloda verilmiştir.\n2 glikozun tamamı glikoliz ve pirüvatın asetil CoA’ya dönüşümü basamaklarından geçtikten sonra oluşan asetil CoA’ların hepsi Krebs döngüsünde yıkılmıştır.\nBuna göre, yalnız Krebs döngüsünde oluşan ATP, NADH ve FADH₂’den elde edilen toplam ATP kaç moleküldür?',
 dogru=48,yan=y8,
 istenen='Krebs döngüsü ve bu döngüde oluşan taşıyıcıların ETS’deki yükseltgenmesiyle elde edilen toplam ATP sayısı.',
 ip=['Önce 2 glikozdan kaç asetil CoA oluştuğunu bul; sonra döngü sayısını kullanarak taşıyıcı sayılarını ve ATP’leri tabloya göre topla.'],
 bilgi=[B('Glikoz–asetil CoA ilişkisi','1 glikoz glikolizde 2 pirüvat verir · Her pirüvat, mitokondride CO₂ kaybederek bir asetil CoA’ya dönüşür · Her asetil CoA Krebs döngüsünün bir turunu başlatır')],
 ad=[A('Asetil CoA sayısı','1 glikoz 2 pirüvat, bu da 2 asetil CoA verir; 2 glikozdan 4 asetil CoA oluşur.','2 × 2 = 4 asetil CoA'),
     A('Tur sayısı','Her asetil CoA döngüyü bir kez döndürür; 4 tur gerçekleşir.','4 tur'),
     A('Ürünleri bul','Bir turda 3 NADH, 1 FADH₂ ve 1 ATP oluşur; 4 tur için bunlar 4 ile çarpılır.','12 NADH · 4 FADH₂ · 4 ATP'),
     A('ATP’yi topla','NADH başına 3, FADH₂ başına 2 ATP ETS’de elde edilir; substrat düzeyi ATP eklenir.','12 × 3 + 4 × 2 + 4 = 36 + 8 + 4'),
     A('Sonuç','Toplam ATP 48’dir.','48 ATP')],
 puf='ATP hesabında önce döngü sayısını, sonra taşıyıcı sayılarını bul; substrat düzeyi ATP’yi eklemeyi unutma.',sekil=SK8)
SIRA[8]=8

# -------- N9 · İki fermantasyonun ortak yönleri · orta · öncüllü
k9=kartla(9,'Laktik asit ve etil alkol fermantasyonu karşılaştırması','İki fermantasyonda da pirüvat (ya da türevi) NADH ile indirgenir ve NAD⁺ yenilenir; CO₂ yalnız etil alkol fermantasyonunda çıkar.','Laktik asit fermantasyonunda da CO₂ çıktığını sanmak; fermantasyonda ETS çalıştığını düşünmek.','orta','öncüllü',3,'hs-ferm','Fermantasyon türlerinin karşılaştırılması')
T9={'I':True,'II':True,'III':False}
N9={'I':'Her iki fermantasyonda da NADH, pirüvatı ya da pirüvattan türeyen asetaldehiti indirger; bu ortak bir olaydır.',
    'II':'Her iki fermantasyonda da glikolizde oluşan NADH yükseltgenir ve NAD⁺ yenilenir; bu ortak bir olaydır.',
    'III':'CO₂ yalnız etil alkol fermantasyonunda çıkar; laktik asit fermantasyonunda pirüvat doğrudan laktik aside dönüştüğünden CO₂ oluşmaz.'}
d9,s9=onc_sec({k for k,v in T9.items() if v},'C')
q('0009',tipId='hs-ferm',tip='Fermantasyon türlerinin karşılaştırılması',z='orta',alt='Fermantasyon',kaz='Laktik asit ve etil alkol fermantasyonlarının ortak yönlerini ayırt eder.',kalip='öncüllü',
 kart=f'{k9} (fermantasyon karşılaştırma) · ortak olaylar',
 metin='Kas hücreleri oksijensiz kaldığında laktik asit fermantasyonu, maya hücreleri oksijensiz ortamda etil alkol fermantasyonu yapar. Her iki süreçte de glikoz önce glikolizle yıkılır.\nI. NADH’ın pirüvat ya da türevini indirgemesi\nII. NAD⁺’nın yenilenmesi\nIII. CO₂’nin açığa çıkması\nBuna göre, yukarıdaki olaylardan hangileri bu iki fermantasyonda ortak olarak gerçekleşir?',
 dogru=d9,sira=s9,yan=onc_cel({k for k,v in T9.items() if v},s9,d9,N9),
 istenen='Her iki fermantasyonda da görülen olaylar.',
 ip=['İki fermantasyonun ürünlerini yan yana yaz ve glikolizin sürebilmesi için hangi taşıyıcının yenilenmesi gerektiğini düşün.'],
 bilgi=[B('Fermantasyonun amacı','glikolizde NAD⁺ tükenirse glikoliz durur · Fermantasyon, NADH’ı yükseltgeyerek NAD⁺’yı yeniler ve böylece glikolizle ATP üretimi sürer')],
 ad=onc_adim({k for k,v in T9.items() if v},N9)+[A('Sonuç','Ortak olanlar I ve II’dir.','Doğru: I ve II')],
 puf='Fermantasyonun ortak görevi NAD⁺’yı yenilemektir; CO₂ üretimi türe göre değişir.')
SIRA[9]=9

# -------- N10 · ATP sentezlenmeyen olay · orta · olumsuz
k10=kartla(10,'ATP sentezi olmayan basamak','Glikolizde, Krebs döngüsünde ve ETS’de ATP sentezi vardır; pirüvatın asetil CoA’ya dönüşümü ve fermantasyonun ikinci basamağı ATP üretmez.','Pirüvatın asetil CoA’ya dönüşümünü ATP üreten basamak saymak.','orta','düz',3,'hs-basamak','ATP sentezi olmayan basamak')
A10='Pirüvik asitten asetil CoA oluşumu sırasında'
q('0010',tipId='hs-basamak',tip='ATP sentezi olmayan basamak',z='orta',alt='ATP üretimi',kaz='Hücresel solunum ve fermantasyon basamaklarından ATP sentezinin olmadığı olayı belirler.',kalip='düz',
 kart=f'{k10} (ATP sentezi olmayan basamak) · yanlış basamak seçimi',
 metin='Hücresel solunumun bazı basamaklarında ATP, substrat düzeyinde ya da kemiozmotik mekanizmayla sentezlenir; bazı basamaklarda ise ATP sentezi hiç gerçekleşmez.\nBuna göre, aşağıdaki olaylardan hangisi sırasında ATP sentezi gerçekleşmez?',
 dogru=A10,
 sira=yer('A',A10,['Glikozdan pirüvik asit oluşumu sırasında','Asetil CoA’nın Krebs döngüsünde yıkılması sırasında','H⁺’ların ATP sentaz aracılığıyla matrikse geçmesi sırasında','Alkol fermantasyonunda glikozun pirüvik asite yıkılması sırasında']),
 yan=[('Glikozdan pirüvik asit oluşumu sırasında','Glikolizde ATP üretilmediğini sanmak; glikolizde substrat düzeyinde ATP sentezlenir.','bilgi'),
      ('Asetil CoA’nın Krebs döngüsünde yıkılması sırasında','Krebs döngüsünde ATP üretimini unutmak; döngüde substrat düzeyinde ATP sentezlenir.','bilgi'),
      ('H⁺’ların ATP sentaz aracılığıyla matrikse geçmesi sırasında','Kemiozmozu ATP üretmeyen bir olay sanmak; protonların ATP sentazdan geçişi ATP sentezinin kendisidir.','bilgi'),
      ('Alkol fermantasyonunda glikozun pirüvik asite yıkılması sırasında','Fermantasyonu ATP üretmeyen bir süreç saymak; ATP, fermantasyonun glikoliz kısmında sentezlenir.','bilgi')],
 istenen='ATP sentezinin gerçekleşmediği olay.',
 ip=['Her olayın hangi basamağa ait olduğunu belirle; hangi basamaklarda substrat düzeyi, hangisinde kemiozmotik ATP sentezi görüldüğünü düşün.'],
 bilgi=[B('ATP sentezi türleri','substrat düzeyinde fosforilasyon fosfatın bir bileşikten ADP’ye aktarılmasıyla, kemiozmotik (oksidatif) fosforilasyon ATP sentazdan H⁺ geçişiyle gerçekleşir')],
 ad=[A('Olayları basamaklara ayır','Her seçenekteki olayın glikoliz, Krebs, ETS ya da fermantasyona ait olduğunu bul.','Glikoliz · Krebs · ETS · fermantasyon'),
     A('ATP sentezli olanları ele','Glikoliz ve Krebs’te substrat düzeyinde, ATP sentazdan H⁺ geçişinde kemiozmotik ATP sentezi vardır.','3 olay ATP üretir'),
     A('Fermantasyonu değerlendir','Fermantasyon sürecinde ATP, glikoliz basamağında sentezlenir.','Alkol fermantasyonunda ATP var'),
     A('Sonuç','Pirüvatın asetil CoA’ya dönüşümünde NADH ve CO₂ oluşur ama ATP sentezlenmez.','ATP yok: pirüvat → asetil CoA')],
 puf='Pirüvat → asetil CoA basamağı NADH ve CO₂ verir, ATP vermez.')
SIRA[10]=10

# -------- N11 · Maya grafiği · orta · grafik
k11=kartla(11,'Oksijen azalırken etil alkol artışı','Ortamda O₂ azalırken etil alkol birikiyorsa hücrelerde oksijenli solunum ile alkol fermantasyonu birlikte yürür; O₂ bitince ATP yalnız fermantasyonla üretilir.','Fermantasyonun O₂ sıfır olunca başladığını sanmak; fermantasyonda ATP üretilmediğini düşünmek.','orta','grafik',3,'hs-grafik','Maya kültüründe O₂ ve etil alkol grafiği')
SK11=tk(grafik([([(0,100),(40,0),(60,0)],'line width=1.8pt'),([(0,0),(30,0),(60,90)],'line width=1.8pt,dash pattern=on 5pt off 3pt')],60,110,[0,10,20,30,40,50,60],[0,50,100],'Zaman (dk)','Miktar (birim)',W=6.2,Hh=3.2,etik=[(12,100,'Ortamdaki O$_2$','above right'),(39,58,'Etil alkol','left')]),.85)
A11='30. ile 40. dakikalar arasında maya hücrelerinde hem oksijenli solunum hem de alkol fermantasyonu gerçekleşir.'
q('0011',tipId='hs-grafik',tip='Maya kültüründe O₂ ve etil alkol grafiği',z='orta',alt='Oksijenli solunum ve fermantasyon',kaz='O₂ ve etil alkol eğrilerinden maya hücrelerindeki solunum türlerini çıkarır.',kalip='grafik',
 kart=f'{k11} (O₂–etil alkol grafiği) · dönemlerin yorumu',
 metin='Glikozlu besiyerine, kapalı bir kapta maya hücreleri eklenmiş ve ortamdaki O₂ miktarı ile etil alkol miktarı zamana bağlı olarak ölçülmüştür. Sonuçlar grafikte verilmiştir. Maya hücrelerinin ATP’yi yalnızca bu iki yoldan ürettiği bilinmektedir.\nBuna göre, aşağıdakilerden hangisi söylenebilir?',
 dogru=A11,
 sira=yer('B',A11,['0–30. dakikalar arasında hücreler ATP’yi yalnız fermantasyonla üretir.','40. dakikadan sonra hücreler ATP üretemez.','40. dakikadan sonra CO₂ üretimi durur.','Etil alkol, oksijenli solunumun ürünüdür.']),
 yan=[('0–30. dakikalar arasında hücreler ATP’yi yalnız fermantasyonla üretir.','Etil alkolün hiç oluşmadığı dönemde O₂ tüketildiğini görmeyip fermantasyon yapıldığını sanmak.','bilgi'),
      ('40. dakikadan sonra hücreler ATP üretemez.','O₂ bittiğinde ATP üretimini bitmiş sanmak; fermantasyon O₂’siz ortamda glikolizle ATP üretmeyi sürdürür.','bilgi'),
      ('40. dakikadan sonra CO₂ üretimi durur.','Fermantasyonu CO₂’siz sanmak; alkol fermantasyonunda glikoz başına CO₂ da oluşur ve etil alkol artarken CO₂ üretimi sürer.','bilgi'),
      ('Etil alkol, oksijenli solunumun ürünüdür.','Etil alkolü oksijenli solunumla ilişkilendirmek; etil alkol fermantasyonun ürünüdür ve oksijensiz koşullarda oluşur.','bilgi')],
 istenen='Grafikten çıkarılabilecek doğru yargı.',
 ip=['Grafiği zaman dilimlerine böl ve her dilimde hangi eğrinin değiştiğine bak; sonra hangi ATP üretim yolunun çalıştığını eşle.'],
 bilgi=[B('Fakültatif solunum','maya gibi bazı canlılar oksijen varken oksijenli solunumla, oksijen yetersizken fermantasyonla ATP üretebilir · Ortamdaki O₂ azaldıkça fermantasyon payı artabilir')],
 ad=[A('Dönemleri ayır','0–30. dakika: O₂ azalır, etil alkol yok. 30–40. dakika: O₂ azalır ve etil alkol artar. 40. dakikadan sonra O₂ yoktur, etil alkol artar.','Üç dönem'),
     A('0–30. dakikayı yorumla','O₂ tüketildiğine göre oksijenli solunum vardır; etil alkol oluşmadığından fermantasyon yoktur.','Yalnız oksijenli solunum'),
     A('30–40. dakikayı yorumla','O₂ hâlâ azalmakta, etil alkol artmaktadır; iki yol birlikte yürür.','Oksijenli solunum + fermantasyon'),
     A('Sonuç','Diğer yargılar grafiğe ya da fermantasyon bilgisine aykırıdır; doğru yargı ikinci dönem içindir.','30–40. dakika: iki yol birlikte')],
 puf='Bir grafik dilimin içinde iki eğri birden değişiyorsa iki olay birlikte gerçekleşir.',sekil=SK11)
SIRA[11]=13

# -------- N12 · FADH₂ hesabı · orta · sayısal
k12=kartla(12,'CO₂ miktarından FADH₂ miktarı','CO₂ sayısından yıkılan glikoz sayısı, buradan Krebs ürünleri bulunur: glikoz başına 6 CO₂ ve Krebs’te 2 FADH₂.','Krebs’te yalnız CO₂ oluştuğunu sanmak; NADH ile FADH₂ sayısını karıştırmak.','orta','hikâyeli',3,'hs-atp','CO₂’den Krebs ürünlerini hesaplama')
CO2_T=48; g12=Fr(CO2_T,OKS_CO2); assert g12==8
f12=KG['FADH2']*g12; assert f12==16
y12=[(KG['FADH2']//2*g12,'Krebs’te glikoz başına yalnız 1 FADH₂ oluştuğunu varsaymak.','bilgi'),
     (KG['FADH2']*Fr(CO2_T,KG['CO2']),'Tüm CO₂’nin yalnız Krebs’te çıktığını (glikoz başına 4) varsayıp glikoz sayısını fazla bulmak.','islem'),
     (KG['CO2']*g12,'FADH₂ yerine glikoz başına Krebs’te çıkan CO₂ sayısını (4) kullanmak.','islem'),
     (KG['NADH']*g12,'FADH₂ yerine Krebs’te oluşan NADH sayısını hesaplamak.','dikkat')]
assert sorted([f12]+[v for v,_,_ in y12])==[8,16,24,32,48]
q('0012',tipId='hs-atp',tip='CO₂’den Krebs ürünlerini hesaplama',z='orta',alt='ATP ve taşıyıcı hesapları',kaz='CO₂ miktarından yıkılan glikozu bulup Krebs’te oluşan FADH₂ sayısını hesaplar.',kalip='hikâyeli',
 kart=f'{k12} (CO₂ → FADH₂) · glikoz sayısı üzerinden',
 metin='Oksijenli solunum yapan bir hücre kültüründe, glikozun tamamı CO₂ ve H₂O’ya yıkılırken toplam 48 molekül CO₂ açığa çıkmıştır.\nAynı sürede Krebs döngüsünde oluşan FADH₂ molekülü sayısı kaçtır?',
 dogru=int(f12),yan=[(int(v),t,tu) for v,t,tu in y12],
 istenen='Krebs döngüsünde oluşan toplam FADH₂ sayısı.',
 ip=['CO₂ sayısından yıkılan glikoz sayısına ulaş; sonra bir glikoz için Krebs’te oluşan FADH₂ sayısıyla çarp.'],
 bilgi=[B('Bir glikozun ürünleri','glikozun altı karbonu oksijenli solunumda tamamen CO₂’ye dönüşür · Asetil CoA sayısı pirüvat sayısına eşittir ve her asetil CoA Krebs döngüsünün bir turunu işletir')],
 ad=[A('Glikoz sayısını bul','1 glikoz oksijenli solunumda 6 CO₂ verir; toplam CO₂ buna bölünür.','48 ÷ 6 = 8 glikoz'),
     A('Tur sayısını bul','1 glikozdan 2 asetil CoA oluşur; her biri Krebs’te bir tur döner.','8 × 2 = 16 tur'),
     A('FADH₂ sayısını hesapla','Krebs döngüsünün her turunda 1 FADH₂ oluşur.','16 × 1 = 16 FADH₂')],
 puf='Önce CO₂’den glikoz sayısına, sonra glikozdan tur sayısına geç; taşıyıcılar tur sayısıyla orantılıdır.')
SIRA[12]=11

# -------- N13 · İşaretli atomlar · zor · öncüllü
k13=kartla(13,'İşaretli atomların izlenmesi','Glikozun karbonları pirüvat ve CO₂’ye, O₂’nin oksijeni ETS’de H₂O’ya geçer; işaretli atomun izi bu yollar üzerinden sürülür.','O₂’nin oksijeninin CO₂’ye geçtiğini sanmak; glikozun karbonunun H₂O’da bulunacağını düşünmek.','zor','öncüllü',4,'hs-basamak','İşaretli atomların izlenmesi')
T13={'I':True,'II':False,'III':True}
N13={'I':'Karbonları ¹⁴C ile işaretli glikoz glikolizde pirüvata dönüşür; pirüvatın karbonları glikozdan geldiğinden ¹⁴C bulunur.',
     'II':'H₂O’nun oksijeni ETS’de O₂’den gelir ve suyda karbon bulunmaz; bu yüzden H₂O’da ¹⁴C bulunmaz.',
     'III':'O₂ ETS’de son elektron alıcısı olarak H₂O’ya indirgenir; bu yüzden H₂O’da ¹⁸O bulunur.'}
d13,s13=onc_sec({k for k,v in T13.items() if v},'E')
q('0013',tipId='hs-basamak',tip='İşaretli atomların izlenmesi',z='zor',alt='İşaretli madde deneyleri',kaz='İşaretli karbon ve oksijenin oksijenli solunumda hangi ürünlere geçtiğini belirler.',kalip='öncüllü',
 kart=f'{k13} (işaretli atomlar) · ¹⁴C glikoz ve ¹⁸O₂',
 metin='Karbon atomlarının tamamı ¹⁴C ile işaretli glikoz ve oksijen atomları ¹⁸O ile işaretli O₂, oksijenli solunum yapan bir hücre kültürüne birlikte verilmiştir. Hücrelerde solunum tamamlanana kadar beklenmiştir.\nI. Glikolizde oluşan pirüvik asitte ¹⁴C\nII. ETS sonunda oluşan H₂O’da ¹⁴C\nIII. ETS sonunda oluşan H₂O’da ¹⁸O\nBuna göre, yukarıdaki moleküllerin hangilerinin belirtilen işaretli atomu içermesi beklenir?',
 dogru=d13,sira=s13,yan=onc_cel({k for k,v in T13.items() if v},s13,d13,N13),
 istenen='İşaretli atomu içermesi beklenen moleküller.',
 ip=['Glikozdan başlayan ve oksijenden başlayan iki ayrı yolu izle; karbonun ve oksijen atomunun hangi son ürünlere ulaştığını ayrı ayrı bul.'],
 bilgi=[B('Atomların kaynağı','organik maddeden gelen karbonlar CO₂’ye dönüşür · ETS’de oluşan suyun hidrojeni NADH ve FADH₂’den, oksijeni ise solunan O₂’den gelir')],
 ad=onc_adim({k for k,v in T13.items() if v},N13)+[A('Sonuç','Beklenen işaretli atomlar I ve III’te bulunur.','Doğru: I ve III')],
 puf='Karbon glikozdan CO₂’ye, oksijen gazı O₂’den H₂O’ya gider; iki yol ETS’de kesişmez.')
SIRA[13]=15

# -------- N14 · İç zar, geçirgenlik · zor · öncüllü · şema
k14=kartla(14,'Protonlara geçirgen iç zar','İç zar H⁺’lara geçirgen olursa derişim farkı azalır, ATP sentazdan geçen H⁺ azalır; ETS’nin elektron akışı ise sürer.','Elektron akışının da durduğunu sanmak; ATP sentezinin değişmeyeceğini düşünmek.','zor','şekilli',4,'hs-ets','İç zarın geçirgenliği ve kemiozmoz')
def ic_zar():
    b=[]
    # dış zar (üstte, çift çizgi), iç zar (ortada)
    b.append('\\draw[line width=1.4pt] (-.2,3.2)--(8.4,3.2);\\draw[line width=.6pt] (-.2,3.0)--(8.4,3.0);')
    b.append('\\draw[line width=1.4pt] (-.2,.12)--(8.4,.12);\\draw[line width=1.4pt] (-.2,-.12)--(8.4,-.12);')
    b.append('\\draw[line width=.6pt,fill=white] (-.2,.12) rectangle (-.2,.12);')
    # ETS kompleksleri
    for cx in (1.3,3.0):
        b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15,rounded corners=3pt] ({cx-.5},-.5) rectangle ({cx+.5},.5);\\draw[line width=1pt,rounded corners=3pt] ({cx-.5},-.5) rectangle ({cx+.5},.5);')
    # ATP sentaz
    ax=6.4
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15] ({ax-.18},-.12) rectangle ({ax+.18},.12);\\draw[line width=1pt] ({ax-.18},-.12) rectangle ({ax+.18},.12);')
    b.append(f'\\draw[line width=1pt] ({ax-.12},-.12)--({ax-.12},-.55);\\draw[line width=1pt] ({ax+.12},-.12)--({ax+.12},-.55);')
    b.append(f'\\draw[line width=1pt,fill=black,fill opacity=.15] ({ax},-.95) circle (.42);\\draw[line width=1pt] ({ax},-.95) circle (.42);')
    b.append(f'\\node[font=\\footnotesize] at ({ax},.62) {{ATP sentaz}};')
    # proton noktaları
    import random
    rnd=random.Random(5)
    ust=[(.4,2.6),(.95,2.2),(1.6,2.7),(2.2,2.3),(2.8,2.65),(3.5,2.25),(4.1,2.7),(4.7,2.2),(5.3,2.6),(5.8,1.8),(6.6,2.4),(7.3,2.0),(7.8,2.7),(5.0,1.5),(2.0,1.55),(4.4,1.4),(7.1,1.3),(3.6,1.0),(.9,1.2)]
    alt=[(.7,-1.2),(3.9,-1.5),(7.9,-1.5),(5.0,-.9)]
    for x,y in ust+alt: b.append(f'\\node[draw,circle,inner sep=0pt,minimum size=.28cm,font=\\scriptsize,fill=white] at ({x},{y}) {{+}};')
    # oklar
    b.append(f'\\draw[{OKS},line width=1.4pt] (2.15,-1.1)--(2.15,2.1);\\node[draw,circle,fill=white,inner sep=1.5pt,font=\\normalsize\\bfseries] at (2.15,-.55) {{1}};')
    b.append(f'\\draw[{OKS},line width=1.4pt] (6.4,2.1)--(6.4,.75);\\node[draw,circle,fill=white,inner sep=1.5pt,font=\\normalsize\\bfseries] at (6.4,1.35) {{2}};')
    # bölge adları
    b.append('\\node[font=\\large\\bfseries] at (-.9,1.6) {K};\\node[font=\\large\\bfseries] at (-.9,-1.2) {L};')
    # matriks içeriği: DNA ve ribozom
    b.append('\\draw[line width=1pt] (7.6,-.8) circle (.22);')
    for rx,ry in [(2.2,-1.0),(4.4,-1.2),(1.0,-1.5),(6.0,-1.7),(3.0,-.9)]: b.append(f'\\fill ({rx},{ry}) circle (.05);')
    return tk('\n'.join(b),.78)
SK14=ic_zar()
T14={'I':True,'II':True,'III':False}
N14={'I':'Protonlar sızdıkça K ile L arasındaki derişim farkı azalır; derişim farkı proton sızıntısıyla kapanır.',
     'II':'Derişim farkı azalınca ATP sentazdan geçen H⁺ sayısı ve dolayısıyla ATP sentezi azalır.',
     'III':'Elektron akışı protonları pompalamak zorunda olmadığında bile sürer; NADH yükseltgenmeye devam eder ve O₂ tüketimi durmaz.'}
d14,s14=onc_sec({k for k,v in T14.items() if v},'D')
q('0014',tipId='hs-ets',tip='İç zarın geçirgenliği ve kemiozmoz',z='zor',alt='ETS ve kemiozmoz',kaz='İç zar H⁺ geçirgenliği artarsa derişim farkı, ATP sentezi ve elektron akışının nasıl etkileneceğini yorumlar.',kalip='şekilli',
 kart=f'{k14} (geçirgen iç zar) · proton sızıntısı',
 metin='Şekilde bir mitokondrinin iç zarının bir bölümü ve zarın iki yanındaki K ve L bölgeleri gösterilmiştir. 1 ve 2 numaralı oklar H⁺ geçişlerini göstermektedir. Zarın H⁺’lara geçirgenliğini, ATP sentaz dışındaki yollardan da H⁺ geçecek biçimde artıran bir madde ortama eklenmiştir. Ortamda NADH ve O₂ bulunmaktadır.\nI. K ile L arasındaki H⁺ derişim farkı azalır.\nII. ATP sentaz aracılığıyla gerçekleşen ATP sentezi azalır.\nIII. Elektron taşıma sistemi çalışmaz.\nBuna göre, madde eklendikten sonra, eklenmeden önceki duruma göre yukarıdakilerden hangileri söylenebilir?',
 dogru=d14,sira=s14,yan=onc_cel({k for k,v in T14.items() if v},s14,d14,N14),
 istenen='Maddenin eklenmesiyle ortaya çıkacak değişiklikler.',
 ip=['Önce şemada hangi bölgenin matriks, hangisinin zarlar arası boşluk olduğunu belirle; sonra H⁺ derişim farkının neyi sürdürdüğünü düşün.'],
 bilgi=[B('Protonlar ve ATP sentezi','protonlar ETS çalışırken matriksten zarlar arası boşluğa pompalanır · ATP sentez enzimi, derişim farkıyla geri akan protonların enerjisini kullanır · Elektron taşınması ile proton pompalanması birbirine bağlı yürür')],
 ad=onc_adim({k for k,v in T14.items() if v},N14)+[A('Sonuç','Madde eklendiğinde derişim farkı ve ATP sentezi azalır, ETS çalışır.','Doğru: I ve II')],
 puf='Proton derişim farkı ATP sentezinin kaynağıdır; farkı bozan madde ATP’yi azaltır, ama elektron akışını durdurmaz.',sekil=SK14)
SIRA[14]=14

# -------- N15 · Maya tüpleri · zor · öncüllü · düzenek
k15=kartla(15,'Kontrollü maya deneyi','Karşılaştırmalı tüplerde tek değişken farkıyla sonuç yorumlanır: glikoz yok, enzim bozulmuş ve normal tüp kıyaslanır.','Her sonucun glikoz olmadan da çıkabileceğini sanmak; sıcaklıkla bozulan enzimleri hesaba katmamak.','zor','şekilli',4,'hs-deney','Mayalı deney tüplerinin karşılaştırılması')
def ucdizi():
    b=[]
    X=(1.2,5.6,10.0)
    b.append(erlen(X[0],.7,True,True,'K','Maya + glikoz çözeltisi',True))
    b.append(erlen(X[1],.7,True,True,'L','Maya + saf su',False))
    b.append(erlen(X[2],.7,True,True,'M','Kaynatılıp soğutulmuş maya + glikoz çözeltisi',False))
    for x,t in zip(X,('bulanıklaştı','berrak kaldı','berrak kaldı')):
        b.append(f'\\node[font=\\footnotesize,anchor=north,text width=1.9cm,align=center] at ({x+1.35},.62) {{{t}}};')
    b.append(f'\\node[font=\\footnotesize,anchor=west] at ({X[2]+1.95},1.1) {{kireç suyu}};\\draw[line width=.5pt] ({X[2]+1.95},1.1)--({X[2]+1.5},.9);')
    b.append(f'\\node[font=\\footnotesize,anchor=east] at ({X[0]-1.15},2.0) {{yağ tabakası}};\\draw[line width=.5pt] ({X[0]-1.1},2.0)--({X[0]-.55},1.65);')
    return tk('\n'.join(b),.7)
SK15=ucdizi()
T15={'I':True,'II':True,'III':False}
N15={'I':'K tüpünde, yağ tabakası nedeniyle oksijensiz ortamda kireç suyu bulanmıştır; yani maya O₂ olmadan CO₂ üretebilir.',
     'II':'L tüpünde glikoz olmadığı için CO₂ çıkmamıştır; K ile L kıyaslandığında CO₂ oluşumunun glikoz gerektirdiği görülür.',
     'III':'M tüpünde kaynatma enzimleri bozduğundan CO₂ çıkmamıştır; bu, enzimlerin yüksek sıcaklıkta işlevini koruduğunu değil kaybettiğini gösterir.'}
d15,s15=onc_sec({k for k,v in T15.items() if v},'D')
q('0015',tipId='hs-deney',tip='Mayalı deney tüplerinin karşılaştırılması',z='zor',alt='Deney yorumlama',kaz='Kontrollü fermantasyon deneyinin sonuçlarından doğru çıkarımları seçer.',kalip='şekilli',
 kart=f'{k15} (kontrollü maya deneyi) · K, L ve M tüpleri',
 metin='Şekildeki K, L ve M tüplerine, kaynatılıp soğutulmuş maya hücreleri dışında, aynı miktarda canlı maya hücresi konmuştur. Tüplerin üzerine yağ tabakası eklenerek ortamla O₂ alışverişi engellenmiş, tüpler aynı sıcaklıkta bir süre bekletilmiş ve çıkış borularındaki gazın kireç suyunda yol açtığı değişim gözlenmiştir. Tüplere başlangıçta çözünmüş O₂ bulunmadığı kabul edilmektedir.\nI. Maya hücreleri O₂ olmadan CO₂ üretebilir.\nII. CO₂ üretimi için ortamda glikoz bulunması gerekir.\nIII. Maya enzimleri kaynatıldıktan sonra da işlevini sürdürür.\nBuna göre, deney sonuçlarından yukarıdakilerden hangileri çıkarılabilir?',
 dogru=d15,sira=s15,yan=onc_cel({k for k,v in T15.items() if v},s15,d15,N15),
 istenen='Deney sonuçlarından çıkarılabilecek yargılar.',
 ip=['Tüpleri ikişer ikişer kıyasla; iki tüp arasında yalnız hangi etkenin farklı olduğuna ve kireç suyunun sonucuna bak.'],
 bilgi=[B('Kontrollü deney','bir etkenin etkisi, yalnız o etkenin farklı tutulduğu tüplerin karşılaştırılmasıyla anlaşılır · Kireç suyu CO₂ ile bulanıklaşır · Isı, enzimlerin yapısını bozarak işlevini yok edebilir')],
 ad=onc_adim({k for k,v in T15.items() if v},N15)+[A('Sonuç','Çıkarılabilecek yargılar I ve II’dir.','Doğru: I ve II')],
 puf='Kontrollü deneyde sonucu bir etkene bağlamak için o etkenin yalnız bir tüpte farklı olması gerekir.',sekil=SK15)
SIRA[15]=16

# -------- N16 · Üç hücre tablo · zor · sayısal
k16=kartla(16,'Ürün sayısından glikoz sayısı ve net ATP','Ürün sayısından hücrenin yıktığı glikoz sayısı bulunur: oksijenli solunumda 6 CO₂, laktik asit fermantasyonunda 2 laktik asit, alkol fermantasyonunda 2 CO₂ oluşur; glikolizde net 2 ATP kazanılır.','Her glikoz için CO₂ sayısını karıştırmak; net ATP yerine brüt ATP’yi kullanmak.','zor','tablo',5,'hs-atp','Ürün sayısından glikoz ve net ATP hesabı')
g=Fr(24,OKS_CO2)+Fr(10,FERM['laktik']['laktat'])+Fr(6,FERM['alkol']['CO2']); assert g==4+5+3==12
c16=g*GL['net']; assert c16==24
y16=[(int((Fr(24,2)+5+3)*2),'Oksijenli solunumda glikoz başına yalnız 2 CO₂ çıktığını varsaymak, böylece X’te yıkılan glikoz sayısını fazla bulmak.','bilgi'),
     (int((4+5+Fr(6,6))*2),'Alkol fermantasyonunda glikoz başına 6 CO₂ çıktığını varsaymak, böylece Z’de yıkılan glikoz sayısını az bulmak.','bilgi'),
     (int((4+10+3)*2),'1 glikozdan 1 laktik asit oluştuğunu varsaymak, böylece Y’de yıkılan glikoz sayısını fazla bulmak.','bilgi'),
     (int(12*GL['uretilen']),'Net ATP yerine glikolizde üretilen toplam ATP’yi (glikoz başına 4) kullanmak.','islem')]
assert [v for v,_,_ in y16]==[40,20,34,48]
SK16=tablo_svg(['Hücre','Solunum türü','Ölçülen ürün','Molekül sayısı'],[['K','Oksijenli solunum','CO₂','24'],['L','Laktik asit fermantasyonu','Laktik asit','10'],['M','Etil alkol fermantasyonu','CO₂','6']])
q('0016',tipId='hs-atp',tip='Ürün sayısından glikoz ve net ATP hesabı',z='zor',alt='ATP hesapları',kaz='Farklı solunum türlerindeki ürün sayılarından yıkılan glikoz sayısını ve glikolizdeki net ATP’yi hesaplar.',kalip='tablo',
 kart=f'{k16} (ürün sayısı → glikoz → net ATP) · K, L, M hücreleri',
 metin='K, L ve M hücreleri glikozu farklı yollarla yıkmış ve her hücrede bir süre sonra ölçülen ürünlerin molekül sayıları tabloda verilmiştir. Hücrelerde glikozun tamamı yıkılmış ve başka ürün birikmemiştir.\nBuna göre, üç hücrede de glikolizde kazanılan toplam net ATP sayısı kaçtır?',
 dogru=int(c16),yan=y16,
 istenen='Üç hücrede glikolizle kazanılan toplam net ATP sayısı.',
 ip=['Her hücre için ölçülen ürün sayısından yıkılan glikoz sayısını ayrı ayrı bul; sonra tek glikozun glikolizdeki net kazancını kullan.'],
 bilgi=[B('Ürünler ve glikoz','oksijenli solunumda 1 glikozdan 6 CO₂, fermantasyonda ise 2’şer molekül ürün oluşur · Glikolizde 1 glikozdan 2 ATP harcanır ve 4 ATP üretilir')],
 ad=[A('K hücresi','Oksijenli solunumda 1 glikozdan 6 CO₂ çıkar.','24 ÷ 6 = 4 glikoz'),
     A('L hücresi','Laktik asit fermantasyonunda 1 glikozdan 2 laktik asit oluşur.','10 ÷ 2 = 5 glikoz'),
     A('M hücresi','Alkol fermantasyonunda 1 glikozdan 2 CO₂ çıkar.','6 ÷ 2 = 3 glikoz'),
     A('Toplam glikoz','Üç hücrenin yıktığı glikozlar toplanır.','4 + 5 + 3 = 12 glikoz'),
     A('Net ATP','Glikolizde glikoz başına net kazanç 4 − 2 = 2 ATP’dir.','12 × 2 = 24 ATP')],
 puf='Her solunum türünün ürün/glikoz oranını bil; önce glikoz sayısını bul, sonra ATP’ye geç.',sekil=SK16)
SIRA[16]=17

# -------- N17 · Pasteur etkisi grafiği · zor · grafik
k17=kartla(17,'Oksijen verilince glikoz tüketim hızı','ATP üretim hızı sabitse glikoz tüketim hızı, glikoz başına ATP verimiyle ters orantılıdır; hız oranı verim oranını verir.','Hız oranını doğrudan ATP sayısı sanmak; net ATP yerine ezber toplam ATP değerini yazmak.','zor','grafik',5,'hs-grafik','Verim farkı ve glikoz tüketim hızı')
before,after=18,1; net_ferm=GL['net']
x17=net_ferm*Fr(before,after); assert x17==36
y17=[(before//after,'Hız oranını doğrudan ATP sayısı sanmak.','islem'),(before//after+net_ferm,'Hız oranına 2 ATP eklemek.','islem'),(38,'Grafikten yararlanmadan ezberlenmiş 38 ATP değerini seçmek.','bilgi'),(GL['uretilen']*(before//after),'Net ATP yerine glikolizde üretilen toplam ATP’yi (4) kullanmak.','islem')]
assert [v for v,_,_ in y17]==[18,20,38,72]
SK17=tk(grafik([([(0,18),(10,18),(10.4,1),(20,1)],'line width=1.8pt')],20,21,[0,5,10,15,20],[1,18],'Zaman (dk)','Glikoz tüketim hızı (µmol/dk)',W=6.0,Hh=3.3,kes=[(10,None,''),(10,18,''),(10,1,'')],etik=[]),.85)
q('0017',tipId='hs-grafik',tip='Verim farkı ve glikoz tüketim hızı',z='zor',alt='ATP hesapları',kaz='ATP üretim hızı sabitken glikoz tüketim hızı değişiminden oksijenli solunumdaki net ATP sayısını çıkarır.',kalip='grafik',
 kart=f'{k17} (glikoz tüketim hızı) · O₂ verildiğinde verim farkı',
 metin='Oksijensiz ortamda, ATP’yi yalnız alkol fermantasyonuyla üreten bir maya kültürünün glikoz tüketim hızı ölçülmüştür. Kültürün 10. dakikada ortamına O₂ verilmiş ve bundan sonra glikozun tamamının oksijenli solunumla yıkıldığı gözlenmiştir. Glikoz tüketim hızının zamana bağlı değişimi grafikte verilmiştir. Kültürün ATP üretim hızı deney boyunca değişmemiştir.\nBuna göre, oksijenli solunumda 1 glikozdan kazanılan net ATP sayısı kaçtır?',
 dogru=int(x17),yan=y17,
 istenen='Oksijenli solunumda 1 glikozdan elde edilen net ATP sayısı.',
 ip=['ATP üretim hızı sabit olduğuna göre iki dönemde “glikoz tüketim hızı × glikoz başına net ATP” çarpımlarını eşitle.'],
 bilgi=[B('Net ATP ve hız','bir hücrenin ATP üretim hızı, birim zamanda yıkılan glikoz sayısı ile bir glikozdan kazanılan net ATP’nin çarpımına eşittir · Alkol fermantasyonunda glikoz başına net ATP, glikolizdeki net kazançtır')],
 ad=[A('İlk dönemi yorumla','Oksijensiz dönemde ATP yalnız glikolizle üretilir; glikoz başına net 2 ATP kazanılır.','Hız: 18 · net ATP: 2'),
     A('İkinci dönemi oku','Grafikte oksijen verildikten sonra glikoz tüketim hızı belirgin biçimde düşer.','Hız: 1'),
     A('ATP hızlarını eşitle','ATP üretim hızı değişmediğinden iki dönemdeki çarpımlar eşittir.','18 × 2 = 1 × x'),
     A('Sonuç','Eşitlikten oksijenli solunumdaki net ATP bulunur.','x = 36')],
 puf='ATP ihtiyacı sabitken tüketim hızı ile glikoz başına verim ters orantılıdır.',sekil=SK17)
SIRA[17]=20

# -------- N18 · Organik moleküllerin solunuma katılması · orta
k18=kartla(18,'Lipit ve proteinlerin solunuma katılması','Yağ asitleri asetil CoA’ya, amino asitlerin amino grubu ayrıldıktan sonra kalan kısmı solunum basamaklarına katılır; solunum yalnız glikozla yürümez.','Proteinleri enerji kaynağı saymamak; amino asitleri amino grupları ayrılmadan solunuma sokmak.','orta','düz',3,'hs-karsilastir','Lipit ve proteinlerin solunuma katılması')
A18='Amino asitlerin amino grubu ayrıldıktan sonra kalan karbon iskeleti solunum basamaklarına girebilir.'
q('0018',tipId='hs-karsilastir',tip='Lipit ve proteinlerin solunuma katılması',z='orta',alt='Enerji kaynakları',kaz='Karbonhidrat dışındaki besinlerin solunuma nasıl katıldığını bilir.',kalip='düz',
 kart=f'{k18} (lipit ve protein yıkımı) · doğru ifadeyi seçme',
 metin='Glikoz hücresel solunumun en temel enerji kaynağıdır; ancak glikoz yetersiz kaldığında hücreler lipitleri ve proteinleri de yıkarak ATP elde edebilir. Bu maddeler glikozdan farklı olarak solunumun değişik basamaklarına katılır.\nBuna göre, lipitlerin ve proteinlerin hücresel solunumdaki yıkımıyla ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=A18,
 sira=yer('A',A18,['Yağ asitleri pirüvik aside dönüştürülerek glikolize girer.','Gliserol, asetil CoA’ya dönüşmeden doğrudan ETS’ye katılır.','Proteinler hücre yapısında kullanıldığından solunumda enerji kaynağı olamaz.','Amino asitler, amino grupları ayrılmadan glikolizin ilk basamağına girer.']),
 yan=[('Yağ asitleri pirüvik aside dönüştürülerek glikolize girer.','Yağ asitlerini glikoz gibi düşünmek; yağ asitleri parçalanıp asetil CoA’ya dönüşür ve Krebs döngüsüne girer.','bilgi'),
      ('Gliserol, asetil CoA’ya dönüşmeden doğrudan ETS’ye katılır.','Organik moleküllerin doğrudan ETS’ye girebildiğini sanmak; ETS’ye giren elektronlar yalnız NADH ve FADH₂’den gelir.','bilgi'),
      ('Proteinler hücre yapısında kullanıldığından solunumda enerji kaynağı olamaz.','Proteinlerin yalnızca yapıcı olduğunu sanmak; gerektiğinde proteinler de solunumda enerji kaynağı olur.','bilgi'),
      ('Amino asitler, amino grupları ayrılmadan glikolizin ilk basamağına girer.','Amino grubunun ayrılma basamağını atlamak; amino asitler önce amino grubunu kaybeder, kalan kısım solunuma katılır.','bilgi')],
 istenen='Lipit ve protein yıkımıyla ilgili doğru ifade.',
 ip=['Her besinin yıkım ürününün solunumun hangi basamağına katıldığını düşün; amino asitlerde ilk olarak hangi grubun ayrıldığını hatırla.'],
 bilgi=[B('Çeşitli besinlerin solunumu','karbonhidrat, lipit ve proteinlerin hepsi yıkılarak solunumun ortak basamaklarına girebilir · Giriş basamağı besinin türüne göre değişir')],
 ad=[A('İfadeleri sınıfla','Her seçenek bir besinin solunuma giriş yolunu anlatıyor.','Yağ asidi · gliserol · protein · amino asit'),
     A('Yağ asidi ve gliserolü ele','Yağ asitleri asetil CoA’ya dönüşür; ETS’ye organik molekül değil, yalnız taşıyıcılardan gelen elektronlar girer.','İlk iki ifade yanlış'),
     A('Proteini değerlendir','Proteinler gerektiğinde solunumda yıkılır; bu yüzden enerji kaynağı olabilir.','Üçüncü ifade yanlış'),
     A('Amino asidi değerlendir','Amino grubu ayrıldıktan sonra karbon iskeleti pirüvat, asetil CoA ya da Krebs ara ürünlerine dönüşür.','Amino grubu ayrılmalı')],
 puf='Besinler nasıl başlarsa başlasın ortak solunum basamaklarına girerek yıkılır; giriş noktası besinin türüne göre değişir.')
SIRA[18]=12

# -------- N19 · Prokaryot solunumu · orta · olumsuz
k19=kartla(19,'Mitokondrisiz aerobik hücrede solunum','Prokaryotta ETS elemanları hücre zarında, glikoliz ve Krebs sitoplazmada gerçekleşir; zarlı organel gerekmez.','Oksijenli solunumun yalnız mitokondride yapılabildiğini sanmak.','orta','düz',3,'hs-yer','Prokaryotta hücresel solunum')
A19='Krebs döngüsü, zarla çevrili bir organel içinde gerçekleşir.'
q('0019',tipId='hs-yer',tip='Prokaryotta hücresel solunum',z='orta',alt='Solunumun gerçekleştiği yerler',kaz='Mitokondrisi olmayan aerobik bakterideki solunum olaylarını yerleriyle eşleştirir.',kalip='düz',
 kart=f'{k19} (prokaryotta solunum) · yanlış ifadeyi bulma',
 metin='Mitokondrisi bulunmayan ve oksijenli solunumla ATP üreten bir bakteri hücresi inceleniyor. Bu hücrede glikoz önce glikolizle yıkılıyor, ardından solunumun diğer basamakları da sürüyor.\nBuna göre, bu bakteri hücresiyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=A19,
 sira=yer('D',A19,['Glikoliz sitoplazmada gerçekleşir.','Elektron taşıma sisteminin elemanları hücre zarında bulunur.','Elektron taşıma sisteminin son elektron alıcısı O₂’dir.','Kemiozmotik mekanizmayla ATP sentezlenebilir.']),
 yan=[('Glikoliz sitoplazmada gerçekleşir.','Kökün yanlış ifadeyi istediğini gözden kaçırıp doğru bir ifadeyi seçmek; glikoliz tüm hücrelerde sitoplazmada gerçekleşir.','dikkat'),
      ('Elektron taşıma sisteminin elemanları hücre zarında bulunur.','Doğru bir ifadeyi yanlış sanmak; mitokondrisiz hücrelerde ETS elemanları plazma zarına gömülüdür.','bilgi'),
      ('Elektron taşıma sisteminin son elektron alıcısı O₂’dir.','Doğru bir ifadeyi yanlış sanmak; oksijenli solunum yapan bakteride de son elektron alıcısı O₂’dir.','bilgi'),
      ('Kemiozmotik mekanizmayla ATP sentezlenebilir.','Kemiozmozu yalnız mitokondriye özgü sanmak; bakteri zarında da H⁺ derişim farkıyla ATP sentezi gerçekleşir.','bilgi')],
 istenen='Mitokondrisiz aerobik bakteriyle ilgili yanlış ifade.',
 ip=['Bakterinin zarlı organeli olmadığını ve solunum olaylarının hangi yapılarda yürüyebileceğini hatırla; kök yanlışı istiyor.'],
 bilgi=[B('Prokaryotik hücrede solunum','prokaryotlarda mitokondri yoktur · Solunum enzimleri sitoplazmada ve hücre zarında bulunur · Zarlı organel olmadığından olaylar sıvı bölgede ya da zarda yürür')],
 ad=[A('Hücreyi tanı','Mitokondrisiz bakteri prokaryottur ve zarlı organeli yoktur.','Zarlı organel yok'),
     A('Doğru ifadeleri ele','Glikoliz sitoplazmada gerçekleşir; ETS elemanları hücre zarındadır, son elektron alıcısı O₂’dir ve ATP kemiozmotik yolla sentezlenebilir.','Dört ifade doğru'),
     A('Kalan ifadeyi sına','Krebs döngüsü bakteride sitoplazmada gerçekleşir; zarla çevrili organel bulunmadığından ifade yanlıştır.','Zarlı organel yok'),
     A('Sonuç','Yanlış olan, Krebs döngüsünün zarlı organelde gerçekleştiğini söyleyen ifadedir.','Yanlış: zarlı organel')],
 puf='Oksijenli solunum için mitokondri şart değildir; prokaryotta olaylar sitoplazma ve hücre zarında yürür.')
SIRA[19]=19

# -------- N20 · Respirometre sıcaklık hesabı · zor · düzenek+tablo
k20=kartla(20,'Kontrollü respirometre ve oran','Kaynatılmış tohumlu düzenek fiziksel etkileri gösterir; canlı tohumlu düzeneğin damla hareketinden bu değer çıkarılarak solunum hızı bulunur.','Kontrol değerini düşmemek; oranı ham değerlerle hesaplamak.','zor','şekilli',5,'hs-deney','Kontrollü respirometre ve oran')
def tabsvg(rows):
    b=[]; cw=[1.7,2.9,2.5,3.4]; x0=0; y0=0; rh=.68
    heads=['Düzenek','Tohum','Sıcaklık (°C)','Hareket (mm)']
    xs=[0]
    for w in cw: xs.append(xs[-1]+w)
    for i,hd in enumerate(heads): b.append(f'\\node[font=\\small\\bfseries,text width={cw[i]-.15}cm,align=center] at ({(xs[i]+xs[i+1])/2},{-rh/2}) {{{hd}}};')
    for r,row in enumerate(rows):
        for i,t in enumerate(row): b.append(f'\\node[font=\\small,text width={cw[i]-.15}cm,align=center] at ({(xs[i]+xs[i+1])/2},{-rh*(r+1)-rh/2}) {{{t}}};')
    n=len(rows)+1
    for r in range(n+1): b.append(f'\\draw[line width={1.2 if r in (0,1,n) else .6}pt] (0,{-rh*r})--({xs[-1]},{-rh*r});')
    for x in xs: b.append(f'\\draw[line width=.6pt] ({x},0)--({x},{-rh*n});')
    return '\n'.join(b)
R20=[('K','Canlı','20','10'),('L','Kaynatılmış','20','2'),('M','Canlı','30','26'),('N','Kaynatılmış','30','6')]
sk20=sise(0,0,'','KOH çözeltisi','',3,boy=1.8).replace('\\node[font=\\normalsize\\bfseries] at (-0.45,0.9) {};','')
SK20=tk(sk20+'\n\\begin{scope}[shift={(-.4,-1.0)}]\n'+tabsvg(R20)+'\n\\end{scope}',.85)
k_=Fr(10-2); m_=Fr(26-6); r20=m_/k_; assert r20==Fr(5,2)
y20=[(Fr(26-6,10),'Yalnız 30 °C’taki kontrol değerini düşmek, 20 °C’taki ham değeri kullanmak.','islem'),
     (Fr(26,10),'Kontrol düzeneklerini hiç hesaba katmamak.','dikkat'),
     (Fr(26,10-2),'Kontrol değerini yalnız 20 °C’ta düşüp 30 °C’ta ham değeri kullanmak.','islem'),
     (Fr(10-2,26-6),'Oranı ters kurmak; 20 °C’taki net değeri 30 °C’taki net değere bölmek.','islem')]
assert sorted([r20]+[v for v,_,_ in y20])==sorted([Fr(2,5),Fr(2),Fr(5,2),Fr(13,5),Fr(13,4)])
q('0020',tipId='hs-deney',tip='Kontrollü respirometre ve oran',z='zor',alt='Solunum deneyi',kaz='Kontrol düzeneklerini kullanarak solunum hızları oranını hesaplar.',kalip='şekilli',
 kart=f'{k20} (kontrollü respirometre) · sıcaklık oranı',
 metin='Şekilde gösterilen düzenekten dört tanesi kurulmuştur. K ve M düzeneklerinde çimlenmekte olan tohumlar, L ve N düzeneklerinde ise aynı miktarda kaynatılıp soğutulmuş tohumlar bulunmaktadır. Her düzenekte damlanın şişeye doğru hareketi aynı sürede ölçülmüş ve sonuçlar tabloda verilmiştir. Kaynatılmış tohumlu düzeneklerdeki hareket, sıcaklık ve basınç gibi fiziksel etkenlerden kaynaklanmaktadır. Tohumlar yalnızca karbonhidrat yıkımıyla oksijenli solunum yapmaktadır.\nBuna göre, tohumların 30 °C’taki solunum hızı, 20 °C’taki solunum hızının kaç katıdır?',
 dogru=r20,yan=y20,
 istenen='30 °C’taki solunum hızının 20 °C’takine oranı.',
 ip=['Her sıcaklıkta canlı tohumlu düzenekten, aynı sıcaklıktaki kaynatılmış tohumlu düzeneği çıkararak solunuma bağlı hareketi bul; sonra oranla.'],
 bilgi=[B('Kontrol düzeneği','canlı olmayan örnekle kurulan düzenek, deneyin dışındaki etkenlerin yarattığı değişimi gösterir · Gerçek etki, deney grubundan kontrol grubunun çıkarılmasıyla bulunur')],
 ad=[A('Düzeneği anla','KOH, CO₂’yi tuttuğundan damlanın şişeye hareketi tüketilen O₂ miktarını yansıtır.','Hareket ∝ O₂ tüketimi'),
     A('20 °C’ı düzelt','Canlı tohumlu K’den, kaynatılmış tohumlu L çıkarılır.','10 − 2 = 8 mm'),
     A('30 °C’ı düzelt','Canlı tohumlu M’den, kaynatılmış tohumlu N çıkarılır.','26 − 6 = 20 mm'),
     A('Oranı kur','30 °C’taki net hareket 20 °C’takine bölünür.','20 ÷ 8 = 2,5')],
 puf='Kontrollü deneyde ham değer değil, kontrol değeri çıkarılmış net değer karşılaştırılır.',sekil=SK20)
SIRA[20]=18

# ===================== SIRALAMA VE YAZMA =====================
# kimlik no (0001–0020): yazım adı → istenen son sıra. P.ANA içindeki kayıtlar yeniden numaralanır.
yeni={f'{k:04d}':f'{SIRA[k]:04d}' for k in SIRA}
for qq in P.ANA:
    eski=qq['id'].rsplit('-',1)[1]; qq['id']=f"aytbio-hucresolunum-{yeni[eski]}"; qq['kardes']=None
P.ANA.sort(key=lambda x:x['id'])
for c in H.KARTLAR: c['kaynak']=KY
for qq in P.ANA: assert qq['zorluk'] in ('kolay','orta','zor')
cnt=Counter(qq['zorluk'] for qq in P.ANA); print(cnt)
assert cnt==Counter(kolay=3,orta=11,zor=6),cnt
P.yaz(os.path.join(BD,'hucresolunum-1.json'),'/tmp/bos-hucresolunum.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 AYT Biyoloji dağılımı (yalnız mantık), MEB 12. sınıf biyoloji müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abhucresolunum.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
