"""Çözüm adımı görselleri (SVG). Koordinatlar sorunun verilerinden hesaplanır.
Renk: çizgiler currentColor; vurgu style="fill:var(--acc,#16A34A)" (açık/koyu mod uyumlu)."""
from fractions import Fraction as Fr
ACC='var(--acc,#16A34A)'
def _svg(w,h,body): return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" font-family="Plus Jakarta Sans,system-ui,sans-serif" font-size="12" role="img">{body}</svg>'
def _t(x,y,s,anchor='middle',size=12,bold=False,renk=None):
    st=f'fill:{renk or "currentColor"};stroke:none'+(';font-weight:700' if bold else '')
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="{size}" style="{st}">{s}</text>'
def dizi_aralik(n,etiket,vurgu=None,sekil='direk'):
    """n nesne, uçlar dahil; aralıklar 1..n-1 numaralı. vurgu: 1'den başlayan sıra."""
    W,x0,x1,y=330,20,310,46; d=(x1-x0)/(n-1); b=[]
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke-width="1.5" opacity=".5"/>')
    for i in range(n-1):
        xa,xb=x0+i*d,x0+(i+1)*d
        b.append(f'<path d="M{xa+3:.1f} {y-14} Q{(xa+xb)/2:.1f} {y-30} {xb-3:.1f} {y-14}" stroke-width="1.2" style="stroke:{ACC}"/>')
        b.append(_t((xa+xb)/2,y-27,str(i+1),size=10,renk=ACC,bold=True))
    for i in range(n):
        x=x0+i*d; v=(vurgu==i+1)
        st=f'style="stroke:{ACC};fill:{ACC}"' if v else ''
        if sekil=='direk': b.append(f'<line x1="{x:.1f}" y1="{y-12}" x2="{x:.1f}" y2="{y+8}" stroke-width="{4 if v else 2.5}" stroke-linecap="round" {st}/>')
        else: b.append(f'<circle cx="{x:.1f}" cy="{y}" r="{5 if v else 4}" stroke-width="1.5" {st}/>')
    b.append(_t(W/2,y+30,etiket,size=12))
    return _svg(W,84,''.join(b))
def iki_sira(uzunluk,n1,k1,n2,k2,ad1,ad2,birim='m'):
    W,x0,x1=330,20,250; L=Fr(uzunluk); b=[]
    def X(v): return x0+float(Fr(v)/L)*(x1-x0)
    p1=L/(n1-1)*(k1-1); p2=L/(n2-1)*(k2-1)
    fmt=lambda v:(f'{float(v):.1f}'.replace('.',','))
    for n,k,ad,y,sh in [(n1,k1,ad1,40,'direk'),(n2,k2,ad2,86,'lamba')]:
        d=L/(n-1)
        b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke-width="1.2" opacity=".45"/>')
        for i in range(n):
            x=X(d*i); v=(i+1==k); st=f'style="stroke:{ACC};fill:{ACC}"' if v else ''
            if sh=='direk': b.append(f'<line x1="{x:.1f}" y1="{y-10}" x2="{x:.1f}" y2="{y+8}" stroke-width="{4 if v else 2.2}" stroke-linecap="round" {st}/>')
            else: b.append(f'<circle cx="{x:.1f}" cy="{y}" r="{5 if v else 3.5}" stroke-width="1.4" {st}/>')
        b.append(_t(x1+10,y+4,ad,anchor='start',size=11))
    xa,xb=X(p1),X(p2)
    b.append(_t(xa,22,f'{k1}. {ad1[:-3]} · {fmt(p1)} {birim}',size=11,bold=True,renk=ACC))
    b.append(_t(xb,112,f'{k2}. {ad2[:-3]} · {fmt(p2)} {birim}',size=11,bold=True,renk=ACC))
    for x in (xa,xb): b.append(f'<line x1="{x:.1f}" y1="50" x2="{x:.1f}" y2="78" stroke-dasharray="3 3" style="stroke:{ACC}"/>')
    b.append(f'<path d="M{xa:.1f} 64 H{xb:.1f}" stroke-width="2" style="stroke:{ACC}"/>')
    b.append(_t(max(xa,xb)+8,68,'fark '+fmt(abs(p2-p1))+' '+birim,anchor='start',size=11,bold=True))
    return _svg(W,124,''.join(b))
