"""AYT Biyoloji · Genetik Şifre-Protein Sentezi · 20 soru (kardeş yok, ipucu 1). Dizi, kodon, nükleotit/aminoasit/bağ sayıları ve öncül değerleri Python'da hesaplanıp assert edilir."""
import sys,os,math,json,itertools
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_bio as H
from _hafif_bio import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
KONU='Genetik Şifre-Protein Sentezi'; UK='abio|Genetik Şifre-Protein Sentezi'
H.KONU=KONU
P=Parti('protein',KONU,UK,ders='AYT Biyoloji',idon='aytbio')
KY='ÖSYM AYT 2018–2025 Biyoloji (Genetik Şifre ve Protein Sentezi; yalnız mantık) · MEB 12. sınıf biyoloji'
TIPLER={'pr-kodlama':'Kalıp iplik, mRNA ve kodon ilişkisi','pr-sifre':'Genetik şifre ve kodon tablosu','pr-sayim':'Nükleotit, amino asit ve bağ sayıları',
 'pr-transk':'Transkripsiyon ve mRNA işlenmesi','pr-transl':'Translasyon','pr-mutasyon':'Mutasyonların protein üzerindeki etkisi','pr-nukleik':'DNA ve RNA yapısı'}
CARD={}
def card(no,tipId,alt,fikir,tuzak,z,kalip,adim,ozet):
    kart(f'K-ABPR-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,ad,tipId,z,alt,kaz,kalip,**k):
    kn=int(no); mk(P,no,ad=ad,adim=len(ad),tipId=tipId,tip=TIPLER[tipId],z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABPR-{kn:02d} ('+CARD[kn]+')',**k)
# ---------------- genetik şifre ----------------
BZ='UCAG'; AAS='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
KOD={a+b+c:AAS[i] for i,(a,b,c) in enumerate(itertools.product(BZ,BZ,BZ))}
AD={'F':'Phe','L':'Leu','S':'Ser','Y':'Tyr','C':'Cys','W':'Trp','P':'Pro','H':'His','Q':'Gln','R':'Arg','I':'Ile','M':'Met','T':'Thr','N':'Asn','K':'Lys','V':'Val','A':'Ala','D':'Asp','E':'Glu','G':'Gly'}
assert sum(1 for v in KOD.values() if v=='*')==3 and set(k for k,v in KOD.items() if v=='*')=={'UAA','UAG','UGA'} and KOD['AUG']=='M'
def cevir(m):
    o=[]
    for i in range(0,len(m)-2,3):
        a=KOD[m[i:i+3]]
        if a=='*': return o,True
        o.append(AD[a])
    return o,False
def kodl(m): return [m[i:i+3] for i in range(0,len(m)-len(m)%3,3)]
TUM={'A':'U','T':'A','G':'C','C':'G'}
def mrna_of(kalip): return ''.join(TUM[c] for c in kalip)
def kalip_of(mrna): return ''.join({'U':'A','A':'T','G':'C','C':'G'}[c] for c in mrna)
def dz(l): return ' – '.join(l)
def uc(s): return ' '.join(s[i:i+3] for i in range(0,len(s),3))
PR="$'$"
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)) and len(set(sira))==5; return sira
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
NM=['I','II','III']
def onc(d,harf,neg=False,sab=None):
    """d={'I':(metin,doğru_mu,gerçek)}; neg: doğru olmayanlar istenir. sab=(fazla,eksik) cümle kalıpları ({x},{n})."""
    C={k for k in NM if d[k][1]!=neg}; assert C and len(C)<=3
    dogru=[s for s in SIR if SETS[s]==C][0]; i=SIR.index(dogru); p='ABCDE'.index(harf)
    cb=SIR[:i]; ca=SIR[i+1:]; assert p<=len(cb) and 4-p<=len(ca),(dogru,harf)
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-i))
    bef=sorted(sorted(cb,key=key)[:p],key=SIR.index); aft=sorted(sorted(ca,key=key)[:4-p],key=SIR.index)
    if sab is None:
        sab=(('{x}. yargıyı doğru sanmış; oysa yanlıştır: {n}.','{x}. yargının doğru olduğunu görememiş: {n}.') if not neg else
             ('{x}. yargıyı yanlış sanmış; oysa doğrudur: {n}.','{x}. yargıyı doğru sanmış; oysa yanlıştır: {n}.'))
    yan=[]
    for s in bef+aft:
        parts=[]
        for x in NM:
            if x in SETS[s]-C: parts.append(sab[0].format(x=x,n=d[x][2]))
            if x in C-SETS[s]: parts.append(sab[1].format(x=x,n=d[x][2]))
        assert parts; yan.append((s,' '.join(parts),'bilgi'))
    return dict(dogru=dogru,sira=bef+[dogru]+aft,yan=yan,C=C)
def oncmetin(giris,d,kok): return giris+'\n'+'\n'.join(f'{x}. {d[x][0]}' for x in NM)+'\n'+kok
def oncad(d,neg,etiket=('doğru','yanlış'),bas=None,son=None):
    a=list(bas or [])
    for x in NM: a.append(A(f'{x}. yargıyı incele',d[x][2][0].upper()+d[x][2][1:]+'.',etiket[0] if d[x][1] else etiket[1]))
    C=[x for x in NM if d[x][1]!=neg]
    a.append(A('Sonucu birleştir',son or 'İstenen yargılar bir arada yazılır.',' ve '.join(C) if len(C)<3 else 'I, II ve III'))
    return a
