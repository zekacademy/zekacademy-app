"""AYT Kimya · Kimyasal Tepkimelerde Enerji · 20 soru (kardeş yok, ipucu 1).
Tüm sayısal cevap ve çeldirici değerleri Fraction ile hesaplanır, assert edilir; öncüllerin doğruluğu tek yerde (stm) tanımlanır."""
import sys,os,math,json
AD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(AD,'..','tyt-kim'))
import _hafif_kim2 as H
from _hafif_kim2 import *
KONU_='Kimyasal Tepkimelerde Enerji'; UK='akim|Kimyasal Tepkimelerde Enerji'
H.KONU=KONU_
P=Parti('tepenerji',KONU_,UK,ders='AYT Kimya',idon='aytkim')
KY='ÖSYM 2019–2026 AYT Kimya (yalnız mantık) · MEB 11. sınıf Kimyasal Tepkimelerde Enerji'
# ---------------- kartlar ----------------
kart('K-AKTE-01','Oluşum entalpisi tanımı','Standart oluşum entalpisi, 1 mol bileşiğin kararlı elementlerinden oluşma entalpisidir; ürün mol sayısı 1, girenler kararlı elementlerdir.','Ürün mol sayısına bakmamak; girenlerin element olmasını yeterli görmek; kararlı hâli (grafit, H₂ gibi) atlamak.','kolay','öncüllü',2,'tep-olusum','Oluşum entalpisi',KY)
kart('K-AKTE-02','Oluşum entalpilerinden tepkime entalpisi','ΔH° = Σn·ΔHf°(ürünler) − Σn·ΔHf°(girenler); elementlerin oluşum entalpisi sıfırdır, katsayılar mol sayısıyla çarpılır.','Katsayıları unutmak; ürün−giren sırasını ters yazmak; elementi sıfır saymamak.','orta','tablo',3,'tep-olusum','Oluşum entalpisi',KY)
kart('K-AKTE-03','Ekzotermik ve endotermik tepkimeler','ΔH işareti ısı alışverişini; potansiyel enerji farkı ΔH’ı belirler. Tepkime ters çevrilirse ΔH işaret değiştirir, katsayılarla orantılı değişir.','İşareti ısı alınıp verilmesiyle karıştırmak; katsayı değişince ΔH’ı sabit tutmak.','orta','düz',2,'tep-kavram','Entalpi kavramları',KY)
kart('K-AKTE-04','Potansiyel enerji diyagramı okuma','İleri aktivasyon enerjisi = tepe − giren; geri aktivasyon enerjisi = tepe − ürün; ΔH = ürün − giren.','Tepe enerjisini aktivasyon enerjisi sanmak; geri tepkimede ürün düzeyi yerine giren düzeyini kullanmak.','kolay','grafik',2,'tep-pe','Potansiyel enerji diyagramı',KY)
kart('K-AKTE-05','Katalizör ve çok basamaklı diyagram','Katalizör aktivasyon enerjisini (ileri ve geri) azaltır, ΔH’ı değiştirmez. Çok basamaklı tepkimede ΔH uç düzeylerin farkıdır; en yüksek aktivasyon enerjili basamak yavaştır.','Katalizörün ΔH’ı değiştirdiğini sanmak; basamak farkını toplam ΔH sanmak.','zor','grafik',4,'tep-pe','Potansiyel enerji diyagramı',KY)
kart('K-AKTE-06','Hess yasası','Entalpi değişimi yoldan bağımsızdır; tepkime ters yazılırsa ΔH’ın işareti değişir, katsayıyla çarpılırsa ΔH de çarpılır, tepkimeler toplanırsa ΔH’lar toplanır.','Ters yazarken işareti değiştirmemek; katsayıyı ΔH’a yansıtmamak; basamakları yanlış toplamak.','orta','düz',3,'tep-hess','Hess yasası',KY)
kart('K-AKTE-07','Bağ enerjisi ile tepkime entalpisi','ΔH ≈ Σ(kırılan bağ enerjileri) − Σ(oluşan bağ enerjileri); yapı formülünden bağ sayıları, katsayılarla birlikte sayılır.','Katsayı ile bağ sayısını çarpmamak; kırılan–oluşan farkını ters almak.','orta','şekilli',4,'tep-bag','Bağ enerjisi ve ΔH',KY)
kart('K-AKTE-08','Kalorimetri ve ısı hesabı','q = m·c·ΔT; açığa çıkan ısı mol sayısına bölünerek molar entalpi, tepkime ΔH’ına oranlanarak miktar bulunur.','J ile kJ’yi karıştırmak; ısıyı mol sayısına bölmemek; verimi yanlış uygulamak.','orta','şekilli',4,'tep-kalori','Kalorimetri ve ısı miktarı',KY)
kart('K-AKTE-09','Hess yasası ve stokiyometri','Hess yasasıyla bulunan ΔH, mol sayısı ve kütle ile ilişkilendirilir; ısı miktarı ΔH × (mol/katsayı) kadardır.','ΔH’ı 1 mol maddeye ait sanmak; katsayıyı mole çevirmemek.','zor','şekilli',5,'tep-hess','Hess yasası',KY)
CARD={c['id']:c for c in H.KARTLAR}
def kk(n,ne): c=CARD[f'K-AKTE-{n}']; return f'K-AKTE-{n} ({c["alt"].lower()}) · {ne}'
def q(no,n,ad,**k):
    assert len(k['ip'])==1 and 3<=len(ad)<=7
    c=CARD[f'K-AKTE-{n}']
    mk(P,no,ad=ad,adim=len(ad),tipId=c['tipId'],tip=c['tip'],kart=kk(n,k.pop('ne')),**k)
