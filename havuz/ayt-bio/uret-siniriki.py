"""AYT Biyoloji · Sinir Sistemi · 2. dalga (10 soru). Kardeş yok, ipucu 1.
Zar iyon hareketleri, ilaç grafikleri, refleks süreleri, elektrot kaydı, derişim grafiği ve sinaps kayıtları Python'da tek yerde tanımlanır, assert edilir."""
import sys,os,math,json
GD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(GD,'..')
sys.path.insert(0,os.path.join(HV,'tyt-bio')); sys.path.insert(0,HV)
import _hafif_bio as H
from _hafif_bio import *
KONU_AD='Sinir Sistemi'; KEY='abio|Sinir Sistemi'
P=Parti('siniriki',KONU_AD,KEY,ders='AYT Biyoloji',idon='aytbio'); H.KONU=KONU_AD
KY='ÖSYM AYT 2018–2026 Biyoloji sinir sistemi soruları (yalnız mantık) · MEB 11. sınıf Denetleyici ve Düzenleyici Sistemler'
TIP={'iyon':('sn2-iyon','Zar iyon dengesi ve pompa'),'ap':('sn2-ap','Aksiyon potansiyeli ve iletim'),'sinaps':('sn2-sinaps','Sinaps, nörotransmitter ve ilaç'),
     'yol':('sn2-yol','Sinir yolu ve süre hesabı'),'kosul':('sn2-kosul','Refleks, otonom sistem ve öğrenme')}
def Q(no,tp,z,kalip,alt,kaz,fikir,tuzak,ozet,ad,**k):
    t,tn=TIP[tp]; kart(f'K-ABSNR2-{no[-2:]}',alt,fikir,tuzak,z,kalip,len(ad),t,tn,KY)
    assert len(k['ip'])==1
    mk(P,no,ad=ad,adim=len(ad),tipId=t,tip=tn,z=z,alt=alt,kaz=kaz,kalip=kalip,kart=f'K-ABSNR2-{no[-2:]} ({ozet})',**k)
def tk(body,scale=1.0): return tikz_svg('\\begin{tikzpicture}[line cap=round,line join=round,font=\\small,scale=%s]\n%s\n\\end{tikzpicture}'%(scale,body))
OKS='-{Stealth[length=2.3mm,width=1.9mm]}'
KOMB=[('I',),('II',),('III',),('I','II'),('I','III'),('II','III'),('I','II','III')]
def adk(c): return ('Yalnız '+c[0]) if len(c)==1 else (' ve '.join(c) if len(c)==2 else ', '.join(c[:-1])+' ve '+c[-1])
def onc(d,h,hedef=True):
    T=tuple(k for k in ('I','II','III') if d[k][0]==hedef); i=KOMB.index(T); bas=i-h; assert 0<=bas<=2,('uygun degil',T,h)
    ops=KOMB[bas:bas+5]; assert ops[h]==T and len(ops)==5
    yan=[]
    for o in ops:
        if o==T: continue
        p=[]
        for x in o:
            if x not in T: p.append(f'{x} öncülünü '+('doğru' if hedef else 'yanlış')+f' sanmış; oysa '+('yanlıştır' if hedef else 'doğrudur')+f': {d[x][1]}')
        for x in T:
            if x not in o: p.append(f'{x} öncülünü '+('yanlış' if hedef else 'doğru')+f' sanmış; oysa '+('doğrudur' if hedef else 'yanlıştır')+f': {d[x][1]}')
        yan.append((adk(o),'. '.join(p)+'.','bilgi'))
    return dict(dogru=adk(T),yan=yan,sira=[adk(o) for o in ops])
