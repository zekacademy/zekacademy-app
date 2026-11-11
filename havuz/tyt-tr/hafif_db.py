"""Dil bilgisi genişletmesi (11 Kasım 2026) · hafif mod yardımcısı.
hafif_dilbilgisi.py'nin genişletilmiş hâli: kalıp seçilebilir, şıklar benzersiz, kök '?' ile biter,
doğru şık belirgin en uzun olamaz, yanlış şıkların çoğunda uç sözcük varken doğru şıkta yoksa durur.
Kullanım:
    from hafif_db import *
    Q=kur('dyazim','Yazım Kuralları','tr|Yazım Kuralları',KARTLAR,TIPLER); Q.n=49
    soru(Q,'0001','K-DBYZ-01','orta','kazanım',3,'Kök?',[(şık,etiket,cel,tur)×5],'C',lambda e:e==Y,'istenen','ipucu',[bilgi],[adımlar],'puf',kalip='öncüllü')
    bitir(Q)
"""
import re
from tr_ortak import *
Y='yanlış'; D='doğru'
UC=r'\b(yalnızca|yalnız|tümüyle|tamamen|hiçbir|hiç|her zaman|daima|asla|kesinlikle|bütün)\b'
def kur(onek,konu_adi,k,kartlar,tipler):
    return Konu(onek,konu_adi,k,kartlar,tipler)
def soru(Q,no,kart,zor,kazanim,adim,metin,opts,harf,pred,istenen,ip,bilgi,adimlar,puf,kalip='düz'):
    """opts: 5 şık, A–E sırasıyla: (metin, etiket, cel, tur). pred(etiket)->bool; tam bir şık sağlamalı ve harf olmalı."""
    assert len(opts)==5 and len({o[0] for o in opts})==5,(no,'şık sayısı/tekrar')
    assert zor in ('kolay','orta','zor') and kalip in ('düz','öncüllü','hikâyeli','tablo'),no
    assert metin.rstrip().endswith('?'),(no,'kök ? ile bitmeli')
    ok=[i for i,o in enumerate(opts) if pred(o[1])]
    assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
    L=[len(o[0]) for o in opts]; d=L[ok[0]]; dig=[x for i,x in enumerate(L) if i!=ok[0]]
    assert not (d>max(dig) and d>=1.25*sum(dig)/4 and d>=25),(no,'doğru şık belirgin en uzun')
    ucy=[o for i,o in enumerate(opts) if i!=ok[0] and re.search(UC,o[0].lower())]
    assert not (len(ucy)>=3 and not re.search(UC,opts[ok[0]][0].lower())),(no,'uç sözcük örüntüsü')
    yan=[(o[0],o[2],o[3]) for i,o in enumerate(opts) if i!=ok[0]]
    for m,c,t in yan: assert c and len(c)>=12 and t in TURLER,(no,m)
    assert 3<=len(adimlar)<=7 and isinstance(ip,str) and len(bilgi)<=3,no
    c=Q.kartlar[kart]; tipId=c['tipId']
    sk,h,cel,tur=sikla(opts[ok[0]][0],yan,harf)
    Q.P.R(no,tipId,Q.tipler[tipId],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · özgün cümleler",metin,sk,h,istenen,[ip],bilgi,adimlar,puf,cel,tur)
def bitir(Q):
    """Kartları ve tek dosyayı yazar; kardeş yok. Harf dengesi ±2 ve n kontrol edilir."""
    for q in Q.P.ANA: q['kardes']=None
    o=Q.onek; kl=[]
    for kid,c in Q.kartlar.items():
        kl.append(dict(id=kid,konu=Q.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=Q.tipler[c['tipId']],kaynak=c['kaynak']))
    tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in Q.kartlar.items() if c['tipId']==t],uygulamaKonu=Q.k) for t,ad in Q.tipler.items()]
    json.dump(dict(konu=Q.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{o}.json','w'),ensure_ascii=False,indent=1)
    Q.P.yaz(f'{H}/{o}-1.json',f'/tmp/bos-{o}.json')
    assert len(Q.P.ANA)==Q.n,(len(Q.P.ANA),Q.n)
    h=Counter(q['cevap']['sik'] for q in Q.P.ANA); ort=Q.n/5
    assert all(abs(h.get(x,0)-ort)<=2.5 for x in 'ABCDE'),('harf dengesi',dict(h))
