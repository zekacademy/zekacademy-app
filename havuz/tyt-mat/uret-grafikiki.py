"""Grafik Problemleri · parti 2 (hafif mod): 24 ana soru, kardeş yok, ipucu 1. Şekil de metin de aynı veri listelerinden üretilir;
her cevap ve her çeldirici değeri bu verilerden kodla hesaplanıp assert edilir. Çizim yardımcıları uret-grafikprob.py'den kopyalandı."""
import sys,os,math
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_mat as H
from _hafif_mat import *
from _hafif_mat import tablo_svg
H.KONU='Grafik Problemleri'
UK='prob|Grafik Problemleri'
P=Parti('grafikiki','Grafik Problemleri',UK)
ACC=G.ACC
TT=lambda **k:k
# ---------- çizim yardımcıları (G._svg / G._t / G.ACC stili; currentColor, viewBox)
def _eksen(x0,yb,x1,yt):
    return (f'<line x1="{x0}" y1="{yb}" x2="{x1}" y2="{yb}" stroke-width="1.6"/>'
            f'<line x1="{x0}" y1="{yb}" x2="{x0}" y2="{yt-8}" stroke-width="1.6"/>'
            f'<path d="M{x0-4} {yt-4} L{x0} {yt-12} L{x0+4} {yt-4}" stroke-width="1.4"/>')
def _izgara(x0,x1,Y,adim,ust,olcek):
    b=[]
    for v in range(adim,ust+1,adim):
        y=Y(v); b.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke-width="1" stroke-dasharray="3 3" opacity=".4"/>')
        if olcek: b.append(G._t(x0-6,y+4,str(v),anchor='end',size=10))
    if olcek: b.append(G._t(x0-6,Y(0)+4,'0',anchor='end',size=10))
    return ''.join(b)
def sutun(et,dg,adim,ust,ybas,xbas=None,olcek=True,W=330,H=226):
    """Sütun grafiği gövdesi. Her değer ızgara çizgisinde bitmeli (okunabilirlik)."""
    assert all(v%adim==0 and 0<v<=ust for v in dg) and len(et)==len(dg)
    x0,x1,yt,yb=46,W-8,34,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,olcek)]
    n=len(et); sl=(x1-x0)/n; bw=min(34,sl*.55)
    for i,(e,v) in enumerate(zip(et,dg)):
        cx=x0+sl*(i+.5); y=Y(v)
        b.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{yb-y:.1f}" stroke-width="1.2" style="fill:{ACC}" fill-opacity=".55"/>')
        b.append(G._t(cx,yb+15,e,size=10))
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def cizgi(et,dg,adim,ust,ybas,xbas=None,W=330,H=226):
    assert all(v%adim==0 and 0<v<=ust for v in dg) and len(et)==len(dg)
    x0,x1,yt,yb=46,W-12,34,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,True)]
    n=len(et); sl=(x1-x0)/n; pts=[(x0+sl*(i+.5),Y(v)) for i,v in enumerate(dg)]
    for (x,y),e in zip(pts,et):
        b.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{yb}" stroke-width="1" stroke-dasharray="2 3" opacity=".55"/>')
        b.append(G._t(x,yb+15,e,size=10))
    b.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" stroke-width="2.4" style="stroke:{ACC}"/>')
    for x,y in pts: b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" style="fill:{ACC};stroke:{ACC}"/>')
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def daire(dl,W=330,H=196,r=74):
    """dl: [(ad, derece)]; dilimler tepeden başlayıp saat yönünde. Açılar dilimin içinde, adlar dışında."""
    assert sum(d for _,d in dl)==360
    cx,cy=W/2,H/2; b=[]; a=-90.0; op=['.14','.42','.26','.56','.34']
    P_=lambda ang,rr:(cx+rr*math.cos(math.radians(ang)),cy+rr*math.sin(math.radians(ang)))
    for i,(ad,d) in enumerate(dl):
        a1=a+d; (xa,ya),(xb,yb)=P_(a,r),P_(a1,r)
        b.append(f'<path d="M{cx:.1f} {cy:.1f} L{xa:.1f} {ya:.1f} A{r} {r} 0 {1 if d>180 else 0} 1 {xb:.1f} {yb:.1f} Z" stroke-width="1.4" style="fill:{ACC}" fill-opacity="{op[i%len(op)]}"/>')
        m=a+d/2; xt,yt=P_(m,r*(.6 if d>=45 else .76)); b.append(G._t(xt,yt+4,f'{d}°',size=11,bold=True))
        xo,yo=P_(m,r+10); c=math.cos(math.radians(m))
        b.append(G._t(xo,yo+4,ad,anchor='start' if c>.25 else ('end' if c<-.25 else 'middle'),size=11))
        a=a1
    return ''.join(b),W,H
def tablo(bas,sat,gen):
    """bas: başlıklar; sat: satırlar (metin); gen: sütun genişlikleri."""
    W=sum(gen)+4; h=26; Hh=h*(len(sat)+1)+4; b=[]; xs=[2]
    for g in gen: xs.append(xs[-1]+g)
    b.append(f'<rect x="2" y="2" width="{W-4}" height="{h}" style="fill:currentColor;stroke:none" fill-opacity=".08"/>')
    for j,s in enumerate(bas): b.append(G._t((xs[j]+xs[j+1])/2,2+h/2+4,s,size=10,bold=True))
    for i,row in enumerate(sat):
        y=2+h*(i+1)
        for j,s in enumerate(row): b.append(G._t((xs[j]+xs[j+1])/2,y+h/2+4,s,size=11,bold=(j==0 or s=='?'),renk=(ACC if s=='?' else None)))
    for i in range(len(sat)+2): b.append(f'<line x1="2" y1="{2+h*i}" x2="{W-2}" y2="{2+h*i}" stroke-width="{1.4 if i in (0,1,len(sat)+1) else 1}"/>')
    for x in xs: b.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{2+h*(len(sat)+1)}" stroke-width="1"/>')
    return ''.join(b),W,Hh
def tek(g): body,W,Hh=g; return G._svg(W,Hh,body)
def alt_alta(*parcalar):
    """[(başlık, (gövde,W,H))] parçalarını alt alta tek SVG'de birleştirir."""
    W=max(p[1][1] for p in parcalar); y=0; b=[]
    for ad,(body,w,h) in parcalar:
        b.append(G._t(W/2,y+14,ad,size=11,bold=True)); b.append(f'<g transform="translate({(W-w)/2:.1f},{y+20})">{body}</g>'); y+=h+26
    return G._svg(W,y,''.join(b))


# ---------- ek çizim yardımcıları (aynı görsel dil)
def sutun_h(et,dg,adim,ust,ybas,xbas=None,W=340,H=226):
    """Sütun; dg içinde None = çizilmemiş sütun ('?' yazılır)."""
    assert all(v is None or (v%adim==0 and 0<v<=ust) for v in dg) and len(et)==len(dg)
    x0,x1,yt,yb=46,W-8,34,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,True)]
    n=len(et); sl=(x1-x0)/n; bw=min(34,sl*.55)
    for i,(e,v) in enumerate(zip(et,dg)):
        cx=x0+sl*(i+.5)
        if v is None: b.append(G._t(cx,yb-8,'?',size=16,bold=True,renk=ACC))
        else:
            y=Y(v); b.append(f'<rect x="{cx-bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{yb-y:.1f}" stroke-width="1.2" style="fill:{ACC}" fill-opacity=".55"/>')
        b.append(G._t(cx,yb+15,e,size=10))
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def _lejant(ogeler,x,y):
    b=[]; cx=x
    for i,(ad,tur) in enumerate(ogeler):
        if tur=='k': b.append(f'<rect x="{cx}" y="{y-8}" width="11" height="10" stroke-width="1.2" style="fill:{ACC}" fill-opacity=".55"/>' if i==0 else f'<rect x="{cx}" y="{y-8}" width="11" height="10" stroke-width="1.2" style="fill:currentColor" fill-opacity=".18"/>')
        else:
            if i==0: b.append(f'<line x1="{cx}" y1="{y-3}" x2="{cx+16}" y2="{y-3}" stroke-width="2.4" style="stroke:{ACC}"/><circle cx="{cx+8}" cy="{y-3}" r="3.2" style="fill:{ACC};stroke:{ACC}"/>')
            else: b.append(f'<line x1="{cx}" y1="{y-3}" x2="{cx+16}" y2="{y-3}" stroke-width="2" stroke-dasharray="5 3"/><rect x="{cx+5}" y="{y-6}" width="6" height="6" style="fill:currentColor;stroke:none"/>')
        w=16 if tur!='k' else 11
        b.append(G._t(cx+w+4,y,ad,anchor='start',size=10)); cx+=w+4+7*len(ad)+14
    return ''.join(b)
