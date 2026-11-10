"""Hafif mod yardımcıları (coğrafya, c grubu): her şıkka etiket, tek doğru şık assert."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HD,'..'))
from ortak import *
import gorsel as G
from collections import Counter
KART={}; TIPLER={}
def kart(id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip,kaynak):
    KART[id]=dict(id=id,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=kaynak)
    TIPLER[tipId]=tip
ROM=['I','II','III']
def ct(s):
    s=sorted(s,key=ROM.index)
    return f'Yalnız {s[0]}' if len(s)==1 else (' ve '.join(s) if len(s)==2 else 'I, II ve III')
def sirali(kumeler):
    return sorted(kumeler,key=lambda s:(len(s),[ROM.index(x) for x in sorted(s,key=ROM.index)]))
def onc_opts(dogru,kombolar,cel):
    """dogru: doğru küme; kombolar: 5 küme (biri doğru); cel: {küme_metni:(cel,tur)}"""
    ks=sirali([frozenset(k) for k in kombolar]); assert len(ks)==5 and frozenset(dogru) in ks
    return [(ct(k),k,None,None) if k==frozenset(dogru) else (ct(k),k,*cel[ct(k)]) for k in ks]
def Q(P,no,kid,zor,kazanim,kalip,adim,metin,opts,pred,istenen,ip,bilgi,adimlar,puf,yeni,sekil=None,harf=None,sirala=None):
    """opts: 5 şık (metin, etiket, cel, tur); doğru şıkta cel=None. pred(etiket)->bool tam bir şık için doğru olmalı."""
    assert len(opts)==5 and len(set(o[0] for o in opts))==5,no
    if sirala: opts=sorted(opts,key=lambda o:sirala(o[0]))
    ok=[i for i,o in enumerate(opts) if pred(o[1])]
    assert len(ok)==1,(no,ok)
    i=ok[0]; assert opts[i][2] is None
    L='ABCDE'; sik=L[i]
    if harf: assert sik==harf,(no,sik,harf)
    cel={};tur={}
    for j,o in enumerate(opts):
        if j!=i:
            assert o[2] and len(o[2])>=12 and o[3] in TURLER,(no,o[0]); cel[L[j]]=o[2]; tur[L[j]]=o[3]
    assert len(adimlar)>=3 and isinstance(ip,str) and len(bilgi)>=1
    c=KART[kid]
    P.R(no,c['tipId'],c['tip'],zor,c['alt'],kazanim,kalip,adim,f"{kid} ({c['alt']}) · {yeni}",metin,[o[0] for o in opts],sik,istenen,[ip],bilgi,adimlar,puf,cel,tur,sekil=sekil)
    return sik
def bitir(P,onek,k,konu_adi,zd=None):
    for q in P.ANA: q['kardes']=None
    P.yaz(os.path.join(HD,f'{onek}-1.json'),f'/tmp/bos-{onek}.json')
    kl=[dict(c,konu=konu_adi) for c in KART.values()]
    tl=[dict(tipId=t,ad=ad,kartlar=[x for x,c in KART.items() if c['tipId']==t],uygulamaKonu=k) for t,ad in TIPLER.items()]
    json.dump(dict(konu=konu_adi,surum=1,kartlar=kl,tipler=tl),open(os.path.join(HD,'..','kartlar',f'{onek}.json'),'w'),ensure_ascii=False,indent=1)
    assert len(P.ANA)==4
    z=Counter(q['zorluk'] for q in P.ANA); assert z==(zd or {'kolay':1,'orta':2,'zor':1}),z
    open(os.path.join(HD,f'{onek}-1.HAZIR'),'w').close()
def T(x,y,s,**k): return G._t(x,y,s,**k)
def svg(w,h,body): return G._svg(w,h,body)
