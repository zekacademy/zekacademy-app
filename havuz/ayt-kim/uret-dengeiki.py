"""AYT Kimya · Kimyasal Tepkimelerde Denge · 2. dalga (dengeiki) · 10 soru. Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
H.KONU='Kimyasal Tepkimelerde Denge'
P=Parti('dengeiki','Kimyasal Tepkimelerde Denge','akim|Kimyasal Tepkimelerde Denge',ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2020–2026 Kimya (Kimyasal Denge, Dengeyi Etkileyen Faktörler; yalnız mantık) · MEB 12. sınıf kimya'
TIPLER={'de-dinamik':'Hız–zaman grafiği ve dinamik denge','de-kc':'Kc ifadesi','de-ice':'Denge hesabı (başlangıç–değişim–denge)','de-le':'Le Chatelier ilkesi ve dengeyi etkileyen faktörler',
 'de-grafik':'Derişim–zaman grafikleri','de-qk':'Tepkime bölümü (Q) ve denge sabiti'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKDE2-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKDE2-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=1.9mm,width=1.7mm]}'
def tikz(lines): return tikz_svg(HEAD+'\n'.join(lines)+TAIL)
def pg(opts,body,pre=''):
    return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n\\begin{axis}['+opts+']\n'+body+'\n\\end{axis}\n'+pre+'\\end{tikzpicture}')
def co(pts): return ' '.join(f'({x:.3f},{y:.4f})' for x,y in pts)
def ease(a,b,t0,t1,xmax,n=24):
    """t0..t1 arasında a'dan b'ye üstel yaklaşım; t1 sonrası b sabit"""
    pts=[]
    for i in range(n+1):
        s=i/n; pts.append((t0+(t1-t0)*s,b+(a-b)*(1-s)**3))
    if xmax>t1: pts.append((xmax,b))
    return pts
SIR=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
SETS={'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}
def onc(truth,why,pos,neg=False):
    """truth: her öncülün doğruluğu (neg=True ise 'sorulan' küme yanlış olanlardır). why: öncülün gerçek durumunu anlatan olgu cümleleri (nötr)."""
    nm=['I','II','III']; C={n for n,t in zip(nm,truth) if (not t if neg else t)}
    dogru=[s for s in SIR if SETS[s]==C][0]; p=SIR.index(dogru)
    cand=[s for s in SIR if s!=dogru]
    key=lambda s:(len(SETS[s]^C),abs(SIR.index(s)-p))
    bef=sorted([s for s in cand if SIR.index(s)<p],key=key)[:pos]; aft=sorted([s for s in cand if SIR.index(s)>p],key=key)[:4-pos]
    assert len(bef)==pos and len(aft)==4-pos,(dogru,pos)
    sec=bef+aft; yan=[]
    for s in sec:
        ex=sorted(SETS[s]-C,key=nm.index); ms=sorted(C-SETS[s],key=nm.index); parts=[]
        for n in ex:
            parts.append(f'{n}. yargıyı da yanlış sanmış; oysa {why[nm.index(n)]}.' if neg else f'{n}. yargıyı da doğru sanmış; oysa {why[nm.index(n)]}.')
        for n in ms:
            parts.append(f'{n}. yargının yanlış olduğunu görememiş; {why[nm.index(n)]}.' if neg else f'{n}. yargının doğru olduğunu görememiş; {why[nm.index(n)]}.')
        yan.append((s,' '.join(parts),'bilgi' if ex else 'dikkat'))
    sira=sorted(sec+[dogru],key=SIR.index); assert sira.index(dogru)==pos
    return dict(dogru=dogru,sira=sira,yan=yan)
def tek(opts,hedef,pos):
    """opts: [(metin,bool,olgu)] 5 adet; hedef: aranan doğruluk değeri; pos: doğru şıkkın sırası (harf)."""
    h=[o for o in opts if o[1]==hedef]; assert len(h)==1
    dg=h[0]; yn=[o for o in opts if o[1]!=hedef]
    sira=yn[:pos]+[dg]+yn[pos:]
    return dict(dogru=dg[0],sira=[x[0] for x in sira],yan=[(o[0],o[2],'bilgi') for o in yn])


# ---------- bilgi kutuları (örnekler soruların maddelerini/sayılarını kullanmaz)
KCB=B('Kc ifadesi','aA(g) + bB(g) ⇌ cC(g) + dD(g) için Kc = [C]ᶜ[D]ᵈ ÷ [A]ᵃ[B]ᵇ; ürünler paya, girenler paydaya yazılır, katsayılar üs olur. Saf katı ve sıvılar ifadede yer almaz. Örnek: 2X(g) + Y(k) ⇌ Z(g) için Kc = [Z] ÷ [X]²')
HZB=B('Hız–zaman grafiği','dengede ileri ve geri hız eşittir. Bir etki yapılınca yalnız birinin hızı ani (dikey) sıçrıyorsa derişimi değişen madde eklenmiş ya da çekilmiştir; iki hız birlikte sıçrıyorsa sıcaklık, hacim ya da basınç değişmiştir. Yeni dengede iki hız yine eşit olur. Örnek: iki hız eşit olduğu sürece derişimler zamanla değişmez')
LEB=B('Le Chatelier ilkesi','dengeye yapılan etki, sistem tarafından azaltılacak yönde yeni bir denge kurularak karşılanır. Derişim, basınç ve hacim etkisinde K değişmez; yalnız sıcaklık K’yı değiştirir. Örnek: ekzotermik dengede sıcaklık düşerse denge ısı veren yöne kayar')
ASB=B('Asal gaz ve hacim','sabit hacimde tepkimeye girmeyen gaz eklenirse derişimler değişmez, denge kaymaz. Sabit basınçta (serbest pistonlu kapta) asal gaz eklenirse hacim büyür, derişimler azalır ve denge gaz mol sayısı çok olan yöne kayar. Örnek: ΔnG = 0 olan dengede hacim değişimi dengeyi kaydırmaz')
QKB=B('Tepkime bölümü (Q)','Q, Kc ile aynı biçimde ama o andaki derişimlerle hesaplanır. Q < K ise ileri, Q > K ise geri yönde net tepkime olur; Q = K ise sistem dengededir. Örnek: K = 9 iken Q = 25 bulunursa ürün miktarı azalır')
ICEB=B('Denge hesabı','başlangıç, değişim ve denge satırlarıyla çalış; değişimler katsayılarla orantılıdır. Kc için mol sayılarını hacme bölerek derişimi kullan. Yeni denge kurulurken ilk dengeye eklenen ya da çekilen miktarı yeni başlangıç say; Q ile K’yı karşılaştırıp kayma yönünü belirle. Örnek: A + B ⇌ C için x mol A harcanırsa C’den x mol oluşur')
KATB=B('Katalizör','katalizör aktifleşme enerjisini azaltarak ileri ve geri hızı aynı oranda artırır; dengeye ulaşma süresini kısaltır. Örnek: katalizörlü deneyde sabit derişim düzeyine daha kısa sürede ulaşılır')
SKB=B('K ve sıcaklık','yalnız sıcaklık K’yı değiştirir. Sıcaklık artınca endotermik tepkimede K artar, ekzotermikte azalır. Örnek: bir denge için K değeri sıcaklıkla 5’ten 2’ye düşmüşse bu tepkime ekzotermiktir')
VRB=B('Verim–sıcaklık eğrileri','verim–sıcaklık grafiğinde aynı sıcaklıkta daha üstte kalan eğri ürünü daha çok veren koşuldur. Eğrilerin sıcaklıkla gidişi ısı türünü, konumları ise basınç ya da başka bir koşul farkını yansıtır. Örnek: verim %75 ise girenin %25’i kalmıştır')

# ================ kartlar
card(1,'Kc ifadesini yazma','Kc ifadesinde yalnız gaz ve çözünen türler yer alır; katsayılar üs olur ve ürünler paya yazılır.','Saf katıyı ifadeye katmak; ürün ile girenleri ters yazmak.','kolay','düz',3,'de-kc','Kc ifadesini doğru yazma')
card(2,'Hız–zaman grafiğiyle etkiyi bulma','Grafikte yalnız bir hızın ani sıçraması derişim değişimini, ikisinin birlikte sıçraması sıcaklık ya da hacim değişimini gösterir.','Ürün eklendiğinde de ileri hızın sıçradığını sanmak.','kolay','grafik',3,'de-dinamik','hız–zaman grafiğinden yapılan etkiyi bulma')
card(3,'Sıcaklık ve tanecik modeli','Aynı kaplarda sıcaklık yükselince ürün taneciği artıyorsa K büyümüş, tepkime endotermiktir.','Dengede hızların sıfır olduğunu düşünmek; K oranını tanecik sayısı oranı almak.','orta','şekilli',4,'de-le','tanecik modelinden K ve ΔH çıkarma')
card(4,'Asal gaz eklenmesi','Asal gaz sabit hacimde denge kaydırmaz; serbest pistonda hacmi büyüttüğü için denge gaz mol sayısı çok yöne kayar.','Asal gazın her durumda dengeyi kaydırmadığını sanmak.','orta','şekilli',4,'de-le','sabit hacim ve sabit basınçta asal gaz etkisi')
card(5,'Q ile K karşılaştırma','Kaplardaki karışımın bileşimi denge durumuyla ilişkilendirilerek net tepkime yönü bulunur.','Q ile K’yı ters kıyaslamak; derişimleri üssüz çarpmak.','orta','tablo',3,'de-qk','Q ve K ile yön belirleme')
card(6,'Dengede mol hesabı','Kc tanımından x çözülür; toplam mol hesaplanırken tüm türler toplanır.','Mol sayısını derişimle karıştırmak.','orta','tablo',4,'de-ice','Kc verilen dengede mol hesabı')
card(7,'Katalizörlü ve katalizörsüz deney','Katalizör yalnız hızı etkiler; grafikte ürün derişimleri aynı değere daha çabuk ya da yavaş ulaşır.','Katalizörün denge derişimini artırdığını sanmak.','orta','grafik',3,'de-grafik','katalizörün grafikteki izi')
card(8,'Sıcaklık değişiminin grafikteki etkisi','Derişimlerin sıçramadan kayması sıcaklık değişimini gösterir; iki dengeden iki Kc hesaplanıp karşılaştırılır.','Sıcaklık değişiminde de derişimlerin ani sıçradığını sanmak.','zor','grafik',5,'de-grafik','iki dengeden Kc oranı ve mol kesri')
card(9,'Ek maddeyle yeni denge','Eklenenler yeni başlangıç sayılır, Q ile K karşılaştırılıp kayma miktarı (x) denklemden çözülür.','Eklenenleri yok saymak; derişimi mole karıştırmak.','zor','tablo',6,'de-ice','ek madde sonrası yeni denge hesabı')
card(10,'Verim–sıcaklık eğrileri','Aynı sıcaklıkta eğrilerin konumu basıncı, sıcaklıkla gidişi ΔH işaretini verir; verimden kalan giren bulunur.','Verimi kalan girenle karıştırmak.','zor','grafik',5,'de-le','verim–sıcaklık eğrilerini yorumlama')

# ================ 01 · kolay · Kc ifadesi, olumsuz kök
o1=[('2SO₂(g) + O₂(g) ⇌ 2SO₃(g) tepkimesi için Kc = [SO₃]² ÷ ([SO₂]² × [O₂])',True,'Ürünler paya, girenler paydaya yazılmış ve katsayılar üs olmuş; ifade doğrudur ve yanlış değildir.'),
    ('CaCO₃(k) ⇌ CaO(k) + CO₂(g) tepkimesi için Kc = [CO₂]',True,'Saf katılar ifadeye yazılmaz, yalnız CO₂ kalır; ifade doğrudur ve yanlış değildir.'),
    ('2NO₂(g) ⇌ N₂O₄(g) tepkimesi için Kc = [N₂O₄] ÷ [NO₂]²',True,'N₂O₄ paya, NO₂ paydaya katsayısı üs olarak yazılmış; ifade doğrudur ve yanlış değildir.'),
    ('C(k) + H₂O(g) ⇌ CO(g) + H₂(g) tepkimesi için Kc = [CO] × [H₂] ÷ ([C] × [H₂O])',False,'Karbon saf katıdır, ifadeye yazılmaz; doğrusu Kc = [CO] × [H₂] ÷ [H₂O] olmalıdır.'),
    ('4NH₃(g) + 5O₂(g) ⇌ 4NO(g) + 6H₂O(g) tepkimesi için Kc = [NO]⁴ × [H₂O]⁶ ÷ ([NH₃]⁴ × [O₂]⁵)',True,'Tüm türler gazdır, ürünler paya, girenler paydaya katsayı üslü yazılmış; ifade doğrudur ve yanlış değildir.')]
r1=tek(o1,False,0)
q('0001',1,[A('Kuralı hatırla','Saf katı ve sıvılar Kc ifadesine yazılmaz; yalnız gazlar ve çözünenler yazılır.','Katılar ifadede yok'),
   A('Her ifadeyi sına','Ürün paya, giren paydaya, katsayılar üs olarak yazılmalıdır.','Beş ifadeyi kontrol et'),
   A('Hatalıyı bul','Karbon katısı [C] olarak paydaya yazılmış olan ifade yanlıştır.','C(k) + H₂O(g) ⇌ CO(g) + H₂(g) ifadesi yanlış')],
 tipId='de-kc',z='kolay',alt='Kc İfadesi',kaz='Heterojen ve homojen denge tepkimelerinin Kc ifadelerinin doğru yazılıp yazılmadığını belirler.',kalip='düz',
 metin='Sabit sıcaklıkta kapalı kaplarda gerçekleşen bazı denge tepkimeleri ve bu tepkimeler için yazılmış denge sabiti (Kc) ifadeleri aşağıda verilmiştir.\nBuna göre, aşağıdakilerden hangisinde verilen Kc ifadesi yanlıştır?',
 sekil=None,dogru=r1['dogru'],yan=r1['yan'],sira=r1['sira'],istenen='Kc ifadesi yanlış yazılmış tepkime.',
 ip=['Hangi türlerin Kc ifadesinde yer alabileceğini tepkimedeki hâllerine bakarak düşün.'],bilgi=[KCB],
 puf='Katı ve sıvı derişimi sabit kabul edilir; ifadede yalnız gaz ve çözünen türler kalır.')

# ================ 02 · kolay · hız–zaman, etki
o2=[('NH₃ gazı eklenmiştir.',True,'NH₃ ileri tepkimenin girenidir; eklenince yalnız ileri hız anında artar, bu grafikteki sıçramayla uyumludur.'),
    ('H₂ gazı eklenmiştir.',False,'H₂ ileri tepkimenin ürünüdür; eklenince anında artan hız ileri değil geri hızdır.'),
    ('N₂ gazı çekilmiştir.',False,'N₂ ürünlerden biridir; çekilince geri hız anında azalır, ileri hızda ani sıçrama olmaz.'),
    ('Katalizör eklenmiştir.',False,'Katalizör ileri ve geri hızı birlikte artırır ve denge derişimlerini değiştirmez; grafikte yalnız ileri hız sıçramıştır.'),
    ('Sıcaklık artırılmıştır.',False,'Sıcaklık artışında ileri ve geri hız birlikte (farklı oranlarda) anında artar; grafikte yalnız ileri hız sıçramıştır.')]
r2=tek(o2,True,1)
xm=10
gi=[(0,4),(3,4),(3,7)]+[(3+4*s/24,5.5+1.5*(1-s/24)**3) for s in range(1,25)]+[(xm,5.5)]
gg=[(0,4),(3,4)]+[(3+4*s/24,5.5-1.5*(1-s/24)**3) for s in range(1,25)]+[(xm,5.5)]
SK=pg('width=6.6cm,height=4.8cm,axis lines=left,xmin=0,xmax=10,ymin=0,ymax=9,xtick={3,7},xticklabels={$t_1$,$t_2$},ytick=\\empty,xlabel={Zaman},ylabel={Tepkime hızı},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(gi)}}};\n\\addplot[thick,dashed,color=red!70!black] coordinates {{{co(gg)}}};\n\\draw[gray,thin,dotted] (axis cs:3,0) -- (axis cs:3,9);\n\\draw[gray,thin,dotted] (axis cs:7,0) -- (axis cs:7,9);\n\\node[anchor=west,font=\\small] at (axis cs:3.3,7.2) {{ileri}};\n\\node[anchor=north,font=\\small] at (axis cs:5.2,4.5) {{geri}};')
q('0002',2,[A('Grafiği oku','t₁ anında yalnız ileri hız eğrisi dikey olarak sıçramıştır; geri hız o anda sabit kalmıştır.','Yalnız ileri hız sıçradı'),
   A('Etkiyi belirle','İleri tepkime 2NH₃ → N₂ + 3H₂ olduğundan ileri hız NH₃ derişimine bağlıdır; anında artış NH₃ derişiminin arttığını gösterir.','NH₃ eklenmiştir'),
   A('Diğer şıkları ele','Sıcaklık ve katalizör iki hızı birlikte, ürün eklenmesi ise geri hızı sıçratır.','Doğru: NH₃ gazı eklenmiştir')],
 tipId='de-dinamik',z='kolay',alt='Hız–Zaman Grafikleri',kaz='Hız–zaman grafiğinden sisteme yapılan etkiyi belirler.',kalip='grafik',
 metin='Sabit hacimli kapalı bir kapta\n2NH₃(g) ⇌ N₂(g) + 3H₂(g)\ndengesi kuruluyor. t₁ anında sistemde tek bir değişiklik yapılıyor ve sistem t₂ anında yeniden dengeye geliyor. İleri (2NH₃ → N₂ + 3H₂) ve geri yöndeki tepkimelerin hızlarının zamanla değişimi grafikte verilmiştir.\nBuna göre, t₁ anında yapılan değişiklik aşağıdakilerden hangisidir?',
 sekil=SK,dogru=r2['dogru'],yan=r2['yan'],sira=r2['sira'],istenen='t₁ anında yapılan etki.',
 ip=['t₁ anında hangi hızın değiştiğine ve hangisinin sabit kaldığına bak.'],bilgi=[HZB],
 puf='Önce hangi hızın değiştiğine bak; sonra o hızı hangi maddenin derişiminin belirlediğini düşün.')

# ================ 03 · orta · tanecik modeli, iki sıcaklık
x2a,xa=5,4; x2b,xb=3,8
assert 2*x2a+xa==2*x2b+xb==14
Vk=1  # iki kap eşit hacimli
K1=Fr(xa**2,x2a); K2=Fr(xb**2,x2b); assert K2>K1 and K2/K1==Fr(20,3) and K2/K1!=4
def kapX(ox,ttl,dim,mon):
    o=[f'\\draw[thick] ({ox:.2f},0) rectangle ({ox+3.2:.2f},2.5);',f'\\node[anchor=south,font=\\small] at ({ox+1.6:.2f},2.55) {{{ttl}}};']
    for (x,y) in dim:
        o.append(f'\\draw[fill=gray!35] ({ox+x:.2f},{y:.2f}) circle (.14); \\draw[fill=gray!35] ({ox+x+.28:.2f},{y:.2f}) circle (.14);')
    for (x,y) in mon: o.append(f'\\draw[fill=white] ({ox+x:.2f},{y:.2f}) circle (.14);')
    return o
dimA=[(0.35,0.4),(1.5,0.4),(2.4,0.7),(0.5,1.2),(1.7,1.0)]; monA=[(2.5,1.7),(0.7,2.0),(1.7,1.85),(1.1,1.55)]
dimB=[(0.4,0.5),(1.9,0.45),(1.2,1.5)]; monB=[(1.0,0.5),(2.8,0.5),(2.6,1.2),(0.5,1.2),(2.2,1.95),(0.7,2.05),(1.7,1.0),(1.6,2.1)]
assert len(dimA)==x2a and len(monA)==xa and len(dimB)==x2b and len(monB)==xb
o=kapX(0,'$T_1$',dimA,monA)+kapX(4.2,'$T_2$',dimB,monB)
o+=['\\draw[fill=gray!35] (1.0,-.45) circle (.14); \\draw[fill=gray!35] (1.28,-.45) circle (.14); \\node[anchor=west] at (1.55,-.45) {\\ce{X2}};','\\draw[fill=white] (3.6,-.45) circle (.14); \\node[anchor=west] at (3.85,-.45) {\\ce{X}};']
SK=tikz(o)
o3=[('Tepkime ekzotermiktir.',False,'T₂ > T₁ iken ürün (X) taneciği çoğaldığından tepkime endotermiktir; ekzotermik diyen bu tanecik sayılarını göz ardı etmiştir.'),
    ('T₂ sıcaklığındaki Kc değeri, T₁ sıcaklığındakinden büyüktür.',True,'Kc = [X]² ÷ [X₂] kaplarda 16 ÷ 5 ve 64 ÷ 3 ile orantılıdır (eşit hacimde); 64 ÷ 3 > 16 ÷ 5 olduğundan T₂’de K büyüktür.'),
    ('Her iki kapta da ileri ve geri tepkimeler durmuştur.',False,'Dengede tepkimeler durmaz; ileri ve geri hız eşittir ama sıfırdan farklıdır.'),
    ('T₂ sıcaklığındaki kapta toplam tanecik sayısı, T₁ sıcaklığındakinden azdır.',False,'T₁’de 5 + 4 = 9, T₂’de 3 + 8 = 11 tanecik vardır; T₂’deki sayı daha büyüktür.'),
    ('T₂ sıcaklığındaki Kc değeri, T₁ sıcaklığındakinin 4 katıdır.',False,'Kc oranı (64 ÷ 3) ÷ (16 ÷ 5) = 20 ÷ 3 bulunur, 4 değildir; 4 oranı tanecik sayılarından yanlış çıkarılmıştır.')]
r3=tek(o3,True,3)
q('0003',3,[A('Taneciklerin sayısını oku','T₁ kabında 5 X₂ ve 4 X; T₂ kabında 3 X₂ ve 8 X taneciği vardır.','T₁: 5 ve 4 · T₂: 3 ve 8'),
   A('Kc ifadesini yaz','Kc = [X]² ÷ [X₂]; kapların hacmi eşittir.','Kc ∝ n(X)² ÷ n(X₂)'),
   A('Kc değerlerini kıyasla','T₁ için 16 ÷ 5 = 3,2; T₂ için 64 ÷ 3 ≈ 21,3 (hacim çarpanı ortak).','K(T₂) > K(T₁)'),
   A('Şıkları ele','Sıcaklık artınca K arttığından tepkime endotermiktir; diğer şıklar çelişir.','Doğru: T₂’deki Kc daha büyüktür')],
 tipId='de-le',z='orta',alt='Sıcaklık ve Denge',kaz='Farklı sıcaklıklardaki denge karışımlarının tanecik modelinden K değerlerini kıyaslar ve tepkimenin ısı türünü belirler.',kalip='şekilli',
 metin='Aynı hacimli iki kapalı kabın birine T₁, diğerine T₂ sıcaklığında (T₂ > T₁) başlangıçta yalnız X₂ gazı konuluyor ve\nX₂(g) ⇌ 2X(g)\ntepkimesinin dengeye gelmesi sağlanıyor. Kaplardaki denge karışımlarının tanecik modeli şekilde verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK,dogru=r3['dogru'],yan=r3['yan'],sira=r3['sira'],istenen='Şekillere göre doğru olan ifade.',
 ip=['Her kaptaki X₂ ve X sayısından Kc ifadesine uygun bir oran kur ve iki sıcaklığı kıyasla.'],bilgi=[SKB],
 puf='Kc ifadesinde X’in üssünü unutma; iki kapta hacim eşit olduğundan mol sayılarıyla kıyas yapılabilir.')

# ================ 04 · orta · asal gaz, iki kap, öncüllü
def kapI():
    return ['\\draw[thick] (0,0) rectangle (2.8,2.4);','\\node[anchor=south,font=\\small] at (1.4,2.45) {Şekil I};',
            '\\node at (1.4,1.5) {\\ce{N2},\\ \\ce{H2},\\ \\ce{NH3}};','\\node[font=\\footnotesize] at (1.4,0.55) {sabit hacim};',
            f'\\draw[vurgu,very thick,{ARR}] (-1.3,1.2) -- (-.1,1.2); \\node[anchor=east] at (-1.35,1.2) {{\\ce{{He}}}};']
def kapII(ox=5.4):
    return [f'\\draw[thick] ({ox},0) -- ({ox},2.8) ({ox},0) -- ({ox+2.8},0) -- ({ox+2.8},2.8);',
            f'\\draw[thick,fill=gray!40] ({ox},1.9) rectangle ({ox+2.8},2.1);',f'\\draw[thick] ({ox+1.4},2.1) -- ({ox+1.4},2.7);',
            f'\\node[anchor=south,font=\\small] at ({ox+1.4},2.85) {{Şekil II}};',f'\\node at ({ox+1.4},1.15) {{\\ce{{N2}},\\ \\ce{{H2}},\\ \\ce{{NH3}}}};',
            f'\\node[font=\\footnotesize] at ({ox+1.4},0.45) {{serbest piston}};',
            f'\\draw[vurgu,very thick,{ARR}] ({ox-1.3},1.0) -- ({ox-.1},1.0); \\node[anchor=east] at ({ox-1.35},1.0) {{\\ce{{He}}}};']
SK=tikz(kapI()+kapII())
w4=onc([True,True,False],['sabit hacimde asal gaz derişimleri değiştirmez, bu nedenle Şekil I’de denge bozulmaz','serbest pistonlu kapta asal gaz hacmi büyütür, derişimler azalır ve denge gaz mol sayısı çok olan girenler yönüne kayar','sıcaklık sabit tutulduğundan iki kapta da Kc değeri değişmez'],1)
q('0004',4,[A('Şekil I’i değerlendir','Hacim sabittir; He derişimleri değiştirmez.','I: doğru (denge kaymaz)'),
   A('Şekil II’yi değerlendir','Dış basınç sabit, piston serbesttir; He eklenince hacim artar ve derişimler azalır. Gaz mol sayısı girenlerde 4, ürünlerde 2’dir.','II: doğru (girenler yönüne kayar)'),
   A('Kc’yi değerlendir','Sıcaklık sabit olduğundan Kc değişmez.','III: yanlış'),
   A('Sonuç','I ve II doğrudur.','I ve II')],
 tipId='de-le',z='orta',alt='Asal Gaz Etkisi',kaz='Sabit hacimli ve serbest pistonlu kaplarda asal gaz eklenmesinin denge ve denge sabiti üzerindeki etkisini yorumlar.',kalip='şekilli',
 metin='Aynı sıcaklıkta iki ayrı kapta\nN₂(g) + 3H₂(g) ⇌ 2NH₃(g)\ndengesi kurulmuştur. Şekil I’deki kap sabit hacimli, Şekil II’deki kap ise sürtünmesiz serbest pistonlu olup dış basınç sabittir. Her iki kaba sabit sıcaklıkta tepkimeye girmeyen He gazı ekleniyor ve sistemler yeniden dengeye geliyor.\nBuna göre,\nI. Şekil I’de denge kaymaz.\nII. Şekil II’de NH₃ miktarı azalır.\nIII. Şekil II’de Kc değeri küçülür.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w4['dogru'],yan=w4['yan'],sira=w4['sira'],istenen='Doğru olan yargılar.',
 ip=['Her kapta He eklenince gazların derişimlerinin değişip değişmediğini ayrı ayrı düşün.'],bilgi=[ASB],
 puf='Üç yargıyı tek tek, kabın türünü gözeterek sına.')

# ================ 05 · orta · Q–K tablo
Kc5=4
kaplar=[('I',Fr(1,2),Fr(1,2),Fr(1),Fr(1)),('II',Fr(1),Fr(1),Fr(1),Fr(1)),('III',Fr(1,4),Fr(1,2),Fr(1),Fr(1))]
def Q5(c,w,d,e): return d*e/(c*w)
yon=lambda Q:'dengede' if Q==Kc5 else ('ileri yönde' if Q<Kc5 else 'geri yönde')
tr5=[yon(Q5(*k[1:])) for k in kaplar]; assert tr5==['dengede','ileri yönde','geri yönde'] and [Q5(*k[1:]) for k in kaplar]==[4,1,8]
S5=lambda a:'I. '+a[0]+', II. '+a[1]+', III. '+a[2]
dog5=S5(tr5)
import itertools
perm=[p for p in itertools.permutations(['dengede','ileri yönde','geri yönde']) if list(p)!=tr5]
pick=[p for p in perm if sum(a!=b for a,b in zip(p,tr5))==2]+[p for p in perm if sum(a!=b for a,b in zip(p,tr5))==3]
pick=pick[:4]; assert len(pick)==4
cp=lambda a:{'dengede':'Q = K','ileri yönde':'Q < K','geri yönde':'Q > K'}[a]
qv=[Q5(*k[1:]) for k in kaplar]
yan5=[]
for p in pick:
    ms=[i for i in range(3) if p[i]!=tr5[i]]
    txt=' '.join(f'{["I","II","III"][i]} numaralı kapta Q = {fm(qv[i])} ve Kc = 4 olduğundan sonuç “{tr5[i]}” olur; “{p[i]}” sanmış.' for i in ms)
    yan5.append((S5(p),txt,'dikkat'))
sira5=[dog5]+[S5(p) for p in pick]
tab5=tablo_svg(['Kap','[CO]','[H₂O]','[CO₂]','[H₂]'],[[k[0]]+[fm(v) for v in k[1:]] for k in kaplar])
q('0005',5,[A('Q ifadesini yaz','Q = [CO₂][H₂] ÷ ([CO][H₂O]); değerler mol/L’dir.','Q = [CO₂] × [H₂] ÷ ([CO] × [H₂O])'),
   A('Q değerlerini hesapla','I: 1 ÷ 0,25 = 4 · II: 1 ÷ 1 = 1 · III: 1 ÷ 0,125 = 8.','Q(I) = 4 · Q(II) = 1 · Q(III) = 8'),
   A('K ile kıyasla','Kc = 4; Q = K dengede, Q < K ileri, Q > K geri yönde net tepkime verir.','I dengede · II ileri · III geri')],
 tipId='de-qk',z='orta',alt='Tepkime Bölümü',kaz='Farklı karışımların Q değerlerini Kc ile karşılaştırarak net tepkime yönünü belirler.',kalip='tablo',
 metin='Belirli bir sıcaklıkta\nCO(g) + H₂O(g) ⇌ CO₂(g) + H₂(g)    Kc = 4\ntepkimesi için özdeş üç kaba CO, H₂O, CO₂ ve H₂ gazları karıştırılıyor. Kaplardaki başlangıç derişimleri tabloda verilmiştir.\nBuna göre, bu sıcaklıkta I, II ve III numaralı kaplardaki net tepkimenin yönü aşağıdakilerden hangisinde doğru verilmiştir?',
 sekil=tab5,dogru=dog5,yan=yan5,sira=sira5,istenen='Kaplardaki net tepkime yönleri.',
 ip=['Her kaptaki derişimlerden ürünlerin çarpımının girenlerin çarpımına oranını yaz.'],bilgi=[QKB],
 puf='Kc ifadesine yalnız o anki derişimleri yaz.')

# ================ 06 · orta · Kc verilen dengede mol
V6=2; Kc6=2; x6=1
cP=Fr(x6,V6); cA=Fr(2-x6,V6); assert cP/(cA*cA)==Kc6
tot6=(2-x6)*2+x6; assert tot6==3
m6=(x6, Fr(tot6,V6), 2*2, 2*2+x6); assert m6==(1,Fr(3,2),4,5)
SK=tablo_svg(['Gaz','Başlangıç (mol)'],[['PCl₃(g)','2'],['Cl₂(g)','2'],['PCl₅(g)','0']])
q('0006',6,[A('Değişimi x al','PCl₃ ve Cl₂’den x mol harcanır, PCl₅’ten x mol oluşur.','PCl₃ = Cl₂ = 2 − x · PCl₅ = x'),
   A('Derişimlere çevir','Hacim 2 L olduğundan mol sayıları 2’ye bölünür.','[PCl₃] = [Cl₂] = (2 − x) ÷ 2 · [PCl₅] = x ÷ 2'),
   A('Kc’ye yaz','Kc = [PCl₅] ÷ ([PCl₃] × [Cl₂]) = 2 olacak şekilde x’i çöz.','2x ÷ (2 − x)² = 2 → x = 1 mol'),
   A('Toplam molü bul','PCl₃ = 1, Cl₂ = 1, PCl₅ = 1 mol.','Toplam = 3 mol')],
 tipId='de-ice',z='orta',alt='Denge Hesabı',kaz='Denge sabiti verilen tepkimede denge anındaki toplam mol sayısını hesaplar.',kalip='tablo',
 metin='2 L hacimli kapalı bir kaba, tabloda verilen miktarlarda PCl₃ ve Cl₂ gazları konuluyor ve sabit sıcaklıkta\nPCl₃(g) + Cl₂(g) ⇌ PCl₅(g)    Kc = 2\ntepkimesi dengeye ulaşıyor.\nBuna göre, denge anında kaptaki toplam gaz mol sayısı kaçtır?',
 sekil=SK,dogru=3,yan=[(m6[0],'Yalnız PCl₅’in mol sayısını (1) toplam gaz sanmış; kalan PCl₃ ve Cl₂ de kapta bulunmaktadır.','dikkat'),
  (m6[1],'Toplam gaz derişimini hesaplamış: 3 mol ÷ 2 L = 1,5 mol/L; soru mol sayısı istemektedir.','islem'),
  (m6[2],'Başlangıçtaki toplam mol sayısını (2 + 2 = 4) vermiş; mol sayısı tepkimeyle 1 azalır.','bilgi'),
  (m6[3],'Başlangıç toplamına (4) oluşan 1 mol PCl₅’i ekleyerek 5 bulmuş; girenlerin harcanmasını unutmuş.','islem')],
 istenen='Denge anındaki toplam gaz mol sayısı.',ip=['Harcanan mol sayısını x al ve Kc ifadesini derişimlerle yaz.'],bilgi=[ICEB],
 puf='Önce x’i Kc denkleminden bul, sonra tüm türlerin molünü topla.')

# ================ 07 · orta · katalizör grafiği
def curve(t1,top,xmax,n=24):
    pts=[(t1*s/n,top*(1-(1-s/n)**3)) for s in range(n+1)]; pts.append((xmax,top)); return pts
cI=curve(8,1,10); cII=curve(4,1,10)
SK=pg('width=6.4cm,height=5cm,axis lines=left,xmin=0,xmax=10,ymin=0,ymax=1.4,xtick=\\empty,ytick distance=0.2,yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman},ylabel={$[\\mathrm{B}]$ (mol/L)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(cI)}}};\n\\addplot[thick,dashed,color=red!70!black] coordinates {{{co(cII)}}};\n\\node[anchor=west,font=\\small] at (axis cs:4.6,0.52) {{Deney I}};\n\\node[anchor=south west,font=\\small] at (axis cs:4.4,1.04) {{Deney II}};')
A0=Fr(3,2); Bq=Fr(1); Aq=A0-Bq/2; Kk=Bq**2/Aq; assert (Aq,Kk)==(1,1)
o7=[('Her iki deneyde de Kc değeri 1’dir.',True,'Dengede [B] = 1, [A] = 1,5 − 0,5 = 1 mol/L olduğundan Kc = 1² ÷ 1 = 1 bulunur ve iki deneyde de aynıdır.'),
    ('Deney I’de katalizör kullanılmıştır.',False,'Katalizör dengeye ulaşma süresini kısaltır; dengeye daha çabuk ulaşan Deney II’dir, Deney I’i seçen bunu ters yorumlamıştır.'),
    ('Deney II’de dengedeki B derişimi Deney I’dekinden büyüktür.',False,'İki eğri de aynı 1,0 mol/L düzeyine yaklaşır; katalizör denge derişimini değiştirmez.'),
    ('Deney II’de Kc değeri Deney I’dekinden büyüktür.',False,'Kc yalnız sıcaklığa bağlıdır ve katalizör değiştirmez; iki deneyde de aynıdır.'),
    ('Deney II’de dengedeki A derişimi 0,5 mol/L’dir.',False,'A derişimi 1,5 − 0,5 = 1 mol/L olur; 0,5 değeri, A’nın B’ye göre 2 kat azaldığını sanmaktan çıkar.')]
r7=tek(o7,True,2)
q('0007',7,[A('Grafiği oku','İki eğri de dengede [B] = 1,0 mol/L düzeyine ulaşıyor; Deney II daha önce ulaşıyor.','[B] denge = 1 mol/L'),
   A('A’nın derişimini bul','A ⇌ 2B’de B 1 mol/L oluştuysa A 0,5 mol/L harcanır.','[A] = 1,5 − 0,5 = 1 mol/L'),
   A('Kc’yi hesapla','Kc = [B]² ÷ [A].','Kc = 1² ÷ 1 = 1'),
   A('Sonuç','Katalizör Kc’yi değiştirmediğinden iki deneyde de Kc = 1’dir.','Doğru: Kc = 1')],
 tipId='de-grafik',z='orta',alt='Katalizör',kaz='Katalizörlü ve katalizörsüz deneylerin derişim–zaman grafiğini yorumlar ve grafikten Kc hesaplar.',kalip='grafik',
 metin='Aynı sıcaklıkta, 1 L’lik özdeş iki kaba başlangıçta yalnız 1,5 mol A gazı konuluyor ve\nA(g) ⇌ 2B(g)\ntepkimesi gerçekleştiriliyor. İki deneyin tek farkı, birinde katalizör kullanılmasıdır. B gazının derişiminin zamanla değişimi grafikte verilmiştir.\nBuna göre aşağıdakilerden hangisi doğrudur?',
 sekil=SK,dogru=r7['dogru'],yan=r7['yan'],sira=r7['sira'],istenen='Grafiğe göre doğru olan ifade.',
 ip=['Eğrilerin ulaştığı düzeyden denge derişimlerini ve Kc’yi hesapla.'],bilgi=[KATB],
 puf='Önce eğrilerin yaklaştığı düzeylerden denge derişimlerini oku, sonra Kc’yi hesapla.')

# ================ 08 · zor · sıcaklık, X ⇌ 2Y, öncüllü
X1,Y1,X3,Y3=Fr(1),Fr(2),Fr(1,2),Fr(3)
assert X1+Y1/2==2==X3+Y3/2
Ka=Y1**2/X1; Kb=Y3**2/X3; assert (Ka,Kb,Kb/Ka)==(4,18,Fr(9,2))
yk1=Y1/(X1+Y1); yk3=Y3/(X3+Y3); assert yk3>yk1
def seg(a,b,t0,t1,n=24): return [(t0+(t1-t0)*s/n,b+(a-b)*(1-s/n)**3) for s in range(n+1)]
xc=seg(2,1,0,4)+[(7,1)]+seg(1,0.5,7,11)+[(13,0.5)]
yc=seg(0,2,0,4)+[(7,2)]+seg(2,3,7,11)+[(13,3)]
SK=pg('width=7.2cm,height=5.4cm,axis lines=left,xmin=0,xmax=13,ymin=0,ymax=3.5,xtick={4,7,11},xticklabels={$t_1$,$t_2$,$t_3$},ytick distance=0.5,yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman},ylabel={Derişim (mol/L)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black] coordinates {{{co(xc)}}};\n\\addplot[thick,dashed,color=red!70!black] coordinates {{{co(yc)}}};\n\\node[anchor=south,font=\\small] at (axis cs:12,0.55) {{X}};\n\\node[anchor=south,font=\\small] at (axis cs:12,3.05) {{Y}};')
w8=onc([False,True,True],['sıcaklık artınca Kc büyüdüğü ve ürün (Y) miktarı arttığı için tepkime ekzotermik değil endotermiktir','t₁ anında Kc = 2² ÷ 1 = 4, t₃ anında Kc = 3² ÷ 0,5 = 18 olduğundan Kc(t₃) = 4,5 × Kc(t₁) olur','Y’nin mol kesri t₁ anında 2 ÷ 3 ≈ 0,67, t₃ anında 3 ÷ 3,5 ≈ 0,86 olduğundan t₃’te daha büyüktür'],3)
w8['yan']=w8['yan']
q('0008',8,[A('Dengeleri oku','t₁: [X] = 1, [Y] = 2 · t₃: [X] = 0,5, [Y] = 3 mol/L.','İki denge değeri'),
   A('Kc değerlerini bul','Kc = [Y]² ÷ [X].','Kc(t₁) = 4 · Kc(t₃) = 18'),
   A('Isı türünü belirle','Sıcaklık artınca Kc büyümüştür; tepkime endotermiktir.','I: yanlış'),
   A('Oran ve mol kesri','18 ÷ 4 = 4,5; mol kesri 2 ÷ 3 ve 3 ÷ 3,5 → ikincisi büyük.','II: doğru · III: doğru'),
   A('Sonuç','II ve III doğrudur.','II ve III')],
 tipId='de-grafik',z='zor',alt='Sıcaklık Değişimi',kaz='Sıcaklık değişiminin derişim–zaman grafiğindeki etkisini yorumlayarak iki dengedeki Kc değerlerini ve ürün oranını karşılaştırır.',kalip='grafik',
 metin='Sabit hacimli kapalı bir kaba yalnız X gazı konuluyor ve\nX(g) ⇌ 2Y(g)\ntepkimesi t₁ anında dengeye ulaşıyor. t₂ anında sistemin sıcaklığı artırılıyor ve sistem t₃ anında yeni dengeye geliyor. Gazların derişimlerinin zamanla değişimi grafikte verilmiştir.\nBuna göre,\nI. Tepkime ekzotermiktir.\nII. t₃ anındaki Kc değeri, t₁ anındakinin 4,5 katıdır.\nIII. Y’nin mol kesri t₃ anında t₁ anındakinden büyüktür.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w8['dogru'],yan=w8['yan'],sira=w8['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['İki dengeden Kc değerlerini ayrı ayrı hesaplamadan hiçbir yargıyı karara bağlama.'],bilgi=[SKB,KCB],
 puf='Sıcaklık değişiminde Kc değişir; her denge için derişimleri ifadeye yeniden yaz.')

# ================ 09 · zor · ek maddeyle yeni denge (H2 + I2 <-> 2HI)
V9=2
e=dict(H2=1,I2=4,HI=6); Kc9=Fr(e['HI']**2,e['H2']*e['I2']); assert Kc9==9
add=dict(H2=3,I2=0,HI=1)
ini={k:Fr(e[k]+add[k],V9) for k in e}; assert ini=={'H2':2,'I2':2,'HI':Fr(7,2)}
Qn=ini['HI']**2/(ini['H2']*ini['I2']); assert Qn==Fr(49,16)<Kc9
x9=Fr(1,2); assert (ini['HI']+2*x9)**2==Kc9*(ini['H2']-x9)*(ini['I2']-x9) and (ini['HI']+2*x9)==3*(2-x9)
mol9=(ini['HI']+2*x9)*V9; assert mol9==9
m9=(Fr(9,2), Fr(7), Fr(8), Fr(5)); assert m9==(ini['HI']+2*x9, ini['HI']*V9, ini['HI']*V9+2*x9, (ini['HI']-2*x9)*V9)
SK=tablo_svg(['Gaz','Dengedeki mol','Eklenen mol'],[['H₂(g)','1','3'],['I₂(g)','4','0'],['HI(g)','6','1']])
q('0009',9,[A('Kc’yi bul','Dengedeki mol/L değerleri: H₂ = 0,5, I₂ = 2, HI = 3; Kc = [HI]² ÷ ([H₂] × [I₂]).','Kc = 9 ÷ (0,5 × 2) = 9'),
   A('Yeni başlangıcı yaz','Eklenenlerle birlikte mol/L: H₂ = 2, I₂ = 2, HI = 3,5.','Q = 3,5² ÷ (2 × 2) ≈ 3,06 < 9'),
   A('Kayma yönü','Q < Kc olduğundan ileri yönde x mol/L ilerler.','(3,5 + 2x)² = 9 (2 − x)²'),
   A('x’i çöz','Her iki tarafın kökü alınır: 3,5 + 2x = 3(2 − x).','x = 0,5 mol/L'),
   A('Mole çevir','[HI] = 3,5 + 1 = 4,5 mol/L; hacim 2 L.','n(HI) = 4,5 × 2 = 9 mol')],
 tipId='de-ice',z='zor',alt='Yeni Denge Hesabı',kaz='Dengedeki sisteme eklenen maddeler sonrası Q ile Kc’yi karşılaştırıp yeni denge mol sayısını hesaplar.',kalip='tablo',
 metin='2 L hacimli kapalı bir kapta\nH₂(g) + I₂(g) ⇌ 2HI(g)\ntepkimesi sabit sıcaklıkta dengededir. Dengedeki gazların mol sayıları ile bu dengedeki kaba sabit sıcaklıkta eklenen gaz miktarları tabloda verilmiştir.\nEkleme yapıldıktan sonra sistem yeniden dengeye geldiğine göre, yeni dengede HI gazının mol sayısı kaçtır?',
 sekil=SK,dogru=9,yan=[(m9[0],'Sonucu mol/L olarak bırakmış: [HI] = 4,5 mol/L; hacim olan 2 L ile çarpmayı unutmuştur.','dikkat'),
  (m9[3],'İlerlemeyi ters yönde almış: 7 − 2 = 5 bulmuştur.','islem'),
  (m9[1],'Eklemeden sonraki karışımı denge sanmış; HI mol sayısı 6 + 1 = 7 kalmıştır, oysa Q < Kc olduğundan tepkime ileri yönde sürer.','bilgi'),
  (m9[2],'İlerleme miktarını (0,5 mol/L) mol sayısı sanmış: 7 + 2 · 0,5 = 8 bulmuştur.','islem')],
 istenen='Yeni dengede HI gazının mol sayısı.',ip=['Eklemeden sonraki karışımın hangi yöne ilerleyeceğini düşün.'],bilgi=[ICEB,QKB],
 puf='Eklenenlerle birlikte yeni başlangıç derişimlerini kur; x’i derişim cinsinden çöz.')

# ================ 10 · zor · verim–sıcaklık, öncüllü
Tx=[400,500,600,700,800]; Pa=[97,80,60,42,28]; Pb=[90,50,32,20,12]
assert all(a>b for a,b in zip(Pa,Pb)) and Pa==sorted(Pa,reverse=True) and Pb==sorted(Pb,reverse=True)
assert 3-Fr(Pa[1],100)==Fr(11,5) and 3-Fr(Pb[1],100)==Fr(5,2) and Fr(5,2)-Fr(11,5)==Fr(3,10)
pa=[(t,v) for t,v in zip(Tx,Pa)]; pb=[(t,v) for t,v in zip(Tx,Pb)]
SK=pg('width=7cm,height=5.4cm,axis lines=left,xmin=400,xmax=800,ymin=0,ymax=100,xtick={400,500,600,700,800},xticklabels={400,$T_1$,600,700,800},ytick distance=10,grid=major,major grid style={gray!45,thin},xlabel={Sıcaklık (K)},ylabel={Verim (\\%)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,color=blue!70!black,smooth] coordinates {{{co(pa)}}};\n\\addplot[thick,dashed,color=red!70!black,smooth] coordinates {{{co(pb)}}};\n\\node[anchor=south west,font=\\small] at (axis cs:640,62) {{$P_1$}};\n\\node[anchor=south west,font=\\small] at (axis cs:640,34) {{$P_2$}};')
w10=onc([True,True,True],['verim sıcaklıkla azaldığından denge sıcaklık artınca girenler yönüne kayar; bu ileri tepkimenin ekzotermik olduğunu gösterir','gaz mol sayısı azalan bu tepkimede basınç artınca verim artar; aynı sıcaklıkta P₁ eğrisi üstte olduğundan P₁ > P₂ dir','T₁ sıcaklığında verim P₁ için %80, P₂ için %50 olduğundan toplam gaz mol sayısı P₁ için 3 − 0,8 = 2,2 mol, P₂ için 3 − 0,5 = 2,5 mol bulunur; fark 0,3 moldür'],4)
q('0010',10,[A('Isı türünü belirle','Eğriler sıcaklıkla aşağı iner: verim sıcaklıkla azalır, tepkime ekzotermiktir.','I: doğru'),
   A('Basıncı kıyasla','Girenlerde 3, ürünlerde 2 mol gaz var; basınç artınca verim artar. P₁ eğrisi üstte olduğundan P₁ > P₂.','II: doğru'),
   A('Toplam molü bul','T₁’de verim P₁ için %80, P₂ için %50; Başlangıçta 2 mol SO₂ ve 1 mol O₂ vardır; tepkime tam yürürse toplam mol 3’ten 2’ye iner, yani her 1 mol verim için toplam 1 mol azalır.','P₁: 3 − 0,8 = 2,2 mol · P₂: 3 − 0,5 = 2,5 mol → fark 0,3'),
   A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],
 tipId='de-le',z='zor',alt='Verim–Sıcaklık Grafiği',kaz='Verim–sıcaklık eğrilerinden tepkimenin ısı türünü, basınçların büyüklüğünü ve kalan giren miktarlarını yorumlar.',kalip='grafik',
 metin='Her denemede 2 mol SO₂ ve 1 mol O₂ ile başlanarak\n2SO₂(g) + O₂(g) ⇌ 2SO₃(g)\ntepkimesi, P₁ ve P₂ basınçlarında ve farklı sıcaklıklarda dengeye getiriliyor. Her denemede SO₂’nin SO₃’e dönüşen yüzdesi (verim) grafikte verilmiştir.\nBuna göre,\nI. Tepkime ekzotermiktir.\nII. P₁ basıncı P₂ basıncından büyüktür.\nIII. T₁ sıcaklığında P₂ basıncındaki dengede toplam gaz mol sayısı, P₁ basıncındakinden 0,3 mol fazladır.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w10['dogru'],yan=w10['yan'],sira=w10['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['Her yargıyı grafikteki eğrilerin konumu ve T₁’deki değerlerle ayrı ayrı sına.'],bilgi=[VRB,SKB],
 puf='Eğrilerin konumuna ve sıcaklıkla gidişine bakarak her yargıyı ayrı sına.')

# ================ yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/dengeiki'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'dengeiki-1.json'),os.path.join(SC,'bos-dengeiki.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|Kimyasal Tepkimelerde Denge'))['kartlar'].append(c['id'])
json.dump(dict(konu='Kimyasal Tepkimelerde Denge',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2020–2026 Kimya (yalnız mantık), MEB 12. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akdengeiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
