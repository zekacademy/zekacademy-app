import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..'))
from ortak import *
import gorsel as G
from fractions import Fraction as Fr
def fm(x):
    x=Fr(x).limit_denominator(10**6); n=x<0; x=abs(x)
    if x.denominator==1: s=str(x.numerator)
    else:
        d=x.denominator
        while d%2==0: d//=2
        while d%5==0: d//=5
        assert d==1,'ondalik degil'
        s=f'{float(x):.6f}'.rstrip('0').rstrip('.').replace('.',',')
    return ('−' if n else '')+s
ORT={}; KARTLAR=[]
def kart(id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip,kaynak):
    KARTLAR.append(dict(id=id,konu=KONU,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=kaynak))
def mk(P,no,kard=False,metin=None,dogru=None,yan=None,istenen=None,ad=None,sekil=None,sira=None,ip=None,bilgi=None,puf=None,kisa=None,
       tipId=None,tip=None,z=None,alt=None,kaz=None,kalip=None,adim=None,kart=None):
    vals=[dogru]+[y[0] for y in yan]; assert len(vals)==5
    if all(not isinstance(v,str) for v in vals):
        fv=[Fr(v).limit_denominator(10**6) for v in vals]; assert len(set(fv))==5
        order=sorted(range(5),key=lambda i:fv[i]); siklar=[fm(vals[i]) for i in order]
        pos={i:'ABCDE'[j] for j,i in enumerate(order)}
    else:
        assert sira and sorted(sira)==sorted(vals), (sira,vals)
        siklar=list(sira); pos={i:'ABCDE'[sira.index(vals[i])] for i in range(5)}
    sik=pos[0]
    cel={pos[i+1]:y[1] for i,y in enumerate(yan)}; tur={pos[i+1]:y[2] for i,y in enumerate(yan)}
    if not kard:
        ORT[no]=(ip,bilgi,puf,kisa)
        P.R(no,tipId,tip,z,alt,kaz,kalip,adim,kart,metin,siklar,sik,istenen,ip,bilgi,ad,puf,cel,tur,kisa=kisa,sekil=sekil)
    else:
        o=ORT[no]
        P.K(no,metin,siklar,sik,istenen,ip or o[0],bilgi or o[1],ad,puf or o[2],cel,tur,kisa=kisa if kisa is not None else o[3],sekil=sekil)