def sutun_g(et,seriler,adim,ust,ybas,xbas=None,W=340,H=240):
    """Gruplu sütun. seriler: [(ad,[değerler])]."""
    k=len(seriler); assert all(len(d)==len(et) and all(v%adim==0 and 0<v<=ust for v in d) for _,d in seriler)
    x0,x1,yt,yb=46,W-8,48,H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,True)]
    n=len(et); sl=(x1-x0)/n; bw=min(24,sl*.8/k)
    for i,e in enumerate(et):
        cx=x0+sl*(i+.5)
        for j,(ad,d) in enumerate(seriler):
            bx=cx-bw*k/2+bw*j; y=Y(d[i]); fill=(f'fill:{ACC}" fill-opacity=".55' if j==0 else 'fill:currentColor" fill-opacity=".18')
            b.append(f'<rect x="{bx:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{yb-y:.1f}" stroke-width="1.2" style="{fill}"/>')
        b.append(G._t(cx,yb+15,e,size=10))
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    b.append(_lejant([(ad,'k') for ad,_ in seriler],x0+14,32))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def cizgi_n(et,seriler,adim,ust,ybas,xbas=None,W=340,H=240):
    """Çizgi; seriler [(ad,[değerler])]; değer None = bilinmeyen ('?' yazılır, çizgiye katılmaz). Çok seride lejant çizilir."""
    assert all(len(d)==len(et) and all(v is None or (v%adim==0 and 0<v<=ust) for v in d) for _,d in seriler)
    coklu=len(seriler)>1
    x0,x1,yt,yb=46,W-12,(48 if coklu else 34),H-(42 if xbas else 26)
    Y=lambda v: yb-(yb-yt)*v/ust
    b=[_izgara(x0,x1,Y,adim,ust,True)]
    n=len(et); sl=(x1-x0)/n
    for i,e in enumerate(et): b.append(G._t(x0+sl*(i+.5),yb+15,e,size=10))
    for j,(ad,d) in enumerate(seriler):
        pts=[(x0+sl*(i+.5),Y(v) if v is not None else None) for i,v in enumerate(d)]
        stil=f'style="stroke:{ACC}" stroke-width="2.4"' if j==0 else 'stroke-width="2" stroke-dasharray="5 3"'
        seg=[]
        for (x,y) in pts+[(0,None)]:
            if y is None:
                if len(seg)>1: b.append('<polyline points="'+' '.join(f'{a:.1f},{c:.1f}' for a,c in seg)+f'" {stil}/>')
                seg=[]
            else: seg.append((x,y))
        for (x,y),v in zip(pts,d):
            if y is None:
                b.append(f'<line x1="{x:.1f}" y1="{yb}" x2="{x:.1f}" y2="{yt}" stroke-width="1" stroke-dasharray="2 3" opacity=".35"/>'); b.append(G._t(x,yb-8,'?',size=16,bold=True,renk=ACC))
            elif j==0: b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" style="fill:{ACC};stroke:{ACC}"/>')
            else: b.append(f'<rect x="{x-3.2:.1f}" y="{y-3.2:.1f}" width="6.4" height="6.4" style="fill:currentColor;stroke:none"/>')
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True))
    if coklu: b.append(_lejant([(ad,'c') for ad,_ in seriler],x0+14,32))
    if xbas: b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def dogrusal(seriler,xmax,xadim,ymax,yadim,xbas,ybas,etiket=None,yatay=None,W=340,H=236):
    """Doğrusal (parçalı) grafik. seriler: [(ad,[(x,y),...])]; köşe noktaları ızgaraya denk gelir ve değerleri eksende okunur.
    etiket: [(x,y,metin,anchor)] serbest yazılar; yatay: [(y,metin)] kesikli yatay çizgi + yazı."""
    x0,x1,yt,yb=46,W-14,34,H-40
    X=lambda v: x0+(x1-x0)*v/xmax; Y=lambda v: yb-(yb-yt)*v/ymax
    b=[]
    for v in range(xadim,xmax+1,xadim): b.append(f'<line x1="{X(v):.1f}" y1="{yb}" x2="{X(v):.1f}" y2="{yt}" stroke-width="1" stroke-dasharray="3 3" opacity=".3"/>'); b.append(G._t(X(v),yb+15,str(v),size=10))
    b.append(G._t(x0-6,yb+15,'0',anchor='end',size=10))
    b.append(_izgara(x0,x1,Y,yadim,ymax,True))
    for y,m in (yatay or []): b.append(f'<line x1="{x0}" y1="{Y(y):.1f}" x2="{x1}" y2="{Y(y):.1f}" stroke-width="1.4" stroke-dasharray="6 3" style="stroke:{ACC}"/>'); b.append(G._t(x1-2,Y(y)-5,m,anchor='end',size=10,bold=True))
    for j,(ad,pts) in enumerate(seriler):
        assert all(px%xadim==0 and py%yadim==0 and 0<=px<=xmax and 0<=py<=ymax for px,py in pts)
        stil=f'style="stroke:{ACC}" stroke-width="2.4"' if j==0 else 'stroke-width="2.2" stroke-dasharray="6 3"'
        b.append('<polyline points="'+' '.join(f'{X(px):.1f},{Y(py):.1f}' for px,py in pts)+f'" {stil}/>')
        for px,py in pts: b.append(f'<circle cx="{X(px):.1f}" cy="{Y(py):.1f}" r="3.4" style="fill:{ACC if j==0 else "currentColor"};stroke:none"/>')
    for x,y,m,an in (etiket or []): b.append(G._t(X(x),Y(y),m,anchor=an,size=11,bold=True))
    b.append(_eksen(x0,yb,x1,yt)); b.append(G._t(6,16,ybas,anchor='start',size=11,bold=True)); b.append(G._t((x0+x1)/2,H-6,xbas,size=11,bold=True))
    return ''.join(b),W,H
def daire_e(dl,W=330,H=196,r=74):
    """dl: [(ad, derece, etiket)]; etiket dilimin içinde gösterilir (örn. '3x'); çizim gerçek açıyla yapılır."""
    assert sum(d for _,d,_ in dl)==360
    cx,cy=W/2,H/2; b=[]; a=-90.0; op=['.14','.42','.26','.56','.34']
    P_=lambda ang,rr:(cx+rr*math.cos(math.radians(ang)),cy+rr*math.sin(math.radians(ang)))
    for i,(ad,d,et) in enumerate(dl):
        a1=a+d; (xa,ya),(xb,yb)=P_(a,r),P_(a1,r)
        b.append(f'<path d="M{cx:.1f} {cy:.1f} L{xa:.1f} {ya:.1f} A{r} {r} 0 {1 if d>180 else 0} 1 {xb:.1f} {yb:.1f} Z" stroke-width="1.4" style="fill:{ACC}" fill-opacity="{op[i%len(op)]}"/>')
        m=a+d/2; xt,yt=P_(m,r*(.6 if d>=45 else .76)); b.append(G._t(xt,yt+4,et,size=11,bold=True))
        xo,yo=P_(m,r+10); c=math.cos(math.radians(m))
        b.append(G._t(xo,yo+4,ad,anchor='start' if c>.25 else ('end' if c<-.25 else 'middle'),size=11))
        a=a1
    return ''.join(b),W,H
def sirali_s(s,d):
    assert s.count(d)==1; return d

KY='ÖSYM 2018–2026 TYT Matematik (Veri ve grafik problemleri) · yayın soru bankaları (yalnız mantık) · MEB 9. sınıf istatistik'
TIPAD={'grb-sutun':'Sütun grafiği okuma, karşılaştırma ve ortalama','grb-cizgi':'Çizgi grafiği: değişim, artış ve ortalama','grb-daire':'Daire grafiği: derece, yüzde ve adet',
 'grb-iki':'İki grafiği (ya da grafik ile tabloyu) birlikte yorumlama','grb-dogrusal':'Doğrusal grafik: yol–zaman ve depo–zaman','grb-oncullu':'Grafiğe göre ifadeleri değerlendirme (öncüllü)','grb-donusum':'Tablo–grafik dönüşümü ve yüzde değişim'}
kart('K-GRB-01','Sütun grafiği: okuma, karşılaştırma, ortalama','Sütun grafiğinden değerler okunur; fark, toplam ve aritmetik ortalama (eksik sütun dahil) hesaplanır.','Komşu sütunu okumak; ortalamayı toplam ya da ortanca sanmak; bölen olarak yanlış adet kullanmak.','orta','grafik',3,'grb-sutun',TIPAD['grb-sutun'],KY)
kart('K-GRB-02','Çizgi grafiği: değişim ve artış','Çizgi grafiğinde ardışık dönemlerin farkı ve yüzde değişimi hesaplanır; en büyük artış ile en büyük yüzde artış ayırt edilir.','Miktar artışı ile yüzde artışı karıştırmak; yüzde değişimi yeni değere bölmek; bilinmeyen noktayı denklemle bulmamak.','orta','grafik',3,'grb-cizgi',TIPAD['grb-cizgi'],KY)
kart('K-GRB-03','Daire grafiği: derece, yüzde, adet','Daire 360°’dir; dilimin değeri toplam × açı ÷ 360 ile bulunur; fark ya da bilinmeyen açı (x) üzerinden toplam ve tutar bulunur.','Açıyı sayı sanmak; açı farkını kişi farkı sanmak; iki daire grafiğinde dilim açılarını sayı yerine kullanmak.','orta','grafik',3,'grb-daire',TIPAD['grb-daire'],KY)
kart('K-GRB-04','İki grafik ya da grafik ve tablo','İki şekildeki veriler (adet, fiyat, oran, kişi sayısı) birleştirilir; gelir = fiyat × adet ve kişi başına değer hesaplanır.','Fiyatı yanlış satırdan okumak; bölümlerin ortalamasını alıp ağırlığı unutmak; iki grafiğin ölçeklerini karıştırmak.','zor','grafik',4,'grb-iki',TIPAD['grb-iki'],KY)
kart('K-GRB-05','Doğrusal grafik: yol–zaman, depo–zaman','Doğrunun eğimi hız ya da akış hızıdır; iki doğrunun kesişimi karşılaşma anıdır; ortalama hız = toplam yol ÷ toplam süre.','Eğimi iki noktanın değerlerini bölmek yerine toplamak; mola süresini katmamak; hızların aritmetik ortalamasını almak.','orta','grafik',3,'grb-dogrusal',TIPAD['grb-dogrusal'],KY)
kart('K-GRB-06','Grafiğe göre ifadeler (öncüllü)','Her ifade grafikten okunan değerlerle ayrı ayrı sınanır; “doğru” ve “yanlış” sorusu karıştırılmaz.','Soru kökünü (doğru/yanlış) yanlış okumak; yüzde artış yerine yeni değerin yüzdesini almak; toplamı hesaplamadan karar vermek.','orta','öncüllü',3,'grb-oncullu',TIPAD['grb-oncullu'],KY)
kart('K-GRB-07','Tablo–grafik dönüşümü ve yüzde değişim','Tablodaki sayılar daire grafiğinde dereceye, sütun grafiğinde orantılı uzunluğa dönüştürülür; gruplu sütunda yüzde değişim hesaplanır.','Sayıyı dereceye ya da cm’ye çevirmeden yazmak; en çok artan ürünle yüzde olarak en çok artan ürünü karıştırmak.','orta','tablo',3,'grb-donusum',TIPAD['grb-donusum'],KY)

SOK=B('Sütun grafiği okuma','sütunun üst ucundan yatay çizgiyi izleyip dikey eksendeki değeri oku')
CIZ=B('Çizgi grafiği okuma','noktadan yatay çizgiyi izleyip dikey eksendeki değeri oku; ardışık noktaların farkı iki dönem arasındaki değişimdir')
ORT=B('Aritmetik ortalama','sayıların toplamı ÷ adedi; toplam = ortalama × adet. Örnek: 4, 6 ve 11’in ortalaması 21 ÷ 3 = 7, toplamları 7 × 3 = 21')
DAI=B('Daire grafiği','tüm daire 360°’dir; dilimin sayısı = toplam × açı ÷ 360. Örnek: 60 kişide 90°’lik dilim ⇒ 60 × 90 ÷ 360 = 15 kişi')
DER=B('Bir derecenin değeri','bilinen sayı ÷ ona karşılık gelen açı. Örnek: 90° = 1800 TL ise 1° = 20 TL')
DEG=B('Yüzde değişim','değişim ÷ eski değer × 100. Örnek: 40’tan 50’ye çıkış ⇒ 10 ÷ 40 = %25 artış')
GEL=B('Gelir','gelir = birim fiyat × satılan adet. Örnek: tanesi 25 TL olan üründen 8 tane ⇒ 200 TL')
HIZ=B('Hız ve eğim','yol–zaman grafiğinde doğrunun eğimi hızdır: hız = yol farkı ÷ süre farkı. Örnek: 2 saatte 100 km yol alan aracın hızı 50 km/sa')
AKI=B('Doğrusal grafikte akış hızı','depo–zaman grafiğinde birim sürede değişen su miktarı eğimdir. Örnek: 3 dakikada 150 L artış ⇒ 50 L/dk')
ORH=B('Ortalama hız','ortalama hız = toplam yol ÷ toplam süre (duraklama süresi dahil). Örnek: 3 saatte 90 km ⇒ 30 km/sa')

