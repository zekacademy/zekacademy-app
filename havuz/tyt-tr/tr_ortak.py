"""Türkçe üretim betikleri için ortak yardımcılar (yalnız tyt-tr klasörüne ait)."""
import sys,os,json,random
H=os.path.dirname(os.path.abspath(__file__)); HAVUZ=os.path.join(H,'..'); sys.path.insert(0,HAVUZ)
from ortak import *
from collections import Counter

def sikla(dogru,yanlislar,harf):
    """dogru: doğru şık metni; yanlislar: 4 adet (metin, cel, tur); harf: doğru şıkkın harfi."""
    assert len(yanlislar)==4
    L='ABCDE'; siklar=[None]*5; cel={}; tur={}
    siklar[L.index(harf)]=dogru
    for l,(m,c,t) in zip([x for x in L if x!=harf],yanlislar):
        siklar[L.index(l)]=m; cel[l]=c; tur[l]=t
    assert len(set(siklar))==5,'aynı şık'
    return siklar,harf,cel,tur

ROM=['I','II','III','IV','V','VI']
def numarali(cumleler_dogru_sirada,perm):
    """cumleler_dogru_sirada: doğru sıradaki cümleler. perm: görünüm sırası; perm[i] = ekranda (i+1). numaralı cümlenin doğru sıradaki indeksi.
    Dönen: (metin, dogru_sira_romen_listesi) — doğru sırada ekrandaki romen numaraları."""
    n=len(cumleler_dogru_sirada); assert sorted(perm)==list(range(n))
    metin='\n'.join(f'{ROM[i]}. {cumleler_dogru_sirada[perm[i]]}' for i in range(n))
    sira=[ROM[perm.index(j)] for j in range(n)]
    return metin,sira

class Konu:
    def __init__(s,onek,konu_adi,k,kartlar,tipler):
        """kartlar: {kartId: dict(alt,fikir,tuzak,zorluk,kalip,adim,tipId,kaynak)}; tipler: {tipId: ad}"""
        s.P=Parti(onek,konu_adi,k,ders='TYT Türkçe',idon='tyttr'); s.onek=onek; s.konu_adi=konu_adi; s.k=k; s.kartlar=kartlar; s.tipler=tipler; s.KADIM={}
        for kid,c in kartlar.items(): assert c['tipId'] in tipler
    def ekle(s,no,kart,zor,kazanim,kalip,adim,A,K,yeni=''):
        c=s.kartlar[kart]; tipId=c['tipId']
        def hazir(d,ana=None):
            d=dict(d)
            if ana:
                for a in ('bilgi','puf','ip','kisa'):
                    d.setdefault(a,ana.get(a))
            siklar,harf,cel,tur=sikla(d['dogru'],d['yan'],d['harf'])
            return d,siklar,harf,cel,tur
        a,sk,h,cel,tur=hazir(A)
        s.P.R(no,tipId,s.tipler[tipId],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · {yeni or 'özgün metin'}",a['metin'],sk,h,a['istenen'],a['ip'],a['bilgi'],a['adim'],a['puf'],cel,tur,kisa=a.get('kisa'))
        K=dict(K); K.setdefault('adim',s.KADIM[no])
        k,sk,h,cel,tur=hazir(K,A)
        s.P.K(no,k['metin'],sk,h,k['istenen'],k['ip'],k['bilgi'],k['adim'],k['puf'],cel,tur,kisa=k.get('kisa'))
    def bitir(s):
        o=s.onek
        kl=[]
        for kid,c in s.kartlar.items():
            kl.append(dict(id=kid,konu=s.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=s.tipler[c['tipId']],kaynak=c['kaynak']))
        tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in s.kartlar.items() if c['tipId']==t],uygulamaKonu=s.k) for t,ad in s.tipler.items()]
        json.dump(dict(konu=s.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{o}.json','w'),ensure_ascii=False,indent=1)
        s.P.yaz(f'{H}/{o}-1.json',f'{H}/{o}-1-kardes.json')
