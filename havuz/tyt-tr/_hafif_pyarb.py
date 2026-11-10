"""Hafif mod yardımcıları (paragraf): her şıkka etiket, tek doğru şık assert edilir. Yalnız pyarb için."""
from tr_ortak import *
def kur(onek,konu_adi,k,kartlar,tipler,n):
    Q=Konu(onek,konu_adi,k,kartlar,tipler); Q.n=n; return Q
def soru(Q,no,kart,zor,kazanim,adim,kalip,metin,opts,harf,pred,istenen,ip,bilgi,adimlar,puf):
    """opts: A–E sırasıyla (metin, etiket, cel, tur). pred(etiket)->bool; tam bir şık sağlamalı ve harf olmalı."""
    assert len(opts)==5
    ok=[i for i,o in enumerate(opts) if pred(o[1])]
    assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
    yan=[(o[0],o[2],o[3]) for i,o in enumerate(opts) if i!=ok[0]]
    for m,c,t in yan: assert c and len(c)>=12 and t in TURLER,(no,m)
    assert 3<=len(adimlar)<=5 and isinstance(ip,str) and len(bilgi)<=2
    c=Q.kartlar[kart]; tipId=c['tipId']
    sk,h,cel,tur=sikla(opts[ok[0]][0],yan,harf)
    Q.P.R(no,tipId,Q.tipler[tipId],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · özgün metin",metin,sk,h,istenen,[ip],bilgi,adimlar,puf,cel,tur)
def bitir(Q):
    for q in Q.P.ANA: q['kardes']=None
    o=Q.onek; kl=[]
    for kid,c in Q.kartlar.items():
        kl.append(dict(id=kid,konu=Q.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=Q.tipler[c['tipId']],kaynak=c['kaynak']))
    tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in Q.kartlar.items() if c['tipId']==t],uygulamaKonu=Q.k) for t,ad in Q.tipler.items()]
    json.dump(dict(konu=Q.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{o}.json','w'),ensure_ascii=False,indent=1)
    Q.P.yaz(f'{H}/{o}-1.json',f'/tmp/bos-{o}.json')
    assert len(Q.P.ANA)==Q.n
