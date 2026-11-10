"""Hafif mod (tarih): her şıkka etiket, tek doğru şık assert; öncüllü sorularda doğru küme öncüllerden hesaplanır."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HV=os.path.join(HD,'..')
sys.path.insert(0,HV)
from ortak import *
from collections import Counter
KY='ÖSYM 2018–2026 TYT Tarih soru dağılım tablosu (örüntü) · MEB 9–11. sınıf tarih'
def O(m,c=None,t='bilgi'):
    """şık: doğruysa c=None; yanlışsa c = o şıkkı seçen öğrencinin hatası."""
    return (m,c is None,c or '',t if c else '')
class Konu:
    def __init__(s,onek,ad,k,n):
        s.onek=onek; s.ad=ad; s.k=k; s.n=n; s.kartlar={}; s.tipler={}
        s.P=Parti(onek,ad,k,ders='TYT Tarih',idon='tyttar')
    def kart(s,id,alt,fikir,tuzak,zorluk,kalip,adim,tipId,tip):
        s.kartlar[id]=dict(id=id,konu=s.ad,alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zorluk,kalip=kalip,adim=adim,tipId=tipId,tip=tip,kaynak=KY); s.tipler[tipId]=tip
    def S(s,no,kart,zor,kazanim,metin,opts,harf,istenen,ip,bilgi,adimlar,puf,not_):
        assert len(opts)==5 and len(set(o[0] for o in opts))==5,no
        ok=[i for i,o in enumerate(opts) if o[1]]
        assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
        c=s.kartlar[kart]; assert c['zorluk']==zor,(no,'zorluk')
        for o in opts:
            if not o[1]: assert len(o[2])>=12 and o[3] in TURLER,(no,o[0])
        assert len(adimlar)>=3 and isinstance(ip,str) and 1<=len(bilgi)<=3
        cel={'ABCDE'[i]:o[2] for i,o in enumerate(opts) if i!=ok[0]}; tur={'ABCDE'[i]:o[3] for i,o in enumerate(opts) if i!=ok[0]}
        s.P.R(no,c['tipId'],c['tip'],zor,c['alt'],kazanim,c['kalip'],c['adim'],f"{kart} ({c['alt']}) · {not_}",metin,[o[0] for o in opts],harf,istenen,[ip],bilgi,adimlar,puf,cel,tur)
    def Q(s,no,kart,zor,kazanim,metin,opts,harf,istenen,ip,bilgi,adim,*rest,islem_son=None):
        """adım listesi: 2 adım (başlık, açıklama, işlem) + otomatik son adım."""
        if len(rest)==3: son,puf,not_=rest
        else:
            puf,not_=rest; son='Her şık metne ve bilgiye göre tek tek kontrol edildi; yalnız '+harf+' şıkkı koşulu sağlar.'
        isl=islem_son or ' · '.join(f"{'ABCDE'[i]}: {'doğru cevap' if o[1] else 'elendi'}" for i,o in enumerate(opts))
        ad=[A(*x) for x in adim]+[A('Şıkları tek tek ele',son,isl)]
        s.S(no,kart,zor,kazanim,metin,opts,harf,istenen,ip,bilgi,ad,puf,not_)
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
    """stm: [(öncül metni, doğru_mu, gerekçe)]; secenekler: 5 küme metni; döner (opts, islem_son). Doğru küme = doğru öncüller."""
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
                i=R.index(fz[0]); out.append((t,False,f'{fz[0]}. öncül yanlıştır ({stm[i][2]}); ona doğru demiş.','bilgi'))
            else:
                i=R.index(eks[0]); out.append((t,False,f'{eks[0]}. öncül doğrudur ({stm[i][2]}); onu yanlış sanmış.','dikkat'))
    assert 'ABCDE'[[o[1] for o in out].index(True)]==harf
    return out,' · '.join(f"{R[i]}: {'doğru' if x[1] else 'yanlış'}" for i,x in enumerate(stm))
def metin_oncul(stm,kok):
    R=['I','II','III','IV','V']
    return '\n'.join(f'{R[i]}. {x[0]}' for i,x in enumerate(stm))+'\n'+kok
