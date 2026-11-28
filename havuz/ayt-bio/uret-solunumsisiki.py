"""AYT Biyoloji · Solunum Sistemi 2. dalga (10 soru, kardeş yok, ipucu 1). Şekiller TikZ/pgfplots/tablo; öncüllerin doğru/yanlış değeri tek yerde (ST)."""
import sys,os,json,math,random
BD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(BD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
P=Parti('solunumsisiki','Solunum Sistemi','abio|Solunum Sistemi',ders='AYT Biyoloji',idon='aytbio')
H.KONU='Solunum Sistemi'
KY='ÖSYM 2018–2026 AYT Biyoloji (Solunum Sistemi) · MEB 11. sınıf biyoloji'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KY)
def q(no,ad,kalip='düz',**k): mk(P,no,ad=ad,adim=len(ad),kalip=kalip,**k)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OK='-{Stealth[length=2.3mm,width=1.9mm]}'
def yer(harf,dogru,yanlar):
    sira=[None]*5; sira['ABCDE'.index(harf)]=dogru; it=iter(yanlar)
    for i in range(5):
        if sira[i] is None: sira[i]=next(it)
    assert sorted(sira)==sorted([dogru]+list(yanlar)) and len(set(sira))==5; return sira
ONC=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
def etiket(S): 
    S=sorted(S); return {1:'Yalnız '+S[0] if len(S)==1 else None}.get(len(S)) or (' ve '.join(S) if len(S)==2 else 'I, II ve III')
def onc(ST,iste,harf,seed=1):
    """ST: {'I':(bool,ifade,neden)}; iste True: doğru olanlar, False: yanlış olanlar. Döner: dogru,sira,yan,adimlar"""
    hedef={r for r in ST if ST[r][0]==iste}; assert hedef and len(hedef)<3 or iste or True
    dg=etiket(hedef); p=ONC.index(dg); idx='ABCDE'.index(harf); assert idx<=p and 4-idx<=6-p,(dg,harf)
    rnd=random.Random(seed); alt=rnd.sample(ONC[:p],idx); ust=rnd.sample(ONC[p+1:],4-idx)
    sira=sorted(alt+[dg]+ust,key=ONC.index); assert sira.index(dg)==idx
    kume=lambda l:{'Yalnız I':{'I'},'Yalnız II':{'II'},'Yalnız III':{'III'},'I ve II':{'I','II'},'I ve III':{'I','III'},'II ve III':{'II','III'},'I, II ve III':{'I','II','III'}}[l]
    yan=[]
    for l in alt+ust:
        W=kume(l); parc=[]
        for r in sorted(W-hedef):
            t=ST[r][0]; parc.append(f"{r} öncülü {'doğru' if t else 'yanlış'}{'dur' if t else 'tır'}. {ST[r][2]} Ancak {'yanlış' if t else 'doğru'} sanılarak kümeye alınmıştır.")
        for r in sorted(hedef-W):
            t=ST[r][0]; parc.append(f"{r} öncülü {'doğru' if t else 'yanlış'}{'dur' if t else 'tır'}. {ST[r][2]} Ancak {'yanlış' if t else 'doğru'} sanılarak dışarıda bırakılmıştır.")
        yan.append((l,' '.join(parc),'bilgi'))
    ad=[A(f'{r} öncülünü değerlendir',ST[r][2],f"{r}: {'doğru' if ST[r][0] else 'yanlış'}") for r in ST]
    ad.append(A('Kümeyi oluştur',f"İstenen yargılara uyan öncüller: {', '.join(sorted(hedef))}.",'Cevap: '+dg))
    return dg,sira,yan,ad
