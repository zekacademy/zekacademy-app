import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_cog_b import *
Q=Konu('bolgeler','Bölgeler','cog|Bölgeler',6)
Q.kart('K-CGBL-01','Bölge türleri','Şekilsel bölge tek ya da birkaç unsurun türdeşliğine, işlevsel bölge merkeze bağlı ilişkiye dayanır.','İşlevsel bir hizmet alanını şekilsel saymak.','kolay','öncüllü',2,'cg-bolge-tur','Şekilsel ve işlevsel bölge')
Q.kart('K-CGBL-02','Bölgenin özellikleri','Bölge ölçüte göre belirlenir; sınırlar ölçüt ve amaca göre değişir, doğal da beşerî de ölçüt olabilir.','Bölgelerin yalnız doğal ölçüte dayandığını sanmak.','orta','düz',3,'cg-bolge-olcut','Bölgenin genel özellikleri')
Q.kart('K-CGBL-03','İşlevsel bölge','İşlevsel bölgede çevre alanlar bir merkeze akışlarla bağlıdır ve merkezden yönetilir.','Bölge türünü yalnız doğal özelliklere bakarak belirlemek.','orta','hikâyeli',3,'cg-bolge-islevsel','İşlevsel bölgeyi tanıma')
Q.kart('K-CGBL-04','Algısal bölge','Algısal bölge, insanların zihnindeki imgeye dayanır; sınırı kişiye göre değişir.','Algısal bölgeyi ölçülebilir verilerle çizilen bölge sanmak.','orta','düz',3,'cg-bolge-algisal','Algısal bölgeyi tanıma')
Q.kart('K-CGBL-05','Ölçüte göre bölge sınırı','Bölge sınırı ölçütlere göre çizilir; iki ölçütün birlikte sağlandığı alan kesişimdir.','Kesişim yerine birleşimi ya da tek ölçütü almak.','zor','şekilli',4,'cg-bolge-izgara','Ölçüte göre bölge sınırı çizme')
Q.kart('K-CGBL-06','Bölge türlerini birlikte ayırma','Bir örnekte ölçütün ne olduğuna bakılarak şekilsel, işlevsel ya da algısal tür belirlenir.','Merkezli hizmet alanlarını şekilsel saymak.','zor','yeni nesil',4,'cg-bolge-uclu','Dört bölgeyi türlerine ayırma')
BIL=B('Bölge türleri','Şekilsel bölge: tek ya da birkaç ortak özelliğe göre ayrılır (iklim, bitki, ürün) · İşlevsel bölge: merkezden yönetilen ya da merkeze bağlı hizmet alanı · Algısal bölge: insanların zihnindeki imgeye göre, sınırı kişiden kişiye değişir')
# ---- 0001
st=[('Tundra bitki örtüsünün yayıldığı alan',True,'bitki örtüsü tek unsura göre türdeş bir alan oluşturur'),
    ('Bir hastanenin tek merkezden yönetilen sağlık hizmeti bölgesi',False,'merkezden yönetilen hizmet alanı işlevsel bölgedir'),
    ('Fındık üretiminin yoğun yapıldığı alan',True,'ürün türdeşliğine dayanır')]
op,dg=oncul(st,['Yalnız I','Yalnız II','II ve III','I ve III','I, II ve III'],'D'); assert dg=={'I','III'}
Q.S('0001','K-CGBL-01','kolay','Verilen bölge örneklerinden şekilsel olanları ayırt eder.',
 metin_oncul('Aşağıda bazı bölge örnekleri verilmiştir.',st,'Bu örneklerden hangileri şekilsel bölgeye örnektir?'),op,'D',
 'Şekilsel bölge örneklerinin belirlenmesi.','Bölgeyi oluşturan ölçüt tek bir ortak özellik mi, yoksa bir merkeze bağlılık mı?',
 [BIL],
 [A('Ölçütü hatırla','Şekilsel bölge, ortak bir özelliğin türdeşliğine dayanır; merkezden yönetim aranmaz.','şekilsel = ortak özellik'),
  A('Örnekleri sına','I ve III ortak bir özelliğe dayanır; II ise tek merkezden yönetilen hizmet alanıdır.','I: şekilsel · II: işlevsel · III: şekilsel'),
  A('Sonuç','Şekilsel örnekler I ve III’tür.','I ve III')],
 'Ortak özellik = şekilsel, merkez ve hizmet = işlevsel.','yeni bölge örnekleri')
