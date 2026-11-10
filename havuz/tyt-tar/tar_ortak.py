"""TYT Tarih üretim betikleri için ortak yardımcılar (yalnız tyt-tar klasörüne ait)."""
import sys,os,json,random
H=os.path.dirname(os.path.abspath(__file__)); HAVUZ=os.path.join(H,'..'); sys.path.insert(0,HAVUZ)
from ortak import *

TUR={'b':'bilgi','i':'islem','d':'dikkat'}
def Kt(alt,tipId,zorluk,kalip,adim,fikir,tuzak,kaynak=None):
    return dict(alt=alt,tipId=tipId,zorluk=zorluk,kalip=kalip,adim=adim,fikir=fikir,tuzak=tuzak,kaynak=kaynak)

class Konu:
    def __init__(s,onek,konu_adi,k,kartlar,tipler):
        """kartlar: {kartId: Kt(...)}; tipler: {tipId: ad}"""
        s.P=Parti(onek,konu_adi,k,ders='TYT Tarih',idon='tyttar'); s.onek=onek; s.konu_adi=konu_adi; s.k=k; s.kartlar=kartlar; s.tipler=tipler
        for kid,c in kartlar.items(): assert c['tipId'] in tipler
        rnd=random.Random(onek); s.seq=[]
        for _ in range(12):
            b=list('ABCDE'); rnd.shuffle(b); s.seq+=b
    def _sik(s,d):
        L='ABCDE'
        if 'sirali' in d:
            sr=d['sirali']; assert len(sr)==5
            dg=[i for i,x in enumerate(sr) if x[2] is None]; assert len(dg)==1
            siklar=[x[0] for x in sr]; harf=L[dg[0]]; cel={}; tur={}
            for i,x in enumerate(sr):
                if x[2] is not None: cel[L[i]]=x[1]; tur[L[i]]=TUR[x[2]]
        else:
            yan=d['yan']; assert len(yan)==4
            harf=d.get('harf') or s.seq.pop(0)
            siklar=[None]*5; cel={}; tur={}; siklar[L.index(harf)]=d['dogru']
            for l,x in zip([c for c in L if c!=harf],yan):
                siklar[L.index(l)]=x[0]; cel[l]=x[1]; tur[l]=TUR[x[2]]
        assert len(set(siklar))==5,'aynı şık'
        return siklar,harf,cel,tur
    def _adim(s,lst): return [A(*x) for x in lst]
    def ekle(s,no,kart,zor,kazanim,kalip,adim,A_,K_,yeni=''):
        c=s.kartlar[kart]; tipId=c['tipId']
        sk,h,cel,tur=s._sik(A_)
        s.P.R(no,tipId,s.tipler[tipId],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · {yeni or 'özgün metin'}",A_['metin'],sk,h,A_['istenen'],A_['ip'],A_['bilgi'],s._adim(A_['adim']),A_['puf'],cel,tur,kisa=A_.get('kisa'))
        K_=dict(K_)
        for a in ('bilgi','puf'): K_.setdefault(a,A_[a])
        sk,h,cel,tur=s._sik(K_)
        s.P.K(no,K_['metin'],sk,h,K_['istenen'],K_['ip'],K_['bilgi'],s._adim(K_['adim']),K_['puf'],cel,tur,kisa=K_.get('kisa'))
    def bitir(s):
        o=s.onek; kl=[]
        for kid,c in s.kartlar.items():
            kl.append(dict(id=kid,konu=s.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=s.tipler[c['tipId']],
                kaynak=c['kaynak'] or f'ÖSYM TYT Tarih 2018–2026 ({s.konu_adi})'))
        tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in s.kartlar.items() if c['tipId']==t],uygulamaKonu=s.k) for t,ad in s.tipler.items()]
        json.dump(dict(konu=s.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{o}.json','w'),ensure_ascii=False,indent=1)
        s.P.yaz(f'{H}/{o}-1.json',f'{H}/{o}-1-kardes.json')

def kalan_tipler(Q):
    from collections import Counter
    print(Counter(q['tipId'] for q in Q.P.ANA))
