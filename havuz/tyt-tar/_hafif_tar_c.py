"""TYT Tarih hafif mod yardımcıları: tek doğru şık assert, öncüllü şıklar ifade doğruluğundan hesaplanır."""
import sys,os,json
HD=os.path.dirname(os.path.abspath(__file__)); HAVUZ=os.path.join(HD,'..')
sys.path.insert(0,HAVUZ)
from ortak import *
from collections import Counter
ROM=['I','II','III','IV']
UK=json.load(open(f'{HAVUZ}/uygulama-konulari.json'))
def anahtar(ad):
    k='tar|'+ad; assert k in UK,k; return k
class Konu:
    def __init__(s,onek,konu_adi,kartlar,tipler):
        s.k=anahtar(konu_adi); s.P=Parti(onek,konu_adi,s.k,ders='TYT Tarih',idon='tyttar'); s.onek=onek; s.konu_adi=konu_adi
        s.kartlar=kartlar; s.tipler=tipler; s.zd={'kolay':1,'orta':2,'zor':1}
        for c in kartlar.values(): assert c['tipId'] in tipler
    def _yaz(s,no,kart,zor,kazanim,adim,kalip,metin,siklar,harf,istenen,ip,bilgi,adimlar,puf,cel,tur):
        c=s.kartlar[kart]; assert c['zorluk']==zor,(no,'kart zorluğu'); assert isinstance(ip,str) and 3<=len(adimlar)<=7 and 1<=len(bilgi)<=3
        s.P.R(no,c['tipId'],s.tipler[c['tipId']],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · özgün metin ve kurgu",metin,siklar,harf,istenen,[ip],bilgi,adimlar,puf,cel,tur)
    def S(s,no,kart,zor,kazanim,adim,kalip,metin,dogru,yanlislar,harf,istenen,ip,bilgi,adimlar,puf):
        """dogru: doğru şık metni; yanlislar: 4 adet (metin, cel, tur) A–E sırasında doğru şık harfi atlanarak yerleşir."""
        assert len(yanlislar)==4 and harf in 'ABCDE'
        siklar=[None]*5; cel={}; tur={}; it=iter(yanlislar)
        for i,l in enumerate('ABCDE'):
            if l==harf: siklar[i]=dogru
            else:
                m,c,t=next(it); assert c and len(c)>=12 and t in TURLER,(no,m); siklar[i]=m; cel[l]=c; tur[l]=t
        assert len(set(siklar))==5,no
        s._yaz(no,kart,zor,kazanim,adim,kalip,metin,siklar,harf,istenen,ip,bilgi,adimlar,puf,cel,tur)
    def oncul(s,no,kart,zor,kazanim,adim,giris,stmts,kok,secenekler,harf,dogru_mu,istenen,ip,bilgi,adimlar,puf):
        n=len(stmts); hedef={i for i,x in enumerate(stmts) if x[1]==dogru_mu}
        def ayir(t):
            if t.startswith('Yalnız'): return {ROM.index(t.split()[1])}
            return {ROM.index(x.strip()) for x in t.replace(' ve ',',').split(',')}
        ok=[i for i,t in enumerate(secenekler) if ayir(t)==hedef]
        assert len(ok)==1 and 'ABCDE'[ok[0]]==harf and len(set(secenekler))==5 and len(secenekler)==5,(no,ok,hedef)
        metin=(giris+'\n' if giris else '')+'\n'.join(f'{ROM[i]}. {x[0]}' for i,x in enumerate(stmts))+'\n'+kok
        cel={};tur={}
        for i,t in enumerate(secenekler):
            if i==ok[0]: continue
            Sx=ayir(t); p=[]
            for j in sorted(Sx-hedef): p.append(f'{ROM[j]}. ifade koşulu sağlamaz: {stmts[j][2].rstrip('.')}.')
            for j in sorted(hedef-Sx): p.append(f'{ROM[j]}. ifade de koşulu sağlar ama seçenekte yok: {stmts[j][2].rstrip('.')}.')
            cel['ABCDE'[i]]=' '.join(p); tur['ABCDE'[i]]='bilgi' if Sx-hedef else 'dikkat'
        s._yaz(no,kart,zor,kazanim,adim,'öncüllü',metin,secenekler,harf,istenen,ip,bilgi,adimlar,puf,cel,tur)
    def bitir(s):
        for q in s.P.ANA: q['kardes']=None
        assert len(s.P.ANA)==4,len(s.P.ANA)
        z=Counter(q['zorluk'] for q in s.P.ANA); assert dict(z)==s.zd,(dict(z),s.zd)
        assert {q['tipId'] for q in s.P.ANA}==set(s.tipler),'her tip en az 1 soru'
        kl=[dict(id=kid,konu=s.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=s.tipler[c['tipId']],kaynak=c['kaynak']) for kid,c in s.kartlar.items()]
        tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in s.kartlar.items() if c['tipId']==t],uygulamaKonu=s.k) for t,ad in s.tipler.items()]
        json.dump(dict(konu=s.konu_adi,surum=1,not_='Kart = fikir; soru metni içermez.',kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/{s.onek}.json','w'),ensure_ascii=False,indent=1)
        s.P.yaz(f'{HD}/{s.onek}-1.json',f'/tmp/bos-{s.onek}.json')
