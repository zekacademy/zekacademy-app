"""TYT Kimya · Atom ve Yapısı · ek paket (atomiki): 22 soru, kardeş yok, ipucu 1.
Katman dağılımları, öncül doğruluğu ve çeldirici değerler Python'da hesaplanır; şekiller bu değerlerden üretilir."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
KONU_='Atom ve Yapısı'; UK='kim|Atom ve Yapısı'
H.KONU=KONU_
P=Parti('atomiki',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2026 TYT Kimya (yalnız mantık) · MEB 9. sınıf Atom ve Yapısı'
# ---------------- kartlar ----------------
TIP={}
def kt(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    kart(f'K-KMAT2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-at2-{tipad}',tip,KY); TIP[n]=(f'km-at2-{tipad}',tip)
kt('01','Temel tanecikler','Proton +1 ve ≈1 akb, nötron 0 ve ≈1 akb, elektron −1 ve ihmal edilecek kütlede (≈1/1836 akb).','Nötron ile elektronu yük bakımından karıştırmak; elektronu protondan ağır sanmak.','kolay','tablo',2,'tanecik','Temel taneciklerin yük ve kütlesi')
kt('02','Rutherford deneyi','Alfa saçılması: çoğu geçer (atom büyük ölçüde boş), azı sapar/geri döner (küçük yoğun artı yüklü çekirdek).','Elektron katmanlarını ve Thomson’ın düzgün artı yük dağılımını bu deneye bağlamak.','orta','öncüllü',3,'rutherford','Alfa saçılması deneyi')
kt('03','Modellerin yetersizliği','Her model yeni gözlem karşısında bir şeyi açıklayamaz: Dalton elektronu, Thomson çekirdeği, Rutherford enerji katmanlarını.','Yeniliği getiren modelle açıklayamayan modeli karıştırmak.','orta','öncüllü',3,'model-acik','Modellerin açıklayamadığı')
kt('04','Tanecik tablosu','Tabloda proton–elektron karşılaştırmasıyla iyon türü, proton ve kütle numarasıyla izo-kavramlar belirlenir.','Elektron sayısı eşit diye izotop demek; kütle numarasını hesaplamadan izobar demek.','orta','öncüllü',3,'tablo-iyon','Tabloda proton, nötron, elektron')
kt('05','Kütle numarası','Kütle numarası proton + nötron; elektronlar kütleye katılmaz. İyon türü p ile e karşılaştırılarak bulunur.','Elektronu da kütle numarasına eklemek.','kolay','düz',2,'iyon-kutle','İyon türü ve kütle numarası')
kt('06','Katman diyagramı','Diyagramdaki elektron toplamı nötr atomda atom numarasını verir; kütle numarası p + n.','Son katmandaki elektronu proton sanmak.','orta','şekilli',3,'katman-hesap','Katman diyagramından hesap')
kt('07','Katman diyagramı yorumu','Çekirdek yükü ile elektron toplamı karşılaştırılarak nötr atom, katyon ve anyon ayrılır.','Aynı katman dağılımını aynı tanecik sanmak.','orta','öncüllü',3,'katman-iyon','Katman diyagramlarında nötr atom ve iyon')
kt('08','Katmanlara dağılım','İlk 20 elementte K: 2, L: 8, M: 8, sonra N; üçüncü katman 8’le dolar.','M katmanını 18’e kadar doldurmak.','orta','düz',3,'dagilim','Katmanlara elektron dağılımı')
kt('09','İzotop özellikleri','İzotoplar aynı proton ve elektrona, farklı nötron ve kütleye sahiptir; kimyasal özellikleri benzer, fiziksel özellikleri farklıdır.','İzotopların kimyasal özelliğinin farklı olduğunu sanmak.','orta','düz',2,'izotop-ozellik','İzotop atomların özellikleri')
kt('10','Enerji düzeyi diyagramı','Üst düzeye çıkış enerji soğurur, alt düzeye iniş ışıma verir; düzeyler arası fark büyükse ışıma enerjisi büyük.','Soğurma ile yayma yönünü karıştırmak.','orta','öncüllü',3,'enerji','Enerji düzeyi diyagramı')
kt('11','Uyarılmış atom','Uyarılmış atomda elektron sayısı değişmez; bir elektron üst katmana çıkmıştır, dönerken ışıma olur.','Uyarılmayı iyonlaşma ile karıştırmak.','kolay','düz',2,'uyarilmis','Temel hâl ve uyarılmış hâl')
kt('12','İzotop–izoton–izobar tablosu','Atom ve nötron sayısından kütle numarası hesaplanır; izo-kavramlar sayılara göre karşılaştırılır.','Atom numarası eşit olanı izoton sanmak.','orta','öncüllü',3,'izo-tablo','İzo-kavramlar tablosu')
kt('13','İzobar ve iyon','İzobarda kütle numarası eşit; atom numarası nötronla bulunur; iyon elektronu yükle düzeltilir.','Anyonun elektron sayısını yük kadar eksik hesaplamak.','zor','düz',4,'izobar-iyon','İzobar atom ve anyon')
kt('14','Model şemaları','Thomson: artı yük içinde elektronlar; Rutherford: yoğun çekirdek; Bohr: enerji katmanları.','Şematik çizimleri modellerle karıştırmak.','orta','şekilli',3,'model-sema','Model şemalarını yorumlama')
kt('15','Model sırası','Dalton → Thomson → Rutherford → Bohr; her model önceki modelin açıklayamadığını açıklar.','Rutherford ile Thomson’ın sırasını karıştırmak.','kolay','düz',2,'kronoloji','Atom modellerinin sırası')
kt('16','Atom–iyon karşılaştırması','Atomdan iyona geçişte proton ve nötron sabit; elektron ve katman sayısı değişebilir.','Katyonun proton sayısının da azaldığını sanmak.','orta','tablo',3,'atom-iyon','Nötr atom ile iyon karşılaştırması')
kt('17','İzoelektronik iyonlar','Elektron sayısı eşit iyonlarda proton sayıları yükten bulunur; sonra katman sayıları karşılaştırılır.','Elektron sayısını atom numarası sanmak.','zor','öncüllü',4,'izoelektronik','İzoelektronik iyonların atomları')
kt('18','Toplam tanecik','Toplam tanecik sayısı ve ilişki cümlelerinden denklem kurulur; kütle numarası p + n.','Elektronu da kütle numarasına katmak.','orta','hikâyeli',3,'toplam','Toplam tanecik denklemi')
kt('19','Anyon katman diyagramı','Anyonda elektron = proton + yük; kütle numarası proton ve nötron toplamıdır.','Yükü ters yönde işlemek.','zor','şekilli',4,'anyon-hesap','Anyon katman diyagramından kütle numarası')
kt('20','Uyarılmış atom diyagramı','İki diyagramda elektron toplamı eşit ve dizilim farklıysa biri uyarılmıştır; üst katmandan alt katmana dönüşte ışıma olur.','Farklı dizilimi farklı element sanmak.','zor','öncüllü',4,'uyarilmis-sema','Uyarılmış atomun katman diyagramı')
kt('21','Tablodan tanecik yorumu','Her tanecik için p, n, e hesaplanıp iyon türü, izo-kavram ve izoelektroniklik değerlendirilir.','Her taneciği nötr atom saymak.','zor','tablo',4,'tablo-yorum','Tanecik tablosundan çıkarım')
kt('22','Işıma','Elektronlar enerji alınca üst katmana çıkar; alt katmana dönerken ışık yayar. Atomun proton ve kütle numarası değişmez.','Işımayı çekirdek tepkimesi sanmak.','kolay','hikâyeli',2,'isima','Işıma ve uyarılma')
GRP={'model':('Atom modelleri',['02','03','14','15']),'katman':('Katman diyagramı ve dağılımı',['06','07','08','19']),
 'uyarilmis':('Uyarılmış atom ve ışıma',['10','11','22','20']),'tabloizo':('Tablodan tanecik ve izo-kavramlar',['04','12','21','09']),
 'iyontemel':('İyon türü ve atom–iyon karşılaştırması',['05','16']),'iyonhesap':('İyonlu tanecik hesapları',['13','17','18']),'tanecik':('Temel taneciklerin yük ve kütlesi',['01'])}
for g_,(ad_,ns_) in GRP.items():
    for n_ in ns_:
        TIP[n_]=(f'km-at2-{g_}',ad_)
        c_=[c for c in H.KARTLAR if c['id']==f'K-KMAT2-{n_}'][0]; c_['tipId']=f'km-at2-{g_}'; c_['tip']=ad_
assert len(TIP)==22
# ---------------- ortak yardımcılar ----------------
RM='I II III'.split()
ORD=['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III','II ve III','I, II ve III']
NAMES={'Yalnız I':{0},'Yalnız II':{1},'Yalnız III':{2},'I ve II':{0,1},'I ve III':{0,2},'II ve III':{1,2},'I, II ve III':{0,1,2}}
def kk(n,ne): return f'K-KMAT2-{n} ({TIP[n][1].lower()}) · {ne}'
def q(no,n,ad,**k):
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=TIP[n][0],tip=TIP[n][1],kart=kk(n,k.pop('ne')),**k)
def onc(no,n,bag,stm,secenek,tail,ne,**k):
    """stm: (metin, doğru_mu, açıklama, yanlış_değerlendirme_cümlesi). Doğruluk tek yerde; anahtar, adım ve çeldirici oradan."""
    truth={i for i,s in enumerate(stm) if s[1]}
    dogru=[a for a in secenek if NAMES[a]==truth]; assert len(dogru)==1 and len(secenek)==5 and len(set(secenek))==5
    assert [ORD.index(a) for a in secenek]==sorted(ORD.index(a) for a in secenek),'şık sırası'
    dogru=dogru[0]; yan=[]
    for a in secenek:
        if a==dogru: continue
        S=NAMES[a]; parts=[]
        for i in sorted(S^truth):
            parts.append(f'{RM[i]}’yi {"doğru" if i in S else "yanlış"} saymış; {stm[i][3]}')
        yan.append((a,' '.join(parts),'bilgi'))
    metin=bag+'\n'+'\n'.join(f'{RM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+tail
    ad=[A(f'{RM[i]}. ifadeyi değerlendir',s[2],f'{RM[i]}: {"doğru" if s[1] else "yanlış"}') for i,s in enumerate(stm)]
    ad.append(A('Sonucu birleştir','Doğru bulunan ifadeler birlikte seçilir.',dogru))
    q(no,n,ad,ne=ne,metin=metin,dogru=dogru,sira=list(secenek),yan=yan,**k)
def tek(S,dogru_ind):
    """S: (şık metni, doğru_mu, hata cümlesi). Tek doğru şık assert edilir; yan listesi üretir."""
    assert sum(1 for s in S if s[1])==1
    d=[s for s in S if s[1]][0]
    return d[0],[(s[0],s[2],'bilgi') for s in S if not s[1]]
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
ARR='-{Stealth[length=2.2mm,width=1.8mm]}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def kab(Z):
    s=[]; k=[2,8,8,8]
    for c in k:
        t=min(c,Z);
        if t<=0: break
        s.append(t); Z-=t
    assert Z==0 and len(s)<=4
    # ilk 20 element: 19 ve 20 için 2,8,8,1/2
    return s
for Z_,e_ in [(7,[2,5]),(12,[2,8,2]),(17,[2,8,7]),(19,[2,8,8,1]),(20,[2,8,8,2]),(11,[2,8,1]),(15,[2,8,5]),(16,[2,8,6]),(13,[2,8,3]),(18,[2,8,8]),(9,[2,7]),(10,[2,8])]:
    assert kab(Z_)==e_,(Z_,kab(Z_))
def bohr(cx,cy,sayilar,etiket,alt='',r0=.9,dr=.5):
    s=f'\\draw[fill=vurgu!15,thick] ({cx},{cy}) circle (.45); \\node at ({cx},{cy}) {{\\small {etiket}}};'
    for i,n in enumerate(sayilar):
        r=r0+dr*i; s+=f'\\draw[thick] ({cx},{cy}) circle ({r:.2f});'
        for k in range(n):
            a=90+360*k/n+17*i; s+=f'\\fill ({cx+r*math.cos(math.radians(a)):.3f},{cy+r*math.sin(math.radians(a)):.3f}) circle (.11);'
    if alt: s+=f'\\node[below] at ({cx},{cy-(r0+dr*(len(sayilar)-1))-.12:.2f}) {{{alt}}};'
    return s
def sec(S,gerek):
    pass
# ======================= 0001 · temel taneciklerin yük ve kütlesi · kolay · tablo =======================
tab=[['X','+1','1'],['Y','0','1'],['Z','−1','1/1836']]
SK=tablo_svg(['Tanecik','Yük (elektron yükü biriminde)','Kütle (akb)'],tab)
S=[('Proton, nötron, elektron',True,''),
   ('Nötron, proton, elektron',False,'Yük sütununu okumamış; yüksüz taneciği ilk sıraya, artı yüklüyü ikinci sıraya yazmış.'),
   ('Proton, elektron, nötron',False,'Çok küçük kütleli taneciği Y’ye, yüksüz olanı Z’ye yazmış; kütle ve yük sütunlarını karıştırmış.'),
   ('Elektron, nötron, proton',False,'Artı yüklü ve çok küçük kütleli taneciklerin yerini değiştirmiş; protonu elektronla karıştırmış.'),
   ('Elektron, proton, nötron',False,'X’e elektronu, Y’ye protonu yazmış; yük sütunundaki işaretleri ters okumuş, yüksüz olanı Z’ye yazmış.')]
d,y=tek(S,1)
q('0001','01',[A('Yüke bak','Artı yük protona, yüksüzlük nötrona, eksi yük elektrona aittir.','X: +1 · Y: 0 · Z: −1'),A('Kütleye bak','Elektronun kütlesi proton ve nötronunkinin binde birinden küçüktür.','Z: 1/1836 akb'),A('Eşleştir','Yük ve kütle birlikte taneciği belirler.','X proton · Y nötron · Z elektron')],
 ne='X, Y ve Z’nin yük ve kütlesi tabloda',z='kolay',alt='Atomun Temel Tanecikleri',kaz='Proton, nötron ve elektronu yük ve kütle bilgisinden ayırt eder.',kalip='tablo',sekil=SK,
 metin='Bir öğrenci, atomu oluşturan üç temel taneciği birbirine karıştırmamak için onlara X, Y ve Z adlarını vermiş ve her birinin yükünü ile kütlesini (akb biriminde, yaklaşık değerlerle) aşağıdaki tabloda toplamıştır. Öğretmeni, tablodaki verilerin taneciklerin adlarını belirlemeye yettiğini söylemiştir.\nBuna göre X, Y ve Z taneciklerinin adları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=d,sira=[S[0][0],S[1][0],S[2][0],S[3][0],S[4][0]],yan=y,istenen='X, Y ve Z taneciklerinin adları.',
 ip=['Tablodaki iki sütunu birlikte oku.'],
 bilgi=[B('Temel tanecikler','proton ve nötronun kütleleri yaklaşık eşittir, elektron ise onlara göre çok hafiftir. Yükün işareti, taneciğin hangi tür olduğunu belirlemeye yardım eder')],
 puf='Yük işareti protonu ve elektronu, kütle ise elektronu ayırır; nötron yüksüzdür.')
assert [x[0] for x in S].index('Proton, nötron, elektron')==0
# ======================= 0002 · Rutherford saçılma deneyi · orta · öncüllü + şekil =======================
R_=3.3; ys=[-1.0,-.75,-.5,-.25,0,.25,.5,.75,1.0]
g='\\draw[fill=gray!35,thick] (-5.6,-.4) rectangle (-4.6,.4); \\node[below,align=center] at (-5.1,-.45) {$\\alpha$ ışını\\\\ kaynağı};'
g+=f'\\draw[thick] (165:{R_}) arc (165:-165:{R_}); \\node[right,align=left] at (22:{R_+.05}) {{ışıldayan\\\\ ekran}};'
g+='\\draw[fill=gray!60] (-.07,-1.35) rectangle (.07,1.35); \\node[above,align=center] at (0,1.4) {ince altın\\\\ levha};'
for y_ in ys:
    g+=f'\\draw[{ARR}] (-4.6,{y_}) -- (-.07,{y_});'
    if y_==1.0: ang=35
    elif y_==-1.0: ang=205
    elif y_==-.75: ang=-30
    else: ang=None
    if ang is None:
        g+=f'\\draw[{ARR}] (.07,{y_}) -- ({math.sqrt(R_**2-y_**2):.3f},{y_});'
    else:
        c,s_=math.cos(math.radians(ang)),math.sin(math.radians(ang))
        # yay ile kesişim: (0.07,y)+t(c,s), |p|=R
        bb=(.07*c+y_*s_); t=-bb+math.sqrt(bb*bb-(.07**2+y_**2-R_**2))
        g+=f'\\draw[{ARR}] (.07,{y_}) -- ({.07+t*c:.3f},{y_+t*s_:.3f});'
SK=tk(g)
onc('0002','02','Rutherford ve çalışma arkadaşları, çok ince bir altın levhayı hızlı alfa (α) parçacıklarıyla bombardıman etmiş; levhadan geçen ya da saparak dönen parçacıkların, çevredeki ışıldayan ekranda bıraktığı izleri incelemiştir. Deneyin şematik görünümü şekilde verilmiştir.',
 [('Atomun artı yükü, atom hacmine düzgün biçimde dağılmıştır.',False,'Artı yük küçük bir çekirdekte toplanmışsa parçacıklar çoğunlukla geçer, azı sapar; düzgün dağılmış artı yük bu sonucu vermez.','Thomson modelindeki düzgün dağılımı bu deneyin sonucu sanmış.'),
  ('Bazı parçacıkların geri dönmesi, atomda artı yüklü ve çok yoğun bir bölge bulunduğunu gösterir.',True,'Artı yüklü alfa parçacıkları, aynı yüklü yoğun bir çekirdeğe yaklaşınca itilir ve geri döner.','geri dönen parçacıkların yoğun çekirdeğe işaret ettiğini görmemiş.'),
  ('Elektronlar, çekirdek çevresinde belirli enerjili katmanlarda dolanır.',False,'Enerji katmanları fikri Bohr modeline aittir; saçılma deneyi katman sayısı hakkında bilgi vermez.','katman fikrini Rutherford’un deneyinin sonucu sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'Buna göre bu deneyin sonuçlarıyla ilgili yukarıdaki ifadelerden hangileri doğrudur?',
 ne='altın levha deneyi ve alfa parçacığı yolları',z='orta',alt='Atom Modelleri',kaz='Alfa saçılması deneyinin sonuçlarından çekirdeğin varlığını çıkarır.',kalip='öncüllü',sekil=SK,
 istenen='Deney sonuçlarıyla uyumlu doğru ifadeler.',
 ip=['Şekilde izlerin yönlerine ve sayılarına bak.'],
 bilgi=[B('Alfa parçacıkları','alfa parçacıkları artı yüklüdür; aynı yüklü bir bölgeye yaklaşınca itilirler')],
 puf='Geçenler boşluğu, geri dönenler küçük yoğun artı yüklü çekirdeği gösterir.')
# ======================= 0003 · modellerin açıklayamadığı · orta · öncüllü =======================
onc('0003','03','Atom modelleri, gözlemlerin artmasıyla birbirini izleyen aşamalarda geliştirilmiştir. Her model, bir öncekinin açıklayamadığı bazı sonuçları açıklamış, ancak yeni gözlemler karşısında kendisi de yetersiz kalmıştır. Bir öğretmen, öğrencilerinden modellerin yetersizliklerini yorumlamalarını istemiştir.',
 [('Dalton modeli, atomun elektron içerdiğini açıklayamaz.',True,'Dalton atomu içi dolu, bölünemeyen küre sayar; elektronların varlığı bu modelde yoktur.','Dalton’un atomu bölünemez saymasının elektronla çeliştiğini görmemiş.'),
  ('Thomson modeli, alfa saçılması deneyinde bazı parçacıkların geri dönmesini açıklayamaz.',True,'Artı yük düzgün dağılmışsa yoğun bir merkez yoktur; geri dönüş ancak yoğun çekirdekle açıklanır.','Thomson’ın modelinin geri dönüşü de açıkladığını sanmış.'),
  ('Rutherford modeli, atomun merkezinde artı yüklü bir çekirdek bulunduğunu açıklayamaz.',False,'Çekirdeği ilk öneren ve saçılma deneyiyle açıklayan Rutherford modelidir.','çekirdeği Rutherford’dan önceki bir modele ait sanmış.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','I ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='üç modelin açıklayamadığı',z='orta',alt='Atom Modelleri',kaz='Atom modellerinin açıklayamadığı sonuçları ayırt eder.',kalip='öncüllü',
 istenen='Doğru olan ifadeler.',
 ip=['Her modelin kendinden öncekine göre neyi eklediğini düşün.'],
 bilgi=[B('Modellerin gelişimi','her model, kendinden önceki modelin açıklayamadığı bir gözlemi açıklamak için önerilmiştir; yeni gözlemler gelince o model de yetersiz kalmıştır')],
 puf='Bir modelin açıklayamadığı şey, genellikle kendinden sonraki modelin yeniliğidir.')
# ======================= 0004 · tablo p-n-e · orta · öncüllü =======================
tb={'X':(17,18,17),'Y':(17,20,18),'Z':(19,20,18)}
Atm={k:v[0]+v[1] for k,v in tb.items()}
izobar=lambda a,b:Atm[a]==Atm[b] and tb[a][0]!=tb[b][0]
izoelek=lambda a,b:tb[a][2]==tb[b][2]
kat=lambda a:tb[a][0]>tb[a][2]
assert (izobar('X','Y'),izoelek('Y','Z'),kat('Z'))==(False,True,True) and Atm=={'X':35,'Y':37,'Z':39}
SK=tablo_svg(['Tanecik','Proton sayısı','Nötron sayısı','Elektron sayısı'],[[k,*map(str,v)] for k,v in tb.items()])
onc('0004','04','Bir kimya laboratuvarında, X, Y ve Z olarak adlandırılan üç taneciğin proton, nötron ve elektron sayıları belirlenmiş ve aşağıdaki tabloya yazılmıştır. Taneciklerin bir kısmı nötr atom, bir kısmı iyondur.',
 [('X ile Y izobardır.',izobar('X','Y'),'İzobarda kütle numaraları eşit olmalıdır; X’in 35, Y’nin 37’dir.','proton sayıları eşit diye aynı tür saymış, kütle numaralarını (35 ve 37) karşılaştırmamış.'),
  ('Y ile Z izoelektroniktir.',izoelek('Y','Z'),'İkisinin de elektron sayısı 18’dir; elektron sayısı eşit tanecikler izoelektroniktir.','elektron sayılarının eşit olduğunu fark etmemiş.'),
  ('Z katyondur.',kat('Z'),'Z’nin protonu elektronundan fazladır; bu durum artı yüklü iyondur.','proton ve elektron sayılarını karşılaştırmamış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='tablodaki üç tanecik',z='orta',alt='Atomun Temel Tanecikleri',kaz='Proton, nötron ve elektron sayılarından iyon türünü ve izo-kavramları belirler.',kalip='öncüllü',sekil=SK,
 istenen='Doğru ifadeler.',
 ip=['Her tanecik için kütle numarasını ve proton–elektron karşılaştırmasını ayrı ayrı yap.'],
 bilgi=[B('İyon ve izo-kavramlar','proton > elektron ise katyon, proton < elektron ise anyondur. İzobarda kütle numarası, izoelektronikte elektron sayısı eşittir. Örnek: O²⁻ ile Ne’nin ikisi de 10 elektron taşır, izoelektroniktir')],
 puf='Önce her taneciğin türünü (p ile e) ve kütle numarasını (p + n) yaz, sonra ifadelere bak.')
# ======================= 0005 · iyon türü ve kütle numarası · kolay =======================
p5,n5,e5=9,10,10; A5=p5+n5; assert A5==19 and e5>p5 and p5+e5==19 and n5+e5==20 and p5+n5+e5==29
S=[('Kütle numarası 19 olan anyon',True,''),
   ('Kütle numarası 19 olan katyon',False,'Elektron sayısının proton sayısından fazla olduğunu görmemiş; elektron fazlası anyondur.'),
   ('Kütle numarası 19 olan nötr atom',False,'Elektron ile protonun eşit olduğunu varsaymış; oysa elektron sayısı 1 fazladır.'),
   ('Kütle numarası 20 olan anyon',False,'Kütle numarasına fazla elektronu da eklemiş; elektronlar kütle numarasına katılmaz.'),
   ('Kütle numarası 29 olan katyon',False,'Proton, nötron ve elektronun hepsini kütle numarasında saymış; ayrıca elektron fazlasını katyon sanmış.')]
d,y=tek(S,0)
q('0005','05',[A('Kütle numarası','Kütle numarası proton ve nötron sayılarının toplamıdır.','A = 9 + 10 = 19'),A('Yükü karşılaştır','Elektron proton sayısından büyüktür.','e = 10 > p = 9'),A('Sonuç','Elektron fazlası eksi yüklü taneciği, yani anyonu gösterir.','kütle numarası 19 · anyon')],
 ne='çekirdek ve elektron verileri',z='kolay',alt='Atomun Temel Tanecikleri',kaz='Proton ve nötrondan kütle numarasını, proton–elektron farkından iyon türünü belirler.',kalip='düz',
 metin='Bir öğrenci, çekirdeğinde 9 proton ve 10 nötron bulunan, çekirdek dışında ise 10 elektron taşıyan bir taneciği incelemektedir. Öğretmeni, elektronların kütlesinin proton ve nötronun kütlesine göre ihmal edilebilecek kadar küçük olduğunu hatırlatmıştır.\nBuna göre bu tanecik için aşağıdakilerden hangisi doğrudur?',
 dogru=d,sira=[S[1][0],S[2][0],S[3][0],S[0][0],S[4][0]],yan=y,istenen='Taneciğin kütle numarası ve türü.',
 ip=['Çekirdekteki taneciklere ve çekirdek dışındaki taneciklerin sayısına ayrı ayrı bak.'],
 bilgi=[B('Kütle numarası ve iyon','kütle numarası = proton + nötron (elektron katılmaz). Elektron sayısı proton sayısından fazlaysa tanecik anyondur. Örnek: 8 proton, 8 nötron, 10 elektronlu tanecik: kütle numarası 16, anyon')],
 puf='Kütle numarası çekirdektekileri sayar; iyon türü için elektronu protonla karşılaştır.')
# ======================= 0006 · katman diyagramından kütle numarası · orta · şekil =======================
c6=kab(15); assert c6==[2,8,5]; Z6=sum(c6); n6=16; A6=Z6+n6
assert (Z6,A6)==(15,31) and n6+c6[-1]==21 and Z6+Z6+n6==46
SK=tk(bohr(0,0,c6,'X','Nötr X atomu'))
q('0006','06',[A('Elektron sayısı','Diyagramdaki elektronlar katman katman sayılır.','2 + 8 + 5 = 15'),A('Proton sayısı','Nötr atomda proton sayısı elektron sayısına eşittir.','p = 15'),A('Kütle numarası','Proton ve nötron sayıları toplanır.','A = 15 + 16 = 31')],
 ne='X atomunun katman diyagramı',z='orta',alt='Bohr Modeli ve Katman Dağılımı',kaz='Katman diyagramındaki elektronlardan atom numarasını, nötrondan kütle numarasını bulur.',kalip='şekilli',sekil=SK,
 metin='Bohr atom modeline göre çizilen ve şekilde katman diyagramı verilen nötr X atomunun çekirdeğinde 16 nötron bulunmaktadır. Çizimde yalnızca elektronlar gösterilmiş, çekirdekteki diğer taneciklerin sayısı yazılmamıştır.\nBuna göre X atomunun kütle numarası kaçtır?',
 dogru=A6,yan=[(15,'Atom numarasını (proton sayısını) kütle numarası sanmış; nötronları eklememiş.','bilgi'),(16,'Verilen nötron sayısını kütle numarası olarak almış.','bilgi'),(21,'Son katmandaki 5 elektronu protonmuş gibi nötronlara eklemiş.','islem'),(46,'Proton, elektron ve nötronun üçünü de toplamış; elektronlar kütle numarasına katılmaz.','bilgi')],
 istenen='X atomunun kütle numarası.',
 ip=['Önce şekildeki noktaları katman katman say.'],
 bilgi=[B('Katman diyagramı','her çember bir katmandır; noktalar elektronları gösterir. Nötr atomda toplam elektron = proton = atom numarası. Örnek: katmanlarında 2 ve 6 elektron olan nötr atomun atom numarası 8’dir')],
 puf='Katman diyagramındaki toplam elektron, nötr atomun atom numarasıdır.')
# ======================= 0007 · katman diyagramları · orta · öncüllü =======================
dgr={'A':(12,[2,8,2]),'B':(12,[2,8]),'C':(8,[2,8])}
assert all(kab(sum(v[1]))==v[1] for v in dgr.values())
nötr=lambda k:dgr[k][0]==sum(dgr[k][1]); anyon=lambda k:dgr[k][0]<sum(dgr[k][1]); esit=lambda a,b:sum(dgr[a][1])==sum(dgr[b][1])
assert (nötr('A'),anyon('B'),esit('B','C'))==(True,False,True)
g=bohr(0,0,dgr['A'][1],'12p','A')+bohr(4.4,0,dgr['B'][1],'12p','B')+bohr(7.8,0,dgr['C'][1],'8p','C')
SK=tk(g)
onc('0007','07','Şekilde A, B ve C taneciklerinin katman diyagramları verilmiştir. Her çekirdeğin içine proton sayısı yazılmıştır; noktalar elektronları göstermektedir.',
 [('A taneciği nötr atomdur.',nötr('A'),'A’da 12 proton ve 2 + 8 + 2 = 12 elektron vardır; sayılar eşit olduğundan nötrdür.','elektron noktalarını sayıp protonla karşılaştırmamış.'),
  ('B taneciği anyondur.',anyon('B'),'B’de 12 proton, 10 elektron vardır; elektron azlığı katyon oluşturur, anyon oluşturmaz.','elektron eksikliğini eksi yük sanmış.'),
  ('B ile C taneciklerinin elektron sayıları eşittir.',esit('B','C'),'İkisinde de katmanlarda 2 ve 8 elektron, toplam 10 elektron vardır.','proton sayıları farklı diye elektron sayılarını da farklı düşünmüş.')],
 ['Yalnız II','I ve II','I ve III','II ve III','I, II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='üç katman diyagramı (12p, 12p, 8p)',z='orta',alt='Bohr Modeli ve Katman Dağılımı',kaz='Katman diyagramlarında proton–elektron sayısını karşılaştırarak atom ve iyon türünü belirler.',kalip='öncüllü',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Her diyagramdaki noktaları toplayıp çekirdekteki proton sayısıyla karşılaştır.'],
 bilgi=[B('Atom, katyon, anyon','proton = elektron: nötr atom; proton > elektron: katyon; proton < elektron: anyon. Örnek: 11 proton, 10 elektronlu tanecik katyondur')],
 puf='Önce her diyagramın elektron toplamını yaz; türü proton–elektron karşılaştırması belirler.')
assert 'I ve III'
# ======================= 0008 · katmanlara dağılım yanlış · orta · olumsuz kök =======================
Dg=[(7,[2,5],True),(12,[2,8,2],True),(17,[2,8,7],True),(19,[2,8,9],False),(20,[2,8,8,2],True)]
for z_,dd,ok_ in Dg: assert (kab(z_)==dd)==ok_
sub=str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')
SY={7:'N',12:'Mg',17:'Cl',19:'K',20:'Ca'}
fm_=lambda z_,dd:f'{str(z_).translate(sub)}{SY[z_]}: '+', '.join(map(str,dd))
sira8=[fm_(z_,dd) for z_,dd,_ in Dg]
d8=[fm_(z_,dd) for z_,dd,ok_ in Dg if not ok_][0]
q('0008','08',[A('Kuralı hatırla','İlk 20 elementte katmanlar 2, 8, 8, sonra dördüncü katman sırasıyla dolar.','K: 2 · L: 8 · M: en çok 8'),A('Her atomu doldur','Atom numarası kadar elektronu bu sırayla yerleştir.','7: 2, 5 · 12: 2, 8, 2 · 17: 2, 8, 7 · 20: 2, 8, 8, 2'),A('Yanlışı bul','19 elektron için üçüncü katman 8’de kalır, dokuzuncu elektron dördüncü katmana geçer.','19: 2, 8, 8, 1 ≠ 2, 8, 9')],
 ne='beş atomun katman dağılımı',z='kolay',alt='Bohr Modeli ve Katman Dağılımı',kaz='İlk 20 elementin katmanlarındaki elektron dağılımını yazar ve hatalı dağılımı bulur.',kalip='düz',
 metin='Bohr atom modeline göre ilk 20 elementin atomlarında elektronlar, çekirdeğe en yakın K katmanından başlayarak sırasıyla K, L, M ve N katmanlarına yerleşir. Bir öğrenci, atom numaraları verilen beş nötr atomun elektron dağılımlarını (K, L, M, N sırasıyla) aşağıdaki gibi yazmıştır.\nBuna göre bu dağılımlardan hangisi yanlıştır?',
 dogru=d8,sira=sira8,yan=[(fm_(7,[2,5]),'Doğru yazılmış dağılımı yanlış sanmış; 7 elektron 2 ve 5 olarak iki katmana yerleşir.','bilgi'),(fm_(12,[2,8,2]),'Doğru dağılımı yanlış saymış; üçüncü katmana 2 elektron geçer.','bilgi'),(fm_(17,[2,8,7]),'Doğru dağılımı yanlış sanmış; 17 elektron 2, 8, 7 dizilir.','bilgi'),(fm_(20,[2,8,8,2]),'Üçüncü katmanın 8’den fazla alabileceğini sanıp dağılımı yanlış bulmuş.','bilgi')],
 istenen='Hatalı yazılan elektron dağılımı.',
 ip=['Her dağılımda elektron toplamını ve katman sırasını kontrol et.'],
 bilgi=[B('Katmanlara dizilim','K katmanı en çok 2, L en çok 8 elektron alır; ilk 20 elementte M katmanı 8 ile dolar, kalan elektronlar N katmanına geçer. Örnek: 13 elektron: 2, 8, 3')],
 puf='İlk 20 elementte 2, 8, 8 doluluğundan sonra elektronlar bir üst katmana geçer.')
# ======================= 0009 · izotop özellikleri · orta · düz =======================
S=[('Elektron sayıları birbirinden farklıdır.',False,'İzotopların proton sayısı aynı olduğundan nötr atomlarında elektron sayısı da aynıdır.'),
   ('Proton sayıları birbirinden farklıdır.',False,'İzotop atomlar aynı elemente aittir; proton sayıları aynıdır.'),
   ('Kimyasal özellikleri birbirinden farklıdır.',False,'Kimyasal özellikler elektron dizilimine bağlıdır; izotoplarda aynıdır.'),
   ('Atom numaraları farklı, kütle numaraları aynıdır.',False,'Bu izobar tanımıdır; izotoplarda atom numarası aynı, kütle numarası farklıdır.'),
   ('Nötron sayıları sırasıyla 10 ve 12’dir.',True,'')]
n_a,n_b=20-10,22-10; assert (n_a,n_b)==(10,12)
d,y=tek(S,4)
q('0009','09',[A('Atom numarası','Neonun atom numarası 10’dur; iki atomda da proton sayısı 10’dur.','p = 10 · 10'),A('Nötron sayıları','Kütle numarasından proton sayısı çıkarılır.','20 − 10 = 10 · 22 − 10 = 12'),A('Şıkları ele','Elektron ve proton sayıları ile kimyasal özellikler aynıdır; kütle numaraları farklıdır.','elektron, proton, kimyasal özellik: aynı'),A('Sonuç','Nötron sayılarını 10 ve 12 veren ifade doğrudur.','nötron: 10 ve 12')],
 ne='neonun iki atomu',z='orta',alt='İzotop, İzoton, İzobar',kaz='İzotop atomların proton, nötron ve elektron sayılarını ve özelliklerini karşılaştırır.',kalip='hikâyeli',
 metin='Doğada neonun başlıca iki izotopu ²⁰Ne ve ²²Ne atomlarıdır; neonun atom numarası 10’dur. Bir öğrenci, bu iki atomu çekirdek yapıları ve özellikleri bakımından karşılaştırmak istemektedir.\nBuna göre ²⁰Ne ve ²²Ne atomları için aşağıdakilerden hangisi doğrudur?',
 dogru=d,sira=[S[3][0],S[0][0],S[4][0],S[1][0],S[2][0]],yan=y,istenen='İki izotop atom için doğru ifade.',
 ip=['İzotop atomların hangi taneciğinin sayısı aynı kalıp hangisinin değiştiğini düşün.'],
 bilgi=[B('İzotop atomlar','proton sayıları (atom numaraları) aynı, nötron sayıları ve kütle numaraları farklı atomlardır. Elektron dizilimi aynı olduğundan kimyasal özellikleri benzer, kütle ve yoğunluk gibi fiziksel özellikleri farklıdır. Örnek: ¹²C ve ¹⁴C izotoptur')],
 puf='İzotoplarda değişen yalnız nötron sayısıdır; kimyasal özellikler aynı kalır.')
# ======================= 0010 · enerji düzeyi diyagramı · orta · öncüllü =======================
lev={'K':0,'L':1.6,'M':2.7,'N':3.4}
g='\\draw[ARR] (-.5,0) -- (-.5,4.1); \\node[rotate=90] at (-.85,2.1) {Enerji};'.replace('ARR',ARR)
for nm,yy in lev.items(): g+=f'\\draw[thick] (0,{yy}) -- (6.2,{yy}); \\node[right] at (6.3,{yy}) {{{nm} katmanı}};'
geç={1:('K','M',1.2),2:('M','L',3.1),3:('N','K',5.0)}
for k,(a,b,x) in geç.items():
    ya,yb=lev[a],lev[b]
    g+=f'\\draw[thick,{ARR}] ({x},{ya}) -- ({x},{yb}); \\node[fill=white,circle,inner sep=1pt] at ({x+.38},{ {1:.8,2:2.15,3:2.15}[k] }) {{\\textbf{{{k}}}}};'
SK=tk(g)
sogur=lambda k:lev[geç[k][1]]>lev[geç[k][0]]
fark=lambda k:abs(lev[geç[k][1]]-lev[geç[k][0]])
assert sogur(1) and not sogur(2) and not sogur(3)
onc('0010','10','Bir atomdaki elektron, dışarıdan enerji alırsa bulunduğu katmandan daha üst bir katmana çıkabilir; üst katmandan alt katmana inerken ise aldığı enerjiyi ışıma biçiminde verir. Şekilde bir atomun K, L, M ve N katmanlarına karşılık gelen enerji düzeyleri (ölçeksiz) ve elektronun üç geçişi gösterilmiştir.',
 [('1 numaralı geçişte atom enerji soğurur.',sogur(1),'K katmanından M katmanına çıkış, daha yüksek enerjili düzeye geçiştir; enerji gerekir.','üst katmana çıkışı ışıma sanmış.'),
  ('2 numaralı geçişte atom enerji soğurur.',sogur(2),'M katmanından L katmanına iniş daha düşük enerjili düzeye geçiştir; enerji ışıma olarak verilir.','üst ve alt düzeye geçişin yönünü karıştırmış.'),
  ('3 numaralı geçişte atom enerji soğurur.',sogur(3),'N katmanından K katmanına iniş daha düşük enerjili düzeye geçiştir; enerji ışıma olarak verilir.','alt katmana inişi enerji soğurma sanmış.')],
 ['Yalnız I','Yalnız II','I ve II','I ve III','II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='üç elektron geçişi',z='orta',alt='Uyarılmış Atom ve Işıma',kaz='Enerji düzeyi diyagramında soğurma ve ışıma geçişlerini ayırt eder.',kalip='öncüllü',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Her okun üst katmana mı alt katmana mı gittiğine bak.'],
 bilgi=[B('Enerji alışverişi','elektron enerji alınca üst katmana, enerji verince alt katmana geçer')],
 puf='Yukarı ok enerji alınmasını, aşağı ok enerji verilmesini (ışımayı) gösterir.')
# ======================= 0011 · uyarılmış hâl · kolay =======================
tem=kab(11); assert tem==[2,8,1]
S=[('2, 8, 1',False,'Bu, temel hâl dağılımıdır; elektronlar bulunabilecekleri en düşük enerjili katmanlardadır.'),
   ('2, 7, 2',True,''),
   ('2, 8',False,'Toplam elektron sayısı 10’dur; bir elektron yitirilmiş (iyon), atom uyarılmış değildir.'),
   ('2, 8, 2',False,'Toplam elektron sayısı 12’dir; atom uyarılmakla elektron kazanmaz.'),
   ('2, 8, 3',False,'Toplam elektron sayısı 13’tür; atom uyarılmakla elektron kazanmaz.')]
for s_ in S: pass
assert sum(map(int,'2,7,2'.split(',')))==11 and '2, 7, 2'!=', '.join(map(str,tem))
d,y=tek(S,1)
q('0011','11',[A('Elektron sayısı','Uyarılmış atomda toplam elektron sayısı değişmez.','toplam 11 elektron'),A('Temel hâl','En düşük enerjili dizilim temel hâldir.','2, 8, 1'),A('Uyarılmış hâl','Toplamı 11 olan ve temel hâlden farklı dizilim uyarılmıştır.','2, 7, 2')],
 ne='atom numarası 11 olan atom',z='kolay',alt='Uyarılmış Atom ve Işıma',kaz='Temel hâldeki atomun uyarılmış hâlini katman dizilimi üzerinde tanır.',kalip='düz',
 metin='Atom numarası 11 olan nötr bir atomun temel hâldeki elektron dizilimi 2, 8, 1’dir. Bir öğrenci, bu atom ısıtıldığında elektronlardan birinin bir üst katmana çıktığını ve atomun uyarıldığını okumuştur.\nBuna göre bu atomun uyarılmış hâline ait elektron dizilimi aşağıdakilerden hangisi olabilir?',
 dogru=d,sira=[S[1][0],S[2][0],S[3][0],S[0][0],S[4][0]],yan=y,istenen='Uyarılmış hâlin elektron dizilimi.',
 ip=['Her seçeneğin toplam elektron sayısını yaz.'],
 bilgi=[B('Uyarılmış atom','Bir elektronun daha yüksek enerjili katmana çıktığı atomdur; elektron sayısı değişmez. Örnek: temel hâli 2, 6 olan atomun uyarılmış hâli 2, 5, 1 olabilir')],
 puf='Uyarılmış atomda elektronlar yer değiştirir, sayıları değişmez.')
# ======================= 0012 · ışıma · kolay · hikâyeli =======================
S=[('Elektronlar üst katmana çıkarken ışıma yapar.',False,'Üst katmana çıkış için enerji gerekir; ışıma, elektron alt katmana dönerken olur.'),
   ('Uyarılmış atomda elektron sayısı, temel hâle göre artmıştır.',False,'Uyarılmada elektronlar yalnız yer değiştirir; elektron sayısı değişmez.'),
   ('Elektronların alt katmana dönmesi sırasında enerji ışık olarak yayılır.',True,''),
   ('Işıma yapan atomun proton sayısı azalır.',False,'Işıma elektronların katman değiştirmesiyle olur; çekirdekteki proton sayısı değişmez.'),
   ('Uyarılma sırasında atomun kütle numarası artar.',False,'Kütle numarası çekirdekteki taneciklere bağlıdır; uyarılmada çekirdek değişmez.')]
d,y=tek(S,2)
q('0012','22',[A('Olayı anla','Gazdan elektrik akımı geçince atomlardaki elektronlar enerji alır.','enerji alma: üst katmana çıkış'),A('Işımayı anla','Elektron alt katmana dönerken fazla enerjiyi ışık olarak verir.','alt katmana iniş: ışıma'),A('Şıkları ele','Üst katmana çıkış enerji gerektirir; elektron, proton ve kütle numarası değişmez.','ışımayı alt katmana dönüşle ilişkilendirmeyen ifadeler yanlış')],
 ne='neon lambası ışıması',z='kolay',alt='Uyarılmış Atom ve Işıma',kaz='Uyarılmış atomun ışıma yapma sürecini nitel olarak açıklar.',kalip='hikâyeli',
 metin='Neon gazıyla doldurulmuş bir cam tüpün uçlarına yüksek gerilim uygulandığında tüp turuncu-kırmızı renkli ışık yayar. Bu olayı inceleyen bir öğrenci, gaz atomlarındaki elektronların elektrik enerjisini alarak üst katmanlara çıktığını, bir süre sonra ise tekrar alt katmanlara döndüğünü öğrenmiştir.\nBuna göre bu olayla ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=d,sira=[S[0][0],S[1][0],S[3][0],S[4][0],S[2][0]],yan=y,istenen='Işıma olayıyla ilgili doğru ifade.',
 ip=['Enerjinin alınması ve verilmesi hangi katman geçişlerine karşılık gelir?'],
 bilgi=[B('Işıma','uyarılmış atom kararsızdır; fazla enerjisini yayarak temel hâle döner. Atomun çekirdeği değişmez')],
 puf='Elektron alt katmana iner, ışık yayılır; çekirdek hiç değişmez.')
# ======================= 0013 · izo-kavramlar tablosu · orta · öncüllü =======================
tb13={'A':(6,6),'B':(6,8),'C':(7,7),'D':(8,8)}
A13={k:v[0]+v[1] for k,v in tb13.items()}
izotop13=lambda a,b:tb13[a][0]==tb13[b][0] and A13[a]!=A13[b]
izobar13=lambda a,b:A13[a]==A13[b] and tb13[a][0]!=tb13[b][0]
izoton13=lambda a,b:tb13[a][1]==tb13[b][1] and tb13[a][0]!=tb13[b][0]
assert (izotop13('A','B'),izobar13('B','C'),izoton13('B','D'))==(True,True,True) and A13=={'A':12,'B':14,'C':14,'D':16}
assert not izoton13('A','C') and not izobar13('A','D')
SK=tablo_svg(['Atom','Atom numarası','Nötron sayısı'],[[k,*map(str,v)] for k,v in tb13.items()])
onc('0013','12','Bir öğrenci, dört farklı nötr atomun atom numarasını ve nötron sayısını aşağıdaki tabloya yazmış; kütle numaralarını ise hesaplamayı unutmuştur. Öğretmeni, izotop, izobar ve izoton kavramlarının bu tablo yardımıyla belirlenebileceğini söylemiştir.',
 [('A ile B izotoptur.',izotop13('A','B'),'İkisinin de atom numarası 6’dır; kütle numaraları 12 ve 14 olduğundan izotoptur.','atom numaralarının eşitliğini fark etmemiş.'),
  ('B ile C izobardır.',izobar13('B','C'),'İkisinin de kütle numarası 14’tür (6 + 8 ve 7 + 7); atom numaraları farklıdır.','kütle numaralarını proton ve nötron toplamıyla hesaplamamış.'),
  ('B ile D izotondur.',izoton13('B','D'),'İkisinin de nötron sayısı 8’dir; atom numaraları farklıdır.','nötron sayılarının eşitliğini görmemiş.')],
 ['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='A, B, C, D atomlarının tablosu',z='orta',alt='İzotop, İzoton, İzobar',kaz='Atom ve nötron sayılarından kütle numarasını bulup izotop, izobar, izoton ilişkilerini belirler.',kalip='öncüllü',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Her atomun kütle numarasını hesapla, sonra eşit olan sayının hangisi olduğuna göre kavramı seç.'],
 bilgi=[B('İzotop, izobar, izoton','izotop: atom numarası aynı; izobar: kütle numarası aynı; izoton: nötron sayısı aynı. Örnek: ⁴⁰Ar ile ⁴⁰Ca izobar, ²³Na ile ²⁴Mg izotondur (12 nötron)')],
 puf='Kütle numarasını p + n ile hesapla; eşit olan sayı kavramı belirler.')
# ======================= 0014 · izobar + anyon · zor =======================
eX=18; qX=2; pX=eX+qX; AX=40; nX=AX-pX; nY=25; AY=AX; pY=AY-nY; eY3=pY+3
assert (pX,nX,pY,eY3)==(20,20,15,18) and pY-3==12 and pY==15 and nY==25
q('0014','13',[A('X’in proton sayısı','X²⁺ iki elektron vermiştir; elektron sayısına 2 eklenince proton sayısı bulunur.','p(X) = 18 + 2 = 20'),A('Kütle numarası','İzobar atomların kütle numaraları eşittir.','A(Y) = A(X) = 40'),A('Y’nin proton sayısı','Kütle numarasından nötron sayısı çıkarılır.','p(Y) = 40 − 25 = 15'),A('Y³⁻’nin elektronu','Anyon 3 elektron almıştır.','e = 15 + 3 = 18')],
 ne='X²⁺ ve Y³⁻',z='zor',alt='İzotop, İzoton, İzobar',kaz='İyon ve izobar bilgisinden bir iyonun elektron sayısını bulur.',kalip='düz',
 metin='Bir kimya öğretmeni tahtaya şu verileri yazmıştır: X²⁺ iyonunun elektron sayısı 18, X atomunun kütle numarası 40’tır. Nötr Y atomu X atomunun izobarıdır ve Y atomunun çekirdeğinde 25 nötron bulunur. Öğretmen, öğrencilerinden Y atomunun 3 elektron alarak oluşturduğu iyonun elektron sayısını bulmalarını istemiştir.\nBuna göre Y³⁻ iyonunun elektron sayısı kaçtır?',
 dogru=eY3,yan=[(12,'Y’nin proton sayısından 3 çıkarmış; anyonda elektron sayısı proton sayısının üstüne eklenir.','dikkat'),(15,'Y’nin nötr atomdaki elektron sayısını iyonunki sanmış; 3 elektron alındığını unutmuş.','dikkat'),(20,'X atomunun proton sayısını (20) Y³⁻ iyonunun elektron sayısı sanmış; izobarlarda atom numaraları farklıdır.','bilgi'),(25,'Y atomunun nötron sayısını elektron sayısı olarak almış.','bilgi')],
 istenen='Y³⁻ iyonundaki elektron sayısı.',
 ip=['Önce X’in proton sayısını bul.'],
 bilgi=[B('İzobar ve anyon','izobar atomların kütle numarası eşittir. Anyonda elektron = proton + yük. Örnek: 8 protonlu bir atomun 2− yüklü iyonunda 10 elektron vardır')],
 puf='İyondan proton sayısını bul, izobarlıkla kütle numarasını aktar, nötrondan çıkar.')
# ======================= 0015 · model şemaları · orta · olumsuz kök · şekil =======================
def thomson(cx):
    s=f'\\draw[fill=vurgu!10,thick] ({cx},0) circle (1.1);'
    for a,r in [(20,.6),(110,.7),(200,.55),(290,.7),(65,.2),(245,.25)]:
        s+=f'\\node at ({cx+r*math.cos(math.radians(a)):.2f},{r*math.sin(math.radians(a)):.2f}) {{\\scriptsize +}};'
    for a,r in [(50,.85),(165,.9),(255,.5),(330,.8),(130,.3),(10,.35)]:
        s+=f'\\fill ({cx+r*math.cos(math.radians(a)):.2f},{r*math.sin(math.radians(a)):.2f}) circle (.07);'
    return s+f'\\node[below] at ({cx},-1.2) {{\\textbf{{I}}}};'
def ruth(cx):
    s=f'\\draw[fill=vurgu!70] ({cx},0) circle (.2); \\node[font=\\scriptsize] at ({cx},0) {{+}};'
    for r in (.7,1.05): s+=f'\\draw[dashed,gray] ({cx},0) circle ({r});'
    for a,r in [(40,.7),(220,.7),(140,1.05),(320,1.05)]:
        s+=f'\\fill ({cx+r*math.cos(math.radians(a)):.2f},{r*math.sin(math.radians(a)):.2f}) circle (.07);'
    return s+f'\\node[below] at ({cx},-1.2) {{\\textbf{{II}}}};'
def bohrm(cx):
    s=f'\\draw[fill=vurgu!70] ({cx},0) circle (.2); \\node[font=\\scriptsize] at ({cx},0) {{+}};'
    for i,(r,n) in enumerate([(.5,2),(.9,3)]):
        s+=f'\\draw[thick] ({cx},0) circle ({r});'
        for k in range(n):
            a=60+360*k/n+25*i; s+=f'\\fill ({cx+r*math.cos(math.radians(a)):.2f},{r*math.sin(math.radians(a)):.2f}) circle (.07);'
    s+=f'\\node[font=\\scriptsize,fill=white,inner sep=.5pt] at ({cx+.5*math.cos(math.radians(150)):.2f},{.5*math.sin(math.radians(150)):.2f}) {{K}}; \\node[font=\\scriptsize,fill=white,inner sep=.5pt] at ({cx+.9*math.cos(math.radians(150)):.2f},{.9*math.sin(math.radians(150)):.2f}) {{L}};'
    return s+f'\\node[below] at ({cx},-1.2) {{\\textbf{{III}}}};'
SK=tk(thomson(0)+ruth(3.2)+bohrm(6.4)+'\\node[font=\\scriptsize] at (3.2,1.55) {$\\bullet$: elektron \\quad +: artı yüklü çekirdek};')
S=[('I numaralı model, elektronun keşfinden sonra öne sürülmüştür.',True,''),
   ('II numaralı modelde atomun artı yükü ve kütlesi küçük bir çekirdekte toplanmıştır.',True,''),
   ('III numaralı modelde elektronlar belirli enerjili katmanlarda bulunur.',True,''),
   ('I numaralı modelde atomun merkezinde artı yüklü bir çekirdek vardır.',False,'Artı yükün atom içine yayıldığı bu modelde çekirdek yoktur; çekirdek II numaralı modelle gelmiştir.'),
   ('II numaralı model, I numaralı modelin geri dönen parçacıkları açıklayamamasını giderir.',True,'')]
yanl=[s for s in S if not s[1]]; assert len(yanl)==1
d=yanl[0][0]
yan15=[(S[0][0],'Doğru ifadeyi yanlış sanmış; elektronu ilk bulan Thomson’dur ve elektronlu model onun modelidir.','bilgi'),
       (S[1][0],'Doğru ifadeyi yanlış sanmış; yoğun çekirdek fikri Rutherford modelindedir.','bilgi'),
       (S[2][0],'Doğru ifadeyi yanlış sanmış; belirli enerjili katmanlar Bohr modelinin temelidir.','bilgi'),
       (S[4][0],'Doğru ifadeyi yanlış saymış; çekirdek varsayımı alfa parçacıklarının geri dönüşünü açıklar.','bilgi')]
q('0015','14',[A('Şemaları tanı','I artı yük içinde elektronlar (Thomson), II yoğun çekirdek (Rutherford), III katmanlar (Bohr) modelidir.','I: Thomson · II: Rutherford · III: Bohr'),A('İfadeleri ele','Her ifade ilgili modelin özelliğiyle karşılaştırılır.','II, III ve I’in elektronla ilgili ifadeleri doğru'),A('Yanlışı bul','I numaralı modelde çekirdek bulunmaz.','I’de çekirdek var → yanlış')],
 ne='üç atom modeli şeması',z='orta',alt='Atom Modelleri',kaz='Atom modeli çizimlerini tanıyıp modellerin özelliklerini yorumlar.',kalip='şekilli',sekil=SK,
 metin='Şekilde, tarihsel gelişim içinde ortaya atılmış üç atom modelinin şematik çizimleri I, II ve III numaralarıyla verilmiştir. Bir öğretmen, öğrencilerinden her çizimin hangi modelin ana fikrini yansıttığını bulmalarını ve modelleri karşılaştırmalarını istemiştir.\nBuna göre aşağıdaki ifadelerden hangisi yanlıştır?',
 dogru=d,sira=[S[3][0],S[0][0],S[1][0],S[4][0],S[2][0]],yan=yan15,istenen='Yanlış ifade.',
 ip=['Her çizimde çekirdeğin olup olmadığına ve elektronların nasıl yerleştirildiğine bak.'],
 bilgi=[B('Model şemaları','her model önceki modelin açıklayamadığı gözlemi açıklamak için önerilmiştir; şemalarda çekirdeğin olup olmadığına ve elektronların nasıl yerleştirildiğine bak')],
 puf='Çekirdek II ile, katmanlar III ile başlar; I’de ikisi de yoktur.')
# ======================= 0016 · modellerin sırası · kolay =======================
kart16={'K':'Bohr','L':'Dalton','M':'Rutherford','N':'Thomson'}
sirama=['Dalton','Thomson','Rutherford','Bohr']
inv={v:k for k,v in kart16.items()}
dog=' – '.join(inv[m] for m in sirama); assert dog=='L – N – M – K'
S=[('L – N – M – K',True,''),
   ('L – M – N – K',False,'Rutherford’un çekirdek modelini Thomson’ın elektronlu modelinden önce koymuş.'),
   ('N – L – M – K',False,'Thomson’ın modelini Dalton’ın bölünemeyen atom modelinden önce yerleştirmiş.'),
   ('L – N – K – M',False,'Bohr’un katman modelini Rutherford’un çekirdek modelinden önce yazmış.'),
   ('M – L – N – K',False,'Çekirdek modelini en başa koymuş; çekirdeğin keşfi elektronun keşfinden sonradır.')]
d,y=tek(S,0)
q('0016','15',[A('Kartları tanı','Her kartın anlattığı modeli bul.','K: Bohr · L: Dalton · M: Rutherford · N: Thomson'),A('Sırayı kur','Modeller, önceki modelin açıklayamadığını gidererek gelişmiştir.','Dalton → Thomson → Rutherford → Bohr'),A('Harflere çevir','Her modelin kart harfini sırayla yaz.','L – N – M – K')],
 ne='dört kartın zaman sırası',z='kolay',alt='Atom Modelleri',kaz='Atom modellerini ortaya çıkış sırasına göre dizer.',kalip='düz',
 metin='Bir öğrenci, atom modellerini anlatan dört kartı eskiden yeniye doğru dizmek istiyor. Kartlarda şu bilgiler yazılıdır:\nK: Elektronlar çekirdek çevresinde belirli enerjili katmanlarda bulunur.\nL: Atom, içi dolu ve bölünemeyen bir küredir.\nM: Atomun artı yükü ve kütlesi çok küçük bir çekirdekte toplanmıştır.\nN: Atom, artı yüklü bir kütle içine gömülmüş elektronlardan oluşur.\nBuna göre kartlar eskiden yeniye hangi sırayla dizilmelidir?',
 dogru=d,sira=[S[1][0],S[2][0],S[3][0],S[4][0],S[0][0]],yan=y,istenen='Kartların eskiden yeniye sırası.',
 ip=['Elektronun, çekirdeğin ve enerji katmanlarının hangi sırayla keşfedildiğini düşün.'],
 bilgi=[B('Modellerin katkıları','Dalton: bölünemez küre; Thomson: elektronu buldu; Rutherford: çekirdeği buldu; Bohr: enerji katmanlarını önerdi')],
 puf='Bölünemez atom, elektron, çekirdek, katman: her yenilik bir öncekinin eksiğini kapatır.')
# ======================= 0017 · atom ve iyon karşılaştırma tablosu · orta · öncüllü =======================
pM,nM=12,12; at=kab(12); iy=kab(10); assert at==[2,8,2] and iy==[2,8]
AM=pM+nM
SK=tablo_svg(['Özellik','Nötr X atomu','X²⁺ iyonu'],[['Katmanlardaki elektron dağılımı','2, 8, 2','2, 8'],['Nötron sayısı',str(nM),str(nM)]])
onc('0017','16','Bir öğrenci, nötr X atomunun ve bu atomdan oluşan X²⁺ iyonunun bazı özelliklerini aşağıdaki tabloda karşılaştırmıştır. Atomun elektron sayısı, tablodaki katman dağılımından bulunabilmektedir. Öğrenci, atomdan iyona geçişte hangi niceliklerin değiştiğini tartışmak istemektedir.',
 [('X atomundan X²⁺ iyonu oluşurken proton sayısı değişmez.',True,'İyonlaşmada yalnız elektronlar alınır ya da verilir; çekirdek ve proton sayısı sabit kalır.','iyonlaşmanın çekirdeği de etkilediğini düşünmüş.'),
  ('X²⁺ iyonunun proton sayısı, elektron sayısından fazladır.',pM>sum(iy),'İyonda 12 proton ve 10 elektron vardır; artı yüklü iyonda proton fazladır.','katyonda elektronun daha fazla olduğunu sanmış.'),
  ('X atomunun kütle numarası, X²⁺ iyonununkinden büyüktür.',False,'Elektronlar kütle numarasına katılmaz; proton ve nötron sayıları değişmediğinden kütle numaraları eşittir.','verilen elektronların kütle numarasından çıkarıldığını sanmış.')],
 ['Yalnız I','I ve II','I ve III','II ve III','I, II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='X atomu ve X²⁺ tablosu',z='orta',alt='Nötr Atom ve İyon',kaz='Nötr atom ile iyonu proton, elektron, nötron ve kütle numarası bakımından karşılaştırır.',kalip='öncüllü',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['Atomdan iyona geçerken çekirdekteki taneciklerin sabit kalıp kalmadığını düşün.'],
 bilgi=[B('Atomdan iyona','iyon oluşurken elektron sayısı ve katman dağılımı değişir. Örnek: Li → Li⁺ geçişinde bir elektron azalır')],
 puf='İyonlaşmada yalnız elektron değişir; proton, nötron ve kütle numarası sabittir.')
# ======================= 0018 · izoelektronik iyonların atomları · zor · öncüllü =======================
ZX=18+2; ZY=18-1; kx=kab(ZX); ky=kab(ZY)
assert (ZX,ZY)==(20,17) and kx==[2,8,8,2] and ky==[2,8,7]
onc('0018','17','Bir kimya öğretmeni, X²⁺ ve Y⁻ iyonlarının her ikisinin de katmanlarındaki elektron dağılımının 2, 8, 8 olduğunu söylemiş ve öğrencilerden bu iyonların nötr atomlarını yorumlamalarını istemiştir. Öğrenciler, atom numaralarını bulup katman diyagramlarını çizmeye çalışmaktadır.',
 [('X atomunun atom numarası 18’dir.',ZX==18,'X²⁺ 18 elektron taşır; nötr atom 2 elektron daha içerir, atom numarası 18 + 2 = 20’dir.','iyondaki elektron sayısını atom numarası sanmış.'),
  ('Y atomunun son katmanında 8 elektron bulunur.',ky[-1]==8,'Y⁻ 18 elektronludur; nötr Y atomunda 17 elektron vardır ve dizilimi 2, 8, 7’dir.','Y atomunun dizilimini iyonununkiyle aynı sanmış.'),
  ('X atomunun katman sayısı, Y atomununkinden fazladır.',len(kx)>len(ky),'X atomu 2, 8, 8, 2 ile dört, Y atomu 2, 8, 7 ile üç katmanlıdır.','iyonların aynı katman sayısına sahip olmasından atomların da aynı katman sayısına sahip olduğunu sanmış.')],
 ['Yalnız I','Yalnız II','Yalnız III','I ve II','II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='X²⁺ ve Y⁻ izoelektronik',z='zor',alt='Nötr Atom ve İyon',kaz='İzoelektronik iyonlardan atom numaralarını ve nötr atomların katman dağılımlarını çıkarır.',kalip='öncüllü',
 istenen='Doğru olan ifadeler.',
 ip=['Her iyonun elektron sayısını yaz.'],
 bilgi=[B('İzoelektronik','elektron sayıları eşit olan taneciklerdir. Katyonun atom numarası elektronuna yük kadar eklenerek, anyonunki yük kadar çıkarılarak bulunur. Örnek: Mg²⁺ ve Ne izoelektroniktir (10 elektron)')],
 puf='İyondan nötr atoma dön: katyonda elektron ekle, anyonda çıkar; sonra dizilimi yaz.')
# ======================= 0019 · toplam tanecik · orta · hikâyeli =======================
pT=16; nT=pT+1; eT=pT+2; tot=pT+nT+eT; AT=pT+nT
assert (tot,AT)==(51,33) and pT+eT==34 and nT+eT==35 and nT==17
q('0019','18',[A('Tanecik sayılarını yaz','X²⁻ iyonunda nötron p + 1, elektron p + 2’dir.','n = p + 1 · e = p + 2'),A('Toplamı kur','Üç taneciğin toplamı 51’dir.','p + (p + 1) + (p + 2) = 51'),A('Protonu bul','Denklem çözülür.','3p + 3 = 51 · p = 16'),A('Kütle numarası','Proton ve nötron toplanır.','A = 16 + 17 = 33')],
 ne='X²⁻ iyonunun toplam tanecik sayısı',z='orta',alt='Atomun Temel Tanecikleri',kaz='İyondaki tanecik sayıları arasındaki ilişkiden denklem kurup kütle numarasını bulur.',kalip='hikâyeli',
 metin='Bir araştırmacı, kimyasal bir analizde X²⁻ iyonunu incelemiştir. İyonun içindeki proton, nötron ve elektronların sayıları toplamının 51 olduğunu bulmuştur. Ayrıca X atomunun nötron sayısının, proton sayısından 1 fazla olduğunu belirlemiştir.\nBuna göre X atomunun kütle numarası kaçtır?',
 dogru=AT,yan=[(17,'Nötron sayısını kütle numarası sanmış; protonları katmamış.','bilgi'),(34,'Kütle numarası yerine proton ve elektron sayılarını toplamış.','bilgi'),(35,'Nötron ve elektron sayılarını toplamış (17 + 18); protonu unutmuş.','bilgi'),(51,'Verilen toplam tanecik sayısını kütle numarası sanmış; elektronlar kütle numarasına katılmaz.','bilgi')],
 istenen='X atomunun kütle numarası.',
 ip=['Proton sayısına p deyip nötron ve elektron sayılarını p cinsinden yaz.'],
 bilgi=[B('İyondaki tanecikler','anyonda elektron sayısı proton sayısından yük kadar fazladır; nötron sayısı bağımsızdır. Örnek: 7 protonlu, 3− yüklü iyonda 10 elektron vardır')],
 puf='Bilinmeyeni proton sayısı seç; diğer iki tanecik onun cinsinden yazılır.')
# ======================= 0020 · anyon katman diyagramı · zor · şekil =======================
c20=kab(18); assert c20==[2,8,8]; e20=sum(c20); q20=2; Zp=e20-q20; A20=34; n20=A20-Zp
assert (Zp,n20)==(16,18) and A20-(e20+q20)==14 and A20-e20==16 and A20-(e20-2*q20)==20
SK=tk(bohr(0,0,c20,'Y','Y$^{2-}$ iyonu'))
q('0020','19',[A('Elektron sayısı','Diyagramdaki elektronlar sayılır.','2 + 8 + 8 = 18'),A('Yükü işle','2− yüklü iyon, atoma göre 2 elektron fazla taşır.','p = 18 − 2 = 16'),A('Nötron sayısı','Kütle numarasından proton sayısı çıkarılır.','n = 34 − 16'),A('Sonuç','Y atomunun nötron sayısı.','18')],
 ne='Y²⁻ iyonu diyagramı',z='zor',alt='Bohr Modeli ve Katman Dağılımı',kaz='Anyonun katman diyagramından atomun proton ve nötron sayısını bulur.',kalip='şekilli',sekil=SK,
 metin='Şekilde, katman diyagramı verilen Y²⁻ iyonu, Y atomunun 2 elektron almasıyla oluşmuştur. Y atomunun kütle numarası 34’tür; diyagramda yalnızca elektronlar gösterilmiştir.\nBuna göre Y atomunun nötron sayısı kaçtır?',
 dogru=n20,yan=[(14,'İyon yükünü ters yönde işleyip proton sayısını 20 bulmuş.','dikkat'),(16,'Elektron sayısını (18) proton sayısı alıp 34 − 18 işlemini yapmış.','bilgi'),(20,'İyon yükünü iki kez çıkararak proton sayısını 14 bulmuş.','dikkat'),(34,'Kütle numarasını nötron sayısı olarak almış.','bilgi')],
 istenen='Y atomunun nötron sayısı.',
 ip=['Şekildeki noktalar atomu mu iyonu mu gösteriyor?'],
 bilgi=[B('Anyonun protonu','anyonda proton sayısı = elektron sayısı − yük. Örnek: 10 elektronlu, 2− yüklü iyonun 8 protonu vardır')],
 puf='Diyagram iyonun elektronunu verir; protonu yükle düzelt, sonra kütle numarasından çıkar.')
# ======================= 0021 · uyarılmış atom diyagramı · zor · öncüllü =======================
def temel(c): return kab(sum(c))==c
dA=[2,8,2]; dB=[2,7,3]; assert sum(dA)==sum(dB)==12 and temel(dA) and not temel(dB)
aynı=sum(dA)==sum(dB); uyA=not temel(dA); isimaBA=(not temel(dB)) and temel(dA)
assert (aynı,uyA,isimaBA)==(True,False,True)
SK=tk(bohr(0,0,dA,'A','A')+bohr(4.6,0,dB,'B','B')+'\\path (6.9,0);')
onc('0021','20','Şekilde, iki nötr atomun katman diyagramları verilmiştir. Atomların ikisi de nötrdür, hiçbiri iyon değildir. Öğretmen, çizimleri karşılaştırarak atomların durumları hakkında yorum yapmalarını istemiştir.',
 [('A ve B aynı elementin atomlarıdır.',aynı,'İkisinde de toplam 12 elektron vardır; nötr atomlarda bu, proton sayısının 12 olduğunu gösterir.','dizilimler farklı diye atomları farklı element sanmış.'),
  ('A atomu uyarılmış hâldedir.',uyA,'A’nın dizilimi 2, 8, 2’dir; elektronlar en düşük enerjili katmanlardadır, yani temel hâldedir.','iki dizilimden birinin diğerinden farklı olmasını A’nın uyarılması sanmış.'),
  ('B atomunun A atomuna dönüşmesi sırasında ışıma yapılır.',isimaBA,'B’de bir elektron L katmanından M katmanına çıkmıştır; geri döndüğünde fazla enerji ışık olarak yayılır.','alt katmana dönüşte enerjinin soğurulduğunu sanmış.')],
 ['Yalnız I','Yalnız III','I ve II','I ve III','I, II ve III'],'Buna göre yukarıdaki ifadelerden hangileri doğrudur?',
 ne='A ve B katman diyagramları (12 elektron)',z='zor',alt='Uyarılmış Atom ve Işıma',kaz='Katman diyagramlarından temel ve uyarılmış hâli ayırt edip ışıma yönünü yorumlar.',kalip='öncüllü',sekil=SK,
 istenen='Doğru olan ifadeler.',
 ip=['İki atomun elektron toplamını ve dizilimlerini karşılaştır.'],
 bilgi=[B('Temel ve uyarılmış hâl','elektronların en düşük enerjili dizilimde bulunduğu hâl temel hâldir. Elektron üst katmana çıkarsa atom uyarılmıştır; elektron sayısı aynı kalır. Örnek: 2, 6 temel; 2, 5, 1 uyarılmış')],
 puf='Elektron toplamı aynı ve dizilimler farklıysa biri uyarılmıştır; ışıma uyarılmış hâlden temel hâle dönerken olur.')
# ======================= 0022 · tablo yorumu · zor · tablo =======================
tb22={'X':(39,20,18),'Y':(40,22,18),'Z':(40,20,18)}  # kütle no, nötron, elektron
p22={k:v[0]-v[1] for k,v in tb22.items()}
assert p22=={'X':19,'Y':18,'Z':20}
izoton22=lambda a,b:tb22[a][1]==tb22[b][1] and p22[a]!=p22[b]
izobar22=lambda a,b:tb22[a][0]==tb22[b][0] and p22[a]!=p22[b]
izotop22=lambda a,b:p22[a]==p22[b] and tb22[a][0]!=tb22[b][0]
yuk=lambda a:p22[a]-tb22[a][2]
assert (izobar22('X','Y'),izoton22('X','Z'),izotop22('Y','Z'),yuk('Y'),yuk('Z'),yuk('X'))==(False,True,False,0,2,1)
SK=tablo_svg(['Tanecik','Kütle numarası','Nötron sayısı','Elektron sayısı'],[[k,*map(str,v)] for k,v in tb22.items()])
S=[('X ile Y izobardır.',False,'İzobarda kütle numaraları eşit olmalıdır; X’in 39, Y’nin 40’tır.'),
   ('X ile Z izotondur.',True,''),
   ('Y ile Z izotoptur.',False,'Y’nin atom numarası 18, Z’ninki 20’dir; izotop atomlarda atom numarası eşit olmalıdır.'),
   ('Y, 2− yüklü bir anyondur.',False,'Y’de 18 proton ve 18 elektron vardır; nötr atomdur.'),
   ('Z, 1+ yüklü bir katyondur.',False,'Z’de 20 proton, 18 elektron vardır; yükü 2+’dır.')]
d,y=tek(S,1)
q('0022','21',[A('Proton sayıları','Kütle numarasından nötron sayısı çıkarılır.','X: 39 − 20 = 19 · Y: 40 − 22 = 18 · Z: 40 − 20 = 20'),A('Yükleri bul','Protonu elektronla karşılaştır.','X: +1 · Y: 0 · Z: +2'),A('İzo-kavramları sına','Kütle numarası, nötron ve atom numarasını karşılaştır.','X–Z: nötron 20 = 20'),A('Sonuç','Yalnız X ile Z’nin izoton olduğunu söyleyen ifade doğrudur.','X ve Z: izoton')],
 ne='X, Y, Z tablosu',z='orta',alt='İzotop, İzoton, İzobar',kaz='Kütle, nötron ve elektron sayılarından proton ve yükü bulup izo-kavramları değerlendirir.',kalip='tablo',sekil=SK,
 metin='Bir araştırma ekibi, X, Y ve Z taneciklerinin kütle numarasını, nötron sayısını ve elektron sayısını ölçmüş ve sonuçları aşağıdaki tabloda toplamıştır. Taneciklerin proton sayıları ölçülmemiş, ancak tablodaki verilerden bulunabilmektedir.\nBuna göre bu taneciklerle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=d,sira=[S[0][0],S[1][0],S[2][0],S[3][0],S[4][0]],yan=y,istenen='Doğru ifade.',
 ip=['Tabloda verilmeyen sayıyı kütle numarası ve nötrondan türet.'],
 bilgi=[B('Tablodan proton','proton sayısı = kütle numarası − nötron sayısı. Yük = proton − elektron. Örnek: kütle numarası 23, nötron 12, elektron 10 olan taneciğin protonu 11, yükü 1+’dır')],
 puf='Önce proton sayısını bul; yük ve izo-kavramlar o sayıdan çıkar.')
bitir(P,'atomiki',UK)