def M(no,tipId,z,alt,kaz,kalip,kart_,metin,dogru,yan,istenen,ip,bilgi,ad,puf,sekil,sira=None):
    mk(P,no,metin=metin,dogru=dogru,yan=yan,istenen=istenen,ad=ad,sekil=sekil,sira=sira,ip=[ip],bilgi=bilgi,puf=puf,tipId=tipId,tip=TIPAD[tipId],z=z,alt=alt,kaz=kaz,kalip=kalip,adim=len(ad),kart=kart_)

# ---------- 01 kolay · sütun ortalama (basketbolcu)
et=['1.','2.','3.','4.','5.','6.']; dg=[12,24,15,18,9,18]
top=sum(dg); ort=Fr(top,6); srt=sorted(dg); med=Fr(srt[2]+srt[3],2)
assert top==96 and ort==16 and med==Fr(33,2) and dg.count(18)==2 and Fr(top,5)==Fr(96,5)
SK=tek(sutun(et,dg,3,24,'Sayı','Maç sırası'))
M('0001','grb-sutun','kolay','Sütun Grafiğinde Ortalama','Sütun grafiğinden değerleri okuyup aritmetik ortalamayı hesaplar.','grafik','K-GRB-01 (sütun grafiği, ortalama) · basketbolcunun maç sayıları',
 'Bir basketbol oyuncusunun bir sezonda oynadığı ilk altı maçta attığı sayılar aşağıdaki sütun grafiğinde gösterilmiştir.\nBuna göre bu oyuncunun bu altı maçta maç başına attığı sayıların aritmetik ortalaması kaçtır?',
 16,[(Fr(33,2),'Ortalama yerine ortancayı (sıralanmış 15 ile 18’in ortası) bulmuş.','bilgi'),(18,'Ortalama yerine en sık görülen değeri (18) almış.','bilgi'),(Fr(96,5),'Toplamı maç sayısı olan 6 yerine 5’e bölmüş.','dikkat'),(96,'Toplamı bulup maç sayısına bölmeyi unutmuş.','islem')],
 'Maç başına atılan sayıların aritmetik ortalaması.',
 'Önce altı sütunun değerini oku, sonra bunların toplamını maç sayısıyla ilişkilendir.',[SOK,ORT],
 [A('Değerleri oku','Altı sütunun değeri.','12 · 24 · 15 · 18 · 9 · 18'),A('Toplamı bul','Altı değeri topla.','12 + 24 + 15 + 18 + 9 + 18 = 96'),A('Ortalamayı bul','Toplamı 6’ya böl.','96 ÷ 6 = 16')],
 'Ortalama sorulduğunda önce tüm sütunları toplayıp sütun sayısına böl; ortanca ve en sık değer ortalama değildir.',SK)

# ---------- 02 kolay · daire derece → kişi
dl=[('Çay',150),('Kahve',90),('Ayran',60),('Meyve suyu',60)]; N=1200
kis={a:Fr(N*d,360) for a,d in dl}; assert kis=={'Çay':500,'Kahve':300,'Ayran':200,'Meyve suyu':200} and kis['Çay']-kis['Kahve']==200 and Fr(N,360)*60==200
SK=tek(daire(dl))
M('0002','grb-daire','kolay','Daire Grafiğinde Fark','Daire grafiğinde dilim açılarından kişi sayılarını bulur ve iki dilimin farkını hesaplar.','grafik','K-GRB-03 (daire grafiği, derece ↔ kişi) · içecek tercihi anketi',
 'Bir anket şirketi, 1200 kişiye en çok tercih ettikleri sıcak ya da soğuk içeceği sormuştur. Her kişi yalnız bir içecek seçmiştir. Cevapların dağılımı aşağıdaki daire grafiğinde gösterilmiştir.\nBuna göre kahveyi seçenler, çayı seçenlerden kaç kişi azdır?',
 200,[(60,'Açı farkını (150° − 90° = 60°) kişi farkı sanmış.','bilgi'),(300,'Çay ile kahve farkı yerine kahveyi seçenlerin sayısını vermiş.','dikkat'),(500,'Fark yerine çayı seçenlerin sayısını vermiş.','dikkat'),(800,'Farkı almak yerine çay ve kahve sayılarını toplamış.','islem')],
 'Çay ve kahve seçenlerin sayıları arasındaki fark.',
 'Bir derecenin kaç kişiye karşılık geldiğini bul.',[DAI,DER],
 [A('Bir derecenin değeri','1200 kişi 360°’ye karşılık gelir.','1200 ÷ 360 = 10/3 kişi'),A('İki dilimin sayısı','Çay 150°, kahve 90°.','çay: 500 kişi · kahve: 300 kişi'),A('Farkı al','Çay − kahve.','500 − 300 = 200')],
 'Daire grafiğinde iki dilimin farkı, açı farkı × (toplam ÷ 360) ile doğrudan bulunabilir.',SK)

# ---------- 03 kolay · çizgi en büyük artış
et=['Pzt','Sal','Çar','Per','Cum','Cmt']; dg=[16,20,12,28,24,32]
fk=[b-a for a,b in zip(dg,dg[1:])]; assert fk==[4,-8,16,-4,8] and max(fk)==16 and max(dg)-min(dg)==20 and max(dg)==32
SK=tek(cizgi(et,dg,4,32,'Sıcaklık (°C)','Günler'))
M('0003','grb-cizgi','kolay','Çizgi Grafiğinde Artış','Çizgi grafiğinden ardışık değerlerin farkını bulup en büyük artışı belirler.','grafik','K-GRB-02 (çizgi grafiği, en büyük artış) · günlük en yüksek sıcaklık',
 'Bir kentte altı gün boyunca ölçülen günlük en yüksek sıcaklıklar aşağıdaki çizgi grafiğinde gösterilmiştir.\nBuna göre iki ardışık gün arasındaki en büyük sıcaklık artışı kaç °C’dir?',
 16,[(4,'Yalnızca ilk iki gün arasındaki artışı (20 − 16) bulmuş.','dikkat'),(8,'Sıcaklık düşüşünün en büyüğünü (20 → 12) ya da son artışı (24 → 32) almış; en büyük artışı seçmemiş.','dikkat'),(20,'Ardışık günlere bakmadan en yüksek ile en düşük sıcaklığın farkını (32 − 12) almış.','bilgi'),(32,'Artış yerine grafikteki en yüksek sıcaklığı vermiş.','dikkat')],
 'İki ardışık gün arasındaki en büyük sıcaklık artışı (°C).',
 'Her gün çiftinde bir sonraki gün değerinden bir önceki gün değerini çıkar.',[CIZ],
 [A('Değerleri oku','Altı günün sıcaklıkları.','16 · 20 · 12 · 28 · 24 · 32'),A('Ardışık farklar','Her günü bir önceki günle karşılaştır.','+4 · −8 · +16 · −4 · +8'),A('En büyük artış','Pozitif farkların en büyüğü.','16 °C (çarşambadan perşembeye)')],
 'En büyük artış, ardışık iki nokta arasındaki en büyük pozitif farktır; en yüksek ve en düşük değerin farkı ardışık olmayabilir.',SK)

# ---------- 04 kolay · yol-zaman
dogru_pts=[(0,0),(3,150)]; v=Fr(150,3); assert v==50 and v*5==250 and v*4==200 and v*2==100
SK=tek(dogrusal([('Motosikletli',dogru_pts)],5,1,250,50,'Süre (saat)','Yol (km)'))
M('0004','grb-dogrusal','kolay','Yol–Zaman Grafiği','Yol–zaman grafiğinden sabit hızı bulur ve verilen sürede alınacak yolu hesaplar.','grafik','K-GRB-05 (yol–zaman, hız) · motosikletli',
 'Bir motosikletlinin düz bir yolda sabit hızla gitmesine ait yol–zaman grafiği aşağıda verilmiştir.\nMotosikletli aynı hızla 5 saat gittiğinde toplam kaç km yol almış olur?',
 250,[(50,'Hızı (50 km/sa) bulup süreyle çarpmayı unutmuş.','islem'),(150,'Grafikteki son değeri (3 saatteki yolu) cevap sanmış.','dikkat'),(200,'Süreyi 5 − 1 = 4 saat almış (50 × 4).','dikkat'),(100,'Hızı (50 km/sa) bulup yalnız grafikte gösterilmeyen son 2 saatle (5 − 3) çarpmış.','dikkat')],
 'Motosikletlinin 5 saatte aldığı toplam yol (km).',
 'Grafikteki bir noktadan hız bulunur.',[HIZ],
 [A('Noktayı oku','Doğru, 3. saatte 150 km’ye ulaşıyor.','3 saat → 150 km'),A('Hızı bul','Yol ÷ süre.','150 ÷ 3 = 50 km/sa'),A('5 saatlik yol','Hız × süre.','50 × 5 = 250 km')],
 'Başlangıçtan geçen doğrusal yol–zaman grafiğinde hız, herhangi bir noktadaki yol ÷ süre değeridir.',SK)

# ---------- 05 kolay · tablo → daire
bas=['Ürün','Satış adedi']; sat=[['Simit',60],['Tost',45],['Poğaça',30],['Ayran',45]]; tp=sum(r[1] for r in sat)
ac={r[0]:Fr(r[1]*360,tp) for r in sat}; assert tp==180 and ac=={'Simit':120,'Tost':90,'Poğaça':60,'Ayran':90} and sum(ac.values())==360
SK=tablo_svg(bas,[[a,str(b)] for a,b in sat])
M('0005','grb-donusum','kolay','Tablodan Daire Grafiğine','Tablodaki sayıları daire grafiğindeki merkez açılara dönüştürür.','tablo','K-GRB-07 (tablodan daire grafiğine) · kantin satış tablosu',
 'Bir okul kantininde bir günde satılan dört ürünün adetleri aşağıdaki tabloda verilmiştir.\nBu veriler bir daire grafiğiyle gösterilecek olursa poğaça satışını gösteren daire diliminin merkez açısı kaç derece olur?',
 60,[(30,'Poğaça adedini (30) açı olarak yazmış.','bilgi'),(90,'Poğaça yerine tost ya da ayran satırını okumuş.','dikkat'),(120,'Poğaça yerine simit satırını okumuş.','dikkat'),(180,'Toplam adedi (180) dereceyle karıştırmış.','dikkat')],
 'Poğaça diliminin merkez açısı (derece).',
 'Poğaça adedinin toplam satışa oranını, tam daire olan 360° ile ilişkilendir.',[DAI],
 [A('Toplam satış','Dört ürünün adetlerini topla.','60 + 45 + 30 + 45 = 180'),A('Poğaçanın payı','Poğaça adedi ÷ toplam.','30 ÷ 180 = 1/6'),A('Açıyı bul','Pay × 360°.','1/6 × 360° = 60°')],
 'Tablodaki bir sayıyı daire grafiğine çevirirken açı = (sayı ÷ toplam) × 360° bağıntısını kullan.',SK)

