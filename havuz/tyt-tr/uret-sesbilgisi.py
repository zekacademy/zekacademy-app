"""TYT Türkçe · Ses Bilgisi: 4 ana soru (hafif mod). Metinler özgündür."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_dilbilgisi import *
AD=A
KY='ÖSYM TYT Türkçe 2018–2026 (ses bilgisi) ve MEB Türk Dili ve Edebiyatı müfredatı'
KARTLAR={
 'K-SES-01':dict(alt='Ünsüz Yumuşaması',fikir='p, ç, t, k ile biten sözcüklere ünlüyle başlayan ek gelince sertin yumuşadığını tanımak.',tuzak='Ünsüz benzeşmesiyle (ek değişimi) karıştırmak.',zorluk='kolay',kalip='düz',adim=2,tipId='ses-yumusama',kaynak=KY),
 'K-SES-02':dict(alt='Ünsüz Benzeşmesi',fikir='Sert ünsüzle biten sözcüğe gelen ekin ilk ünsüzünün sertleştiğini tanımak.',tuzak='Yumuşamayı (kök değişimi) benzeşme sanmak.',zorluk='orta',kalip='düz',adim=3,tipId='ses-benzesme',kaynak=KY),
 'K-SES-03':dict(alt='Ünlü Uyumları',fikir='Sözcüğün büyük ve küçük ünlü uyumuna uyup uymadığını ünlüleri sınıflayarak belirlemek.',tuzak='Yalnız ilk iki ünlüye bakıp küçük ünlü uyumunu atlamak.',zorluk='orta',kalip='düz',adim=3,tipId='ses-uyum',kaynak=KY),
 'K-SES-04':dict(alt='Ses Olaylarını Eşleştirme',fikir='Sözcüklerde görülen ses olayını (yumuşama, benzeşme, düşme) doğru adlandırmak.',tuzak='Ünlü düşmesini yumuşamayla karıştırmak.',zorluk='zor',kalip='düz',adim=4,tipId='ses-eslestirme',kaynak=KY),
}
TIPLER={'ses-yumusama':'Ünsüz yumuşaması','ses-benzesme':'Ünsüz benzeşmesi','ses-uyum':'Ünlü uyumları','ses-eslestirme':'Ses olayı eşleştirme'}
Q=kur('sesbilgisi','Ses Bilgisi','tr|Ses Bilgisi',KARTLAR,TIPLER); Q.n=4
# --- ünlü uyumu denetimi (kodla) ---
UN='aeıioöuü'; KALIN='aıou'; DUZ='aeıi'; YUV='oöuü'
def buyuk(s):
    v=[c for c in s if c in UN]; return all(x in KALIN for x in v) or all(x not in KALIN for x in v)
def kucuk(s):
    v=[c for c in s if c in UN]
    for p,x in zip(v,v[1:]):
        if p in DUZ and x not in DUZ: return False
        if p in YUV and x not in 'aeuü': return False
    return True
assert (buyuk('karpuz'),kucuk('karpuz'))==(True,False)
for w in ('çiçek','kapı'): assert buyuk(w) and kucuk(w),w
for w in ('kitap','kalem'): assert not buyuk(w),w
B_YUM=B('Ünsüz yumuşaması','p, ç, t, k ile biten sözcüğe ünlüyle başlayan ek gelince p→b, ç→c, t→d, k→ğ olur · kitap → kitabı, ağaç → ağacı')
B_BEN=B('Ünsüz benzeşmesi','sert ünsüzle (f, s, t, k, ç, ş, h, p) biten sözcüğe gelen ekin ilk ünsüzü sert olur · kitap+çı → kitapçı, sokak+ta → sokakta')
B_UYUM=B('Ünlü uyumları','büyük ünlü uyumu: sözcükteki tüm ünlüler kalın (a ı o u) ya da ince (e i ö ü) · küçük ünlü uyumu: düz ünlüden (a e ı i) sonra düz, yuvarlak ünlüden (o ö u ü) sonra u, ü, a ya da e gelir · karpuz: büyüğe uyar, küçüğe uymaz')
B_OLAY=B('Ses olayları','yumuşama: kitap → kitabı · benzeşme: kitap+çı → kitapçı · ünlü düşmesi: ağız → ağzı, burun → burnu, alın → alnı')
Y='yok'; D='var'
# 0001 yumuşama · kolay · D
soru(Q,'0001','K-SES-01','kolay','Ünsüz yumuşaması olan sözcüğü belirler.',2,
 'Aşağıdaki sözcüklerden hangisinde ünsüz yumuşaması vardır?',
 [('evden',Y,'Ev + -den: sözcüğün sonundaki ünsüz değişmemiştir; yumuşama yoktur.','bilgi'),
  ('kalemi',Y,'Kalem + -i: kök sonundaki “m” yumuşak bir ünsüzdür; değişmemiştir.','dikkat'),
  ('okulda',Y,'Okul + -da: kök sonu ünsüz değişmemiştir.','bilgi'),
  ('kitabı',D,'',''),
  ('çocuklar',Y,'Çocuk + -lar: ek ünsüzle başladığı için kökteki “k” yumuşamaz.','dikkat')],
 'D',lambda t:t==D,'Ünsüz yumuşaması bulunan sözcük.',
 'p, ç, t, k ile biten kök, ünlüyle başlayan ek aldığında hangi ünsüze dönüşür?',[B_YUM],
 [AD('Kuralı hatırla','Sert ünsüzle biten sözcüğe ünlüyle başlayan ek gelince sert ünsüz yumuşar.','p→b, ç→c, t→d, k→ğ'),AD('Şıkları ele','A, B, C’de kök sonu değişmemiş; E’de ek ünsüzle başladığı için “k” yumuşamamış.','A, B, C, E: yumuşama yok'),AD('Yumuşamayı bul','“Kitap + -ı” → kitabı: p, b’ye dönüşmüş.','D: kitabı')],
 'Ek ünlüyle başlıyor ve kökün son harfi sertse kökün sonunda yumuşama olabilir.')

# 0002 benzeşme · orta · B
soru(Q,'0002','K-SES-02','orta','Ünsüz benzeşmesi olan sözcüğü belirler.',3,
 'Aşağıdaki sözcüklerden hangisinde ünsüz benzeşmesi vardır?',
 [('evden',Y,'Ev + -den: “v” sert ünsüz değildir; ekin “d”si değişmemiştir.','bilgi'),
  ('kitapçı',D,'',''),
  ('kalemlik',Y,'Kalem + -lik: “m” sert ünsüz değildir; ek aynen kalmıştır.','bilgi'),
  ('burnu',Y,'Burun + -u: ünlü düşmesi görülür; benzeşme yoktur.','dikkat'),
  ('çocuklar',Y,'Çocuk + -lar: “k” sert olsa da ekin “l”si sertleşmemiştir; benzeşme yoktur.','dikkat')],
 'B',lambda t:t==D,'Ünsüz benzeşmesi bulunan sözcük.',
 'Ekin ilk ünsüzü, kökün sonundaki sert ünsüzün etkisiyle sertleşmiş mi?',[B_BEN],
 [AD('Kuralı hatırla','Sert ünsüzle biten sözcüğe -cı, -da, -dan gibi ekler gelince ekin ilk ünsüzü sertleşir.','c→ç, d→t, g→k'),AD('Şıkları ele','A, C, E’de ek değişmemiş; D’de görülen olay ünlü düşmesidir.','A, C, D, E: benzeşme yok'),AD('Benzeşmeyi bul','“Kitap + -cı” → kitapçı: ekin “c”si “ç”ye dönmüş.','B: kitapçı')],
 'Sert ünsüzle biten kökün ardından ekte c, d, g yerine ç, t, k görüyorsan benzeşme vardır.')

# 0003 ünlü uyumu · orta · E
SOZ=[('çiçek',(True,True)),('kapı',(True,True)),('kitap',(False,False)),('kalem',(False,False)),('karpuz',(True,False))]
for w,(b,k) in SOZ:
    if b is True and k is False: pass
    assert buyuk(w)==b,(w,'büyük'); 
    if b: assert kucuk(w)==k,(w,'küçük')
soru(Q,'0003','K-SES-03','orta','Büyük ünlü uyumuna uyup küçük ünlü uyumuna uymayan sözcüğü belirler.',3,
 'Aşağıdaki sözcüklerden hangisi büyük ünlü uyumuna uyar, ancak küçük ünlü uyumuna uymaz?',
 [('çiçek',(buyuk('çiçek'),kucuk('çiçek')),'Ünlüleri i–e: ince ve düz; iki uyuma da uyar.','dikkat'),
  ('kapı',(buyuk('kapı'),kucuk('kapı')),'Ünlüleri a–ı: kalın ve düz; iki uyuma da uyar.','dikkat'),
  ('kitap',(buyuk('kitap'),kucuk('kitap')),'Ünlüleri i–a: biri ince, biri kalın; büyük ünlü uyumuna uymaz.','bilgi'),
  ('kalem',(buyuk('kalem'),kucuk('kalem')),'Ünlüleri a–e: biri kalın, biri ince; büyük ünlü uyumuna uymaz.','bilgi'),
  ('karpuz',(buyuk('karpuz'),kucuk('karpuz')),'','')],
 'E',lambda t:t==(True,False),'Büyük ünlü uyumuna uyup küçük ünlü uyumuna uymayan sözcük.',
 'Önce ünlülerin hepsi kalın mı ince mi diye bak; sonra düz ünlüden sonra yuvarlak ünlü gelip gelmediğini denetle.',[B_UYUM],
 [AD('Ölçütleri hatırla','Büyük ünlü uyumu: ünlüler hep kalın ya da hep ince. Küçük ünlü uyumu: düz ünlüden sonra düz ünlü gelir.','büyük: kalın/ince · küçük: düz/yuvarlak'),AD('Şıkları sına','çiçek ve kapı iki uyuma da uyar; kitap ve kalem büyük ünlü uyumuna uymaz.','A, B, C, D: elenir'),AD('Cevabı seç','karpuz: a–u ünlüleri kalındır (büyük uyum ✓); ama düz “a”dan sonra yuvarlak “u” geldiği için küçük uyum ✗.','E: karpuz')],
 'Önce büyük ünlü uyumunu ele; geriye kalanlarda düz ünlüden sonra yuvarlak ünlü geliyor mu diye bak.')

# 0004 eşleştirme · zor · A
soru(Q,'0004','K-SES-04','zor','Sözcükte görülen ses olayının adını doğru eşleştirir.',4,
 'Aşağıdaki sözcüklerden hangisinin karşısında yazılan ses olayı yanlıştır?',
 [('burnu – ünsüz yumuşaması',Y,'',''),
  ('kitabı – ünsüz yumuşaması',D,'Kitap + -ı → kitabı: p, b’ye dönüşmüştür; ses olayı doğru verilmiştir.','bilgi'),
  ('ağzı – ünlü düşmesi',D,'Ağız + -ı → ağzı: ikinci hecedeki ünlü düşmüştür; doğru verilmiştir.','bilgi'),
  ('sokakta – ünsüz benzeşmesi',D,'Sokak + -ta: ekin “d”si sert “k”nin etkisiyle “t” olmuştur; benzeşmedir.','dikkat'),
  ('alnı – ünlü düşmesi',D,'Alın + -ı → alnı: ikinci hecedeki ünlü düşmüştür; doğru verilmiştir.','dikkat')],
 'A',lambda t:t==Y,'Ses olayı yanlış verilmiş olan sözcük.',
 'Burun + -u sözcüğünde bir ünsüz mü değişiyor, bir ünlü mü kayboluyor?',[B_OLAY],
 [AD('Olayları hatırla','Yumuşamada sert ünsüz yumuşak olur; benzeşmede ek sertleşir; düşmede ünlü kaybolur.','yumuşama · benzeşme · düşme'),AD('Şıkları çözümle','kitabı: p→b (yumuşama) ✓. sokakta: d→t (benzeşme) ✓. ağzı ve alnı: ünlü düşmesi ✓.','B, C, D, E: doğru'),AD('Yanlışı bul','Burun + -u → burnu: “u” ünlüsü düşmüştür; yumuşama değil, ünlü düşmesidir.','A: ünlü düşmesi olmalı')],
 'Bir harf başka bir harfe dönüşüyorsa yumuşama/benzeşme; bir harf kayboluyorsa düşme.')
bitir(Q)