def gosterge_say(bas,bitis_etiket,aralik,ok_aralik):
    W,x0,step,y=330,22,30,50; b=[]
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x0+step*10}" y2="{y}" stroke-width="2"/>')
    for i in range(11):
        h=14 if i in (0,5,10) else 8
        b.append(f'<line x1="{x0+i*step}" y1="{y}" x2="{x0+i*step}" y2="{y-h}" stroke-width="2"/>')
    for i in range(ok_aralik):
        xa=x0+i*step; b.append(f'<path d="M{xa+3} {y-18} Q{xa+step/2} {y-32} {xa+step-3} {y-18}" stroke-width="1.2" style="stroke:{ACC}"/>')
        b.append(_t(xa+step/2,y-29,str(i+1),size=10,bold=True,renk=ACC))
    b.append(_t(x0,y+18,str(bas))); b.append(_t(x0+5*step,y+18,str(bitis_etiket)))
    px=x0+ok_aralik*step
    b.append(f'<path d="M{px} {y+4} L{px-6} {y+16} L{px+6} {y+16} Z" style="fill:#e53935;stroke:#e53935"/>')
    b.append(_t(px,y+32,f'{bas} + {ok_aralik} × {aralik} = {bas+ok_aralik*aralik}',size=11,bold=True,renk=ACC))
    return _svg(W,92,''.join(b))
def sayi_dogrusu(payda,isaretler,nokta,a=46,bt=53):
    """isaretler: [(pay_değeri(float), etiket)] ; nokta: (pay, etiket)"""
    W,x0,x1,y=330,20,310,40; b=[]
    X=lambda v:x0+(v-a)/(bt-a)*(x1-x0)
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke-width="1.5"/>')
    for v in range(a,bt+1): b.append(f'<line x1="{X(v):.1f}" y1="{y-4}" x2="{X(v):.1f}" y2="{y+4}" opacity=".5"/>'); b.append(_t(X(v),y+18,str(v),size=10))
    for v,et in isaretler:
        b.append(f'<line x1="{X(v):.1f}" y1="{y-14}" x2="{X(v):.1f}" y2="{y+6}" stroke-width="2"/>'); b.append(_t(X(v),y-18,et,size=11,bold=True))
    v,et=nokta; b.append(f'<circle cx="{X(v):.1f}" cy="{y}" r="5" style="fill:{ACC};stroke:{ACC}"/>'); b.append(_t(X(v),y+34,et,size=11,bold=True,renk=ACC))
    b.append(_t(W/2,y+50,f'paydalar {payda}',size=10))
    return _svg(W,98,''.join(b))
def tepsi(dilim,bolunen,parca,boyali):
    W,H,x0,y0,w,h=330,96,15,10,300,60; b=[]; d=w/dilim
    for i in range(dilim):
        x=x0+i*d
        if i<bolunen:
            pw=d/parca
            for j in range(parca):
                k=i*parca+j; fill=f'style="fill:{ACC};stroke:currentColor" fill-opacity=".85"' if k<boyali else ''
                b.append(f'<rect x="{x+j*pw:.1f}" y="{y0}" width="{pw:.1f}" height="{h}" stroke-width="1" {fill}/>')
        b.append(f'<rect x="{x:.1f}" y="{y0}" width="{d:.1f}" height="{h}" stroke-width="2"/>')
    b.append(_t(W/2,y0+h+20,f'1 parça = 1/{dilim*parca} · boyalı {boyali} parça',size=11,bold=True))
    return _svg(W,H,''.join(b))