# ---------- 06 orta · gruplu sütun, iki şube
et=['Nisan','Mayıs','Haziran','Temmuz']; ms=[30,50,70,40]; sh=[40,30,50,60]
tp=[a+b for a,b in zip(ms,sh)]; assert tp==[70,80,120,100] and max(tp)==120 and tp.index(120)==2
assert max(ms)==70 and max(sh)==60 and max(ms)+max(sh)==130 and tp[3]==100
SK=tek(sutun_g(et,[('Merkez',ms),('Sahil',sh)],10,80,'Satılan bisiklet','Aylar'))
M('0006','grb-sutun','orta','Gruplu Sütun Grafiği','İki gruplu sütun grafiğinde aylık toplamları karşılaştırıp en yüksek toplamı bulur.','grafik','K-GRB-01 (gruplu sütun, aylık toplam) · bisiklet mağazasının iki şubesi',
 'Bir bisiklet mağazasının Merkez ve Sahil şubelerinin nisan–temmuz aylarında sattığı bisiklet sayıları aşağıdaki grafikte gösterilmiştir.\nBuna göre iki şubenin birlikte en çok bisiklet sattığı ayda, bu iki şubenin sattığı toplam bisiklet sayısı kaçtır?',
 120,[(60,'Yalnız Sahil şubesinin en yüksek sütununu (temmuz) okumuş.','dikkat'),(70,'Yalnız Merkez şubesinin en yüksek sütununu (haziran) okumuş.','dikkat'),(100,'Sahil’in en çok sattığı ayı (temmuz) seçip o ayın toplamını (40 + 60) almış.','bilgi'),(130,'Her şubenin kendi en yüksek sütununu (70 + 60) farklı aylar olsa da toplamış.','islem')],
 'İki şubenin birlikte en çok sattığı aydaki toplam satış.',
 'Önce her ay için iki sütunun değerini birlikte düşün.',[SOK],
 [A('Değerleri oku','Her ay Merkez ve Sahil.','Nisan: 30, 40 · Mayıs: 50, 30 · Haziran: 70, 50 · Temmuz: 40, 60'),A('Aylık toplamlar','İki şubeyi topla.','70 · 80 · 120 · 100'),A('En büyüğü seç','Haziran.','120')],
 'Birlikte sorulduğunda her ay için iki şubenin değerlerini topla, sonra en büyüğünü seç.',SK)

# ---------- 07 orta · çizgi, en büyük yüzde artış
et=['Oca','Şub','Mar','Nis','May','Haz']; dg=[30,40,60,70,100,120]
yz=[Fr(b-a,a)*100 for a,b in zip(dg,dg[1:])]; assert yz==[Fr(100,3),50,Fr(50,3),Fr(300,7),20] and max(yz)==50 and yz.index(50)==1
assert max(b-a for a,b in zip(dg,dg[1:]))==30 and Fr(60,40)*100==150 and Fr(120-30,30)*100==300 and Fr(120-100,100)*100==20
SK=tek(cizgi(et,dg,10,120,'Kullanıcı (bin)','Aylar'))
M('0007','grb-cizgi','orta','Yüzde Artış','Çizgi grafiğinde bir önceki aya göre yüzde artışları hesaplayıp en büyüğünü bulur.','grafik','K-GRB-02 (çizgi grafiği, yüzde artış) · mobil uygulama kullanıcıları',
 'Bir mobil uygulamanın ocak–haziran aylarındaki aylık aktif kullanıcı sayıları (bin kişi) aşağıdaki çizgi grafiğinde gösterilmiştir.\nBuna göre bir önceki aya göre yüzde artışı en fazla olan ayda bu artış yüzde kaçtır?',
 50,[(20,'Yüzde artışı en fazla olan ayı aramadan son ayın (100 → 120) artışını almış.','dikkat'),(30,'Yüzde yerine miktar artışının en büyüğünü (70 → 100 için 30 bin) vermiş.','bilgi'),(150,'Mart değerini şubat değerine bölüp (60 ÷ 40) yeni değerin eskiye oranını artış yüzdesi sanmış.','islem'),(300,'Ardışık aylara bakmadan ocaktan hazirana toplam artışı (30 → 120) bulmuş.','dikkat')],
 'En büyük yüzde artışı (%).',
 'Her ay için artışı bir önceki aya böl; en büyük miktar artışı en büyük yüzde artışı vermeyebilir.',[CIZ,DEG],
 [A('Değerleri oku','Altı ayın kullanıcı sayıları (bin).','30 · 40 · 60 · 70 · 100 · 120'),A('Yüzde artışları','(yeni − eski) ÷ eski × 100.','%33,3 · %50 · %16,7 · %42,9 · %20'),A('En büyüğünü seç','Şubattan marta geçiş.','40 → 60: 20 ÷ 40 = %50')],
 'En büyük artış miktarı ile en büyük yüzde artış farklı aylarda olabilir; yüzdeyi her seferinde bir önceki değere bölerek bul.',SK)

# ---------- 08 orta · daire farktan toplam
dl=[('Üretim',150),('Satış',100),('Muhasebe',70),('İnsan kaynakları',40)]; d=dict(dl)
assert sum(d.values())==360; fark=30; k=Fr(fark,d['Üretim']-d['Satış']); N=360*k
assert N==216 and N*150/360==90 and N*100/360==60 and Fr(fark*360,150)==Fr(72) and Fr(fark*360,100)==Fr(108)
SK=tek(daire(dl))
M('0008','grb-daire','orta','Daire Grafiğinde Fark','Daire grafiğinde iki dilimin açı farkı ile kişi farkını eşleyerek toplam sayıyı bulur.','grafik','K-GRB-03 (daire grafiği, farktan toplam) · şirket bölümleri',
 'Bir şirkette çalışanların bölümlere göre dağılımı aşağıdaki daire grafiğinde gösterilmiştir. Üretim bölümündeki çalışan sayısı, satış bölümündeki çalışan sayısından 30 fazladır.\nBuna göre şirketin toplam çalışan sayısı kaçtır?',
 216,[(60,'Toplam yerine satış bölümündeki çalışan sayısını (100° için 60 kişi) vermiş.','dikkat'),(72,'30 kişiyi üretimin 150°’sine eşleyip 360 ÷ 150 ile çarpmış; farkın açısını (50°) kullanmamış.','bilgi'),(90,'Toplam yerine üretim bölümündeki çalışan sayısını (150° için 90 kişi) vermiş.','dikkat'),(108,'30 kişiyi satışın 100°’sine eşleyip 360 ÷ 100 ile çarpmış; farkın açısını (50°) kullanmamış.','bilgi')],
 'Şirketin toplam çalışan sayısı.',
 'Fark olan 30 kişi, hangi açı farkına karşılık geliyor?',[DAI,DER],
 [A('Açı farkı','Üretim − satış açıları.','150° − 100° = 50°'),A('Bir derecenin değeri','50° ↔ 30 kişi.','30 ÷ 50 = 0,6 kişi'),A('Toplam çalışan','Tam daire 360°.','360 × 0,6 = 216')],
 'İki dilimin farkı verildiğinde, açı farkı ile kişi farkını eşleyip bir derecenin değerini bul; sonra 360 ile çarp.',SK)

# ---------- 09 orta · yol-zaman kesişim
p1=[(0,0),(6,240)]; p2=[(0,240),(3,0)]
v1=Fr(240,6); v2=Fr(240,3); assert v1==40 and v2==80
tk=Fr(240,v1+v2); yer=v1*tk; assert tk==2 and yer==80 and 240-yer==160 and Fr(240,2)==120
SK=tek(dogrusal([('Araç 1',p1),('Araç 2',p2)],6,1,240,40,'Süre (saat)','A’ya uzaklık (km)',etiket=[(5,172,'Araç 1','middle'),(1.3,150,'Araç 2','start')]))
M('0009','grb-dogrusal','orta','Karşılaşma Noktası','İki doğrusal yol–zaman grafiğinin kesişiminden karşılaşma anını ve konumunu bulur.','grafik','K-GRB-05 (yol–zaman, kesişim) · iki araç, A ve B şehirleri',
 'A ve B şehirleri arasındaki 240 km’lik düz yolda iki araç, aynı anda ve sabit hızlarla biri A’dan B’ye, diğeri B’den A’ya doğru yola çıkmıştır. Araçların A şehrine olan uzaklıklarının zamana göre değişimi aşağıdaki grafikte gösterilmiştir.\nBuna göre araçlar karşılaştıkları anda 1. aracın B şehrine ulaşması için kaç km yolu kalmıştır?',
 160,[(2,'Karşılaşma süresini (2 saat) yol sanmış.','dikkat'),(80,'Karşılaşma noktasının A’ya uzaklığını vermiş; B’ye kalanı bulmamış.','dikkat'),(120,'Araçların hızlarını hesaba katmadan yolun yarısını (240 ÷ 2) almış.','bilgi'),(240,'Toplam yolu cevap sanmış.','dikkat')],
 'Karşılaşma anında 1. aracın B’ye kalan yolu (km).',
 'Her aracın hızını grafikten bul; karşılaşma anı grafikte nerede görünüyor?',[HIZ],
 [A('Hızları bul','1. araç 6 saatte 240 km; 2. araç 3 saatte 240 km.','40 km/sa · 80 km/sa'),A('Karşılaşma anı','Yaklaşma hızı 40 + 80 = 120 km/sa.','240 ÷ 120 = 2 saat'),A('1. aracın yolu','2 saatte aldığı yol.','40 × 2 = 80 km'),A('B’ye kalan','Toplam yoldan çıkar.','240 − 80 = 160 km')],
 'Zıt yönden gelen iki araçta karşılaşma süresi = toplam yol ÷ hızlar toplamı; grafikte bu nokta doğruların kesiştiği noktadır.',SK)