def onctxt(giris,ST,kok): return giris+'\n'+'\n'.join(f'{r}. {ST[r][1]}' for r in ST)+'\n'+kok
def tablo_s(bas,sat): return tablo_svg(bas,sat)
def graf(govde,w='7.4cm',h='5cm'): return tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+govde+'\n\\end{tikzpicture}')
# ---- kartlar (2. dalga: K-ABSS2-NN) ----
kartla('K-ABSS2-01','Soluk havasının bileşimi ve gaz değişim yüzeyi','Soluk alınan ve verilen havanın bileşimi, alveolde kana geçen ve kandan alveole gelen gazların farkını yansıtır; gaz değişimi hızı gaz değişim yüzeyinin özelliklerine ve kısmi basınç farkına bağlıdır, kanın kılcaldaki kalış süresi de sonucu belirler.','Azotun da gaz değişimine katıldığını sanmak; kısmi basınç dengesi kurulduktan sonra da gaz geçişinin sürdüğünü düşünmek.','kolay','tablo',3,'ss-gaz-yuzey','Hava bileşimi ve gaz değişim yüzeyi')
kartla('K-ABSS2-02','Solunum sistemi hastalıkları','Solunum hastalıkları ya hava yolunu (astım, bronşit) ya da alveolleri (amfizem, zatürre) etkiler; kirpikli epitel ve mukus hava yolunu temizler; hastalığın etkisi gaz değişim yüzeyi ve hava akışı üzerinden yorumlanır.','Her solunum hastalığının aynı yapıyı bozduğunu sanmak; alveol kaybının yüzey alanını artırdığını düşünmek.','kolay','şekilli',3,'ss-hastalik','Solunum sistemi hastalıkları ve savunma')
kartla('K-ABSS2-03','Solunum hacimleri ve dakikada solunan hava','Dakikada akciğerlere giren hava, bir solukta alınan hava ile dakikadaki soluk sayısının çarpımıdır; hacimler grafikte iki seviye arasındaki farktan okunur; egzersizde kapasiteler korunur, yedek hacimler değişir.','Grafikteki en yüksek değeri soluk hacmi sanmak; kapasiteleri değişen büyüklük sanmak.','orta','grafik',4,'ss-hacim-hesap','Hacim–zaman grafiği ve dakikada solunan hava')
kartla('K-ABSS2-04','Hemoglobin ve oksijen taşıma kapasitesi','Kanın oksijen taşıma kapasitesi hemoglobin miktarına ve hemoglobinin oksijenle birleşebilen kısmına bağlıdır; plazmada çözünen oksijenin kısmi basıncı bu kapasiteyle aynı şey değildir; CO2 ve H+ hemoglobinin ilgisini değiştirir.','Kısmi basıncı normal olan her kanın oksijeni yeterli taşıdığını sanmak; CO2 taşınmasında enzimin yerini karıştırmak.','zor','tablo',4,'ss-hb-tasima','Hemoglobin, oksijen taşıma ve CO₂ taşınması')
kartla('K-ABSS2-05','Solunumun kimyasal düzenlenmesi','Solunum hızı, kemoreseptörlerin algıladığı kan gazı ve pH değişimleriyle ayarlanır; O2 azalması belirli bir eşikten sonra belirgin etki yapar; CO2 ve pH değişimi ise küçük sapmalarda bile etkilidir.','Oksijen azlığının her düzeyde solunumu orantılı artırdığını sanmak.','orta','grafik',4,'ss-kemoreseptor','Kemoreseptörler ve solunum hızı')
kartla('K-ABSS2-06','Plevra ve akciğerin göğüs boşluğuna bağlılığı','Akciğerler plevra zarıyla örtülüdür; akciğerin göğüs duvarını izleyerek hacmini değiştirmesi plevra boşluğundaki basınca bağlıdır.','İki akciğerin tek ortak boşlukta olduğunu sanmak; diyafram kasılınca her akciğerin otomatik şiştiğini düşünmek.','zor','şekilli',4,'ss-pnomotoraks','Plevra basıncı ve akciğerin şişmesi')
B_HAVA=B('Soluk havasının bileşimi','soluk alınan hava ile soluk verilen havanın bileşimi, akciğerlerde gaz değişimi olduğu için farklıdır · azot gaz değişiminde belirgin rol almaz')
B_YUZ=B('Gaz değişimi hızı','gazlar alveol ile kılcal damar arasında difüzyonla geçer · geçiş hızı gaz değişim yüzeyinin özelliklerine ve kısmi basınç farkına bağlıdır · kan kılcal damarda sınırlı süre kalır')
B_HAST=B('Solunum hastalıkları','solunum hastalıkları hava yolunu ya da alveolleri etkileyebilir · bir hastalığın sonucu, etkilenen yapının normal işleviyle yorumlanır')
B_HESAP=B('Dakikada solunan hava','bir solukla alınan hava hacmi ile dakikadaki soluk sayısının çarpımı dakikada akciğerlere giren havayı verir · kapasiteler birkaç hacmin toplamıdır')
B_HBK=B('Taşıma kapasitesi','oksijeni asıl taşıyan hemoglobindir, plazmada çözünen oksijen çok azdır · taşınan oksijen miktarı hemoglobin miktarına ve onun oksijen bağlayabilen kısmına bağlıdır')
B_KEMO=B('Solunumun kimyasal düzenlenmesi','kemoreseptörler kandaki gaz ve pH değişimini algılar · bu bilgi omurilik soğanındaki solunum merkezine iletilir · merkez solunum kaslarının çalışma hızını ayarlar')
B_PLV=B('Plevra','akciğerler plevra denen zarla örtülüdür · plevra boşluğundaki basınç akciğerin göğüs duvarını izlemesini etkiler')
B_HAC=B('Solunum hacimleri','soluk hacmi dinlenme soluğunda alınıp verilen havadır · vital kapasite soluk hacmi ile iki yedek hacmin toplamıdır · egzersizde soluk hacmi artar, vital kapasite sabit kalır')
B_HB=B('Hemoglobin','her hemoglobin molekülü dört hem grubu taşır ve en çok dört O₂ bağlar · oksihemoglobin oranı O₂ bağlama bölgelerinin dolu kısmını gösterir · CO hemoglobine O₂’den çok daha güçlü bağlanır')
B_CO2=B('CO₂ taşınması','CO₂ kanda bikarbonat, karbaminohemoglobin ve çözünmüş CO₂ biçimlerinde taşınır · alyuvardaki karbonik anhidraz CO₂ ile suyun tepkimesini hızlandırır · H⁺ hemoglobine bağlanabilir')
# =================== 01 · hava bileşimi tablosu · kolay · C ===================
HV_={'X':(21,'0,04',78),'Y':(16,'4',78)}
assert HV_['X'][0]>HV_['Y'][0] and float(HV_['X'][1].replace(',','.'))<float(HV_['Y'][1].replace(',','.')) and HV_['X'][2]==HV_['Y'][2]
SK1=tablo_svg(['Hava örneği','O₂ (%)','CO₂ (%)','N₂ (%)'],[[k,str(v[0]),v[1],str(v[2])] for k,v in HV_.items()])
dog1='Y örneği soluk verilen havadır; çünkü akciğerlerde O₂ kana geçmiş, CO₂ ise kandan alveol havasına geçmiştir.'
q('0001',tipId='ss-gaz-yuzey',tip='Hava bileşimi ve gaz değişim yüzeyi',z='kolay',alt='Soluk havasının bileşimi',kaz='Soluk alınan ve verilen havanın bileşimini karşılaştırarak akciğerlerdeki gaz değişimini yorumlar.',kalip='tablo',
 kart='K-ABSS2-01 (hava bileşimi) · iki hava örneğinin tanınması',
 metin='Tabloda, dinlenme hâlindeki sağlıklı bir insanın soluk alırken ve soluk verirken ölçülen hava örneklerinin yaklaşık gaz oranları verilmiştir. Örneklerden hangisinin soluk alınan, hangisinin soluk verilen hava olduğu belirtilmemiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog1,sira=yer('C',dog1,['X örneği soluk verilen havadır; çünkü akciğerlerde O₂ oranı yüksek olan hava kandan O₂ almıştır.','Y örneği soluk alınan havadır; çünkü solunum yolunda hava CO₂ ile zenginleşerek akciğerlere ulaşır.','Y örneği soluk verilen havadır; çünkü azot kana geçip geri verildiğinden iki örnekteki azot oranı aynıdır.','Y örneği soluk verilen havadır; çünkü bu havada O₂ tamamen tükenmiş ve yalnız CO₂ kalmıştır.']),
 yan=[('X örneği soluk verilen havadır; çünkü akciğerlerde O₂ oranı yüksek olan hava kandan O₂ almıştır.','Tabloda O₂ oranı X’te %21, Y’de %16’dır; akciğerde O₂ kana geçtiği için oranı düşen örnek Y’dir, kandan O₂ alınması ise gerçekleşmez.','bilgi'),
      ('Y örneği soluk alınan havadır; çünkü solunum yolunda hava CO₂ ile zenginleşerek akciğerlere ulaşır.','Y’de CO₂ oranı %4’tür; hava CO₂ ile alveol düzeyinde, gaz değişimi sonrasında zenginleşir ve bu hava soluk olarak verilir; soluk alınan havada CO₂ %0,04’tür.','bilgi'),
      ('Y örneği soluk verilen havadır; çünkü azot kana geçip geri verildiğinden iki örnekteki azot oranı aynıdır.','Azot gaz değişimine belirgin katılmaz; bu yüzden oranı %78 ile iki örnekte de aynı kalır. Aynı oran, azotun kana geçip geri verildiğini göstermez.','dikkat'),
      ('Y örneği soluk verilen havadır; çünkü bu havada O₂ tamamen tükenmiş ve yalnız CO₂ kalmıştır.','Tabloda Y’de O₂ hâlâ %16’dır; soluk verilen havada O₂ tükenmez, yalnız oranı azalır ve CO₂ oranı %4’e çıkar.','islem')],
 istenen='Tablodaki oranlara göre doğru olan yorum.',
 ip=['İki örnekte O₂ ve CO₂ oranlarının yönünü karşılaştır, azotun değişip değişmediğine de bak.'],
 bilgi=[B_HAVA,B_YUZ],
 ad=[A('Oranları karşılaştır','X’te O₂ %21 ve CO₂ %0,04, Y’de O₂ %16 ve CO₂ %4’tür; azot iki örnekte %78’dir.','O₂: 21 → 16 · CO₂: 0,04 → 4 · N₂: 78 = 78'),
     A('Gaz değişimini yorumla','Akciğerde O₂ kana geçer, CO₂ kandan alveole geçer; bu nedenle O₂ oranı azalan, CO₂ oranı artan hava soluk verilen havadır.','Y: soluk verilen hava'),
     A('Azotu değerlendir','Azot gaz değişiminde belirgin rol almadığından oranı iki örnekte de aynı kalır.','N₂ değişmez'),
     A('Yorumu seç','Y’nin soluk verilen hava olduğunu ve gaz geçiş yönlerini doğru açıklayan ifade seçilir.','Doğru ifade belirlendi')],
 puf='O₂ ve CO₂ oranları hangi yönde değişti, önce onu sapta.',sekil=SK1)