# ---- 0002
Q.S('0002','K-CGBL-02','orta','Bölgenin tanımına ve sınırlarının nasıl belirlendiğine ilişkin bilgileri değerlendirir.',
 'Bölgelerle ilgili aşağıdakilerden hangisi yanlıştır?',
 [('Ölçüt değiştiğinde bölgenin sınırları da değişebilir.',False,'Bu ifade doğrudur; bölge sınırı ölçüte bağlıdır.','dikkat'),('Bölgeler yalnızca doğal ölçütlere göre belirlenir; beşerî ölçüt kullanılamaz.',True,'',''),('Aynı alan, farklı amaçlarla birden fazla bölge türüne dâhil edilebilir.',False,'Bu ifade doğrudur; aynı alan farklı ölçütlerle farklı bölgelere girebilir.','dikkat'),('Bölgelendirme, mekânı tanımayı ve planlamayı kolaylaştırır.',False,'Bu ifade doğrudur; bölgelendirme amacı budur.','dikkat'),('Bölgeler arasındaki sınırlar çoğu zaman keskin bir çizgi değil, geçiş alanıdır.',False,'Bu ifade doğrudur; komşu bölgeler arasında geçiş kuşağı bulunur.','dikkat')],'B',
 'Yanlış olan ifade.','Kökte “yanlış” isteniyor; doğru ifadeleri eleyerek kalanı bul.',
 [B('Bölge','Bölge, belirli ölçütlere göre sınırlandırılmış alandır. Ölçüt doğal (iklim, bitki) ya da beşerî (nüfus, ekonomi) olabilir; ölçüt değişirse sınır değişir. Örnek: “Yağışlı alan” ile “sanayi alanı” farklı sınırlara sahiptir.')],
 [A('Kökü oku','“Yanlış” isteniyor; doğru ifadeleri eleyeceksin.','aranan: yanlış ifade'),
  A('Doğruları ele','A, C, D ve E bölgenin ölçüte bağlı, amaçlı ve geçişli olduğunu söyler.','A, C, D, E: doğru'),
  A('Yanlışı bul','Bölgeler beşerî ölçütlerle de belirlenir (nüfus, ekonomi).','B: yanlış')],
 'Köke dikkat et: “yanlış” sorularında doğru olanlar elenir.','genel bölge bilgileri')
# ---- 0003
Q.S('0003','K-CGBL-03','orta','Merkeze bağlı bir hizmet alanını işlevsel bölge olarak tanır.',
 'Bir kargo şirketinin dağıtım merkezi C kentindedir. Çevredeki beş ilçeye gönderilecek paketler bu merkezden yönetilerek dağıtılmaktadır.\nBu dağıtım alanı ile ilgili aşağıdakilerden hangisi söylenebilir?',
 [('Şekilsel bölgedir; çünkü ilçelerin hepsi aynı bitki örtüsüne sahiptir.',False,'Bölgeyi bitki değil, merkezden yönetilen dağıtım ilişkisi oluşturur.','bilgi'),('Algısal bölgedir; çünkü sınırlar insanların zihnindeki imgeye göre çizilmiştir.',False,'Dağıtım alanı somut ve merkezden yönetilir; zihinsel imgeye dayanmaz.','bilgi'),('Doğal bir bölgedir; çünkü sınırlar akarsu havzasına göre belirlenmiştir.',False,'Sınırı doğal bir unsur değil, kargonun merkeze bağlı dağıtımı belirler.','dikkat'),('İklim bölgesidir; çünkü ilçelerin sıcaklık değerleri benzerdir.',False,'Soruda iklimle ilgili bir veri yoktur; ölçüt dağıtım hizmetidir.','dikkat'),('İşlevsel bölgedir; çünkü ilçeler dağıtım açısından C kentindeki merkeze bağlıdır.',True,'','')],'E',
 'Dağıtım alanının bölge türü.','Bölgeyi bir araya getiren şeyin ortak özellik mi, yoksa merkeze bağlılık mı olduğuna bak.',
 [BIL],
 [A('Ölçütü bul','Alanı oluşturan şey, ilçelerin tek bir merkezden yönetilmesidir.','ölçüt: merkeze bağlılık'),
  A('Türü belirle','Merkezden yönetilen hizmet alanı işlevsel bölgedir.','merkez + çevre = işlevsel'),
  A('Şıkları ele','Bitki, imge, havza ve sıcaklık ölçütleri soruda yoktur.','E: doğru · A, B, C, D: yanlış')],
 'Hizmet, dağıtım ve yönetim alanları işlevsel bölgedir.','kargo dağıtım örneği')