# ---------- 10 orta · depo boşalma
pts=[(0,0),(4,400),(8,200)]; dolum=Fr(400,4); bosalma=Fr(400-200,8-4)
t_bos=4+Fr(400,bosalma); assert dolum==100 and bosalma==50 and t_bos==12 and Fr(200,bosalma)==4 and Fr(400,bosalma)==8 and 8+Fr(200,dolum)==10 and Fr(200,dolum)==2
SK=tek(dogrusal([('Su',pts)],8,1,400,100,'Süre (dakika)','Su miktarı (L)'))
M('0010','grb-dogrusal','orta','Depo Boşalma','Depo–zaman grafiğinde dolum ve boşalma hızlarını ayırıp tamamen boşalma anını bulur.','grafik','K-GRB-05 (depo–zaman, boşalma) · önce dolan sonra boşalan depo',
 'Başlangıçta boş olan bir depoya su doldurulmuş, ardından depodaki su boşaltılmıştır. Depodaki su miktarının zamana göre değişimi aşağıdaki grafikte gösterilmiştir. Dolum ve boşaltma sırasında akış hızları sabittir ve boşaltma, grafikteki hızla aynı biçimde sürmektedir.\nBuna göre depo, dolum başladıktan kaç dakika sonra tamamen boşalır?',
 12,[(4,'Grafiğin bitiminden sonra kalan süreyi (200 ÷ 50) toplam süre sanmış.','dikkat'),(8,'Boşalma süresini (400 ÷ 50) bulup dolumun geçen 4 dakikasını eklememiş.','dikkat'),(10,'Boşalma hızı yerine dolum hızını (100 L/dk) kullanıp 8 + 200 ÷ 100 işlemini yapmış.','bilgi'),(2,'Boşalma hızı yerine dolum hızını (100 L/dk) alıp yalnız kalan süreyi (200 ÷ 100) vermiş.','islem')],
 'Depo dolum başladıktan kaç dakika sonra tamamen boşalır?',
 'Boşalma hızını, grafiğin azalan bölümünün iki noktasından bul.',[AKI],
 [A('Boşalma hızı','4. dakikada 400 L, 8. dakikada 200 L.','(400 − 200) ÷ (8 − 4) = 50 L/dk'),A('Kalan su','8. dakikada depoda 200 L var.','200 ÷ 50 = 4 dakika daha'),A('Toplam süre','Grafiğin bitişine kalan süreyi ekle.','8 + 4 = 12 dakika')],
 'Azalan doğrunun eğimi boşalma hızıdır; kalan miktarı bu hıza bölerek ek süreyi bul.',SK)

# ---------- 11 orta · öncüllü sütun (doğrular)
yil=['2018','2019','2020','2021','2022','2023']; dg=[20,30,50,40,60,50]
def onc(v):
    I=v.index(max(v))==4 and v.count(max(v))==1
    II=v[3]>v[2]
    III=v[0]+v[1]==v[2]
    return (I,II,III)
ad_={(True,False,False):'Yalnız I',(False,True,False):'Yalnız II',(True,True,False):'I ve II',(True,False,True):'I ve III',(True,True,True):'I, II ve III'}
assert onc(dg)==(True,False,True) and ad_[onc(dg)]=='I ve III'
assert ad_[onc([20,50,50,40,60,50])]=='Yalnız I'      # III'te 2019 yerine 2020 okunmuş
assert ad_[onc(dg[::-1])]=='Yalnız II'                 # ters sırayla okuma
assert ad_[onc([20,30,40,50,60,50])]=='I ve II'        # 2020 ve 2021 yer değiştirmiş
assert ad_[onc([20,30,50,55,60,50])]=='I, II ve III'   # 2021 sütunu 2020’den uzun sanılmış
sira=['Yalnız I','Yalnız II','I ve II','I ve III','I, II ve III']
SK=tek(sutun(yil,dg,10,60,'Fidan sayısı (bin)','Yıllar'))
M('0011','grb-oncullu','orta','Grafik İfadeleri','Sütun grafiğinden değerleri okuyup üç ifadeyi ayrı ayrı sınar.','öncüllü','K-GRB-06 (öncüllü, doğru ifadeler) · fidan dikim grafiği',
 'Bir orman işletmesinin 2018–2023 yıllarında diktiği fidan sayıları (bin) aşağıdaki sütun grafiğinde gösterilmiştir.\nBu grafiğe göre,\nI. En fazla fidan 2022 yılında dikilmiştir.\nII. 2021 yılında dikilen fidan sayısı, 2020 yılında dikilenden fazladır.\nIII. 2018 ve 2019 yıllarında dikilen fidanların toplamı, 2020 yılında dikilenlere eşittir.\nifadelerinden hangileri doğrudur?',
 'I ve III',[('Yalnız I','III’te 2019 yerine 2020 sütununu okuyup 2018 + 2020 = 70 ≠ 50 bulmuş; III’ü yanlış sanmış, I’i doğru, II’yi yanlış bulmuş.','dikkat'),('Yalnız II','Sütunları ters sırayla (2023’ten 2018’e) okumuş; bu durumda I yanlış, II doğru, III yanlış çıkmış.','dikkat'),('I ve II','2020 ve 2021 sütunlarının değerlerini yer değiştirerek okumuş (2020: 40, 2021: 50); II doğru, III yanlış çıkmış.','dikkat'),('I, II ve III','II’yi değerlendirirken 2021 sütununu 2020’den uzun sanmış; I ve III’ü doğru bulmuş.','dikkat')],
 'Doğru olan ifadelerin hangileri olduğu.',
 'Her ifadeyi, ilgili sütunların değerlerini ayrı ayrı okuyarak sına.',[SOK],
 [A('Değerleri oku','2018–2023 sütunları.','20 · 30 · 50 · 40 · 60 · 50'),A('I ve II','En yüksek sütun 60 ile 2022’dedir. 2021: 40, 2020: 50 olduğundan fazla değil, azalmıştır.','I doğru · II yanlış'),A('III','2018 + 2019 toplamı.','20 + 30 = 50 = 2020 ⇒ III doğru')],
 'Öncüllü sorularda her ifadeyi grafikteki değerlerle tek tek sına; “doğru” mu “yanlış” mı istendiğini soru kökünde işaretle.',SK,sira=sira)

# ---------- 12 orta · eksik sütun, ortalama
et=['Pzt','Sal','Çar','Per','Cum']; dg=[40,60,None,50,70]; ortv=50
bil=[x for x in dg if x is not None]; x=ortv*5-sum(bil)
assert x==30 and sum(bil)==220 and Fr(sum(bil),4)==55 and ortv*5==250 and 0<x<=80
SK=tek(sutun_h(et,dg,10,80,'Üye sayısı','Günler'))
M('0012','grb-sutun','orta','Eksik Sütun ve Ortalama','Ortalamadan toplamı bulup grafikte gösterilmeyen sütunun değerini hesaplar.','grafik','K-GRB-01 (sütun grafiği, ortalama, eksik değer) · spor salonu girişleri',
 'Bir spor salonuna hafta içi beş gün boyunca her gün giren üye sayıları aşağıdaki sütun grafiğinde gösterilmiştir. Çarşamba günü giren üye sayısı grafikte gösterilmemiş, “?” ile belirtilmiştir. Beş günde günlük ortalama 50 üye girmiştir.\nBuna göre çarşamba günü kaç üye girmiştir?',
 30,[(50,'Ortalamayı (50) doğrudan eksik sütunun değeri sanmış.','dikkat'),(55,'Bilinen dört sütunun ortalamasını (220 ÷ 4) bulup eksik değeri o sanmış.','bilgi'),(220,'Bilinen dört sütunun toplamını cevap sanmış.','islem'),(250,'Beş günün toplamını (50 × 5) bulup bilinen sütunları çıkarmamış.','islem')],
 'Çarşamba günü giren üye sayısı.',
 'Ortalamadan beş günün toplamını bul, bilinen dört gün toplamıyla karşılaştır.',[SOK,ORT],
 [A('Beş günün toplamı','Toplam = ortalama × gün sayısı.','50 × 5 = 250'),A('Bilinen dört gün','Sütunları oku ve topla.','40 + 60 + 50 + 70 = 220'),A('Eksik sütun','Toplamdan çıkar.','250 − 220 = 30')],
 'Eksik değer sorularında önce toplamı (ortalama × adet) bul, sonra bilinen değerlerin toplamını çıkar.',SK)

# ---------- 13 orta · sütun + tablo (çiçekçi)
cic=['Gül','Lale','Papatya','Orkide']; adet=[40,60,80,20]; fiy=[25,15,10,50]; gel=[a*f for a,f in zip(adet,fiy)]
assert gel==[1000,900,800,1000]
bas=['Çiçek','Tanesi (TL)','Gelir (TL)']; sat=[['Gül','?','1000'],['Lale','15','900'],['Papatya','10','800'],['Orkide','?','1000']]
assert Fr(900,60)==15 and Fr(800,80)==10 and Fr(1000,adet[0])==25 and Fr(1000,adet[3])==50
SK=alt_alta(('Şekil 1 · Satılan çiçek sayısı',sutun(cic,adet,20,80,'Adet','Çiçek türü')),('Şekil 2 · Satış tablosu',tablo(bas,sat,[90,100,100])))
assert 50-25==25 and 40-20==20 and Fr(50,25)==2 and 25+50==75
M('0013','grb-iki','orta','Sütun Grafiği ve Tablo','Sütun grafiğindeki adetlerle tablodaki gelirlerden birim fiyatları bulur.','grafik','K-GRB-04 (sütun grafiği + tablo, gelir = fiyat × adet) · çiçekçi',
 'Bir çiçekçide bir günde satılan dört çiçek türünün adetleri Şekil 1’deki sütun grafiğinde, bu çiçeklerin bir tanesinin satış fiyatı ve elde edilen gelir Şekil 2’deki tabloda verilmiştir. Tabloda gül ve orkide için tanesinin fiyatı belirtilmemiştir.\nBuna göre orkidenin tanesi, gülün tanesinden kaç TL pahalıdır?',
 25,[(2,'İki fiyatın farkı yerine oranını (50 ÷ 25) bulmuş.','dikkat'),(20,'Fiyat farkı yerine satış adetlerinin farkını (40 − 20) almış.','bilgi'),(50,'Fark yerine orkidenin fiyatını vermiş.','dikkat'),(75,'Farkı almak yerine iki fiyatı toplamış (25 + 50).','islem')],
 'Orkide ile gülün birim fiyatları arasındaki fark (TL).',
 'Fiyatı, gelirin adede bölünmesiyle bulabilirsin.',[SOK,GEL],
 [A('Adetleri oku','Şekil 1’den gül ve orkide.','gül: 40 · orkide: 20'),A('Fiyatları bul','Fiyat = gelir ÷ adet.','gül: 1000 ÷ 40 = 25 TL · orkide: 1000 ÷ 20 = 50 TL'),A('Farkı al','Orkide − gül.','50 − 25 = 25 TL')],
 'Tabloda birim fiyat eksikse, gelirini grafikteki adede bölerek bul.',SK)

