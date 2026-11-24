"""AYT Fizik · Kara Cisim Işıması · 20 soru (kardeş yok, ipucu 1). Şekil verileri aynı sayılardan üretilir; her cevap ve çeldirici assert edilir."""
import sys,os,json,math
from fractions import Fraction as Fr
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,HV); sys.path.insert(0,os.path.join(HV,'tyt-fiz')); sys.path.insert(0,os.path.join(HV,'tyt-mat'))
import _hafif as H
from _hafif import *
from cizim import tikz_svg
from _hafif_mat import tablo_svg
KONU_AD='Kara Cisim Işıması'; KEY='afiz|Kara Cisim Işıması'
P=Parti('karacisim',KONU_AD,KEY,ders='AYT Fizik',idon='aytfiz'); H.KONU=KONU_AD
KAYNAK='ÖSYM AYT 2018–2026 Fizik modern fizik soruları (yalnız mantık) · 345 AYT Fizik s.355, 364 · Bilgi Sarmal AYT Fizik denemeleri · MEB 12. sınıf kuantum fiziğine giriş'
def kartla(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip): kart(id,alt,fikir,tuzak,z,kalip,adim,tipId,tip,KAYNAK)
def q(no,ad,**k):
    assert len(k['ip'])==1; mk(P,no,ad=ad,adim=len(ad),**k)
def tk(body,opt=''): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small'+opt+']\n'+body+'\n\\end{tikzpicture}')

# ---------- Planck biçimli ışıma eğrileri (şekil verisi) ----------
KK=4.965
def g(x): return x**-5/(math.exp(KK/x)-1)
G1=g(1.0)
def Ish(lam,lm): return lm**-5*g(lam/lm)/G1          # tepe dalga boyu lm olan cismin şiddeti (T ~ 1/lm, doruk ~ T^5)
def Ircl(lam,lm): return lm**-5*(lam/lm)**-4*(math.exp(KK)-1)/KK/1.0  # Rayleigh-Jeans limiti (klasik)
COL=['vurgu','blue!65!black','red!70!black']
def egri_sekil(curves,xmax,ticks=None,tickl=None,ylab='Işıma şiddeti',h=5.0,w=8.0,visible=False,unl_peak=(),ymaxf=1.14):
    """curves: [(etiket, lm)]; ticks: x işaretleri. Tepe noktalarından x eksenine kesikli çizgi."""
    ref=max(Ish(lm,lm) for _,lm in curves)
    ymax=ymaxf; s=[]
    ticks=ticks or []; tickl=tickl or [str(t) for t in ticks]
    head=('\\begin{axis}[width=%.1fcm,height=%.1fcm,axis lines=left,clip mode=individual,xlabel={Dalga boyu (nm)},ylabel={%s},xmin=0,xmax=%d,ymin=0,ymax=%.2f,'
          '%s,ytick=\\empty,tick label style={font=\\small},label style={font=\\small},xlabel style={at={(ticklabel* cs:1.0)},anchor=north west},ylabel style={at={(ticklabel* cs:1.0)},anchor=south west}]\n')%(w,h,ylab,xmax,ymax,('xtick={%s},xticklabels={%s}'%(','.join(str(t) for t in ticks),','.join(tickl))) if ticks else 'xtick=\\empty')
    for i,(lab,lm,*opt) in enumerate(curves):
        pts=[(0,0)]; x=0.3*lm
        while x<=xmax+1e-9:
            pts.append((x,Ish(x,lm)/ref)); x+=max(xmax/70,5)
        pk=Ish(lm,lm)/ref
        col=COL[i%3]
        s.append('\\addplot[%s,very thick] coordinates {%s};'%(col,' '.join('(%.1f,%.4f)'%p for p in pts)))
        lab=lab.replace('T₁','$T_1$').replace('T₂','$T_2$')
        if lab: s.append('\\node[above,font=\\small\\bfseries] at (axis cs:%.1f,%.4f) {%s};'%(lm,pk,lab))
        s.append('\\draw[dashed,gray] (axis cs:%.1f,0) -- (axis cs:%.1f,%.4f);'%(lm,lm,pk))
    return tk(head+'\n'.join(s)+'\n\\end{axis}')

def sira_cmp(curves,lam):  # yardımcı: aynı dalga boyunda şiddet karşılaştırma (assert için)
    return [Ish(lam,lm) for _,lm in curves]

# ---------- seviye (merdiven) şekli ----------
def merdiven(nmax,oklar,lab_ok=True):
    s=[]
    for n in range(nmax+1):
        y=n*0.8
        s.append('\\draw[thick] (0.6,%.2f) -- (3.0,%.2f);\\node[left] at (0.5,%.2f) {$%s$};'%(y,y,y,('0' if n==0 else ('hf' if n==1 else '%dhf'%n))))
    cols=['vurgu','blue!65!black','red!70!black']
    for i,(a,b,lab) in enumerate(oklar):
        x=1.1+i*0.85
        s.append('\\draw[%s,very thick,-{Stealth[length=2.2mm,width=2mm]}] (%.2f,%.2f) -- (%.2f,%.2f);'%(cols[i%3],x,a*0.8,x,b*0.8))
        s.append('\\node[%s,font=\\small\\bfseries,fill=white,inner sep=1pt] at (%.2f,%.2f) {%s};'%(cols[i%3],x+0.0,(a+b)*0.4+0.0,lab))
    s.append('\\node[above] at (1.8,%.2f) {Enerji};'%(nmax*0.8+0.25))
    return tk('\n'.join(s))