# ---- 0004
Q.S('0004','K-CGBL-04','orta','Algısal bölge örneğini diğer bölge türlerinden ayırır.',
 'Aşağıdakilerden hangisi algısal bölgeye örnektir?',
 [('Halkın “tatil yöresi” diye andığı, sınırı belirsiz kıyılar',True,'',''),('Yıllık ortalama yağışı 600 mm’nin üzerinde olan geniş alan',False,'Yağış ölçülebilir bir ölçüttür; bu şekilsel bölgedir.','bilgi'),('Bir belediyenin çöp toplama hizmeti verdiği tüm mahalleler',False,'Merkezden yönetilen hizmet alanıdır; işlevsel bölgedir.','bilgi'),('Pamuk tarımının yoğun olarak yapıldığı geniş ova alanı',False,'Tek bir ürüne dayanan türdeş alandır; şekilsel bölgedir.','bilgi'),('Bir ilin resmî idari sınırları içinde kalan geniş alan',False,'İdari sınır resmî ve kesindir; insanların algısına bağlı değildir.','dikkat')],'A',
 'Algısal bölge örneği.','Sınırı ölçüyle çizilemeyen, kişiden kişiye değişen bölgeyi ara.',
 [BIL],
 [A('Tanımı hatırla','Algısal bölgenin sınırı insanların zihnindeki imgeye göre belirlenir.','algısal = zihinde'),
  A('Şıkları sına','Yağış ve pamuk ölçülebilir ölçüttür; çöp toplama merkezden yönetilir; idari sınır resmîdir.','B, D: şekilsel · C: işlevsel · E: idari'),
  A('Sonuç','Yalnız A kişilerin algısına göre belirlenir.','A')],
 'Ölçülemeyen, kişiye göre değişen sınır algısal bölgenin işaretidir.','algısal bölge örneği')
# ---- 0005
Y={(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,2),(3,3)}
Z={(1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)}
assert len(Y)==12 and len(Z)==9 and len(Y&Z)==5 and len(Z-Y)==4 and len(Y|Z)==16 and len(Y)-len(Y&Z)==7
def izgara(S,x0,y0,c=26):
    o=[]
    for r in range(5):
        for k in range(5):
            on=(r,k) in S
            o.append(f'<rect x="{x0+k*c}" y="{y0+r*c}" width="{c}" height="{c}" stroke-width="1.2" style="fill:{G.ACC if on else "currentColor"};fill-opacity:{.45 if on else .04}"/>')
    return ''.join(o)
sk=svg(310,190,T(70,16,'I. Yağış > 800 mm',size=11,bold=True)+T(240,16,'II. Yükselti > 1000 m',size=11,bold=True)+izgara(Y,5,26)+izgara(Z,175,26)+T(155,178,'Renkli kare: ölçütü sağlayan alan',size=10))
Q.S('0005','K-CGBL-05','zor','İki ölçüte göre çizilen bölgenin alanını şekilden hesaplar.',
 'Aşağıdaki şekilde aynı alanın karelere bölünmüş iki haritası verilmiştir. I. haritada yıllık yağışı 800 mm’den fazla olan, II. haritada yüksekliği 1000 m’den fazla olan kareler renklidir.\nHem yağışı 800 mm’den fazla hem de yüksekliği 1000 m’den fazla olan alan bir bölge kabul edildiğine göre bu bölge, yalnız yağış ölçütüne göre belirlenen bölgeden kaç kare daha küçüktür?',
 [('4',False,'Yalnız yükselti ölçütünü sağlayıp yağış ölçütünü sağlamayan kareleri saymış.','dikkat'),('5',False,'İki ölçütü birlikte sağlayan kareleri (5) bulup bölgenin küçülme miktarını sanmış.','dikkat'),('7',True,'',''),('9',False,'Yükselti ölçütünü sağlayan kare sayısını (9) vermiş.','dikkat'),('16',False,'İki harita birleştirilmiş (kesişim yerine birleşim); 16 kare bulmuş.','bilgi')],'C',
 'Yağış bölgesi ile iki ölçütlü bölge arasındaki kare farkı.','İki ölçütün birlikte sağlandığı kareler her iki haritada da renkli olanlardır; önce onları say.',
 [B('Birden çok ölçüt','Birden çok ölçütle belirlenen bölge, ölçütlerin hepsinin birlikte sağlandığı alandır (kesişim). Örnek: “yağışlı ve yüksek” alan, yalnız “yağışlı” alandan küçüktür.')],
 [A('Yağış bölgesini say','I. haritadaki renkli kareleri say.','yağış ölçütü: 12 kare'),
  A('Ortak kareleri bul','Hem I hem II. haritada renkli olan kareleri say.','her iki ölçüt: 5 kare'),
  A('Farkı hesapla','Yalnız yağış bölgesinden iki ölçütlü bölgeyi çıkar.','12 − 5 = 7 kare'),
  A('Şıkları ele','4 yalnız yükseltiyi, 9 tüm yükselti karelerini, 16 birleşimi verir.','C: 7')],
 'Birden çok ölçüt varsa ortak (kesişen) alanı say; ölçütler arttıkça bölge küçülür.','ızgara kodla sayıldı, tek doğru 7',sekil=sk)