# ---------- 14 orta · çizgi iki makine
et=['Pzt','Sal','Çar','Per','Cum','Cmt']; X=[40,50,60,50,70,80]; Yv=[30,60,40,70,50,60]
gn=[i for i in range(6) if X[i]>Yv[i]]; assert gn==[0,2,4,5]
sx=sum(X[i] for i in gn); sy=sum(Yv[i] for i in gn); assert sx==250 and sy==180 and sx-sy==70
assert sum(X)-sum(Yv)==40 and sum(abs(a-b) for a,b in zip(X,Yv))==100 and max(abs(a-b) for a,b in zip(X,Yv))==20
SK=tek(cizgi_n(et,[('X makinesi',X),('Y makinesi',Yv)],10,80,'Üretim (adet)','Günler'))
M('0014','grb-cizgi','orta','İki Çizgi Grafiği','İki çizgi grafiğini karşılaştırıp koşulu sağlayan günlerdeki üretim farkını bulur.','grafik','K-GRB-02 (iki seri çizgi, koşullu fark) · iki makinenin günlük üretimi',
 'Bir fabrikadaki X ve Y makinelerinin bir haftanın altı gününde ürettiği parça sayıları aşağıdaki çizgi grafiğinde gösterilmiştir.\nBuna göre X makinesinin Y makinesinden daha fazla parça ürettiği günlerde, X makinesinin toplam üretimi Y makinesinin toplam üretiminden kaç parça fazladır?',
 70,[(20,'Tek bir günün (en büyük günlük fark) değerini vermiş.','dikkat'),(40,'Altı günün tamamında X ile Y’nin toplamlarının farkını (350 − 310) almış; koşulu uygulamamış.','bilgi'),(100,'Tüm günlerin farklarını mutlak değerce toplamış.','bilgi'),(250,'Fark yerine X makinesinin o günlerdeki toplamını vermiş.','islem')],
 'Koşulu sağlayan günlerde X’in üretimi ile Y’nin üretiminin toplamları arasındaki fark.',
 'Önce hangi günlerde X’in Y’nin üstünde olduğunu belirle.',[CIZ],
 [A('Koşulu sağlayan günler','X, Y’den fazla: Pazartesi, Çarşamba, Cuma, Cumartesi.','4 gün'),A('Toplamlar','Bu günlerde X ve Y.','X: 40 + 60 + 70 + 80 = 250 · Y: 30 + 40 + 50 + 60 = 180'),A('Fark','X toplamı − Y toplamı.','250 − 180 = 70')],
 'İki çizginin karşılaştırıldığı koşullu sorularda önce koşulu sağlayan günleri işaretle, toplamı yalnızca onlar üzerinden al.',SK)

# ---------- 15 orta · daire x
N=36000; dl=[('Kira',120,'120°'),('Market',90,'3x'),('Fatura',60,'2x'),('Eğitim',30,'x'),('Tasarruf',60,'60°')]
xx=Fr(360-120-60,6); assert xx==30 and 3*xx==90 and 2*xx==60 and sum(d for _,d,_ in dl)==360
t=lambda a:Fr(N*a,360); assert t(60)==6000 and t(30)==3000 and t(90)==9000 and t(120)==12000
x_yanl=Fr(360-120,6); assert x_yanl==40 and t(2*x_yanl)==8000
SK=tek(daire_e(dl,H=200))
M('0015','grb-daire','orta','Daire Grafiğinde Bilinmeyen','Daire diliminin açısı bilinmeyen (x cinsinden) olduğunda x’i bulup tutarı hesaplar.','grafik','K-GRB-03 (daire grafiği, x’li açılar) · aile bütçesi',
 'Aylık geliri 36 000 TL olan bir ailenin gelirinin harcama türlerine göre dağılımı aşağıdaki daire grafiğinde gösterilmiştir. Gelirin tamamı bu beş türe ayrılmıştır; bazı dilimlerin merkez açıları x cinsinden verilmiştir.\nBuna göre bu aile faturalara aylık kaç TL ayırmaktadır?',
 6000,[(3000,'x’i (30°) bulmuş ama fatura diliminin 2x olduğunu atlayıp x’e karşılık gelen tutarı vermiş.','dikkat'),(8000,'Denklemi kurarken 60°’lik tasarruf dilimini unutup 6x = 240 ⇒ x = 40 bulmuş; fatura 80° ⇒ 8000.','bilgi'),(9000,'Fatura yerine market diliminin (3x = 90°) tutarını vermiş.','dikkat'),(12000,'Fatura yerine kira diliminin (120°) tutarını vermiş.','dikkat')],
 'Faturalara ayrılan aylık tutar (TL).',
 'Tüm açıların toplamı 360° olmalı; önce x’i bul.',[DAI,DER],
 [A('Denklemi kur','Açılar toplamı 360°.','120 + 3x + 2x + x + 60 = 360 ⇒ 6x = 180 ⇒ x = 30'),A('Fatura açısı','Fatura diliminin açısı 2x.','2 × 30 = 60°'),A('Tutarı bul','Gelir × açı ÷ 360.','36 000 × 60 ÷ 360 = 6 000 TL')],
 'Açılardan biri x cinsinden verilmişse önce tam daire için denklem kurup x’i bul; sonra istenen dilimin tutarını hesapla.',SK)

# ---------- 16 orta · gruplu sütun yüzde değişim
et=['Erik','Kayısı','Üzüm','İncir']; a22=[40,20,50,30]; a23=[55,30,40,35]
pc=[Fr(b-a,a)*100 for a,b in zip(a22,a23)]; assert pc==[Fr(75,2),50,-20,Fr(50,3)] and max(pc)==50 and pc.index(50)==1
assert max(b-a for a,b in zip(a22,a23))==15 and 30-20==10 and a23[1]==30
SK=tek(sutun_g(et,[('2022',a22),('2023',a23)],5,60,'İhracat (bin ton)','Ürünler'))
M('0016','grb-donusum','orta','Gruplu Sütunda Yüzde','Gruplu sütun grafiğinde iki yıl arasındaki yüzde değişimi hesaplar ve en büyüğünü belirler.','grafik','K-GRB-07 (gruplu sütun, yüzde değişim) · kuru meyve ihracatı',
 'Dört kuru meyve ürününün 2022 ve 2023 yıllarındaki ihracat miktarları (bin ton) aşağıdaki grafikte gösterilmiştir.\nBuna göre 2022’den 2023’e ihracat miktarı yüzde olarak en çok artan ürünün artış yüzdesi kaçtır?',
 50,[(10,'Yüzde yerine kayısının miktar artışını (30 − 20) vermiş.','dikkat'),(15,'Miktar olarak en çok artan ürünün (erik) artışını yüzde sanmış.','bilgi'),(Fr(75,2),'Miktar olarak en çok artan ürünü (erik) seçip onun yüzde artışını (15 ÷ 40) hesaplamış.','bilgi'),(30,'Yüzde yerine kayısının 2023’teki ihracat miktarını (30 bin ton) vermiş.','dikkat')],
 'Yüzde olarak en çok artan ürünün artış yüzdesi.',
 'Her ürün için artışı, 2022 değerine böl.',[SOK,DEG],
 [A('Değerleri oku','2022 ve 2023 sütunları.','2022: 40 · 20 · 50 · 30 — 2023: 55 · 30 · 40 · 35'),A('Yüzde değişimler','(2023 − 2022) ÷ 2022 × 100.','erik %37,5 · kayısı %50 · üzüm −%20 · incir %16,7'),A('En büyüğü','Kayısı.','%50')],
 'En çok artan ürün ile yüzde olarak en çok artan ürün farklı olabilir; yüzdeyi eski değere göre hesapla.',SK)

# ---------- 17 orta · tablo → sütun ölçeği
ay_=['Mart','Nisan','Mayıs','Haziran']; tk_=[36,60,24,48]; cm=Fr(15)
assert [cm*v/max(tk_) for v in tk_]==[9,15,6,12] and cm*min(tk_)/max(tk_)==6
SK=tablo_svg(['Ay','Takipçi sayısı (bin)'],[[a,str(b)] for a,b in zip(ay_,tk_)])
M('0017','grb-donusum','orta','Tablodan Sütun Grafiğine','Tablodaki sayıları orantılı uzunluklara çevirerek sütun grafiği çizimini yorumlar.','tablo','K-GRB-07 (tablodan sütun grafiğine, ölçek) · takipçi sayıları',
 'Bir sosyal medya hesabının mart–haziran aylarındaki takipçi sayıları (bin kişi) aşağıdaki tabloda verilmiştir.\nBu veriler sütun grafiğiyle gösterilirken sütun yükseklikleri takipçi sayılarıyla doğru orantılı alınacak ve en yüksek sütun 15 cm olacaktır.\nBuna göre en kısa sütunun yüksekliği kaç cm olur?',
 6,[(9,'En kısa sütun yerine mart sütununu (36 bin) hesaplamış.','dikkat'),(12,'En kısa sütun yerine haziran sütununu (48 bin) hesaplamış.','dikkat'),(15,'En yüksek sütunun yüksekliğini cevap sanmış.','dikkat'),(24,'Takipçi sayısını (24 bin) doğrudan cm olarak yazmış.','bilgi')],
 'En kısa sütunun yüksekliği (cm).',
 'Sütun yüksekliği ile sayı arasındaki oran sabittir; en büyük sayıya 15 cm düşüyor.',[B('Doğru orantı','biri kaç katına çıkarsa diğeri de o kadar katına çıkar. Örnek: 40’a 10 cm düşüyorsa 20’ye 5 cm düşer')],
 [A('En yüksek sütun','En büyük takipçi sayısı nisan: 60.','60 bin ↔ 15 cm'),A('Bir birimin uzunluğu','15 cm’yi 60’a böl.','15 ÷ 60 = 0,25 cm'),A('En kısa sütun','En küçük sayı mayıs: 24.','24 × 0,25 = 6 cm')],
 'Ölçekli çizimde her sütunun uzunluğu, en büyük sütunla sayıların oranı kadardır.',SK)