RM='I II III'.split()
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
NAMES={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def onc(no,n,bag,stm,secenek,tail,ne,**k):
    """stm: (metin, doğru_mu, açıklama, yanlışı_doğru_sanma_hatası, doğruyu_yanlış_sanma_hatası)."""
    truth={i for i,s in enumerate(stm) if s[1]}
    dogru=[a for a in secenek if NAMES[a]==truth]; assert len(dogru)==1 and len(secenek)==5 and len(set(secenek))==5
    assert [ORD.index(a) for a in secenek]==sorted(ORD.index(a) for a in secenek),'şık sırası'
    dogru=dogru[0]; yan=[]
    for a in secenek:
        if a==dogru: continue
        S=NAMES[a]; parts=[]
        for i in sorted(S^truth):
            parts.append(f'{RM[i]}. ifadeyi doğru saymış; {stm[i][3]}' if i in S else f'{RM[i]}. ifadeyi yanlış saymış; {stm[i][4]}')
        yan.append((a,' '.join(parts),'bilgi'))
    metin=bag+'\n'+'\n'.join(f'{RM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+tail
    ad=[A(f'{RM[i]}. ifadeyi değerlendir',s[2],f'{RM[i]}: {"doğru" if s[1] else "yanlış"}') for i,s in enumerate(stm)]
    ad.append(A('Sonucu birleştir','Doğru bulunan ifadeler birlikte seçilir.',dogru))
    q(no,n,ad,ne=ne,metin=metin,dogru=dogru,sira=list(secenek),yan=yan,**k)
def tek(S):
    """S: (şık metni, doğru_mu, hata cümlesi). Tek doğru şık assert edilir."""
    assert sum(1 for s in S if s[1])==1
    d=[s for s in S if s[1]][0]
    return d[0],[(s[0],s[2],'bilgi') for s in S if not s[1]]
# ---------------- şekil yardımcıları ----------------
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def pe_fig(curves,ticks,labels,sc=.04,xn=None,legend=None):
    """curves: [(nodes,stil)], nodes=[(düzey,'p'|'t'|'v')]; ticks: eksende yazılacak değerler; labels: {düğüm_no:(metin,'a'|'b')} ilk eğri için."""
    g=''; n=len(curves[0][0]); xs=[1.0+1.75*i for i in range(n)]; top=max(l for nd,_ in curves for l,_ in nd)
    wd={'p':.4,'v':.25,'t':0}
    for nodes,stil in curves:
        path=''; 
        for i,(L,kd) in enumerate(nodes):
            x=xs[i]; s=(x-wd[kd],L*sc); e=(x+wd[kd],L*sc)
            if i==0: path+=f'({s[0]:.3f},{s[1]:.3f}) '
            else:
                dx=(s[0]-prev[0])*.5; path+=f'.. controls ({prev[0]+dx:.3f},{prev[1]:.3f}) and ({s[0]-dx:.3f},{s[1]:.3f}) .. ({s[0]:.3f},{s[1]:.3f}) '
            if wd[kd]>0: path+=f'-- ({e[0]:.3f},{e[1]:.3f}) '
            prev=e
        g+=f'\\draw[{stil}] {path};'
    xmax=xs[-1]+.8
    g+=f'\\draw[{ARR},thick] (0,0) -- (0,{top*sc+.6:.3f}); \\draw[{ARR},thick] (0,0) -- ({xmax+.2:.3f},0);'
    g+=f'\\node[rotate=90] at (-1.0,{top*sc/2+.3:.3f}) {{Potansiyel enerji (kJ)}};\\node[below] at ({xmax/2:.3f},-.05) {{Tepkime koordinatı}};'
    for v in ticks:
        xt=None
        for nodes,_ in curves:
            for i,(L,kd) in enumerate(nodes):
                if L==v and xt is None: xt=xs[i]-wd[kd]
        assert xt is not None,v
        g+=f'\\draw[dashed,gray] (0,{v*sc:.3f}) -- ({xt:.3f},{v*sc:.3f}); \\draw (0,{v*sc:.3f}) -- (-.08,{v*sc:.3f}); \\node[left,inner sep=2pt] at (-.05,{v*sc:.3f}) {{{v}}};'
    nodes0=curves[0][0]
    for i,(t,pos) in labels.items():
        L=nodes0[i][0]
        if pos=='a': g+=f'\\node[above] at ({xs[i]:.3f},{L*sc+.02:.3f}) {{{t}}};'
        else: g+=f'\\node[below] at ({xs[i]:.3f},{L*sc-.02:.3f}) {{{t}}};'
    if legend:
        lx=xmax-1.9; ly=top*sc-.1
        g+=f'\\draw[thick] ({lx},{ly}) -- ({lx+.6},{ly}); \\node[right] at ({lx+.65},{ly}) {{\\footnotesize Katalizörsüz}}; \\draw[thick,dashed,vurgu] ({lx},{ly-.45}) -- ({lx+.6},{ly-.45}); \\node[right] at ({lx+.65},{ly-.45}) {{\\footnotesize Katalizörlü}};'
    return tk(g)
def ladder(levels,arrows,sc,W=8.2,note=True):
    """levels: (y,metin,'a'|'b',x0); arrows: (x,y1,y2,etiket,oran)."""
    g=''
    for y,t,pos,x0 in levels:
        g+=f'\\draw[thick] ({x0},{y*sc:.3f}) -- ({W},{y*sc:.3f});'
        g+=(f'\\node[above left,inner sep=2pt] at ({W},{y*sc:.3f}) {{{t}}};' if pos=='a' else f'\\node[below left,inner sep=2pt] at ({W},{y*sc:.3f}) {{{t}}};')
    for x,y1,y2,lab,fr in arrows:
        g+=f'\\draw[vurgu,very thick,{ARR}] ({x},{y1*sc:.3f}) -- ({x},{y2*sc:.3f}); \\node[right,inner sep=3pt] at ({x},{(y1+(y2-y1)*fr)*sc:.3f}) {{{lab}}};'
    if note: g+=f'\\node[below,gray] at ({W/2},{min(y for y,_,_,_ in levels)*sc-.55:.3f}) {{\\footnotesize Şekil ölçekli değildir.}};'
    return tk(g)
def bond(x1,x2,y,n=1,gap=.07):
    return ''.join(f'\\draw[thick] ({x1},{y+(i-(n-1)/2)*gap*2:.3f}) -- ({x2},{y+(i-(n-1)/2)*gap*2:.3f});' for i in range(n))
def at(x,y,t): return f'\\node at ({x},{y}) {{{t}}};'
def tablo_tikz(x,y,baslik,satir):
    cols='l'+'r'*(len(baslik)-1)
    body=' & '.join(baslik)+'\\\\ \\hline '+'\\\\ '.join(' & '.join(r) for r in satir)
    return f'\\node[draw,inner sep=4pt] at ({x},{y}) {{\\small\\begin{{tabular}}{{{cols}}}{body}\\end{{tabular}}}};'
def sira_say(vals): return sorted(vals)
def fmk(x): return fm(x)

# =============== 0001 · oluşum entalpisi tanımı · kolay · öncüllü ===============
onc('0001','01','Standart koşullarda gerçekleşen aşağıdaki tepkimelerin standart entalpi değişimleri ayrı ayrı ölçülmüştür.',
 [('½H₂(g) + ½Cl₂(g) → HCl(g)',True,'Kararlı elementlerden 1 mol HCl oluşuyor; kesirli katsayı bu durumu bozmaz.','—','kesirli katsayılı yazımın oluşum tepkimesi olamayacağını sanmış.'),
  ('N₂(g) + O₂(g) → 2NO(g)',False,'Tepkimede 2 mol NO oluşuyor; oluşum entalpisi 1 mol bileşik için tanımlıdır.','girenlerin element olmasını yeterli görüp oluşan mol sayısına bakmamış.','—'),
  ('2C(grafit) + 2H₂(g) → C₂H₄(g)',True,'Kararlı hâldeki elementlerden (grafit ve H₂) 1 mol C₂H₄ oluşuyor.','—','katsayıların 2 olmasından ürünün de 2 mol olduğunu sanmış.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','II ve III'],'Buna göre bu tepkimelerden hangilerinin standart entalpi değişimi, oluşan bileşiğin standart oluşum entalpisine eşittir?',
 ne='üç tepkimenin oluşum tepkimesi olup olmadığı',z='kolay',alt='Oluşum Entalpisi',kaz='Bir tepkimenin standart oluşum tepkimesi olup olmadığını ürün mol sayısı ve kararlı elementlere göre belirler.',kalip='öncüllü',
 istenen='ΔH°’ı oluşum entalpisine eşit olan tepkimeler.',
 ip=['Her tepkimede girenlerin ne olduğuna ve ürünün kaç mol oluştuğuna bak.'],
 bilgi=[B('Standart oluşum entalpisi','bir bileşiğin 1 molünün, standart koşullarda en kararlı hâldeki elementlerinden oluşması sırasındaki entalpi değişimidir. Örnek: C(grafit) + 2S(rombik) → CS₂(s) tepkimesinin ΔH°’ı CS₂(s)’nin oluşum entalpisidir')],
 puf='Oluşum tepkimesinde girenler kararlı elementlerdir ve ürün bileşikten tam 1 mol oluşur.')

# =============== 0002 · PE diyagramı · kolay · grafik ===============
R2,T2,P2=20,90,60
ea_i=T2-R2; dH=P2-R2; ea_g=T2-P2; assert (ea_i,dH,ea_g)==(70,40,30) and len({R2,T2,P2,ea_i,dH,ea_g})==6
SK=pe_fig([([(R2,'p'),(T2,'t'),(P2,'p')],'thick,vurgu')],[R2,P2,T2],{0:('X$_2$ + Y$_2$','a'),2:('2XY','a')})
q('0002','04',[A('Diyagramı oku','Girenler 20, ürünler 60, tepe noktası 90 kJ düzeyindedir.','giren: 20 · ürün: 60 · tepe: 90'),
 A('Ters tepkimeyi düşün','Ters tepkimede başlangıç düzeyi ürünlerin düzeyidir.','başlangıç: 2XY (60 kJ)'),
 A('Aktivasyon enerjisini bul','Aktivasyon enerjisi, tepe ile başlangıç düzeyi arasındaki farktır.','Ea(geri) = 90 − 60 = 30 kJ')],
 ne='X₂ + Y₂ → 2XY diyagramı, geri tepkimenin Ea’sı',metin='Şekilde, X₂(g) + Y₂(g) → 2XY(g) tepkimesinin potansiyel enerji–tepkime koordinatı diyagramı verilmiştir.\nBuna göre 2XY(g) → X₂(g) + Y₂(g) tepkimesinin aktivasyon enerjisi kaç kJ’dir?',
 dogru=ea_g,yan=[(dH,'İleri tepkimenin entalpi değişimini (60 − 20 = 40 kJ) geri tepkimenin aktivasyon enerjisi sanmış.','dikkat'),(P2,'Ürünlerin potansiyel enerjisini (60 kJ) aktivasyon enerjisi sanmış.','dikkat'),(ea_i,'İleri tepkimenin aktivasyon enerjisini (90 − 20 = 70 kJ) bulmuş; geri tepkimenin başlangıcının ürünler olduğunu görmemiş.','bilgi'),(T2,'Tepe noktasının enerjisini (90 kJ) aktivasyon enerjisi sanmış.','bilgi')],
 z='kolay',alt='Potansiyel Enerji Diyagramı',kaz='Potansiyel enerji diyagramından geri tepkimenin aktivasyon enerjisini bulur.',kalip='grafik',sekil=SK,
 istenen='Geri tepkimenin aktivasyon enerjisi (kJ).',
 ip=['Geri tepkime ürünlerden başlar; tepe noktasına çıkmak için gereken enerjiyi düşün.'],
 bilgi=[B('Aktivasyon enerjisi','tepkimenin başlayabilmesi için girenlerin aşması gereken enerji engelidir. Örnek: giren 10 kJ, tepe 50 kJ ise ileri aktivasyon enerjisi 40 kJ’dir')],
 puf='Geri tepkimenin aktivasyon enerjisi = tepe − ürün düzeyi.')

# =============== 0003 · ısı–mol–kütle · kolay ===============
dH3=Fr(-572); n3=Fr(27,18); assert n3==Fr(3,2); q3=-dH3/2*n3; assert q3==429
yn=[(Fr(286),'Tepkime denklemindeki 2 mol H₂O için verilen ısıyı 1 mole bölmüş ama mol sayısıyla (1,5) çarpmamış.','dikkat'),(-dH3,'Tepkimenin tamamı için verilen ısıyı (572 kJ) değiştirmeden yazmış; 27 g’ın 1,5 mol olduğunu hesaba katmamış.','dikkat'),(-dH3*n3,'1,5 mol suyu 2 mol’lük tepkimeyle doğrudan çarpmış (1,5 × 572); katsayıyı hesaba katmamış.','islem'),(-dH3/2*n3/2,'Hem katsayıya hem de mol sayısına birer kez daha bölmüş (1,5 ÷ 2 × 286).','islem')]
assert [float(v) for v,_,_ in yn]==[286,572,858,214.5]
q('0003','08',[A('Mol sayısını bul','Su, mol kütlesi 18 g/mol olan bir maddedir.','n = 27 ÷ 18 = 1,5 mol'),
 A('1 mol için ısıyı bul','Verilen ΔH, tepkimede oluşan 2 mol H₂O içindir.','572 ÷ 2 = 286 kJ/mol'),
 A('Toplam ısıyı hesapla','Açığa çıkan ısı mol sayısıyla orantılıdır.','286 × 1,5 = 429 kJ')],
 ne='27 g H₂O(s) oluşurken açığa çıkan ısı',metin='2H₂(g) + O₂(g) → 2H₂O(s)    ΔH = −572 kJ\n(H: 1, O: 16)\nBu tepkimeye göre 27 g H₂O(s) oluşurken açığa çıkan ısı kaç kJ’dir?',
 dogru=q3,yan=yn,z='kolay',alt='Tepkime Isısı',kaz='Verilen ΔH değerinden belirli kütledeki ürün için açığa çıkan ısıyı hesaplar.',kalip='düz',
 istenen='27 g H₂O(s) oluşurken açığa çıkan ısı (kJ).',
 ip=['ΔH değerinin kaç mol su için verildiğine dikkat et.'],
 bilgi=[B('Tepkime ısısı ve mol','ΔH, denklemdeki katsayılara göre oluşan ya da harcanan madde miktarı içindir; farklı miktarda ısı için orantı kurulur. Örnek: 4 mol maddeye −80 kJ veriliyorsa 1 mol maddeye −20 kJ düşer')],
 puf='ΔH’ı önce 1 mole indir, sonra mol sayısıyla çarp.')

# =============== 0004 · ΔHf tablo → yanma ΔH · orta · tablo ===============
hf4={'C₃H₈(g)':-104,'CO₂(g)':-394,'H₂O(s)':-286}
dH4=3*hf4['CO₂(g)']+4*hf4['H₂O(s)']-hf4['C₃H₈(g)']; assert dH4==-2222
SK=tablo_svg(['Madde','Standart oluşum entalpisi (kJ/mol)'],[[k,fm(v)] for k,v in hf4.items()])
d1=hf4['CO₂(g)']+hf4['H₂O(s)']-hf4['C₃H₈(g)']; d2=3*hf4['CO₂(g)']+4*hf4['H₂O(s)']; d3=-dH4; d4=3*hf4['CO₂(g)']+hf4['H₂O(s)']-hf4['C₃H₈(g)']
assert (d1,d2,d3,d4)==(-576,-2326,2222,-1364)
q('0004','02',[A('Formülü yaz','ΔH°, ürünlerin oluşum entalpileri toplamından girenlerinkinin çıkarılmasıyla bulunur; O₂ element olduğundan sıfırdır.','ΔH° = Σn·ΔHf(ürün) − Σn·ΔHf(giren)'),
 A('Ürünleri hesapla','Her oluşum entalpisi katsayısıyla çarpılır.','3 × (−394) + 4 × (−286) = −2326'),
 A('Girenleri çıkar','Girenlerde yalnız C₃H₈ sıfırdan farklıdır.','−2326 − (−104) = −2222 kJ')],
 ne='propanın yanma tepkimesinin ΔH°’ı',metin='Aşağıdaki tabloda bazı maddelerin 25 °C’deki standart oluşum entalpileri verilmiştir.\nBuna göre C₃H₈(g) + 5O₂(g) → 3CO₂(g) + 4H₂O(s) tepkimesinin standart entalpi değişimi kaç kJ’dir?',
 dogru=dH4,yan=[(d1,'Ürünlerin oluşum entalpilerini katsayılarıyla çarpmadan toplamış (−394 − 286 + 104).','dikkat'),(d2,'Girenlerin oluşum entalpisini (C₃H₈ için −104 kJ) çıkarmayı unutmuş.','dikkat'),(d3,'Girenler − ürünler biçiminde çıkarmış; ΔH’ın işaretini ters bulmuş.','bilgi'),(d4,'Katsayıyı yalnız CO₂’e uygulamış (3 × (−394) − 286 + 104).','islem')],
 z='orta',alt='Oluşum Entalpisinden Tepkime Entalpisi',kaz='Standart oluşum entalpilerinden tepkime entalpisini hesaplar.',kalip='tablo',sekil=SK,
 istenen='Tepkimenin standart entalpi değişimi (kJ).',
 ip=['Ürünlerin ve girenlerin oluşum entalpilerini katsayılarıyla çarpıp topla; elementlerin değerini düşün.'],
 bilgi=[B('Oluşum entalpisinden ΔH','ΔH° = ürünlerin Σn·ΔHf° − girenlerin Σn·ΔHf°; kararlı elementlerin ΔHf° değeri sıfırdır. Örnek: 2A + B → 3C için ΔH° = 3·ΔHf(C) − 2·ΔHf(A) − ΔHf(B)')],
 puf='Önce ürünler toplamı, sonra girenler toplamı; fark her zaman ürün − giren.')

# =============== 0005 · katalizör · orta · öncüllü · PE ===============
R5,T5u,T5c,P5=50,130,100,20
assert P5-R5==-30 and T5u-R5==80 and T5c-R5==50 and T5c-P5==80 and T5u-P5==110
SK=pe_fig([([(R5,'p'),(T5u,'t'),(P5,'p')],'thick'),([(R5,'p'),(T5c,'t'),(P5,'p')],'thick,dashed,vurgu')],[P5,R5,T5c,T5u],{0:('Girenler','a'),2:('Ürünler','a')},
 legend=True)
onc('0005','05','Şekilde, ısı veren bir tepkimenin katalizörsüz (düz çizgi) ve katalizörlü (kesikli çizgi) gerçekleşme yolları potansiyel enerji–tepkime koordinatı diyagramında gösterilmiştir.',
 [('Katalizör kullanılsa da kullanılmasa da tepkimenin entalpi değişimi −30 kJ’dir.',True,'ΔH, girenlerle ürünlerin enerji farkıdır (20 − 50 = −30 kJ); katalizör yalnız tepe noktasını düşürür.','—','katalizörün ΔH’ı da değiştirdiğini düşünmüş.'),
  ('Katalizör, geri tepkimenin aktivasyon enerjisini değiştirmez.',False,'Tepe noktası düştüğü için geri tepkimenin aktivasyon enerjisi de azalır (110 kJ’den 80 kJ’e).','katalizörün yalnız ileri tepkimeyi etkilediğini sanmış.','—'),
  ('Katalizörlü yolda ileri tepkimenin aktivasyon enerjisi 80 kJ’dir.',False,'Katalizörlü yolda ileri aktivasyon enerjisi 100 − 50 = 50 kJ’dir; 80 kJ katalizörsüz yoldaki değerdir.','katalizörsüz yolun aktivasyon enerjisini (130 − 50 = 80 kJ) katalizörlü yola ait sanmış.','—')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve III','II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='katalizörün diyagramdaki etkisi',z='orta',alt='Potansiyel Enerji Diyagramı',kaz='Katalizörlü ve katalizörsüz diyagramı karşılaştırarak ΔH ve aktivasyon enerjilerini yorumlar.',kalip='öncüllü',sekil=SK,
 istenen='Doğru ifadeler.',
 ip=['Katalizörlü ve katalizörsüz yolların hangi düzeylerde birleştiğine bak.'],
 bilgi=[B('Katalizör','tepkimeye girip kendisi sonunda değişmeden kalan ve tepkimeye daha düşük enerjili bir yol sağlayan maddedir; girenlerin ve ürünlerin enerjisi bu nedenle değişmez')],
 puf='Diyagramda giren, ürün ve tepe düzeylerini ayrı ayrı oku; her ifadeyi bu düzeylerle sına.')

# =============== 0006 · Hess şeması SO3 · orta · öncüllü ===============
dA,dB=-396,-297; dC=dA-dB; assert dC==-99 and 2*dC==-198
SK=ladder([(0,'S(k) + 3/2 O$_2$(g)','a',0),(-62,'SO$_2$(g) + 1/2 O$_2$(g)','a',2.3),(-100,'SO$_3$(g)','b',0)],[(.6,0,-100,'$\\Delta H=-396$ kJ',.2),(3.3,0,-62,'$\\Delta H=-297$ kJ',.5),(5.6,-62,-100,'$\\Delta H=?$',.5)],.052)
onc('0006','06','Şekilde, kükürdün (S) oksijenle SO₃(g) oluşturması iki farklı yoldan gösterilmiş ve iki yoldaki entalpi değişimlerinden bazıları verilmiştir.',
 [('2SO₂(g) + O₂(g) → 2SO₃(g) tepkimesinin entalpi değişimi −99 kJ’dir.',False,'1 mol SO₃ için entalpi değişimi −99 kJ’dir; denklemde 2 mol SO₃ oluştuğundan ΔH = −198 kJ olur.','katsayıyı ΔH’a yansıtmayı unutmuş.','—'),
  ('SO₃(g)’ün standart oluşum entalpisi −396 kJ/mol’dür.',True,'Kararlı elementlerden (S(k) ve O₂) 1 mol SO₃ oluşurken ΔH = −396 kJ’dir.','—','oluşum entalpisinin şekildeki toplam basamaktan okunacağını görmemiş.'),
  ('SO₃(g) → SO₂(g) + ½O₂(g) tepkimesi ekzotermiktir.',False,'Bu tepkime SO₂ + ½O₂ → SO₃’ün tersidir; ΔH = +99 kJ olduğundan endotermiktir.','ters tepkimede ΔH’ın işaretinin değiştiğini görmemiş.','—')],
 ['Yalnız II','Yalnız III','I ve II','I ve III','II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='SO₃ oluşumunun Hess şeması',z='orta',alt='Hess Yasası',kaz='Hess yasasıyla eksik entalpi değişimini bulup tepkime ve oluşum entalpisi ifadelerini değerlendirir.',kalip='öncüllü',sekil=SK,
 istenen='Doğru ifadeler.',
 ip=['Şekilde iki yolun aynı başlangıçtan aynı ürüne vardığına dikkat et.'],
 bilgi=[B('Hess yasası','bir tepkimenin entalpi değişimi izlenen yoldan bağımsızdır; basamakların ΔH’ları toplamı doğrudan yolun ΔH’ına eşittir. Örnek: A → B → C için ΔH(A→C) = ΔH(A→B) + ΔH(B→C)')],
 puf='Doğrudan yol = basamakların toplamı; ters yönde ΔH’ın işareti değişir.')

# =============== 0007 · bağ enerjisi N2+3H2 · orta · şekil ===============
E7={'N≡N':946,'H–H':436,'N–H':391}
kir=E7['N≡N']+3*E7['H–H']; olu=6*E7['N–H']; dH7=kir-olu; assert (kir,olu,dH7)==(2254,2346,-92)
w1=E7['N≡N']+E7['H–H']-olu; w2=Fr(dH7,2); w3=-dH7; w4=kir-3*E7['N–H']
assert (w1,w2,w3,w4)==(-964,-46,92,1081)
g=at(0,0,'N')+at(1.3,0,'N')+bond(.2,1.1,0,3)+at(2.1,0,'+')+at(2.65,0,'3')+at(3.2,0,'H')+at(4.2,0,'H')+bond(3.45,3.95,0)
g+=f'\\draw[{ARR},thick] (4.8,0) -- (5.5,0);'+at(5.95,0,'2')
for cx in [7.2]:
    g+=at(cx,0,'N')+at(cx,1.0,'H')+at(cx-.85,-.6,'H')+at(cx+.85,-.6,'H')
    g+=f'\\draw[thick] ({cx},.22) -- ({cx},.72); \\draw[thick] ({cx-.2},-.15) -- ({cx-.62},-.4); \\draw[thick] ({cx+.2},-.15) -- ({cx+.62},-.4);'
g+=tablo_tikz(4.1,-2.5,['Bağ','Enerji (kJ/mol)'],[['N$\\equiv$N','946'],['H--H','436'],['N--H','391']])
SK=tk(g)
q('0007','07',[A('Kırılan bağları say','1 mol N≡N ve 3 mol H–H bağı kırılır.','946 + 3 × 436 = 2254 kJ'),
 A('Oluşan bağları say','2 mol NH₃’ün her molekülünde 3 tane N–H bağı vardır; toplam 6 mol N–H oluşur.','6 × 391 = 2346 kJ'),
 A('Farkı al','Kırılan bağların enerjisinden oluşanlarınki çıkarılır.','ΔH = 2254 − 2346 = −92 kJ')],
 ne='N₂ + 3H₂ → 2NH₃ tepkimesinin ΔH’ı',metin='Şekilde, N₂(g) ile H₂(g)’nin tepkimesinden NH₃(g) oluşumu yapı formülleriyle ve ilgili bağ enerjileriyle verilmiştir.\nBuna göre bu tepkimenin entalpi değişimi kaç kJ’dir?',
 dogru=dH7,yan=[(w1,'H₂’nin katsayısını (3) hesaba katmamış; yalnız bir H–H bağı kırılmış saymış.','dikkat'),(w2,'ΔH’ı 1 mol NH₃ için bulup yazmış; denklemde 2 mol NH₃ oluşuyor.','dikkat'),(w3,'Oluşan bağlar − kırılan bağlar biçiminde çıkarmış; işareti ters bulmuş.','bilgi'),(w4,'Yalnız bir NH₃ molekülündeki 3 N–H bağını oluşan saymış.','islem')],
 z='orta',alt='Bağ Enerjileri',kaz='Yapı formülleri ve bağ enerjilerinden tepkime entalpisini hesaplar.',kalip='şekilli',sekil=SK,
 istenen='Tepkimenin entalpi değişimi (kJ).',
 ip=['Her bağ türünün sayısını katsayılarla birlikte say; hangilerinin kırıldığını, hangilerinin oluştuğunu ayır.'],
 bilgi=[B('Bağ enerjisi ve ΔH','bağ kırılması enerji ister, bağ oluşumu enerji verir; ΔH = kırılan bağ enerjileri toplamı − oluşan bağ enerjileri toplamı. Örnek: A–A + B–B → 2A–B için ΔH = E(A–A) + E(B–B) − 2E(A–B)')],
 puf='ΔH = kırılan − oluşan; bağ sayılarını katsayıyla çarpmayı unutma.')

# =============== 0008 · bilinmeyen bağ enerjisi · orta · şekil ===============
E8={'C–H':414,'Cl–Cl':243,'H–Cl':431}; dH8=-113
x8=E8['C–H']+E8['Cl–Cl']-E8['H–Cl']-dH8; assert x8==339
u1=E8['C–H']+E8['Cl–Cl']-E8['H–Cl']+dH8; u2=E8['C–H']+E8['Cl–Cl']+dH8*-1; u3=E8['C–H']+E8['Cl–Cl']+E8['H–Cl']-dH8; u4=4*E8['C–H']+E8['Cl–Cl']-E8['H–Cl']-dH8
assert (u1,u2,u3,u4)==(113,770,1201,1581)
s=.8
def ch4(cx,cl=None):
    r=at(cx,0,'C')+at(cx,s,'H')+at(cx,-s,'H')+at(cx-s,0,'H')
    r+=f'\\draw[thick] ({cx},.2) -- ({cx},{s-.2}); \\draw[thick] ({cx},-.2) -- ({cx},{-s+.2}); \\draw[thick] ({cx-.2},0) -- ({cx-s+.2},0);'
    if cl: r+=at(cx+s,0,'Cl')+f'\\draw[thick] ({cx+.2},0) -- ({cx+s-.28},0);'
    else: r+=at(cx+s,0,'H')+f'\\draw[thick] ({cx+.2},0) -- ({cx+s-.2},0);'
    return r
g=ch4(1.0)+at(2.55,0,'+')+at(3.25,0,'Cl')+at(4.35,0,'Cl')+bond(3.6,4.0,0)+f'\\draw[{ARR},thick] (4.95,0) -- (5.6,0);'+ch4(6.9,True)+at(8.9,0,'+')+at(9.5,0,'H')+at(10.4,0,'Cl')+bond(9.75,10.1,0)
g=f'\\begin{{scope}}[scale=.82]{g}\\end{{scope}}'
g+=tablo_tikz(4.2,-2.2,['Bağ','Enerji (kJ/mol)'],[['C--H','414'],['Cl--Cl','243'],['H--Cl','431']])
SK=tk(g)
q('0008','07',[A('Kırılan bağları belirle','CH₄’te 1 tane C–H bağı ve Cl₂’de Cl–Cl bağı kırılır.','414 + 243 = 657 kJ'),
 A('Oluşan bağları belirle','CH₃Cl’de bir C–Cl bağı, HCl’de bir H–Cl bağı oluşur.','oluşan = E(C–Cl) + 431'),
 A('ΔH eşitliğini yaz','ΔH, kırılanların toplamından oluşanların toplamının çıkarılmasıdır.','657 − (E + 431) = −113'),
 A('Bilinmeyeni çöz','Eşitlikten C–Cl bağ enerjisi bulunur.','E(C–Cl) = 657 − 431 + 113 = 339 kJ/mol')],
 ne='C–Cl bağ enerjisi',metin='Metanın klorla tepkimesinden klorometan (CH₃Cl) ve hidrojen klorür oluşur. Tepkimenin entalpi değişimi −113 kJ’dir. Şekilde tepkime yapı formülleriyle ve bazı bağ enerjileriyle verilmiştir.\nBuna göre C–Cl bağının enerjisi kaç kJ/mol’dür?',
 dogru=x8,yan=[(u1,'ΔH’ı eşitlikte işaretiyle ters kullanmış (+113); bu yüzden değeri 113 bulmuş.','bilgi'),(u2,'Oluşan H–Cl bağının enerjisini (431 kJ/mol) eşitliğe katmamış.','dikkat'),(u3,'H–Cl bağını oluşan değil kırılan bağlar arasında saymış.','bilgi'),(u4,'CH₄’teki dört C–H bağının hepsini kırılan saymış; yalnız birinin kırıldığını görmemiş.','dikkat')],
 z='orta',alt='Bağ Enerjileri',kaz='Tepkime entalpisi ve bilinen bağ enerjilerinden bilinmeyen bağ enerjisini bulur.',kalip='şekilli',sekil=SK,
 istenen='C–Cl bağının enerjisi (kJ/mol).',
 ip=['Yapı formüllerini karşılaştırarak hangi bağların kırılıp hangilerinin oluştuğunu belirle.'],
 bilgi=[B('Kırılan ve oluşan bağlar','tepkimede değişmeyen bağlar hesaba katılmaz; yalnız kopan ve yeni oluşan bağlar sayılır. Örnek: A₂ + B₂ → 2AB tepkimesinde A–A ve B–B kırılır, iki tane A–B bağı oluşur')],
 puf='Yalnız değişen bağları yaz: ΔH = kırılanlar − oluşanlar.')

# =============== 0009 · kavramlar · orta · olumsuz kök ===============
d,y=tek([('Ekzotermik bir tepkimede girenlerin toplam potansiyel enerjisi, ürünlerinkinden büyüktür.',False,'Doğru bir ifadeyi yanlış sanmış; ısı veren tepkimede enerji farkı ortama ısı olarak verilir.'),
 ('Standart koşullarda kararlı hâldeki bir elementin standart oluşum entalpisi sıfırdır.',False,'Elementin oluşumu için bir değişim olmadığını görmeyip doğru ifadeyi yanlış saymış.'),
 ('Endotermik bir tepkimenin entalpi değişimi pozitif değerlidir.',False,'Isı alan tepkimenin ΔH’ının pozitif olduğunu bilmeyip doğru ifadeyi yanlış saymış.'),
 ('Bir tepkimenin tüm katsayıları iki katına çıkarılırsa entalpi değişimi değişmez.',True,''),
 ('Bir maddenin yanma tepkimesi ekzotermiktir; çevreye ısı verir.',False,'Yanmanın ısı vermesini bilmeyip doğru ifadeyi yanlış saymış.')])
# doğru şık metni (yanlış ifade) ve çeldiriciler
q('0009','03',[A('İfadeleri sırayla ele al','Soruda yanlış olan ifade aranıyor; doğru ifadeler elenir.','A, B, C, E: doğru'),
 A('Katsayı etkisini düşün','ΔH, tepkimede girenlerin ve ürünlerin mol sayısına bağlı toplam ısıdır.','katsayı × 2 → ΔH × 2'),
 A('Yanlış ifadeyi seç','Katsayılar 2 katına çıkınca ΔH de 2 katına çıkar; değişmez diyen ifade yanlıştır.','D: yanlış')],
 ne='yanlış ifade',metin='Bir öğretmen, kimyasal tepkimelerde enerji değişimine ilişkin öğrencilerinden aşağıdaki ifadelerden birinin yanlış olduğunu bulmalarını istiyor. İfadeler tepkimelerin sabit sıcaklık ve basınçta gerçekleştiği varsayılarak yazılmıştır.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 dogru=d,sira=[ 'Ekzotermik bir tepkimede girenlerin toplam potansiyel enerjisi, ürünlerinkinden büyüktür.','Standart koşullarda kararlı hâldeki bir elementin standart oluşum entalpisi sıfırdır.','Endotermik bir tepkimenin entalpi değişimi pozitif değerlidir.','Bir tepkimenin tüm katsayıları iki katına çıkarılırsa entalpi değişimi değişmez.','Bir maddenin yanma tepkimesi ekzotermiktir; çevreye ısı verir.'],yan=y,
 z='kolay',alt='Ekzotermik ve Endotermik Tepkimeler',kaz='Entalpi ile ilgili temel kavramlardaki yanlış ifadeyi bulur.',kalip='düz',
 istenen='Yanlış olan ifade.',
 ip=['Her ifadeyi ΔH ve potansiyel enerji tanımlarına göre sına.'],
 bilgi=[B('Ekzotermik ve endotermik','ekzotermik tepkimede ürünlerin enerjisi girenlerden düşüktür ve ΔH < 0’dır; endotermik tepkimede ürünlerin enerjisi yüksektir ve ΔH > 0’dır. Örnek: ΔH = −30 kJ ise tepkime ısı verir')],
 puf='Yanlış ifadeyi bulmak için her seçeneği ilgili tanıma göre tek tek sına.')

# =============== 0010 · kalorimetre NaOH · orta · öncüllü · düzenek ===============
m10,c10,T1,T2_=100,Fr(42,10),25,35; dT10=T2_-T1; q10=m10*c10*dT10; n10=Fr(4,40); dHm=-q10/1000/n10
assert q10==4200 and n10==Fr(1,10) and dHm==-42
def beaker(cx,tc,hg,alt):
    g=f'\\draw[thick] ({cx-1.0},2.7) -- ({cx-1.0},0) -- ({cx+1.0},0) -- ({cx+1.0},2.7);'
    g+=f'\\fill[vurgu!20] ({cx-.985},.02) rectangle ({cx+.985},1.8);'
    g+=f'\\draw[thick] ({cx+.35},.45) -- ({cx+.35},3.0); \\draw[thick,fill=vurgu!60] ({cx+.35},.45) circle (.1);\\draw[line width=2pt,vurgu] ({cx+.35},.45) -- ({cx+.35},{hg});'
    g+=f'\\node at ({cx+.35},3.35) {{{tc}}}; \\node at ({cx},-.4) {{{alt}}};'
    return g
g=beaker(1.2,'$25\\ ^\\circ$C',1.1,'100 g su')+beaker(6.4,'$35\\ ^\\circ$C',1.9,'NaOH çözeltisi')
g+=f'\\draw[{ARR},thick] (2.9,1.4) -- (4.7,1.4); \\node[above,align=center] at (3.8,1.5) {{4 g NaOH(k)\\\\ eklenir}};'
SK=tk(g)
onc('0010','08','Bir öğrenci, ısı yalıtımlı kalorimetre kabındaki 100 g suya 4 g katı NaOH ekliyor ve tamamen çözünene kadar karıştırıyor. Suyun sıcaklığı şekilde gösterildiği gibi değişiyor. Suyun öz ısısı 4,2 J/g·°C, NaOH’ın mol kütlesi 40 g/mol’dür. Isı alışverişinin yalnız su ile olduğu ve ısı kaybının bulunmadığı varsayılacaktır.',
 [('NaOH’ın suda çözünmesi endotermiktir.',False,'Çözeltinin sıcaklığı yükseldiğine göre çözünme ortama ısı vermiştir; olay ekzotermiktir.','sıcaklık artışını çözünmenin ısı aldığı biçiminde yorumlamış.','—'),
  ('Suyun aldığı ısı 4,2 kJ’dir.',True,'q = 100 × 4,2 × 10 = 4200 J olup bu değer 4,2 kJ’dir.','—','4200 J ile 4,2 kJ’yi farklı değerler sanmış.'),
  ('NaOH’ın molar çözünme entalpisi −42 kJ/mol’dür.',True,'4 g NaOH 0,1 mol olduğundan 4,2 kJ ÷ 0,1 mol = 42 kJ/mol ısı açığa çıkar; ekzotermik olduğundan ΔH = −42 kJ/mol’dür.','—','4,2 kJ ısıyı mol sayısına (0,1) bölmeyi atlamış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='NaOH çözünme ısısı ve kalorimetre verileri',z='orta',alt='Kalorimetri',kaz='Kalorimetre verilerinden ısı miktarını ve molar çözünme entalpisini yorumlar.',kalip='öncüllü',sekil=SK,
 istenen='Doğru ifadeler.',
 ip=['Önce suyun aldığı ısıyı, sonra 1 mol için karşılığını düşün.'],
 bilgi=[B('Isı hesabı','bir maddenin aldığı ya da verdiği ısı q = m·c·ΔT ile bulunur; 1 kJ = 1000 J’dür. Örnek: 50 g suyun sıcaklığı 2 °C artarsa q = 50 × 4,2 × 2 = 420 J olur')],
 puf='Önce q = m·c·ΔT (J), sonra kJ’ye çevir ve mol sayısına böl.')

# =============== 0011 · ΔHf çubuk grafiği · orta · olumsuz kök ===============
hf11={'NO(g)':90,'NH₃(g)':-46,'HCl(g)':-92,'H₂O(g)':-242}
assert 2*hf11['H₂O(g)']==-484 and -2*hf11['HCl(g)']==184 and min(hf11,key=hf11.get)=='H₂O(g)'
scy=.02
g=f'\\draw[{ARR},thick] (0,{-260*scy:.2f}) -- (0,{130*scy:.2f}); \\draw[thick] (0,0) -- (7.6,0);'
for v in [-200,-100,0,100]:
    g+=f'\\draw (0,{v*scy:.2f}) -- (-.08,{v*scy:.2f}); \\node[left,inner sep=2pt] at (-.05,{v*scy:.2f}) {{${v}$}};'
    if v!=0: g+=f'\\draw[dotted,gray] (0,{v*scy:.2f}) -- (7.6,{v*scy:.2f});'
g+=f'\\node[rotate=90] at (-1.0,{-60*scy:.2f}) {{Standart oluşum entalpisi (kJ/mol)}};'
for i,(k,v) in enumerate(hf11.items()):
    x=1.2+1.7*i; ke=k.replace('₂','$_2$').replace('₃','$_3$')
    g+=f'\\draw[thick,fill=vurgu!25] ({x-.5},0) rectangle ({x+.5},{v*scy:.2f});'
    g+=f'\\node at ({x},{v*scy+(.3 if v>0 else -.3):.2f}) {{{("+"+str(v)) if v>0 else "$-$"+str(-v)}}};'
    g+=f'\\node at ({x},{130*scy+.45:.2f}) {{{ke}}};'
SK=tk(g)
d,y=tek([('NO(g)’nin elementlerinden oluşması endotermiktir.',False,'NO’nun oluşum entalpisinin pozitif olması ısı alındığını gösterir; doğru bir ifadeyi yanlış saymış.'),
 ('NH₃(g)’ün 1 molü elementlerinden oluşurken 46 kJ ısı açığa çıkar.',False,'ΔHf = −46 kJ/mol ısı verildiği anlamına gelir; doğru bir ifadeyi yanlış saymış.'),
 ('2HCl(g) → H₂(g) + Cl₂(g) tepkimesinin entalpi değişimi +184 kJ’dir.',False,'Bu tepkime 2 mol HCl oluşumunun tersidir (2 × (−92) = −184 kJ); işaret değişip +184 olur, ifade doğrudur.'),
 ('2H₂(g) + O₂(g) → 2H₂O(g) tepkimesinin entalpi değişimi −242 kJ’dir.',True,''),
 ('Grafikteki maddeler içinde oluşum entalpisi en küçük olan H₂O(g)’dir.',False,'−242 kJ/mol grafikteki en küçük değerdir; doğru bir ifadeyi yanlış saymış.')])
q('0011','02',[A('Grafiği oku','Her çubuk, maddenin 1 molünün elementlerinden oluşma entalpisini gösterir.','NO: +90 · NH₃: −46 · HCl: −92 · H₂O: −242'),
 A('İfadeleri sırayla kontrol et','A, B, C ve E grafikteki değerlerle ve işaret yorumuyla uyumludur.','A, B, C, E: doğru'),
 A('Katsayıyı hesaba kat','Denklemde 2 mol H₂O(g) oluşuyor, grafik ise 1 mol içindir.','2 × (−242) = −484 kJ'),
 A('Yanlış ifadeyi seç','−242 kJ yalnız 1 mol için geçerlidir.','D: yanlış')],
 ne='yanlış ifade',metin='Şekilde, bazı gazların 25 °C’deki standart oluşum entalpileri çubuk grafikle gösterilmiştir.\nBuna göre aşağıdakilerden hangisi yanlıştır?',
 dogru=d,sira=['NO(g)’nin elementlerinden oluşması endotermiktir.','NH₃(g)’ün 1 molü elementlerinden oluşurken 46 kJ ısı açığa çıkar.','2HCl(g) → H₂(g) + Cl₂(g) tepkimesinin entalpi değişimi +184 kJ’dir.','2H₂(g) + O₂(g) → 2H₂O(g) tepkimesinin entalpi değişimi −242 kJ’dir.','Grafikteki maddeler içinde oluşum entalpisi en küçük olan H₂O(g)’dir.'],yan=y,
 z='orta',alt='Oluşum Entalpisi',kaz='Oluşum entalpisi grafiğinden tepkime entalpisine ilişkin yargıları değerlendirir.',kalip='grafik',sekil=SK,
 istenen='Yanlış olan ifade.',
 ip=['Grafikteki değerlerin kaç mol madde için verildiğine dikkat et.'],
 bilgi=[B('Oluşum entalpisi yorumu','ΔHf negatifse bileşik elementlerinden ısı vererek, pozitifse ısı alarak oluşur; değer 1 mol bileşik içindir. Örnek: ΔHf = −20 kJ/mol olan bileşiğin 3 molü oluşurken 60 kJ ısı açığa çıkar')],
 puf='Grafikteki değerlerin hangi madde miktarı için verildiğine bak; her ifadeyi buna göre sına.')

# =============== 0012 · tablo öncüllü · orta ===============
hf12={'C₂H₂(g)':227,'C₂H₄(g)':52,'CO₂(g)':-394}
dH12=hf12['C₂H₄(g)']-hf12['C₂H₂(g)']; assert dH12==-175 and hf12['C₂H₄(g)']>0 and hf12['C₂H₂(g)']>0
SK=tablo_svg(['Madde','Standart oluşum entalpisi (kJ/mol)'],[[k,('+' if v>0 else '')+fm(v)] for k,v in hf12.items()])
onc('0012','02','Aşağıdaki tabloda bazı gazların 25 °C’deki standart oluşum entalpileri verilmiştir.',
 [('C₂H₄(g)’nin elementlerinden oluşması endotermiktir.',True,'ΔHf(C₂H₄) = +52 kJ/mol pozitif olduğundan oluşum sırasında ısı alınır.','—','pozitif oluşum entalpisini ısı verilmesi sanmış.'),
  ('C₂H₂(g) + H₂(g) → C₂H₄(g) tepkimesinin entalpi değişimi −175 kJ’dir.',True,'ΔH° = (+52) − (+227 + 0) = −175 kJ; H₂ element olduğundan sıfırdır.','—','H₂’nin oluşum entalpisini ya da girenlerin çıkarılmasını yanlış uygulamış.'),
  ('C₂H₂(g)’nin elementlerinden oluşması sırasında ortama ısı verilir.',False,'ΔHf(C₂H₂) = +227 kJ/mol pozitif olduğundan oluşum sırasında ısı alınır.','pozitif değerin ısı verildiği anlamına geldiğini sanmış.','—')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='oluşum entalpisi tablosundan yargılar',z='orta',alt='Oluşum Entalpisi',kaz='Oluşum entalpisi tablosundan oluşum ve tepkime ısılarına ilişkin yargıları değerlendirir.',kalip='öncüllü',sekil=SK,
 istenen='Doğru ifadeler.',
 ip=['Her ifadede işareti ve hangi tepkimenin istendiğini kontrol et.'],
 bilgi=[B('Oluşum entalpisi ve işaret','ΔHf° negatifse oluşum ısı verir, pozitifse ısı alır. Kararlı elementlerin ΔHf° değeri sıfırdır. Örnek: ΔHf° = +15 kJ/mol olan bir bileşik elementlerinden ısı alarak oluşur')],
 puf='Önce ifadenin işaret yorumunu, sonra gerekiyorsa ürün − giren hesabını yap.')

# =============== 0013 · Hess · orta ===============
a13,b13=68,-114; dH13=a13-b13; assert dH13==182
q('0013','06',[A('Hedefi belirle','İstenen tepkimede NO girenler tarafında değil, ürünler tarafında yer alır.','N₂ + O₂ → 2NO'),
 A('İkinci tepkimeyi çevir','NO ikinci tepkimede girendir; ters çevirince ΔH işaret değiştirir.','2NO₂ → 2NO + O₂   ΔH = +114 kJ'),
 A('Tepkimeleri topla','Ortak maddeler sadeleşir.','N₂ + 2O₂ → 2NO₂ ve 2NO₂ → 2NO + O₂'),
 A('Entalpileri topla','ΔH değerleri de toplanır.','ΔH = 68 + 114 = +182 kJ')],
 ne='N₂ + O₂ → 2NO tepkimesinin ΔH’ı',metin='Aşağıda iki tepkime ve standart entalpi değişimleri verilmiştir.\nN₂(g) + 2O₂(g) → 2NO₂(g)    ΔH = +68 kJ\n2NO(g) + O₂(g) → 2NO₂(g)    ΔH = −114 kJ\nBuna göre N₂(g) + O₂(g) → 2NO(g) tepkimesinin standart entalpi değişimi kaç kJ’dir?',
 dogru=dH13,yan=[(-dH13,'Doğru toplamı (+182 kJ) bulmuş ama sonucun işaretini ters yazmış.','islem'),(a13+b13,'İkinci tepkimeyi tersine çevirmeden iki ΔH’ı toplamış (68 − 114).','bilgi'),(Fr(dH13,2),'Bulduğu değeri 1 mol NO için yazmış; denklemde 2 mol NO oluşuyor.','dikkat'),(-b13,'Yalnız ikinci tepkimenin ΔH’ının mutlak değerini yazmış; ilk tepkimeyi hesaba katmamış.','dikkat')],
 z='orta',alt='Hess Yasası',kaz='Tepkimeleri ters çevirip toplayarak istenen tepkimenin entalpi değişimini bulur.',kalip='düz',
 istenen='N₂(g) + O₂(g) → 2NO(g) tepkimesinin ΔH’ı (kJ).',
 ip=['NO’nun hangi tepkimede girenler, hangisinde ürünler tarafında olması gerektiğine bak.'],
 bilgi=[B('Tepkime toplama','tepkime ters yazılırsa ΔH’ın işareti değişir; tepkimeler toplanırken ΔH’lar da toplanır. Örnek: A → B ΔH = −5 kJ ise B → A ΔH = +5 kJ’dir')],
 puf='İstenen tepkimede ortak olmayan maddelere göre tepkimeleri çevir, sonra topla.')

# =============== 0014 · Hess kavram · orta · öncüllü ===============
a14,b14=-60,20; assert a14+b14==-40 and -b14==-20 and 2*a14==-120
onc('0014','06','X(g) + Y(g) → Z(g)    ΔH = −60 kJ\nZ(g) → T(g)    ΔH = +20 kJ\nTepkimeler aynı sıcaklık ve basınçta gerçekleşmektedir.',
 [('X(g) + Y(g) → T(g) tepkimesinin entalpi değişimi −40 kJ’dir.',True,'İki tepkime toplanır: (−60) + (+20) = −40 kJ.','—','tepkimeleri toplamak gerektiğini görmemiş.'),
  ('T(g) → Z(g) tepkimesinin entalpi değişimi −20 kJ’dir.',True,'Z → T tepkimesinin tersidir; ΔH’ın işareti değişir ve −20 kJ olur.','—','ters tepkimede ΔH’ın işaret değiştirdiğini unutmuş.'),
  ('2X(g) + 2Y(g) → 2Z(g) tepkimesinin entalpi değişimi −120 kJ’dir.',True,'Katsayılar 2 ile çarpıldığında ΔH de 2 ile çarpılır.','—','katsayı artınca ΔH’ın değişmediğini sanmış.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='Hess yasasının kuralları',z='orta',alt='Hess Yasası',kaz='Tepkimeyi tersine çevirme, katsayıyla çarpma ve toplamanın entalpi değişimine etkisini yorumlar.',kalip='öncüllü',
 istenen='Doğru ifadeler.',
 ip=['Her ifadede tepkimenin verilenlere göre nasıl değiştirildiğine bak.'],
 bilgi=[B('Hess yasası kuralları','ters çevirmede ΔH’ın işareti değişir, katsayılarla çarpmada ΔH de aynı sayıyla çarpılır, toplamada ΔH’lar toplanır. Örnek: M → N ΔH = +9 kJ ise 3M → 3N için ΔH = +27 kJ’dir')],
 puf='Verilen tepkimeye uygulanan işlemi ΔH’a da uygula.')

# =============== 0015 · karışım · zor · tablo ===============
hc={'CH₄(g)':890,'C₂H₆(g)':1560}; Mk={'CH₄(g)':16,'C₂H₆(g)':30}
nT=Fr(1,2); Q15=579
y15=(Q15-hc['CH₄(g)']*nT)/(hc['C₂H₆(g)']-hc['CH₄(g)']); x15=nT-y15
assert (x15,y15)==(Fr(3,10),Fr(1,5)) and x15*hc['CH₄(g)']+y15*hc['C₂H₆(g)']==Q15
m15=x15*16+y15*30; assert m15==Fr(54,5)
sw=y15*16+x15*30; allc=nT*16; allc2=nT*30; ch4only=x15*16
assert (sw,allc,allc2,ch4only)==(Fr(61,5),8,15,Fr(24,5)) and len({m15,sw,allc,allc2,ch4only})==5
SK=tablo_svg(['Madde','Standart yanma entalpisi (kJ/mol)'],[['CH₄(g)','−890'],['C₂H₆(g)','−1560']])
q('0015','09',[A('Bilinmeyenleri tanımla','CH₄ ve C₂H₆’nın mol sayıları x ve y olsun; toplam mol 0,5’tir.','x + y = 0,5'),
 A('Isı denklemini yaz','Her maddenin mol sayısı yanma ısısıyla çarpılıp toplanır.','890x + 1560y = 579'),
 A('Denklemleri çöz','Birinci denklem 890 ile çarpılıp çıkarılır.','670y = 579 − 445 = 134 → y = 0,2 · x = 0,3'),
 A('Kütleleri hesapla','Mol sayıları mol kütleleriyle çarpılır.','0,3 × 16 + 0,2 × 30 = 4,8 + 6'),
 A('Toplamı bul','İki kütle toplanır.','4,8 + 6 = 10,8 g')],
 ne='CH₄ ve C₂H₆ karışımının kütlesi',metin='Aşağıdaki tabloda CH₄ ve C₂H₆ gazlarının standart yanma entalpileri verilmiştir.\nCH₄ ve C₂H₆ gazlarından oluşan 0,5 mol karışım, standart koşullarda yeterli O₂ ile tamamen yakıldığında 579 kJ ısı açığa çıkıyor.\nAtom kütleleri H: 1, C: 12 olduğuna göre karışımın kütlesi kaç gramdır?',
 dogru=m15,yan=[(sw,'CH₄ ve C₂H₆’nın mol sayılarını yer değiştirmiş (0,2 mol CH₄, 0,3 mol C₂H₆).','islem'),(allc,'Karışımın tamamını CH₄ sanıp 0,5 × 16 hesaplamış.','dikkat'),(allc2,'Karışımın tamamını C₂H₆ sanıp 0,5 × 30 hesaplamış.','dikkat'),(ch4only,'Yalnız CH₄’ün kütlesini (0,3 × 16) bulmuş; C₂H₆’yı eklememiş.','dikkat')],
 z='zor',alt='Hess Yasası ve Stokiyometri',kaz='Yanma entalpilerinden karışımın bileşimini ve kütlesini bulur.',kalip='tablo',sekil=SK,
 istenen='Karışımın kütlesi (g).',
 ip=['Toplam mol ve toplam ısı için iki denklem kurabilirsin.'],
 bilgi=[B('Yanma entalpisi','1 mol maddenin standart koşullarda yeterli O₂ ile tamamen yanması sırasındaki entalpi değişimidir; açığa çıkan ısı, yanan mol sayısıyla doğru orantılıdır. Örnek: 1 mol yakıt 100 kJ veriyorsa 3 mol yakıt 300 kJ verir')],
 puf='İki bilinmeyenli karışım sorusunda mol toplamı ve ısı toplamı denklemlerini birlikte çöz.')

# =============== 0016 · O–H bağ enerjisi · zor · yapı ===============
E16={'H–H':436,'O=O':498}; hf16=-241
ohb=Fr(E16['H–H']+Fr(E16['O=O'],2)-hf16,2); assert ohb==463
v1=Fr(E16['H–H']+Fr(E16['O=O'],2)+hf16,2); v2=Fr(E16['H–H']+Fr(E16['O=O'],2)-hf16,4); v3=Fr(E16['H–H']+E16['O=O']-hf16,2); v4=2*ohb
assert (v1,v2,v3,v4)==(222,Fr(463,2),Fr(1175,2),926)
g=at(.0,0,'H')+at(1.2,0,'H')+bond(.22,.98,0)+at(1.95,0,'+')+at(2.6,0,'1/2')+at(3.4,0,'O')+at(4.5,0,'O')+bond(3.65,4.25,0,2)
g+=f'\\draw[{ARR},thick] (5.1,0) -- (5.9,0);'+at(7.2,0,'O')+at(6.3,-.75,'H')+at(8.1,-.75,'H')+'\\draw[thick] (7.0,-.17) -- (6.52,-.55); \\draw[thick] (7.4,-.17) -- (7.88,-.55);'
g+=at(.6,-1.05,'436 kJ/mol')+at(3.95,-1.05,'498 kJ/mol')
SK=tk(g)
q('0016','07',[A('Kırılan bağları belirle','1 mol H–H ve ½ mol O=O bağı kırılır.','436 + ½ × 498 = 685 kJ'),
 A('Oluşan bağları belirle','1 mol H₂O’da 2 mol O–H bağı oluşur.','oluşan = 2 × E(O–H)'),
 A('ΔH eşitliğini yaz','Oluşum entalpisi bu tepkimenin ΔH’ıdır.','685 − 2E = −241'),
 A('O–H bağ enerjisini bul','Eşitlik E için çözülür.','E = (685 + 241) ÷ 2 = 463 kJ/mol')],
 ne='O–H bağının enerjisi',metin='Gaz hâlindeki suyun standart oluşum entalpisi −241 kJ/mol’dür. Şekilde H₂O(g)’nin elementlerinden oluşumu yapı formülleriyle ve bazı bağ enerjileriyle verilmiştir.\nBuna göre O–H bağının enerjisi kaç kJ/mol’dür?',
 dogru=ohb,yan=[(v1,'ΔH’ı eşitlikte işaretiyle ters kullanmış (685 − 241 = 444 kJ’yi 2’ye bölmüş).','bilgi'),(v2,'Toplam enerjiyi 4’e bölmüş; H₂O’da yalnız 2 O–H bağı olduğunu görmemiş.','dikkat'),(v3,'O=O bağını ½ ile çarpmadan tam almış (436 + 498 + 241 = 1175 kJ’yi 2’ye bölmüş).','dikkat'),(v4,'Bulduğu 926 kJ’yi bağ sayısı olan 2’ye bölmemiş; iki O–H bağının toplamını yazmış.','islem')],
 z='orta',alt='Bağ Enerjileri',kaz='Oluşum entalpisi ve bağ enerjilerini birleştirerek bilinmeyen bağ enerjisini hesaplar.',kalip='şekilli',sekil=SK,
 istenen='O–H bağının enerjisi (kJ/mol).',
 ip=['Şekildeki tepkimede katsayıların ½ olduğuna ve 1 mol suda kaç O–H bağı bulunduğuna dikkat et.'],
 bilgi=[B('Bağ sayısı','bir molekülde aynı türden birden fazla bağ varsa toplam bağ enerjisi bağ sayısıyla çarpılır; katsayılar bağ sayısına da yansır. Örnek: katsayısı 3 olan bir molekülde molekül başına 2 aynı bağ varsa 6 mol bağ vardır')],
 puf='Katsayıları bağ sayısına yansıt; oluşum entalpisi 1 mol bileşik içindir.')

# =============== 0017 · Hess + kütle (termit) · zor ===============
h1,h2=-1676,-824; dT=h1-h2; assert dT==-852
Q17=1278; nr17=Fr(Q17,-dT); assert nr17==Fr(3,2)
mFe=2*nr17*56; assert mFe==168
y1=nr17*56; y2=3*27; y3=nr17*160; y4=nr17*102
assert (y1,y2,y3,y4)==(84,81,240,153) and len({mFe,y1,y2,y3,y4})==5
q('0017','09',[A('Hedef tepkimeyi belirle','Fe₂O₃ + 2Al → Al₂O₃ + 2Fe elde edilmeli; Al₂O₃ üründe, Fe₂O₃ girende olmalı.','(1) aynen, (2) ters'),
 A('Tepkimeleri topla','İkinci tepkime çevrilince ΔH’ın işareti değişir.','ΔH = −1676 + 824 = −852 kJ'),
 A('Tepkime sayısını bul','−852 kJ, denklemin bir kez gerçekleşmesi içindir.','1278 ÷ 852 = 1,5 kez'),
 A('Fe mol sayısını bul','Her gerçekleşmede 2 mol Fe oluşur.','1,5 × 2 = 3 mol Fe'),
 A('Kütleyi hesapla','Mol sayısı mol kütlesiyle çarpılır.','3 × 56 = 168 g')],
 ne='1278 kJ ısıyla oluşan Fe kütlesi',metin='25 °C’de aşağıdaki tepkimelerin standart entalpi değişimleri verilmiştir.\n2Al(k) + 3/2O₂(g) → Al₂O₃(k)    ΔH = −1676 kJ\n2Fe(k) + 3/2O₂(g) → Fe₂O₃(k)    ΔH = −824 kJ\nFe₂O₃(k) + 2Al(k) → Al₂O₃(k) + 2Fe(k) tepkimesinde 1278 kJ ısı açığa çıkıyor.\nFe’nin atom kütlesi 56 g/mol olduğuna göre oluşan Fe kaç gramdır?',
 dogru=mFe,yan=[(y1,'Tepkime sayısını (1,5) Fe’nin mol sayısı sanmış (1,5 × 56).','islem'),(y2,'Isıyı yanlış yorumlayıp harcanan Al’nin kütlesini (3 mol × 27) bulmuş.','dikkat'),(y3,'Harcanan Fe₂O₃’ün kütlesini (1,5 mol × 160) bulmuş.','dikkat'),(y4,'Oluşan Al₂O₃’ün kütlesini (1,5 mol × 102) bulmuş.','dikkat')],
 z='zor',alt='Hess Yasası ve Stokiyometri',kaz='Hess yasasıyla tepkime entalpisini bulup ısı miktarından oluşan madde kütlesini hesaplar.',kalip='düz',
 istenen='Oluşan Fe kütlesi (g).',
 ip=['Önce verilen tepkimeleri hedef tepkimeyi verecek biçimde düzenle.'],
 bilgi=[B('Isı–mol orantısı','tepkimenin ΔH değeri, denklemdeki katsayılarla gerçekleşmesi için geçerlidir; açığa çıkan ısı bu değerin kaç katı ise tepkime o kadar kez gerçekleşmiştir.')],
 puf='Önce Hess ile ΔH, sonra ısı ÷ ΔH ile tepkime sayısı, sonra mol ve kütle.')

# =============== 0018 · Hess şeması + kütle · zor ===============
dd1,dd2=-788,-566; dd3=dd1-dd2; assert dd3==-222 and 2*(-394)==dd1
Qh=333; nr=Fr(Qh,-dd3); nCO=2*nr; mCO=nCO*28; assert (nr,nCO,mCO)==(Fr(3,2),3,84)
f1=nCO*12; f2=nr*28; f3=nr*32; f4=2*28
assert (f1,f2,f3,f4)==(36,42,48,56) and len({mCO,f1,f2,f3,f4})==5
SK=ladder([(0,'2C(k) + 2O$_2$(g)','a',0),(-55,'2CO(g) + O$_2$(g)','a',2.2),(-100,'2CO$_2$(g)','b',0)],[(.6,0,-100,'$\\Delta H=-788$ kJ',.2),(2.9,-55,-100,'$\\Delta H=-566$ kJ',.5),(5.2,0,-55,'$\\Delta H=?$',.5)],.05)
q('0018','09',[A('Şemadan ΔH’ı çıkar','Aynı sonuca iki yoldan gidilir; doğrudan yolun ΔH’ı basamakların toplamına eşittir.','−788 = ΔH + (−566)'),
 A('Bilinmeyeni bul','ΔH denklemden yalnız bırakılır.','ΔH = −788 + 566 = −222 kJ'),
 A('Tepkime sayısını bul','−222 kJ, denklemin bir kez gerçekleşmesi için geçerlidir.','333 ÷ 222 = 1,5 kez'),
 A('Mol sayısına geç','Denklemde 2 mol CO oluşur.','1,5 × 2 = 3 mol CO'),
 A('Kütleyi hesapla','Mol sayısı mol kütlesiyle çarpılır.','3 × 28 = 84 g')],
 ne='333 kJ ısıyla oluşan CO kütlesi',metin='Şekilde, C(k)’nın O₂(g) ile CO₂(g) oluşturması doğrudan yoldan ve CO(g) üzerinden gösterilmiş; bazı entalpi değişimleri verilmiştir.\nC: 12, O: 16 olduğuna göre 2C(k) + O₂(g) → 2CO(g) tepkimesinde 333 kJ ısı açığa çıktığında kaç gram CO(g) oluşur?',
 dogru=mCO,yan=[(f1,'Oluşan CO yerine tepkimeye giren C’nin kütlesini (3 mol × 12) bulmuş.','dikkat'),(f2,'333 kJ için bulduğu 1,5 değerini CO’nun mol sayısı sanmış (1,5 × 28).','islem'),(f3,'Harcanan O₂’nin kütlesini (1,5 mol × 32) bulmuş.','dikkat'),(f4,'Isıyı hesaba katmadan denklemdeki 2 mol CO’yu kütleye çevirmiş (2 × 28).','dikkat')],
 z='zor',alt='Hess Yasası ve Stokiyometri',kaz='Hess şemasından tepkime entalpisini bulup ısı miktarından oluşan madde kütlesini hesaplar.',kalip='şekilli',sekil=SK,
 istenen='Oluşan CO(g) kütlesi (g).',
 ip=['Önce şemadan bilinmeyen entalpi değişimini bul; sonra bu değerin kaç mol ürüne karşılık geldiğine bak.'],
 bilgi=[B('Isı–mol orantısı','tepkimenin ΔH değeri, denklemdeki katsayılarla gerçekleşmesi için geçerlidir; ısı miktarı bu değerin kaç katı olduğu kadar tepkimenin gerçekleştiğini gösterir. Örnek: ΔH = −50 kJ olan tepkimede 150 kJ ısı için tepkime 3 kez gerçekleşir')],
 puf='Önce Hess ile ΔH, sonra ısı ÷ ΔH ile tepkime sayısı, sonra mol ve kütle.')

# =============== 0019 · yakıt + su ısıtma · zor ===============
hf19={'C₂H₅OH(s)':-278,'CO₂(g)':-394,'H₂O(s)':-286}
dHc=2*hf19['CO₂(g)']+3*hf19['H₂O(s)']-hf19['C₂H₅OH(s)']; assert dHc==-1368
nE=Fr(46,10)/46; assert nE==Fr(1,10); Qf=-dHc*nE; assert Qf==Fr(1368,10)
verim=Fr(1,2); Qsu=Qf*verim*1000; mw=1900; cw=4; dT19=Qsu/(mw*cw); assert dT19==9
son=20+dT19; assert son==29
a1=dT19; a2=20+Fr(Qf*verim*1000*Fr(1,2),mw*cw); a3=20+Qf*1000/(mw*cw); a4=20+Qf/verim*1000/(mw*cw)
assert (a1,a2,a3,a4)==(9,Fr(49,2),38,56) and len({son,a1,a2,a3,a4})==5
q('0019','08',[A('Yanma entalpisini bul','ΔH°, ürünlerin oluşum entalpileri toplamı eksi girenlerinkidir; O₂ sıfırdır.','2 × (−394) + 3 × (−286) − (−278) = −1368 kJ'),
 A('Etanolün mol sayısını bul','Mol sayısı kütlenin mol kütlesine bölümüdür.','4,6 ÷ 46 = 0,1 mol'),
 A('Açığa çıkan ısıyı bul','Isı, mol sayısıyla yanma ısısının çarpımıdır; %50’si suya aktarılır.','0,1 × 1368 = 136,8 kJ · 136,8 × 0,5 = 68,4 kJ'),
 A('Sıcaklık artışını hesapla','q = m·c·ΔT bağıntısı kullanılır; 68,4 kJ = 68400 J.','ΔT = 68400 ÷ (1900 × 4) = 9 °C'),
 A('Son sıcaklığı yaz','Artış başlangıç sıcaklığına eklenir.','20 + 9 = 29 °C')],
 ne='suyun son sıcaklığı',metin='25 °C’de C₂H₅OH(s), CO₂(g) ve H₂O(s)’nin standart oluşum entalpileri sırasıyla −278, −394 ve −286 kJ/mol’dür.\nBir öğrenci 4,6 g C₂H₅OH(s)’yi C₂H₅OH(s) + 3O₂(g) → 2CO₂(g) + 3H₂O(s) tepkimesine göre tamamen yakıyor ve açığa çıkan ısının yalnız %50’sinin 20 °C’deki 1,9 kg suya aktarıldığını belirliyor.\nSuyun öz ısısı 4 J/g·°C, C₂H₅OH’ın mol kütlesi 46 g/mol olduğuna göre suyun son sıcaklığı kaç °C’dir?',
 dogru=son,yan=[(a1,'Sıcaklık artışını (9 °C) suyun son sıcaklığı sanmış; başlangıç sıcaklığını eklememiş.','dikkat'),(a2,'Etanolün mol sayısını 0,05 bulmuş (mol kütlesini 92 almış); ısı yarıya düşmüş.','islem'),(a3,'Isının tamamının suya aktarıldığını varsaymış (%50 verimi uygulamamış).','dikkat'),(a4,'%50 verimle çarpmak yerine bölmüş (136,8 ÷ 0,5 kJ).','islem')],
 z='zor',alt='Kalorimetri',kaz='Oluşum entalpilerinden yanma ısısını bulup verimli ısı aktarımıyla suyun sıcaklık değişimini hesaplar.',kalip='düz',
 istenen='Suyun son sıcaklığı (°C).',
 ip=['Önce yanma tepkimesinin entalpi değişimini bul; sonra suya geçen ısıdan sıcaklık artışına git.'],
 bilgi=[B('Verim ve su ısınması','açığa çıkan ısının yalnız bir kısmı suya geçiyorsa suyun aldığı ısı q = verim × toplam ısıdır; sıcaklık artışı ΔT = q ÷ (m·c) ile bulunur. Örnek: 30 kJ ısının %20’si 1 kg suya geçerse q = 6 kJ olur')],
 puf='Sıra: ΔHc → mol → toplam ısı → verim → ΔT → son sıcaklık.')

# =============== 0020 · bağ enerjisinden oluşum entalpisi · zor ===============
E20={'C=C':614,'C–C':348,'C–H':413,'H–H':436}; hfa=52
dHh=E20['C=C']+E20['H–H']-E20['C–C']-2*E20['C–H']; assert dHh==-124
hf20=hfa+dHh; assert hf20==-72
x1=hfa+(E20['C=C']-E20['C–C']-2*E20['C–H']); x2=dHh; x3=hfa-dHh; x4=hfa+(E20['C=C']+E20['H–H']-E20['C–C']-E20['C–H'])
assert (x1,x2,x3,x4)==(-508,-124,176,341) and len({hf20,x1,x2,x3,x4})==5
q('0020','07',[A('Kırılan bağları belirle','C₂H₄’ün C=C bağı ve H₂’nin H–H bağı kırılır.','614 + 436 = 1050 kJ'),
 A('Oluşan bağları belirle','C₂H₆’da bir C–C ve iki yeni C–H bağı oluşur.','348 + 2 × 413 = 1174 kJ'),
 A('Hidrojenlenme ΔH’ını bul','ΔH, kırılanlardan oluşanların çıkarılmasıdır.','1050 − 1174 = −124 kJ'),
 A('Oluşum entalpisine geç','C₂H₆’nın oluşumu, C₂H₄’ün oluşumu ile bu tepkimenin toplamıdır.','ΔHf(C₂H₆) = +52 + (−124) = −72 kJ/mol')],
 ne='C₂H₆(g)’nin standart oluşum entalpisi',metin='Aşağıda bazı bağ enerjileri (kJ/mol) verilmiştir.\nC=C: 614    C–C: 348    C–H: 413    H–H: 436\nC₂H₄(g)’nin standart oluşum entalpisi +52 kJ/mol’dür. C₂H₄(g) + H₂(g) → C₂H₆(g) tepkimesi gaz fazında gerçekleşmektedir.\nBuna göre C₂H₆(g)’nin standart oluşum entalpisi kaç kJ/mol’dür?',
 dogru=hf20,yan=[(x1,'H–H bağının kırılmasını hesaba katmamış (614 − 1174 = −560 kJ); sonra +52’yi eklemiş.','dikkat'),(x2,'Bağ enerjilerinden bulduğu tepkime entalpisini (−124 kJ) C₂H₆’nın oluşum entalpisi sanmış.','bilgi'),(x3,'Tepkime entalpisinin işaretini ters bulmuş (+124) ve +52’ye eklemiş.','bilgi'),(x4,'Oluşan C–H bağı sayısını 1 almış (ΔH = +289 kJ); sonra +52’yi eklemiş.','islem')],
 z='zor',alt='Bağ Enerjileri',kaz='Bağ enerjilerinden tepkime entalpisini bulup oluşum entalpisi ile birleştirir.',kalip='düz',
 istenen='C₂H₆(g)’nin standart oluşum entalpisi (kJ/mol).',
 ip=['Önce verilen tepkimenin ΔH’ını bağlardan bul; sonra oluşum entalpileriyle ilişkilendir.'],
 bilgi=[B('Oluşum entalpisi ve tepkime entalpisi','ΔH° = ΔHf(ürün) − ΔHf(giren) bağıntısından, bilinen bir oluşum entalpisi ve tepkime entalpisiyle bilinmeyen oluşum entalpisi bulunur. Örnek: A + B → C için ΔH = ΔHf(C) − ΔHf(A) − ΔHf(B)')],
 puf='Bağlardan ΔH bul, sonra ΔH = ΔHf(ürün) − ΔHf(giren) ilişkisinden oluşum entalpisine ulaş.')

# ---------------- bitir ----------------
for q_ in P.ANA: q_['kardes']=None
P.yaz(os.path.join(AD,'tepenerji-1.json'),'/tmp/bos-tepenerji.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=UK))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2019–2026 AYT Kimya çıkmış soruları, MEB 11. sınıf müfredatı.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
 open(os.path.join(AD,'..','kartlar','aktepenerji.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler),'soru',len(P.ANA))