# ---- 0006
kucuk=lambda x:x.replace('İ','i').replace('I','ı').lower()
TURL=['Şekilsel','İşlevsel','Algısal']
R=[('Yıllık ortalama sıcaklığı 10 °C’nin altında kalan alan','Şekilsel','sıcaklık tek ölçütle ölçülür, türdeş alan oluşturur'),
   ('Bir banka şubesinin müşterilerinin yaşadığı ve şubeye bağlı alan','İşlevsel','alan şube merkezine bağlıdır'),
   ('İnsanların zihninde “kuzey” denince canlanan alan','Algısal','sınırı zihindeki imgeye göre değişir'),
   ('Bir limanın merkezden yönetilen sevkiyat ağının ulaştığı alan','İşlevsel','merkezden yönetilen sevkiyat alanıdır')]
dogru=tuple(x[1] for x in R)
cand=[('Şekilsel','İşlevsel','İşlevsel','İşlevsel'),('Şekilsel','İşlevsel','Şekilsel','Şekilsel'),('İşlevsel','Şekilsel','Algısal','İşlevsel'),('Algısal','İşlevsel','Algısal','İşlevsel'),dogru]
assert len(set(cand))==5 and cand[4]==dogru
Rm=['I','II','III','IV']
op=[]
for c in cand:
    if c==dogru: op.append((' – '.join(c),True,'','')); continue
    i=[j for j in range(4) if c[j]!=dogru[j]][0]
    op.append((' – '.join(c),False,f'{Rm[i]}. bölgeyi {kucuk(c[i])} saymış; oysa {R[i][2]}, yani {kucuk(dogru[i])} bölgedir.','bilgi'))
Q.S('0006','K-CGBL-06','zor','Dört örnek bölgeyi ölçütlerine bakarak şekilsel, işlevsel ve algısal olarak ayırır.',
 'Bir araştırmada dört bölge tanımlanmıştır:\nI. '+R[0][0]+'\nII. '+R[1][0]+'\nIII. '+R[2][0]+'\nIV. '+R[3][0]+'\nBu bölgeler sırasıyla hangi bölge türüne örnektir?',op,'E',
 'I, II, III ve IV numaralı bölgelerin türleri.','Her bölgede sınırı belirleyen ölçütün ne olduğuna bak: ortak özellik, merkez ya da zihindeki imge.',
 [BIL],
 [A('Ölçütleri bul','Her bölgenin sınırını neyin belirlediğine bak.','I: sıcaklık · II: şubeye bağlılık · III: zihinde imge · IV: merkezden yönetim'),
  A('Türleri yaz','Ortak özellik şekilsel, merkeze bağlılık işlevsel, zihindeki imge algısaldır.','I: şekilsel · II: işlevsel · III: algısal · IV: işlevsel'),
  A('Şıkla eşle','Sıralama Şekilsel – İşlevsel – Algısal – İşlevsel olmalıdır.','E')],
 'Her örnekte “sınırı ne belirliyor?” sorusunu sor: özellik, merkez ya da imge.','4 örnek, tür eşleştirmesi kodla')
Q.bitir()