def tek(dogru,yanlislar,h,hedef=True):
    assert len(yanlislar)==4
    sira=[m for m,_ in yanlislar]; sira.insert(h,dogru[0])
    yan=[(m,(f'Bu ifadeyi doğru sanmış; oysa yanlıştır: {n}.' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}.'),'bilgi') for m,n in yanlislar]
    return dict(dogru=dogru[0],yan=yan,sira=sira)
def pgf(pts): return ' '.join(f'({x:.2f},{y:.1f})' for x,y in pts)
def ap(t,tp,s=1.0):
    u=t-(tp-s)
    if u<=0: return -70.0
    if u<=s: return -70+105*(1-math.cos(math.pi*u/s))/2
    if u<=2*s: return 35-105*(1-math.cos(math.pi*(u-s)/s))/2
    if u<=3.6*s: return -70-10*math.sin(math.pi*(u-2*s)/(1.6*s))
    return -70.0
NA='$\\mathrm{Na^+}$'; KK='$\\mathrm{K^+}$'

# ======================= 01 · Zar iyon hareketleri (kolay, şekilli) =======================
ZAR=[('Na','iç'),('K','dış'),('Na','dış'),('Na','iç'),('K','dış')]   # I..V: iyon, hedef taraf
DERISIM={'Na':'dışarıda fazla','K':'içeride fazla'}
def karsi(ion,hedef): return (ion=='Na' and hedef=='dış') or (ion=='K' and hedef=='iç')
assert [i+1 for i,(a,b) in enumerate(ZAR) if karsi(a,b)]==[3]
def f_zar():
    b=['\\fill[black,fill opacity=.10] (0,2.0) rectangle (9.6,2.5);\\draw[line width=1.2pt] (0,2.0)--(9.6,2.0) (0,2.5)--(9.6,2.5);']
    xs=[1.2,3.0,4.8,6.6,8.4]
    for k,(x,(ion,h)) in enumerate(zip(xs,ZAR)):
        b.append(f'\\draw[line width=1pt,fill=white] ({x-.38},1.88) rectangle ({x+.38},2.62);')
        y1,y2=(3.7,1.05) if h=='iç' else (1.05,3.7)
        b.append(f'\\draw[{OKS},line width=1.4pt,color=vurgu] ({x},{y1})--({x},{y2});')
        sy=3.3 if h=='iç' else 1.35
        b.append(f'\\node[font=\\normalsize\\bfseries,anchor=west,fill=white,inner sep=1pt] at ({x+.1},{sy}) {{{NA if ion=="Na" else KK}}};')
        b.append(f'\\node[font=\\normalsize\\bfseries] at ({x},4.15) {{{"I II III IV V".split()[k]}}};')
    b.append('\\node[font=\\small,anchor=east,align=right] at (-.3,3.2) {Hücre dışı\\\\[-1pt]'+NA+' çok, '+KK+' az};')
    b.append('\\node[font=\\small,anchor=east,align=right] at (-.3,1.3) {Hücre içi\\\\[-1pt]'+NA+' az, '+KK+' çok};')
    return tk('\n'.join(b),.62)
SK1=f_zar()
Q('0001','iyon','kolay','şekilli','Dinlenme hâlinde iyon hareketleri','Zar iki yanındaki derişim farkına göre ATP gerektiren iyon hareketini belirler.','Derişimi az olan tarafa geçiş ATP istemez; derişimi çok olan tarafa geçiş için ATP gerekir.','Derişim farkına karşı taşımayı difüzyon sanmak; yalnız kanallı geçişi ATP gerektiren hareket saymak.','derişim farkına karşı taşıma',
 [A('Derişimleri oku','Şekilde Na⁺ hücre dışında, K⁺ hücre içinde daha çoktur.','Na⁺: dışarıda fazla · K⁺: içeride fazla'),
  A('Yönü derişimle karşılaştır','Her okta iyonun derişimi fazla olan taraftan mı, az olan tarafa mı gittiğine bakılır.','Fazladan aza: ATP yok · azdan fazlaya: ATP var'),
  A('Hareketleri ele','Na⁺ dışarıdan içeri ve K⁺ içeriden dışarı geçişleri derişim farkı yönündedir; yalnız bir hareket farka karşıdır.','Farka karşı: Na⁺ içeriden dışarı'),
  A('Numarayı bul','Na⁺ içeriden dışarı hareketi III numaralı oktur.','III numaralı hareket')],
 metin='Şekilde dinlenme hâlindeki bir nöronun akson zarında gerçekleşen iyon hareketleri oklarla gösterilmiş ve I, II, III, IV ve V ile numaralandırılmıştır. Zarın iki yanındaki Na⁺ ve K⁺ derişimleri de şekilde belirtilmiştir.\nBuna göre, numaralı hareketlerden hangisinin gerçekleşmesi için doğrudan ATP gerekir?',
 sekil=SK1,sira=['I','II','III','IV','V'],dogru='III',
 yan=[('I','I numaralı harekette Na⁺ derişimi fazla olan dış ortamdan az olan hücre içine geçer; bu geçiş farka uygun olduğundan ATP gerekmez.','bilgi'),
      ('II','II numaralı harekette K⁺ derişimi fazla olan hücre içinden dışarı geçer; geçiş derişim farkı yönündedir ve ATP gerekmez.','bilgi'),
      ('IV','IV numaralı harekette Na⁺ yine derişimi fazla olan dış ortamdan içeri geçer; bu geçiş farka uygundur ve ATP gerekmez.','bilgi'),
      ('V','V numaralı harekette K⁺ derişimi fazla olan içeriden dışarı geçer; ATP harcanmadan gerçekleşen bir geçiştir.','bilgi')],
 istenen='Doğrudan ATP gerektiren iyon hareketi',ip=['Her okta iyonun derişimi fazla olan tarafa mı, az olan tarafa mı gittiğine bak.'],
 bilgi=[B('Madde geçişinde enerji','derişimi fazla ortamdan az ortama geçiş enerji gerektirmez · Derişimi az ortamdan fazla ortama taşıma ise enerji ister')],puf='Derişim farkına karşı taşıma ATP ister.')

# ======================= 02 · Nörotransmitter (kolay, düz, olumsuz) =======================
Q('0002','sinaps','kolay','düz','Nörotransmitterler','Nörotransmitterlerin salınımı ve etkisiyle ilgili yanlış ifadeyi belirler.','Nörotransmitter akson ucundaki veziküllerden salınır ve hedef hücre reseptörüne bağlanır.','Salınımın dendrit ucundan olduğunu sanmak.','nörotransmitter özellikleri',
 [A('İfadeleri sırala','Her ifade, nörotransmitterin depolanması, salınımı ve etkisi bakımından kontrol edilir.','Depolama · salınım · etki'),
  A('Bölgeleri karşılaştır','Her ifadede söylenen yapının sinapstaki görevi, nöronun uzantılarının işleviyle karşılaştırılır.','Uzantı işlevi ↔ ifade'),
  A('Yanlışı bul','Dendrit uzantıları uyarıyı alır, nörotransmitter salmaz.','Yanlış: dendrit uçlarından salınır')],
 metin='İki nöron arasındaki iletim, bir nörondan salınan kimyasal maddelerin diğer nörona etki etmesiyle sağlanır.\nNörotransmitterlerle ilgili aşağıdaki ifadelerden hangisi yanlıştır?',
 **tek(('Sinaptik aralığa yalnız dendrit uçlarından salınırlar.','nörotransmitterler akson ucundaki veziküllerden salınır, dendrit uçlarından değil'),
       [('Akson ucundaki keseciklerde depolanırlar.','nörotransmitterler akson ucundaki veziküllerde depolanır'),
        ('Salınımları kesecik zarının hücre zarıyla birleşmesiyle gerçekleşir.','salınım ekzositozla, kesecik zarının hücre zarıyla kaynaşmasıyla olur'),
        ('Karşı nörondaki reseptörlere bağlanarak etki gösterirler.','etki, karşı nöron zarındaki özgül reseptörlere bağlanmayla başlar'),
        ('Etkilerini tamamladıktan sonra yıkılabilir ya da geri alınabilirler.','sinaptik aralıktaki nörotransmitter enzimlerle yıkılabilir veya akson ucuna geri alınabilir')],0,hedef=False),
 istenen='Nörotransmitterle ilgili yanlış ifade',ip=['Nörotransmitterin hangi uzantıdan salındığını ve hangi yapıya bağlandığını düşün.'],
 bilgi=[B('Sinaps','sinaps; iki nöron arasındaki bağlantı bölgesidir · Kimyasal sinapsta iletim, nörotransmitter denen maddelerle sağlanır')],puf='Her ifadenin sinapsta hangi nöron bölgesini anlattığını ayrı ayrı sına.')

def gr(govde): return tikz_svg('\\begin{tikzpicture}[font=\\small]\n'+govde+'\n\\end{tikzpicture}')
def onctxt(giris,ifd,kok): return giris+'\n'+'\n'.join(f'{r}. {t}' for r,t in ifd.items())+'\n'+kok
GOV='tick label style={font=\\footnotesize},label style={font=\\small},every axis plot/.append style={line width=1.5pt}'
# ======================= 03 · Dış ortam Na+ derişimi (orta, grafik, öncüllü, B) =======================
def apq(t,tp,peak,s=1.0):
    u=t-(tp-s); h=peak+70
    if u<=0: return -70.0
    if u<=s: return -70+h*(1-math.cos(math.pi*u/s))/2
    if u<=2*s: return peak-h*(1-math.cos(math.pi*(u-s)/s))/2
    if u<=3.6*s: return -70-10*math.sin(math.pi*(u-2*s)/(1.6*s))
    return -70.0
PX,PY=35,10
tt=[i/20 for i in range(0,141)]
assert abs(max(apq(t,2.5,PX) for t in tt)-PX)<.5 and abs(max(apq(t,2.5,PY) for t in tt)-PY)<.5
assert apq(0,2.5,PX)==apq(0,2.5,PY)==-70 and apq(6.9,2.5,PX)==apq(6.9,2.5,PY)==-70
b=['\\begin{axis}[width=8.4cm,height=5.4cm,xmin=0,xmax=7,ymin=-90,ymax=50,xtick={0,1,2,3,4,5,6,7},ytick={-70,-40,-20,0,20,40},axis lines=left,xlabel={Zaman (ms)},ylabel={Zar potansiyeli (mV)},ymajorgrids=true,grid style={gray!30},'+GOV+']',
   f'\\addplot[black] coordinates {{{pgf([(t,apq(t,2.5,PX)) for t in tt])}}};',f'\\addplot[vurgu!80!black] coordinates {{{pgf([(t,apq(t,2.5,PY)) for t in tt])}}};',
   '\\node[font=\\small\\bfseries] at (axis cs:3.55,38) {X};\\node[font=\\small\\bfseries,vurgu!80!black] at (axis cs:3.55,13) {Y};','\\end{axis}']
SK3=gr('\n'.join(b))
ST3={'I':(False,'Dinlenme potansiyeli iki ortamda da −70 mV’tur; grafikte uyarı öncesindeki düzey aynıdır'),
     'II':(True,'Y ortamında tepe değeri daha düşüktür; depolarizasyonda hücre içine giren Na⁺ miktarı azalmıştır'),
     'III':(False,'Y eğrisi de uyarıdan sonra −70 mV’a dönmüştür; repolarizasyon bu ortamda da gerçekleşmiştir')}
I3=onc(ST3,1,True)
Q('0003','ap','orta','grafik','Aksiyon potansiyeli ve dış ortam Na⁺ derişimi','Dış ortam Na⁺ derişiminin aksiyon potansiyeli evrelerine etkisini grafikten yorumlar.','Depolarizasyon hücre dışından içeri Na⁺ girişiyle olur; dış ortamda Na⁺ azalırsa giren miktar ve tepe değeri azalır, repolarizasyon ise K⁺ çıkışıyla sürer.','Dış ortamdaki Na⁺ azlığının dinlenme potansiyelini ya da repolarizasyonu da ortadan kaldırdığını sanmak.','dış ortam Na⁺ derişimi grafiği',
 [A('Eğrileri karşılaştır','Uyarıdan önce iki eğri aynı düzeyde başlar, tepe değerleri farklıdır ve ikisi de uyarıdan sonra başlangıç düzeyine döner.','Başlangıç: aynı · tepe: farklı · dönüş: var'),
  A('Depolarizasyonu yorumla','Depolarizasyon Na⁺ girişiyle oluşur; tepe değeri düşük olan ortamda giren Na⁺ da azdır.','Düşük tepe: az Na⁺ girişi'),
  A('Öncülleri değerlendir','Her öncül, grafikteki başlangıç düzeyi, tepe değeri ve dönüş ile ayrı ayrı karşılaştırılır.','Doğru öncül belirlendi')],
 metin=onctxt('Bir akson, hücre dışı sıvısındaki Na⁺ derişimi normal olan ortamda (X) ve bu derişimi azaltılmış ortamda (Y) tutularak her seferinde eşik değerin üzerinde bir uyarıyla uyarılmıştır. İki ortamda kaydedilen zar potansiyeli değişimleri grafikte verilmiştir.\nBu grafiğe göre,',
   {'I':'Dış ortamdaki Na⁺ derişiminin azalması, aksonun dinlenme potansiyelini belirgin biçimde değiştirmiştir.','II':'Y ortamında depolarizasyon sırasında hücre içine giren Na⁺ miktarı X ortamındakinden azdır.','III':'Y ortamında repolarizasyon gerçekleşmediğinden zar potansiyeli dinlenme düzeyine dönmemiştir.'},'yargılarından hangileri doğrudur?'),
 sekil=SK3,dogru=I3['dogru'],yan=I3['yan'],sira=I3['sira'],istenen='Doğru olan yargıların belirlenmesi',ip=['Uyarıdan önceki düzeye, tepe değerine ve uyarıdan sonraki düzeye iki eğride ayrı ayrı bak.'],
 bilgi=[B('Aksiyon potansiyeli','depolarizasyonda Na⁺ kanalları açılır ve Na⁺ hücre içine girer · repolarizasyonda K⁺ kanalları açılır ve K⁺ hücre dışına çıkar')],puf='Her eğride başlangıç, tepe ve dönüş düzeyini ayrı karşılaştır.')

# ======================= 04 · İlaç etkisi, akson (orta, tablo, öncüllü, E) =======================
KT={'Kontrol':(-70,35,2),'X':(-70,-58,None),'Y':(-70,35,6)}
assert KT['Y'][1]==KT['Kontrol'][1] and KT['Y'][2]>KT['Kontrol'][2] and KT['X'][1]<KT['Kontrol'][1]
SK4=tablo_svg(['Ortam','Dinlenme (mV)','Tepe değeri (mV)','Dönüş süresi (ms)'],[[k,fm(v[0]),('+'+fm(v[1]) if v[1]>0 else fm(v[1])),('Yok' if v[2] is None else str(v[2]))] for k,v in KT.items()])
ST4={'I':(True,'X’te tepe değeri −58 mV’ta kaldığından depolarizasyon olmamıştır, yani Na⁺ kanalları etkilenmiştir; Y’de tepe değeri kontrolle aynıdır ve yalnız dönüş uzamıştır, yani K⁺ kanalları etkilenmiştir'),
     'II':(False,'Y’de tepe değeri kontroldeki gibi +35 mV’tur; depolarizasyon bu aksonda da gerçekleşmiştir'),
     'III':(True,'Repolarizasyon K⁺ çıkışıyla olur; Y’de K⁺ kanalları açılamadığından dönüş süresi 2 ms’den 6 ms’ye uzamıştır')}
I4=onc(ST4,4,True)
Q('0004','ap','orta','tablo','Akson zarında ilaç etkisi','Tablo verilerinden iyon kanalı engelinin aksiyon potansiyeli evrelerine etkisini çıkarır.','Na⁺ kanalı engellenirse depolarizasyon olmaz; K⁺ kanalı engellenirse tepe değeri korunur ama repolarizasyon uzar.','Tepe değeri kontrolle aynı olan aksonda da depolarizasyonun bozulduğunu sanmak.','iyon kanalı engeli tablosu',
 [A('Kontrolü oku','Kontrol aksonunda uyarı sonrası tepe değeri +35 mV’a çıkar ve dönüş 2 ms sürer.','Kontrol: +35 mV · 2 ms'),
  A('X ve Y’yi karşılaştır','X’te tepe değeri düşük kalmış, Y’de tepe aynı kalmış ancak dönüş uzamıştır.','X: depolarizasyon bozuk · Y: repolarizasyon bozuk'),
  A('Kanalları eşleştir','Depolarizasyondan Na⁺ kanalları, repolarizasyondan K⁺ kanalları sorumludur; bozulan evre etkilenen kanalı gösterir.','X: Na⁺ kanalı · Y: K⁺ kanalı'),
  A('Öncülleri değerlendir','Her öncül tablodaki değerlerle karşılaştırılır.','Doğru öncüller belirlendi')],
 metin=onctxt('Üç aynı akson, ilaç uygulanmamış (Kontrol) ve X ya da Y ilacı uygulanmış ortamlarda eşik değerin üzerinde uyarılmıştır. İlaçlardan biri akson zarındaki Na⁺ kanallarını, diğeri K⁺ kanallarını açılamaz hâle getirmektedir. Tabloda dinlenme potansiyeli, uyarıdan sonra ulaşılan en yüksek değer ve bu değerden sonra dinlenme düzeyine dönüş süresi verilmiştir.\nBuna göre,',
   {'I':'X ilacı Na⁺ kanallarını, Y ilacı K⁺ kanallarını etkilemiştir.','II':'Y uygulanan aksonda depolarizasyon gerçekleşmemiştir.','III':'Y uygulanan aksonda dinlenme düzeyine dönüşün uzaması K⁺ çıkışının engellenmesinden kaynaklanır.'},'yargılarından hangileri doğrudur?'),
 sekil=SK4,dogru=I4['dogru'],yan=I4['yan'],sira=I4['sira'],istenen='Doğru olan yargıların belirlenmesi',ip=['Tepe değerinin ve dönüş süresinin hangi evreyi yansıttığını düşün.'],
 bilgi=[B('İyon kanalları ve evreler','Na⁺ kanalları depolarizasyondan, K⁺ kanalları repolarizasyondan sorumludur · kanallardan biri çalışmazsa ilgili evre bozulur')],puf='Hangi evrenin bozulduğuna bak, sonra kanalı eşleştir.')

# ======================= 05 · Sinaptik aralıkta nörotransmitter derişimi (orta, grafik, C) =======================
def nt(t,peak,tau):
    if t<=1: return 0.0
    if t<=2: return peak*(t-1)
    return peak*math.exp(-(t-2)/tau)
NK=(8,1.0); NX=(8,3.0); NY=(3,1.0)
tn=[i/10 for i in range(0,81)]
assert NX[0]==NK[0] and NX[1]>NK[1] and NY[0]<NK[0] and NY[1]==NK[1]
b=['\\begin{axis}[width=8.2cm,height=5.4cm,xmin=0,xmax=8,ymin=0,ymax=9.5,xtick={0,1,2,3,4,5,6,7,8},ytick={0,2,4,6,8},axis lines=left,xlabel={Zaman (ms)},ylabel={Aralıktaki nörotransmitter (birim)},ymajorgrids=true,grid style={gray!30},'+GOV+']',
   f'\\addplot[black] coordinates {{{pgf([(t,nt(t,*NK)) for t in tn])}}};',f'\\addplot[vurgu!80!black,dashed] coordinates {{{pgf([(t,nt(t,*NX)) for t in tn])}}};',f'\\addplot[black!60,dotted] coordinates {{{pgf([(t,nt(t,*NY)) for t in tn])}}};',
   '\\node[font=\\small\\bfseries] at (axis cs:3.9,1.9) {K};\\node[font=\\small\\bfseries,vurgu!80!black] at (axis cs:5.4,3.6) {X};\\node[font=\\small\\bfseries,black!60] at (axis cs:2.8,.7) {Y};','\\end{axis}']
SK5=gr('\n'.join(b))
d5=['X aralıktan uzaklaştırmayı yavaşlatmış, Y salınan miktarı azaltmıştır.','X salınan miktarı artırmış, Y aralıktan uzaklaştırmayı hızlandırmıştır.','X salınan miktarı artırmış, Y salınan miktarı azaltmıştır.','X aralıktan uzaklaştırmayı hızlandırmış, Y salınan miktarı azaltmıştır.','X aralıktan uzaklaştırmayı yavaşlatmış, Y aralıktan uzaklaştırmayı hızlandırmıştır.']
Q('0005','sinaps','orta','grafik','Sinaptik aralıkta nörotransmitter derişimi','Nörotransmitter derişim–zaman grafiğinden ilaçların salınım ve uzaklaştırma basamağına etkisini yorumlar.','Tepe değeri salınan miktarı, düşüşün hızı ise nörotransmitterin yıkım ve geri alımla aralıktan uzaklaştırılma hızını yansıtır.','Düşüşü yavaşlayan eğriyi salınımı artmış sanmak; tepe değeri düşük eğriyi uzaklaştırması hızlanmış saymak.','derişim–zaman grafiği',
 [A('Kontrolü oku','Kontrolde derişim uyarıdan sonra hızla yükselip tepeye ulaşır, sonra düşer.','K: yüksel → tepe → düş'),
  A('X ile K’yı karşılaştır','X’in tepe değeri K ile aynıdır; yalnız düşüşü daha yavaştır.','X: tepe aynı · düşüş yavaş'),
  A('Y ile K’yı karşılaştır','Y’nin tepe değeri K’dan düşüktür; düşüşü ise K ile aynı hızdadır.','Y: tepe düşük · düşüş aynı'),
  A('Basamakları eşleştir','Tepe salınan miktarla, düşüş hızı uzaklaştırma hızıyla ilgilidir.','X: uzaklaştırma yavaş · Y: salınım az')],
 metin='Tek bir uyarıyla uyarılan presinaptik nöronun akson ucundan salınan nörotransmitterin sinaptik aralıktaki derişimi, ilaç verilmemiş (K) ve X ya da Y ilacı verilmiş preparatlarda ölçülmüştür. İlaçlardan her biri yalnız bir basamağı, nörotransmitterin salınmasını ya da aralıktan yıkım ve geri alımla uzaklaştırılmasını etkilemektedir.\nGrafiğe göre, X ve Y ilaçlarının etkileri aşağıdakilerden hangisidir?',
 sekil=SK5,sira=[d5[1],d5[2],d5[0],d5[3],d5[4]],dogru=d5[0],
 yan=[(d5[1],'X’in tepe değeri K ile aynıdır; salınan miktar artmamıştır, yalnız düşüş yavaşlamıştır. Y’nin düşüş hızı K ile aynı olduğundan uzaklaştırması hızlanmamıştır, salınımı azalmıştır.','bilgi'),
      (d5[2],'X’in tepe değeri K ile aynıdır; bu nedenle salınan miktar artmamıştır; eğrideki fark yalnız düşüşün yavaşlamasıdır, bu da uzaklaştırmanın yavaşladığını gösterir.','bilgi'),
      (d5[3],'X’in düşüşü K’dan yavaştır; bu durum uzaklaştırmanın hızlanmadığını, yavaşladığını gösterir.','bilgi'),
      (d5[4],'Y’nin düşüşü K ile aynı hızdadır; uzaklaştırma hızlanmamıştır, tepe değerinin düşük olması salınımın azaldığını gösterir.','bilgi')],
 istenen='İlaçların etkilediği basamaklar',ip=['Tepe değerinin ve düşüş hızının hangi basamağı yansıttığını düşün.'],
 bilgi=[B('Sinaptik aralıkta nörotransmitter','nörotransmitter salınınca aralıktaki derişim artar · yıkım ya da geri alımla aralıktan uzaklaştırılınca derişim azalır')],puf='Tepe salınımı, düşüş uzaklaştırmayı gösterir.')

# ======================= 06 · Refleks süresi hesabı (zor, şekilli, D) =======================
DUYU=(360,60); ARA=(12,6); MOT=(600,50); SG=1; NSG=3
tD=DUYU[0]//DUYU[1]; tA=ARA[0]//ARA[1]; tM=MOT[0]//MOT[1]
assert DUYU[0]%DUYU[1]==0 and ARA[0]%ARA[1]==0 and MOT[0]%MOT[1]==0
TOP=tD+tA+tM+SG*NSG; assert (tD,tA,tM,TOP)==(6,2,12,23)
assert TOP-SG*NSG==20 and TOP-tA==21 and TOP-SG==22 and TOP+SG==24
b=['\\node[draw,rounded corners=3pt,line width=1pt,minimum height=.9cm,align=center,fill=vurgu!12] (r) at (0.1,0) {Reseptör};',
   '\\node[draw,rounded corners=3pt,line width=1pt,minimum height=.9cm,align=center,fill=vurgu!12] (k) at (13.9,0) {Kas};']
seg=[(1.1,4.4,'Duyu nöronu',f'{DUYU[0]} mm · {DUYU[1]} m/s'),(5.7,7.9,'Ara nöron',f'{ARA[0]} mm · {ARA[1]} m/s'),(9.2,12.0,'Motor nöron',f'{MOT[0]} mm · {MOT[1]} m/s')]
for x1,x2,ad_,v in seg:
    b.append(f'\\draw[{OKS},line width=1.6pt] ({x1},0)--({x2},0);')
    b.append(f'\\node[font=\\small\\bfseries] at ({(x1+x2)/2},.55) {{{ad_}}};\\node[font=\\small] at ({(x1+x2)/2},-.55) {{{v}}};')
for x in (5.05,8.55,12.5):
    b.append(f'\\node[circle,draw,line width=1pt,fill=white,inner sep=1.5pt,font=\\footnotesize] at ({x},0) {{{SG} ms}};\\node[font=\\footnotesize] at ({x},.75) {{sinaps}};')
SK6=tk('\n'.join(b),.85)
d6=[TOP-SG*NSG,TOP-tA,TOP-SG,TOP,TOP+SG]
Q('0006','yol','zor','şekilli','Refleks yayında iletim süresi','İletim hızı, yol uzunluğu ve sinaps gecikmesini birlikte kullanarak refleks yanıtının süresini hesaplar.','Her nöronda süre, uzunluğun hıza bölümüdür; yol boyunca geçilen her sinaps ayrıca gecikme ekler ve toplam süre bunların toplamıdır.','Sinaps gecikmelerini unutmak ya da sinaps sayısını yanlış saymak; kısa nöronun süresini ihmal etmek.','iletim süresi + sinaps gecikmesi',
 [A('Nöronların sürelerini bul','Her nöronda süre, uzunluğun iletim hızına bölünmesiyle bulunur; mm / (m/s) işlemi ms verir.','Duyu: 360/60 = 6 · Ara: 12/6 = 2 · Motor: 600/50 = 12'),
  A('Sinapsları say','Duyu–ara nöron, ara–motor nöron ve motor nöron–kas arasında üç sinaps vardır; her biri 1 ms gecikme ekler.','3 sinaps → 3 ms'),
  A('Toplamı hesapla','Nöronlardaki süreler ile sinaps gecikmeleri toplanır.','6 + 2 + 12 + 3 = 23 ms')],
 metin='Şekilde, parmağı bir cisme değen bir kişide kolun çekilmesini sağlayan refleks yayı şematik olarak gösterilmiş; nöronların aksonlarının uzunlukları ve iletim hızları verilmiştir. Her sinapsta impuls 1 ms gecikir; reseptörde ve kasta geçen süreler ile nöron gövdelerindeki iletim süreleri ihmal edilecektir. Şekil ölçekli değildir.\nBuna göre, reseptörün uyarılmasından kasın uyarılmasına kadar geçen süre kaç ms’dir?',
 sekil=SK6,dogru=TOP,
 yan=[(TOP-SG*NSG,'Üç sinapstaki gecikmeler toplama katılmamıştır; yalnız 6 + 2 + 12 = 20 ms bulunmuştur. Oysa her sinaps 1 ms gecikme ekler ve toplam 23 ms olur.','islem'),
      (TOP-tA,'Ara nöronun iletim süresi (12/6 = 2 ms) atlanmıştır; 6 + 12 + 3 = 21 ms bulunmuştur. Oysa ara nöron da impulsu iletir ve süreye katılır.','islem'),
      (TOP-SG,'Motor nöron ile kas arasındaki sinaps sayılmamış, yalnız iki sinaps eklenmiştir; 6 + 2 + 12 + 2 = 22 ms bulunmuştur. Oysa bu bağlantı da bir sinapstır ve 1 ms ekler.','dikkat'),
      (TOP+SG,'Reseptör ile duyu nöronu arasına da bir sinaps eklenip dört gecikme sayılmıştır; 6 + 2 + 12 + 4 = 24 ms bulunmuştur. Oysa reseptör duyu nöronunun ucudur ve orada sinaps yoktur.','dikkat')],
 istenen='Reseptörden kasa kadar geçen toplam süre',ip=['Önce her nöronun süresini, sonra yoldaki sinaps sayısını belirle.'],
 bilgi=[B('İletim süresi','bir nöronda geçen süre, akson uzunluğunun iletim hızına oranıdır · sinapsta impuls kimyasal iletim nedeniyle kısa bir süre gecikir')],puf='Süre = uzunluk / hız; sinaps gecikmelerini ayrıca ekle.')

# ======================= 07 · Tek yönlü iletim ve elektrot kaydı (orta, şekilli, olumsuz, D) =======================
KAYIT={'I':False,'II':True,'III':True,'IV':False,'V':False}
NEDEN07={'I':'A nöronu B’nin presinaptik nöronudur; sinapsta iletim tek yönlü olduğundan impuls B’den A’ya geçmez ve bu elektrotta kayıt alınmaz',
 'II':'uyarı aksonun ortasına verildiğinde impuls iki yönde ilerler; hücre gövdesi yönüne giden impuls bu elektrotta kaydedilir',
 'III':'akson ucu yönüne giden impuls bu elektrottan geçer ve kaydedilir',
 'IV':'B’nin akson ucuna ulaşan impuls engelleyici sinapsta C zarını eşik değerden uzaklaştırır; C’nin aksonunda impuls oluşmaz ve kayıt alınmaz',
 'V':'D nöronu da B’nin presinaptik nöronudur; impuls sinapsta geriye geçmediğinden bu elektrotta kayıt alınmaz'}
assert [r for r,v in KAYIT.items() if v]==['II','III']
b=[]
def nor(x,y,ad_): b.append(f'\\draw[line width=1.2pt,fill=vurgu!15] ({x},{y}) circle (.42);\\node[font=\\small\\bfseries] at ({x},{y}) {{{ad_}}};')
def tut(x,y,r): b.append(f'\\draw[line width=1.6pt,fill=black] ({x},{y+.4})--({x-.14},{y+.68})--({x+.14},{y+.68})--cycle;\\draw[line width=.8pt] ({x},{y+.68})--({x},{y+.85});\\node[font=\\normalsize\\bfseries] at ({x},{y+1.12}) {{{r}}};')
nor(0,0,'A'); nor(3.8,0,'B'); nor(9.4,0,'C'); nor(1.2,2.5,'D')
b.append('\\draw[line width=1.3pt] (.42,0)--(2.9,0);\\fill (2.9,0) circle (.14);')
b.append('\\draw[line width=1.3pt] (4.22,0)--(8.6,0);\\fill (8.6,0) circle (.14);')
b.append('\\draw[line width=1.3pt] (9.82,0)--(12.0,0);')
b.append('\\draw[line width=1.3pt] (1.62,2.5) to[out=0,in=100] (3.6,.55);\\fill (3.6,.55) circle (.14);')
b.append('\\node[font=\\small,color=vurgu!70!black] at (3.2,-.75) {uyarıcı};\\node[font=\\small,color=vurgu!70!black] at (2.55,1.3) {uyarıcı};\\node[font=\\small\\bfseries,align=center] at (8.6,-.75) {engelleyici};')
tut(1.7,0,'I'); tut(4.9,0,'II'); tut(7.4,0,'III'); tut(11.0,0,'IV'); tut(2.55,2.0,'V')
b.append(f'\\draw[{OKS},line width=1.8pt,color=vurgu] (6.2,-1.25)--(6.2,-.2);\\node[font=\\small\\bfseries,color=vurgu!70!black] at (6.2,-1.55) {{Uyarı}};')
SK7=tk('\n'.join(b),.78)
d7=['Yalnız II','II, III ve IV','I ve V','II ve III','I, IV ve V']
def kume07(o):
    S=set(o.replace('Yalnız ','').replace(' ve ',',').replace(', ',',').split(',')); return S
assert kume07(d7[3])=={'II','III'}
def yan07(o):
    S=kume07(o); p=[]
    for r in 'I II III IV V'.split():
        if r in S and not KAYIT[r]: p.append(f'{r} elektrotunda kayıt alınmaz: {NEDEN07[r]}')
        if r not in S and KAYIT[r]: p.append(f'{r} elektrotunda kayıt alınır: {NEDEN07[r]}')
    return '. '.join(x[0].upper()+x[1:] for x in p)+'.'
Q('0007','yol','orta','şekilli','Tek yönlü iletim ve elektrot kaydı','İmpulsun akson boyunca iki yönlü, sinapslarda tek yönlü iletildiğini yorumlayarak elektrot kayıtlarını öngörür.','Uyarı aksonun ortasına verilirse impuls iki yöne ilerler; sinapsı yalnız presinaptikten postsinaptik nörona geçer ve geriye geçmez.','Aksondaki iletimi tek yönlü, sinapstaki iletimi çift yönlü sanmak.','akson ve sinaps iletim yönü',
 [A('İletim yönlerini ayır','Aksonun ortasında oluşan impuls iki yöne ilerler; sinapsta ise iletim tek yönlüdür.','Akson: iki yön · sinaps: tek yön'),
  A('Elektrotları yerleştir','II ve III aynı aksonun iki yanındadır, IV sinapsın ilerisindedir; I ve V ise B’nin gerisindeki nöronlardadır.','II, III: B aksonu; IV: C; I, V: presinaptik'),
  A('Kayıt alınanı bul','Aksondaki II ve III numaralı elektrotlardan impuls geçer; I ve V presinaptik nöronlarda, IV ise engelleyici sinapsın ilerisindedir.','Kayıt: II ve III')],
 metin='Şekilde A, B, C ve D nöronları arasındaki bağlantılar ile sinir sistemindeki beş elektrodun (I–V) konumları gösterilmiştir. A ve D nöronlarının B ile yaptığı sinapslar uyarıcı, B nöronunun C ile yaptığı sinaps ise engelleyicidir. B nöronunun aksonunun ortasına eşik değerin üzerinde bir uyarı verilmiştir.\nBuna göre, numaralı elektrotların hangilerinde impuls kaydedilir?',
 sekil=SK7,sira=d7,dogru='II ve III',
 yan=[(o,yan07(o),'bilgi') for o in d7 if o!='II ve III'],
 istenen='İmpuls kaydedilen elektrotlar',ip=['Aksondaki ve sinapstaki iletim yönünü ayrı ayrı düşün, her elektrodun hangi nöronda olduğuna bak.'],
 bilgi=[B('İmpuls iletimi','akson boyunca iletim uyarılan noktadan başlar · sinapsta iletim akson ucundan salınan nörotransmitterle sağlanır')],puf='Her elektrodun hangi nöronda ve sinapsın hangi yanında olduğunu işaretle.')

# ======================= 08 · Otonom sinirler ve kalp atış hızı (zor, grafik, öncüllü, E) =======================
def sm(t,a,b_): 
    if t<=a: return 0.0
    if t>=b_: return 1.0
    return (1-math.cos(math.pi*(t-a)/(b_-a)))/2
def hr(t,rest,egz): return rest+(egz-rest)*(sm(t,2,3)-sm(t,6,7.5))
HRK=(70,150); HRL=(100,170); HRM=(66,90)
assert HRL[0]>HRK[0]>HRM[0] and HRL[1]>HRK[1]>HRM[1] and (HRM[1]-HRM[0])<(HRK[1]-HRK[0])
th=[i/10 for i in range(0,91)]
b=['\\begin{axis}[width=8.4cm,height=5.6cm,xmin=0,xmax=9,ymin=40,ymax=190,xtick={0,1,2,3,4,5,6,7,8,9},ytick={60,100,140,180},axis lines=left,xlabel={Zaman (dk)},ylabel={Kalp atış hızı (atım/dk)},ymajorgrids=true,grid style={gray!30},'+GOV+']',
   '\\fill[gray!18] (axis cs:2,40) rectangle (axis cs:6.5,190);\\node[font=\\small] at (axis cs:4.3,184) {Egzersiz};',
   f'\\addplot[black] coordinates {{{pgf([(t,hr(t,*HRK)) for t in th])}}};',f'\\addplot[vurgu!80!black,dashed] coordinates {{{pgf([(t,hr(t,*HRL)) for t in th])}}};',f'\\addplot[black!60,dotted] coordinates {{{pgf([(t,hr(t,*HRM)) for t in th])}}};',
   '\\node[font=\\small\\bfseries] at (axis cs:1,77) {K};\\node[font=\\small\\bfseries,vurgu!80!black] at (axis cs:1,107) {L};\\node[font=\\small\\bfseries,black!60] at (axis cs:1,59) {M};','\\end{axis}']
SK8=gr('\n'.join(b))
ST8={'I':(False,'Kalbi hızlandıran sinirin kesilmesi dinlenme hızını artırmaz; L’de dinlenme hızı kontrolden yüksektir, bu da yavaşlatıcı sinirin kesildiğini gösterir'),
     'II':(True,'M’de egzersizdeki artış kontrole göre küçüktür (66 → 90 atım/dk); egzersizde hızı artıran, yani kalbi hızlandıran sinir kesilmiştir'),
     'III':(True,'Yavaşlatıcı sinir kesilince (L) dinlenme hızı 70’ten 100 atım/dk’ya çıkmıştır; bu, sağlıklı bireyde bu sinirin kalbi yavaşlattığını gösterir')}
I8=onc(ST8,4,True)
Q('0008','kosul','zor','grafik','Otonom sinirlerin kalp atışına etkisi','Sinir kesme deneyi sonuçlarından sempatik ve parasempatik sinirlerin kalp atış hızına etkilerini birlikte çıkarır.','Sempatik sinir kalbi hızlandırır, parasempatik sinir yavaşlatır; hangisinin kesildiği dinlenme ve egzersiz hızlarının kontrole göre değişiminden anlaşılır.','Kesilen sinirin hangisi olduğunu kontrolle karşılaştırmadan, yalnız egzersiz hızına bakarak belirlemeye çalışmak.','sinir kesme deneyi',
 [A('Kontrolü oku','K eğrisinde kalp atış hızı dinlenmede düşük, egzersizde yüksektir.','K: 70 → 150 atım/dk'),
  A('L ve M’yi kontrolle karşılaştır','L’de dinlenme hızı kontrolden yüksektir; M’de egzersizdeki artış kontrole göre azdır.','L: dinlenme yüksek · M: artış az'),
  A('Sinirleri eşleştir','Dinlenme hızını artıran kesi, yavaşlatıcı siniri; egzersiz artışını azaltan kesi, hızlandırıcı siniri gösterir.','L: yavaşlatıcı kesik · M: hızlandırıcı kesik'),
  A('Yargıları değerlendir','Her yargı bu eşleştirmeyle karşılaştırılır.','Doğru yargılar belirlendi')],
 metin=onctxt('Bir hayvanda kalbi hızlandıran ve yavaşlatan otonom sinirlerden yalnız biri kesilmiş; L ve M hayvanlarında kesilen sinirler farklıdır. Sağlam bir hayvan (K) ile L ve M hayvanlarının kalp atış hızları, egzersiz öncesinde, sırasında ve sonrasında ölçülmüş; sonuçlar grafikte verilmiştir.\nBu grafiğe göre,',
   {'I':'L hayvanında kalbi hızlandıran sinir kesilmiştir.','II':'M hayvanında kalbi hızlandıran sinir kesilmiştir.','III':'Sağlıklı bir hayvanda dinlenme hâlinde kalp atış hızı, yavaşlatıcı sinirin etkisiyle düşük tutulur.'},'yargılarından hangileri doğrudur?'),
 sekil=SK8,dogru=I8['dogru'],yan=I8['yan'],sira=I8['sira'],istenen='Doğru olan yargıların belirlenmesi',ip=['Kontrole göre dinlenme hızının ve egzersizdeki artışın nasıl değiştiğine bak.'],
 bilgi=[B('Otonom sinirler','sempatik sinirler kalp atışını hızlandırır · parasempatik sinirler kalp atışını yavaşlatır · iki sistem birlikte kalp hızını ayarlar')],puf='Dinlenme hızı ve egzersizdeki artışı kontrolle karşılaştır.')

# ======================= 09 · Uyarıcı ve engelleyici sinapslar (zor, tablo, A) =======================
ET={'A':('Uyarıcı',2),'B':('Uyarıcı',3),'E':('Uyarıcı',5),'C':('Engelleyici',-3),'F':('Engelleyici',-2)}; ESIK=6
net=lambda s: sum(ET[x][1] for x in s)
assert net('ABEC')==7 and net('BEC')==5 and net('AECF')==2 and net('ABECF')==5 and net('ABCF')==0
SK9=tablo_svg(['Nöron','Sinaps türü','Uyarıldığında D’de etki (birim)'],[[k,v[0],('+'+str(v[1]) if v[1]>0 else '−'+str(-v[1]))] for k,v in ET.items()])
d9=['A, B, E ve C','B, E ve C','A, E, C ve F','A, B, E, C ve F','A, B, C ve F']
Q('0009','sinaps','zor','tablo','Uyarıcı ve engelleyici sinapsların toplamı','Uyarıcı ve engelleyici sinapsların etkilerini toplayarak postsinaptik nörondaki impuls oluşumunu öngörür.','Postsinaptik nöronda uyarıcı etkiler artı, engelleyici etkiler eksi olarak toplanır; toplam eşik değere ulaşırsa impuls oluşur.','Engelleyici sinapsın etkisini toplama katmak yerine çıkarmamak; eşik değerin altındaki toplamda da impuls beklemek.','uyarıcı–engelleyici toplamı',
 [A('Etkileri oku','A, B ve E uyarıcıdır ve D’de artı etki yapar; C ve F engelleyicidir ve eksi etki yapar.','A: +2 · B: +3 · E: +5 · C: −3 · F: −2'),
  A('Toplamları hesapla','Her şıktaki nöronların etkileri cebirsel olarak toplanır.','Her şık için net etki'),
  A('Eşikle karşılaştır','Net etkisi en az eşik değer olan şıkta D’de impuls oluşur.','Net etki ≥ 6 olan şık')],
 metin='D nöronuna A, B, C, E ve F nöronları sinaps yapmaktadır. Tabloda bu nöronlardan her biri tek başına uyarıldığında D nöronunun zarında oluşturduğu etki verilmiştir. Birden fazla nöron aynı anda uyarılırsa etkiler cebirsel olarak toplanır ve toplam etki en az +6 birim olduğunda D nöronunda impuls oluşur.\nBuna göre, aşağıdaki nöron gruplarından hangisi aynı anda uyarıldığında D nöronunda impuls oluşur?',
 sekil=SK9,sira=d9,dogru=d9[0],
 yan=[(d9[1],'Toplam etki +3 + 5 + (−3) = +5 birimdir; eşik değer olan +6’nın 1 birim altındadır ve impuls oluşmaz.','dikkat'),
      (d9[2],'Toplam etki +2 + 5 + (−3) + (−2) = +2 birimdir; iki engelleyici nöron etkiyi eşik değerin çok altına düşürür.','islem'),
      (d9[3],'Toplam etki +2 + 3 + 5 + (−3) + (−2) = +5 birimdir; eşik değerin yalnız 1 birim altında kaldığı için impuls oluşmaz.','dikkat'),
      (d9[4],'Toplam etki +2 + 3 + (−3) + (−2) = 0 birimdir; eşik değer olan +6’ya ulaşılamaz.','islem')],
 istenen='D nöronunda impuls oluşturan grup',ip=['Engelleyici nöronun etkisini eksi işaretle toplayıp eşik değerle karşılaştır.'],
 bilgi=[B('Uyarıcı ve engelleyici sinapslar','uyarıcı sinapslar postsinaptik nöronu eşik değere yaklaştırır · engelleyici sinapslar eşik değerden uzaklaştırır · nöron eşik değere ulaşırsa impuls oluşturur')],puf='Etkileri işaretleriyle topla, eşikle karşılaştır.')

# ======================= 10 · Sinir sistemi hastalıkları (orta, öncüllü, olumsuz, B) =======================
ST10={'I':(True,'Parkinson hastalığında dopamin üreten nöronlar kaybolur ve hareketin denetimi bozulur'),
      'II':(False,'Miyelin kılıfın yıkımıyla iletimin yavaşlaması multipl skleroz hastalığının özelliğidir; Alzheimer hastalığı beyindeki sinir hücrelerinin kaybına bağlı bellek ve düşünme bozukluğuyla ilgilidir'),
      'III':(True,'Epilepside beyindeki nöronların kontrolsüz ve eş zamanlı uyarılması nöbete yol açar')}
I10=onc(ST10,1,False)
Q('0010','kosul','orta','öncüllü','Sinir sistemi hastalıkları','Sinir sistemi hastalıklarının nedenlerine ve belirtilerine ilişkin yargıları değerlendirir.','Parkinson dopamin üreten nöronların kaybıyla, Alzheimer sinir hücresi kaybı ve bellek bozukluğuyla, epilepsi nöronların kontrolsüz uyarılmasıyla, multipl skleroz ise miyelin kaybıyla ilişkilidir.','Hastalıkların neden ve belirtilerini birbirine karıştırmak.','hastalık–neden eşleştirmesi',
 [A('Hastalıkları hatırla','Parkinson dopamin kaybıyla, epilepsi kontrolsüz nöron uyarılmasıyla, Alzheimer ise bellek kaybı ve nöron kaybıyla ilişkilidir.','Parkinson: dopamin · Epilepsi: nöbet · Alzheimer: bellek'),
  A('Yargıları sına','Her yargıdaki neden ve belirti ilgili hastalıkla karşılaştırılır.','Yanlış yargı belirlendi'),
  A('Kümeyi oluştur','Yalnız yanlış olan yargıların bulunduğu seçenek işaretlenir.','Yalnız II')],
 metin=onctxt('Sinir sistemini etkileyen hastalıkların nedenleri ve belirtileri incelenmektedir.\nBu hastalıklarla ilgili,',
   {'I':'Parkinson hastalığında beyinde dopamin üreten nöronların kaybı sonucu hareketlerin denetimi bozulur.','II':'Alzheimer hastalığında nöronların miyelin kılıfının yıkılması sonucu impuls iletimi yavaşlar.','III':'Epilepsi nöbetlerinde beyindeki nöronlar kontrolsüz ve eş zamanlı olarak uyarılır.'},'yargılarından hangileri yanlıştır?'),
 dogru=I10['dogru'],yan=I10['yan'],sira=I10['sira'],istenen='Yanlış olan yargıların belirlenmesi',ip=['Her hastalığın hangi yapı ya da maddeyle ilişkili olduğunu ayrı ayrı hatırla.'],
 bilgi=[B('Sinir sistemi hastalıkları','bazı hastalıklarda belirli nöron grupları kaybolur ya da işlev bozulur · belirtiler etkilenen yapının görevine göre değişir')],puf='Her hastalığı etkilenen yapıyla eşleştir.')

# ======================= bitiş =======================
from collections import Counter
for q in P.ANA: q['kardes']=None
P.yaz(os.path.join(GD,'siniriki-1.json'),'/tmp/bos-siniriki.json')
tipler={}
for c in KARTLAR: tipler.setdefault(c['tipId'],dict(tipId=c['tipId'],ad=c['tip'],kartlar=[],uygulamaKonu=KEY))['kartlar'].append(c['id'])
json.dump(dict(konu=KONU_AD,surum=1,not_='Kart = fikir; soru metni içermez. Kaynaklar: ÖSYM AYT 2018–2026 Biyoloji sinir sistemi (yalnız mantık), MEB 11. sınıf.',kartlar=KARTLAR,tipler=list(tipler.values())),
          open(os.path.join(HV,'kartlar','absiniriki.json'),'w'),ensure_ascii=False,indent=1)
HR=Counter(q['cevap']['sik'] for q in P.ANA); assert all(HR[h]==2 for h in 'ABCDE'),HR
assert Counter(q['zorluk'] for q in P.ANA)=={'kolay':2,'orta':5,'zor':3}
assert 4<=len({q['tipId'] for q in P.ANA})<=6
print('şekil',sum(1 for q in P.ANA if q['sekil']),HR)