# ---------- 18 zor · daire + sütun (vardiya)
dl=[('Sabah',160),('Öğle',120),('Gece',80)]; N=90; isc={a:Fr(N*d,360) for a,d in dl}; assert isc=={'Sabah':40,'Öğle':30,'Gece':20}
uret={'Sabah':1000,'Öğle':900,'Gece':200}; kb={a:Fr(uret[a],isc[a]) for a in uret}; assert kb=={'Sabah':25,'Öğle':30,'Gece':10}
dig=Fr(uret['Sabah']+uret['Gece'],isc['Sabah']+isc['Gece']); assert dig==20 and kb['Öğle']-dig==10
assert kb['Öğle']-kb['Sabah']==5 and kb['Öğle']-Fr(kb['Sabah']+kb['Gece'],2)==Fr(25,2)
SK=alt_alta(('Şekil 1 · İşçilerin vardiyalara dağılımı',daire(dl,H=176,r=62)),('Şekil 2 · Vardiyalarda üretilen toplam parça',sutun(['Sabah','Öğle','Gece'],[uret[a] for a in uret],100,1000,'Parça sayısı','Vardiya')))
M('0018','grb-iki','zor','Daire ve Sütun Grafiği','Daire grafiğinden işçi sayılarını, sütun grafiğinden üretimi okuyup ağırlıklı işçi başına üretimi karşılaştırır.','grafik','K-GRB-04 (daire + sütun, işçi başına üretim) · fabrika vardiyaları',
 'Bir fabrikada toplam 90 işçi çalışmaktadır. İşçilerin sabah, öğle ve gece vardiyalarına göre dağılımı Şekil 1’deki daire grafiğinde, her vardiyanın bir günde ürettiği toplam parça sayısı Şekil 2’deki sütun grafiğinde gösterilmiştir. Aynı vardiyadaki işçilerin her birinin ürettiği parça sayısı eşittir.\nBuna göre öğle vardiyasındaki bir işçinin ürettiği parça sayısı, sabah ve gece vardiyalarındaki tüm işçilerin işçi başına ortalama ürettiği parça sayısından kaç fazladır?',
 10,[(5,'Karşılaştırmayı yalnız sabah vardiyasıyla (30 − 25) yapmış; gece vardiyasını katmamış.','dikkat'),(Fr(25,2),'Sabah ve gece vardiyalarının işçi başına üretimlerinin aritmetik ortalamasını (25 + 10) ÷ 2 almış; işçi sayılarını ağırlık olarak katmamış.','bilgi'),(20,'Fark yerine sabah ve gece işçilerinin işçi başına ortalama üretimini (1200 ÷ 60) vermiş.','dikkat'),(30,'Fark yerine öğle vardiyasındaki bir işçinin üretimini (900 ÷ 30) vermiş.','dikkat')],
 'Öğle vardiyasında işçi başına üretim ile sabah+gece işçileri başına ortalama üretim arasındaki fark.',
 'Daire grafiğinden her vardiyadaki işçi sayısını, sütun grafiğinden toplam üretimi bul.',[DAI,B('Birim başına ortalama','toplam üretim ÷ toplam işçi. Örnek: 2 işçi 40, 3 işçi 90 parça üretirse 5 işçinin işçi başına ortalaması 130 ÷ 5 = 26')],
 [A('İşçi sayıları','90 işçi 360°’ye karşılık gelir; her derece 1/4 işçi.','sabah: 160° → 40 · öğle: 120° → 30 · gece: 80° → 20'),A('Üretimleri oku','Şekil 2’den.','sabah: 1000 · öğle: 900 · gece: 200'),A('Öğle vardiyası','İşçi başına üretim.','900 ÷ 30 = 30'),A('Sabah + gece','Toplam üretim ÷ toplam işçi.','(1000 + 200) ÷ (40 + 20) = 20'),A('Fark','Öğle − (sabah + gece ortalaması).','30 − 20 = 10')],
 'Gruplar birleştirilince ortalama, ortalamaların ortalaması değil, toplam üretimin toplam işçiye bölümüdür.',SK)

# ---------- 19 zor · öncüllü iki çizgi, yanlış olanlar
et=['Eki','Kas','Ara','Oca','Şub']; Kz=[30,45,60,45,75]; Gz=[45,30,60,75,60]
I_=sum(Gz)>sum(Kz); II_=(Gz[3]-Gz[1])*100==Gz[1]*250; III_=all(g>k for g,k in zip(Gz,Kz))
assert sum(Kz)==255 and sum(Gz)==270 and I_ and not II_ and not III_ and Fr((Gz[3]-Gz[1])*100,Gz[1])==150 and Fr(Gz[3]*100,Gz[1])==250 and Gz[1]<Kz[1]
sira=['Yalnız II','Yalnız III','I ve II','II ve III','I, II ve III']
SK=tek(cizgi_n(et,[('Kuzey',Kz),('Güney',Gz)],15,90,'Ziyaretçi (yüz kişi)','Aylar'))
M('0019','grb-oncullu','zor','Yanlış İfadeleri Bulma','İki çizgi grafiğinden toplam, yüzde artış ve karşılaştırma ifadelerini sınayıp yanlış olanları belirler.','öncüllü','K-GRB-06 (öncüllü, yanlış ifadeler) · iki kafenin ziyaretçi grafiği',
 'Kuzey ve Güney adlı iki kafenin ekim–şubat aylarındaki aylık ziyaretçi sayıları (yüz kişi) aşağıdaki çizgi grafiğinde gösterilmiştir.\nBu grafiğe göre,\nI. Beş ayda Güney kafeyi ziyaret edenlerin toplamı, Kuzey kafeyi ziyaret edenlerin toplamından fazladır.\nII. Güney kafenin ziyaretçi sayısı, kasım ayına göre ocak ayında %250 artmıştır.\nIII. Her ay Güney kafenin ziyaretçi sayısı, Kuzey kafeninkinden fazladır.\nifadelerinden hangileri yanlıştır?',
 'II ve III',[('Yalnız II','I’i doğru bulmuş. III’ü doğru sanmış: kasımda Güney’in Kuzey’den fazla olduğunu düşünüp iki çizgiyi o ayda karıştırmış. II’yi yanlış bulmuş.','dikkat'),('Yalnız III','II’yi doğru sanmış: 75 ÷ 30 = 2,5 oranını artış yüzdesi (%250) almış; artışı (45) eski değere bölmemiş. I’i doğru, III’ü yanlış bulmuş.','islem'),('I ve II','I’i yanlış sanmış: şubattaki büyük Kuzey değerine (75) bakıp toplamı hesaplamadan Kuzey’in fazla olduğunu düşünmüş. II’yi yanlış bulmuş; III’ü doğru sanmış.','dikkat'),('I, II ve III','I’i yanlış sanmış: Kuzey ile Güney çizgilerini birbirine karıştırıp toplamları ters okumuş (Kuzey 270, Güney 255); II ve III’ü de yanlış bulmuş.','islem')],
 'Yanlış olan ifadelerin hangileri olduğu.',
 'Her ifadeyi ayrı ayrı sına; toplamlar için beş ayın değerlerini topla.',[CIZ,DEG],
 [A('Değerleri oku','Kuzey ve Güney.','Kuzey: 30 · 45 · 60 · 45 · 75 — Güney: 45 · 30 · 60 · 75 · 60'),A('I','Toplamlar.','Kuzey: 255 · Güney: 270 ⇒ I doğru'),A('II','Güney: kasım 30, ocak 75.','(75 − 30) ÷ 30 = %150 ⇒ %250 değil, II yanlış'),A('III','Kasımda Güney 30, Kuzey 45; aralıkta eşitler.','Güney her ay fazla değil ⇒ III yanlış')],
 'Yanlış ifadeler sorulduğunda her ifadenin doğru mu yanlış mı olduğunu ayrı belirle; sonra yalnızca yanlışları işaretle.',SK,sira=sira)

# ---------- 20 zor · yol-zaman ortalama hız
pts=[(0,0),(2,60),(3,60),(5,150)]
v_son=Fr(150-60,5-3); ortv=Fr(150,5); assert v_son==45 and ortv==30 and v_son-ortv==15
assert Fr(150,4)==Fr(75,2) and v_son-Fr(150,4)==Fr(15,2) and v_son-Fr(30+0+45,3)==20 and Fr(60,2)==30
SK=tek(dogrusal([('Bisikletli',pts)],5,1,150,30,'Süre (saat)','Yol (km)'))
M('0020','grb-dogrusal','zor','Ortalama Hız','Parçalı yol–zaman grafiğinde duraklamayı da kapsayan ortalama hızı bulup son bölümdeki hızla karşılaştırır.','grafik','K-GRB-05 (yol–zaman, ortalama hız) · duraklamalı bisiklet yolculuğu',
 'Bir bisikletlinin bir yolculuğu sırasında aldığı yolun zamana göre değişimi aşağıdaki grafikte gösterilmiştir. Bisikletli, grafikteki her bölümde sabit hızla gitmiş, bir bölümde ise dinlenmek için durmuştur.\nBuna göre bisikletlinin son bölümdeki hızı, bu yolculuk boyunca (dinlenme süresi dahil) ortalama hızından kaç km/sa fazladır?',
 15,[(Fr(15,2),'Ortalama hızı bulurken dinlenme süresini (1 saat) toplam süreden çıkarmış (150 ÷ 4 = 37,5).','dikkat'),(20,'Ortalama hızı üç bölümün hızlarının aritmetik ortalaması olarak almış: (30 + 0 + 45) ÷ 3 = 25.','bilgi'),(30,'Fark yerine yolculuğun ortalama hızını (150 ÷ 5) vermiş.','dikkat'),(45,'Fark yerine son bölümdeki hızı vermiş.','dikkat')],
 'Son bölümdeki hız ile ortalama hız arasındaki fark (km/sa).',
 'Her bölümün hızını eğiminden bul; ortalama hız hesabında hangi süreyi kullanacağına dikkat et.',[HIZ,ORH],
 [A('Son bölümün hızı','3. saatte 60 km, 5. saatte 150 km.','(150 − 60) ÷ (5 − 3) = 45 km/sa'),A('Toplam yol ve süre','Dinlenme dahil 5 saatte 150 km.','150 km · 5 saat'),A('Ortalama hız','Toplam yol ÷ toplam süre.','150 ÷ 5 = 30 km/sa'),A('Fark','Son bölüm hızı − ortalama hız.','45 − 30 = 15 km/sa')],
 'Ortalama hız hesabında duraklama süresi de toplam süreye katılır; hızların aritmetik ortalaması ortalama hız değildir.',SK)