def bitir(P,onek,k):
    HV=os.path.join(HD,'..')
    P.yaz(os.path.join(HD,f'{onek}-1.json'),os.path.join(HD,f'{onek}-1-kardes.json'))
    tipler={}
    for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=k))['kartlar'].append(c['id'])
    json.dump(dict(konu=P.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM 2018–2026 TYT Fizik çıkmış soruları, MEB 9–10. sınıf müfredatı.',kartlar=KARTLAR,tipler=list(tipler.values())),
              open(os.path.join(HV,'kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    print('tipler',len(tipler))
def T(x,y,s,**k): return G._t(x,y,s,**k)
import math
def dalga_grafik(xmax,lam,etiketler,eksen_ad,yad='y'):
    """y = sin(2πx/lam), 0..xmax. etiketler: [(konum, yazı)]"""
    W,H,y0,A_=330,140,72,38; x0,x1=44,312; o=[]
    sx=lambda x:x0+(x1-x0)*x/xmax
    o.append(f'<line x1="{x0}" y1="{y0}" x2="{x1+10}" y2="{y0}" stroke-width="1.4"/><line x1="{x0}" y1="{y0+52}" x2="{x0}" y2="{y0-52}" stroke-width="1.4"/>')
    o.append(T(x0-8,y0-46,yad,anchor='end',size=12,bold=True)); o.append(T(x1+14,y0-10,eksen_ad,anchor='end',size=12,bold=True))
    pts=' '.join(f'{sx(xmax*i/240):.1f},{y0-A_*math.sin(2*math.pi*xmax*i/240/lam):.1f}' for i in range(241))
    o.append(f'<polyline points="{pts}" stroke-width="2.4" style="stroke:{G.ACC}"/>')
    for p,l in etiketler:
        o.append(f'<line x1="{sx(p):.1f}" y1="{y0-4}" x2="{sx(p):.1f}" y2="{y0+4}" stroke-width="1.4"/>'); o.append(T(sx(p),y0+18,l,size=11))
    return G._svg(W,H,''.join(o))
KONU='Dalgalar'
P=Parti('dalgalar','Dalgalar','fiz|Dalgalar',ders='TYT Fizik',idon='tytfiz')
KY='ÖSYM 2018–2025 (dalgalar) · MEB 10. sınıf'
kart('K-FZDA-01','Dalga türleri','Mekanik dalga ortam ister; elektromanyetik dalga (ışık, radyo) boşlukta da yayılır. Enine/boyuna ayrımı.','Işığı mekanik sanmak; ses–ışık ayrımını karıştırmak.','kolay','öncüllü',2,'fz-dg-sinif','Dalgaların sınıflandırılması',KY)
kart('K-FZDA-02','Grafikten hız','Grafikten dalga boyu ya da periyot okunur; v = λ × f = λ ÷ T.','Yarım dalga boyunu λ saymak; toplam uzunluğu λ sanmak.','orta','grafik',3,'fz-dg-grafik','Dalga grafiği ve hız',KY)
kart('K-FZDA-03','Yay dalgası','Yayda hız ortama (gerginlik), frekans kaynağa bağlıdır; λ = v ÷ f.','Frekansın da ortamla değiştiğini sanmak.','orta','öncüllü',3,'fz-dg-yay','Yay dalgasının özellikleri',KY)
kart('K-FZDA-04','Su dalgası geçişi','Derin–sığ geçişte frekans sabit kalır; v ve λ doğru orantılı değişir.','Dalga boyunun değişmediğini sanmak; oranı ters kurmak.','orta','hikâyeli',3,'fz-dg-su','Su dalgasının ortam değiştirmesi',KY)
kart('K-FZDA-05','Dalga boyu ve uzaklık','Frekans ve hızdan λ bulunur; tepe–çukur uzaklıkları λ/2’nin katlarıdır.','Tepe–çukur arasını λ almak; sayma hatası.','zor','hikâyeli',5,'fz-dg-hiz','Dalga denklemi ve uzaklıklar',KY)
kart('K-FZDA-06','Atmaların karşılaşması','Ters atmalar karşılaşınca üst üste binip yayı düzleştirir; göreli hızla süre hesabı.','Süreyi tek atmanın yoluna göre hesaplamak.','zor','hikâyeli',4,'fz-dg-atma','Yayda atmaların süperpozisyonu',KY)
DAL=B('Dalga büyüklükleri','T = 1 ÷ f ve v = λ × f. İki ardışık tepe arası bir dalga boyu (λ), tepe ile komşu çukur arası λ ÷ 2’dir. Örnek: f = 2 Hz, λ = 3 m → v = 6 m/s')
# ---- 0001
S1=['Yalnız I','Yalnız II','I ve III','II ve III','I, II ve III']
mk(P,'0001',tipId='fz-dg-sinif',tip='Dalgaların sınıflandırılması',z='kolay',alt='Dalgalar',kaz='Mekanik ve elektromanyetik dalgaları, yayılma ortamına göre ayırt eder.',kalip='öncüllü',adim=2,
 kart='K-FZDA-01 (dalga türleri) · yeni dalgalar, istenen ortam gerektirenler',
 metin='I. Ses dalgası\nII. Işık dalgası\nIII. Su yüzeyindeki dalga\nBu dalgalardan hangilerinin yayılabilmesi için maddesel bir ortama gerek vardır?',
 dogru='I ve III',sira=S1,yan=[('Yalnız I','Su dalgasının da mekanik olduğunu (III) atlamış.','dikkat'),('Yalnız II','Işığın ortam gerektirdiğini sanmış; ışık boşlukta da yayılır.','bilgi'),('II ve III','Işığın ortam gerektirdiğini sanıp sesi (I) atlamış.','bilgi'),('I, II ve III','Işığın da ortam gerektirdiğini sanmış; ışık elektromanyetik dalgadır.','bilgi')],
 istenen='Yayılması için ortam gereken dalgalar.',
 ip=['Güneş ışığı uzayın boşluğundan Dünya’ya gelir.','Ortam gerektirenler mekanik dalgalardır.','Ses ve su dalgası hangi tür?'],
 bilgi=[B('Mekanik ve elektromanyetik dalga','mekanik dalgalar (ses, su, yay) yayılmak için maddesel ortam ister; elektromanyetik dalgalar (ışık, radyo, X ışınları) boşlukta da yayılır')],
 ad=[A('Mekanik dalgaları ayır','Ses havadaki, su dalgası suyun yüzeyindeki titreşimle yayılır; ortam ister.','I ve III mekanik'),A('Işığa bak','Işık elektromanyetik dalgadır; boşlukta da yayılır.','II ortam istemez'),A('Sonuç','Ortam isteyenler ses ve su dalgasıdır.','I ve III')],
 puf='Ses, su ve yay dalgaları mekaniktir (ortam ister); ışık ve radyo dalgaları elektromanyetiktir (ortamsız yayılır).')
S1k=['Yalnız I','Yalnız III','I ve II','I ve III','II ve III']
mk(P,'0001',True,metin='I. Havada yayılan ses dalgası\nII. Su yüzeyindeki dalga\nIII. Işık dalgası\nBu dalgalardan hangileri boyuna dalgadır?',
 dogru='Yalnız I',sira=S1k,yan=[('Yalnız III','Işığı boyuna sanmış; ışık enine dalgadır.','bilgi'),('I ve II','Su yüzeyindeki dalgayı boyuna sanmış; su dalgası enine dalgadır.','bilgi'),('I ve III','Işığı boyuna sanmış; ışık enine dalgadır.','bilgi'),('II ve III','Ses dalgasını enine sanmış; ses boyuna dalgadır.','bilgi')],
 istenen='Boyuna dalga olanlar.',
 ip=['Boyuna dalgada titreşim yönü yayılma yönüyle aynıdır.','Ses havada sıkışma ve genleşme olarak ilerler.','Su ve ışık dalgalarında titreşim yayılmaya dik mi?'],
 bilgi=[B('Enine ve boyuna dalga','enine dalgada titreşim yönü yayılma yönüne diktir (su, ışık, yay dalgası); boyuna dalgada titreşim yönü yayılma yönüyle aynıdır (ses)')],
 ad=[A('Titreşim yönüne bak','Boyuna dalgada madde, dalganın ilerleme doğrultusunda titreşir.','boyuna: titreşim ∥ yayılma'),A('Dalgaları sınıfla','Ses sıkışma–genleşmedir, boyunadır. Su yüzeyi ve ışık enine dalgadır.','I: boyuna · II, III: enine'),A('Sonuç','Yalnız ses dalgası boyunadır.','Yalnız I')])
# ---- 0002 grafik y–x
assert 4*5==20 and 2*5==10 and 8*5==40 and Fr(4,5)==Fr(8,10) and 4+5==9
mk(P,'0002',tipId='fz-dg-grafik',tip='Dalga grafiği ve hız',z='orta',alt='Dalgalar',kaz='Konum–yer değiştirme grafiğinden dalga boyunu okuyup hızı hesaplar.',kalip='grafik',adim=3,
 kart='K-FZDA-02 (grafikten dalga boyu ve hız) · yeni grafik ve frekans',
 metin='Şekilde, bir yay üzerinde ilerleyen dalganın belirli bir andaki konum–yer değiştirme (y–x) grafiği verilmiştir. Dalganın frekansı 5 Hz’dir.\nBuna göre dalganın yayılma hızı kaç m/s’dir?',
 sekil=dalga_grafik(8,4,[(0,'0'),(2,'2'),(4,'4'),(6,'6'),(8,'8')],'x (m)'),
 dogru=20,yan=[(Fr(8,10),'Hızı λ ÷ f olarak hesaplamış (4 ÷ 5).','islem'),(9,'Dalga boyu ile frekansı toplamış (4 + 5).','bilgi'),(10,'Yarım dalga boyunu (2 m) dalga boyu sanmış.','dikkat'),(40,'Grafiğin tüm uzunluğunu (8 m) dalga boyu sanmış; grafikte iki dalga var.','dikkat')],
 istenen='Dalganın yayılma hızı (m/s).',
 ip=['Bir dalga boyu, aynı fazdaki iki ardışık nokta arasındaki uzaklıktır.','Grafikte sıfırdan başlayıp aynı yönde tekrar sıfırdan geçene kadar bir dalga boyu.','Hız = dalga boyu × frekans.'],
 bilgi=[DAL],
 ad=[A('Dalga boyunu oku','Dalga x = 0’dan başlar, x = 4 m’de aynı noktaya (aynı yönde sıfır) döner; bir tam dalga 4 m’dir.','λ = 4 m (grafikte 2 dalga, 8 m)'),A('Hız bağıntısı','Dalga hızı dalga boyu ile frekansın çarpımıdır.','v = λ × f'),A('Sonuç','Değerler yerine konur.','v = 4 × 5 = 20 m/s')],
 puf='Grafikte bir tam dalgayı bul (aynı fazda iki nokta arası); hız = dalga boyu × frekans.')
assert Fr(2)/Fr(2,5)==5 and 2*Fr(2,5)==Fr(4,5) and Fr(2)/Fr(1,5)==10 and 1/Fr(2,5)==Fr(5,2)
mk(P,'0002',True,metin='Şekilde, bir su dalgasının üzerindeki bir tıpanın zamanla yer değiştirmesini gösteren y–t grafiği verilmiştir. Dalgaların dalga boyu 2 m’dir.\nBuna göre dalganın yayılma hızı kaç m/s’dir?',
 sekil=dalga_grafik(1.2,0.4,[(0,'0'),(0.2,'0,2'),(0.4,'0,4'),(0.6,'0,6'),(0.8,'0,8'),(1.0,'1,0'),(1.2,'1,2')],'t (s)'),
 dogru=5,yan=[(Fr(8,10),'Hızı λ × T olarak hesaplamış (2 × 0,4).','islem'),(2,'Dalga boyunu (2 m) hız sanmış.','dikkat'),(Fr(5,2),'Frekansı (2,5 Hz) hız sanmış.','dikkat'),(10,'Yarım periyodu (0,2 s) periyot sanmış.','dikkat')],
 istenen='Dalganın yayılma hızı (m/s).',
 ip=['y–t grafiğinde bir periyot, aynı noktaya aynı yönde dönüş süresidir.','Grafikte 3 tam titreşim kaç saniyede oluyor?','Hız = dalga boyu ÷ periyot.'],
 ad=[A('Periyodu oku','Grafikte 3 tam titreşim 1,2 s’de tamamlanıyor.','T = 1,2 ÷ 3 = 0,4 s'),A('Hız bağıntısı','Hız, dalga boyunun periyoda oranıdır.','v = λ ÷ T'),A('Sonuç','Değerler yerine konur.','v = 2 ÷ 0,4 = 5 m/s')])
# ---- 0003 yay
S3=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
mk(P,'0003',tipId='fz-dg-yay',tip='Yay dalgasının özellikleri',z='orta',alt='Yay Dalgası',kaz='Yay dalgasında gerginliğin hız, dalga boyu ve frekans üzerindeki etkisini belirler.',kalip='öncüllü',adim=3,
 kart='K-FZDA-03 (yay dalgası, gerginlik) · yeni durum, öncüllü',
 metin='Bir ucundan sabit frekansla titreştirilen gergin bir yayda ilerleyen dalgalar oluşturuluyor. Kaynağın frekansı değiştirilmeden yay daha gergin hâle getiriliyor.\nBuna göre;\nI. Dalgaların yayılma hızı artar.\nII. Dalga boyu artar.\nIII. Dalgaların frekansı değişmez.\nifadelerinden hangileri doğrudur?',
 dogru='I, II ve III',sira=S3,yan=[('Yalnız I','Hız artınca frekans sabit kaldığından dalga boyunun da arttığını (II) ve frekansın değişmediğini (III) atlamış.','dikkat'),('Yalnız II','Gerginliğin hızı artırdığını (I) ve frekansın sabit kaldığını (III) atlamış.','dikkat'),('I ve II','Frekansın sabit kaldığını (III) atlamış; frekansı kaynak belirler.','bilgi'),('I ve III','Hız artınca dalga boyunun da arttığını (II) atlamış.','dikkat')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Yayda dalga hızı yayın gerginliğine bağlıdır.','Frekansı kaynak belirler; yay gerginleşince frekans değişir mi?','v = λ × f bağıntısında f sabit, v artıyorsa λ ne olur?'],
 bilgi=[DAL,B('Frekans ve hız','dalganın frekansını kaynak belirler, ortam değişse de frekans değişmez; yayılma hızını ortam (yayda gerginlik) belirler')],
 ad=[A('Hız','Yay gerginleştikçe dalga hızı artar.','v artar → I doğru'),A('Frekans','Frekansı kaynak belirler; kaynak değişmediğinden sabittir.','f sabit → III doğru'),A('Dalga boyu','v = λ × f bağıntısında f sabit, v arttığından λ artar.','λ = v ÷ f artar → II doğru'),A('Sonuç','Üç ifade de doğrudur.','I, II ve III')],
 puf='Ortam değişince (ya da gerginlik değişince) hız ve dalga boyu değişir; frekans kaynağa bağlı olduğu için sabit kalır.')
S3k=['Yalnız I','Yalnız II','I ve II','II ve III','I, II ve III']
mk(P,'0003',True,metin='Gerginliği değiştirilmeyen bir yayda, kaynağın frekansı artırılarak dalgalar oluşturuluyor.\nBuna göre;\nI. Dalgaların yayılma hızı artar.\nII. Dalga boyu azalır.\nIII. Dalgaların periyodu azalır.\nifadelerinden hangileri doğrudur?',
 dogru='II ve III',sira=S3k,yan=[('Yalnız I','Hızın arttığını sanmış; gerginlik sabitse hız değişmez.','bilgi'),('Yalnız II','Periyodun azaldığını (III) atlamış; T = 1 ÷ f.','dikkat'),('I ve II','Hızın arttığını sanmış; hız yalnız yayın gerginliğine bağlıdır.','bilgi'),('I, II ve III','Hızın arttığını sanmış; gerginlik değişmediğinden hız sabittir.','bilgi')],
 istenen='Doğru olan ifadelerin hangileri olduğu.',
 ip=['Yayın gerginliği aynı kaldığına göre dalga hızı için ne söylenebilir?','Frekans artarsa periyot nasıl değişir?','v = λ × f bağıntısında v sabit, f artıyorsa λ ne olur?'],
 ad=[A('Hız','Gerginlik değişmediğinden hız sabittir.','v sabit → I yanlış'),A('Periyot','T = 1 ÷ f; frekans artınca periyot azalır.','T azalır → III doğru'),A('Dalga boyu','v = λ × f bağıntısında v sabit, f arttığından λ azalır.','λ = v ÷ f azalır → II doğru')])
# ---- 0004 su derin->siğ
f_=Fr(12)/6; l2=Fr(8)/f_; assert f_==2 and l2==4 and Fr(6*12,8)==9
mk(P,'0004',tipId='fz-dg-su',tip='Su dalgasının ortam değiştirmesi',z='orta',alt='Su Dalgası',kaz='Su dalgası derinden sığa geçerken frekansın sabit kalmasından yeni dalga boyunu bulur.',kalip='hikâyeli',adim=3,
 kart='K-FZDA-04 (derin–sığ geçişi) · yeni hızlar, istenen sığdaki dalga boyu',
 metin='Bir dalga leğeninde derin bölgede yayılan su dalgalarının hızı 12 cm/s ve dalga boyu 6 cm’dir. Dalgalar sığ bölgeye geçtiğinde hızları 8 cm/s oluyor.\nBuna göre dalgaların sığ bölgedeki dalga boyu kaç cm’dir?',
 dogru=4,yan=[(2,'Frekansı (2 Hz) dalga boyu sanmış.','dikkat'),(6,'Dalga boyunun ortam değişince değişmediğini sanmış.','bilgi'),(9,'Oranı ters kurmuş: 6 × 12 ÷ 8.','islem'),(12,'İlk ortamdaki hızı dalga boyu sanmış.','dikkat')],
 istenen='Sığ bölgedeki dalga boyu (cm).',
 ip=['Dalgalar ortam değiştirirken kaynağın frekansı değişmez.','Önce derin bölgedeki frekansı v = λ × f ile bul.','Sığ bölgede aynı frekansla λ = v ÷ f.'],
 bilgi=[DAL,B('Ortam değişimi','dalga bir ortamdan diğerine geçerken frekans değişmez; hız ve dalga boyu birlikte (doğru orantılı) değişir: v₁ ÷ λ₁ = v₂ ÷ λ₂')],
 ad=[A('Frekansı bul','Derin bölgede v = λ × f yazılır.','f = 12 ÷ 6 = 2 Hz'),A('Frekans sabit','Sığ bölgede de frekans 2 Hz’dir.','f = 2 Hz'),A('Dalga boyu','Sığ bölgede λ = v ÷ f.','λ = 8 ÷ 2 = 4 cm')],
 puf='Ortam değişince frekans sabit kalır; v ÷ λ oranı her iki ortamda da aynıdır.')
assert Fr(10)/5==2 and Fr(15)/2==Fr(15,2)
mk(P,'0004',True,metin='Bir dalga leğeninde sığ bölgede yayılan su dalgalarının hızı 10 cm/s ve dalga boyu 2 cm’dir. Dalgalar derin bölgeye geçtiğinde hızları 15 cm/s oluyor.\nBuna göre dalgaların derin bölgedeki dalga boyu kaç cm’dir?',
 dogru=3,yan=[(2,'Dalga boyunun ortam değişince değişmediğini sanmış.','bilgi'),(5,'Frekansı (5 Hz) dalga boyu sanmış.','dikkat'),(Fr(15,2),'Yeni hızı ilk ortamdaki dalga boyuna bölmüş (15 ÷ 2).','islem'),(30,'Yeni hızı ilk dalga boyuyla çarpmış (15 × 2).','islem')],
 istenen='Derin bölgedeki dalga boyu (cm).',
 ad=[A('Frekansı bul','Sığ bölgede v = λ × f yazılır.','f = 10 ÷ 2 = 5 Hz'),A('Frekans sabit','Derin bölgede de frekans 5 Hz’dir.','f = 5 Hz'),A('Dalga boyu','Derin bölgede λ = v ÷ f.','λ = 15 ÷ 5 = 3 cm')])
# ---- 0005 zor hız ve uzaklık
f_=Fr(20,5); lam=Fr(40)/f_; assert f_==4 and lam==10 and Fr(5,2)*lam==25 and 3*lam==30 and Fr(3,2)*lam==15 and 2*lam==20
mk(P,'0005',tipId='fz-dg-hiz',tip='Dalga denklemi ve uzaklıklar',z='zor',alt='Dalgalar',kaz='Frekans ve hızdan dalga boyunu bulup tepe ve çukurlar arasındaki uzaklığı hesaplar.',kalip='hikâyeli',adim=5,
 kart='K-FZDA-05 (dalga boyu ve tepe–çukur uzaklığı) · yeni sayılar, 3. çukur',
 metin='Bir dalga kaynağı 5 saniyede 20 tam titreşim yapıyor ve oluşturduğu dalgalar 40 m/s hızla yayılıyor.\nBuna göre bir dalga tepesi ile bu tepeden sonra gelen 3. çukur arasındaki uzaklık kaç m’dir?',
 dogru=25,yan=[(15,'Tepe ile 2. çukur arasını (1,5λ) hesaplamış.','dikkat'),(20,'Tepe ile 3. çukur arasını 2λ almış.','dikkat'),(5,'Tepe ile ilk çukur arasını (λ ÷ 2) hesaplamış.','dikkat'),(10,'Tepe ile ilk çukur arasını λ almış; tepe–çukur arasının λ ÷ 2 olduğunu atlamış.','bilgi')],
 istenen='Tepe ile 3. çukur arasındaki uzaklık (m).',
 ip=['Önce kaynağın frekansını bul: titreşim sayısı ÷ süre.','Dalga boyunu v = λ × f ile hesapla.','Tepe ile ilk çukur λ ÷ 2 uzaktadır; sonraki her çukur λ daha uzakta.'],
 bilgi=[DAL],
 ad=[A('Frekans','Frekans, birim zamandaki titreşim sayısıdır.','f = 20 ÷ 5 = 4 Hz'),A('Dalga boyu','v = λ × f bağıntısından λ bulunur.','λ = 40 ÷ 4 = 10 m'),A('Çukurların konumu','Tepeden ilk çukur λ ÷ 2, ikinci λ ÷ 2 + λ, üçüncü λ ÷ 2 + 2λ uzaktadır.','5 m · 15 m · 25 m'),A('Sonuç','3. çukur için uzaklık 2,5λ’dır.','2,5 × 10 = 25 m')],
 puf='Tepe ile n. çukur arası (n − 1/2) × λ’dır; önce frekanstan ve hızdan λ’yı bul.')
f_=Fr(16,8); lam=Fr(12)/f_; assert f_==2 and lam==6 and Fr(7,2)*lam==21 and 3*lam==18 and 4*lam==24 and Fr(5,2)*lam==15 and Fr(9,2)*lam==27
mk(P,'0005',True,metin='Bir dalga kaynağı 8 saniyede 16 tam titreşim yapıyor ve oluşturduğu dalgalar 12 m/s hızla yayılıyor.\nBuna göre bir dalga çukuru ile bu çukurdan sonra gelen 4. tepe arasındaki uzaklık kaç m’dir?',
 dogru=21,yan=[(15,'Çukur ile 3. tepe arasını (2,5λ) hesaplamış.','dikkat'),(18,'Çukur ile 4. tepe arasını 3λ almış.','dikkat'),(24,'Çukur ile 4. tepe arasını 4λ almış; çukur–tepe arasının λ ÷ 2 olduğunu atlamış.','bilgi'),(27,'Çukur ile 5. tepe arasını (4,5λ) hesaplamış.','dikkat')],
 istenen='Çukur ile 4. tepe arasındaki uzaklık (m).',
 ad=[A('Frekans','Frekans, birim zamandaki titreşim sayısıdır.','f = 16 ÷ 8 = 2 Hz'),A('Dalga boyu','v = λ × f bağıntısından λ bulunur.','λ = 12 ÷ 2 = 6 m'),A('Tepelerin konumu','Çukurdan ilk tepe λ ÷ 2, sonraki her tepe λ daha uzaktadır.','3 m · 9 m · 15 m · 21 m'),A('Sonuç','4. tepe için uzaklık 3,5λ’dır.','3,5 × 6 = 21 m')])
# ---- 0006 atma
t=Fr(24)/(2*4); assert t==3 and Fr(24,4)==6 and Fr(24,16)==Fr(3,2)
mk(P,'0006',tipId='fz-dg-atma',tip='Yayda atmaların süperpozisyonu',z='zor',alt='Yay Dalgası',kaz='Karşılaşan ters atmaların yayı düzleştirdiği anı göreli hızla hesaplar.',kalip='hikâyeli',adim=4,
 kart='K-FZDA-06 (atmaların karşılaşması) · yeni uzunluk ve hız',
 metin='Uzunluğu 24 m olan gergin bir yayın iki ucundan, genlikleri eşit olan biri tepe, diğeri çukur biçiminde iki atma aynı anda birbirine doğru gönderiliyor. Atmaların yayılma hızı 4 m/s’dir ve atmalar yayın orta noktasında karşılaşıyor.\nBuna göre gönderildikten kaç saniye sonra yay tamamen doğrusal görünür?',
 dogru=3,yan=[(24,'Yayın uzunluğunu (24 m) süre sanmış.','dikkat'),(4,'Atmanın hızını (4 m/s) süre sanmış.','dikkat'),(6,'Tek atmanın tüm yayı gitme süresini (24 ÷ 4) hesaplamış.','dikkat'),(12,'Karşılaşma noktasının uzaklığını (12 m) süre sanmış.','dikkat')],
 istenen='Yayın tamamen doğrusal göründüğü an (s).',
 ip=['Yay, karşılaşma anında iki atmanın toplamıdır.','Genlikleri eşit ters atmalar üst üste binince toplam yer değiştirme ne olur?','Atmalar birbirine yaklaşırken her biri orta noktaya kaç m gider?'],
 bilgi=[B('Atmaların üst üste binmesi','karşılaşan atmaların yer değiştirmeleri toplanır. Genlikleri eşit tepe ve çukur üst üste gelince yay anlık olarak düz görünür; sonra atmalar yollarına devam eder')],
 ad=[A('Karşılaşma noktası','Atmalar aynı hızla, zıt yönden gelir; yayın orta noktasında buluşurlar.','24 ÷ 2 = 12 m'),A('Düz görünüm','Eşit genlikli tepe ve çukur üst üste binince toplam yer değiştirme sıfırdır.','tepe + çukur = 0'),A('Süre','Her atma 12 m yol alır.','t = 12 ÷ 4'),A('Sonuç','Yay bu anda doğrusaldır.','t = 3 s')],
 puf='Zıt yönden gelen eşit hızlı atmalar orta noktada buluşur; süre = (uzunluk ÷ 2) ÷ hız.')
t=Fr(30)/(2*3); assert t==5
mk(P,'0006',True,metin='Uzunluğu 30 m olan gergin bir yayın iki ucundan, genlikleri eşit olan biri tepe, diğeri çukur biçiminde iki atma aynı anda birbirine doğru gönderiliyor. Atmaların yayılma hızı 3 m/s’dir ve atmalar yayın orta noktasında karşılaşıyor.\nBuna göre gönderildikten kaç saniye sonra yay tamamen doğrusal görünür?',
 dogru=5,yan=[(Fr(5,2),'Toplam uzunluğu iki atmanın hızları toplamının iki katına bölmüş (30 ÷ 12).','islem'),(3,'Atmanın hızını (3 m/s) süre sanmış.','dikkat'),(10,'Tek atmanın tüm yayı gitme süresini (30 ÷ 3) hesaplamış.','dikkat'),(15,'Karşılaşma noktasının uzaklığını (15 m) süre sanmış.','dikkat')],
 istenen='Yayın tamamen doğrusal göründüğü an (s).',
 ad=[A('Karşılaşma noktası','Atmalar aynı hızla zıt yönden gelir; yayın orta noktasında buluşurlar.','30 ÷ 2 = 15 m'),A('Düz görünüm','Eşit genlikli tepe ve çukur üst üste binince toplam yer değiştirme sıfırdır.','tepe + çukur = 0'),A('Süre','Her atma 15 m yol alır.','t = 15 ÷ 3'),A('Sonuç','Yay bu anda doğrusaldır.','t = 5 s')])
bitir(P,'dalgalar','fiz|Dalgalar')
