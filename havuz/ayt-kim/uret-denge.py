"""AYT Kimya · Kimyasal Tepkimelerde Denge · 20 soru (kardeş yok, ipucu 1). Şekil değerleri Python'da hesaplanır; her cevap ve çeldirici assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-kim')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif_kim2 as H
from _hafif_kim2 import *
from cizim import tikz_svg
from math import sqrt,exp
H.KONU='Kimyasal Tepkimelerde Denge'
P=Parti('denge','Kimyasal Tepkimelerde Denge','akim|Kimyasal Tepkimelerde Denge',ders='AYT Kimya',idon='aytkim')
KY='ÖSYM AYT 2020–2026 Kimya (Kimyasal Denge, Dengeyi Etkileyen Faktörler; yalnız mantık) · MEB 12. sınıf kimya'
TIPLER={'de-dinamik':'Dinamik denge ve hız–zaman grafiği','de-kc':'Kc ifadesi ve hesabı','de-kp':'Kp, kısmi basınç ve Kp–Kc ilişkisi','de-ice':'Denge hesabı (başlangıç–değişim–denge)',
 'de-le':'Le Chatelier ilkesi','de-grafik':'Derişim–zaman grafikleri','de-qk':'Tepkime bölümü (Q) ve denge sabiti','de-kb':'Denge sabitlerinin birleştirilmesi','de-enerji':'Enerji diyagramı ve denge'}
CARD={}
def card(no,alt,fikir,tuzak,z,kalip,adim,tipId,ozet):
    kart(f'K-AKDE-{no:02d}',alt,fikir,tuzak,z,kalip,adim,tipId,TIPLER[tipId],KY); CARD[no]=ozet
def q(no,cn,ad,**k):
    mk(P,no,ad=ad,adim=len(ad),kart=f'K-AKDE-{cn:02d} ('+CARD[cn]+')',tip=TIPLER[k['tipId']],**k)
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
DD=B('Dinamik denge','kapalı kapta ileri ve geri tepkimelerin hızları eşitlenince denge kurulur; tepkimeler durmaz, madde derişimleri sabit kalır. Örnek: CO(g) + H₂O(g) ⇌ CO₂(g) + H₂(g) dengesinde dört gazın da derişimi sabittir, ama her iki yönde tepkime sürer')
KCB=B('Denge sabiti (Kc)','aA + bB ⇌ cC + dD için Kc = [C]ᶜ[D]ᵈ ÷ [A]ᵃ[B]ᵇ; derişimler denge anındaki mol/L değerleridir. Saf katı ve sıvılar ifadeye yazılmaz. Örnek: 2A(g) + B(g) ⇌ C(g) için Kc = [C] ÷ ([A]² × [B])')
KPB=B('Kısmi basınç ve Kp','gaz karışımında i gazının kısmi basıncı Pᵢ = (mol kesri) × P_toplam; Kp ifadesi Kc gibi yazılır, ama derişim yerine kısmi basınç kullanılır. Örnek: A(g) ⇌ 2B(g) için Kp = P_B² ÷ P_A')
KPKC=B('Kp ile Kc ilişkisi','Kp = Kc × (R·T)^Δn; Δn = gaz hâlindeki ürünlerin katsayıları toplamı − gaz hâlindeki girenlerin katsayıları toplamı. Δn = 0 ise Kp = Kc olur. Örnek: A(g) + B(g) ⇌ 3C(g) için Δn = +1')
LCB=B('Le Chatelier ilkesi','dengedeki sisteme dışarıdan etki edilirse sistem etkiyi azaltacak yönde yeni bir dengeye gelir. Gaz derişimi artarsa o gazı harcayan yöne, hacim küçülürse gaz mol sayısı az olan yöne, sıcaklık artarsa endotermik yöne kayar. Katalizör dengeyi kaydırmaz, yalnız dengeye ulaşma süresini kısaltır')
KTB=B('K ve sıcaklık','denge sabiti yalnız sıcaklığa bağlıdır. Endotermik tepkimede sıcaklık artınca K artar, ekzotermik tepkimede K azalır. Derişim, basınç, hacim ve katalizör K değerini değiştirmez. Örnek: ΔH < 0 olan bir tepkime ısıtılınca ürün miktarı azalır')
DTB=B('Derişim–zaman grafiği','derişimlerin değişmediği yatay bölgeler denge bölgesidir. Anında (dikey) sıçrama bir maddenin eklendiğini ya da çıkarıldığını gösterir; sıçramadan sonra eğrilerin eğimi yeni dengeye giden yönü verir. Değişim miktarlarının oranı katsayıların oranıdır. Örnek: ΔA = 0,2 ve ΔB = 0,4 ise katsayılar 1 : 2 dir')
QKB=B('Tepkime bölümü (Q)','Q, Kc ile aynı biçimde ama herhangi bir andaki derişimlerle yazılır. Q < K ise tepkime ileri yönde, Q > K ise geri yönde ilerler; Q = K ise sistem dengededir. Örnek: K = 10 iken Q = 3 bulunursa ürün oluşumu sürer')
KBB=B('K değerlerinin birleştirilmesi','tepkime tersine çevrilirse K → 1/K; katsayılar n ile çarpılırsa K → Kⁿ; tepkimeler toplanırsa K değerleri çarpılır. Örnek: K₁ ve K₂ değerli iki tepkimenin toplamının denge sabiti K₁ × K₂ dir')
ICEB=B('Denge hesabı','tepkime başlangıç, değişim ve denge satırlarıyla tablolanır; değişim miktarları katsayılarla orantılıdır. Kc yazılırken derişimler (mol ÷ hacim) kullanılır. Örnek: A(g) ⇌ 2B(g) tepkimesinde A’dan x mol harcanırsa B’den 2x mol oluşur')
HETB=B('Heterojen denge','saf katı ve sıvıların derişimi sabit sayılır, K ifadesine yazılmaz; yalnız gazlar (ve çözünenler) yazılır. Örnek: C(k) + O₂(g) ⇌ CO₂(g) için Kp = P_CO₂ ÷ P_O₂. Katı miktarı yeter durumda ise değişince denge kaymaz')
EDB=B('Enerji diyagramı','ileri tepkimenin aktifleşme enerjisi Ea(ileri) = geçiş hâli − girenler; Ea(geri) = geçiş hâli − ürünler; ΔH = Ea(ileri) − Ea(geri). Katalizör iki aktifleşme enerjisini de aynı miktarda azaltır, ΔH ve K değişmez')

# ================ 01 · kolay · hız–zaman grafiği, dinamik denge
card(1,'Dinamik denge ve hız grafiği','Hız–zaman grafiğinde eğrilerin birleştiği an dengedir; sonrasında ileri ve geri hız eşit ve sıfırdan farklıdır, derişimler sabittir.','Dengede tepkimenin durduğunu sanmak; denge sonrası ürün derişiminin artmaya devam ettiğini düşünmek.','kolay','grafik',3,'de-dinamik','hız–zaman grafiğinden dengeyi yorumlama')
t1_,xm_=5,8
gh=ease(8,4,0,t1_,xm_); gg=ease(0,4,0,t1_,xm_)
SK=pg('width=6.4cm,height=4.6cm,axis lines=left,xmin=0,xmax=8,ymin=0,ymax=10,xtick={5},xticklabels={$t_1$},ytick=\\empty,xlabel={Zaman},ylabel={Tepkime hızı},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,smooth] coordinates {{{co(gh)}}};\n\\addplot[thick,dashed,smooth] coordinates {{{co(gg)}}};\n\\draw[gray,thin,dotted] (axis cs:5,0) -- (axis cs:5,10);\n\\node[anchor=west] at (axis cs:1.5,7.4) {{ileri}};\n\\node[anchor=west] at (axis cs:1.5,1.6) {{geri}};')
w1=onc([True,False,False],['0–t₁ aralığında ileri tepkime hızı geri tepkime hızından büyüktür, bu yüzden net olarak HI oluşur','dinamik dengede ileri ve geri tepkimeler sürer; hızları sıfır değil birbirine eşittir','t₁ anında denge kurulmuştur ve bu andan sonra HI derişimi sabit kalır'],0)
q('0001',1,[A('Grafiği oku','0–t₁ aralığında ileri hız eğrisi geri hız eğrisinin üstündedir; ürün birikir.','I: doğru'),
   A('Dengeden sonrasına bak','t₁ anında eğriler birleşir ve sonra eşit, sıfırdan farklı bir değerde kalır.','II: yanlış (tepkimeler durmaz)'),
   A('Derişimleri yorumla','İleri ve geri hız eşit olduğu için net değişim olmaz; HI derişimi sabittir.','III: yanlış'),
   A('Sonuç','Yalnız I yargısı doğrudur.','Yalnız I')],
 tipId='de-dinamik',z='kolay',alt='Dinamik Denge',kaz='Hız–zaman grafiğinden dengenin kurulduğu anı belirler; dengede ileri ve geri hızları ve derişimlerin davranışını yorumlar.',kalip='grafik',
 metin='Sabit sıcaklıkta, sabit hacimli kapalı bir kaba yalnız H₂ ve I₂ gazları konuluyor ve\nH₂(g) + I₂(g) ⇌ 2HI(g)\ntepkimesinin dengeye gelmesi sağlanıyor. Tepkimenin ileri ve geri yöndeki hızlarının zamanla değişimi grafikte gösterilmiştir.\nBuna göre,\nI. 0–t₁ aralığında net olarak HI oluşmaktadır.\nII. t₁ anından sonra ileri ve geri yöndeki tepkimeler durmuştur.\nIII. t₁ anından sonra HI derişimi artmaya devam eder.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w1['dogru'],yan=w1['yan'],sira=w1['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['Eğrilerin birleştiği andan önce ve sonra ileri ile geri hızın birbirine göre durumunu karşılaştır.'],bilgi=[DD],
 puf='Denge “tepkimenin bittiği” an değil, iki yöndeki hızların eşitlendiği andır.')

# ================ 02 · kolay · tablo → Kc
card(2,'Derişim tablosundan Kc','Kc ifadesi katsayıları üs yaparak yazılır; denge derişimleri yerine konur.','Katsayıları üs yapmamak; ürün ve girenleri ters yazmak.','kolay','tablo',3,'de-kc','denge derişimlerinden Kc hesabı')
n2,h2,nh3=Fr(1,2),Fr(1,10),Fr(1,10)
Kc2=nh3**2/(n2*h2**3); assert Kc2==20
m2a=nh3/(n2*h2); m2b=1/Kc2; m2c=nh3**2/(n2*h2); m2d=nh3/(n2*h2**3)
assert (m2a,m2b,m2c,m2d)==(2,Fr(1,20),Fr(1,5),200)
SK=tablo_svg(['Gaz','Derişim (mol/L)'],[['N₂(g)','0,5'],['H₂(g)','0,1'],['NH₃(g)','0,1']])
q('0002',2,[A('Kc ifadesini yaz','Katsayılar üs olur; ürün payda değil paya yazılır.','Kc = [NH₃]² ÷ ([N₂] × [H₂]³)'),
   A('Değerleri yerleştir','Tablodaki derişimleri ifadede yerine koy.','Kc = (0,1)² ÷ (0,5 × (0,1)³)'),
   A('Hesapla','Payı ve paydayı ayrı ayrı bul.','Pay = 0,01 · Payda = 0,5 × 0,001 = 0,0005'),
   A('Sonuç','Oranı bul.','Kc = 0,01 ÷ 0,0005 = 20')],
 tipId='de-kc',z='kolay',alt='Denge Sabiti',kaz='Denge derişimlerinden Kc değerini hesaplar.',kalip='tablo',
 metin='Sabit sıcaklıkta kapalı bir kapta\nN₂(g) + 3H₂(g) ⇌ 2NH₃(g)\ntepkimesi dengeye ulaştığında gazların derişimleri tabloda verilmiştir.\nBuna göre, tepkimenin bu sıcaklıktaki denge sabiti (Kc) kaçtır?',
 sekil=SK,dogru=20,yan=[(m2a,'Derişimleri katsayılarla üs yapmadan yazmış: 0,1 ÷ (0,5 × 0,1) = 2.','bilgi'),
  (m2b,'Kc ifadesini ürün ve girenleri ters yazarak kurmuş; sonuç 1 ÷ 20 = 0,05 olmuş.','bilgi'),
  (m2c,'H₂ derişiminin üssünü 3 yerine 1 almış: 0,1² ÷ (0,5 × 0,1) = 0,2.','dikkat'),
  (m2d,'NH₃ derişiminin üssünü 2 yerine 1 almış: 0,1 ÷ (0,5 × 0,1³) = 200.','dikkat')],
 istenen='Tepkimenin denge sabiti Kc.',ip=['Kc ifadesini yazarken her derişimin üssünün tepkime denklemindeki hangi sayıya bağlı olduğuna dikkat et.'],bilgi=[KCB],
 puf='Önce denge sabiti ifadesini yaz, sonra sayıları yerleştir; üslerin katsayıdan geldiğini unutma.')

# ================ 03 · kolay · derişim–zaman, öncüllü
card(9,'Derişim–zaman grafikleri','Yatay bölge dengedir; değişim miktarlarının oranı katsayıları verir; dengede iki yöndeki hız eşittir.','Dengede derişimlerin eşit olduğunu sanmak; değişimleri katsayıdan bağımsız okumak.','orta','grafik',3,'de-grafik','derişim–zaman grafiğini okuma')
c3=ease(Fr(1,2),Fr(1,5),0,5,8); d3=ease(0,Fr(3,5),0,5,8)
c3=[(x,float(y)) for x,y in c3]; d3=[(x,float(y)) for x,y in d3]
SK=pg('width=6.4cm,height=5cm,axis lines=left,xmin=0,xmax=8,ymin=0,ymax=0.7,xtick={5},xticklabels={$t_1$},ytick distance=0.1,yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman},ylabel={Derişim (mol/L)},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick,smooth] coordinates {{{co(c3)}}};\n\\addplot[thick,dashed,smooth] coordinates {{{co(d3)}}};\n\\node[anchor=south] at (axis cs:6.8,0.2) {{$\\mathrm{{N_2O_4}}$}};\n\\node[anchor=south] at (axis cs:6.8,0.6) {{$\\mathrm{{NO_2}}$}};')
w3=onc([True,False,True],['grafikte t₁ anından sonra derişimler değişmez; bu, dengenin kurulduğunu gösterir','t₁ anından sonra N₂O₄ derişimi 0,2 mol/L, NO₂ derişimi 0,6 mol/L olduğundan derişimler eşit değildir','NO₂ derişimi 0,6 mol/L artarken N₂O₄ derişimi 0,3 mol/L azalır; bu, katsayıların 2 : 1 oranıyla uyumludur'],2)
q('0003',9,[A('Dengeyi belirle','t₁ anından sonra derişimler sabit kalıyor.','I: doğru'),
   A('Derişimleri karşılaştır','Denge anında N₂O₄ ≈ 0,2 mol/L, NO₂ ≈ 0,6 mol/L okunur; eşit değillerdir.','II: yanlış'),
   A('Değişimleri bul','N₂O₄: 0,5 → 0,2 azalma 0,3; NO₂: 0 → 0,6 artış 0,6.','0,6 = 2 × 0,3 → III: doğru'),
   A('Sonuç','I ve III doğrudur.','I ve III')],
 tipId='de-grafik',z='kolay',alt='Derişim–Zaman Grafikleri',kaz='Derişim–zaman grafiğinden dengenin kurulduğu anı, derişimlerin eşit olup olmadığını ve değişim oranlarını yorumlar.',kalip='grafik',
 metin='Sabit sıcaklıkta, sabit hacimli kapalı bir kaba yalnız N₂O₄ gazı konuluyor ve\nN₂O₄(g) ⇌ 2NO₂(g)\ntepkimesi gerçekleşiyor. Gazların derişimlerinin zamanla değişimi grafikte verilmiştir.\nBuna göre,\nI. t₁ anında tepkime dengeye ulaşmıştır.\nII. t₁ anından sonra N₂O₄ ve NO₂ derişimleri birbirine eşittir.\nIII. 0–t₁ aralığında NO₂ derişimindeki artış, N₂O₄ derişimindeki azalmanın 2 katıdır.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w3['dogru'],yan=w3['yan'],sira=w3['sira'],istenen='Grafiğe göre doğru olan yargılar.',
 ip=['Her yargıyı, ilgili eğrilerin ya da değişim miktarlarının grafikteki değerleriyle sına.'],bilgi=[DTB],
 puf='Derişimlerin değişim oranı katsayıların oranına eşittir; dengede derişimler eşit olmak zorunda değildir.')

# ================ 04 · orta · tablo, başlangıç–denge → Kc
card(3,'Mol tablosundan Kc','Denge mol sayıları hacme bölünerek derişime çevrilir; tüketilen miktarlar katsayılarla orantılıdır.','Hacmi hesaba katmamak; tüketilen miktarı katsayıyla ilişkilendirmemek.','orta','tablo',4,'de-kc','başlangıç ve denge mollerinden Kc hesabı')
V4,s4,o4,x4=5,6,6,4
S4=Fr(s4-x4,V4); O4=(Fr(o4)-Fr(x4,2))/V4; T4=Fr(x4,V4)
Kc4=T4**2/(S4**2*O4); assert Kc4==5
m4a=1/Kc4; m4b=Fr(x4**2,(s4-x4)**2)/(Fr(o4)-Fr(x4,2)); m4c=T4**2/(S4*O4); m4d=T4**2/(S4**2*((Fr(o4)-x4)/V4)); m4e=T4**2/((Fr(s4)/V4-Fr(x4,2*V4))**2*O4)
assert (m4a,m4b,m4c,m4d,m4e)==(Fr(1,5),1,2,10,Fr(5,4))
SK=tablo_svg(['Gaz','Başlangıç (mol)','Denge (mol)'],[['SO₂(g)','6','?'],['O₂(g)','6','?'],['SO₃(g)','0','4']])
q('0004',3,[A('Tüketilenleri bul','4 mol SO₃ oluştuysa katsayılar 2 : 1 : 2 olduğundan 4 mol SO₂ ve 2 mol O₂ harcanmıştır.','SO₂: 6 − 4 = 2 mol · O₂: 6 − 2 = 4 mol'),
   A('Derişimlere çevir','Denge mol sayıları kap hacmi olan 5 L’ye bölünür.','[SO₂] = 0,4 · [O₂] = 0,8 · [SO₃] = 0,8 mol/L'),
   A('Kc ifadesini yaz','Katsayılar üs olur.','Kc = [SO₃]² ÷ ([SO₂]² × [O₂])'),
   A('Hesapla','Değerleri yerleştir.','Kc = 0,64 ÷ (0,16 × 0,8) = 0,64 ÷ 0,128 = 5')],
 tipId='de-kc',z='orta',alt='Denge Sabiti',kaz='Başlangıç ve denge mol sayılarından denge derişimlerini bulup Kc değerini hesaplar.',kalip='tablo',
 metin='Sabit sıcaklıkta 5 L hacimli kapalı bir kaba SO₂ ve O₂ gazları konuluyor ve\n2SO₂(g) + O₂(g) ⇌ 2SO₃(g)\ntepkimesi dengeye ulaşıyor. Maddelerin başlangıçtaki ve dengedeki mol sayılarına ait bilgiler tabloda verilmiştir.\nBuna göre, tepkimenin bu sıcaklıktaki Kc değeri kaçtır?',
 sekil=SK,dogru=5,yan=[(m4a,'Kc ifadesini ürün ve girenleri ters yazarak kurmuş: 1 ÷ 5 = 0,2.','bilgi'),
  (m4b,'Mol sayılarını hacme bölmeden yerleştirmiş: 4² ÷ (2² × 4) = 1.','dikkat'),
  (m4c,'Kc ifadesinde [SO₂] derişimine üs olarak 2 yerine 1 yazmış: 0,64 ÷ (0,4 × 0,8) = 2.','bilgi'),
  (m4d,'O₂ için tüketilen miktarı 4 mol almış (katsayıyı SO₃ ile aynı sanmış): [O₂] = 0,4 ve Kc = 0,64 ÷ (0,16 × 0,4) = 10.','bilgi'),
  (m4e,'SO₂ için tüketilen miktarı 2 mol almış: [SO₂] = 0,8 ve Kc = 0,64 ÷ (0,64 × 0,8) = 1,25.','islem')][:4],
 istenen='Tepkimenin Kc değeri.',ip=['Tabloda eksik olan denge mol sayılarını katsayı oranlarını kullanarak tamamla; sonra hacmi unutma.'],bilgi=[ICEB],
 puf='Kc için önce denge mollerini bulup hacme böl; katsayı oranı tüketim oranını verir.')

# ---------- şekil yardımcıları
def piston(ox,h,hm,w,inside=(),vlab=None,arrow=False,solids=()):
    o=[f'\\fill[vurgu!12] ({ox:.2f},0) rectangle ({ox+w:.2f},{h:.2f});',
       f'\\draw[thick] ({ox:.2f},{hm+.3:.2f}) -- ({ox:.2f},0) -- ({ox+w:.2f},0) -- ({ox+w:.2f},{hm+.3:.2f});',
       f'\\draw[thick,fill=gray!40] ({ox:.2f},{h:.2f}) rectangle ({ox+w:.2f},{h+.2:.2f});',
       f'\\draw[thick] ({ox+w/2:.2f},{h+.2:.2f}) -- ({ox+w/2:.2f},{hm+.9:.2f});',
       f'\\draw[thick] ({ox+w/2-.45:.2f},{hm+.9:.2f}) -- ({ox+w/2+.45:.2f},{hm+.9:.2f});']
    if arrow: o.append(f'\\draw[vurgu,very thick,{ARR}] ({ox+w/2:.2f},{hm+1.7:.2f}) -- ({ox+w/2:.2f},{hm+1.05:.2f});')
    for (sx,sw,sh,lab) in solids:
        o.append(f'\\draw[fill=gray!35] ({ox+sx:.2f},0) rectangle ({ox+sx+sw:.2f},{sh:.2f});')
        o.append(f'\\node[font=\\footnotesize] at ({ox+sx+sw/2:.2f},{sh/2:.2f}) {{{lab}}};')
    for i,t in enumerate(inside):
        o.append(f'\\node[font=\\footnotesize] at ({ox+w/2:.2f},{(h*0.78 if h>2 else h*0.5)-0.38*i:.2f}) {{{t}}};')
    if vlab: o.append(f'\\draw[{{Stealth[length=1.6mm]}}-{{Stealth[length=1.6mm]}}] ({ox+w+.3:.2f},0) -- ({ox+w+.3:.2f},{h:.2f}); \\node[anchor=west] at ({ox+w+.3:.2f},{h/2:.2f}) {{{vlab}}};')
    return o

# ================ 05 · orta · Kp, tanecik modeli
card(5,'Kısmi basınç ve Kp','Kısmi basınç = mol kesri × toplam basınç; Kp ifadesinde Kc gibi katsayılar üs olur.','Toplam basıncı kısmi basınç yerine kullanmak; tanecik sayılarını doğrudan Kp ifadesine yazmak.','orta','şekilli',4,'de-kp','tanecik modelinden Kp hesabı')
nsq,nci,Pt5=2,6,4
P5a=Fr(nsq,nsq+nci)*Pt5; P5b=Fr(nci,nsq+nci)*Pt5
Kp5=P5b**2/P5a; assert (P5a,P5b,Kp5)==(1,3,9)
m5=(P5b/P5a, 2*P5b/P5a, Fr(Pt5**2)/P5a, Fr(nci**2,nsq)); assert m5==(3,6,16,18)
sq=[(1.0,0.7),(3.2,1.9)]; ci=[(2.1,0.6),(3.3,0.7),(0.8,1.9),(1.9,1.7),(2.7,1.2),(1.2,1.2)]
assert len(sq)==nsq and len(ci)==nci
o=['\\draw[thick] (0,0) rectangle (4.2,2.6);']
for x,y in sq: o.append(f'\\draw[fill=gray!35] ({x-.15:.2f},{y-.15:.2f}) rectangle ({x+.15:.2f},{y+.15:.2f});')
for x,y in ci: o.append(f'\\draw[fill=white] ({x:.2f},{y:.2f}) circle (.16);')
o+= ['\\draw[fill=gray!35] (0.3,-.55) rectangle (.6,-.25); \\node[anchor=west] at (.7,-.4) {\\ce{N2O4}};','\\draw[fill=white] (2.45,-.4) circle (.16); \\node[anchor=west] at (2.7,-.4) {\\ce{NO2}};']
SK=tikz(o)
q('0005',5,[A('Taneciklerin sayısını oku','Şekilde 2 tane N₂O₄ ve 6 tane NO₂ tanesi var; toplam 8 tanecik.','n(N₂O₄) : n(NO₂) = 2 : 6'),
   A('Kısmi basınçları bul','Kısmi basınç = mol kesri × toplam basınç.','P(N₂O₄) = 2/8 × 4 = 1 atm · P(NO₂) = 6/8 × 4 = 3 atm'),
   A('Kp ifadesini yaz','Girenin ve ürünün katsayıları üs olur.','Kp = P(NO₂)² ÷ P(N₂O₄)'),
   A('Hesapla','Değerleri yerleştir.','Kp = 3² ÷ 1 = 9')],
 tipId='de-kp',z='orta',alt='Kısmi Basınç ve Kp',kaz='Tanecik modelinden kısmi basınçları bulup Kp değerini hesaplar.',kalip='şekilli',
 metin='Sabit sıcaklıkta kapalı bir kapta\nN₂O₄(g) ⇌ 2NO₂(g)\ntepkimesi dengededir. Kaptaki toplam basınç 4 atm olup denge anındaki gaz karışımının tanecik modeli şekilde verilmiştir.\nBuna göre, tepkimenin bu sıcaklıktaki Kp değeri kaçtır?',
 sekil=SK,dogru=9,yan=[(m5[0],'Kp ifadesinde P(NO₂) basıncının üssünü 2 yerine 1 yazmış: 3 ÷ 1 = 3.','dikkat'),
  (m5[1],'Katsayıyı üs yerine çarpan olarak kullanmış: (2 × 3) ÷ 1 = 6.','bilgi'),
  (m5[2],'Toplam basıncı NO₂’nin kısmi basıncı yerine kullanmış: 4² ÷ 1 = 16.','bilgi'),
  (m5[3],'Kısmi basınç yerine tanecik sayılarını yazmış: 6² ÷ 2 = 18.','dikkat')],
 istenen='Tepkimenin Kp değeri.',ip=['Önce toplam basıncı, gazların tanecik sayısı oranında paylaştır.'],bilgi=[KPB],
 puf='Kp için tanecik (mol) oranından kısmi basınçları bul; sayıları doğrudan ifadeye yazma.')

# ================ 06 · orta · Kp–Kc, olumsuz öncüllü
card(6,'Kp–Kc ilişkisi','Kp = Kc·(RT)^Δn; RT > 1 olduğunda Δn < 0 ise Kp < Kc, Δn > 0 ise Kp > Kc, Δn = 0 ise Kp = Kc.','Katı ve sıvıları Δn hesabına katmak; Δn işaretini ters yorumlamak.','orta','öncüllü',4,'de-kp','Kp ile Kc arasındaki ilişki')
RT6=Fr(82,1000)*500; assert RT6==41
def dn(g,r): return g-r
tr6=[('H₂(g) + I₂(g) ⇌ 2HI(g)',2-2,'Kp = Kc'),('N₂(g) + 3H₂(g) ⇌ 2NH₃(g)',2-4,'Kp > Kc'),('C(k) + CO₂(g) ⇌ 2CO(g)',2-1,'Kp < Kc')]
w6=onc([True,False,False],['Δn = 0 olduğundan Kp = Kc × (RT)⁰ = Kc olur','Δn = 2 − 4 = −2 ve RT = 41 > 1 olduğundan Kp = Kc ÷ 41² değeri Kc’den küçüktür','Δn = 2 − 1 = +1 ve RT = 41 > 1 olduğundan Kp = 41 × Kc değeri Kc’den büyüktür'],4,neg=True)
assert Fr(1,41)**2<1 and 41>1
q('0006',6, [A('Δn değerlerini bul','Yalnız gaz hâlindeki maddelerin katsayıları sayılır; katılar dışarıda kalır.','I: Δn = 0 · II: Δn = −2 · III: Δn = +1'),
  A('RT değerini hesapla','R × T = 0,082 × 500 = 41 olduğundan RT, 1’den büyüktür.','RT = 41 > 1'),
  A('Yargıları sına','Kp = Kc × (RT)^Δn bağıntısı kullanılır.','I: Kp = Kc → doğru · II: Kp = Kc ÷ 41² → Kp < Kc, yargı yanlış · III: Kp = 41 × Kc → Kp > Kc, yargı yanlış'),
  A('Sonuç','Yanlış yargılar aranıyor.','II ve III')],
 tipId='de-kp',z='orta',alt='Kp ile Kc İlişkisi',kaz='Gaz hâlindeki maddelerin mol sayısındaki değişime (Δn) göre Kp ile Kc arasındaki ilişkiyi belirler.',kalip='öncüllü',
 metin='500 K sıcaklıkta gerçekleşen denge tepkimeleri ile bu tepkimelerin Kp ve Kc değerleri arasındaki ilişkiler aşağıda verilmiştir.\nI. H₂(g) + I₂(g) ⇌ 2HI(g) tepkimesinde Kp = Kc dir.\nII. N₂(g) + 3H₂(g) ⇌ 2NH₃(g) tepkimesinde Kp > Kc dir.\nIII. C(k) + CO₂(g) ⇌ 2CO(g) tepkimesinde Kp < Kc dir.\n(R = 0,082 L·atm/mol·K)\nBuna göre, bu yargılardan hangileri yanlıştır?',
 dogru=w6['dogru'],yan=w6['yan'],sira=w6['sira'],istenen='Yanlış olan yargılar.',
 ip=['Her tepkime için Δn’yi bul ve R × T çarpımının değerini hesapla; sonra Kp = Kc × (RT)^Δn bağıntısını yorumla.'],bilgi=[KPKC],
 puf='RT > 1 iken Kp ile Kc’nin sıralaması Δn’nin işaretiyle aynı yöndedir: Δn < 0 ise Kp < Kc, Δn > 0 ise Kp > Kc.')

# ================ 07 · orta · katı içeren denge, tablo
card(4,'Katı içeren denge','Saf katı ve sıvılar Kc ifadesine yazılmaz; yalnız gazların derişimleri kullanılır.','Katıları Kc ifadesine yazmak; mol sayısı ile derişimi karıştırmak.','orta','tablo',3,'de-kc','katı içeren denge ve Kc')
V7=2; nH2,nH2O=Fr(4,5),Fr(8,5)
Kc7=(nH2O/V7)**4/(nH2/V7)**4; assert Kc7==16
nFe,nFe3O4=3,Fr(3,2)
m7=(1/Kc7, nH2O/nH2, (nH2O/nH2)**2, (Fr(nFe,V7)**3*(nH2O/V7)**4)/(Fr(nFe3O4,V7)*(nH2/V7)**4)); assert m7==(Fr(1,16),2,4,72)
SK=tablo_svg(['Madde','Denge (mol)'],[['Fe₃O₄(k)','1,5'],['H₂(g)','0,8'],['Fe(k)','3'],['H₂O(g)','1,6']])
q('0007',4,[A('Kc ifadesini yaz','Katılar yazılmaz; yalnız gazlar kalır ve katsayılar üs olur.','Kc = [H₂O]⁴ ÷ [H₂]⁴'),
   A('Derişimlere çevir','Gazların mol sayıları 2 L’ye bölünür.','[H₂] = 0,8 ÷ 2 = 0,4 · [H₂O] = 1,6 ÷ 2 = 0,8 mol/L'),
   A('Hesapla','Oranı bul ve dördüncü kuvveti al.','Kc = (0,8 ÷ 0,4)⁴ = 2⁴ = 16')],
 tipId='de-kc',z='orta',alt='Heterojen Denge',kaz='Katı ve gaz içeren denge tepkimesinde Kc ifadesini yazar ve değerini hesaplar.',kalip='tablo',
 metin='2 L hacimli kapalı bir kapta\nFe₃O₄(k) + 4H₂(g) ⇌ 3Fe(k) + 4H₂O(g)\ntepkimesi sabit sıcaklıkta dengeye ulaştığında maddelerin mol sayıları tabloda verilmiştir.\nBuna göre, tepkimenin bu sıcaklıktaki Kc değeri kaçtır?',
 sekil=SK,dogru=16,yan=[(m7[0],'Kc ifadesini ürün ve girenleri ters yazarak kurmuş: (0,4 ÷ 0,8)⁴ = 1 ÷ 16 = 0,0625.','bilgi'),
  (m7[1],'Derişimlerin oranını almış ama dördüncü kuvvetini almayı unutmuş: 0,8 ÷ 0,4 = 2.','dikkat'),
  (m7[2],'Katsayıyı 4 yerine 2 alarak oranın karesini yazmış: (0,8 ÷ 0,4)² = 4.','dikkat'),
  (m7[3],'Katıları da Kc ifadesine yazmış: (1,5³ × 0,8⁴) ÷ (0,75 × 0,4⁴) = 72.','bilgi')],
 istenen='Tepkimenin Kc değeri.',ip=['Kc ifadesine hangi maddelerin yazılıp hangilerinin yazılmayacağına karar vererek başla.'],bilgi=[HETB],
 puf='Katı ve sıvı yazılmaz; gazların derişimini mol ÷ hacim ile bul.')

# ================ 08 · orta · piston, Le Chatelier öncüllü
card(7,'Hacim değişimi ve denge','Hacim azalınca denge gaz mol sayısı az olan yöne kayar; Kc değişmez; yeni derişimler ilk derişimlerden büyük kalır.','Kc’nin değiştiğini sanmak; derişimin ilk değerine döndüğünü düşünmek.','orta','şekilli',3,'de-le','piston ile hacim değişimi ve denge')
Kc8=Fr(1,4); a0,b0=Fr(1),Fr(1,2); assert b0*b0/a0==Kc8
A1=2*a0; B1=2*b0   # hacim yarıya -> derişimler 2 katı
z=Fr(1,4); assert (B1-z)**2==Kc8*(A1+z)   # (1-z)^2=0.25(2+z)
assert (B1-z)>b0 and (A1+z)>a0
n_before=a0; n_after=(A1+z)/2; assert n_after>n_before
o=piston(0,2.4,2.4,1.9,vlab='$V$')+piston(3.5,1.2,2.4,1.9,vlab='$V/2$',arrow=True)
o.append('\\node at (2.7,-.7) {\\ce{PCl5(g) <=> PCl3(g) + Cl2(g)}};')
o.append('\\node[font=\\footnotesize] at (2.7,-1.25) {sabit sıcaklık};')
SK=tikz(o)
w8=onc([True,True,False],['hacim azalınca denge gaz mol sayısı az olan yöne, yani PCl₅ yönüne kayar; PCl₅ mol sayısı artar','Kc yalnız sıcaklığa bağlıdır; sıcaklık sabit olduğundan değişmez','hacim yarıya inince derişimler önce iki katına çıkar, denge kayması bu artışı yalnız kısmen azaltır; yeni PCl₃ derişimi ilkinden büyüktür'],1)
q('0008',7,[A('Gaz mol sayılarını karşılaştır','Girenlerde 1, ürünlerde 2 mol gaz var; hacim küçülünce denge girenler yönüne kayar.','Denge PCl₅ yönüne kayar'),
   A('I ve II’yi değerlendir','PCl₅ mol sayısı artar; Kc yalnız sıcaklığa bağlıdır.','I: doğru · II: doğru'),
   A('III’ü değerlendir','Derişimler önce iki katına çıkar, kayma bu artışı tamamen geri almaz.','III: yanlış'),
   A('Sonuç','Doğru yargılar seçilir.','I ve II')],
 tipId='de-le',z='orta',alt='Le Chatelier İlkesi',kaz='Hacim değişiminin denge konumuna, Kc değerine ve derişimlere etkisini yorumlar.',kalip='şekilli',
 metin='Sabit sıcaklıkta, sürtünmesiz hareketli pistonlu bir kapta\nPCl₅(g) ⇌ PCl₃(g) + Cl₂(g)\ntepkimesi dengededir. Piston, şekilde gösterildiği gibi itilerek gazların hacmi yarıya düşürülüyor ve sistem yeniden dengeye geliyor.\nBuna göre,\nI. PCl₅ mol sayısı artar.\nII. Kc değeri değişmez.\nIII. PCl₃ derişimi ilk dengedekinden küçük olur.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w8['dogru'],yan=w8['yan'],sira=w8['sira'],istenen='Doğru olan yargılar.',
 ip=['Hacim değişiminin hangi yöndeki tepkimeyi desteklediğini gaz mol sayılarına bakarak belirle; derişimlerin önce ne olduğunu da düşün.'],bilgi=[LCB],
 puf='Hacim küçülünce derişimler önce artar, sonra denge kaymasıyla kısmen geri döner; ilk değerine hiçbir zaman dönmez.')

# ================ 09 · orta · Kc–T grafiği
card(8,'Sıcaklık, K ve ΔH','Kc sıcaklıkla azalıyorsa tepkime ekzotermiktir; sıcaklık artınca ürün azalır, tüm hızlar artar.','Sıcaklıkla yalnız endotermik yöndeki hızın arttığını sanmak.','orta','grafik',3,'de-le','Kc–sıcaklık grafiği ve denge')
kt=[(x,1.2+8*exp(-0.42*(x-1))) for x in [1+0.4*i for i in range(21)]]
SK=pg('width=6.2cm,height=4.6cm,axis lines=left,xmin=0,xmax=10,ymin=0,ymax=10,xtick=\\empty,ytick=\\empty,xlabel={Sıcaklık (K)},ylabel={$K_c$},label style={font=\\small}',
 f'\\addplot[thick,smooth] coordinates {{{co(kt)}}};')
w9=onc([True,True,True],['denge sabiti sıcaklık arttıkça küçüldüğüne göre tepkime ekzotermiktir (ΔH < 0)','sıcaklık artınca K küçülür; denge girenler yönüne kayar ve C gazının mol sayısı azalır','sıcaklık artınca hem ileri hem geri tepkimenin hızı artar; yalnız ileri ile geri hız farklı oranda artar'],4)
q('0009',8,[A('Grafiği yorumla','Kc sıcaklıkla azalıyor; ürün oranı küçülüyor.','Tepkime ekzotermik (ΔH < 0) → I: doğru'),
   A('Dengenin kaymasına bak','Sıcaklık artınca denge girenler yönüne kayar.','C miktarı azalır → II: doğru'),
   A('Hızları değerlendir','Sıcaklık arttıkça tanecikler daha çok çarpışır; her iki yönün hızı da artar.','III: doğru'),
   A('Sonuç','Üç yargı da doğrudur.','I, II ve III')],
 tipId='de-le',z='orta',alt='Sıcaklığın Etkisi',kaz='Kc–sıcaklık grafiğinden tepkimenin ısı değişimini yorumlar; sıcaklık artışının denge ve hızlara etkisini belirler.',kalip='grafik',
 metin='Belirli bir sıcaklık aralığında\nA(g) + B(g) ⇌ 2C(g)\ndengesine ait denge sabiti (Kc) değerinin sıcaklıkla değişimi grafikte verilmiştir.\nBuna göre,\nI. Tepkime ekzotermiktir.\nII. Sabit hacimde sıcaklık artırılırsa C gazının mol sayısı azalır.\nIII. Sıcaklık artırılırsa ileri ve geri yöndeki tepkimelerin hızları artar.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w9['dogru'],yan=w9['yan'],sira=w9['sira'],istenen='Doğru olan yargılar.',
 ip=['Grafiği yorumlayıp her yargıyı Le Chatelier ilkesi ve sıcaklığın hıza etkisiyle sına.'],bilgi=[KTB],
 puf='K sıcaklıkla azalıyorsa tepkime ekzotermiktir; sıcaklık artışı her iki yönün hızını artırır.')

# ================ 10 · orta · derişim–zaman, bileşen eklenmesi (olumsuz kök)
n0,h0,a0_=0.4,0.2,0.2; Kc10=a0_**2/(n0*h0**3); assert abs(Kc10-12.5)<1e-9
add10=0.4
def f10(y): return (a0_+2*y)**2-Kc10*(n0-y)*(h0+add10-3*y)**3
lo,hi=0.0,0.19
for _ in range(100):
    mid=(lo+hi)/2
    if f10(lo)*f10(mid)<=0: hi=mid
    else: lo=mid
y10=(lo+hi)/2
nN,nH,nA=n0-y10,h0+add10-3*y10,a0_+2*y10
assert nN>0 and nH>0 and abs(nA**2/(nN*nH**3)-Kc10)<1e-6 and nA>a0_ and y10>0
print('Q10 y',round(y10,4),round(nN,3),round(nH,3),round(nA,3))
T1,T2,T3,XM=3,5,8,11
g_N=ease(0.5,n0,0,T1,T2)+[(T2,n0)]+ease(n0,nN,T2,T3,XM)
g_H=ease(0.5,h0,0,T1,T2)+[(T2,h0),(T2,h0+add10)]+ease(h0+add10,nH,T2,T3,XM)
g_A=ease(0,a0_,0,T1,T2)+[(T2,a0_)]+ease(a0_,nA,T2,T3,XM)
SK=pg('width=6.8cm,height=5.2cm,axis lines=left,xmin=0,xmax=11,ymin=0,ymax=0.7,xtick={3,5,8},xticklabels={$t_1$,$t_2$,$t_3$},ytick distance=0.1,yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman},ylabel={Derişim (mol/L)},legend style={draw=none,font=\\small,at={(0.99,0.99)},anchor=north east,fill=none},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick] coordinates {{{co(g_N)}}};\n\\addlegendentry{{$\\mathrm{{N_2}}$}}\n\\addplot[thick,dashed] coordinates {{{co(g_H)}}};\n\\addlegendentry{{$\\mathrm{{H_2}}$}}\n\\addplot[thick,dotted,very thick] coordinates {{{co(g_A)}}};\n\\addlegendentry{{$\\mathrm{{NH_3}}$}}')
card(10,'Derişim–zaman grafiğinde etki','Anlık sıçrama maddenin eklendiğini gösterir; denge o maddeyi harcayan yöne kayar; K sabit sıcaklıkta değişmez.','Kc değerinin etki sonrası değiştiğini sanmak; sıçramayı sıcaklık etkisiyle karıştırmak.','orta','grafik',4,'de-grafik','derişim–zaman grafiğinde bileşen eklenmesi')
o10=tek([('t₂ anında kaba H₂ gazı eklenmiştir.',True,'Grafikte t₂ anında yalnız H₂ derişimi ani olarak yükselmektedir; bu ifade doğru olduğu hâlde yanlış sanılmıştır.'),
 ('t₁–t₂ aralığında ileri ve geri yöndeki tepkime hızları eşittir.',True,'Derişimler t₁–t₂ aralığında sabit olduğundan sistem dengededir ve hızlar eşittir; bu ifade doğrudur.'),
 ('t₂–t₃ aralığında ileri yöndeki tepkime hızı geri yöndekinden büyüktür.',True,'H₂ eklenince denge ürünler yönüne kayar; NH₃ derişimi arttığına göre ileri hız geri hızdan büyüktür, bu ifade doğrudur.'),
 ('t₃ anında NH₃ derişimi t₁ anındakinden büyüktür.',True,'Grafikte NH₃ eğrisi t₃ anında t₁ anındaki değerin üstündedir; bu ifade doğrudur.'),
 ('t₃ anında Kc değeri t₁ anındakinden büyüktür.',False,'Sıcaklık sabit olduğundan Kc değişmez; bu ifade yanlıştır.')],False,0)
q('0010',10,[A('t₂ anını yorumla','Yalnız H₂ derişimi ani olarak artmış; bu, kaba H₂ eklendiğini gösterir.','A: doğru'),
   A('Denge aralıklarına bak','t₁–t₂ aralığında derişimler sabittir; hızlar eşittir.','B: doğru'),
   A('Yeni dengeye giden yolu incele','H₂ azalıyor, N₂ azalıyor, NH₃ artıyor; ileri hız geri hızdan büyüktür ve NH₃ ilkinden fazladır.','C ve D: doğru'),
   A('Kc değerini değerlendir','Kc yalnız sıcaklığa bağlıdır ve sıcaklık sabittir.','Kc değişmez → bu ifade söylenemez')],
 tipId='de-grafik',z='orta',alt='Derişim–Zaman Grafikleri',kaz='Derişim–zaman grafiğinde bir maddenin eklenmesini fark eder; yeni dengeye geçişte hız, derişim ve Kc değişimlerini yorumlar.',kalip='grafik',
 metin='Sabit hacimli kapalı bir kapta, sabit sıcaklıkta\nN₂(g) + 3H₂(g) ⇌ 2NH₃(g)\ntepkimesi t₁ anında dengeye ulaşıyor. t₂ anında sisteme bir etki yapılıyor ve t₃ anında yeniden denge kuruluyor. Gazların derişimlerinin zamanla değişimi grafikte verilmiştir.\nBuna göre, aşağıdaki ifadelerden hangisi söylenemez?',
 sekil=SK,dogru=o10['dogru'],yan=o10['yan'],sira=o10['sira'],istenen='Söylenemeyen (yanlış) ifade.',
 ip=['Sıcaklık sabit tutulurken t₂ anında hangi eğrinin ani değiştiğine bakarak yapılan etkiyi belirle.'],bilgi=[DTB],
 puf='Anlık sıçrama bir maddenin eklendiğini, kesintisiz değişim ise tepkimenin ilerlediğini gösterir; sabit sıcaklıkta Kc değişmez.')

# ================ 11 · orta · derişim–zaman → Kc (katsayılar grafikten)
X0,X1,Y0,Y1,Z0,Z1=Fr(1),Fr(2,5),Fr(4,5),Fr(1,2),Fr(0),Fr(3,5)
dX,dY,dZ=X0-X1,Y0-Y1,Z1-Z0; assert (dX,dY,dZ)==(Fr(3,5),Fr(3,10),Fr(3,5)) and (dX/dY,dZ/dY)==(2,2)
Kc11=Z1**2/(X1**2*Y1); assert Kc11==Fr(9,2)
m11=(Z1**2/(X1*Y1), Z1/(X1*Y1), Z1**2/(X1*Y1**2), Z1**2/(X1**2*Y1**2)); assert m11==(Fr(9,5),3,Fr(18,5),9)
gx=[(x,float(y)) for x,y in ease(X0,X1,0,5,8)]; gy=[(x,float(y)) for x,y in ease(Y0,Y1,0,5,8)]; gz=[(x,float(y)) for x,y in ease(Z0,Z1,0,5,8)]
SK=pg('width=6.6cm,height=5.4cm,axis lines=left,xmin=0,xmax=8,ymin=0,ymax=1.0,xtick={5},xticklabels={$t_1$},ytick distance=0.1,yticklabel={\\pgfmathprintnumber[fixed,fixed zerofill,precision=1,use comma]{\\tick}},grid=major,major grid style={gray!45,thin},xlabel={Zaman},ylabel={Derişim (mol/L)},legend style={draw=none,font=\\small,at={(0.99,0.99)},anchor=north east,fill=none},label style={font=\\small},tick label style={font=\\small}',
 f'\\addplot[thick] coordinates {{{co(gx)}}};\n\\addlegendentry{{X}}\n\\addplot[thick,dashed] coordinates {{{co(gy)}}};\n\\addlegendentry{{Y}}\n\\addplot[thick,dotted,very thick] coordinates {{{co(gz)}}};\n\\addlegendentry{{Z}}')
q('0011',9,[A('Değişimleri oku','Grafikte t₁ anına kadar X: 1,0 → 0,4; Y: 0,8 → 0,5; Z: 0 → 0,6 olmuştur.','ΔX = 0,6 · ΔY = 0,3 · ΔZ = 0,6'),
   A('Katsayıları bul','Değişim miktarları katsayılarla orantılıdır; en küçük tam sayı oranı alınır.','ΔX : ΔY : ΔZ = 2 : 1 : 2 → 2X + Y ⇌ 2Z'),
   A('Kc ifadesini yaz','Denge anındaki derişimler (t₁ sonrası) kullanılır.','Kc = [Z]² ÷ ([X]² × [Y])'),
   A('Hesapla','Değerleri yerleştir.','Kc = 0,6² ÷ (0,4² × 0,5) = 0,36 ÷ 0,08 = 4,5')],
 tipId='de-grafik',z='orta',alt='Derişim–Zaman Grafikleri',kaz='Derişim–zaman grafiğindeki değişim miktarlarından katsayıları bulup Kc değerini hesaplar.',kalip='grafik',
 metin='Sabit hacimli kapalı bir kapta, sabit sıcaklıkta gerçekleşen ve X ile Y gazlarının Z gazına dönüştüğü bir tepkimede X, Y ve Z’nin derişimlerinin zamanla değişimi grafikte verilmiştir. Tepkime denkleminin katsayıları verilmemiştir ve t₁ anında denge kurulmuştur.\nBuna göre, tepkimenin bu sıcaklıktaki Kc değeri kaçtır?',
 sekil=SK,dogru=Fr(9,2),yan=[(m11[0],'X için katsayıyı 1 almış: Kc = 0,6² ÷ (0,4 × 0,5) = 1,8.','bilgi'),
  (m11[1],'Tepkimeyi X + Y ⇌ Z sanıp katsayıları üs yapmamış: Kc = 0,6 ÷ (0,4 × 0,5) = 3.','bilgi'),
  (m11[2],'Katsayıları karıştırarak X için 1, Y için 2 almış: Kc = 0,6² ÷ (0,4 × 0,5²) = 3,6.','bilgi'),
  (m11[3],'Y için de katsayıyı 2 almış: Kc = 0,6² ÷ (0,4² × 0,5²) = 9.','bilgi')],
 istenen='Tepkimenin Kc değeri.',ip=['Denge öncesindeki derişim değişimlerinin oranından tepkimenin katsayılarını çıkar.'],bilgi=[DTB],
 puf='Katsayıları bilmiyorsan derişim değişimlerinin oranına bak; Kc için yalnız denge derişimlerini kullan.')

# ================ 12 · orta · Q ile K, kap şeması
card(11,'Tepkime bölümü Q','Q, başlangıç derişimleriyle Kc gibi hesaplanır; Q < K ise ileri, Q > K ise geri yönde ilerler; K sabit sıcaklıkta değişmez.','Mol sayısını derişim yerine kullanmak; Q ile K’yı karşılaştırırken yönü ters yorumlamak.','orta','şekilli',4,'de-qk','Q ile K karşılaştırması')
V12,nNO2,nN2O4,K12=2,Fr(1),Fr(1,2),4
Q12=(nN2O4/V12)/(nNO2/V12)**2; assert Q12==1 and Q12<K12
o=['\\draw[thick] (0,0) rectangle (3.6,2.3);','\\node at (1.8,1.5) {\\ce{NO2}: 1 mol};','\\node at (1.8,.8) {\\ce{N2O4}: 0,5 mol};',
   '\\draw[{Stealth[length=1.6mm]}-{Stealth[length=1.6mm]}] (3.9,0) -- (3.9,2.3); \\node[anchor=west] at (3.9,1.15) {$V = 2$ L};']
SK=tikz(o)
w12=onc([False,True,False],['başlangıçta Q = [N₂O₄] ÷ [NO₂]² = 0,25 ÷ 0,25 = 1 olup Kc = 4’ten küçüktür','Q < Kc olduğundan tepkime ileri yönde ilerler ve N₂O₄ derişimi artar','Kc yalnız sıcaklığa bağlıdır; sıcaklık sabit olduğundan değişmez'],0)
q('0012',11,[A('Derişimleri bul','Mol sayıları 2 L’ye bölünür.','[NO₂] = 0,5 mol/L · [N₂O₄] = 0,25 mol/L'),
   A('Q değerini hesapla','Q ifadesi Kc ile aynı biçimde yazılır.','Q = [N₂O₄] ÷ [NO₂]² = 0,25 ÷ 0,25 = 1'),
   A('Q ile Kc’yi karşılaştır','Q < Kc olduğundan sistem ürün yönüne ilerler.','1 < 4 → ileri yön'),
   A('Yargıları değerlendir','I yanlış; II doğru; Kc sabit olduğundan III yanlış.','Yalnız II')],
 tipId='de-qk',z='orta',alt='Tepkime Bölümü (Q)',kaz='Q ile Kc değerini karşılaştırarak tepkimenin yönünü ve derişim değişimini yorumlar.',kalip='şekilli',
 metin='Belirli bir sıcaklıkta\n2NO₂(g) ⇌ N₂O₄(g)\ntepkimesinin denge sabiti Kc = 4 tür. Bu sıcaklıkta, hacmi sabit tutulan bir kaba şekilde belirtilen miktarlarda NO₂ ve N₂O₄ gazları konuluyor.\nBuna göre,\nI. Başlangıçta Q > Kc dir.\nII. Dengeye ulaşıncaya kadar N₂O₄ derişimi artar.\nIII. Dengeye ulaşıncaya kadar Kc değeri artar.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w12['dogru'],yan=w12['yan'],sira=w12['sira'],istenen='Doğru olan yargılar.',
 ip=['Kaptaki mol sayılarını önce derişime çevir ve Q’yu Kc ile aynı biçimde yaz.'],bilgi=[QKB],
 puf='Q ile K karşılaştırması yönü verir; K ise yalnız sıcaklıkla değişir.')

# ================ 13 · orta · K değerlerini birleştirme
card(12,'Denge sabitlerinin birleştirilmesi','Tepkime tersine çevrilirse K → 1/K, katsayılar n katına çıkarsa K → Kⁿ, tepkimeler toplanırsa K’ler çarpılır.','Ters çevirme ya da yarıya bölmeyi hesaba katmamak; toplama yerine bölme yapmak.','orta','hikâyeli',4,'de-kb','K değerlerinin birleştirilmesi')
K1,K2=2,32
Ktop=K1*K2; Ksonuc=Fr(1)/Fr(int(sqrt(Ktop))); assert int(sqrt(Ktop))**2==Ktop and Ksonuc==Fr(1,8)
m13=(Fr(int(sqrt(Ktop))),Fr(Ktop),Fr(K2,K1),Fr(1,Ktop)); assert m13==(8,64,16,Fr(1,64))
q('0013',12,[A('Toplam tepkimeyi kur','İki tepkime toplanınca NO sadeleşir.','N₂ + O₂ ⇌ 2NO · 2NO + O₂ ⇌ 2NO₂ → N₂(g) + 2O₂(g) ⇌ 2NO₂(g)'),
   A('Toplamın K’sini bul','Tepkimeler toplanınca K değerleri çarpılır.','Ktop = 2 × 32 = 64'),
   A('Hedef tepkimeyi karşılaştır','Hedef, toplam tepkimenin tersinin yarısıdır: NO₂ ⇌ ½N₂ + O₂.','Ters çevirme: 1 ÷ 64 · yarıya bölme: kök alma'),
   A('Hesapla','K → (1 ÷ Ktop)^(1/2).','K = (1 ÷ 64)^(1/2) = 1 ÷ 8 = 0,125')],
 tipId='de-kb',z='orta',alt='Denge Sabitlerinin Birleştirilmesi',kaz='Denge sabitleri bilinen tepkimelerden, ters çevirme, katsayı değiştirme ve toplama kurallarıyla yeni tepkimenin denge sabitini hesaplar.',kalip='düz',
 metin='Belirli bir sıcaklıkta aşağıdaki tepkimelerin denge sabitleri verilmiştir.\nN₂(g) + O₂(g) ⇌ 2NO(g)    K₁ = 2\n2NO(g) + O₂(g) ⇌ 2NO₂(g)    K₂ = 32\nBuna göre, aynı sıcaklıkta\nNO₂(g) ⇌ ½N₂(g) + O₂(g)\ntepkimesinin denge sabiti kaçtır?',
 dogru=Fr(1,8),yan=[(m13[0],'Tepkimeyi tersine çevirmeyi unutup yalnız kök almış: √64 = 8.','bilgi'),
  (m13[1],'İki denge sabitini çarpıp toplam tepkimenin K değerinde bırakmış: 2 × 32 = 64.','bilgi'),
  (m13[2],'Tepkimeler arasında bölme yapmış: 32 ÷ 2 = 16.','islem'),
  (m13[3],'Tersini almış ancak katsayıyı ½ ile çarpmanın kök almak olduğunu unutmuş: 1 ÷ 64 = 0,015625.','bilgi')],
 istenen='Hedef tepkimenin denge sabiti.',ip=['Verilen iki tepkimeyi toplayarak hedefe en yakın tepkimeyi elde et; sonra tersine çevirme ve katsayı farkını düşün.'],bilgi=[KBB],
 puf='Önce toplayıp K’leri çarp; ters çevirince 1/K, katsayıyı n’ye çarpınca Kⁿ.')

# ================ 14 · orta · C(k) + CO₂ ⇌ 2CO, manometre kapları
card(13,'Katı içeren denge ve Kp','Kp ifadesine yalnız gazların kısmi basınçları girer; sabit hacimde basınç değişimi gaz mol sayısı değişimini verir.','Katıyı Kp ifadesine yazmak; toplam basıncı kısmi basınç yerine kullanmak.','orta','şekilli',4,'de-kp','katı içeren denge ve Kp')
P0,Pt=Fr(3),Fr(9,2); x14=Pt-P0; assert x14==Fr(3,2)
pco2,pco=P0-x14,2*x14; Kp14=pco**2/pco2; assert (pco2,pco,Kp14)==(Fr(3,2),3,6)
m14=(pco/pco2,pco**2/P0,pco**2,Pt**2/pco2); assert m14==(2,3,9,Fr(27,2))
def kap(ox,gtxt,pm,ttl):
    r=[f'\\draw[thick] ({ox},0) rectangle ({ox+2.8},2.2);',f'\\draw[fill=gray!35] ({ox+.3},0) rectangle ({ox+1.1},.5); \\node[font=\\footnotesize] at ({ox+.7},.25) {{C(k)}};',
       f'\\node[font=\\footnotesize] at ({ox+1.4},1.3) {{{gtxt}}};',f'\\draw[thick] ({ox+2.1},2.2) -- ({ox+2.1},2.7); \\draw[thick,fill=white] ({ox+2.1},3.3) circle (.62); \\node at ({ox+2.1},3.3) {{{pm}}};',
       f'\\node at ({ox+1.4},-.4) {{{ttl}}};']
    return r
o=kap(0,'\\ce{CO2}(g)','3 atm','Başlangıç')+kap(4.4,'\\ce{CO2}(g),\\ \\ce{CO}(g)','4,5 atm','Denge')+['\\draw[ARR,thick] (3,1.1) -- (4.2,1.1);'.replace('ARR',ARR)]
SK=tikz(o)
q('0014',13,[A('Tepkimeyi tablola','CO₂’den x atm harcanırsa 2x atm CO oluşur.','P(CO₂) = 3 − x ve P(CO) = 2x'),
   A('Toplam basıncı kullan','Katı basınca katkı yapmaz; toplam basınç gazların toplamıdır.','(3 − x) + 2x = 4,5 → x = 1,5 atm'),
   A('Kısmi basınçları bul','x değeri yerine konur.','P(CO₂) = 1,5 atm · P(CO) = 3 atm'),
   A('Kp ifadesini yaz ve hesapla','Katı ifadeye yazılmaz.','Kp = P(CO)² ÷ P(CO₂) = 9 ÷ 1,5 = 6')],
 tipId='de-kp',z='orta',alt='Kp ve Heterojen Denge',kaz='Katı içeren gaz dengesinde toplam basınç değişiminden kısmi basınçları bulup Kp değerini hesaplar.',kalip='şekilli',
 metin='Sabit hacimli kapalı bir kapta, yeterli miktarda C katısı ve CO₂ gazı bulunuyor. Sabit sıcaklıkta\nC(k) + CO₂(g) ⇌ 2CO(g)\ntepkimesi dengeye ulaşıyor. Kaptaki gaz basıncının başlangıçtaki ve dengedeki değerleri şekilde manometrelerle gösterilmiştir.\nBuna göre, tepkimenin bu sıcaklıktaki Kp değeri kaçtır?',
 sekil=SK,dogru=6,yan=[(m14[0],'P(CO)’nun üssünü 2 yerine 1 almış: 3 ÷ 1,5 = 2.','dikkat'),
  (m14[1],'CO₂’nin denge basıncı yerine başlangıç basıncını yazmış: 3² ÷ 3 = 3.','dikkat'),
  (m14[2],'CO₂’yi katı gibi yok sayıp ifadeye yazmamış: 3² = 9.','bilgi'),
  (m14[3],'CO’nun kısmi basıncı yerine toplam basıncı yazmış: 4,5² ÷ 1,5 = 13,5.','bilgi')],
 istenen='Tepkimenin Kp değeri.',ip=['Sabit hacimde basınç artışının, gaz mol sayısındaki hangi değişimden kaynaklandığını tepkime denkleminden çıkar.'],bilgi=[HETB],
 puf='Katı Kp ifadesine yazılmaz; sabit hacim ve sıcaklıkta toplam basınç artışı gaz mol sayısı artışını verir.')

# ================ 15 · zor · Kc ve denge mol → başlangıç mol
card(14,'Denge hesabı ve başlangıç miktarı','Kc ve bir denge miktarı bilindiğinde değişim tablosu geriye doğru kurulur; başlangıç = denge + tüketilen.','Hacme bölmeyi unutmak; denge miktarını başlangıç sanmak.','zor','hikâyeli',5,'de-ice','Kc ve denge bilgisinden başlangıç miktarı')
V15,Kc15,nHI=2,36,6
cHI=Fr(nHI,V15); prod=cHI**2/Kc15; assert prod==Fr(1,4)
cH=Fr(1,2); assert cH*cH==prod                      # [H2]=[I2]
nH_eq=cH*V15; tuk=Fr(nHI,2); a15=nH_eq+tuk
assert (nH_eq,tuk,a15)==(1,3,4) and Fr(nHI**2,V15**2)/((a15-tuk)/V15)**2==Kc15
m15=(nH_eq,a15/V15,tuk,cH); assert m15==(1,2,3,Fr(1,2))
q('0015',14,[A('Kc ifadesini yaz','Δn = 0 olduğundan hacim sadeleşse de derişimlerle çalışmak güvenlidir.','Kc = [HI]² ÷ ([H₂] × [I₂])'),
   A('HI derişimini bul','6 mol HI, 2 L kapta.','[HI] = 6 ÷ 2 = 3 mol/L'),
   A('H₂ derişimini bul','[H₂] = [I₂] olduğundan paydada [H₂]² vardır.','36 = 3² ÷ [H₂]² → [H₂] = 0,5 mol/L'),
   A('Denge ve tüketilen mol','H₂ denge molü, HI oluşumundan tüketilen H₂ molü.','n(H₂) = 0,5 × 2 = 1 mol · tüketilen = 6 ÷ 2 = 3 mol'),
   A('Başlangıcı bul','Başlangıç = denge + tüketilen.','1 + 3 = 4 mol')],
 tipId='de-ice',z='zor',alt='Denge Hesapları',kaz='Denge sabiti ve bir denge miktarından, tüketilen miktarı katsayılarla ilişkilendirerek başlangıç mol sayısını hesaplar.',kalip='hikâyeli',
 metin='2 L hacimli kapalı bir kaba eşit mol sayısında H₂ ve I₂ gazları konuluyor ve belirli bir sıcaklıkta\nH₂(g) + I₂(g) ⇌ 2HI(g)\ntepkimesi dengeye ulaşıyor. Bu sıcaklıkta Kc = 36 olup denge anında kapta 6 mol HI gazı bulunmaktadır.\nBuna göre, başlangıçta kaba konulan H₂ gazı kaç moldür?',
 dogru=4,yan=[(m15[0],'Denge anındaki H₂ mol sayısını (1 mol) başlangıç miktarı olarak yazmış.','dikkat'),
  (m15[1],'Başlangıç miktarını mol yerine derişim olarak bulmuş (4 ÷ 2 = 2 mol/L) ve hacimle çarpmayı unutmuş.','islem'),
  (m15[2],'Yalnız tüketilen H₂ miktarını (6 ÷ 2 = 3 mol) bulup denge miktarını eklememiş.','dikkat'),
  (m15[3],'Denge anındaki H₂ derişimini (0,5 mol/L) başlangıç mol sayısı olarak yazmış.','dikkat')],
 istenen='Başlangıçtaki H₂ gazının mol sayısı.',ip=['Önce Kc ifadesinden denge anındaki H₂ derişimini bul; sonra HI oluşumu için tüketilen miktarı ekle.'],bilgi=[ICEB],
 puf='Başlangıç = denge + tüketilen; tüketilen miktar ürün miktarından katsayı oranıyla bulunur.')

# ================ 16 · zor · piston, yeni denge toplam basıncı
card(15,'Hacim değişiminden sonra yeni denge','Hacim küçülünce kısmi basınçlar önce katlanır; Q ile K karşılaştırılıp denge kayması Kp’den hesaplanır.','Kaymayı hesaba katmamak; basıncın hacimden bağımsız olduğunu sanmak.','zor','şekilli',5,'de-ice','hacim değişiminden sonra yeni denge basıncı')
Pa,Pb=Fr(2),Fr(2); Kp16=Pb**2/Pa; assert Kp16==2
f16=2; Pa1,Pb1=f16*Pa,f16*Pb; Q16=Pb1**2/Pa1; assert Q16>Kp16
y16=Fr(-1,2); assert (Pb1+2*y16)**2==Kp16*(Pa1-y16)
Pa2,Pb2=Pa1-y16,Pb1+2*y16; Ptop=Pa2+Pb2; assert (Pa2,Pb2,Ptop)==(Fr(9,2),3,Fr(15,2))
m16=(Pb2,Pa+Pb,Pa2,f16*(Pa+Pb)); assert m16==(3,4,Fr(9,2),8)
o=piston(0,2.4,2.4,2.5,inside=('$\\mathrm{N_2O_4}$: 2 atm','$\\mathrm{NO_2}$: 2 atm'),vlab='$V$')+piston(4.4,1.2,2.4,2.5,inside=('yeni denge',),vlab='$V/2$',arrow=True)
o.append('\\node at (3.4,-.7) {\\ce{N2O4(g) <=> 2NO2(g)}};'); o.append('\\node[font=\\footnotesize] at (3.4,-1.25) {sabit sıcaklık};')
SK=tikz(o)
q('0016',15,[A('Kp değerini bul','İlk dengedeki kısmi basınçlarla Kp yazılır.','Kp = 2² ÷ 2 = 2'),
   A('Hacim yarıya inince','Sıcaklık sabit olduğundan basınçlar önce iki katına çıkar.','P(N₂O₄) = 4 atm · P(NO₂) = 4 atm'),
   A('Q ile Kp’yi karşılaştır','Q > Kp olduğundan denge N₂O₄ yönüne (geri) kayar.','Q = 4² ÷ 4 = 4 > 2'),
   A('Kaymayı hesapla','N₂O₄ y atm artarsa NO₂ 2y atm azalır.','(4 − 2y)² ÷ (4 + y) = 2 → y = 0,5'),
   A('Toplam basıncı bul','Yeni kısmi basınçlar toplanır.','P(N₂O₄) = 4,5 · P(NO₂) = 3 → 7,5 atm')],
 tipId='de-ice',z='zor',alt='Denge Hesapları',kaz='Hacim değişiminden sonra kısmi basınçların önce değiştiğini, ardından Kp değerine göre kaymayı hesaplayarak yeni toplam basıncı bulur.',kalip='şekilli',
 metin='Sabit sıcaklıkta, sürtünmesiz hareketli pistonlu bir kapta\nN₂O₄(g) ⇌ 2NO₂(g)\ntepkimesi dengededir. Dengedeki gazların kısmi basınçları şekilde verilmiştir. Piston itilerek hacim yarıya düşürülüyor ve sistem yeniden dengeye geliyor.\nBuna göre, yeni dengede kaptaki toplam gaz basıncı kaç atm’dir?',
 sekil=SK,dogru=Ptop,yan=[(m16[0],'Yalnız NO₂’nin kısmi basıncını (3 atm) sormuş gibi yanıtlamış.','dikkat'),
  (m16[1],'Hacim yarıya inse de gaz miktarı ve sıcaklık sabit olduğundan basıncın değişmediğini düşünmüş: 2 + 2 = 4 atm.','bilgi'),
  (m16[2],'Yalnız N₂O₄’ün kısmi basıncını (4,5 atm) toplam basınç sanmış.','dikkat'),
  (m16[3],'Basınçların iki katına çıktığını (8 atm) bulmuş ama denge kaymasını hesaba katmamış.','bilgi')],
 istenen='Yeni dengede toplam basınç (atm).',ip=['Hacim küçülünce kısmi basınçlar önce ne olur; sonra denge hangi yöne ve ne kadar kayar, Kp sabitliğinden hesapla.'],bilgi=[KPB,LCB],
 puf='Kayma miktarı için ilk denge Kp’sini yaz; hacim değişince sıçrayan basınçlardan başlayıp yeni denkleme yerleştir.')

# ================ 17 · zor · Cl₂ ekleme, yeni denge mol
card(16,'Madde eklenince yeni denge','Kc sabit kalır; eklenen maddenin derişimi katlanır, değişim miktarı kareli denklemden bulunur.','Eklenen miktarı hacme bölmemek; Kc’yi eski değerinde tutmamak.','zor','şekilli',6,'de-ice','madde eklenince yeni denge hesabı')
V17=2; nPCl5,nPCl3,nCl2=4,2,2; ek=4
cP5,cP3,cC=Fr(nPCl5,V17),Fr(nPCl3,V17),Fr(nCl2,V17); Kc17=cP3*cC/cP5; assert Kc17==Fr(1,2)
zz=Fr(1,2); nc=cC+Fr(ek,V17); assert (cP3-zz)*(nc-zz)==Kc17*(cP5+zz)
mol17=(cP3-zz)*V17; assert mol17==1
m17=(Fr(nPCl3),cP3-zz,(cP5+zz),(cP5+zz)*V17); assert m17==(2,Fr(1,2),Fr(5,2),5)
SK=pg('width=6.2cm,height=4.4cm,ybar,bar width=14pt,axis lines=left,symbolic x coords={PCl5,PCl3,Cl2},xtick=data,xticklabels={$\\mathrm{PCl_5}$,$\\mathrm{PCl_3}$,$\\mathrm{Cl_2}$},ymin=0,ymax=5,ytick={0,1,2,3,4,5},ylabel={Mol sayısı},nodes near coords,every node near coord/.style={font=\\small},enlarge x limits=0.3,label style={font=\\small},tick label style={font=\\small}',
 '\\addplot[fill=gray!35,draw=black] coordinates {(PCl5,4) (PCl3,2) (Cl2,2)};')
q('0017',16,[A('İlk dengeyi derişime çevir','Mol sayıları 2 L’ye bölünür.','[PCl₅] = 2 · [PCl₃] = 1 · [Cl₂] = 1 mol/L'),
   A('Kc değerini bul','Sıcaklık sabit olduğundan yeni dengede de geçerli.','Kc = (1 × 1) ÷ 2 = 0,5'),
   A('Eklenen Cl₂’yi derişime çevir','4 mol Cl₂, 2 L’de 2 mol/L eder.','[Cl₂] = 1 + 2 = 3 mol/L (anlık)'),
   A('Kaymayı hesapla','Denge PCl₅ yönüne kayar; PCl₃ ve Cl₂’den x mol/L harcanır.','(1 − x)(3 − x) ÷ (2 + x) = 0,5 → x = 0,5'),
   A('PCl₃ mol sayısını bul','Yeni derişimi hacimle çarp.','[PCl₃] = 0,5 mol/L → 0,5 × 2 = 1 mol')],
 tipId='de-ice',z='zor',alt='Denge Hesapları',kaz='Dengedeki sisteme madde eklendiğinde Kc sabitliğinden yeni denge miktarlarını hesaplar.',kalip='şekilli',
 metin='Sabit sıcaklıkta 2 L hacimli kapalı bir kapta\nPCl₅(g) ⇌ PCl₃(g) + Cl₂(g)\ntepkimesi dengededir. Denge anındaki maddelerin mol sayıları grafikte verilmiştir. Kaba sabit sıcaklıkta 4 mol Cl₂ gazı ekleniyor ve sistem yeniden dengeye geliyor.\nBuna göre, yeni dengede kapta kaç mol PCl₃ gazı bulunur?',
 sekil=SK,dogru=1,yan=[(m17[0],'Denge kaymasını hesaba katmayıp PCl₃ mol sayısının değişmediğini (2 mol) düşünmüş.','bilgi'),
  (m17[1],'Yeni dengedeki PCl₃ derişimini (0,5 mol/L) mol sayısı olarak yazmış.','islem'),
  (m17[2],'PCl₅’in yeni derişimini (2,5 mol/L) PCl₃’ün mol sayısı sanmış.','dikkat'),
  (m17[3],'Sorulanı karıştırıp PCl₅’in yeni mol sayısını (2,5 × 2 = 5 mol) bulmuş.','dikkat')],
 istenen='Yeni dengedeki PCl₃ gazının mol sayısı.',ip=['Eklenen gazın derişimini hesaplayıp Kc’nin sıcaklık sabit olduğunda değişmeyeceğini kullan; kayma miktarı için bir bilinmeyen tanımla.'],bilgi=[ICEB],
 puf='Madde eklenince önce derişimi güncelle, sonra Kc’yi koruyacak kayma miktarını bul.')

# ================ 18 · zor · piston, heterojen Kp, öncüllü
card(17,'Heterojen denge ve hacim','Yalnız CO₂ gazı Kp ifadesinde yer alır: Kp = P(CO₂). Sabit T’de basınç sabit kalır, hacim değişince gaz mol sayısı değişir.','Hacim küçülünce basıncın artacağını sanmak; saf katı eklenince dengenin kaydığını düşünmek.','zor','şekilli',5,'de-le','heterojen dengede hacim etkisi')
Kp18=Fr(1,2)
def n_gas(V): return Kp18*V       # n=PV/RT (RT sabit ⇒ n ∝ V)
assert n_gas(2)==2*n_gas(1) and n_gas(Fr(1,2))==n_gas(1)/2
o=piston(0,2.4,2.4,2.6,inside=('$\\mathrm{CO_2}$: 0,5 atm',),vlab='$V$',solids=[(.2,1.0,.55,'$\\mathrm{CaCO_3}$'),(1.5,.9,.55,'$\\mathrm{CaO}$')])
o.append('\\node at (1.3,-.7) {\\ce{CaCO3(k) <=> CaO(k) + CO2(g)}};'); o.append('\\node[font=\\footnotesize] at (1.3,-1.25) {sabit sıcaklık};')
SK=tikz(o)
w18=onc([False,False,True],['Kp = P(CO₂) olduğundan sabit sıcaklıkta yeni dengede de CO₂ basıncı 0,5 atm’dir; hacim değişince basınç değil mol sayısı değişir','CaO saf katıdır; miktarı denge ifadesinde yer almaz ve dengeyi kaydırmaz, CO₂ mol sayısı değişmez','hacim iki katına çıkınca CaCO₃ ayrışarak CO₂ basıncını 0,5 atm’de tutar; n = PV ÷ RT olduğundan CO₂ mol sayısı artar'],0)
q('0018',17,[A('Kp ifadesini yaz','Katılar yazılmaz.','Kp = P(CO₂) = 0,5 atm (sabit T’de değişmez)'),
   A('I’i değerlendir','Hacim yarıya inince CO₂ basıncı yine 0,5 atm olur; fazla CO₂ CaCO₃ oluşturur.','I: yanlış'),
   A('II’yi değerlendir','Saf katı eklemek dengeyi kaydırmaz, CO₂ mol sayısı değişmez.','II: yanlış'),
   A('III’ü değerlendir','Hacim iki katına çıkarken basınç 0,5 atm kalır, n = PV ÷ RT iki katına çıkar.','III: doğru'),
   A('Sonuç','Yalnız III doğrudur.','Yalnız III')],
 tipId='de-le',z='zor',alt='Heterojen Denge',kaz='Katı–gaz dengesinde Kp ifadesinden yararlanarak hacim değişiminin ve katı eklenmesinin CO₂ basıncı ve mol sayısı üzerindeki etkisini belirler.',kalip='şekilli',
 metin='Sabit sıcaklıkta, sürtünmesiz hareketli pistonlu bir kapta yeterli miktarda CaCO₃(k) ve CaO(k) ile\nCaCO₃(k) ⇌ CaO(k) + CO₂(g)\ntepkimesi dengededir. Dengedeki CO₂ gazının basıncı şekilde verilmiştir.\nBuna göre, sabit sıcaklıkta,\nI. Piston itilerek hacim yarıya düşürülüp yeniden denge kurulduğunda CO₂ basıncı 1 atm olur.\nII. Hacim sabit tutulup kaba bir miktar CaO(k) eklenirse CO₂ mol sayısı azalır.\nIII. Piston çekilerek hacim iki katına çıkarılıp yeniden denge kurulduğunda CO₂ mol sayısı artar.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w18['dogru'],yan=w18['yan'],sira=w18['sira'],istenen='Doğru olan yargılar.',
 ip=['Bu denge için Kp ifadesini yazıp hangi niceliğin sabit sıcaklıkta sabit kaldığına bak.'],bilgi=[HETB,LCB],
 puf='Tek gaz içeren heterojen dengede basınç sabittir; hacim değişince değişen gaz mol sayısıdır.')

# ================ 19 · zor · enerji diyagramı + denge, öncüllü
card(18,'Enerji diyagramı ve denge','Ea(ileri) − Ea(geri) = ΔH; endotermik tepkimede sıcaklık artınca K artar; katalizör iki aktifleşme enerjisini eşit azaltır.','Katalizörün ΔH’yi ya da K’yi değiştirdiğini sanmak; endotermikte sıcaklık artışının ürünü azalttığını düşünmek.','zor','şekilli',5,'de-enerji','enerji diyagramı ve denge yorumu')
Er,Eg,Ep=20,80,50; Eaf=Eg-Er; Ear=Eg-Ep; dH=Ep-Er
assert (Eaf,Ear,dH)==(60,30,30) and Eaf-Ear==dH and dH>0
kat=10; assert (Eaf-kat)-(Ear-kat)==dH and Ear-kat==20
sc=.05
pts=f'(0,{Er*sc}) (1.0,{Er*sc}) (1.5,{Er*sc+.02}) (2.0,{Eg*sc-.05}) (2.4,{Eg*sc}) (2.8,{Eg*sc-.05}) (3.3,{Ep*sc+.1}) (3.8,{Ep*sc}) (5,{Ep*sc})'
o=[f'\\draw[->,thick] (0,0) -- (0,4.5) node[above] {{Potansiyel enerji (kJ)}};',f'\\draw[->,thick] (0,0) -- (5.4,0) node[right,font=\\small] {{Tepkime ilerlemesi}};',
   f'\\draw[thick] (0,{Er*sc}) -- (1.0,{Er*sc}) .. controls (1.9,{Er*sc}) and (1.6,{Eg*sc}) .. (2.4,{Eg*sc}) .. controls (3.2,{Eg*sc}) and (2.9,{Ep*sc}) .. (3.8,{Ep*sc}) -- (5,{Ep*sc});']
for e,t in ((Er,'20'),(Ep,'50'),(Eg,'80')):
    o.append(f'\\draw[dotted,gray] (0,{e*sc}) -- (5,{e*sc}); \\draw (-.08,{e*sc}) -- (.08,{e*sc}); \\node[anchor=east,font=\\small] at (-.1,{e*sc}) {{{t}}};')
o.append(f'\\node[above,font=\\small] at (.6,{Er*sc}) {{A(g)}};'); o.append(f'\\node[above,font=\\small] at (4.4,{Ep*sc}) {{B(g)}};')
SK=tikz(o)
w19=onc([False,True,True],['bu tepkime endotermiktir (ΔH = +30 kJ); sıcaklık artınca denge ürün yönüne kayar ve B miktarı artar','katalizör iki yöndeki aktifleşme enerjisini de aynı miktarda azaltır: 60 − 10 = 50 kJ ve 30 − 10 = 20 kJ olur','endotermik tepkimede sıcaklık azalınca Kc küçülür'],4)
q('0019',18,[A('Diyagramı oku','Girenler 20, geçiş hâli 80, ürünler 50 kJ düzeyinde.','Ea(ileri) = 80 − 20 = 60 kJ · Ea(geri) = 80 − 50 = 30 kJ'),
   A('Isı değişimini bul','ΔH = Ea(ileri) − Ea(geri) = ürünlerin enerjisi − girenlerin enerjisi.','ΔH = 50 − 20 = +30 kJ → endotermik'),
   A('I’i değerlendir','Endotermik tepkimede sıcaklık artınca denge ürün yönüne kayar.','I: yanlış'),
   A('II’yi değerlendir','Katalizör iki aktifleşme enerjisini eşit azaltır; geri tepkimenin Ea’sı 30 − 10 = 20 kJ olur.','II: doğru'),
   A('III’ü değerlendir','Endotermikte sıcaklık düşünce K küçülür.','III: doğru')],
 tipId='de-enerji',z='zor',alt='Enerji Diyagramı',kaz='Enerji diyagramından Ea ve ΔH değerlerini okuyarak sıcaklığın, katalizörün ve K’nın denge üzerindeki etkisini yorumlar.',kalip='şekilli',
 metin='A(g) ⇌ B(g) tepkimesinin potansiyel enerji – tepkime ilerlemesi diyagramı şekilde verilmiştir.\nBuna göre,\nI. Sabit hacimde sıcaklık artırılırsa dengedeki B miktarı azalır.\nII. Katalizör kullanılıp ileri tepkimenin aktifleşme enerjisi 10 kJ azaltılırsa geri tepkimenin aktifleşme enerjisi 20 kJ olur.\nIII. Sıcaklık düşürülürse tepkimenin denge sabiti (K) küçülür.\nyargılarından hangileri doğrudur?',
 sekil=SK,dogru=w19['dogru'],yan=w19['yan'],sira=w19['sira'],istenen='Doğru olan yargılar.',
 ip=['Diyagramdaki üç enerji düzeyini okuyup her yargıyı bu değerlerle sına.'],bilgi=[EDB,KTB],
 puf='Enerji diyagramı hem ΔH’yi hem sıcaklık etkisini hem de katalizör etkisini birlikte yorumlatır.')

# ================ 20 · zor · ayrışma yüzdesi → Kc → Kp
card(19,'Ayrışma yüzdesi, Kc ve Kp','Ayrışma yüzdesinden denge mol sayıları, derişimler, Kc ve Kp = Kc(RT)^Δn zinciri kurulur.','Hacme bölmemek; Δn ile RT’yi birlikte kullanmamak.','zor','hikâyeli',6,'de-kp','ayrışma yüzdesinden Kp hesabı')
V20,n0_,yuz=2,4,Fr(1,2)
d20=n0_*yuz; nSO3=n0_-d20; nSO2=d20; nO2=d20/2
cs3,cs2,co2=Fr(nSO3,V20),Fr(nSO2,V20),Fr(nO2,V20); Kc20=cs2**2*co2/cs3**2; assert (cs3,cs2,co2,Kc20)==(1,1,Fr(1,2),Fr(1,2))
RT=Fr(82,1000)*1000; assert RT==82; dn20=3-2; Kp20=Kc20*RT**dn20; assert Kp20==41
m20=(Kc20, Fr(nSO2**2*nO2,nSO3**2), Fr(nSO2**2*nO2,nSO3**2)*RT, Kc20*RT**2); assert m20==(Fr(1,2),1,82,3362)
q('0020',19,[A('Ayrışan ve kalan miktarı bul','%50 ayrışma: 4 mol SO₃’ün 2 molü ayrışır; katsayılar 2 : 2 : 1.','SO₃: 2 mol · SO₂: 2 mol · O₂: 1 mol'),
   A('Derişimlere çevir','Mol sayıları 2 L’ye bölünür.','[SO₃] = 1 · [SO₂] = 1 · [O₂] = 0,5 mol/L'),
   A('Kc değerini hesapla','Katsayılar üs olur.','Kc = [SO₂]² × [O₂] ÷ [SO₃]² = 0,5'),
   A('Δn’yi bul','Gaz mol sayısı değişimi: ürünlerde 3, girenlerde 2.','Δn = 3 − 2 = +1'),
   A('Kp’ye dönüştür','Kp = Kc × (RT)^Δn.','RT = 0,082 × 1000 = 82 → Kp = 0,5 × 82 = 41')],
 tipId='de-kp',z='zor',alt='Kp ile Kc İlişkisi',kaz='Ayrışma yüzdesinden denge derişimlerini ve Kc değerini bulup Kp = Kc(RT)^Δn bağıntısıyla Kp’yi hesaplar.',kalip='hikâyeli',
 metin='Sabit hacimli 2 L’lik kapalı bir kaba 4 mol SO₃ gazı konuluyor ve 1000 K sıcaklıkta\n2SO₃(g) ⇌ 2SO₂(g) + O₂(g)\ntepkimesine göre SO₃ gazının %50’si ayrışarak denge kuruluyor.\n(R = 0,082 L·atm/mol·K)\nBuna göre, tepkimenin 1000 K’deki Kp değeri kaçtır?',
 dogru=41,yan=[(m20[0],'Kc değerini (0,5) Kp olarak yazmış; Δn ve RT’yi hiç kullanmamış.','bilgi'),
  (m20[1],'Derişimler yerine mol sayılarını yazarak Kc’yi (2² × 1 ÷ 2² = 1) bulup Kp’ye çevirmeyi unutmuş.','islem'),
  (m20[2],'Kc’yi mol sayılarıyla (1) hesaplayıp (RT)¹ ile çarpmış: 1 × 82 = 82.','islem'),
  (m20[3],'Δn’yi 1 yerine 2 alarak Kp = 0,5 × 82² = 3362 bulmuş.','bilgi')],
 istenen='Tepkimenin 1000 K’deki Kp değeri.',ip=['Önce ayrışan miktarla denge derişimlerini bul; Kc’den Kp’ye geçerken gazların mol sayısındaki değişime dikkat et.'],bilgi=[KPKC,ICEB],
 puf='Kp’ye gitmeden önce Kc’yi derişimle hesapla; Δn ile RT, dönüşümün tek anahtarıdır.')

# ================ yaz
for qq in P.ANA: qq['kardes']=None
SC='/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/denge'; os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'denge-1.json'),os.path.join(SC,'bos-denge.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu='akim|Kimyasal Tepkimelerde Denge'))['kartlar'].append(c['id'])
json.dump(dict(konu='Kimyasal Tepkimelerde Denge',surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2020–2026 Kimya (yalnız mantık), MEB 12. sınıf kimya.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','akdenge.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