# =================== 02 · amfizem şeması · kolay · A ===================
b=[]
def alv(cx,cy,r,aralik=False):
    return f'\\draw[line width=1.1pt,fill=vurgu!15] ({cx},{cy}) circle ({r});'
for (x,y) in [(0,0),(.75,.1),(1.5,0),(.35,.7),(1.1,.75),(1.85,.7),(.0,-.7),(.75,-.65),(1.5,-.7)]:
    b.append(alv(x,y,.34))
b.append('\\draw[line width=1.1pt,fill=vurgu!15] (4.9,.55) circle (.8);\\draw[line width=1.1pt,fill=vurgu!15] (6.55,-.35) circle (.75);\\draw[line width=1.1pt,fill=vurgu!15] (4.95,-.85) circle (.45);')
b.append('\\node[font=\\normalsize\\bfseries] at (.9,-1.5) {I};\\node[font=\\normalsize\\bfseries] at (5.7,-1.5) {II};')
SK2=tk('\n'.join(b),.85)
dog2='Gaz değişimine ayrılan toplam yüzey alanı daralmıştır; bu nedenle birim zamanda kana geçen O₂ miktarı azalır.'
q('0002',tipId='ss-hastalik',tip='Solunum sistemi hastalıkları ve savunma',z='kolay',alt='Alveol hasarı',kaz='Alveol yapısının bozulmasının gaz değişim yüzeyi ve oksijen geçişi üzerindeki etkisini yorumlar.',kalip='şekilli',
 kart='K-ABSS2-02 (amfizem) · alveol sayısı ve yüzey alanı',
 metin='Şekilde, aynı büyütmeyle çizilmiş iki akciğer dokusu kesiti verilmiştir. I sağlıklı bir bireyin dokusunu, II ise amfizem hastalığı olan bir bireyin dokusunu göstermektedir. Her iki kesit de aynı doku hacmini temsil etmektedir.\nBuna göre, II numaralı dokuda aşağıdakilerden hangisinin gerçekleşmesi beklenir?',
 dogru=dog2,sira=yer('A',dog2,['Alveol sayısı azaldığı için her alveolde gaz geçişi hızlanır ve kanın O₂ düzeyi artar.','Bronşların iç çapı daralır ve soluk borusundaki kıkırdak halkalar kaybolur.','Gaz değişimine ayrılan yüzey alanı daralır; ancak gazlar difüzyonla geçtiği için kana geçen O₂ miktarı değişmez.','Alveol duvarı kalınlaşır ve gazların geçmesi gereken mesafe uzar; yüzey alanı ise değişmez.']),
 yan=[('Alveol sayısı azaldığı için her alveolde gaz geçişi hızlanır ve kanın O₂ düzeyi artar.','Şekilde II’de alveol sayısı 9’dan 3’e inmiştir; toplam yüzey alanı daraldığından kana geçen O₂ artmaz, azalır.','islem'),
      ('Bronşların iç çapı daralır ve soluk borusundaki kıkırdak halkalar kaybolur.','Bronş daralması astımın özelliğidir; şekildeki değişim alveollerdedir ve soluk borusunun halkalarıyla ilgisi yoktur.','bilgi'),
      ('Gaz değişimine ayrılan yüzey alanı daralır; ancak gazlar difüzyonla geçtiği için kana geçen O₂ miktarı değişmez.','Difüzyonla geçen gaz miktarı yüzey alanıyla orantılıdır; alan daralınca birim zamanda geçen O₂ azalır.','dikkat'),
      ('Alveol duvarı kalınlaşır ve gazların geçmesi gereken mesafe uzar; yüzey alanı ise değişmez.','Şekilde duvar kalınlığı değil alveol sayısı ve yüzey alanı değişmiştir; alveollerin birleşmesi yüzey alanını belirgin biçimde küçültür.','bilgi')],
 istenen='II numaralı dokuda beklenen sonuç.',
 ip=['Alveollerin sayısı ve boyutu değişince gaz değişimine açık toplam yüzeyin nasıl etkilendiğini düşün.'],
 bilgi=[B('Gaz değişimi hızı','gazlar alveol ile kılcal damar arasında difüzyonla geçer · geçen gaz miktarı gaz değişim yüzeyinin özelliklerine bağlıdır')],
 ad=[A('Şekilleri karşılaştır','I’de çok sayıda küçük alveol, II’de az sayıda büyük boşluk vardır.','I: 9 küçük alveol · II: 3 büyük boşluk'),
     A('Yüzey alanına çevir','Küçük keseciklerin toplam yüzeyi, aynı hacimdeki birkaç büyük boşluğun yüzeyinden çok daha geniştir.','II’de toplam yüzey alanı azalır'),
     A('Gaz geçişini yorumla','Difüzyonla geçen gaz miktarı yüzey alanıyla orantılıdır; alan azalınca birim zamanda kana geçen O₂ azalır.','O₂ geçişi azalır')],
 puf='Aynı hacimde küçük keseciklerin mi yoksa büyük boşlukların mu toplam yüzeyi geniştir?',sekil=SK2)