def zaman_seridi(dilimler,an,etiket):
    """dilimler: [(süre, ad, renk)]"""
    W,x0,x1,y=330,15,315,28; T=sum(s for s,_,_ in dilimler); b=[]; t=0
    X=lambda v:x0+v/T*(x1-x0)
    for s,ad,r in dilimler:
        b.append(f'<rect x="{X(t):.1f}" y="{y}" width="{X(t+s)-X(t):.1f}" height="22" rx="3" style="fill:{r};stroke:none" fill-opacity=".85"/>')
        b.append(_t((X(t)+X(t+s))/2,y+15,ad,size=10,bold=True,renk='#fff'))
        b.append(_t(X(t),y+38,str(t),size=10)); t+=s
    b.append(_t(X(T),y+38,str(T),size=10))
    b.append(f'<path d="M{X(an):.1f} {y-2} L{X(an)-6:.1f} {y-14} L{X(an)+6:.1f} {y-14} Z" style="fill:currentColor"/>')
    b.append(_t(X(an),y-18,etiket,size=11,bold=True))
    return _svg(W,78,''.join(b))
def kutular(gruplar,vurgu):
    W,H=330,92; b=[]; bw=96; gap=(W-3*bw)/4
    for i,g in enumerate(gruplar):
        x=gap+i*(bw+gap); v=(vurgu in g)
        b.append(f'<rect x="{x:.1f}" y="18" width="{bw}" height="46" rx="10" stroke-width="{2.5 if v else 1.5}" {"style=%sstroke:%s%s" % (chr(34),ACC,chr(34)) if v else ""}/>')
        for j,c in enumerate(g):
            cx=x+16+j*32
            b.append(f'<rect x="{cx-12:.1f}" y="28" width="24" height="26" rx="4" stroke-width="1.2" {"style=%sfill:%s;stroke:%s%s" % (chr(34),ACC,ACC,chr(34)) if c==vurgu else ""}/>')
            b.append(_t(cx,46,str(c),size=13,bold=True,renk='#fff' if c==vurgu else None))
        b.append(_t(x+bw/2,82,'toplam '+str(sum(g)),size=11))
    return _svg(W,H,''.join(b))
def otopark(sutun,satir,kapali_sutun,gorunen_dolu,gizli_dolu):
    W,x0,y0,c=330,12,14,30; b=[]
    w=sutun*c; H=y0+satir*c+44
    g=0; gz=0
    for r in range(satir):
        for s in range(sutun):
            x,y=x0+s*c,y0+r*c; kap=s>=sutun-kapali_sutun
            if not kap:
                dolu=g<gorunen_dolu; g+=1
                b.append(f'<rect x="{x+2}" y="{y+2}" width="{c-4}" height="{c-4}" rx="4" stroke-width="1.2" {"style=%sfill:currentColor%s fill-opacity=%s.55%s" % (chr(34),chr(34),chr(34),chr(34)) if dolu else ""}/>')
            else:
                dolu=gz<gizli_dolu; gz+=1
                b.append(f'<rect x="{x+2}" y="{y+2}" width="{c-4}" height="{c-4}" rx="4" stroke-width="1.2" stroke-dasharray="3 2" {"style=%sfill:currentColor%s fill-opacity=%s.25%s" % (chr(34),chr(34),chr(34),chr(34)) if dolu else "style=%sstroke:%s%s" % (chr(34),ACC,chr(34))}/>')
    kx=x0+(sutun-kapali_sutun)*c
    b.append(f'<rect x="{kx-2}" y="{y0-4}" width="{kapali_sutun*c+4}" height="{satir*c+8}" rx="8" stroke-width="2" stroke-dasharray="6 4"/>')
    b.append(_t(kx+kapali_sutun*c/2,y0+satir*c+18,'kamyonun arkası',size=11,bold=True))
    b.append(_t(x0+(sutun-kapali_sutun)*c/2,y0+satir*c+18,f'görünen: {gorunen_dolu} dolu',size=11))
    b.append(_t(x0+w/2,y0+satir*c+36,f'arkada {gizli_dolu} dolu, {kapali_sutun*satir-gizli_dolu} boş (yeşil)',size=11,bold=True,renk=ACC))
    return _svg(W,H,''.join(b))