ROM=['I','II','III']
COMB=[('Yalnız I',{0}),('Yalnız II',{1}),('Yalnız III',{2}),('I ve II',{0,1}),('I ve III',{0,2}),('II ve III',{1,2}),('I, II ve III',{0,1,2})]
def onc(no,hedef,giris,stm,ip,bilgi,puf,istenen,tipId,tip,z,alt,kaz,kart,kalip,sekil=None,kok='yargılarından hangileri doğrudur?'):
    T={i for i,s in enumerate(stm) if s[1]}
    idx=[i for i,(a,b) in enumerate(COMB) if b==T]; assert len(idx)==1; ci=idx[0]; p='ABCDE'.index(hedef)
    assert p<=ci and 4-p<=6-ci,(no,ci,p)
    win=COMB[ci-p:ci-p+5]; assert len(win)==5 and win[p][1]==T
    yan=[]
    for a,b in win:
        if b==T: continue
        d=sorted(b^T)
        yan.append((a,' '.join(stm[i][3] for i in d),'bilgi'))
    metin=giris+'\nBuna göre,\n'+'\n'.join(f'{ROM[i]}. {s[0]}' for i,s in enumerate(stm))+'\n'+kok
    ad=[A(f'{ROM[i]}. yargıyı incele',s[2],f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış')) for i,s in enumerate(stm)]
    ad.append(A('Sonucu yaz','Doğru olan yargıları birleştir.',' · '.join(f'{ROM[i]}: '+('doğru' if s[1] else 'yanlış') for i,s in enumerate(stm))+' → '+COMB[ci][0]))
    q(no,ad,tipId=tipId,tip=tip,z=z,alt=alt,kaz=kaz,kart=kart,kalip=kalip,metin=metin,dogru=COMB[ci][0],yan=yan,sira=[a for a,b in win],
      istenen=istenen,ip=ip,bilgi=bilgi,puf=puf,sekil=sekil)

# ================= KARTLAR =================
kartla('K-AFKC-01','Işıma şiddeti–dalga boyu grafiği','Eğrinin tepe dalga boyu sıcaklığı belirler: tepe dalga boyu küçükse sıcaklık büyüktür; sıcak cismin eğrisi her dalga boyunda daha yukarıdadır, altındaki alan (toplam güç) büyüktür.','Tepe dalga boyu büyük cismi sıcak sanmak; eğrinin yüksekliğine bakıp sıcaklığı yorumlamak; ışımanın tek dalga boyunda olduğunu düşünmek.','kolay','grafik',3,'kc-grafik','Işıma şiddeti–dalga boyu grafiği yorumu')
kartla('K-AFKC-02','Wien yer değiştirme yasası','λ_maks·T = sabit (Wien sabiti b); sıcaklık ile tepe dalga boyu ters orantılıdır. Dalga boyu m ya da nm cinsinden, sıcaklık kelvin olarak alınır.','Doğru orantı kurmak; nm–m dönüşümünde üs hatası; kelvin farkını dalga boyu farkı sanmak.','orta','grafik',4,'kc-wien','Wien yasası ve tepe dalga boyu hesabı')
kartla('K-AFKC-03','Sıcaklık artışının etkileri','Sıcaklık artınca tepe dalga boyu küçülür, her dalga boyundaki şiddet ve eğri altındaki alan büyür; tek tek fotonların hepsinin enerjisi artmaz, spektrum sürekli kalır.','Bütün fotonların enerjisinin arttığını sanmak; tepe dalga boyunun büyüdüğünü düşünmek; ışımanın yalnız tek renkte olduğunu sanmak.','orta','grafik',3,'kc-sicaklik','Sıcaklık değişiminin ışımaya etkisi')
kartla('K-AFKC-04','Işıma rengi ve görünür bölge','Görünür bölgede dalga boyu küçüldükçe renk kırmızıdan mora gider; tepe dalga boyu küçük olan cisim daha sıcaktır. Kızılötesine kayan tepe, cismin görünürde de az ışıma yaptığını gösterir.','Sıcak cismi kırmızı, soğuk cismi mor sanmak; tepe dalga boyu görünür dışındaysa hiç görünür ışıma yapılmadığını düşünmek.','orta','şekilli',3,'kc-renk','Tepe dalga boyu, renk ve görünür bölge')
kartla('K-AFKC-05','Planck’ın kuantum varsayımı','Salınıcılar yalnız E = n·h·f enerjili düzeylerde bulunur ve enerji alışverişi hf’nin tam katları kadar olur; bir düzeyden komşu düzeye geçişte hf enerjili ışıma yayılır.','Enerjiyi sürekli sanmak; geçişte yayılan enerjiyi son düzeyin enerjisi sanmak; hf ile nhf’yi karıştırmak.','orta','şekilli',4,'kc-planck','Planck’ın kuantum varsayımı ve enerji düzeyleri')
kartla('K-AFKC-06','Klasik fizik ve kara cisim ışıması','Klasik fizik kısa dalga boylarında şiddetin sonsuza gideceğini öngörür; deneysel eğri tepe yapıp azalır ve uzun dalga boylarında klasik öngörüye yaklaşır. Planck, enerji alışverişinin kesikli olduğunu varsayarak deneyle uyum sağlamıştır.','Planck’ın ışımanın sürekli olduğunu varsaydığını düşünmek; klasik eğriyi deneysel sanmak.','orta','grafik',3,'kc-tarih','Klasik fiziğin yetersizliği ve Planck’ın çözümü')
kartla('K-AFKC-07','Tepe fotonunun enerjisi','E = h·f = hc/λ; tepe fotonunun enerjisi tepe dalga boyuyla ters, sıcaklıkla doğru orantılıdır. Dalga boyu nm iken hc = 1240 eV·nm, Å iken hc = 12400 eV·Å alınır.','nm–Å dönüşüm hatası; enerjiyi dalga boyu ile doğru orantılı sanmak; enerjiyi sıcaklığın karesiyle orantılamak.','orta','grafik',3,'kc-enerji','Tepe fotonunun enerjisi ve sıcaklık')

# ================= SORULAR =================
# ---- 01 kolay · iki eğri, sıcaklık oranı ----
lK,lL=400,600
assert Fr(lL,lK)==Fr(3,2) and Fr(lL,lK)**2==Fr(9,4) and Fr(lK,lL)==Fr(2,3) and Fr(lK,lL)**2==Fr(4,9)
SK=egri_sekil([('K',lK),('L',lL)],1800,[lK,lL])
q('0001',[A('Tepe dalga boylarını oku','Her eğrinin en yüksek noktasının altındaki dalga boyu, o cismin tepe dalga boyudur.','λ_K = 400 nm · λ_L = 600 nm'),
  A('Wien yasasını yaz','Tepe dalga boyu ile mutlak sıcaklığın çarpımı sabittir; yani ters orantılıdır.','λ_K × T_K = λ_L × T_L'),
  A('Sıcaklık oranını bul','Oran, tepe dalga boylarının ters oranına eşittir.','T_K ÷ T_L = λ_L ÷ λ_K = 600 ÷ 400 = 3/2')],
 tipId='kc-grafik',tip='Işıma şiddeti–dalga boyu grafiği yorumu',z='kolay',alt='Işıma Grafikleri',kaz='Işıma şiddeti–dalga boyu grafiğinden tepe dalga boylarını okuyup cisimlerin sıcaklıklarını oranlar.',
 kart='K-AFKC-01 (iki eğri, tepe dalga boyları) · sıcaklık oranı',kalip='grafik',
 metin='K ve L kara cisimlerinin ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir.\nBuna göre, K cisminin sıcaklığının L cisminin sıcaklığına oranı T_K/T_L kaçtır?',
 dogru='3/2',yan=[('4/9','Oranın tersinin karesini almış: (400 ÷ 600)² = 4/9.','islem'),('2/3','Tepe dalga boylarını doğru orantılı kabul edip 400 ÷ 600 = 2/3 bulmuş.','bilgi'),('1','Sıcaklığın tepe dalga boyunu değiştirmediğini düşünerek iki cismi aynı sıcaklıkta kabul etmiş.','bilgi'),('9/4','Tepe dalga boylarının oranının karesini almış: (600 ÷ 400)² = 9/4.','islem')],
 sira=['4/9','2/3','1','3/2','9/4'],
 istenen='K cisminin sıcaklığının L cisminin sıcaklığına oranı.',ip=['Sıcaklık ile tepe dalga boyu arasındaki ilişki doğru orantı mı, ters orantı mı?'],
 bilgi=[B('Wien yer değiştirme yasası','λ_maks × T = sabit. Sıcaklık arttıkça eğrinin tepe dalga boyu küçülür. Örnek: tepe dalga boyu 3 katına çıkan cismin sıcaklığı 3 kat azalmıştır')],
 puf='Tepe dalga boyu küçüldükçe sıcaklık artar; oran tersine çevrilir.',sekil=SK)

# ---- 02 kolay · üç eğri öncüllü ----
l2=[('K',600),('L',750),('M',900)]
for lam in (300,600,750,900,1500,2000): v=sira_cmp(l2,lam); assert v[0]>v[1]>v[2]
SK=egri_sekil(l2,1500,[600,750,900])
onc('0002','A','K, L ve M kara cisimlerinin ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir.',
 [('Cisimlerin sıcaklıkları arasında T_K > T_L > T_M ilişkisi vardır.',True,'Tepe dalga boyu en küçük olan cisim en sıcak, en büyük olan en soğuktur; 600 < 750 < 900 nm olduğundan K en sıcak, M en soğuktur.','I numaralı yargıda tepe dalga boyu büyük olan cismin daha sıcak olduğunu düşünmüş.'),
  ('M cisminin en şiddetle yaydığı fotonun frekansı, üç cismin içinde en büyüğüdür.',False,'Frekans dalga boyuyla ters orantılıdır; tepe dalga boyu en büyük olan M’nin tepe fotonunun frekansı en küçüktür.','II numaralı yargıda dalga boyu büyük olan ışığın frekansının da büyük olduğunu düşünmüş.'),
  ('Cisimlerden yalnız K, kızılötesi bölgede ışıma yapar.',False,'Kara cisim sürekli bir spektrum yayar; üç cismin de eğrisi uzun dalga boylarında sıfırdan büyüktür, yani hepsi kızılötesinde de ışıma yapar.','III numaralı yargıda ışımanın yalnız tepe dalga boyunda yapıldığını düşünmüş.')],
 ['Her yargının eğrinin hangi özelliğiyle (tepe konumu, yükseklik, yayılım) ilgili olduğunu belirle.'],
 [B('Kara cisim spektrumu','Kara cisim, her dalga boyunda ışıma yapar; sıcaklık yalnız eğrinin şeklini ve tepe noktasını değiştirir. Örnek: 3000 K’lik bir cisim de çok az da olsa mor ışık yayar')],
 'Yargıdaki niceliği eğri üzerinde nerede okuyacağını belirle.','Doğru olan yargılar.','kc-grafik','Işıma şiddeti–dalga boyu grafiği yorumu','kolay','Işıma Grafikleri','Üç eğrili grafikte sıcaklık, frekans ve spektrum hakkındaki yargıları değerlendirir.','K-AFKC-01 (üç eğri) · nitel öncüllü','grafik',sekil=SK)

# ---- 03 kolay · Wien orantısı, şekilsiz ----
T3a,T3b,l3=2000,4000,1500
l3b=Fr(l3*T3a,T3b); assert l3b==750 and Fr(l3)/4==Fr(375) and Fr(l3*T3b,T3a)==3000 and l3*4==6000
q('0003',[A('Sıcaklık oranını yaz','Sıcaklık 2000 K’den 4000 K’ye çıkarak 2 katına çıkmıştır.','T₂ ÷ T₁ = 4000 ÷ 2000 = 2'),
  A('Wien yasasını uygula','Tepe dalga boyu sıcaklıkla ters orantılıdır; sıcaklık 2 katına çıkınca dalga boyu yarıya iner.','λ₁ × T₁ = λ₂ × T₂'),
  A('Dalga boyunu hesapla','Değerler yerine konur.','λ₂ = 1500 × 2000 ÷ 4000 = 750 nm')],
 tipId='kc-wien',tip='Wien yasası ve tepe dalga boyu hesabı',z='kolay',alt='Wien Yasası',kaz='Wien yasasında sıcaklık değişince tepe dalga boyunun nasıl değiştiğini orantıyla hesaplar.',
 kart='K-AFKC-02 (orantı kurma) · sıcaklığın iki katına çıkması',kalip='düz',
 metin='Sıcaklığı 2000 K olan bir kara cismin ışıma şiddetinin en büyük olduğu dalga boyu 1500 nm’dir. Cismin sıcaklığı daha sonra 4000 K’ye çıkarılmaktadır.\nBuna göre, bu durumda cismin ışıma şiddetinin en büyük olduğu dalga boyu kaç nm olur?',
 dogru=750,yan=[(375,'Tepe dalga boyunun sıcaklığın karesiyle ters orantılı olduğunu düşünmüş: 1500 ÷ 4 = 375.','bilgi'),(1500,'Tepe dalga boyunun sıcaklıkla değişmediğini düşünmüş.','bilgi'),(3000,'Dalga boyunu sıcaklıkla doğru orantılı alıp 1500 × 2 = 3000 bulmuş.','bilgi'),(6000,'Dalga boyunun sıcaklığın karesiyle doğru orantılı olduğunu düşünmüş: 1500 × 4 = 6000.','bilgi')],
 istenen='Sıcaklık 4000 K iken tepe dalga boyu (nm).',ip=['Sıcaklık iki katına çıkarken tepe dalga boyunun hangi yönde ve kaç kat değiştiğini düşün.'],
 bilgi=[B('Wien yer değiştirme yasası','λ_maks × T = sabit. Sıcaklık arttıkça tepe dalga boyu aynı oranda küçülür. Örnek: sıcaklık 3 katına çıkarsa tepe dalga boyu üçte birine iner')],
 puf='Sıcaklık ve tepe dalga boyu ters orantılıdır; çarpımları sabittir.')

# ---- 04 orta · tek eğri, Wien sabiti ile sıcaklık ----
b_=Fr(3,1000); l4=Fr(1000)*Fr(1,10**9); T4=b_/l4; assert T4==3000
assert b_/Fr(1,10**8)==300000 and b_/Fr(1,10**5)==300 and b_/Fr(1,10**7)==30000 and b_*1000==3
SK=egri_sekil([('',1000)],3000,[1000],ylab='Işıma şiddeti',w=7.0)
q('0004',[A('Tepe dalga boyunu oku','Eğrinin en yüksek noktasındaki dalga boyu 1000 nm’dir.','λ_maks = 1000 nm'),
  A('Metreye çevir','1 nm = 10⁻⁹ m olduğundan dalga boyu metre cinsine çevrilir.','λ_maks = 1000 × 10⁻⁹ = 10⁻⁶ m'),
  A('Wien yasasını uygula','Sıcaklık, Wien sabitinin tepe dalga boyuna bölümüne eşittir.','T = b ÷ λ_maks'),
  A('Sıcaklığı hesapla','Değerler yerine konur.','T = 3 × 10⁻³ ÷ 10⁻⁶ = 3000 K')],
 tipId='kc-wien',tip='Wien yasası ve tepe dalga boyu hesabı',z='orta',alt='Wien Yasası',kaz='Işıma grafiğinden okunan tepe dalga boyu ile Wien yasasını kullanarak sıcaklığı hesaplar.',
 kart='K-AFKC-02 (Wien sabiti ile sıcaklık) · nm–m dönüşümü',kalip='grafik',
 metin='Bir kara cismin ışıma şiddetinin dalga boyuna bağlı değişim grafiği şekilde verilmiştir.\n(Wien sabiti 3 × 10⁻³ m·K alınız.)\nBuna göre, cismin sıcaklığı kaç K’dir?',
 dogru=3000,yan=[(300,'1000 nm’yi 10⁻⁵ m alarak 3 × 10⁻³ ÷ 10⁻⁵ = 300 bulmuş.','islem'),(1000,'Grafikteki dalga boyu değerini (1000) sıcaklık olarak yazmış.','dikkat'),(30000,'1000 nm’yi 10⁻⁷ m alarak 3 × 10⁻³ ÷ 10⁻⁷ = 30000 bulmuş.','islem'),(300000,'1000 nm’yi 10⁻⁸ m alarak 3 × 10⁻³ ÷ 10⁻⁸ = 300000 bulmuş.','islem')],
 istenen='Cismin sıcaklığı (K).',ip=['Wien sabiti metre cinsinden verildiği için grafikteki dalga boyunu aynı birime çevir.'],
 bilgi=[B('Birim dönüşümü','1 nm = 10⁻⁹ m ve 1 Å = 10⁻¹⁰ m’dir. Wien yasasında T kelvin, λ metre alınır. Örnek: 250 nm = 2,5 × 10⁻⁷ m')],
 puf='Wien sabiti metre·kelvin olduğu için nm’yi metreye çevirmeden hesaplama.',sekil=SK)

# ---- 05 orta · aynı cisim T1, T2 öncüllü ----
SK=egri_sekil([('T₁',900),('T₂',600)],2700)
for lam in (200,400,600,900,1500,2500): v=sira_cmp([('a',900),('b',600)],lam); assert v[1]>v[0]
onc('0005','D','Bir kara cismin T₁ ve T₂ sıcaklıklarındaki ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir.',
 [('T₂ sıcaklığında ışıma eğrisinin tepe dalga boyu, T₁ sıcaklığındakinden küçüktür.',True,'Eğrinin tepesi T₂’de daha kısa dalga boyundadır; Wien yasasına göre bu, sıcaklığın T₂’de daha büyük olduğunu gösterir.','I numaralı yargıda sıcaklık arttıkça tepe dalga boyunun büyüdüğünü düşünmüş.'),
  ('Cismin birim zamanda yaydığı toplam enerji, T₂ sıcaklığında T₁ sıcaklığındakinden büyüktür.',True,'Eğrinin altındaki alan toplam ışıma gücünü verir; T₂ eğrisi her dalga boyunda daha yukarıda olduğundan alanı daha büyüktür.','II numaralı yargıda toplam ışımanın sıcaklıkla değişmediğini düşünmüş.'),
  ('T₂ sıcaklığında yayılan fotonların her birinin enerjisi, T₁ sıcaklığında yayılan fotonların her birinin enerjisinden büyüktür.',False,'İki sıcaklıkta da spektrum süreklidir; T₂’de de uzun dalga boylu, düşük enerjili fotonlar yayılır ve T₁’de de kısa dalga boylu fotonlar vardır.','III numaralı yargıda bütün fotonların enerjisinin sıcaklıkla arttığını düşünmüş.')],
 ['Eğrinin altındaki alanın ve tepe konumunun neyi gösterdiğini düşün.'],
 [B('Eğri altındaki alan','Işıma şiddeti–dalga boyu eğrisinin altındaki alan, cismin birim zamanda yaydığı toplam enerjiyi (ışıma gücünü) gösterir. Örnek: bir eğri diğerinin her noktasının üstündeyse alanı daha büyüktür')],
 'Eğri altındaki alanın ve tepe konumunun ne gösterdiğine bak.','Doğru olan yargılar.','kc-sicaklik','Sıcaklık değişiminin ışımaya etkisi','orta','Sıcaklığın Etkisi','Aynı cismin farklı sıcaklıklardaki ışıma eğrilerini karşılaştırarak tepe dalga boyu, toplam güç ve foton enerjisi hakkında yargılar değerlendirir.','K-AFKC-03 (T₁–T₂ eğrileri) · toplam güç ve foton enerjisi','grafik',sekil=SK)

# ---- 06 orta · Planck merdiveni öncüllü ----
SK=merdiven(4,[(3,2,'K'),(4,2,'L'),(3,0,'M')])
onc('0006','A','Planck’ın kuantum varsayımına göre ışıma yapan bir salınıcının enerjisi, frekansı f olmak üzere yalnız belirli düzeylerde bulunur. Bu düzeyler ve salınıcının yaptığı üç geçiş şekilde verilmiştir. K, L ve M geçişlerinde salınıcı birer foton yaymaktadır.',
 [('K geçişinde yayılan fotonun enerjisi, L geçişinde yayılan fotonun enerjisine eşittir.',False,'K geçişinde enerji farkı 3hf − 2hf = hf, L geçişinde 4hf − 2hf = 2hf olduğundan iki fotonun enerjisi eşit değildir.','I numaralı yargıda iki geçişin de aynı son düzeye indiğinden fotonların eşit enerjili olduğunu düşünmüş.'),
  ('M geçişinde yayılan fotonun frekansı, K geçişinde yayılan fotonun frekansının 3 katıdır.',True,'M’de enerji farkı 3hf, K’de hf’dir; foton enerjisi frekansla doğru orantılı olduğundan M’nin fotonunun frekansı 3 f, K’ninki f’dir.','II numaralı yargıda yayılan fotonun frekansının geçişten bağımsız olduğunu düşünmüş.'),
  ('L geçişinde yayılan fotonun dalga boyu, M geçişinde yayılan fotonun dalga boyundan küçüktür.',False,'Dalga boyu enerjiyle ters orantılıdır; L’nin enerjisi (2hf) M’ninkinden (3hf) küçük olduğundan L’nin dalga boyu daha büyüktür.','III numaralı yargıda enerjisi küçük fotonun dalga boyunun da küçük olduğunu düşünmüş.')],
 ['Her geçişte yayılan fotonun enerjisini, iki düzey arasındaki farktan bul.'],
 [B('Planck’ın kuantum varsayımı','Salınıcının enerjisi E = n·h·f biçimindedir (n = 0, 1, 2, …). Bir düzeyden diğerine geçişte yayılan ya da soğurulan enerji, düzeylerin enerji farkına eşittir. Örnek: 5hf düzeyinden 4hf düzeyine inen salınıcı hf enerjili foton yayar')],
 'Yayılan fotonun enerjisi, iki düzeyin enerjileri arasındaki farktır.','Doğru olan yargılar.','kc-planck','Planck’ın kuantum varsayımı ve enerji düzeyleri','orta','Planck Varsayımı','Salınıcının enerji düzeyleri arasındaki geçişlerde yayılan fotonların enerji, frekans ve dalga boyunu karşılaştırır.','K-AFKC-05 (enerji merdiveni, üç geçiş) · öncüllü','şekilli',sekil=SK)

# ---- 07 orta · kuantum sayısı, şekilsiz ----
h7=Fr(66,10)*Fr(10)**-34; f7=5*Fr(10)**14; E7=Fr(132,100)*Fr(10)**-18
n7=E7/(h7*f7); assert Fr(66,10)*Fr(10)**-34*4*Fr(10)**14==Fr(264,100)*Fr(10)**-19
assert n7==4 and E7/(h7*Fr(5)*Fr(10)**15)==Fr(2,5) and E7/(h7*Fr(5)*Fr(10)**13)==40 and E7/(h7*f7/2)==8 and E7/(2*h7*f7)==2
q('0007',[A('Bir kuantumun enerjisini bul','Salınıcı enerjisini hf’nin katları olarak alır; önce hf hesaplanır.','hf = 6,6 × 10⁻³⁴ × 5 × 10¹⁴ = 3,3 × 10⁻¹⁹ J'),
  A('Planck bağıntısını yaz','Toplam enerji, kuantum sayısı ile hf’nin çarpımıdır.','E = n × h × f'),
  A('Kuantum sayısını bul','Toplam enerji hf’ye bölünür.','n = 1,32 × 10⁻¹⁸ ÷ 3,3 × 10⁻¹⁹ = 4')],
 tipId='kc-planck',tip='Planck’ın kuantum varsayımı ve enerji düzeyleri',z='orta',alt='Planck Varsayımı',kaz='Planck bağıntısıyla salınıcının kuantum sayısını hesaplar.',
 kart='K-AFKC-05 (E = nhf) · sayısal kuantum sayısı',kalip='düz',
 metin='Planck’ın kuantum varsayımına göre, frekansı 5 × 10¹⁴ Hz olan bir salınıcının enerjisi E = n·h·f bağıntısına uyar. Salınıcının enerjisi 1,32 × 10⁻¹⁸ J olarak ölçülmüştür.\n(Planck sabiti h = 6,6 × 10⁻³⁴ J·s alınız.)\nBuna göre, salınıcının kuantum sayısı n kaçtır?',
 dogru=4,yan=[(Fr(2,5),'Frekansı 5 × 10¹⁵ Hz alarak hf’yi 3,3 × 10⁻¹⁸ J bulmuş ve n = 0,4 hesaplamış.','islem'),(2,'Enerjiyi 2hf’ye bölerek n = 2 bulmuş.','bilgi'),(8,'Bağıntıyı E = ½·n·h·f alarak n = 8 bulmuş.','bilgi'),(40,'Frekansı 5 × 10¹³ Hz alarak hf’yi 3,3 × 10⁻²⁰ J bulmuş ve n = 40 hesaplamış.','islem')],
 istenen='Salınıcının kuantum sayısı n.',ip=['Önce salınıcının bir kuantumunun enerjisini bul; sonra toplam enerjinin kaç kuantum içerdiğine bak.'],
 bilgi=[B('Enerji kuantumu','Frekansı f olan bir salınıcı için en küçük enerji paketi hf’dir ve toplam enerji E = n·h·f olur (n = 0, 1, 2, …). Örnek: 2hf enerjili salınıcıda n = 2’dir')],
 puf='Önce bir kuantumun (hf) enerjisini hesapla, sonra toplam enerjiyi buna böl.')

# ---- 08 orta · renkler ----
def renk(l): return 'Kırmızı' if 620<=l<=750 else 'Yeşil' if 495<=l<=570 else 'Mor' if 380<=l<=450 else '?'
l8=[('K',650),('L',540),('M',430)]
cev8=' – '.join(renk(l) for _,l in l8); assert cev8=='Kırmızı – Yeşil – Mor'
for lam in (300,430,540,650,1200): v=sira_cmp(l8,lam); assert v[2]>v[1]>v[0]
SK=egri_sekil(l8,1900,[400,700],['400','700'])
q('0008',[A('Tepe dalga boylarını sırala','Eğrilerin tepe noktaları görünür bölgede, 400 ile 700 nm arasındadır; K en sağda, M en soldadır.','λ_K > λ_L > λ_M'),
  A('Dalga boyu–renk ilişkisini hatırla','Görünür ışıkta dalga boyu küçüldükçe renk kırmızıdan mora doğru gider.','kırmızı: 700 nm civarı · mor: 400 nm civarı'),
  A('Renkleri eşleştir','En büyük tepe dalga boyu kırmızıya, en küçüğü mora, ortadaki yeşile karşılık gelir.','K: kırmızı · L: yeşil · M: mor')],
 tipId='kc-renk',tip='Tepe dalga boyu, renk ve görünür bölge',z='orta',alt='Işımanın Rengi',kaz='Işıma grafiğindeki tepe dalga boylarına göre cisimlerin en şiddetle yaydığı ışığın renklerini belirler.',
 kart='K-AFKC-04 (tepe dalga boyu ve renk) · görünür bölge sınırları',kalip='grafik',
 metin='K, L ve M kara cisimlerinin ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir. Görünür ışık bölgesi yaklaşık 400 nm (mor) ile 700 nm (kırmızı) arasındadır.\nBuna göre, K, L ve M cisimlerinin en şiddetle yaydığı ışıkların renkleri sırasıyla aşağıdakilerden hangisidir?',
 dogru=cev8,yan=[('Mor – Yeşil – Kırmızı','Dalga boyu büyük olan ışığı mor, küçük olanı kırmızı sanarak renk sırasını tersine bilmiş.','bilgi'),('Yeşil – Kırmızı – Mor','Renk sırasını yeşil, kırmızı, mor biçiminde bilip dalga boyu büyükten küçüğe bu sırayı izlemiş.','bilgi'),('Kırmızı – Mor – Yeşil','Renk sırasını kırmızı, mor, yeşil biçiminde bilip dalga boyu büyükten küçüğe bu sırayı izlemiş.','bilgi'),('Mor – Kırmızı – Yeşil','Renk sırasını mor, kırmızı, yeşil biçiminde bilip dalga boyu büyükten küçüğe bu sırayı izlemiş.','bilgi')],
 sira=[cev8,'Mor – Yeşil – Kırmızı','Yeşil – Kırmızı – Mor','Kırmızı – Mor – Yeşil','Mor – Kırmızı – Yeşil'],
 istenen='K, L ve M’nin en şiddetle yaydığı ışıkların renkleri.',ip=['Görünür bölgede dalga boyu ile renk arasındaki sıralamayı, grafikteki işaretli iki sınır değerinden yararlanarak kur.'],
 bilgi=[B('Görünür ışık','Görünür bölgede dalga boyu büyükten küçüğe doğru renkler kırmızı, turuncu, sarı, yeşil, mavi, mordur. Örnek: 600 nm civarındaki ışık turuncu–sarıdır')],
 puf='Grafikteki sınır değerlerini renk uçlarıyla eşleştir.',sekil=SK)

# ---- 09 orta · iki yıldız, tepe fotonu enerji farkı (Å) ----
la,lb=800,1240; Ea=Fr(12400,la*10); Eb=Fr(12400,lb*10); d9=Ea-Eb
assert Ea==Fr(155,100) and Eb==1 and d9==Fr(55,100)
assert Fr(12400,la)-Fr(12400,lb)==Fr(55,10) and Fr(12400,la*100)-Fr(12400,lb*100)==Fr(55,1000) and Ea+Eb==Fr(255,100)
l9=[('K',la),('L',lb)]
for lam in (300,800,1240,2500): v=sira_cmp(l9,lam); assert v[0]>v[1]
SK=egri_sekil(l9,3000,[la,lb])
q('0009',[A('Tepe dalga boylarını oku','Grafikte K’nin tepesi 800 nm’de, L’nin tepesi 1240 nm’dedir.','λ_K = 800 nm · λ_L = 1240 nm'),
  A('Ångström’e çevir','hc değeri eV·Å cinsinden verildiği için dalga boyları Å olmalıdır; 1 nm = 10 Å.','λ_K = 8000 Å · λ_L = 12400 Å'),
  A('Foton enerjilerini hesapla','Fotonun enerjisi hc’nin dalga boyuna bölümüdür.','E_K = 12400 ÷ 8000 = 1,55 eV · E_L = 12400 ÷ 12400 = 1 eV'),
  A('Farkı bul','K’nin tepe fotonunun enerjisinden L’ninki çıkarılır.','ΔE = 1,55 − 1 = 0,55 eV')],
 tipId='kc-enerji',tip='Tepe fotonunun enerjisi ve sıcaklık',z='orta',alt='Foton Enerjisi',kaz='Işıma grafiğindeki tepe dalga boylarına karşılık gelen foton enerjilerini hesaplayıp karşılaştırır.',
 kart='K-AFKC-07 (E = hc/λ, Å birimi) · iki yıldızın tepe fotonları',kalip='grafik',
 metin='Yüzey sıcaklıkları farklı K ve L yıldızlarının ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir. Yıldızlar kara cisim gibi davranmaktadır.\n(hc = 12400 eV·Å alınız.)\nBuna göre, K yıldızının en şiddetle yaydığı fotonun enerjisi, L yıldızınınkinden kaç eV fazladır?',
 dogru=d9,yan=[(Fr(55,1000),'1 nm’yi 100 Å alarak dalga boylarını 80000 Å ve 124000 Å bulmuş: 0,155 − 0,1 = 0,055.','islem'),(Fr(155,100),'Yalnız K’nin tepe fotonunun enerjisini (1,55 eV) vermiş, L’ninkini çıkarmamış.','dikkat'),(Fr(255,100),'İki fotonun enerjisini çıkarmak yerine toplamış: 1,55 + 1 = 2,55.','dikkat'),(Fr(55,10),'nm cinsindeki dalga boylarını Å’e çevirmeden kullanmış: 15,5 − 10 = 5,5.','dikkat')],
 istenen='K’nin tepe fotonunun enerjisinin L’ninkinden fazlası (eV).',ip=['hc değerinin birimi ile grafikteki dalga boylarının biriminin aynı olması gerekir.'],
 bilgi=[B('Foton enerjisi','E = h·f = hc/λ. Birimler: hc = 12400 eV·Å = 1240 eV·nm ve 1 nm = 10 Å. Örnek: 4000 Å’luk bir fotonun enerjisi 12400 ÷ 4000 = 3,1 eV’tur')],
 puf='Foton enerjisi dalga boyuyla ters orantılıdır; birimleri eşitlemeyi unutma.',sekil=SK)

# ---- 10 orta · klasik ve deneysel eğri öncüllü ----
def sekil10():
    lm=500; xmax=3000; ymaxf=1.5; ref=1.0
    pl=[(0,0)]; x=0.3*lm
    while x<=xmax+1e-9: pl.append((x,Ish(x,lm)/Ish(lm,lm))); x+=45
    cl=[]; x=1.0*lm
    while x<=xmax+1e-9:
        y=Ircl(x,lm)/Ish(lm,lm)
        if y<=ymaxf: cl.append((x,y))
        x+=45
    # klasik eğri üst kenarı: ilk nokta tam ymax'ta
    xs=lm*((math.exp(KK)-1)/KK/ymaxf)**0.25  # y=ymax
    cl=[(xs,ymaxf)]+[p for p in cl if p[0]>xs]
    # tutarlılık: klasik değer ymax'a eşit
    assert abs(Ircl(xs,lm)/Ish(lm,lm)-ymaxf)<1e-6
    head='\\begin{axis}[width=8cm,height=5cm,axis lines=left,clip mode=individual,xlabel={Dalga boyu},ylabel={Işıma şiddeti},xmin=0,xmax=%d,ymin=0,ymax=%.2f,xtick=\\empty,ytick=\\empty,label style={font=\\small},xlabel style={at={(ticklabel* cs:1.0)},anchor=north west},ylabel style={at={(ticklabel* cs:1.0)},anchor=south west}]\n'%(xmax,ymaxf+0.05)
    s='\\addplot[blue!65!black,very thick,dashed] coordinates {%s};\n'%' '.join('(%.1f,%.4f)'%p for p in cl)
    s+='\\addplot[vurgu,very thick] coordinates {%s};\n'%' '.join('(%.1f,%.4f)'%p for p in pl)
    s+='\\node[blue!65!black,font=\\small\\bfseries,fill=white,inner sep=1pt] at (axis cs:%.1f,1.18) {Eğri 1};\\node[above,font=\\small\\bfseries,text=black] at (axis cs:%.1f,1.0) {Eğri 2};'%(xs+420,lm)
    return tk(head+s+'\n\\end{axis}')
SK=sekil10()
onc('0010','E','Bir kara cismin ışıma şiddetinin dalga boyuna bağlı değişimi için klasik fiziğin öngördüğü eğri ile deneyde ölçülen eğri şekilde birlikte verilmiştir. Eğrilerden biri klasik fizik öngörüsüne, diğeri deney sonuçlarına aittir.',
 [('Eğri 2, klasik fiziğin öngördüğü eğridir.',False,'Klasik fizik kısa dalga boylarına gidildikçe şiddetin sınırsız artacağını öngörür; yalnız Eğri 1 böyle yükselir. Tepe yapıp azalan Eğri 2 deney sonucudur.','I numaralı yargıda sınırsız artan eğrinin deney sonucu olduğunu düşünmüş.'),
  ('Uzun dalga boylarında iki eğri birbirine yaklaşır.',True,'Klasik öngörü ile deney sonucu yalnız uzun dalga boylarında uyum gösterir; şekilde de eğriler sağa doğru birbirine yaklaşır.','II numaralı yargıda klasik fiziğin her dalga boyunda deneyle uyumlu olduğunu ya da hiç uyumlu olmadığını düşünmüş.'),
  ('Planck, Eğri 2’yi açıklamak için salınıcıların enerji alışverişinin kesikli olduğunu varsaymıştır.',True,'Planck, deneyle uyum için salınıcı enerjisinin hf’nin tam katları olduğunu, yani enerji alışverişinin kesikli olduğunu varsaymıştır; böylece kısa dalga boyunda şiddet sınırsız artmaz.','III numaralı yargıda Planck’ın klasik fizikteki sürekli enerji anlayışını koruduğunu düşünmüş.')],
 ['Eğrilerden hangisinin kısa dalga boylarında sınırsız yükseldiğini ve Planck’ın hangi varsayımı getirdiğini düşün.'],
 [B('Klasik fizik ve Planck','Klasik fizik, kısa dalga boylarında ışıma şiddetinin sonsuza gideceğini öngörür; deney ise tepe yapıp azalan bir eğri verir. Planck, enerji alışverişinin hf’nin tam katlarıyla olduğunu varsayarak deneyle uyum sağlamıştır. Örnek: frekansı arttıkça kuantum enerjisi arttığından yüksek frekanslı ışıma güçleşir')],
 'Hangi eğrinin kısa dalga boyunda sınırsız arttığını ayırt et.','Doğru olan yargılar.','kc-tarih','Klasik fiziğin yetersizliği ve Planck’ın çözümü','orta','Planck ve Klasik Fizik','Klasik fiziğin öngördüğü ve deneysel ışıma eğrilerini karşılaştırır, Planck’ın varsayımının gerekçesini değerlendirir.','K-AFKC-06 (klasik–deneysel eğri) · Planck’ın çözümü','grafik',sekil=SK)

# ---- 11 orta · iki sıcaklık, fark verilmiş ----
SK=egri_sekil([('T₁',1200),('T₂',800)],3600,[800,1200])
T1=Fr(2400); T2=T1*Fr(1200,800); assert T2-T1==1200 and T2==3600 and Fr(1200,800)==Fr(3,2)
assert Fr(3,2)*1200==1800 and T1+T2==6000 and Fr(1,2)*1200==600
q('0011',[A('Tepe dalga boylarını oku','Grafikte T₁ eğrisinin tepesi 1200 nm’de, T₂ eğrisinin tepesi 800 nm’dedir.','λ₁ = 1200 nm · λ₂ = 800 nm'),
  A('Sıcaklık oranını kur','Tepe dalga boyu ile sıcaklık ters orantılıdır; dalga boyu küçük olan T₂ daha sıcaktır.','T₂ ÷ T₁ = λ₁ ÷ λ₂ = 1200 ÷ 800 = 3 ÷ 2'),
  A('Farkı kullan','T₂, T₁’in 1,5 katı olduğundan aradaki fark T₁’in yarısıdır.','T₂ − T₁ = 0,5 × T₁ = 1200 K'),
  A('Sıcaklığı bul','Denklem çözülür.','T₁ = 2400 K')],
 tipId='kc-wien',tip='Wien yasası ve tepe dalga boyu hesabı',z='orta',alt='Wien Yasası',kaz='Aynı cismin iki sıcaklıktaki eğrilerinden oran kurup sıcaklık farkı bilgisiyle sıcaklığı bulur.',
 kart='K-AFKC-02 (iki sıcaklık, oran ve fark) · T₁’i bulma',kalip='grafik',
 metin='Bir kara cismin T₁ ve T₂ sıcaklıklarındaki ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir. T₂ sıcaklığı, T₁ sıcaklığından 1200 K büyüktür.\nBuna göre, T₁ sıcaklığı kaç K’dir?',
 dogru=2400,yan=[(6000,'T₁ ile T₂’nin toplamını (2400 + 3600) T₁ olarak vermiş.','dikkat'),(1200,'Sıcaklık farkını (1200 K) doğrudan T₁ olarak yazmış.','dikkat'),(1800,'Sıcaklık farkını tepe dalga boylarının oranıyla çarpmış: 1200 × 1,5 = 1800.','islem'),(3600,'Tepe dalga boyu büyük olan eğriyi daha sıcak alıp T₁ = 1,5·T₂ kurmuş; 0,5·T₂ = 1200 ve T₂ = 2400 bulup T₁ = 3600 yazmış.','bilgi')],
 istenen='T₁ sıcaklığı (K).',ip=['Önce iki sıcaklığın oranını tepe dalga boylarından yaz; sonra sıcaklık farkını bu oranla ilişkilendir.'],
 bilgi=[B('Wien yasasıyla oran','λ₁·T₁ = λ₂·T₂ olduğundan T₂ ÷ T₁ = λ₁ ÷ λ₂’dir. Örnek: tepe dalga boyu yarıya inen cismin sıcaklığı 2 katına çıkmıştır')],
 puf='Oranı Wien yasasından yaz, farkı oranla birlikte denkleme koy.',sekil=SK)

# ---- 12 orta · tablo öncüllü ----
Tt={'K':2000,'L':3000,'M':6000}; bW=3*10**6
lt={k:Fr(bW,v) for k,v in Tt.items()}; assert lt=={'K':1500,'L':1000,'M':500}
assert Fr(Tt['M'],Tt['K'])==3 and not (400<=lt['L']<=700) and 400<=lt['M']<=700
SK=tablo_svg(['Cisim','Sıcaklık (K)'],[[k,str(v)] for k,v in Tt.items()])
onc('0012','E','K, L ve M kara cisimlerinin sıcaklıkları tabloda verilmiştir. Görünür ışık bölgesi 400 nm ile 700 nm arasındadır.\n(Wien sabiti 3 × 10⁻³ m·K alınız.)',
 [('M cisminin en şiddetle yaydığı fotonun enerjisi, K cisminin en şiddetle yaydığı fotonun enerjisinin 3 katıdır.',True,'Tepe fotonunun enerjisi tepe dalga boyuyla ters, sıcaklıkla doğru orantılıdır; M’nin sıcaklığı K’ninkinin 6000 ÷ 2000 = 3 katıdır.','I numaralı yargıda foton enerjisinin sıcaklıkla ters orantılı olduğunu düşünmüş.'),
  ('L cisminin tepe dalga boyu görünür ışık bölgesindedir.',False,'L’nin tepe dalga boyu 3 × 10⁻³ ÷ 3000 = 10⁻⁶ m = 1000 nm’dir; bu değer 700 nm’den büyük olduğundan kızılötesi bölgededir.','II numaralı yargıda dalga boyunu hesaplarken nm–m dönüşümünü yanlış yapıp görünür bölgeye düşürmüş.'),
  ('M cisminin tepe dalga boyu görünür ışık bölgesindedir.',True,'M’nin tepe dalga boyu 3 × 10⁻³ ÷ 6000 = 5 × 10⁻⁷ m = 500 nm’dir ve 400–700 nm aralığındadır.','III numaralı yargıda sıcak cismin tepe dalga boyunun görünür bölgenin dışında kaldığını düşünmüş.')],
 ['Her cismin tepe dalga boyunu Wien yasasından nm cinsinden bul ve görünür bölgeyle karşılaştır.'],
 [B('Tepe dalga boyu ve bölgeler','Tepe dalga boyu λ = b ÷ T ile bulunur. Görünür bölge yaklaşık 400–700 nm’dir; daha uzun dalga boyları kızılötesi, daha kısa olanlar morötesi bölgededir. Örnek: tepe dalga boyu 900 nm olan cismin en şiddetli ışıması kızılötesindedir')],
 'Önce tepe dalga boyunu hesapla, sonra hangi bölgeye düştüğüne bak.','Doğru olan yargılar.','kc-renk','Tepe dalga boyu, renk ve görünür bölge','orta','Işımanın Rengi','Tabloda verilen sıcaklıklardan tepe dalga boylarını bulup görünür bölge ve foton enerjisi hakkındaki yargıları değerlendirir.','K-AFKC-04 (sıcaklık tablosu) · görünür bölge ve foton enerjisi','tablo',sekil=SK)

# ---- 13 orta · Planck varsayımı nitel, şekilsiz ----
onc('0013','E','Planck, kara cisim ışımasını açıklamak için ışıma yapan salınıcıların enerji alışverişinin kesikli olduğunu ileri sürmüştür.\n(Planck sabiti h = 6,6 × 10⁻³⁴ J·s alınız.)',
 [('Planck sabiti, ışığın frekansına göre değişmeyen bir sabittir.',True,'h evrensel bir sabittir; foton enerjisinin frekansla artması E = h·f bağıntısındaki f’nin değişmesinden gelir, h’nin değişmesinden değil.','I numaralı yargıda Planck sabitinin ışığın rengine göre değiştiğini düşünmüş.'),
  ('Salınıcılar enerji alışverişini yalnız hf’nin tam katları kadar yapabilir.',True,'Planck varsayımına göre salınıcının enerjisi n·h·f değerlerini alır; bu yüzden alınıp verilen enerji hf’nin tam katlarıdır.','II numaralı yargıda enerji alışverişinin her değerde olabileceğini düşünmüş.'),
  ('Frekansı 4 × 10¹⁴ Hz olan ışığın bir kuantumunun enerjisi 2,64 × 10⁻¹⁹ J’dir.',True,'E = h·f = 6,6 × 10⁻³⁴ × 4 × 10¹⁴ = 26,4 × 10⁻²⁰ = 2,64 × 10⁻¹⁹ J’dir.','III numaralı yargıda 10’un kuvvetlerini toplarken hata yapıp enerjiyi farklı bulmuş.')],
 ['Kuantum enerjisinin neye bağlı olduğunu ve h’nin ne tür bir nicelik olduğunu düşün.'],
 [B('Enerji kuantumu','E = h·f; h evrensel bir sabittir (yaklaşık 6,6 × 10⁻³⁴ J·s) ve kuantum enerjisi yalnız frekansa bağlıdır. Örnek: frekansı 2 katına çıkan ışığın kuantumunun enerjisi de 2 katına çıkar')],
 'Her yargıda hangi niceliğin neye bağlı olduğunu ayır.','Doğru olan yargılar.','kc-planck','Planck’ın kuantum varsayımı ve enerji düzeyleri','orta','Planck Varsayımı','Planck’ın kuantum varsayımı ve kuantum enerjisiyle ilgili yargıları değerlendirir.','K-AFKC-05 (kuantum, h sabiti, renk) · nitel öncüllü','öncüllü')

# ---- 14 orta · iki eğri, doğru yargı ----
l14=[('K',500),('L',750)]
for lam in (300,500,750,1500,2200): v=sira_cmp(l14,lam); assert v[0]>v[1]
SK=egri_sekil(l14,2250,[500,750])
dog14='K cisminin en şiddetle yaydığı fotonun enerjisi, L cisminin en şiddetle yaydığı fotonun enerjisinden büyüktür.'
s14=['K cisminin sıcaklığı, L cisminin sıcaklığından küçüktür.','L cisminin en şiddetle yaydığı fotonun frekansı, K cisminin en şiddetle yaydığı fotonun frekansından büyüktür.','L cisminin birim zamanda yaydığı toplam enerji, K cisminin birim zamanda yaydığı toplam enerjiden büyüktür.','L cisminin sıcaklığı artırılırsa en şiddetle yaydığı ışığın dalga boyu büyür.']
q('0014',[A('Tepe dalga boylarını karşılaştır','K’nin tepe dalga boyu 500 nm, L’ninki 750 nm’dir; Wien yasasına göre K daha sıcaktır.','λ_K < λ_L → T_K > T_L'),
  A('Foton enerjilerini karşılaştır','Fotonun enerjisi dalga boyuyla ters orantılıdır; K’nin tepe fotonu daha kısa dalga boyludur.','E = hc ÷ λ → E_K > E_L'),
  A('Şıkları ele','Daha sıcak K’nin toplam gücü ve tepe frekansı da daha büyüktür; sıcaklık artınca tepe dalga boyu küçülür.','A, B, C, D: yanlış · E: doğru')],
 tipId='kc-grafik',tip='Işıma şiddeti–dalga boyu grafiği yorumu',z='orta',alt='Işıma Grafikleri',kaz='İki eğrili grafikten sıcaklık, foton enerjisi ve toplam güç hakkında doğru çıkarımı belirler.',
 kart='K-AFKC-01 (iki eğri, doğru çıkarım) · foton enerjisi',kalip='grafik',
 metin='Bir laboratuvarda sıcaklıkları farklı olan K ve L kara cisimlerinin spektrumları ölçülmüş ve elde edilen eğriler şekilde gösterilmiştir.\nBuna göre, aşağıdakilerden hangisi doğrudur?',
 dogru=dog14,yan=[(s14[0],'Tepe dalga boyu küçük olan cismin daha soğuk olduğunu düşünmüş.','bilgi'),(s14[1],'Dalga boyu büyük olan ışığın frekansının da büyük olduğunu düşünmüş.','bilgi'),(s14[2],'Eğri altındaki alanın daha küçük olduğu halde, tepe dalga boyu büyük olan cismin daha çok enerji yaydığını düşünmüş.','dikkat'),(s14[3],'Sıcaklık arttıkça tepe dalga boyunun büyüdüğünü düşünmüş.','bilgi')],
 sira=s14+[dog14],
 istenen='Grafiğe göre doğru olan yargı.',ip=['Önce hangi cismin daha sıcak olduğunu bul; sonra her şıkkı sıcaklıkla ilişkilendir.'],
 bilgi=[B('Foton enerjisi ve dalga boyu','E = hc/λ olduğundan dalga boyu küçük olan fotonun enerjisi ve frekansı büyüktür. Örnek: mor ışık fotonu kırmızı ışık fotonundan daha enerjilidir')],
 puf='Önce sıcaklık sıralamasını çıkar, sonra frekans, enerji ve güç için aynı sırayı kullan.',sekil=SK)

# ---- 15 zor · enerji oranı ve sıcaklık farkı ----
l15=1240; E15=Fr(1240,l15); E15b=3; T15=Fr(4800,E15b-1); T15b=T15*E15b
assert E15==1 and T15==2400 and T15b==7200 and Fr(4800,3)==1600 and 4800*3==14400 and abs(Fr(3*10**6,l15)-T15)<80
SK=egri_sekil([('',l15)],3720,[l15],w=7.0)
q('0015',[A('İlk tepe fotonunun enerjisini bul','Grafikteki tepe dalga boyuna karşılık gelen foton enerjisi hc’nin dalga boyuna bölümüdür.','E₁ = 1240 ÷ 1240 = 1 eV'),
  A('Enerji oranını sıcaklık oranına çevir','Tepe fotonunun enerjisi sıcaklıkla doğru orantılıdır.','E₂ ÷ E₁ = 3 = T₂ ÷ T₁'),
  A('Farkı yaz','T₂ = 3·T₁ olduğundan iki sıcaklığın farkı T₁’in 2 katıdır.','T₂ − T₁ = 2 × T₁ = 4800 K'),
  A('Sıcaklığı hesapla','Denklem çözülür.','T₁ = 2400 K')],
 tipId='kc-enerji',tip='Tepe fotonunun enerjisi ve sıcaklık',z='zor',alt='Foton Enerjisi',kaz='Foton enerjisi bağıntısı ile Wien yasasını birleştirip sıcaklık farkından başlangıç sıcaklığını hesaplar.',
 kart='K-AFKC-07 (enerji oranı ve sıcaklık farkı) · iki kavram birleşimi',kalip='grafik',
 metin='Bir kara cismin ışıma şiddetinin dalga boyuna bağlı değişim grafiği şekilde verilmiştir. Cismin sıcaklığı 4800 K artırıldığında en şiddetle yaydığı fotonun enerjisi 3 eV olmaktadır.\n(hc = 1240 eV·nm alınız.)\nBuna göre, cismin başlangıçtaki sıcaklığı kaç K’dir?',
 dogru=2400,yan=[(1600,'Sıcaklık artışını enerji oranına (3) bölmüş: 4800 ÷ 3 = 1600.','islem'),(4800,'Sıcaklık artışını (4800 K) doğrudan başlangıç sıcaklığı olarak yazmış.','dikkat'),(7200,'Artıştan sonraki sıcaklığı (2400 + 4800 = 7200 K) başlangıç sıcaklığı olarak yazmış.','dikkat'),(14400,'Sıcaklık artışını enerji oranıyla çarpmış: 4800 × 3 = 14400.','islem')],
 istenen='Cismin başlangıçtaki sıcaklığı (K).',ip=['Grafikten başlangıçtaki tepe fotonunun enerjisini bul; sonra enerji ile sıcaklık arasındaki ilişkiyi kur.'],
 bilgi=[B('Foton enerjisi ve tepe dalga boyu','E = hc/λ_maks ve nm için hc = 1240 eV·nm’dir. Tepe dalga boyu sıcaklıkla ters orantılı olduğundan tepe fotonunun enerjisi sıcaklıkla aynı yönde değişir. Örnek: tepe dalga boyu 2480 nm olan cismin tepe fotonunun enerjisi 0,5 eV’tur')],
 puf='Enerji ile sıcaklık arasındaki orantıyı kurup farkı denkleme koy.',sekil=SK)

# ---- 16 zor · soğurma + yayma, dalga boyları ----
lk=600; lL16=Fr(lk)*Fr(3,2)
assert lL16==900 and Fr(lk)*Fr(2,3)==400 and Fr(lk)*Fr(4,2)==1200 and Fr(lk)*Fr(1,4)==150
SK=merdiven(4,[(1,4,'K'),(4,2,'L')])
q('0016',[A('K geçişinin enerji farkını bul','Salınıcı 1hf düzeyinden 4hf düzeyine çıkarken bu farkı soğurur.','E_K = 4hf − hf = 3hf'),
  A('L geçişinin enerji farkını bul','4hf düzeyinden 2hf düzeyine inerken bu farkı yayar.','E_L = 4hf − 2hf = 2hf'),
  A('Dalga boyu ilişkisini kur','Dalga boyu foton enerjisiyle ters orantılıdır.','λ_L ÷ λ_K = E_K ÷ E_L = 3 ÷ 2'),
  A('Dalga boyunu hesapla','Değerler yerine konur.','λ_L = 600 × 3 ÷ 2 = 900 nm')],
 tipId='kc-planck',tip='Planck’ın kuantum varsayımı ve enerji düzeyleri',z='zor',alt='Planck Varsayımı',kaz='Salınıcının enerji düzeyleri arasındaki soğurma ve yayma geçişlerinde fotonların dalga boylarını karşılaştırır.',
 kart='K-AFKC-05 (soğurma ve yayma geçişi, dalga boyu oranı) · iki geçiş',kalip='şekilli',
 metin='Frekansı f olan bir salınıcının enerji düzeyleri şekilde verilmiştir. Salınıcı K geçişini yaparken bir foton soğurmakta, L geçişini yaparken bir foton yaymaktadır. K geçişinde soğurulan fotonun boşluktaki dalga boyu 600 nm’dir.\nBuna göre, L geçişinde yayılan fotonun boşluktaki dalga boyu kaç nm’dir?',
 dogru=900,yan=[(150,'Geçişlerin başlangıç düzeylerinin enerjilerini (hf ve 4hf) foton enerjisi sanıp 600 × 1 ÷ 4 = 150 bulmuş.','dikkat'),(400,'Dalga boyunu enerjiyle doğru orantılı alıp 600 × 2 ÷ 3 = 400 bulmuş.','bilgi'),(600,'İki geçişte de enerji farkını hf alıp iki fotonun dalga boyunu eşit bulmuş.','bilgi'),(1200,'Geçişlerin bitiş düzeylerinin enerjilerini (4hf ve 2hf) foton enerjisi sanıp 600 × 4 ÷ 2 = 1200 bulmuş.','dikkat')],
 istenen='L geçişinde yayılan fotonun dalga boyu (nm).',ip=['Her geçişte soğurulan ya da yayılan fotonun enerjisini iki düzeyin farkından bul.'],
 bilgi=[B('Foton enerjisi ve dalga boyu','Boşlukta E = hc/λ olduğundan foton enerjisi k kat büyükse dalga boyu k kat küçüktür. Salınıcıda yayılan ya da soğurulan fotonun enerjisi, düzeylerin enerji farkına eşittir. Örnek: 6hf ile 5hf düzeyleri arasındaki geçişte foton enerjisi hf’dir')],
 puf='Foton enerjisi iki düzeyin farkıdır; dalga boyu enerjiyle ters orantılıdır.',sekil=SK)

# ---- 17 zor · sıcaklık farkı, Wien ve foton enerjisi ----
lL17=2000; TL17=Fr(3*10**6,lL17); TK17=TL17+1500; lK17=Fr(3*10**6)/TK17; EK17=Fr(12400)/(lK17*10)
assert TL17==1500 and TK17==3000 and lK17==1000 and EK17==Fr(124,100)
assert Fr(12400,1000)==Fr(124,10) and Fr(12400,1000*100)==Fr(124,1000) and Fr(12400,20000)==Fr(62,100)
assert Fr(12400,(lL17-1500)*10)==Fr(248,100) and Fr(12400,Fr(lL17*3000,1500)*10)==Fr(31,100)
SK=egri_sekil([('L',lL17)],6000,[lL17],w=7.0)
q('0017',[A('L’nin sıcaklığını bul','Wien yasasından sıcaklık, Wien sabitinin tepe dalga boyuna bölümüdür; dalga boyu metreye çevrilir.','T_L = 3 × 10⁻³ ÷ (2000 × 10⁻⁹) = 1500 K'),
  A('K’nin sıcaklığını bul','K cismi L’den 1500 K daha sıcaktır.','T_K = 1500 + 1500 = 3000 K'),
  A('K’nin tepe dalga boyunu yaz','Wien yasası yeniden uygulanır ve Å’e çevrilir.','λ_K = 3 × 10⁻³ ÷ 3000 = 10⁻⁶ m = 10000 Å'),
  A('Tepe fotonunun enerjisini hesapla','Foton enerjisi hc’nin dalga boyuna bölümüdür.','E_K = 12400 ÷ 10000 = 1,24 eV')],
 tipId='kc-wien',tip='Wien yasası ve tepe dalga boyu hesabı',z='zor',alt='Wien Yasası',kaz='Wien yasasını art arda uygulayıp sıcaklık farkından tepe dalga boyunu ve tepe fotonunun enerjisini hesaplar.',
 kart='K-AFKC-02 (iki cisim, sıcaklık farkı) · Wien ve foton enerjisi',kalip='grafik',
 metin='L kara cisminin ışıma şiddetinin dalga boyuna bağlı değişim grafiği şekilde verilmiştir. K kara cisminin sıcaklığı, L cisminin sıcaklığından 1500 K büyüktür.\n(Wien sabiti 3 × 10⁻³ m·K, hc = 12400 eV·Å alınız.)\nBuna göre, K cisminin en şiddetle yaydığı fotonun enerjisi kaç eV’tur?',
 dogru=EK17,yan=[(Fr(31,100),'Dalga boyunu sıcaklıkla doğru orantılı alıp λ_K = 2000 × 3000 ÷ 1500 = 4000 nm = 40000 Å bulmuş: 12400 ÷ 40000 = 0,31.','bilgi'),(Fr(62,100),'Tepe dalga boyunun sıcaklıkla değişmediğini düşünüp 2000 nm = 20000 Å için 12400 ÷ 20000 = 0,62 bulmuş.','bilgi'),(Fr(248,100),'Sıcaklık farkını (1500 K) dalga boyu farkı sanıp 2000 − 1500 = 500 nm = 5000 Å için 12400 ÷ 5000 = 2,48 bulmuş.','dikkat'),(Fr(124,10),'Hesapladığı 1000 nm’yi Å’e çevirmeden 1000 Å alıp 12400 ÷ 1000 = 12,4 bulmuş.','dikkat')],
 istenen='K cisminin en şiddetle yaydığı fotonun enerjisi (eV).',ip=['Önce L’nin sıcaklığını bulmak, sonra K’nin tepe dalga boyuna ve fotonunun enerjisine geçmek gerekir; birimlere dikkat et.'],
 bilgi=[B('Sıcaklıktan tepe fotonuna','Wien yasasında λ_maks = b ÷ T’dir; bulunan dalga boyu Å’e çevrilip E = hc/λ ile fotonun enerjisine geçilir. Örnek: tepe dalga boyu 2 × 10⁻⁶ m olan cismin sıcaklığı 1500 K’dir')],
 puf='Sıcaklığı bul, tepe dalga boyuna geç, sonra enerjiyi hesapla.',sekil=SK)

# ---- 18 orta · K ve L, öncüllü (Yalnız III) ----
l18=[('K',600),('L',900)]
for lam in (300,600,900,1800,2500): v=sira_cmp(l18,lam); assert v[0]>v[1]
SK=egri_sekil(l18,2700,[600,900])
onc('0018','A','K ve L kara cisimlerinin ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir.',
 [('L cisminin sıcaklığı, K cisminin sıcaklığının 1,5 katıdır.',False,'Tepe dalga boyu ile sıcaklık ters orantılıdır; K’nin tepe dalga boyu daha küçük olduğundan sıcaklığı L’ninkinin 900 ÷ 600 = 1,5 katıdır; L daha soğuktur.','I numaralı yargıda dalga boyu büyük olan cismin sıcaklığını 1,5 kat büyük sanmış.'),
  ('K cisminin sıcaklığı artırılırsa en şiddetle yaydığı ışığın dalga boyu 600 nm’den büyük olur.',False,'Sıcaklık artınca eğrinin tepesi daha kısa dalga boyuna kayar; K’nin tepe dalga boyu 600 nm’den küçük olur.','II numaralı yargıda sıcaklık arttıkça tepe dalga boyunun büyüdüğünü düşünmüş.'),
  ('K cisminin en şiddetle yaydığı fotonun enerjisi, L cisminin en şiddetle yaydığı fotonun enerjisinin 1,5 katıdır.',True,'Foton enerjisi dalga boyuyla ters orantılıdır; E_K ÷ E_L = λ_L ÷ λ_K = 900 ÷ 600 = 1,5.','III numaralı yargıda enerji oranını dalga boyu oranıyla doğru orantılı kurup yanlış değerlendirmiş.')],
 ['Sıcaklık, tepe dalga boyu ve foton enerjisi arasındaki ilişkileri ayrı ayrı kur.'],
 [B('Oran kurma','İki cismin tepe dalga boyları oranı, sıcaklıkların ve tepe fotonu enerjilerinin ters oranına eşittir. Örnek: tepe dalga boyu yarı olan cismin tepe fotonu 2 kat enerjilidir')],
 'Oranları her zaman tepe dalga boylarının tersiyle kur.','Doğru olan yargılar.','kc-sicaklik','Sıcaklık değişiminin ışımaya etkisi','orta','Sıcaklığın Etkisi','İki cismin ışıma eğrilerinden sıcaklık oranı, tepe dalga boyunun sıcaklıkla değişimi ve foton enerjisi oranı hakkındaki yargıları değerlendirir.','K-AFKC-03 (iki eğri, oran ve değişim) · öncüllü','grafik',sekil=SK)

# ---- 19 zor · üç eğri, öncüllü (II ve III), nicel yargılar ----
l19=[('K',800),('L',1000),('M',1200)]
for lam in (300,800,1000,1200,2000): v=sira_cmp(l19,lam); assert v[0]>v[1]>v[2]
assert Fr(3*10**6,1200)==2500 and Fr(1200,800)==Fr(3,2) and Fr(1240,1000)==Fr(124,100) and Fr(3,1000)/Fr(12,10**8)==25000
SK=egri_sekil(l19,1600,[800,1000,1200])
onc('0019','D','K, L ve M kara cisimlerinin ışıma şiddetinin dalga boyuna bağlı değişim grafikleri şekilde verilmiştir.\n(Wien sabiti 3 × 10⁻³ m·K, hc = 1240 eV·nm alınız.)',
 [('M cisminin sıcaklığı 25000 K’dir.',False,'M’nin tepe dalga boyu 1200 nm = 1,2 × 10⁻⁶ m’dir; T = 3 × 10⁻³ ÷ (1,2 × 10⁻⁶) = 2500 K bulunur, 25000 K değil.','I numaralı yargıda 1200 nm’yi 1,2 × 10⁻⁷ m alarak sıcaklığı 25000 K bulmuş.'),
  ('K cisminin en şiddetle yaydığı fotonun enerjisi, M cisminin en şiddetle yaydığı fotonun enerjisinin 1,5 katıdır.',True,'Foton enerjisi dalga boyuyla ters orantılıdır; E_K ÷ E_M = λ_M ÷ λ_K = 1200 ÷ 800 = 1,5.','II numaralı yargıda enerji oranını dalga boyu oranıyla doğru orantılı kurup 2/3 bulmuş.'),
  ('L cisminin en şiddetle yaydığı fotonun enerjisi 1,24 eV’tur.',True,'L’nin tepe dalga boyu 1000 nm’dir; E = hc ÷ λ = 1240 ÷ 1000 = 1,24 eV bulunur.','III numaralı yargıda enerjiyi hc ile dalga boyunun çarpımına bölerek ya da birimi karıştırarak farklı bir değer bulmuş.')],
 ['Her yargıdaki niceliği, grafikteki tepe dalga boyundan Wien yasası ya da foton enerjisi bağıntısıyla ayrı ayrı hesapla.'],
 [B('Tepe dalga boyundan nicelikler','Tepe dalga boyundan sıcaklık T = b ÷ λ_maks, foton enerjisi E = hc ÷ λ_maks ile bulunur; nm–m dönüşümüne dikkat edilir. Örnek: tepe dalga boyu 2000 nm olan cismin tepe fotonunun enerjisi 1240 ÷ 2000 = 0,62 eV’tur')],
 'Her yargıyı grafikten okuduğun tepe dalga boyuyla ayrı ayrı hesapla.','Doğru olan yargılar.','kc-sicaklik','Sıcaklık değişiminin ışımaya etkisi','zor','Sıcaklığın Etkisi','Üç eğrili grafikte tepe dalga boylarından sıcaklık ve foton enerjisi hesaplayarak nicel yargıları değerlendirir.','K-AFKC-03 (üç eğri, nicel yargılar) · öncüllü','grafik',sekil=SK)

# ---- 20 zor · foton enerjisinden sıcaklık oranı ----
l20=Fr(5,10**7); TG=Fr(3,1000)/l20; E20=Fr(124,100); lY=Fr(1240)/E20
assert TG==6000 and lY==1000 and Fr(500)/lY==Fr(1,2) and Fr(lY,500)==2 and Fr(500,lY)**2==Fr(1,4) and Fr(lY,500)**2==4
SK=egri_sekil([('Güneş',500)],1500,[500],w=7.0)
q('0020',[A('Yıldızın tepe dalga boyunu bul','Fotonun enerjisi ve hc bilindiğinden dalga boyu hc’nin enerjiye bölümüyle bulunur.','λ_Y = 1240 ÷ 1,24 = 1000 nm'),
  A('Güneş’in tepe dalga boyunu oku','Grafikte tepe noktasının altındaki değer 500 nm’dir.','λ_G = 500 nm'),
  A('Wien yasasını uygula','Sıcaklık tepe dalga boyuyla ters orantılıdır.','T_Y ÷ T_G = λ_G ÷ λ_Y'),
  A('Oranı hesapla','Değerler yerine konur.','T_Y ÷ T_G = 500 ÷ 1000 = 1/2')],
 tipId='kc-enerji',tip='Tepe fotonunun enerjisi ve sıcaklık',z='zor',alt='Foton Enerjisi',kaz='Tepe fotonunun enerjisinden tepe dalga boyunu bulup Wien yasasıyla sıcaklık oranını hesaplar.',
 kart='K-AFKC-07 (enerjiden dalga boyu, sıcaklık oranı) · iki kavram birleşimi',kalip='grafik',
 metin='Güneş’in yaydığı ışımanın şiddetinin dalga boyuna bağlı değişim grafiği şekilde verilmiştir. Güneş’i kara cisim kabul eden bir araştırmacı, başka bir yıldızın en şiddetle yaydığı fotonun enerjisini 1,24 eV olarak belirlemiştir.\n(hc = 1240 eV·nm alınız.)\nBuna göre, bu yıldızın yüzey sıcaklığının Güneş’in yüzey sıcaklığına oranı kaçtır?',
 dogru='1/2',yan=[('1/4','Oranın karesini alarak (500 ÷ 1000)² = 1/4 bulmuş.','islem'),('1','Tepe fotonunun enerjisinin sıcaklıktan bağımsız olduğunu düşünüp iki yıldızı aynı sıcaklıkta kabul etmiş.','bilgi'),('2','Oranı ters kurmuş: λ_Y ÷ λ_G = 1000 ÷ 500 = 2.','bilgi'),('4','Oranı ters kurup karesini almış: (1000 ÷ 500)² = 4.','islem')],
 sira=['1/4','1/2','1','2','4'],
 istenen='Yıldızın sıcaklığının Güneş’in sıcaklığına oranı.',ip=['Önce yıldızın tepe dalga boyunu bul, sonra sıcaklık ile tepe dalga boyu arasındaki ilişkiyi kullan.'],
 bilgi=[B('Enerjiden dalga boyuna','E = hc/λ bağıntısından λ = hc/E bulunur; nm için hc = 1240 eV·nm’dir. Örnek: enerjisi 2,48 eV olan fotonun dalga boyu 500 nm’dir')],
 puf='Önce enerjiyi dalga boyuna çevir, sonra Wien yasasıyla oranla.',sekil=SK)

# ---------- yaz ----------
for x in P.ANA: x['kardes']=None
SC=os.environ.get('SCRATCH','/tmp/claude-0/-home-claude-zekacademy-app/cf3686d6-69fb-532a-907b-5b8d50f6cef4/scratchpad/kc')
os.makedirs(SC,exist_ok=True)
P.yaz(os.path.join(GD,'karacisim-1.json'),os.path.join(SC,'bos-karacisim.json'))
tipler={}
for c in H.KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Fizik, MEB 12. sınıf kuantum fiziğine giriş (kara cisim ışıması).',kartlar=H.KARTLAR,tipler=list(tipler.values())),open(os.path.join(HV,'kartlar','afkaracisim.json'),'w'),ensure_ascii=False,indent=1)
print('tipler',len(tipler))