# =================== 03 · öncüllü · orta · E ===================
ST3={'I':(True,'Soluk yolunu döşeyen epitelde mukus salgılayan ve kirpikli hücreler bulunur; kirpiklerin hareketi mukusu ve ona yapışan parçacıkları ağıza doğru taşır.','Kirpikli ve mukus salgılayan epitel, toz ve mikropları tutup ağıza doğru ileten bir temizleme düzeneğidir.'),
     'II':(False,'Sigara dumanı, soluk yolundaki kirpiklerin hareketini hızlandırarak mukusla birlikte parçacıkların dışarı atılmasını kolaylaştırır.','Sigara dumanı kirpiklerin hareketini bozar; mukusla tutulan parçacıklar atılamaz ve birikir.'),
     'III':(True,'Astımda bronş ve bronşçukların iç çapı daralır; bu nedenle havanın akciğerlere girip çıkması güçleşir.','Bronş ve bronşçukların daralması hava akışına direnç oluşturur ve soluk alıp vermeyi güçleştirir.')}
dg,sr,yn,ad=onc(ST3,True,'E',seed=11)
q('0003',tipId='ss-hastalik',tip='Solunum sistemi hastalıkları ve savunma',z='orta',alt='Hava yolu savunması ve astım',kaz='Soluk yolunun savunma düzeneği ile sigara ve astımın etkilerine ilişkin yargıları değerlendirir.',kalip='öncüllü',
 kart='K-ABSS2-02 (savunma, sigara, astım) · kirpik, mukus ve bronş daralması',
 metin=onctxt('İnsanda solunum yolu ve solunum yolu hastalıklarıyla ilgili olarak aşağıdaki yargılar verilmiştir.',ST3,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Kirpik hareketinin ne işe yaradığını ve her hastalıkta hangi yapının etkilendiğini ayrı ayrı düşün.'],bilgi=[B_HAST],ad=ad,
 puf='Her yargıyı etkilenen yapı ve onun normal işleviyle karşılaştır.')
# =================== 04 · hacim–zaman grafiği · orta · B ===================
TV_R,TV_E,F_R,F_E,BAZ=500,1500,12,24,2500
PR,PE=5.0,2.5
assert 60/PR==F_R and 60/PE==F_E
VR=lambda t:BAZ+TV_R/2*(1-math.cos(2*math.pi*t/PR)); VE=lambda t:BAZ+TV_E/2*(1-math.cos(2*math.pi*t/PE))
assert abs(max(VR(i/100) for i in range(0,1001))-(BAZ+TV_R))<1 and abs(max(VE(i/100) for i in range(0,1001))-(BAZ+TV_E))<1
DAK=TV_E*F_E/1000; assert DAK==36 and TV_R*F_R/1000==6
D4=[6,72,96,156]; assert 4000*24/1000==96 and 1500*48/1000==72 and (BAZ+TV_E+BAZ)*24/1000==156 and TV_E*F_E/1000==36
sr_=' '.join(f'({i/10:.1f},{VR(i/10):.0f})' for i in range(0,101)); se_=' '.join(f'({i/10:.1f},{VE(i/10):.0f})' for i in range(0,101))
b=['\\begin{axis}[width=8.2cm,height=5.4cm,xmin=0,xmax=10,ymin=2000,ymax=4500,xtick={0,2,4,6,8,10},ytick={2500,3000,3500,4000},axis lines=left,xlabel={Zaman (sn)},ylabel={Akciğerdeki hava hacmi (mL)},yticklabel style={/pgf/number format/.cd,1000 sep={}},ymajorgrids=true,grid style={gray!30},tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt}]',
   f'\\addplot[vurgu!80!black] coordinates {{{sr_}}};',f'\\addplot[black] coordinates {{{se_}}};',
   '\\node[font=\\small\\bfseries,vurgu!80!black] at (axis cs:2.1,3260) {X};\\node[font=\\small\\bfseries] at (axis cs:.55,3900) {Y};','\\end{axis}']
SK4=graf('\n'.join(b))
q('0004',tipId='ss-hacim-hesap',tip='Hacim–zaman grafiği ve dakikada solunan hava',z='orta',alt='Dakikada solunan hava',kaz='Hacim–zaman grafiğinden soluk hacmi ve soluk sayısını okuyarak dakikada akciğerlere giren havayı hesaplar.',kalip='grafik',
 kart='K-ABSS2-03 (hacim–zaman) · soluk hacmi × soluk sayısı',
 metin='Aynı kişinin akciğerlerindeki hava hacminin 10 saniyelik iki kayıttaki değişimi grafikte verilmiştir. X eğrisi dinlenme hâlindeki, Y eğrisi şiddetli egzersiz sırasındaki kaydı göstermektedir. Her iki kayıtta da soluk alıp verme düzenli bir biçimde tekrarlanmıştır.\nBuna göre, bu kişinin şiddetli egzersiz sırasında bir dakikada akciğerlerine giren hava hacmi kaç litredir?',
 dogru=DAK,yan=[(D4[0],'10 saniyelik kayıt bir dakika sanılmış; Y’de bu sürede 4 soluk vardır ve 4 × 1,5 = 6 litre bulunmuştur.','dikkat'),
   (D4[1],'Hacim tepe noktaları ile vadiler ayrı soluk sayılmış; dakikada 48 soluk alınarak 1,5 × 48 = 72 litre bulunmuştur.','islem'),
   (D4[2],'Soluk hacmi yerine grafikteki en yüksek değer (4000 mL) alınmış; 4 × 24 = 96 litre bulunmuştur.','islem'),
   (D4[3],'Soluk hacmi yerine en yüksek ve en düşük değerler toplanmış; (4000 + 2500) mL × 24 = 156 litre bulunmuştur.','islem')],
 istenen='Egzersiz sırasında dakikada akciğerlere giren hava hacmi (L).',
 ip=['Bir solukta ne kadar hava hareket ediyor, dakikada kaç soluk var?'],
 bilgi=[B_HESAP,B_HAC],
 ad=[A('Y eğrisinde soluk hacmini oku','Bir soluk alınırken hacim 2500 mL’den 4000 mL’ye çıkar; bu farkı soluk hacmi verir.','4000 − 2500 = 1500 mL'),
     A('Soluk sayısını bul','10 saniyelik kayıtta Y eğrisi 4 tam tekrar yapar; bir dakika bunun 6 katıdır.','4 × 6 = 24 soluk/dk'),
     A('Dakikada giren havayı hesapla','Soluk hacmi ile dakikadaki soluk sayısı çarpılır.','1500 × 24 = 36000 mL'),
     A('Birimi çevir','1000 mL bir litredir.','36000 mL = 36 L')],
 puf='Bir soluğun hacmini ve dakikadaki soluk sayısını ayrı ayrı bulup çarp.',sekil=SK4)
# =================== 05 · hemoglobin tablosu öncüllü · orta · D ===================
HB5={'K':(15,100,97),'L':(8,100,97),'M':(15,100,55)}
assert HB5['L'][0]<HB5['K'][0] and HB5['L'][1]==HB5['K'][1] and HB5['L'][2]==HB5['K'][2] and HB5['M'][2]<HB5['K'][2] and HB5['M'][0]==HB5['K'][0]
KAP={k:v[0]*v[2]/100 for k,v in HB5.items()}  # taşınan O2 ~ Hb × doygunluk
assert KAP['L']<KAP['K'] and KAP['M']<KAP['K'] and KAP['L']<KAP['M']
SK5=tablo_svg(['Birey','Hb (g/100 mL kan)','Plazmada O₂ (mmHg)','Oksihemoglobin (%)'],[[k,str(v[0]),str(v[1]),str(v[2])] for k,v in HB5.items()])
ST5={'I':(True,'L bireyinde hemoglobin molekülleri normal ölçüde O₂ taşımasına karşın, kanın toplam O₂ taşıma kapasitesi K bireyininkinden düşüktür.','L’de hemoglobin miktarı 8 g olduğundan, her molekül %97 doygun olsa bile taşınan toplam O₂ azdır.'),
     'II':(False,'M bireyinde plazmadaki O₂ kısmi basıncı normal olduğundan, kanın O₂ taşıma kapasitesi K bireyininkiyle aynıdır.','M’de hemoglobinin büyük kısmı CO ile birleştiğinden oksihemoglobin %55’e düşmüştür; plazmada O₂ kısmi basıncı normal olsa da taşıma kapasitesi azdır.'),
     'III':(False,'L bireyindeki düşük taşıma kapasitesi, alveolden plazmaya O₂ geçişinin bozulduğunu gösterir.','L’de plazmadaki O₂ kısmi basıncı K ile aynıdır (100 mmHg); alveolden geçiş bozulmamış, hemoglobin miktarı azalmıştır.')}
dg,sr,yn,ad=onc(ST5,False,'D',seed=13)
q('0005',tipId='ss-hb-tasima',tip='Hemoglobin, oksijen taşıma ve CO₂ taşınması',z='orta',alt='Oksijen taşıma kapasitesi',kaz='Hemoglobin miktarı, oksihemoglobin oranı ve kısmi basınç verilerinden oksijen taşıma kapasitesini yorumlar.',kalip='öncüllü',
 kart='K-ABSS2-04 (taşıma kapasitesi) · hemoglobin miktarı ve CO',
 metin='Tabloda, sağlıklı bir bireyin (K), demir eksikliğine bağlı olarak hemoglobin miktarı azalmış bir bireyin (L) ve karbonmonoksit zehirlenmesi geçiren bir bireyin (M) kanından, aynı koşullarda alınan örneklerde ölçülen değerler verilmiştir. Oksihemoglobin, toplam hemoglobinin O₂ bağlamış kısmını göstermektedir.\nBu bireylerle ilgili olarak,\n'+'\n'.join(f'{r}. {ST5[r][1]}' for r in ST5)+'\nyargılarından hangileri yanlıştır?',
 dogru=dg,sira=sr,yan=yn,istenen='Yanlış olan yargıların belirlenmesi.',
 ip=['Kısmi basıncın, hemoglobin miktarının ve oksihemoglobin oranının kapasiteyi hangi yönden etkilediğini ayrı ayrı yorumla.'],bilgi=[B_HBK,B_HB],ad=ad,
 puf='Her yargıyı tablodaki üç sütunla ayrı ayrı karşılaştır.',sekil=SK5)
# =================== 06 · kemoreseptör grafikleri · orta · D (yanlış) ===================
VO={120:6,100:6,80:6.5,60:7,50:10,40:15,30:23}; VC={30:3,40:6,45:9,50:13,55:19,60:26}
d_o=lambda a,b:VO[b]-VO[a]; d_c=lambda a,b:VC[b]-VC[a]
assert d_o(100,80)==0.5 and d_c(40,45)==3 and d_o(100,80)<d_c(40,45)           # A doğru
assert VC[50]/VC[40]>2 and VC[50]==13                                           # B doğru
assert VO[60]-VO[100]==1 and VO[60]-VO[100]<2                                   # C doğru
assert (VO[50]-VO[100])==4 and (VC[50]-VC[40])==7 and 4<7                       # D yanlış (O2 daha büyük artış diyor)
po=' '.join(f'({k},{v})' for k,v in sorted(VO.items())); pc=' '.join(f'({k},{v})' for k,v in sorted(VC.items()))
ax='width=5.3cm,height=4.6cm,ymin=0,ymax=28,ytick={0,5,10,15,20,25},axis lines=left,ymajorgrids=true,grid style={gray!30},tick label style={font=\\footnotesize},label style={font=\\small},title style={font=\\small\\bfseries},every axis plot/.append style={line width=1.5pt,smooth}'
SK6=graf(f'''\\begin{{axis}}[name=a,{ax},xmin=20,xmax=120,xtick={{20,40,60,80,100,120}},xlabel={{Alveol O$_2$ kısmi basıncı (mmHg)}},ylabel={{Dakikada solunan hava (L)}},title={{K}}]
\\addplot[vurgu!80!black] coordinates {{{po}}};
\\end{{axis}}
\\begin{{axis}}[at={{(a.east)}},xshift=1.3cm,anchor=west,{ax},xmin=30,xmax=60,xtick={{30,40,50,60}},xlabel={{Alveol CO$_2$ kısmi basıncı (mmHg)}},title={{L}}]
\\addplot[black] coordinates {{{pc}}};
\\end{{axis}}''')
dog6='O₂ kısmi basıncının 100 mmHg’den 50 mmHg’ye düşmesi, CO₂ kısmi basıncının 40 mmHg’den 50 mmHg’ye çıkmasından daha büyük bir solunum artışına yol açar.'
q('0006',tipId='ss-kemoreseptor',tip='Kemoreseptörler ve solunum hızı',z='orta',alt='O₂ ve CO₂ uyaranlarının etkisi',kaz='İki gazın kısmi basıncı ile solunum arasındaki ilişkiyi grafiklerden okuyarak karşılaştırır.',kalip='grafik',
 kart='K-ABSS2-05 (kemoreseptör) · O₂ eşik etkisi ve CO₂ etkisinin karşılaştırılması',
 metin='Bir araştırmada gönüllünün alveol havasındaki O₂ ve CO₂ kısmi basınçları birbirinden bağımsız olarak değiştirilmiştir. K grafiğinde CO₂ kısmi basıncı 40 mmHg’de, L grafiğinde ise O₂ kısmi basıncı 100 mmHg’de sabit tutulmuş; her koşulda dakikada solunan hava ölçülmüştür.\nBuna göre, aşağıdakilerden hangisi yanlıştır?',
 dogru=dog6,sira=yer('D',dog6,['O₂ kısmi basıncı 100 mmHg’den 80 mmHg’ye düşerken dakikada solunan havadaki değişim, CO₂ kısmi basıncı 40 mmHg’den 45 mmHg’ye çıkarkenki değişimden küçüktür.','CO₂ kısmi basıncı 40 mmHg’den 50 mmHg’ye çıktığında dakikada solunan hava, başlangıçtakinin iki katından fazla olur.','O₂ kısmi basıncının 100 mmHg’den 60 mmHg’ye düşmesi dakikada solunan havayı 2 L’den az artırır.','Her iki grafikteki artış, kemoreseptörlerin uyarılmasıyla solunum merkezinin solunum kaslarını daha hızlı çalıştırmasına bağlıdır.']),
 yan=[('O₂ kısmi basıncı 100 mmHg’den 80 mmHg’ye düşerken dakikada solunan havadaki değişim, CO₂ kısmi basıncı 40 mmHg’den 45 mmHg’ye çıkarkenki değişimden küçüktür.','K’de 6 L’den 6,5 L’ye 0,5 L, L’de 6 L’den 9 L’ye 3 L artış vardır; 0,5 < 3 olduğundan ifade doğrudur.','islem'),
   ('CO₂ kısmi basıncı 40 mmHg’den 50 mmHg’ye çıktığında dakikada solunan hava, başlangıçtakinin iki katından fazla olur.','L’de 40 mmHg’de 6 L olan değer 50 mmHg’de 13 L olur; 13 > 2 × 6 olduğundan ifade doğrudur.','islem'),
   ('O₂ kısmi basıncının 100 mmHg’den 60 mmHg’ye düşmesi dakikada solunan havayı 2 L’den az artırır.','K’de 100 mmHg’de 6 L, 60 mmHg’de 7 L okunur; artış 1 L’dir ve ifade doğrudur. O₂ etkisi eşik değerin altında belirginleşir.','dikkat'),
   ('Her iki grafikteki artış, kemoreseptörlerin uyarılmasıyla solunum merkezinin solunum kaslarını daha hızlı çalıştırmasına bağlıdır.','Kemoreseptörler kandaki gaz değişimini algılar, bilgiyi omurilik soğanındaki solunum merkezine iletir; merkez solunum kaslarını hızlandırır, ifade doğrudur.','bilgi')],
 istenen='Grafiklere göre yanlış olan ifade.',
 ip=['Her ifadedeki iki kısmi basınç aralığını grafikte ayrı ayrı bulup artış miktarlarını karşılaştır.'],
 bilgi=[B_KEMO,B_HESAP],
 ad=[A('Değerleri oku','İfadelerde geçen kısmi basınçlara karşılık gelen dakikada solunan hava değerleri iki grafikten okunur.','K: 100→6, 80→6,5, 60→7, 50→10 · L: 40→6, 45→9, 50→13'),
     A('Artışları hesapla','O₂ için 100 mmHg’den 50 mmHg’ye gidişteki artış ile CO₂ için 40 mmHg’den 50 mmHg’ye gidişteki artış bulunur.','O₂: 10 − 6 = 4 L · CO₂: 13 − 6 = 7 L'),
     A('Karşılaştır','O₂ düşüşünün neden olduğu artış 4 L, CO₂ artışının neden olduğu artış 7 L olduğundan O₂’nin etkisi daha büyük değildir.','4 < 7 → ilgili ifade yanlıştır')],
 puf='Her ifadedeki iki aralığı grafikte ayrı ayrı bulup farkları karşılaştır.',sekil=SK6)
# =================== 07 · pnömotoraks şekli · zor · B ===================
b=['\\draw[line width=1.3pt,rounded corners=22pt] (-3.7,-1.7) rectangle (3.1,2.3);',
   '\\draw[line width=1.6pt,vurgu!80!black] (-3.7,-1.15) .. controls (-1.6,-.35) and (1.6,-.35) .. (3.1,-1.15);',
   '\\fill[gray!35,rounded corners=3pt] (-3.55,-.85) rectangle (-2.9,2.0);',
   '\\draw[line width=1.1pt,fill=vurgu!18] (-.45,-.55) .. controls (-.3,.6) and (-.35,1.7) .. (-.7,2.0) .. controls (-1.5,2.1) and (-2.6,1.8) .. (-2.85,.7) .. controls (-2.95,-.1) and (-2.7,-.7) .. (-2.4,-.85) .. controls (-1.6,-.6) and (-1.0,-.65) .. (-.45,-.55) -- cycle;',
   '\\draw[line width=1.1pt,fill=vurgu!18] (.45,-.55) .. controls (.3,.6) and (.35,1.7) .. (.7,2.0) .. controls (1.5,2.1) and (2.6,1.8) .. (2.85,.7) .. controls (2.95,-.1) and (2.7,-.7) .. (2.4,-.85) .. controls (1.6,-.6) and (1.0,-.65) .. (.45,-.55) -- cycle;',
   '\\draw[line width=1.2pt] (-.1,-.5) -- (-.1,2.0) -- (.15,2.0) -- (.15,-.5) -- cycle;',
   '\\node[font=\\normalsize\\bfseries] at (-1.6,.85) {K};\\node[font=\\normalsize\\bfseries] at (1.6,.85) {L};\\node[font=\\normalsize\\bfseries] at (-3.22,.6) {M};\\node[font=\\small] at (-.3,-1.45) {diyafram};',
   '\\draw[line width=.9pt,-{Stealth[length=2mm]}] (-4.6,1.0) -- (-3.4,1.0);']
SK7=tk('\n'.join(b),.9)
dog7='L akciğeri şişerek hava alır; K akciğerinin hacmi ise diyafram kasılsa da belirgin biçimde artmaz.'
q('0007',tipId='ss-pnomotoraks',tip='Plevra basıncı ve akciğerin şişmesi',z='zor',alt='Plevra boşluğu ve pnömotoraks',kaz='Plevra boşluğundaki basıncın akciğerin göğüs duvarını izlemesindeki rolünü yeni bir durumda yorumlar.',kalip='şekilli',
 kart='K-ABSS2-06 (plevra) · ayrı plevra boşlukları ve basınç',
 metin='Şekilde, göğüs duvarında oluşan bir yırtıktan geçen havanın yalnız sağ plevra boşluğunu (M) doldurduğu ve bu boşlukta basıncın atmosfer basıncına eşitlendiği bir bireyin göğüs kafesi kesiti verilmiştir. K sağ akciğeri, L sol akciğeri göstermektedir; solunum kasları normal çalışmaktadır.\nBuna göre, bu bireyin soluk alması sırasında aşağıdakilerden hangisi gerçekleşir?',
 dogru=dog7,sira=yer('B',dog7,['Her iki akciğer de şişer; çünkü iki akciğer tek bir plevra boşluğu içinde yer alır.','L akciğeri şişmez; çünkü bir plevra boşluğundaki basınç kaybı diğer akciğerin plevra basıncını da atmosfer düzeyine çıkarır.','K akciğeri de şişer; çünkü akciğer dokusundaki kas lifleri kasılarak akciğeri genişletir.','K akciğeri de aynı oranda şişer; çünkü akciğerler diyaframa doğrudan bağlıdır ve onunla birlikte aşağı iner.']),
 yan=[('Her iki akciğer de şişer; çünkü iki akciğer tek bir plevra boşluğu içinde yer alır.','Her akciğer ayrı bir plevra kesesi içindedir; M’deki basınç değişimi L’nin plevra boşluğunu etkilemez ve K’nin şişmesini de sağlayamaz.','bilgi'),
      ('L akciğeri şişmez; çünkü bir plevra boşluğundaki basınç kaybı diğer akciğerin plevra basıncını da atmosfer düzeyine çıkarır.','Plevra boşlukları birbirinden ayrı olduğundan L’nin plevra basıncı atmosferin altında kalır; diyafram kasılınca L şişer.','dikkat'),
      ('K akciğeri de şişer; çünkü akciğer dokusundaki kas lifleri kasılarak akciğeri genişletir.','Akciğer dokusunda akciğeri kendi başına genişletecek kas lifi yoktur; akciğer, plevra basıncı sayesinde göğüs duvarını izleyerek şişer.','bilgi'),
      ('K akciğeri de aynı oranda şişer; çünkü akciğerler diyaframa doğrudan bağlıdır ve onunla birlikte aşağı iner.','Akciğer diyaframa doğrudan bağlı değildir; plevra boşluğundaki atmosferin altındaki basınç akciğeri duvara tutar. M’de bu basınç bozulduğundan K diyaframı izlemez.','islem')],
 istenen='Soluk alma sırasında gerçekleşen durum.',
 ip=['Akciğerin göğüs duvarını izlemesini sağlayan koşulun hangi akciğerde sürdüğünü düşün.'],
 bilgi=[B_PLV,B_HAC],
 ad=[A('Durumu belirle','M’de basınç atmosfere eşitlenmiş, L’nin plevra boşluğu ise sağlam kalmıştır.','K: plevra basıncı = atmosfer · L: atmosferin altında'),
     A('Akciğerin şişme koşulunu hatırla','Akciğerin göğüs duvarını izleyerek şişmesi, plevra boşluğundaki basıncın atmosferin altında olmasına bağlıdır.','Plevra basıncı düşük → akciğer duvarı izler'),
     A('Her akciğeri değerlendir','L’de koşul sürdüğünden L şişer; K’de koşul bozulduğundan K esnekliğiyle küçük kalır.','L şişer · K şişmez')],
 puf='Göğüs duvarını izleme koşulunu her akciğer için ayrı ayrı sına.',sekil=SK7)
# =================== 08 · hemoglobin sayısal tablo · zor · C ===================
HB8={'K':(100,96,75),'L':(50,96,56)}
SAY=lambda n,a,v:Fr(n*4*(a-v),100)
BK,BL=SAY(*HB8['K']),SAY(*HB8['L']); assert (BK,BL)==(84,80) and BK-BL==4
yan8=[(1,'Her hemoglobinin yalnız 1 O₂ bağladığı varsayılmış; K için 21, L için 20 bulunup fark 1 alınmıştır.','islem'),
      (2,'Her hemoglobinin 2 O₂ bağladığı varsayılmış; K için 42, L için 40 bulunup fark 2 alınmıştır.','islem'),
      (188,'Bırakılan yerine dokudan dönen kandaki bağlı O₂ alınmış; K için 100 × 4 × 0,75 = 300, L için 50 × 4 × 0,56 = 112 ve fark 188 bulunmuştur.','dikkat'),
      (192,'Bırakılan yerine akciğerden çıkan kandaki bağlı O₂ alınmış; K için 100 × 4 × 0,96 = 384, L için 50 × 4 × 0,96 = 192 ve fark 192 bulunmuştur.','dikkat')]
assert 100*4*Fr(75,100)-50*4*Fr(56,100)==188 and 100*4*Fr(96,100)-50*4*Fr(96,100)==192 and 100*(96-75)/100==21 and 50*(96-56)/100==20
SK8=tablo_svg(['Birey','Hb molekülü (milyon)','Akciğer çıkışı (%)','Doku çıkışı (%)'],[[k,str(v[0]),str(v[1]),str(v[2])] for k,v in HB8.items()])
q('0008',tipId='ss-hb-tasima',tip='Hemoglobin, oksijen taşıma ve CO₂ taşınması',z='zor',alt='Dokulara bırakılan oksijen',kaz='Hemoglobin sayısı ve oksihemoglobin oranlarından dokulara bırakılan oksijen miktarını hesaplar.',kalip='tablo',
 kart='K-ABSS2-04 (taşıma) · hemoglobin sayısı, doygunluk farkı ve O₂ bağlama bölgesi',
 metin='Tabloda, K ve L bireylerinin eşit hacimli kan örneklerindeki hemoglobin molekülü sayıları ile bu örneklerin akciğerden çıkışta ve dokulardan dönüşte ölçülen oksihemoglobin yüzdeleri verilmiştir. Oksihemoglobin yüzdesi, hemoglobinlerin O₂ bağlayabileceği toplam bölgenin O₂ ile dolu olan kısmını göstermektedir.\nBuna göre, kan örneklerinin dokulara bıraktığı O₂ molekülü sayısı K’de L’dekinden kaç milyon fazladır?',
 dogru=4,yan=yan8,istenen='K ile L örneklerinin dokulara bıraktığı O₂ molekülü sayıları arasındaki fark (milyon).',
 ip=['Dokuya bırakılan O₂’nin hangi iki niceliğe bağlı olduğunu düşün.'],
 bilgi=[B_HB,B_HBK],
 ad=[A('Bırakılan yüzdeyi bul','Dokuya bırakılan O₂, akciğerden çıkan ve dokudan dönen kandaki oksihemoglobin yüzdelerinin farkıdır.','K: 96 − 75 = 21 · L: 96 − 56 = 40'),
     A('Bölge sayısını hesapla','Her hemoglobin 4 O₂ bağlayabildiğinden toplam bağlama bölgesi hemoglobin sayısının 4 katıdır.','K: 100 × 4 = 400 · L: 50 × 4 = 200'),
     A('Bırakılan O₂’yi hesapla','Bölge sayısı bırakılan yüzdeyle çarpılır.','K: 400 × 0,21 = 84 · L: 200 × 0,40 = 80'),
     A('Farkı al','K’nin bıraktığı sayıdan L’ninki çıkarılır.','84 − 80 = 4 milyon')],
 puf='Önce her örnek için bırakılan yüzdeyi, sonra O₂ bağlama bölgesi sayısını bul.',sekil=SK8)
# =================== 09 · gaz değişim hızı · orta · E (olumsuz) ===================
dog9='Alveol duvarı ile kılcal damar duvarı arasındaki doku mesafesinin artması'
q('0009',tipId='ss-gaz-yuzey',tip='Hava bileşimi ve gaz değişim yüzeyi',z='orta',alt='Gaz geçiş hızını etkileyen etmenler',kaz='Difüzyon hızını belirleyen etmenleri alveol–kılcal damar sistemine uygulayarak yorumlar.',kalip='düz',
 kart='K-ABSS2-01 (gaz değişim yüzeyi) · difüzyon hızını artıran ve azaltan etmenler',
 metin='Akciğerlerde alveol havası ile kılcal damar kanı arasındaki gaz geçişi difüzyonla gerçekleşir. Birim zamanda geçen gaz miktarı, difüzyona uygun koşulların değişmesiyle artabilir ya da azalabilir.\nAşağıdakilerden hangisi alveol ile kılcal damar arasındaki gaz geçiş hızını artırmaz?',
 dogru=dog9,sira=yer('E',dog9,['Gaz değişimine katılan alveol yüzeyinin genişlemesi','Soluk alınan havadaki O₂ kısmi basıncının artması','Alveol duvarını oluşturan hücre tabakasının incelmesi','Kandaki CO₂ kısmi basıncının alveol havasındakine göre artması']),
 yan=[('Gaz değişimine katılan alveol yüzeyinin genişlemesi','Yüzey genişleyince difüzyonla geçen gaz miktarı artar; bu durum geçiş hızını artırır.','bilgi'),
      ('Soluk alınan havadaki O₂ kısmi basıncının artması','Alveolde O₂ kısmi basıncı arttıkça kanla arasındaki fark büyür ve O₂ geçişi hızlanır.','bilgi'),
      ('Alveol duvarını oluşturan hücre tabakasının incelmesi','Duvar incelince gazların kat edeceği mesafe kısalır ve geçiş hızlanır.','bilgi'),
      ('Kandaki CO₂ kısmi basıncının alveol havasındakine göre artması','CO₂ geçişi kısmi basıncın yüksek olduğu kandan alçak olduğu alveole doğrudur; fark büyüdükçe CO₂ çıkışı hızlanır.','dikkat')],
 istenen='Gaz geçiş hızını artırmayan durum.',
 ip=['Difüzyon hızını yüzey alanı, mesafe ve kısmi basınç farkının nasıl etkilediğini düşün.'],
 bilgi=[B_YUZ],
 ad=[A('Etmenleri belirle','Difüzyon hızı yüzey alanı ile artar, gazların kat ettiği mesafe ile azalır, kısmi basınç farkı büyüdükçe artar.','Alan ↑ · mesafe ↓ · fark ↑ → hız ↑'),
     A('Seçenekleri değerlendir','Dört seçenek bu etmenlerden birini hızı artıracak yönde değiştirir; mesafeyi artıran seçenek ise hızı düşürür.','Mesafe ↑ → hız ↓'),
     A('Sonucu belirle','Hızı artırmayan durum, gazların geçeceği doku mesafesinin artmasıdır.','Doğru seçenek belirlendi')],
 puf='Her seçeneğin yüzey alanı, mesafe ya da kısmi basınç farkından hangisini nasıl değiştirdiğine bak.')
# =================== 10 · egzersiz öncüllü · zor · A ===================
T0,T1,F0,F1=400,1600,15,25
assert T0*F0/1000==6 and T1*F1/1000==40 and T1/T0==4 and Fr(40,6)!=4
ST10={'I':(True,'Egzersiz sırasında hücresel solunumun hızlanması kanda CO₂ düzeyini artırır; pH’ın düşmesi kemoreseptörleri uyarır ve solunum merkezi aracılığıyla solunum kasları hızlandırılır.','Artan CO₂ ve düşen pH kemoreseptörlerden solunum merkezine, oradan solunum kaslarına giden bir yol izler; hız artar.'),
      'II':(False,'Soluk hacmi 4 kat arttığı için dakikada solunan hava miktarı da 4 katına çıkmıştır.','Soluk sayısı da 15’ten 25’e çıktığından dakikada solunan hava 6 L’den 40 L’ye, yani 4 katından fazla artmıştır.'),
      'III':(False,'Egzersizdeki solunum artışının başlıca nedeni, kanda O₂ kısmi basıncının eşik değerin altına inmesidir.','Egzersizde solunum artışını başlatan başlıca uyaran O₂ azalması değil, CO₂ artışı ve pH düşüşüdür.')}
dg,sr,yn,ad=onc(ST10,True,'A',seed=17); assert dg=='Yalnız I'
q('0010',tipId='ss-kemoreseptor',tip='Kemoreseptörler ve solunum hızı',z='zor',alt='Egzersizde solunum',kaz='Egzersizde solunum hızı ve hacimlerindeki değişimi düzenleme ve hesaplama bilgileriyle birlikte yorumlar.',kalip='öncüllü',
 kart='K-ABSS2-05 (kemoreseptör) · K-ABSS2-03 (hacim hesabı) · egzersizde solunum',
 metin=onctxt('Sağlıklı bir bireyin dinlenme hâlinde soluk hacmi 400 mL ve dakikadaki soluk sayısı 15, hızlı koşu sırasında ise soluk hacmi 1600 mL ve dakikadaki soluk sayısı 25’tir. Bu birey ile ilgili olarak aşağıdaki yargılar ileri sürülmüştür.',ST10,'Buna göre, bu yargılardan hangileri doğrudur?'),
 dogru=dg,sira=sr,yan=yn,istenen='Doğru olan yargıların belirlenmesi.',
 ip=['Dakikada solunan havayı iki durum için ayrı hesapla ve solunumu hızlandıran uyaranın hangisi olduğunu düşün.'],bilgi=[B_KEMO,B_HESAP],ad=ad,
 puf='Her yargıyı hesaplayarak ya da düzenleme zincirine bakarak ayrı ayrı sına.')
# =================== yaz ===================
for qq in P.ANA: qq['kardes']=None
P.yaz(os.path.join(BD,'solunumsisiki-1.json'),'/tmp/bos-solunumsisiki.json')
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=P.k))['kartlar'].append(c['id'])
json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT Biyoloji çıkmış soruları (yalnız mantık), MEB 11. sınıf biyoloji.',kartlar=H.KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','absolunumsisiki.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