def tek(items,hedef,harf,yon=('Bu ifadeyi doğru sanmış; oysa yanlıştır: ','Bu ifadeyi yanlış sanmış; oysa doğrudur: ')):
    """items=[(metin,doğru_mu,gerçek)]; hedef True: tek doğru; False: tek yanlış ifade istenir."""
    h=[s for s in items if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    dg=h[0]; dig=[s for s in items if s[1]!=hedef]; assert len(dig)==4
    sira=dig[:]; sira.insert('ABCDE'.index(harf),dg)
    yan=[(m,(yon[0] if hedef else yon[1])+n+'.','bilgi') for m,b,n in dig]
    return dict(dogru=dg[0],yan=yan,sira=[s[0] for s in sira]),dg[2]
# ---------------- şekil yardımcıları ----------------
def N(x,y,t,o=''): return f'\\node[{o}] at ({x:.3f},{y:.3f}) {{{t}}};'
def seqfig(rows,dx=0.34,gap=0.22):
    b=[]
    for ttl,letters,y in rows:
        xs=[i*dx+(i//3)*gap for i in range(len(letters))]
        for x,ch in zip(xs,letters): b.append(N(x,y,ch,'font=\\large\\ttfamily\\bfseries'))
        b.append(N(-0.55,y,f'3{PR}','font=\\normalsize')); b.append(N(xs[-1]+0.55,y,f'5{PR}','font=\\normalsize'))
        b.append(N(-0.8,y+0.62,ttl,'anchor=west,font=\\normalsize\\bfseries'))
    return tk('\n'.join(b))
def cod_svg():
    W=480; x0=58; cw=105; ch=62; y0=42; b=[]
    b.append(G._t(x0+2*cw,14,'2. nükleotit',size=12,bold=True))
    b.append(f'<text transform="translate(14,{y0+2*ch}) rotate(-90)" text-anchor="middle" font-size="12" style="fill:currentColor;stroke:none;font-weight:700">1. nükleotit</text>')
    for j,s in enumerate(BZ):
        b.append(f'<rect x="{x0+j*cw+1}" y="22" width="{cw-2}" height="18" style="fill:{G.ACC};fill-opacity:.18;stroke:none"/>'); b.append(G._t(x0+j*cw+cw/2,35,s,size=12,bold=True))
        b.append(f'<rect x="{x0-22}" y="{y0+j*ch+1}" width="20" height="{ch-2}" style="fill:{G.ACC};fill-opacity:.18;stroke:none"/>'); b.append(G._t(x0-12,y0+j*ch+ch/2+4,s,size=12,bold=True))
    for i,a in enumerate(BZ):
        for j,c in enumerate(BZ):
            for k,e in enumerate(BZ):
                cod=a+c+e; aa=KOD[cod]; nm='Dur' if aa=='*' else AD[aa]
                b.append(G._t(x0+j*cw+14,y0+i*ch+14+k*14,f'{cod}  {nm}',anchor='start',size=11.5,bold=(aa=='*')))
    for i in range(5): b.append(f'<line x1="{x0}" y1="{y0+i*ch}" x2="{x0+4*cw}" y2="{y0+i*ch}" stroke-width="1.2"/>')
    for j in range(5): b.append(f'<line x1="{x0+j*cw}" y1="{y0}" x2="{x0+j*cw}" y2="{y0+4*ch}" stroke-width="1.2"/>')
    return G._svg(W,y0+4*ch+4,''.join(b))
COD=cod_svg()
# ---------------- bilgi kutuları (örnekler sorulardaki sayı ve dizileri kullanmaz) ----------------
BK=B('Kalıp iplik, mRNA ve kodon','mRNA, DNA’nın kalıp ipliğine tümleyen ribonükleotitlerle sentezlenir (kalıptaki A ↔ mRNA’da U, T ↔ A, G ↔ C, C ↔ G). mRNA’nın dizisi, kalıba karşı duran kodlayıcı ipliğin T yerine U taşıyan hâlidir. Üçlü nükleotit gruplarına kodon denir; kodonlar 5’→3’ yönünde okunur. Örnek: kalıp 3’–TAG–5’ ise mRNA 5’–AUC–3’ olur')
BS=B('Genetik şifrenin özellikleri','64 kodondan 61’i amino asit şifreler, 3’ü (UAA, UAG, UGA) dur kodonudur ve amino asit şifrelemez. AUG hem başlangıç kodonu hem metiyonin kodonudur. Bir amino asit birden fazla kodonla şifrelenebilir, ancak bir kodon tek amino asit şifreler. Kodonlar üçer nükleotitlik gruplar hâlinde, örtüşmeden ve boşluksuz okunur. Şifre bütün canlılarda büyük ölçüde ortaktır')
BP=B('Peptit bağı ve su','Amino asitler ribozomda dehidrasyon sentezi ile peptit bağıyla bağlanır; her bağda 1 su molekülü açığa çıkar. Tek zincirli, n amino asitli polipeptitte n − 1 peptit bağı ve n − 1 su molekülü vardır. Dur kodonu amino asit şifrelemez. Örnek: 10 amino asitli zincirde 9 peptit bağı bulunur')
BN=B('Nükleotit ve amino asit sayısı','Dur kodonu dahil kodlayıcı bölgede kodon sayısı = amino asit sayısı + 1’dir. mRNA’nın nükleotit sayısı kodon sayısının 3 katı, çift zincirli genin nükleotit sayısı 6 katıdır. Örnek: 20 amino asitli polipeptit için mRNA’da 63, çift zincirli genin kodlayıcı bölgesinde 126 nükleotit bulunur')
BH=B('Baz eşleşmesi ve hidrojen bağı','DNA’da A ile T arasında 2, G ile C arasında 3 hidrojen bağı bulunur; çift zincirli DNA’da A = T ve G = C’dir. RNA’da timin yerine urasil bulunur ve RNA genellikle tek zincirlidir; baz oranları eşit olmak zorunda değildir. Örnek: 10 A–T ve 5 G–C çiftinde 10 × 2 + 5 × 3 = 35 hidrojen bağı vardır')
BM=B('Mutasyon türleri','Bir nükleotitin başka bir nükleotitle yer değiştirmesinde kodon aynı amino asidi şifrelerse sessiz, başka amino asidi şifrelerse yanlış anlamlı, dur kodonuna dönüşürse anlamsız mutasyon olur (polipeptit kısalır). Bir ya da iki nükleotit ekleme ya da çıkarma okuma çerçevesini kaydırır ve sonraki kodonların hepsini değiştirir. Örnek: GAA kodonunun GAG olması sessiz mutasyondur (ikisi de Glu)')
BT=B('Transkripsiyon','RNA polimeraz DNA’yı açar, kalıp ipliği 3’→5’ yönünde okur ve ribonükleotitleri 5’→3’ yönünde birbirine bağlayarak RNA’yı uzatır. Ökaryotlarda transkripsiyon çekirdekte, translasyon sitoplazmada ribozomlarda olur; ilk mRNA’dan intronlar çıkarılır ve eksonlar birleştirilir. Bakterilerde zar ile ayrılmış çekirdek yoktur ve translasyon mRNA sentezi sürerken başlayabilir')
BL=B('Translasyon','Ribozomun küçük alt birimi mRNA’ya bağlanır, başlatıcı tRNA (metiyonin taşır) AUG kodonuna eşleşir, ardından büyük alt birim katılır. tRNA’ların antikodonu kodona tümleyendir; ribozom mRNA üzerinde 5’→3’ yönünde ilerler. Dur kodonuna karşılık gelen tRNA yoktur, dur kodonunda sentez sonlanır. Bir mRNA üzerinde aynı anda birden fazla ribozom çalışabilir (polizom)')
BC=B('DNA ve RNA’nın nükleotit bileşimi','DNA’da A, T, G, C; RNA’da A, U, G, C nükleotitleri bulunur. Çift zincirli DNA’da A = T ve G = C olması gerekir; bu oranlar sağlansa bile molekülün çift zincirli olduğu kesin değildir. Bu eşitlik sağlanmıyorsa molekül çift zincirli olamaz. Urasil içeren molekül RNA’dır')
BD=B('Deney sonucunu yorumlama','Bir yargıya ulaşılabilmesi için sonucun doğrudan verilerden çıkarılabilmesi gerekir; yargı gerçekte doğru olsa bile veriler onu göstermiyorsa bu deneyle ulaşılamaz. Örnek: bir deneyde yalnız iki türden örnek incelenmişse “bütün canlılarda böyledir” sonucuna varılamaz')
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKU='-{Stealth[length=2.3mm,width=1.9mm]}'

# ===== 01 · kolay · dizi şekli · kalıp → mRNA kodonu
card(1,'pr-kodlama','Kalıp iplikten mRNA kodonu','mRNA kalıba tümleyen sentezlenir; kalıp üçlüleri sırayla tümlenerek istenen kodon bulunur.','Kalıp üçlüsünü doğrudan kodon sanmak; T yerine U yazıp tümleyenini almamak; kodon sırasını yanlış saymak.','kolay','şekilli',3,'kalıp iplikten 3. kodon')
m1=['AUG','GCU','ACG','GGA','CUU','UGA']; k1=kalip_of(''.join(m1)); assert mrna_of(k1)==''.join(m1)
kt=k1[6:9]; assert kt=='TGC' and mrna_of(kt)=='ACG' and 'ACG'[::-1]=='GCA' and m1[3]=='GGA'
d1=[('TGC','Kalıp ipliğin 3. üçlüsünü olduğu gibi kodon sanmış; oysa mRNA kalıba tümleyen sentezlenir ve urasil içerir.','bilgi'),
    ('UGC','Kalıptaki üçlüde T yerine U yazmış ama tümleyenini almamış; kalıp dizisini mRNA dizisi gibi okumuş.','bilgi'),
    ('GCA','Tümleyen nükleotitleri doğru bulmuş fakat kodonu 3’→5’ yönünde, ters sırayla yazmış.','dikkat'),
    ('GGA','Başlangıç kodonunu saymayıp 4. üçlüyü 3. kodon olarak almış.','dikkat')]
q('0001',[A('Üçlülere ayır','Kalıp iplik üçlü gruplar hâlinde verilmiştir; her üçlü bir kodona karşılık gelir.','1. üçlü TAC · 2. üçlü CGA · 3. üçlü TGC'),
   A('Tümleyenini yaz','mRNA’da A ↔ U, T ↔ A, G ↔ C, C ↔ G eşleşir; ribonükleotitlerde timin yerine urasil bulunur.','3. üçlü TGC → ACG'),
   A('Kodonu seç','Kalıp ve mRNA aynı hizada olduğundan 3. kodon, 3. üçlünün tümleyenidir.','3. kodon: ACG')],
  'pr-kodlama','kolay','Kalıp iplik–mRNA','Kalıp iplik dizisinden mRNA kodonunu belirler.','şekilli',
  metin='Şekilde, bir genin kalıp ipliğinin başlangıç bölümü üçlü gruplar hâlinde verilmiştir. Bu bölgeden sentezlenen mRNA’nın ilk kodonu başlangıç kodonudur ve mRNA, kalıp ipliğe tümleyen nükleotitlerle sentezlenmektedir.\nBuna göre, bu mRNA’nın 3. kodonu aşağıdakilerden hangisidir?',
  sekil=seqfig([('Kalıp iplik',k1[:18],0)]),dogru='ACG',yan=d1,sira=yer('B','ACG',[x[0] for x in d1]),
  istenen='mRNA’nın 3. kodonu.',ip=['mRNA’nın kalıpla hangi nükleotit çiftleriyle eşleştiğini hatırla; yalnız 3. üçlüye odaklan.'],bilgi=[BK],
  puf='mRNA’yı bulmak için kalıbın her nükleotitine tümleyenini yaz; timin yerine urasil kullanılır.')

# ===== 02 · kolay · genetik şifre özellikleri (yanlış olan)
card(2,'pr-sifre','Genetik şifrenin özellikleri','64 kodondan 61’i amino asit, 3’ü dur kodonudur; aynı amino asit birden fazla kodonla şifrelenebilir.','64 kodonun hepsinin amino asit şifrelediğini sanmak.','kolay','düz',2,'genetik şifre özellikleri')
it2=[('Aynı amino asidi şifreleyen birden fazla kodon bulunabilir.',True,'amino asit çeşidi 20 iken amino asit şifreleyen 61 kodon vardır; bu yüzden bazı amino asitler birden fazla kodonla şifrelenir'),
     ('AUG kodonu hem translasyonun başlangıç sinyali hem de metiyoninin şifresidir.',True,'AUG hem başlangıç kodonu hem metiyonin kodonudur'),
     ('Kodonlar mRNA üzerinde birbirini örtmeden ardışık olarak okunur.',True,'genetik şifre üçer nükleotitlik gruplar hâlinde, örtüşmeden ve boşluksuz okunur'),
     ('Toplam 64 kodonun tamamı birer amino asidi şifreler.',False,'64 kodondan 3’ü (UAA, UAG, UGA) dur kodonudur ve amino asit şifrelemez; amino asit şifreleyen kodon sayısı 61’dir'),
     ('Dur kodonlarına karşılık gelen antikodona sahip bir tRNA bulunmaz.',True,'dur kodonlarını tanıyan tRNA yoktur; sentez bu kodonlarda sonlanır')]
r2,n2=tek(it2,False,'D')
assert 64-3==61 and n2.startswith('64 kodondan 3')
q('0002',[A('Her ifadeyi değerlendir','Kodon sayısı, kodonların okunuşu ve dur kodonları genetik şifrenin temel özellikleridir.','Aynı amino asit, çoklu kodon: doğru · AUG: doğru · örtüşmeme: doğru · dur için tRNA yok: doğru'),
   A('Kodon sayısını say','Dört bazın üçlü kombinasyonları 4 × 4 × 4 = 64 kodon verir; bunların 3’ü dur kodonudur.','64 − 3 = 61 amino asit kodonu'),
   A('Yanlışı belirle','64 kodonun tamamının amino asit şifrelediği ifadesi 61 kodon gerçeğiyle çelişir.','“64’ünün tamamı amino asit şifreler” yanlış')],
  'pr-sifre','kolay','Genetik şifre','Genetik şifrenin özelliklerini ayırt eder.','düz',
  metin='Canlılarda genetik bilgi, mRNA üzerindeki nükleotit dizisinin üçer nükleotitlik kodonlar hâlinde okunmasıyla polipeptite çevrilir. Kodonların hangi amino asidi şifrelediğini gösteren genetik şifre tablosu, bütün canlılarda büyük ölçüde ortaktır.\nBuna göre, genetik şifre ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
  dogru=r2['dogru'],yan=r2['yan'],sira=r2['sira'],istenen='Genetik şifre hakkında yanlış olan ifade.',
  ip=['Kodonların toplam sayısı ile dur kodonlarının amino asit şifreleyip şifrelemediğini düşün.'],bilgi=[BS],
  puf='64 kodonun 61’i amino asit, 3’ü dur kodonudur; “hepsi amino asit şifreler” ifadesi hep yanlıştır.')

# ===== 03 · kolay · su molekülü sayısı
card(3,'pr-sayim','Peptit bağı ve su sayısı','n amino asitli tek zincirde n − 1 peptit bağı oluşur ve her bağda 1 su açığa çıkar.','Amino asit sayısı kadar su sanmak; her bağda iki su saymak.','kolay','düz',3,'polipeptit sentezinde su sayısı')
n3=50; su3=n3-1; assert su3==49
d3=[(50,'Her amino asit için bir su molekülü açığa çıktığını sanmış; oysa bağ sayısı amino asit sayısından 1 eksiktir.','bilgi'),
    (51,'Başlangıç ve dur kodonları için de birer su molekülü ekleyerek 49 + 2 = 51 bulmuş; kodonlar su çıkışı oluşturmaz.','bilgi'),
    (98,'Her peptit bağında iki su molekülü açığa çıktığını düşünerek 2 × 49 = 98 bulmuş.','bilgi'),
    (150,'Amino asit sayısını kodondaki nükleotit sayısıyla çarparak 3 × 50 = 150 bulmuş; nükleotit sayısı su sayısını belirlemez.','islem')]
assert 51==su3+2 and 98==2*su3 and 150==3*n3
q('0003',[A('Bağ sayısını bul','Tek zincirde ardışık amino asitler arasında bağ oluşur; n amino asit arasında n − 1 bağ vardır.','50 − 1 = 49 peptit bağı'),
   A('Su ile ilişkilendir','Dehidrasyon sentezinde her peptit bağı oluşurken 1 su molekülü açığa çıkar.','1 bağ → 1 su'),
   A('Toplamı yaz','Toplam su sayısı oluşan bağ sayısına eşittir.','49 su molekülü')],
  'pr-sayim','kolay','Peptit bağı','Polipeptit sentezinde oluşan su molekülü sayısını amino asit sayısından hesaplar.','düz',
  metin='Bir hücrede ribozomda tek zincirli bir polipeptit sentezlenmektedir. Polipeptit 50 amino asitten oluşmakta ve amino asitlerin tamamı birbirine peptit bağıyla bağlanmaktadır. Zincirden amino asit ayrılmamakta ve zincire amino asit dışında bir molekül eklenmemektedir.\nBuna göre, bu polipeptidin sentezi sırasında toplam kaç molekül su açığa çıkar?',
  dogru=su3,yan=d3,istenen='Sentez boyunca açığa çıkan toplam su molekülü sayısı.',
  ip=['Zincirde ardışık iki amino asit arasında kaç bağ bulunduğunu ve her bağın oluşumunda ne açığa çıktığını düşün.'],bilgi=[BP],
  puf='Tek zincirde su molekülü sayısı = peptit bağı sayısı = amino asit sayısı − 1.')

# ===== 04 · orta · kodon tablosu · kalıp → polipeptit
card(4,'pr-kodlama','Kalıp iplikten polipeptit dizilimi','Kalıp → mRNA → kodonlar → kodon tablosu ile amino asit dizilimi, dur kodonunda biter.','Kalıbı doğrudan okumak; kodon sırasını ya da okuma çerçevesini yanlış almak.','orta','şekilli',4,'kalıptan polipeptit dizilimi')
m4='AUGUGGCAUAAAGGUUGA'; k4=kalip_of(m4); p4,s4=cevir(m4); assert s4 and p4==['Met','Trp','His','Lys','Gly'] and k4=='TACACCGTATTTCCAACT'
a4=cevir(k4.replace('T','U'))[0]; b4=[AD[KOD[c]] for c in kodl(m4)[:-1]][::-1]; c4=cevir(m4[::-1])[0]; e4=cevir(m4[1:])[0]

assert a4==['Tyr','Thr','Val','Phe','Pro','Thr'] and b4==['Gly','Lys','His','Trp','Met'] and c4==['Ser','Trp','Lys','Tyr','Gly','Val'] and e4==['Cys','Gly','Ile','Lys','Val']
d4=[(dz(a4),'Kalıp ipliği tümlemeden doğrudan kodon gibi okumuş (T yerine U yazmış); mRNA kalıba tümleyendir.','bilgi'),
    (dz(b4),'mRNA’yı doğru bulmuş ama kodonları sağdan sola okuyup amino asit sırasını ters yazmış; translasyon 5’ ucundaki başlangıç kodonundan başlar.','dikkat'),
    (dz(c4),'mRNA dizisini baştan sona ters çevirip (3’→5’) üçlülere ayırmış; kodonlar mRNA’da 5’→3’ okunur.','dikkat'),
    (dz(e4),'Okumaya başlangıç kodonundan değil, ikinci nükleotitten başlamış; okuma çerçevesi AUG ile belirlenir.','dikkat')]
q('0004',[A('mRNA’yı yaz','Kalıba tümleyen ribonükleotitler eşleşir: A ↔ U, T ↔ A, G ↔ C, C ↔ G.',f'3’–{uc(k4)}–5’ → 5’–{uc(m4)}–3’'),
   A('Kodonlara ayır','mRNA, başlangıç kodonundan itibaren üçlü gruplar hâlinde okunur.',' · '.join(kodl(m4))),
   A('Tablodan amino asitleri bul','Her kodonun karşısındaki amino asit tablodan okunur; UGA dur kodonudur ve amino asit eklemez.',' · '.join(f'{c} → {"Dur" if KOD[c]=="*" else AD[KOD[c]]}' for c in kodl(m4))),
   A('Dizilimi yaz','Dur kodonuna kadar olan amino asitler N ucundan C ucuna sıralanır.',dz(p4))],
  'pr-kodlama','orta','Kalıp–polipeptit','Kalıp iplik dizisinden kodon tablosunu kullanarak polipeptit dizilimini bulur.','şekilli',
  metin=f'Bir bakteri geninin kalıp ipliğinin başlangıç bölümü 3’–{k4}–5’ dizisindedir. Bu bölgeden sentezlenen mRNA’nın ilk kodonu başlangıç kodonudur ve translasyon dizinin sonundaki ilk dur kodonunda sonlanmaktadır. Şekilde standart kodon tablosu verilmiştir.\nBuna göre, bu bölgeden sentezlenen polipeptidin amino asit dizilimi, N ucundan C ucuna doğru aşağıdakilerden hangisidir?',
  sekil=COD,dogru=dz(p4),yan=d4,sira=yer('C',dz(p4),[x[0] for x in d4]),istenen='Polipeptidin amino asit dizilimi.',
  ip=['Önce kalıba tümleyen mRNA’yı yaz, sonra başlangıç kodonundan başlayarak üçlülere ayır.'],bilgi=[BK,BS],
  puf='Sıra hep kalıp → mRNA → kodon → amino asit; dur kodonu dizilime girmez.')

# ===== 05 · orta · tablo · nükleotit, bağ sayıları (öncüllü)
card(5,'pr-sayim','Amino asit sayısından nükleotit ve bağ sayısı','Dur dahil kodon sayısı = amino asit + 1; mRNA 3 katı, çift zincirli gen 6 katı nükleotit; peptit bağı = amino asit − 1.','Dur kodonunu saymamak; peptit bağını amino asit sayısına eşitlemek.','orta','tablo',4,'üç polipeptit nükleotit/bağ yargıları')
aa5={'P1':30,'P2':45,'P3':60}
n5_mrna=(aa5['P2']+1)*3; n5_gen=(aa5['P3']+1)*6; b5_p1=aa5['P1']-1
assert (n5_mrna,n5_gen,b5_p1)==(138,366,29)
d5={'I':('P2’yi şifreleyen mRNA, dur kodonu dahil 138 nükleotitten oluşur.',n5_mrna==138,'P2 için 45 amino asit ile dur kodonu birlikte 46 kodon eder; 46 × 3 = 138 nükleotit bulunur'),
    'II':('P3’ü şifreleyen genin kodlayıcı bölgesi, çift zincirli olarak dur kodonu dahil 366 nükleotit içerir.',n5_gen==366,'P3 için 60 amino asit ile dur kodonu 61 kodon eder; çift zincirde 61 × 6 = 366 nükleotit bulunur'),
    'III':('P1’in sentezi sırasında ribozomda 30 peptit bağı oluşur.',b5_p1==30,'30 amino asitli tek zincirde 30 − 1 = 29 peptit bağı oluşur')}
r5=onc(d5,'B')
q('0005',oncad(d5,False,bas=[A('Kodon ve nükleotit ilişkisi','Dur kodonu da kodlayıcı bölgenin parçasıdır; kodon sayısı amino asit sayısından 1 fazladır.','Kodon sayısı = amino asit sayısı + 1')]),
  'pr-sayim','orta','Nükleotit ve bağ hesapları','Amino asit sayısından mRNA ve gen nükleotit sayıları ile peptit bağı sayısını hesaplar.','tablo',
  metin=oncmetin('Tabloda, intron içermeyen üç genden sentezlenen ve tek zincirden oluşan P1, P2 ve P3 polipeptitlerinin amino asit sayıları verilmiştir. Her genin kodlayıcı bölgesi başlangıç kodonuyla başlar, tek bir dur kodonuyla sonlanır ve mRNA’da kodlayıcı bölge dışında nükleotit bulunmaz.',d5,'Buna göre, bu yargılardan hangileri doğrudur?'),
  sekil=tablo_svg(['Polipeptit','Amino asit sayısı'],[[k,str(v)] for k,v in aa5.items()]),dogru=r5['dogru'],yan=r5['yan'],sira=r5['sira'],
  istenen='Doğru olan yargılar.',ip=['Her yargıda dur kodonunun sayıya katılıp katılmadığına ve bağ sayısının amino asit sayısıyla ilişkisine bak.'],bilgi=[BN,BP],
  puf='Nükleotit sayılarında dur kodonunu unutma; peptit bağında ise amino asit sayısından 1 çıkar.')

# ===== 06 · orta · translasyon şeması · antikodondan kodlayıcı iplik
card(6,'pr-kodlama','Antikodondan kodlayıcı ipliğe','Antikodon kodona, kodon da kalıba tümleyendir; kodlayıcı iplik mRNA ile aynı dizidir (T yerine U).','Kalıp ve kodlayıcı ipliği karıştırmak; P ve A bölgelerinin sırasını ters almak.','orta','şekilli',4,'tRNA antikodonlarından gen dizisi')
ac6=['CGA','UUC']; mr6=''.join(mrna_of(a.replace('U','T')) if False else ''.join({'A':'U','U':'A','G':'C','C':'G'}[c] for c in a) for a in ac6)
assert mr6=='GCUAAG'; kod6=mr6.replace('U','T'); kal6=kalip_of(mr6); assert kod6=='GCTAAG' and kal6=='CGATTC'
f6=lambda s:f'5’–{s}–3’'
d6=[(f6(kal6[:3]+kal6[3:]),'Antikodonları DNA harfleriyle (U yerine T) yazmış; bu dizi kalıp iplikle aynıdır, kodlayıcı ipliğin tümleyenidir.','bilgi'),
    (f6(mr6),'Doğru mRNA’yı bulmuş fakat kodlayıcı DNA ipliğinde urasil değil timin bulunduğunu unutmuş.','bilgi'),
    (f6(kod6[3:]+kod6[:3]),'Dizi doğru ama P ve A bölgelerinin sırasını ters almış; ribozom 5’→3’ ilerlediğinden P’deki kodon mRNA’da önce gelir.','dikkat'),
    (f6(kal6[::-1]),'Kalıp ipliğin 5’→3’ yazılışını bulup bunu kodlayıcı iplik sanmış.','bilgi')]
assert len({x[0] for x in d6}|{f6(kod6)})==5
def transl_fig():
    b=[]
    b.append('\\draw[rounded corners=10pt,line width=1pt,fill=vurgu!30] (1.7,-0.55) rectangle (6.05,0.9);')
    b.append('\\draw[rounded corners=14pt,line width=1pt,fill=vurgu!14] (1.6,0.9) rectangle (6.15,3.5);')
    b.append('\\draw[line width=2pt] (0,0)--(8.2,0);')
    b.append(N(-0.45,0,f'5{PR}')); b.append(N(8.65,0,f'3{PR}'))
    for xs,ac,aa in ((2.0,ac6[0],True),(4.1,ac6[1],False)):
        xc=xs+0.75
        b.append(f'\\draw[line width=1pt,fill=white,rounded corners=6pt] ({xs+0.35},0.62) rectangle ({xs+1.15},2.0);')
        b.append(f'\\draw[line width=.8pt,fill=white] ({xs+0.02},0.12) rectangle ({xs+1.48},0.58);')
        for i,ch in enumerate(ac): b.append(N(xs+0.27+0.48*i,0.35,ch,'font=\\normalsize\\bfseries'))
        for i in (1,2): b.append(f'\\draw[line width=.5pt] ({xs+0.02+0.49*i},0.12)--({xs+0.02+0.49*i},0.58);')
    # P tRNA: polipeptit zinciri (3 amino asit), A tRNA: 1 amino asit
    for (cx,cy) in ((2.75,2.3),(2.4,2.8),(2.75,3.2)): b.append(f'\\draw[line width=.9pt,fill=vurgu!45] ({cx},{cy}) circle (.17);')
    b.append('\\draw[line width=.9pt] (2.75,2.13)--(2.75,2.0);\\draw[line width=.6pt] (2.75,2.3)--(2.4,2.8)--(2.75,3.2);')
    b.append('\\draw[line width=.9pt,fill=vurgu!45] (4.85,2.3) circle (.17);\\draw[line width=.9pt] (4.85,2.13)--(4.85,2.0);')
    b.append(N(2.75,-0.95,'P','font=\\normalsize\\bfseries')); b.append(N(4.85,-0.95,'A','font=\\normalsize\\bfseries'))
    b.append('\\draw[line width=1.2pt,-{Stealth[length=2.3mm,width=1.9mm]}] (6.6,-0.9)--(7.9,-0.9);')
    return tk('\n'.join(b))
q('0006',[A('Antikodonlardan kodonlara','Antikodon, bağlandığı kodona tümleyendir; ikisi de aynı hizada yazıldığından harf harf tümlenir.','CGA → GCU · UUC → AAG'),
   A('mRNA bölümünü birleştir','P bölgesindeki kodon solda, A bölgesindekiyle birlikte 5’→3’ okunacak biçimde yazılır.','mRNA: 5’–GCU AAG–3’'),
   A('Kodlayıcı ipliğe geç','Kodlayıcı iplik, mRNA ile aynı diziyi taşır; yalnız urasil yerine timin bulunur.','5’–GCT AAG–3’')],
  'pr-kodlama','orta','Antikodon–gen','tRNA antikodonlarından, mRNA’yı ve kodlayıcı DNA ipliğini belirler.','şekilli',
  metin=f'Şekilde bir ribozomda translasyonun sürdüğü bir an gösterilmiştir. P ve A bölgelerindeki tRNA’ların antikodonları 3’→5’ yönünde, mRNA’nın 5’ ucu solda olacak biçimde yazılmıştır; mRNA’nın nükleotitleri gösterilmemiştir. Ribozom, mRNA üzerinde sağa doğru ilerlemektedir.\nBuna göre, bu iki tRNA’nın bağlandığı mRNA bölgesini sentezleyen genin kodlayıcı ipliğinin bu bölümü aşağıdakilerden hangisidir?',
  sekil=transl_fig(),dogru=f6(kod6),yan=d6,sira=yer('E',f6(kod6),[x[0] for x in d6]),istenen='Kodlayıcı ipliğin 5’→3’ dizisi.',
  ip=['Antikodonlardan önce mRNA kodonlarını bul; sonra mRNA ile kodlayıcı DNA ipliği arasındaki tek farkı düşün.'],bilgi=[BK,BL],
  puf='Antikodon → kodon (tümleyen) → kodlayıcı iplik (aynı dizi, U yerine T).')

# ===== 07 · orta · prokaryot–ökaryot (yanlış olanlar)
card(7,'pr-transk','Bakteri ve ökaryot protein sentezi','Bakteride transkripsiyon ve translasyon aynı bölmede eş zamanlı; ökaryotta mRNA çekirdekte sentezlenir, sitoplazmada ribozomlarda okunur.','Ökaryotta translasyonun çekirdekte olduğunu sanmak.','orta','öncüllü',3,'bakteri–insan protein sentezi')
d7={'I':('Bakterilerde mRNA sentezi sürerken ribozomlar mRNA’ya bağlanıp translasyona başlayabilir.',True,'bakterilerde çekirdek zarı yoktur, transkripsiyon ve translasyon aynı bölmede ve eş zamanlı yürüyebilir'),
    'II':('İnsan hücrelerinde mRNA’nın sentezlendiği bölme ile polipeptit sentezinin yapıldığı bölme aynıdır.',False,'insan hücrelerinde mRNA çekirdekte sentezlenir, polipeptit sitoplazmadaki ribozomlarda sentezlenir'),
    'III':('Hem bakterilerde hem insanda polipeptit sentezi ribozomlarda gerçekleşir.',True,'translasyon her iki canlı grubunda da ribozomlarda yapılır')}
r7=onc(d7,'A',neg=True)
q('0007',oncad(d7,True),'pr-transk','orta','Prokaryot ve ökaryot','Prokaryot ve ökaryotlarda transkripsiyon–translasyon bölmelerini karşılaştırır.','öncüllü',
  metin=oncmetin('Bakteri hücrelerinde ve insan hücrelerinde protein sentezi; mRNA’nın sentezlendiği ve okunduğu hücre bölmeleri bakımından farklılıklar gösterir.',d7,'Buna göre, bu yargılardan hangileri yanlıştır?'),
  dogru=r7['dogru'],yan=r7['yan'],sira=r7['sira'],istenen='Yanlış olan yargılar.',
  ip=['Her iki hücre tipinde mRNA’nın nerede sentezlendiğini ve okunduğunu ayrı ayrı düşün.'],bilgi=[BT,BL],
  puf='Bakteride süreçler aynı bölmede iç içe; ökaryotta çekirdekte transkripsiyon, sitoplazmada translasyon.')

# ===== 08 · orta · kodon tablosu · sessiz mutasyon sayısı
card(8,'pr-sifre','Tek nükleotit değişimlerinin sonuçları','Bir kodonun 9 olası tek nükleotit değişimi tabloda taranır; aynı amino asit çıkanlar sessizdir.','Yalnız 3. nükleotit değişimlerini saymak; dur kodonunu amino asit saymak.','orta','şekilli',4,'CGA kodonunda sessiz değişimler')
def degisimler(k):
    out=[]
    for i in range(3):
        for b in BZ:
            if b!=k[i]: out.append(k[:i]+b+k[i+1:])
    return out
k8='CGA'; dv=degisimler(k8); assert len(dv)==9
ses=[c for c in dv if KOD[c]==KOD[k8]]; yan_=[c for c in dv if KOD[c] not in (KOD[k8],'*')]; son=[c for c in dv if KOD[c]=='*']
assert (len(ses),len(yan_),len(son))==(4,4,1) and sorted(ses)==['AGA','CGC','CGG','CGU'] and son==['UGA']
ucnt=[c for c in dv if c[:2]==k8[:2] and KOD[c]==KOD[k8]]; assert len(ucnt)==3
d8=[(3,'Yalnız 3. nükleotitteki değişimleri (CGU, CGC, CGG) saymış; 1. nükleotitteki CGA → AGA değişimi de arjinin şifrelediğinden sessizdir.','dikkat'),
    (5,'Dur kodonuna (UGA) dönüşen değişimi de sessiz saymış; dur kodonu amino asit şifrelemez ve polipeptiti kısaltır.','bilgi'),
    (8,'Dur kodonuna dönüşen dışındaki bütün değişimleri sessiz saymış; amino asidi değiştirenler (Gly, Gln, Pro, Leu) sessiz değildir.','bilgi'),
    (9,'Dokuz değişimin hepsinde amino asit dizilimi değişmediğini düşünmüş; oysa 5 değişim diziliminin değişmesine yol açar.','bilgi')]
assert 5==len(ses)+len(son) and 8==len(ses)+len(yan_)
q('0008',[A('Olası değişimleri yaz','Üç nükleotitin her biri diğer üç nükleotitten biriyle yer değiştirebilir; 3 × 3 = 9 farklı kodon oluşur.','CGA → AGA, GGA, UGA · CAA, CCA, CUA · CGU, CGC, CGG'),
   A('Tablodan amino asitleri oku','CGA arjinindir (Arg); her yeni kodonun amino asidi tablodan okunur.','AGA Arg · GGA Gly · UGA Dur · CAA Gln · CCA Pro · CUA Leu · CGU, CGC, CGG Arg'),
   A('Sessizleri ayır','Arjinin şifrelemeye devam edenler diziliminin değişmediği değişimlerdir.','AGA, CGU, CGC, CGG → 4 değişim')],
  'pr-sifre','orta','Sessiz mutasyon','Kodon tablosunda tek nükleotit değişimlerini tarayarak sessiz mutasyon sayısını bulur.','şekilli',
  metin='Bir genin kalıp ipliğinde meydana gelen tek bir nükleotit değişimi, mRNA’daki bir kodonun yalnız bir nükleotidinin başka bir nükleotitle yer değiştirmesine yol açmaktadır. Değişime uğrayan kodon, mRNA’da CGA’dır ve her olası değişim eşit şansla gerçekleşebilmektedir. Şekilde standart kodon tablosu verilmiştir.\nBuna göre, CGA kodonunda olabilecek farklı tek nükleotit değişimlerinden kaç tanesinde polipeptidin amino asit dizilimi değişmez?',
  sekil=COD,dogru=4,yan=d8,istenen='Amino asit dizilimini değiştirmeyen farklı değişim sayısı.',
  ip=['Kodonun her üç nükleotidini ayrı ayrı değiştirerek elde ettiğin dokuz kodonun amino asidini tabloda karşılaştır.'],bilgi=[BM,BS],
  puf='Sessiz mutasyon aranırken önce 3. nükleotite, sonra diğer ikisine de bak; tabloyu eksiksiz tara.')

# ===== 09 · orta · deney tablosu · ulaşılamaz yargılar
card(9,'pr-sifre','Sentetik mRNA deneyi','Sonuçlardan yalnız doğrudan gözlenenlere ulaşılır; çoklu kodon ve evrensellik bu verilerden çıkarılamaz.','Gerçekte doğru olan her bilgiye deneyle ulaşıldığını sanmak.','orta','tablo',4,'sentetik mRNA deneyi yorumu')
d9={'I':('UCU ve CUC kodonları farklı amino asitleri şifreler.',True,'üçüncü tüpte mRNA, UCU ve CUC kodonlarının ardışık tekrarından oluşur ve polipeptitte Ser ile Leu dönüşümlü sıralanır; bu iki kodon farklı amino asitleri şifreler'),
    'II':('Bir amino asit birden fazla kodon tarafından şifrelenebilir.',False,'tüplerin hiçbirinde aynı amino asidi şifreleyen iki farklı kodon gözlenmemiştir; bu bilgi gerçekte doğru olsa da sonuçlardan çıkarılamaz'),
    'III':('Genetik şifre bütün canlılarda aynıdır.',False,'deney yalnız tek bir hücre özütüyle yapılmıştır; şifrenin bütün canlılarda aynı olduğu bu sonuçlardan çıkarılamaz')}
assert cevir('UUUUUUUUUUUU')[0]==['Phe']*4 and cevir('AAAAAAAAAAAA')[0]==['Lys']*4 and cevir('UCUCUCUCUCUC')[0]==['Ser','Leu','Ser','Leu']
sab9=('{x}. yargıya ulaşılamayacağını sanmış; oysa deney sonuçlarından bu yargıya ulaşılabilir: {n}.','{x}. yargıya ulaşılabileceğini sanmış; oysa deney sonuçları bu yargıyı göstermez: {n}.')
r9=onc(d9,'D',neg=True,sab=sab9)
q('0009',oncad(d9,True,etiket=('ulaşılabilir','ulaşılamaz'),bas=[A('Verileri oku','Tablodaki her satır, tek tip mRNA’dan hangi polipeptidin oluştuğunu gösterir.','poli-U → Phe · poli-A → Lys · (UC) tekrarı → Ser–Leu dönüşümlü')],son='Deney verilerinden çıkarılamayan yargılar bir arada yazılır.'),
  'pr-sifre','orta','Deney yorumu','Sentetik mRNA deneyinin sonuçlarından hangi yargılara ulaşılabileceğini değerlendirir.','tablo',
  metin=oncmetin('Bir araştırmacı, ribozom, tRNA, 20 çeşit amino asit ve gerekli enzimleri içeren hücre özütünü üç ayrı tüpe paylaştırıyor. Her tüpe nükleotit dizisi bilinen tek tip sentetik mRNA ekleyerek oluşan polipeptitleri çözümlüyor. Kodonların üçer nükleotitten oluştuğu bilinmektedir. Sonuçlar tabloda verilmiştir.',d9,'Buna göre, bu yargılardan hangilerine bu deneyin sonuçlarıyla ulaşılamaz?'),
  sekil=tablo_svg(['Tüp','Eklenen sentetik mRNA','Oluşan polipeptit'],[['1','UUUUUUUUUUUU…','Phe – Phe – Phe – …'],['2','AAAAAAAAAAAA…','Lys – Lys – Lys – …'],['3','UCUCUCUCUCUC…','Ser – Leu – Ser – Leu – …']]),
  dogru=r9['dogru'],yan=r9['yan'],sira=r9['sira'],istenen='Deney sonuçlarıyla ulaşılamayan yargılar.',
  ip=['Her yargının tablodaki hangi satırdan doğrudan okunabildiğine bak; hiçbir satırın göstermediği yargıyı ele.'],bilgi=[BD,BS],
  puf='Yargı gerçekte doğru olsa bile, veriler onu göstermiyorsa o deneyle ulaşılamaz.')

# ===== 10 · orta · transkripsiyon şeması · yanlış ifade
card(10,'pr-transk','Transkripsiyon şeması','RNA polimeraz kalıp ipliği 3’→5’ okur, mRNA 5’→3’ uzar; mRNA kalıba tümleyen, kodlayıcı iplikle benzerdir.','Kalıbın 5’→3’ okunduğunu sanmak.','orta','şekilli',3,'transkripsiyon şeması ifadeleri')
def transk_fig():
    b=[]
    b.append('\\draw[fill=vurgu!16,draw=none] (4.0,0.7) ellipse (1.55 and 1.5);')
    for (xa,xb) in ((0.1,2.5),(5.5,7.9)):
        b.append(f'\\draw[line width=1.5pt] ({xa-0.3},1.0)--({xb+0.3 if xa>1 else xb},1.0);' if False else f'\\draw[line width=1.5pt] ({xa},1.0)--({xb},1.0);\\draw[line width=1.5pt] ({xa},0.4)--({xb},0.4);')
        x=xa+0.15
        while x<xb: b.append(f'\\draw[line width=.6pt] ({x:.2f},0.4)--({x:.2f},1.0);'); x+=0.3
    b.append('\\draw[line width=1.5pt,rounded corners=9pt] (2.5,1.0)--(3.1,1.75)--(4.9,1.75)--(5.5,1.0);')
    b.append('\\draw[line width=1.5pt,rounded corners=9pt] (2.5,0.4)--(3.1,-0.35)--(4.9,-0.35)--(5.5,0.4);')
    b.append('\\draw[line width=1.9pt,vurgu,rounded corners=6pt] (4.5,-0.1)--(3.5,-0.1)--(2.9,-0.75)--(1.2,-1.25);')
    b.append(N(-0.45,1.0,f'5{PR}'));b.append(N(8.35,1.0,f'3{PR}'));b.append(N(-0.45,0.4,f'3{PR}'));b.append(N(8.35,0.4,f'5{PR}'))
    b.append(N(0.85,-1.35,f'5{PR}'))
    b.append(N(0.7,1.75,'I','font=\\normalsize\\bfseries'));b.append(f'\\draw[{OKU},line width=.8pt] (0.7,1.5)--(0.8,1.07);')
    b.append(N(7.4,-0.55,'II','font=\\normalsize\\bfseries'));b.append(f'\\draw[{OKU},line width=.8pt] (7.4,-0.3)--(7.3,0.33);')
    b.append(N(4.0,2.55,'III','font=\\normalsize\\bfseries'));b.append(f'\\draw[{OKU},line width=.8pt] (4.0,2.3)--(4.0,2.02);')
    b.append(N(2.0,-0.55,'IV','font=\\normalsize\\bfseries'));b.append(f'\\draw[{OKU},line width=.8pt] (2.0,-0.78)--(2.0,-1.0);' if False else '')
    b.append(f'\\draw[{OKU},line width=1.3pt] (5.6,-1.0)--(7.2,-1.0);')
    return tk('\n'.join(b),0.95)
it10=[('II numaralı iplik kalıp olarak kullanılır; mRNA bu ipliğe tümleyen ribonükleotitlerle sentezlenir.',True,'mRNA, II numaralı ipliğe tümleyen nükleotitlerle uzamaktadır; bu iplik kalıptır'),
      ('III numaralı yapı, ribonükleotitleri birbirine bağlayarak mRNA zincirini uzatır.',True,'III numaralı yapı RNA polimerazdır ve ribonükleotitleri birbirine bağlar'),
      ('RNA polimeraz, kalıp ipliği 5’→3’ yönünde okuyarak ilerler.',False,'kalıp olan II numaralı iplik soldan sağa 3’→5’ yönündedir ve enzim bu yönde ilerlediğinden kalıp 3’→5’ yönünde okunur'),
      ('IV numaralı molekülün dizisi, I numaralı ipliğin dizisine benzer; yalnız timin yerine urasil içerir.',True,'mRNA kalıba tümleyendir; kalıba karşı duran kodlayıcı iplikle aynı diziyi, T yerine U ile taşır'),
      ('Şekildeki olay, ökaryotik hücrelerde çekirdekte gerçekleşir.',True,'ökaryotlarda mRNA sentezi çekirdekte yapılır')]
r10,n10=tek(it10,False,'C',yon=('Bu ifadeyi doğru sanmış; oysa yanlıştır: ','Bu ifadeyi yanlış sanmış; oysa doğrudur: '))
q('0010',[A('Şekli oku','Soldan sağa I iplik 5’→3’, II iplik 3’→5’ uzanır; enzim sağa doğru ilerler, mRNA IV ise II’ye tümleyen olarak uzamaktadır.','II: kalıp · III: enzim · IV: mRNA'),
   A('Doğru ifadeleri ele','Kalıp ve mRNA ilişkisi, enzimin görevi, mRNA–kodlayıcı iplik benzerliği ve olayın yeri doğru verilmiştir.','Dört ifade doğru'),
   A('Okuma yönünü incele','Kalıp II numaralı iplik 3’ ucu solda olacak biçimde yazılmıştır ve enzim sağa ilerlemektedir; bu da 3’→5’ yönüne karşılık gelir.','Enzim kalıbı 3’→5’ okur'),
   A('Yanlışı seç','Kalıbın 5’→3’ okunduğunu söyleyen ifade şekille ve temel bilgiyle çelişir.','“5’→3’ okuyarak” yanlış')],
  'pr-transk','orta','Transkripsiyon','Transkripsiyon şemasını yorumlayarak yanlış ifadeyi bulur.','şekilli',
  metin='Şekilde, bir ökaryotik hücrenin çekirdeğinde mRNA sentezinin gerçekleştiği DNA bölgesi gösterilmiştir. I ve II DNA ipliklerini, III ve IV ise olaya katılan diğer yapıları göstermektedir; ok, III numaralı yapının ilerleme yönünü belirtmektedir. Uçlar 5’ ve 3’ ile işaretlenmiştir.\nBuna göre, şekildeki olayla ilgili aşağıdakilerden hangisi yanlıştır?',
  sekil=transk_fig(),dogru=r10['dogru'],yan=r10['yan'],sira=r10['sira'],istenen='Şekille ilgili yanlış olan ifade.',
  ip=['mRNA’nın hangi DNA ipliğine tümleyen uzadığına ve enzimin bu iplik üzerinde hangi uçtan hangi uca ilerlediğine bak.'],bilgi=[BT,BK],
  puf='mRNA 5’→3’ uzar; bunun için RNA polimeraz kalıbı 3’→5’ okur.')

# ===== 11 · orta · kalıp bileşiminden mRNA bileşimi
card(11,'pr-kodlama','Kalıp bileşiminden mRNA bileşimi','mRNA’daki her nükleotit sayısı kalıptaki tümleyen nükleotidin sayısına eşittir.','Kalıptaki sayıları doğrudan mRNA’ya taşımak.','orta','düz',3,'kalıptan mRNA nükleotit sayıları')
kA,kT,kG,kC=20,26,28,16; assert kA+kT+kG+kC==90
mA,mU,mG,mC=kT,kA,kC,kG; dog11=mA+mG; assert dog11==42
d11=[(kA+kC,'Adenin sayısı olarak kalıptaki adenini (20), guanin sayısı olarak kalıptaki sitozini (16) almış; adenin sayısı kalıptaki timine eşittir.','bilgi'),
     (kA+kT,'mRNA’daki adenin ve guanin yerine kalıptaki adenin ve timin sayılarını (20 + 26) toplamış.','bilgi'),
     (kA+kG,'Kalıptaki adenin ve guanin sayılarını (20 + 28) doğrudan almış; oysa mRNA kalıba tümleyendir ve sayılar yer değiştirir.','bilgi'),
     (kT+kG,'Adenin için kalıptaki timini (26) doğru bulmuş, guanin için kalıptaki guanini (28) almış; mRNA’daki guanin kalıptaki sitozine karşılık gelir.','bilgi')]
assert [x[0] for x in d11]==[36,46,48,54]
q('0011',[A('Eşleşmeleri belirle','mRNA’da A kalıptaki T’ye, G kalıptaki C’ye karşılık gelir; U ise kalıptaki A’ya karşılık gelir.','mRNA’da A kalıptaki T’den; U kalıptaki A’dan; G kalıptaki C’den; C kalıptaki G’den gelir'),
   A('mRNA’daki sayıları bul','Kalıptaki her nükleotit, karşısına tümleyenini getirir ve sayıları aynı kalır.','A = 26 · G = 16 (U = 20, C = 28)'),
   A('Toplamı hesapla','İstenen nükleotitlerin sayıları toplanır.','26 + 16 = 42')],
  'pr-kodlama','orta','Nükleotit sayıları','Kalıp ipliğin nükleotit sayılarından mRNA’daki nükleotit sayılarını bulur.','düz',
  metin='Bir genin kalıp ipliğinin 90 nükleotitlik bir bölümünde 20 adenin, 26 timin, 28 guanin ve 16 sitozin nükleotiti bulunmaktadır. Bu bölümün tamamı transkripsiyonla mRNA’ya kopyalanmakta ve başka hiçbir nükleotit eklenmemektedir.\nBuna göre, oluşan mRNA’da adenin ile guanin nükleotitlerinin toplam sayısı kaçtır?',
  dogru=dog11,yan=d11,istenen='mRNA’daki adenin ve guanin nükleotitlerinin toplam sayısı.',
  ip=['mRNA’daki adenin ve guanin için kalıpta hangi nükleotitlerin karşılık geldiğini düşün.'],bilgi=[BK],
  puf='mRNA’daki bir nükleotidin sayısı, kalıptaki tümleyen nükleotidin sayısına eşittir.')

# ===== 12 · zor · gen yapısı · ekson–intron
card(12,'pr-transk','Eksonlardan polipeptit uzunluğu','Olgun mRNA yalnız eksonlardan oluşur; kodon sayısı eksonların toplamının 3’e bölümüdür ve dur kodonu amino asit vermez.','İntronları da saymak; dur kodonunu amino asit saymak.','zor','şekilli',5,'ekson–intron ve amino asit sayısı')
ex=[150,120,210,90]; inn=[240,300,90]; assert sum(ex)%3==0
top=sum(ex)+sum(inn); aa12=(sum(ex)-3)//3; assert (top,sum(ex),aa12)==(1200,570,189)
d12=[(sum(ex)//3,'Olgun mRNA’daki 190 kodondan dur kodonunu da amino asit saymış; dur kodonu amino asit şifrelemez.','bilgi'),
     (top//3-1,'İntronları çıkarmadan 1200 nükleotitin tamamını kodon saymış (1200 ÷ 3 − 1 = 399); intronlar mRNA’dan atılır.','bilgi'),
     (top//3,'İntronları çıkarmamış ve dur kodonunu da amino asit saymış (1200 ÷ 3 = 400).','bilgi'),
     (sum(ex),'Eksonların nükleotit sayısını (570) amino asit sayısı sanmış; her amino asit üç nükleotitle şifrelenir.','islem')]
assert [x[0] for x in d12]==[190,399,400,570]
def gen_fig():
    b=[]; x=0.0; sc=1/120
    for i,e in enumerate(ex):
        w=e*sc; b.append(f'\\draw[line width=1pt,fill=vurgu!30] ({x:.3f},0) rectangle ({x+w:.3f},0.7);'); b.append(N(x+w/2,0.35,str(e),'font=\\normalsize\\bfseries')); x+=w
        if i<len(inn):
            w=inn[i]*sc; b.append(f'\\draw[line width=1.3pt] ({x:.3f},0.35)--({x+w:.3f},0.35);'); b.append(N(x+w/2,0.72+0.0,str(inn[i]),'font=\\normalsize,anchor=south')); x+=w
    b.append(N(-0.45,0.35,f'5{PR}'));b.append(N(x+0.45,0.35,f'3{PR}'))
    b.append('\\draw[line width=1pt,fill=vurgu!30] (1.2,-1.05) rectangle (1.8,-0.65);'); b.append(N(1.95,-0.85,'Ekson','anchor=west,font=\\normalsize'))
    b.append('\\draw[line width=1.3pt] (4.2,-0.85)--(4.9,-0.85);'); b.append(N(5.05,-0.85,'İntron','anchor=west,font=\\normalsize'))
    b.append(N(6.9,-0.85,'(sayılar nükleotit sayısıdır)','anchor=west,font=\\normalsize'))
    return tk('\n'.join(b),0.95)
q('0012',[A('Eksonları topla','Olgun mRNA’da yalnız eksonlar kalır; intronlar transkripsiyondan sonra çıkarılır.','150 + 120 + 210 + 90 = 570 nükleotit'),
   A('Kodon sayısını bul','Her kodon üç nükleotitten oluşur.','570 ÷ 3 = 190 kodon'),
   A('Dur kodonunu çıkar','Kodlayıcı bölgenin son kodonu dur kodonudur ve amino asit şifrelemez.','190 − 1 = 189 amino asit')],
  'pr-transk','zor','Ekson–intron','Eksonların toplamından dur kodonunu çıkararak polipeptit uzunluğunu hesaplar.','şekilli',
  metin='Şekilde, ökaryotik bir genin ekson ve intron bölgeleri nükleotit sayılarıyla birlikte gösterilmiştir. Gen transkribe edildikten sonra intronlar çıkarılıp eksonlar birleştirilmekte; oluşan olgun mRNA’nın tamamı translasyonda kodlayıcı bölge olarak kullanılmaktadır. İlk ekson başlangıç kodonuyla başlar, son ekson dur kodonuyla biter ve olgun mRNA’da başka nükleotit bulunmaz.\nBuna göre, bu genden sentezlenen polipeptit kaç amino asitten oluşur?',
  sekil=gen_fig(),dogru=aa12,yan=d12,istenen='Polipeptidin amino asit sayısı.',
  ip=['Hangi bölgelerin olgun mRNA’da kaldığını belirle; kalan nükleotitlerden kodon sayısına, oradan amino asit sayısına geç.'],bilgi=[BT,BN],
  puf='Olgun mRNA = eksonlar; amino asit sayısı = eksonların toplamı ÷ 3 − 1.')

# ===== 13 · orta · dizi şekli · anlamsız mutasyon
card(13,'pr-mutasyon','Anlamsız mutasyonun etkisi','Tek nükleotit değişimiyle bir kodon UAA, UAG ya da UGA olursa polipeptit orada sonlanır.','Yalnız tek amino asidin değiştiğini sanmak.','orta','şekilli',4,'anlamsız mutasyonda kısalma')
m13='AUGGCUCAGUUCGGACUAAAGUGA'; k13n=kalip_of(m13); k13m=k13n[:6]+'ATC'+k13n[9:]; m13m=mrna_of(k13m)
assert k13n[6:9]=='GTC' and m13m[6:9]=='UAG' and len(cevir(m13)[0])==7 and len(cevir(m13m)[0])==2
fark13=7-2; assert fark13==5
d13=[(1,'Yalnız 3. kodondaki amino asidin kaybolduğunu düşünmüş; oysa değişen kodon dur kodonuna dönüştüğü için sonrası da sentezlenmez.','bilgi'),
     (2,'Mutasyonlu polipeptitte kalan amino asit sayısını (2) kısalma miktarı sanmış.','dikkat'),
     (4,'Mutasyonun olduğu kodondan sonraki amino asitleri (4) saymış, 3. kodondaki amino asidi saymamış.','dikkat'),
     (7,'Polipeptidin tamamının kaybolduğunu düşünmüş; mutasyondan önceki iki kodon normal şekilde okunur.','bilgi')]
q('0013',[A('mRNA’ları yaz','Her iki kalıba tümleyen mRNA yazılır; yalnız 3. üçlü farklıdır.',f'Normal: {uc(m13)} · Mutasyonlu: {uc(m13m)}'),
   A('3. kodonu incele','Mutasyonlu gende 3. kodon UAG olmuştur; UAG bir dur kodonudur.','CAG (Gln) → UAG (dur)'),
   A('Polipeptit uzunluklarını bul','Normal gen dur kodonu UGA’ya kadar 7 amino asit, mutasyonlu gen ise 3. kodonda dur kodonuna ulaştığı için 2 amino asit sentezler.','7 ve 2 amino asit'),
   A('Farkı hesapla','Kısalma, iki polipeptidin amino asit sayıları arasındaki farktır.','7 − 2 = 5')],
  'pr-mutasyon','orta','Anlamsız mutasyon','Kalıp iplikteki değişimin dur kodonu oluşturmasıyla polipeptidin kaç amino asit kısaldığını bulur.','şekilli',
  metin='Şekilde, bir bakteri geninin normal ve mutasyona uğramış hâllerine ait kalıp iplik dizileri üçlü gruplar hâlinde verilmiştir. Her iki gende de transkripsiyon soldaki ilk üçlüden başlamakta, mRNA’daki ilk kodon başlangıç kodonu olmakta ve translasyon ilk dur kodonunda sonlanmaktadır.\nBuna göre, mutasyonlu gende sentezlenen polipeptit, normal polipeptide göre kaç amino asit kısalmıştır?',
  sekil=seqfig([('Normal gen',k13n,1.5),('Mutasyonlu gen',k13m,0)],dx=0.3,gap=0.2),dogru=fark13,yan=d13,istenen='Polipeptit kısalması (amino asit sayısı olarak).',
  ip=['İki kalıp dizisini karşılaştırıp farklı olan üçlüyü bul; bu üçlüye karşılık gelen mRNA kodonunun ne olduğuna bak.'],bilgi=[BM,BK],
  puf='Kodon dur kodonuna dönüşürse, polipeptit o kodondan önceki amino asitlerle sonlanır.')

# ===== 14 · zor · kodon tablosu · çerçeve kayması
card(14,'pr-mutasyon','Nükleotit eklenmesi ve okuma çerçevesi','Tek nükleotit eklenmesi çerçeveyi kaydırır; eklenen yerden sonraki kodonlar değişir ve yeni bir dur kodonu oluşabilir.','Yalnız eklenen yerdeki amino asidin değiştiğini sanmak; eklenen nükleotidi tümlemeden yazmak.','zor','şekilli',5,'çerçeve kayması ve yeni dur kodonu')
m14='AUGGCUACCUUUGAUCGAUAA'; k14=kalip_of(m14); assert k14=='TACCGATGGAAACTAGCTATT'
k14m=k14[:6]+'T'+k14[6:]; m14m=mrna_of(k14m); p14,_=cevir(m14); p14m,s14m=cevir(m14m)
assert p14==['Met','Ala','Thr','Phe','Asp','Arg'] and p14m==['Met','Ala','Asn','Leu'] and s14m
mu14=m14[:6]+'U'+m14[6:]; p14u=cevir(mu14)[0]; assert p14u==['Met','Ala','Tyr','Leu']
d14=[(dz(p14),'Eklenen nükleotidin polipeptidi etkilemediğini düşünmüş; oysa okuma çerçevesi kaydığı için eklenen yerden sonraki kodonlar değişir.','bilgi'),
     (dz(p14[:2]+['Asn']+p14[3:]),'Yalnız eklenme yerindeki kodonun değiştiğini sanmış; çerçeve kaydığı için sonraki kodonlar da değişir.','bilgi'),
     (dz(p14[:2]+['Asn']+p14[2:]),'Eklenen bir nükleotidin polipeptide bir amino asit eklediğini düşünmüş; oysa üçlü okuma çerçevesi kayar.','bilgi'),
     (dz(p14u),'Kalıba eklenen timine karşılık mRNA’ya urasil eklendiğini sanmış; mRNA’ya eklenen nükleotit, timinin tümleyeni olan adenindir.','bilgi')]
assert len({dz(p14m)}|{x[0] for x in d14})==5
q('0014',[A('Normal mRNA’yı yaz','Kalıba tümleyen mRNA yazılır ve kodonlara ayrılır.',f'{uc(m14)} → Met, Ala, Thr, Phe, Asp, Arg, dur'),
   A('Eklenmeyi mRNA’ya yansıt','Kalıbın 6. ve 7. nükleotitleri arasına T eklenince mRNA’nın 6. ve 7. nükleotitleri arasına A eklenir.',f'mRNA: {m14[:6]} A {m14[6:]}'),
   A('Yeni kodonlara ayır','AUG başlangıç kodonundan itibaren üçlü gruplar yeniden oluşur; ekleme yerinden sonra bütün üçlüler farklıdır.',uc(m14m)),
   A('Tablodan oku','Her kodonun amino asidi tablodan bulunur; UGA bu çerçevede dur kodonu olarak ilk kez okunur.',' · '.join(f'{c} → {"Dur" if KOD[c]=="*" else AD[KOD[c]]}' for c in kodl(m14m)[:5])),
   A('Polipeptidi yaz','Sentez dur kodonunda sonlanır.',dz(p14m))],
  'pr-mutasyon','zor','Çerçeve kayması','Nükleotit eklenmesiyle kayan okuma çerçevesinde yeni kodonlardan oluşan polipeptidi bulur.','şekilli',
  metin=f'Bir bakteri geninin kalıp ipliğinin bir bölümü 3’–{k14}–5’ dizisindedir. Bu bölümden sentezlenen mRNA’nın ilk kodonu başlangıç kodonudur ve translasyon ilk dur kodonunda sonlanmaktadır. Gende meydana gelen bir mutasyonla, kalıp ipliğin 6. ve 7. nükleotitleri arasına bir timin nükleotidi eklenmiştir. Şekilde standart kodon tablosu verilmiştir.\nBuna göre, mutasyonlu gen bu bölümden hangi polipeptidi sentezler?',
  sekil=COD,dogru=dz(p14m),yan=d14,sira=yer('E',dz(p14m),[x[0] for x in d14]),istenen='Mutasyonlu genin sentezlediği polipeptit.',
  ip=['Kalıba eklenen nükleotidin mRNA’da hangi nükleotide karşılık geldiğini bul; sonra üçlü okumanın ekleme yerinden sonra nasıl değiştiğini incele.'],bilgi=[BM,BK],
  puf='Üçün katı olmayan ekleme ya da çıkarma okuma çerçevesini kaydırır ve ilerideki kodonları baştan değiştirir.')

# ===== 15 · zor · mutasyon: hidrojen bağı + peptit bağı
card(15,'pr-mutasyon','Dur kodonu oluşturan baz çifti değişimi','G≡C → A=T değişimi 1 hidrojen bağı azaltır; erken dur kodonu peptit bağı sayısını amino asit kaybı kadar azaltır.','Bağ sayısını nükleotit sayısıyla karıştırmak; kayıp amino asidi yanlış saymak.','zor','düz',5,'baz çifti değişimi ve bağ sayıları')
n15=60; kodno=21; assert KOD['CAG']=='Q' and KOD['UAG']=='*'
bag_n=n15-1; bag_m=(kodno-1)-1; kayip15=bag_n-bag_m; assert (bag_n,bag_m,kayip15)==(59,19,40) and 3-2==1 and n15-kodno==39
dg15='H bağı 1 azalır; peptit bağı 40 azalır'
d15=[('H bağı 1 artar; peptit bağı 40 azalır','A=T çiftinin G≡C çiftinden daha çok hidrojen bağı içerdiğini sanmış; oysa G≡C üç, A=T iki hidrojen bağlıdır.','bilgi'),
     ('H bağı 2 azalır; peptit bağı 40 azalır','Kalıptaki ve kodlayıcıdaki değişimi ayrı birer bağ kaybı saymış; oysa tek baz çifti değişmiştir ve kayıp 3 − 2 = 1 bağdır.','islem'),
     ('H bağı 1 azalır; peptit bağı 39 azalır','Kaybı 60 − 21 = 39 bulmuş; mutasyonlu polipeptit 20 amino asitli olduğundan 59 − 19 = 40 peptit bağı kaybolur.','islem'),
     ('H bağı değişmez; peptit bağı 40 azalır','Baz çifti değişince hidrojen bağı sayısının değişmediğini düşünmüş; oysa A=T ve G≡C çiftlerinin bağ sayıları farklıdır.','bilgi')]
q('0015',[A('Hidrojen bağı değişimi','G≡C çifti 3, A=T çifti 2 hidrojen bağı içerir; bir çift değiştiği için fark bulunur.','3 → 2: 1 azalır'),
   A('Mutasyonlu kodonu bul','Kalıpta G yerine A gelince mRNA’da C yerine U oluşur; CAG, UAG’ye dönüşür ve UAG dur kodonudur.','21. kodon CAG → UAG (dur)'),
   A('Polipeptit uzunluklarını bul','Normalde 60, mutasyonlu gende ise 21. kodondan önceki 20 amino asit sentezlenir.','60 ve 20 amino asit'),
   A('Peptit bağı farkını hesapla','Tek zincirde peptit bağı sayısı amino asit sayısından 1 eksiktir.','59 − 19 = 40 azalır')],
  'pr-mutasyon','zor','Mutasyon ve bağ sayıları','Dur kodonu oluşturan baz çifti değişiminde hidrojen bağı ve peptit bağı değişimini hesaplar.','düz',
  metin='Bir bakteri geninden sentezlenen polipeptit 60 amino asitten oluşmaktadır. Genin kalıp ipliğindeki bir G nükleotidi A ile, kodlayıcı iplikte buna karşı gelen C nükleotidi de T ile yer değiştirmiş; böylece bir G≡C baz çifti, A=T baz çiftine dönüşmüştür. Bu değişim, mRNA’nın 21. kodonunun CAG iken UAG olmasına yol açmıştır ve translasyon ilk dur kodonunda sonlanmaktadır.\nBuna göre, mutasyon sonucunda genin toplam hidrojen bağı sayısı ile sentezlenen polipeptitteki peptit bağı sayısı nasıl değişir?',
  dogru=dg15,yan=d15,sira=yer('D',dg15,[x[0] for x in d15]),istenen='Hidrojen bağı ve peptit bağı sayısındaki değişim.',
  ip=['Baz çiftlerinin hidrojen bağı sayılarını karşılaştır; ardından yeni kodonun polipeptidi nerede sonlandırdığına bak.'],bilgi=[BH,BP],
  puf='G≡C ile A=T arasındaki dönüşüm 1 hidrojen bağı farkı yaratır; erken dur kodonu, kaybolan amino asit sayısı kadar peptit bağı azaltır.')

# ===== 16 · zor · tablo · nükleik asit bileşimi (kesinlikle doğru)
card(16,'pr-nukleik','Nükleotit bileşiminden molekül türü','Urasil RNA’yı gösterir; A = T ve G = C olması çift zincir için gerekli ama yeterli kanıt değildir; eşitlik bozuksa çift zincir olamaz.','Eşit oranları çift zincirin kanıtı saymak.','zor','tablo',4,'X, Y, Z nükleik asit bileşimi')
t16={'X':(30,30,0,20,20),'Y':(24,0,30,26,20),'Z':(22,28,0,18,32)}
X,Y,Z=t16['X'],t16['Y'],t16['Z']
assert Y[2]>0 and X[0]==X[1] and X[3]==X[4] and Z[1]>0 and Z[0]!=Z[1] and Z[3]!=Z[4]
d16={'I':('Y bir RNA molekülüdür.',True,'Y’de urasil bulunur ve DNA’da urasil bulunmaz'),
     'II':('X çift zincirli bir DNA molekülüdür.',False,'X’te A = T ve G = C olması çift zincirli olduğunu kesinleştirmez; tek zincirli bir DNA’da da sayılar tesadüfen eşit olabilir'),
     'III':('Z tek zincirli bir DNA molekülüdür.',True,'Z’de timin bulunduğundan DNA’dır ve A ile T, G ile C sayıları eşit olmadığından çift zincirli olamaz')}
r16=onc(d16,'C')
q('0016',oncad(d16,False,son='Kesinlikle doğru olan yargılar bir arada yazılır.',bas=[A('Tabloyu oku','Urasil ve timin sütunları RNA–DNA ayrımını, A–T ve G–C eşitlikleri ise zincir sayısı hakkında bilgi verir.','X: A = T ve G = C; Y: urasil var; Z: timin var, A ≠ T ve G ≠ C')]),
  'pr-nukleik','zor','Nükleik asit bileşimi','Nükleotit sayılarından molekülün türü ve zincir sayısı hakkında kesin çıkarım yapar.','tablo',
  metin=oncmetin('Tabloda, tek bir nükleik asit molekülünden oluşan X, Y ve Z örneklerindeki nükleotit sayıları verilmiştir. Örneklerdeki moleküllerin hepsi tam olarak çözümlenmiş ve başka nükleotit bulunmamıştır.',d16,'Buna göre, bu yargılardan hangileri kesinlikle doğrudur?'),
  sekil=tablo_svg(['Molekül','Adenin','Timin','Urasil','Guanin','Sitozin'],[[k]+[str(x) for x in v] for k,v in t16.items()]),
  dogru=r16['dogru'],yan=r16['yan'],sira=r16['sira'],istenen='Kesinlikle doğru olan yargılar.',
  ip=['Hangi nükleotitin bulunması DNA ya da RNA için ayırt edicidir; eşit oranların neyi kesinleştirip neyi kesinleştirmediğini düşün.'],bilgi=[BC,BH],
  puf='Urasil RNA’yı kesinleştirir; A = T ve G = C yalnız çift zincire uyumdur, ama eşitlik yoksa çift zincir kesinlikle olamaz.')

# ===== 17 · zor · mRNA bileşimi → gen hidrojen bağı ve timin sayısı
card(17,'pr-sayim','mRNA oranlarından gen bağ ve nükleotit sayısı','mRNA’daki A + U toplamı gendeki A=T çift sayısını, G + C toplamı G≡C çift sayısını verir; kalıptaki T sayısı mRNA’daki A sayısına eşittir.','Kalıp ve kodlayıcı iplik sayılarını karıştırmak; hidrojen bağlarını ters almak.','zor','düz',5,'mRNA oranlarından gen hidrojen bağı')
nn=300; a17,u17,g17,c17=[round(nn*x) for x in (0.15,0.25,0.35,0.25)]; assert (a17,u17,g17,c17)==(45,75,105,75) and a17+u17+g17+c17==nn
cift_at=a17+u17; cift_gc=g17+c17; H17=2*cift_at+3*cift_gc; T17=a17; assert (cift_at,cift_gc,H17,T17)==(120,180,780,45)
fm2=lambda h,t:f'{h} – {t}'
d17=[(fm2(H17//2,T17),'Yalnız tek ipliği (mRNA kadar nükleotit) göz önüne alarak hidrojen bağlarını yarıya indirmiş; çift zincirli gende bağlar iki iplik arasında oluşur.','bilgi'),
     (fm2(3*cift_at+2*cift_gc,T17),'Bağ sayılarını ters almış: A=T için 3, G≡C için 2 hidrojen bağı saymış.','bilgi'),
     (fm2(H17,u17),'Hidrojen bağını doğru bulmuş ama kalıptaki timin sayısı olarak mRNA’daki urasil sayısını (75) almış; oysa kalıptaki timin mRNA’daki adenine karşılık gelir.','dikkat'),
     (fm2(2*H17,T17),'Çift zincirli gende her ipliğin nükleotitlerini ayrı ayrı sayıp bağları ikiye katlamış; oysa bir bağ iki nükleotit arasında oluşur.','islem')]
sira17=sorted([fm2(H17,T17)]+[x[0] for x in d17],key=lambda s:tuple(map(int,s.split(' – '))))
assert sira17.index(fm2(H17,T17))==2
q('0017',[A('Nükleotit sayılarını bul','mRNA’nın 300 nükleotitindeki sayılar oranlardan hesaplanır.','A = 45 · U = 75 · G = 105 · C = 75'),
   A('Baz çiftlerini say','mRNA’daki A ve U, gendeki A=T çiftlerine; G ve C, G≡C çiftlerine karşılık gelir.','A=T çifti: 45 + 75 = 120 · G≡C çifti: 105 + 75 = 180'),
   A('Hidrojen bağlarını hesapla','A=T çiftinde 2, G≡C çiftinde 3 hidrojen bağı bulunur.','120 × 2 + 180 × 3 = 780'),
   A('Kalıptaki timini bul','Kalıptaki timin, mRNA’daki adenin ile eşleşir.','Kalıpta T = mRNA’da A = 45')],
  'pr-sayim','zor','mRNA–gen hesabı','mRNA nükleotit oranlarından genin hidrojen bağı ve kalıp ipliğindeki timin sayısını bulur.','düz',
  metin='İntron içermeyen bir bakteri geninden sentezlenen 300 nükleotitlik mRNA’nın nükleotit oranları adenin %15, urasil %25, guanin %35 ve sitozin %25’tir. mRNA, genin çift zincirli bölümünün tamamından sentezlenmiştir.\nBuna göre, bu gen bölümündeki toplam hidrojen bağı sayısı ile kalıp ipliğindeki timin sayısı sırasıyla aşağıdakilerden hangisidir?',
  dogru=fm2(H17,T17),yan=d17,sira=sira17,istenen='Toplam hidrojen bağı sayısı ve kalıp ipliğindeki timin sayısı.',
  ip=['mRNA’daki her nükleotidin gendeki hangi baz çiftine ve kalıptaki hangi nükleotide karşılık geldiğini eşle.'],bilgi=[BH,BK],
  puf='Gendeki baz çifti sayıları mRNA’daki A + U ve G + C toplamlarına eşittir.')

# ===== 18 · zor · polizom şeması (öncüllü)
card(18,'pr-transl','Polizom ve polipeptit uzunlukları','Ribozomlar mRNA üzerinde 5’→3’ ilerler; 3’ uca en yakın ribozomun zinciri en uzundur; peptit bağı = amino asit − 1.','Peptit bağı sayısını amino asit sayısına eşitlemek.','zor','şekilli',5,'polizom yargıları')
nz=[3,7,12]; kod18=25; ex_b=sum(n-1 for n in nz); fin_b=3*(kod18-1-1)
assert (ex_b,fin_b)==(19,69)
d18={'I':('En uzun polipeptiti sentezleyen ribozom, mRNA’nın 3’ ucuna en yakın olandır.',True,'ribozomlar mRNA üzerinde 5’→3’ ilerler; en uzun zincire sahip ribozom en çok ilerlemiş olduğundan 3’ uca en yakındır'),
     'II':('Şekildeki üç polipeptit zincirinde toplam 22 peptit bağı bulunur.',ex_b==22,'zincirlerde 3 + 7 + 12 = 22 amino asit vardır; tek zincirde bağ sayısı amino asit sayısından 1 eksik olduğundan 2 + 6 + 11 = 19 peptit bağı bulunur'),
     'III':('Üç ribozom da sentezi tamamladığında oluşan polipeptitlerde toplam 72 peptit bağı bulunur.',fin_b==72,'25 kodonun biri dur kodonudur; 24 amino asitli her zincirde 23 bağ olduğundan toplam 3 × 23 = 69 peptit bağı oluşur')}
r18=onc(d18,'A')
def poli_fig():
    b=['\\draw[line width=2pt] (0,0)--(11,0);',N(-0.45,0,f'5{PR}'),N(11.45,0,f'3{PR}')]
    for n in nz:
        x=0.8+0.4*n
        b.append(f'\\draw[line width=1pt,fill=vurgu!30] ({x:.2f},-0.08) ellipse (0.52 and 0.24);')
        b.append(f'\\draw[line width=1pt,fill=vurgu!14] ({x:.2f},0.42) ellipse (0.6 and 0.42);')
        for i in range(n): b.append(f'\\draw[line width=.7pt,fill=vurgu!45] ({x-0.15:.2f},{0.95+0.2*i:.2f}) circle (.08);')
        b.append(N(x-0.15,0.95+0.2*(n-1)+0.38,f'{n} aa','font=\\normalsize'))
    return tk('\n'.join(b),0.9)
q('0018',oncad(d18,False,bas=[A('Şekli oku','Zincirdeki amino asit sayıları şekilde verilmiştir; ribozomlar soldan sağa, 5’ uçtan 3’ uca doğru ilerler.','Zincirler: 3, 7 ve 12 amino asit')]),
  'pr-transl','zor','Polizom','Polizom şemasında ribozom konumu ve polipeptit uzunluklarıyla peptit bağı sayılarını değerlendirir.','şekilli',
  metin=oncmetin('Şekilde, tek bir mRNA molekülü üzerinde aynı anda translasyon yapan üç ribozom ve her birinin o anda sentezlediği polipeptit zincirinin amino asit sayısı gösterilmiştir. mRNA’nın kodlayıcı bölgesi, dur kodonu dahil 25 kodondan oluşmaktadır.',d18,'Buna göre, bu yargılardan hangileri doğrudur?'),
  sekil=poli_fig(),dogru=r18['dogru'],yan=r18['yan'],sira=r18['sira'],istenen='Doğru olan yargılar.',
  ip=['Ribozomların ilerleme yönünü ve peptit bağı sayısının amino asit sayısıyla ilişkisini hatırla; üçüncü yargıda dur kodonuna dikkat et.'],bilgi=[BL,BP],
  puf='Zincir uzunluğu ribozomun mRNA üzerinde ne kadar ilerlediğini gösterir; bağ sayısı hep amino asit sayısından 1 eksiktir.')

# ===== 19 · orta · aynı polipeptit, farklı genler (ulaşılabilir)
card(19,'pr-sifre','Aynı polipeptidi şifreleyen farklı mRNA’lar','Aynı amino asit dizilimi, farklı nükleotit dizili mRNA’larla şifrelenebilir; amino asit sayısı ve peptit bağı sayısı eşit kalır.','Amino asit dizilimi aynıysa mRNA dizisinin de aynı olması gerektiğini sanmak.','orta','öncüllü',3,'aynı polipeptit, farklı mRNA')
d19={'I':('X ve Y genlerinden sentezlenen mRNA’ların nükleotit dizileri aynı değildir.',True,'kodlayıcı bölgelerdeki G + C oranları farklı olduğundan mRNA dizileri aynı olamaz'),
     'II':('Bu mRNA’larda amino asit şifreleyen kodon sayıları birbirine eşittir.',True,'polipeptitlerin amino asit dizilimi aynı olduğundan amino asit sayıları ve her amino asit için bir kodon bulunduğundan kodon sayıları eşittir'),
     'III':('İki mRNA’dan polipeptit sentezlenirken oluşan peptit bağı sayıları eşittir.',True,'amino asit sayıları eşit olduğundan peptit bağı sayıları da eşittir')}
r19=onc(d19,'E',sab=('{x}. yargıya ulaşılamayacağını sanmış; oysa verilen bilgilerden bu yargıya ulaşılır: {n}.','{x}. yargıya ulaşılabileceğini görememiş: {n}.'))
q('0019',oncad(d19,False,etiket=('ulaşılabilir','ulaşılamaz'),son='Kesinlikle ulaşılabilen yargılar bir arada yazılır.'),
  'pr-sifre','orta','Dejenerasyon','Aynı amino asit dizilimini şifreleyen genlerin mRNA özelliklerini çıkarım yoluyla değerlendirir.','öncüllü',
  metin=oncmetin('Aynı amino asit diziliminde tek bir polipeptidi şifreleyen X ve Y genlerinin kodlayıcı bölgeleri incelendiğinde, guanin ve sitozin nükleotitlerinin oranının X’te %40, Y’de %60 olduğu belirleniyor. İki genin de kodlayıcı bölgesinin tamamı mRNA’ya aktarılıyor ve translasyonda kullanılıyor.',d19,'Buna göre, bu bilgilerden hangilerine kesinlikle ulaşılabilir?'),
  dogru=r19['dogru'],yan=r19['yan'],sira=r19['sira'],istenen='Kesinlikle ulaşılabilen yargılar.',
  ip=['Aynı amino asit dizilimini şifreleyen iki mRNA’nın neyinin aynı kalmak zorunda olduğunu, neyinin farklı olabileceğini düşün.'],bilgi=[BS,BN],
  puf='Aynı amino asit dizilimi, aynı kodon dizilimi demek değildir; ancak amino asit ve kodon sayıları eşit kalır.')

# ===== 20 · orta · translasyon (doğru olduğu söylenemez)
card(20,'pr-transl','Translasyonun başlaması ve sonlanması','Küçük alt birim mRNA’ya bağlanır; başlatıcı tRNA AUG’ye eşleşir ve metiyonin taşır; dur kodonuna karşılık gelen tRNA yoktur.','Büyük alt birimin mRNA’ya bağlandığını ve dur kodonu için tRNA bulunduğunu sanmak.','orta','öncüllü',3,'translasyonun başlama ve sonlanma yargıları')
d20={'I':('Translasyonun başlamasında ribozomun büyük alt birimi, mRNA’nın 5’ ucuna bağlanır.',False,'mRNA’ya önce ribozomun küçük alt birimi bağlanır; büyük alt birim sonra katılır'),
     'II':('Başlatıcı tRNA, AUG kodonuna bağlanır ve metiyonin taşır.',True,'başlangıç kodonu AUG’dir ve ona bağlanan başlatıcı tRNA metiyonin taşır'),
     'III':('Dur kodonuna karşılık gelen antikodonlu özel bir tRNA gelerek polipeptit sentezini sonlandırır.',False,'dur kodonlarını tanıyan tRNA yoktur; sentez bu kodonlarda sonlanır')}
r20=onc(d20,'E',neg=True,sab=('{x}. yargının doğru olduğunun söylenemeyeceğini sanmış; oysa yargı doğrudur: {n}.','{x}. yargıyı doğru sanmış; oysa yargı yanlıştır: {n}.'))
q('0020',oncad(d20,True,son='Doğru olduğu söylenemeyen yargılar bir arada yazılır.'),
  'pr-transl','orta','Translasyon evreleri','Translasyonun başlama ve sonlanma evrelerindeki olayları değerlendirir.','öncüllü',
  metin=oncmetin('Ökaryotik bir hücrede ribozomlarda polipeptit sentezi sırasında mRNA, ribozom ve tRNA’lar arasında gerçekleşen olaylarla ilgili aşağıdaki yargılar öne sürülüyor.',d20,'Buna göre, bu yargılardan hangilerinin doğru olduğu söylenemez?'),
  dogru=r20['dogru'],yan=r20['yan'],sira=r20['sira'],istenen='Doğru olduğu söylenemeyen yargılar.',
  ip=['Ribozomun hangi alt biriminin mRNA ile ilk eşleştiğini ve dur kodonuna ne olduğunu hatırla.'],bilgi=[BL,BS],
  puf='Translasyonda mRNA’ya küçük alt birim bağlanır; dur kodonunda tRNA değil sonlanma gerçekleşir.')

# ---------------- bitiş ----------------
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/bos-protein.json'
for x in P.ANA: x['kardes']=None
P.yaz(os.path.join(GD,'protein-1.json'),SC)
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2025 Biyoloji (yalnız mantık), MEB 12. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','abprotein.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