# ---------- 21 zor · depo iki musluk
pts=[(0,0),(2,200),(6,800)]; ha=Fr(200,2); hab=Fr(800-200,6-2); hb=hab-ha
assert ha==100 and hab==150 and hb==50 and Fr(800,hb)==16 and Fr(800,ha)==8 and Fr(600,hb)==12
SK=tek(dogrusal([('Su',pts)],6,1,800,100,'Süre (dakika)','Su miktarı (L)',yatay=[(800,'Kapasite: 800 L')]))
M('0021','grb-dogrusal','zor','İki Musluk','Parçalı depo–zaman grafiğinden iki musluğun birlikte açıkken ve tek başına akış hızlarını ayırıp bir musluğun doldurma süresini bulur.','grafik','K-GRB-05 (depo–zaman, iki musluk) · A ve B muslukları',
 'Kapasitesi 800 L olan boş bir depoyu doldurmak için önce yalnız A musluğu açılmış, 2. dakikada A açık kalırken B musluğu da açılmıştır. Muslukların akış hızları sabittir ve depodaki su miktarının zamana göre değişimi aşağıdaki grafikte gösterilmiştir; depo 6. dakikada dolmuştur.\nBuna göre aynı boş depoyu yalnız B musluğu kaç dakikada doldurur?',
 16,[(6,'Grafikteki dolma anını (6. dakika) B’nin tek başına doldurma süresi sanmış.','dikkat'),(8,'B’yi A sanmış: yalnız A’nın hızıyla (100 L/dk) doldurma süresini (800 ÷ 100) bulmuş.','dikkat'),(12,'B’nin hızını doğru (50 L/dk) bulmuş ama depoyu 800 yerine 2. dakikadan sonra dolan 600 L sanıp 600 ÷ 50 almış.','dikkat'),(50,'B’nin hızını (50 L/dk) bulup depoyu bu hıza bölmeden süre yerine hızı vermiş.','islem')],
 'Yalnız B musluğunun boş depoyu doldurma süresi (dakika).',
 'Önce yalnız A açıkken, sonra A ile B birlikte açıkken akış hızını grafikten bul.',[AKI],
 [A('A’nın hızı','İlk 2 dakikada 200 L.','200 ÷ 2 = 100 L/dk'),A('A + B’nin hızı','2. ile 6. dakika arasında 200 L → 800 L.','(800 − 200) ÷ 4 = 150 L/dk'),A('B’nin hızı','Birlikte − A.','150 − 100 = 50 L/dk'),A('B’nin doldurma süresi','Kapasite ÷ hız.','800 ÷ 50 = 16 dakika')],
 'Birlikte çalışan iki musluğun hızı toplamdır; birinin hızını grafikten bulup toplamdan çıkararak diğerinin hızına ulaş.',SK)

# ---------- 22 zor · sütun + çizgi (tiyatro geliri)
ay4=['Eki','Kas','Ara','Oca']; sey=[200,300,400,100]; fp=[60,50,70,80]
gl=[a*b for a,b in zip(sey,fp)]; assert gl==[12000,15000,28000,8000] and max(gl)-min(gl)==20000
assert (max(sey)-min(sey))*max(fp)==24000 and max(sey)*max(fp)==32000 and max(gl)==28000 and min(gl)==8000
SK=alt_alta(('Şekil 1 · Aylık seyirci sayısı',sutun(ay4,sey,100,400,'Seyirci','Aylar')),('Şekil 2 · Bilet fiyatı',cizgi(ay4,fp,10,80,'Fiyat (TL)','Aylar')))
M('0022','grb-iki','orta','Sütun ve Çizgi Grafiği','Sütun grafiğindeki seyirci sayısı ile çizgi grafiğindeki bilet fiyatını çarparak aylık gelirleri karşılaştırır.','grafik','K-GRB-04 (sütun + çizgi, gelir = fiyat × adet) · tiyatro',
 'Bir tiyatronun ekim–ocak aylarındaki aylık seyirci sayıları Şekil 1’deki sütun grafiğinde, o aylarda satılan biletlerin fiyatı Şekil 2’deki çizgi grafiğinde gösterilmiştir. Her ay tüm seyirciler o ayın bilet fiyatını ödemiştir.\nBuna göre bilet gelirinin en yüksek olduğu ay ile en düşük olduğu ay arasındaki gelir farkı kaç TL’dir?',
 20000,[(8000,'Fark yerine en düşük aylık geliri (ocak) vermiş.','dikkat'),(24000,'Seyirci farkını (400 − 100) en yüksek bilet fiyatıyla (80 TL) çarpmış.','bilgi'),(28000,'Fark yerine en yüksek aylık geliri (aralık) vermiş.','dikkat'),(32000,'En çok seyirciyi (400) en yüksek fiyatla (80) çarpıp en yüksek geliri öyle bulmuş.','bilgi')],
 'En yüksek ve en düşük aylık bilet gelirleri arasındaki fark (TL).',
 'Her ay için iki şekilden okuduğun değerleri çarp.',[SOK,GEL],
 [A('Aylık gelirler','Seyirci × bilet fiyatı.','ekim: 200 × 60 = 12 000 · kasım: 300 × 50 = 15 000 · aralık: 400 × 70 = 28 000 · ocak: 100 × 80 = 8 000'),A('En yüksek ve en düşük','Aralık ve ocak.','28 000 ve 8 000'),A('Fark','Çıkar.','28 000 − 8 000 = 20 000 TL')],
 'İki grafikten gelir hesaplanırken en çok seyirci ile en yüksek fiyat aynı ayda olmayabilir; her ay için ayrı çarp.',SK)

# ---------- 23 zor · iki daire grafiği
y22=[('Çocuk',90),('Genç',120),('Yetişkin',120),('Yaşlı',30)]; y23=[('Çocuk',144),('Genç',96),('Yetişkin',90),('Yaşlı',30)]
T22,T23=240,300; c22={a:Fr(T22*d,360) for a,d in y22}; c23={a:Fr(T23*d,360) for a,d in y23}
assert c22=={'Çocuk':60,'Genç':80,'Yetişkin':80,'Yaşlı':20} and c23=={'Çocuk':120,'Genç':80,'Yetişkin':75,'Yaşlı':25}
art=Fr(c23['Yaşlı']-c22['Yaşlı'],c22['Yaşlı'])*100; assert art==25 and 25-20==5 and Fr(25,20)*100==125 and 30-30==0
SK=alt_alta(('Şekil 1 · 2022 üyeleri (toplam 240)',daire(y22,H=170,r=56)),('Şekil 2 · 2023 üyeleri (toplam 300)',daire(y23,H=170,r=56)))
M('0023','grb-daire','orta','İki Daire Grafiği','İki farklı toplama ait daire grafiklerinde aynı açıya karşılık gelen sayıların farklı olduğunu görüp yüzde değişimi hesaplar.','grafik','K-GRB-03 (iki daire grafiği, yüzde değişim) · kütüphane üyeleri',
 'Bir ilçe kütüphanesinin üyelerinin yaş gruplarına göre dağılımı, 2022 yılı için Şekil 1’deki, 2023 yılı için Şekil 2’deki daire grafiğinde gösterilmiştir. Kütüphanenin üye sayısı 2022’de 240, 2023’te 300’dür.\nBuna göre yaşlı üye sayısı 2022’ye göre 2023’te yüzde kaç artmıştır?',
 25,[(0,'İki grafikte de yaşlı diliminin açısı 30° olduğu için sayının değişmediğini düşünmüş.','bilgi'),(5,'Yüzde yerine artış miktarını (25 − 20 = 5 kişi) vermiş.','dikkat'),(20,'Artış yüzdesi yerine 2022’deki yaşlı üye sayısını (20) vermiş.','dikkat'),(125,'Yeni sayının eskiye oranını (25 ÷ 20) artış yüzdesi sanmış.','islem')],
 'Yaşlı üye sayısındaki yüzde artış.',
 'Her yılın yaşlı üye sayısını ayrı ayrı bul.',[DAI,DEG],
 [A('2022’de yaşlılar','240 kişinin 30°’lik dilimi.','240 × 30 ÷ 360 = 20'),A('2023’te yaşlılar','300 kişinin 30°’lik dilimi.','300 × 30 ÷ 360 = 25'),A('Yüzde artış','(yeni − eski) ÷ eski × 100.','5 ÷ 20 = %25')],
 'Toplamları farklı iki daire grafiğinde dilim açılarını değil, her dilimin sayısını bularak karşılaştır.',SK)

# ---------- 24 zor · çizgi, iki bilinmeyen
et=['1.','2.','3.','4.','5.','6.']; nets=[10,15,None,None,25,30]; ortv=22
bil=sum(x for x in nets if x is not None); xy=ortv*6-bil; assert bil==80 and xy==52
y4=Fr(xy+10,2); x3=Fr(xy-10,2); assert y4==31 and x3==21 and y4-x3==10 and 0<x3<=40 and y4<=40
assert Fr(xy,2)==26
SK=tek(cizgi_n(et,[('Net',nets)],5,40,'Net','Deneme sırası'))
M('0024','grb-cizgi','zor','İki Bilinmeyenli Çizgi','Çizgi grafiğinde iki noktanın değeri gösterilmediğinde ortalama ve farktan yararlanarak noktaları bulur.','grafik','K-GRB-02 (çizgi grafiği, ortalama ve iki bilinmeyen) · deneme netleri',
 'Bir öğrencinin girdiği altı deneme sınavındaki matematik netleri aşağıdaki çizgi grafiğinde gösterilmiştir. Öğrencinin 3. ve 4. denemedeki netleri grafikte gösterilmemiş, “?” ile belirtilmiştir. Öğrencinin altı denemedeki net ortalaması 22’dir ve 4. denemedeki neti, 3. denemedeki netinden 10 fazladır.\nBuna göre öğrenci 4. denemede kaç net yapmıştır?',
 31,[(21,'3. denemenin netini (21) bulup 4. denemeyi 10 eklemeden vermiş.','dikkat'),(22,'Net ortalamasını (22) doğrudan 4. denemenin neti sanmış.','dikkat'),(26,'3. ve 4. denemelerin toplamını (52) ikiye bölüp iki denemeyi eşit saymış.','bilgi'),(10,'İki net arasındaki farkı (10) 4. denemenin neti sanmış.','dikkat')],
 '4. denemedeki net.',
 'Önce altı denemenin toplamından bilinen dört denemenin toplamını çıkararak iki bilinmeyenin toplamını bul.',[ORT],
 [A('Toplam net','Toplam = ortalama × deneme sayısı.','22 × 6 = 132'),A('Bilinen dört deneme','10 + 15 + 25 + 30.','80'),A('3. ve 4. toplamı','Toplamdan çıkar.','132 − 80 = 52'),A('Denklem','x + y = 52, y = x + 10.','2x + 10 = 52 ⇒ x = 21, y = 31')],
 'İki bilinmeyen, “toplamları” ve “farkları” verildiğinde, toplam ve farktan ikisi de bulunur: büyük = (toplam + fark) ÷ 2.',SK)

bitir(P,'grafikiki',UK)
