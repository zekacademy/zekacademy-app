"""Hafif mod yardımcıları (dil bilgisi konuları): her şıkka etiket, tam bir şık koşulu sağlamalı."""
from tr_ortak import *
def kur(onek,konu_adi,k,kartlar,tipler):
    return Konu(onek,konu_adi,k,kartlar,tipler)
def soru(Q,no,kart,zor,kazanim,adim,metin,opts,harf,pred,istenen,ip,bilgi,adimlar,puf):
    """opts: 5 şık, A–E sırasıyla: (metin, etiket, cel, tur). pred(etiket)->bool; tam bir şık sağlamalı ve harf olmalı."""
    assert len(opts)==5
    ok=[i for i,o in enumerate(opts) if pred(o[1])]
    assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
    yan=[(o[0],o[2],o[3]) for i,o in enumerate(opts) if i!=ok[0]]
    for m,c,t in yan: assert c and len(c)>=12 and t in TURLER,(no,m)
    assert len(adimlar)>=3 and isinstance(ip,str)
    c=Q.kartlar[kart]; tipId=c['tipId']
    sk,h,cel,tur=sikla(opts[ok[0]][0],yan,harf)
    Q.P.R(no,tipId,Q.tipler[tipId],zor,c['alt'],kazanim,'düz',adim,f"{kart} ({c['alt']}) · özgün cümleler",metin,sk,h,istenen,[ip],bilgi,adimlar,puf,cel,tur)
def bitir(Q):
    for q in Q.P.ANA: q['kardes']=None
    o=Q.onek; kl=[]
    for kid,c in Q.kartlar.items():
        kl.append(dict(id=kid,konu=Q.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=Q.tipler[c['tipId']],kaynak=c['kaynak']))
    tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in Q.kartlar.items() if c['tipId']==t],uygulamaKonu=Q.k) for t,ad in Q.tipler.items()]
    json.dump(dict(konu=Q.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{o}.json','w'),ensure_ascii=False,indent=1)
    Q.P.yaz(f'{H}/{o}-1.json',f'/tmp/bos-{o}.json')
    assert len(Q.P.ANA)==Q.n
