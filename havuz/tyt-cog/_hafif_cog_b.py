"""Hafif mod (coğrafya B): her şıkka doğru/yanlış etiketi, tek doğru şık assert; öncüllü sorularda doğruluk kümesi hesaplanır."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV)
from ortak import *
import gorsel as G
from collections import Counter
KY='ÖSYM 2018–2026 TYT Coğrafya Nüfus/Göç/Bölgeler dağılımı (örüntü) · MEB 9–10. sınıf coğrafya'
class Konu:
    def __init__(s,onek,ad,k,n):
        s.onek=onek; s.ad=ad; s.k=k; s.n=n; s.kartlar={}; s.tipler={}
        s.P=Parti(onek,ad,k,ders='TYT Coğrafya',idon='tytcog')
    def kart(s,id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip):
        s.kartlar[id]=dict(id=id,konu=s.ad,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KY); s.tipler[tipId]=tip
    def S(s,no,kart,zor,kazanim,metin,opts,harf,istenen,ip,bilgi,adimlar,puf,not_,sekil=None,kalip=None,adim=None):
        """opts: 5 şık A–E sırasıyla (metin, doğru_mu, cel, tur)."""
        assert len(opts)==5 and len(set(o[0] for o in opts))==5,no
        ok=[i for i,o in enumerate(opts) if o[1]]
        assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
        c=s.kartlar[kart]; assert c['zorluk']==zor,(no,'zorluk')
        yan=[(o[0],o[2],o[3]) for i,o in enumerate(opts) if i!=ok[0]]
        for m,cl,t in yan: assert cl and len(cl)>=12 and t in TURLER,(no,m)
        assert len(adimlar)>=3 and isinstance(ip,str) and 1<=len(bilgi)<=3
        S_=[o[0] for o in opts]; sik=harf
        cel={ 'ABCDE'[i]:o[2] for i,o in enumerate(opts) if i!=ok[0]}; tur={'ABCDE'[i]:o[3] for i,o in enumerate(opts) if i!=ok[0]}
        s.P.R(no,c['tipId'],c['tip'],zor,c['alt'],kazanim,kalip or c['kalip'],adim or c['adim'],f"{kart} ({c['alt']}) · {not_}",metin,S_,sik,istenen,[ip],bilgi,adimlar,puf,cel,tur,sekil=sekil)
    def bitir(s):
        P=s.P
        for q in P.ANA: q['kardes']=None
        assert len(P.ANA)==s.n
        z=Counter(q['zorluk'] for q in P.ANA)
        assert dict(z)==(getattr(s,'zd',None) or ({'kolay':1,'orta':3,'zor':2} if s.n==6 else {'kolay':1,'orta':2,'zor':1})),z
        assert set(q['tipId'] for q in P.ANA)==set(s.tipler)
        tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in s.kartlar.items() if c['tipId']==t],uygulamaKonu=s.k) for t,ad in s.tipler.items()]
        json.dump(dict(konu=s.ad,surum=1,not_='Kart = fikir; soru metni içermez.',kartlar=list(s.kartlar.values()),tipler=tl),open(f'{HV}/kartlar/{s.onek}.json','w'),ensure_ascii=False,indent=1)
        P.yaz(f'{HD}/{s.onek}-1.json',f'/tmp/bos-{s.onek}.json')
def oncul(stm,secenekler,harf):
    """stm: [(öncül metni, doğru_mu, gerekçe)]; secenekler: 5 küme metni ('I ve III'); döner opts listesi. Doğru küme = doğru öncüller."""
    R=['I','II','III','IV','V']; dogru={R[i] for i,x in enumerate(stm) if x[1]}
    def kume(t):
        t=t.replace('Yalnız ','').replace(' ve ',', ').replace(' ',''); return set(t.split(','))
    out=[]
    for t in secenekler:
        K=kume(t)
        if K==dogru: out.append((t,True,'',''))
        else:
            eks=sorted(dogru-K,key=R.index); fz=sorted(K-dogru,key=R.index)
            if fz:
                i=R.index(fz[0]); cl=f'{fz[0]}. öncül yanlıştır ({stm[i][2]}); ona doğru demiş.'; tr='bilgi'
            else:
                i=R.index(eks[0]); cl=f'{eks[0]}. öncül doğrudur ({stm[i][2]}); onu yanlış sanmış.'; tr='dikkat'
            out.append((t,False,cl,tr))
    return out,dogru
def metin_oncul(giris,stm,kok):
    R=['I','II','III','IV','V']
    return giris+('\n' if giris else '')+'\n'.join(f'{R[i]}. {x[0]}' for i,x in enumerate(stm))+'\n'+kok
def T(x,y,s,**k): return G._t(x,y,s,**k)
def svg(w,h,b): return G._svg(w,h,b)
