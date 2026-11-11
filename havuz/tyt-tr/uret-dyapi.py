"""TYT Türkçe · Sözcükte Yapı/Ekler genişletmesi: 26 soru (hafif mod). Metinler özgündür.
Sözcük çözümlemeleri tek sözlükte (Z) tutulur; şık açıklamaları ve etiketler oradan üretilir."""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def K(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBYP-01':K('Basit, Türemiş ve Birleşik Sözcükler','Sözcüğün yapıca basit, türemiş ya da birleşik olduğunu kök ve ek çözümlemesiyle ayırt etmek.','Çekim ekli sözcüğü türemiş saymak; birleşik sözcüğü tek sözcük sanıp basit saymak.','orta','düz',3,'dyp-yapi'),
 'K-DBYP-02':K('Yapım Eki – Çekim Eki Ayrımı','Sözcükteki eklerin yapım mı çekim mi olduğunu ayırıp yalnız yapım ya da yalnız çekim eki içeren sözcüğü bulmak.','Çoğul, iyelik ve hâl eklerini yapım eki sanmak; hem yapım hem çekim eki olan sözcüğü atlamak.','orta','düz',3,'dyp-yapimcekim'),
 'K-DBYP-03':K('Yapım Eklerinin Türü','Yapım ekinin kökün ve türettiği sözcüğün türüne göre (isimden isim, fiilden isim, isimden fiil, fiilden fiil) adlandırılması.','Eki türettiği sözcüğe bakıp adlandırmak; birden çok ekli sözcükte sırayı karıştırmak.','orta','düz',4,'dyp-ekturu'),
 'K-DBYP-04':K('Çekim Ekleri ve Ek Sırası','Hâl, iyelik, çoğul ve tamlayan eklerini tanımak; çoğul–iyelik–hâl sırasını bilmek.','Yapım ekini çekim ekinden önce ya da sonra karıştırmak; hâl eklerini birbirine karıştırmak.','orta','düz',3,'dyp-cekim'),
 'K-DBYP-05':K('Kök, Gövde ve Ek Sayısı','Sözcüğün kökünü ve gövdesini bulmak; yapım ve çekim eklerini sayarak karşılaştırmak.','Gövdeyi kök sanmak; eki eksik ya da fazla saymak.','orta','düz',4,'dyp-koksayi'),
 'K-DBYP-06':K('Numaralı Parçada Yapıca Farklı Sözcük','Numaralanmış sözcükleri yapı, ek türü ve ek sayısı bakımından karşılaştırıp ötekilerden ayrılanı bulmak.','Çekim ekini yapım eki saymak; numaralı sözcüğü bağlamdan koparıp çözümlememek.','orta','öncüllü',4,'dyp-parca'),
}
TIPLER={'dyp-yapi':'Basit, türemiş ve birleşik sözcükler','dyp-yapimcekim':'Yapım eki ve çekim eki ayrımı','dyp-ekturu':'Yapım ekinin türü','dyp-cekim':'Çekim ekleri ve ek sırası','dyp-koksayi':'Kök, gövde ve ek sayısı','dyp-parca':'Numaralı parçada yapıca farklı sözcük'}
Q=kur('dyapi','Sözcükte Yapı/Ekler','tr|Sözcükte Yapı/Ekler',KARTLAR,TIPLER); Q.n=26
# ---------------- sözcük sözlüğü ----------------
Z={}
def z(w,c,yapi,ya,ce,tur=()): Z[w]=dict(w=w,c=f'{w}: {c}',yapi=yapi,ya=ya,ce=ce,tur=list(tur),k=c)
def basit(w,ce=0,c=None): z(w,c or (f'{w} (kök, ad)' if not ce else ''),'basit',0,ce)
for w in ('masa','deniz','bulut','defter','kuş','dağ'): z(w,f'{w} (kök, ad); ek almamıştır','basit',0,0)
z('kuş','kuş (kök, ad); ek almamıştır','basit',0,0)
z('denizlerde','deniz (kök, ad) + -ler (çoğul, çekim) + -de (bulunma hâli, çekim)','basit',0,2)
z('evlerde','ev (kök, ad) + -ler (çoğul) + -de (bulunma hâli)','basit',0,2)
z('evlerim','ev (kök, ad) + -ler (çoğul) + -im (iyelik)','basit',0,2)
z('kitaplarda','kitap (kök, ad) + -lar (çoğul) + -da (bulunma hâli)','basit',0,2)
z('dağlarda','dağ (kök, ad) + -lar (çoğul) + -da (bulunma hâli)','basit',0,2)
z('çocuklar','çocuk (kök, ad) + -lar (çoğul)','basit',0,1)
z('masaya','masa (kök, ad) + -ya (yönelme hâli)','basit',0,1)
z('denizden','deniz (kök, ad) + -den (ayrılma hâli)','basit',0,1)
z('defterim','defter (kök, ad) + -im (iyelik)','basit',0,1)
z('masalarımız','masa (kök, ad) + -lar (çoğul) + -ımız (iyelik)','basit',0,2)
z('başkent','baş + kent (iki sözcük birleşmiş)','birleşik',0,0)
z('gecekondu','gece + kondu (iki sözcük birleşmiş)','birleşik',0,0)
z('karabiber','kara + biber (iki sözcük birleşmiş)','birleşik',0,0)
z('akarsu','akar + su (iki sözcük birleşmiş)','birleşik',0,0)
z('başkentte','baş + kent (birleşik gövde) + -te (bulunma hâli)','birleşik',0,1)
z('gözlük','göz (kök, ad) + -lük (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('gözlükçü','göz (kök, ad) + -lük (yapım) + -çü (yapım)','türemiş',2,0,['isimden isim']*2)
z('gözlükçülük','göz (kök, ad) + -lük (yapım) + -çü (yapım) + -lük (yapım)','türemiş',3,0,['isimden isim']*3)
z('gözlüklerim','göz (kök, ad) + -lük (yapım) + -ler (çoğul) + -im (iyelik)','türemiş',1,2,['isimden isim'])
z('gözlüklerimiz','göz (kök, ad) + -lük (yapım) + -ler (çoğul) + -imiz (iyelik)','türemiş',1,2,['isimden isim'])
z('gözlükte','göz (kök, ad) + -lük (yapım) + -te (bulunma hâli)','türemiş',1,1,['isimden isim'])
z('balıkçı','balık (kök, ad) + -çı (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('balıkçılar','balık (kök, ad) + -çı (yapım) + -lar (çoğul)','türemiş',1,1,['isimden isim'])
z('balıkçılara','balık (kök, ad) + -çı (yapım) + -lar (çoğul) + -a (yönelme hâli)','türemiş',1,2,['isimden isim'])
z('balıkçılarda','balık (kök, ad) + -çı (yapım) + -lar (çoğul) + -da (bulunma hâli)','türemiş',1,2,['isimden isim'])
z('balıkçılarımızdan','balık (kök, ad) + -çı (yapım) + -lar (çoğul) + -ımız (iyelik) + -dan (ayrılma hâli)','türemiş',1,3,['isimden isim'])
z('balıkçılık','balık (kök, ad) + -çı (yapım) + -lık (yapım)','türemiş',2,0,['isimden isim']*2)
z('kitaplık','kitap (kök, ad) + -lık (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('kitaplıkta','kitap (kök, ad) + -lık (yapım) + -ta (bulunma hâli)','türemiş',1,1,['isimden isim'])
z('kitaplıklarım','kitap (kök, ad) + -lık (yapım) + -lar (çoğul) + -ım (iyelik)','türemiş',1,2,['isimden isim'])
z('sessiz','ses (kök, ad) + -siz (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('sessizlik','ses (kök, ad) + -siz (yapım) + -lik (yapım)','türemiş',2,0,['isimden isim']*2)
z('sessizlikte','ses (kök, ad) + -siz (yapım) + -lik (yapım) + -te (bulunma hâli)','türemiş',2,1,['isimden isim']*2)
z('sessizlikten','ses (kök, ad) + -siz (yapım) + -lik (yapım) + -ten (ayrılma hâli)','türemiş',2,1,['isimden isim']*2)
z('sulu','su (kök, ad) + -lu (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('tuzlu','tuz (kök, ad) + -lu (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('tuzlukta','tuz (kök, ad) + -luk (yapım) + -ta (bulunma hâli)','türemiş',1,1,['isimden isim'])
z('akıllı','akıl (kök, ad) + -lı (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('evcil','ev (kök, ad) + -cil (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('evsiz','ev (kök, ad) + -siz (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('dağcı','dağ (kök, ad) + -cı (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('dağcılara','dağ (kök, ad) + -cı (yapım) + -lar (çoğul) + -a (yönelme hâli)','türemiş',1,2,['isimden isim'])
z('dağcılarda','dağ (kök, ad) + -cı (yapım) + -lar (çoğul) + -da (bulunma hâli)','türemiş',1,2,['isimden isim'])
z('okuyucu','oku- (kök, fiil) + -yucu (yapım, fiilden isim)','türemiş',1,0,['fiilden isim'])
z('koşucu','koş- (kök, fiil) + -ucu (yapım, fiilden isim)','türemiş',1,0,['fiilden isim'])
z('satıcı','sat- (kök, fiil) + -ıcı (yapım, fiilden isim)','türemiş',1,0,['fiilden isim'])
z('satıcılık','sat- (kök, fiil) + -ıcı (yapım, fiilden isim) + -lık (yapım, isimden isim)','türemiş',2,0,['fiilden isim','isimden isim'])
z('temizleyici','temiz (kök, ad soylu) + -le (yapım, isimden fiil) + -yici (yapım, fiilden isim)','türemiş',2,0,['isimden fiil','fiilden isim'])
z('sevindirici','sev- (kök, fiil) + -in (yapım, fiilden fiil) + -dir (yapım, fiilden fiil) + -ici (yapım, fiilden isim)','türemiş',3,0,['fiilden fiil','fiilden fiil','fiilden isim'])
z('temizledi','temiz (kök, ad soylu) + -le (yapım, isimden fiil) + -di (geçmiş zaman, çekim)','türemiş',1,1,['isimden fiil'])
z('temizlemek','temiz (kök, ad soylu) + -le (yapım, isimden fiil) + -mek (mastar)','türemiş',1,0,['isimden fiil'])
z('okutmak','oku- (kök, fiil) + -t (yapım, fiilden fiil) + -mak (mastar)','türemiş',1,0,['fiilden fiil'])
z('gözlükleri','göz (kök, ad) + -lük (yapım) + -ler (çoğul) + -i (iyelik)','türemiş',1,2,['isimden isim'])
z('çiçekçi','çiçek (kök, ad) + -çi (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('sütçü','süt (kök, ad) + -çü (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('sütlü','süt (kök, ad) + -lü (yapım, isimden isim)','türemiş',1,0,['isimden isim'])
z('yolcularımızdan','yol (kök, ad) + -cu (yapım) + -lar (çoğul) + -ımız (iyelik) + -dan (ayrılma hâli)','türemiş',1,3,['isimden isim'])
z('sütçülerimizden','süt (kök, ad) + -çü (yapım) + -ler (çoğul) + -imiz (iyelik) + -den (ayrılma hâli)','türemiş',1,3,['isimden isim'])
z('kitaplıklarımızdan','kitap (kök, ad) + -lık (yapım) + -lar (çoğul) + -ımız (iyelik) + -dan (ayrılma hâli)','türemiş',1,3,['isimden isim'])
z('sessizliklerimizde','ses (kök, ad) + -siz (yapım) + -lik (yapım) + -ler (çoğul) + -imiz (iyelik) + -de (bulunma hâli)','türemiş',2,3,['isimden isim']*2)
z('sevinmek','sev- (kök, fiil) + -in (yapım, fiilden fiil) + -mek (mastar)','türemiş',1,0,['fiilden fiil'])
z('yazdırmak','yaz- (kök, fiil) + -dır (yapım, fiilden fiil) + -mak (mastar)','türemiş',1,0,['fiilden fiil'])
z('döndürmek','dön- (kök, fiil) + -dür (yapım, fiilden fiil) + -mek (mastar)','türemiş',1,0,['fiilden fiil'])
z('okuttu','oku- (kök, fiil) + -t (yapım, fiilden fiil) + -tu (geçmiş zaman, çekim)','türemiş',1,1,['fiilden fiil'])
z('susturdu','sus- (kök, fiil) + -tur (yapım, fiilden fiil) + -du (geçmiş zaman, çekim)','türemiş',1,1,['fiilden fiil'])
z('sevindirdi','sev- (kök, fiil) + -in (yapım, fiilden fiil) + -dir (yapım, fiilden fiil) + -di (geçmiş zaman, çekim)','türemiş',2,1,['fiilden fiil']*2)
def tek(ya,ce): return f'{ya} yapım, {ce} çekim eki'
def romen(i): return ROM[i]
def parca(txt):
    ws=[]; n=[0]
    def f(m):
        ws.append(m.group(1).lower()); i=len(ws)-1; assert int(m.group(2))==i+1,txt[:30]
        return f'{m.group(1)} ({ROM[i]})'
    return re.sub(r'([^\s\[\]]+)\[(\d)\]',f,txt),ws
def dsoru(no,kart,zor,kazanim,adim,kok,siklar,harf,pred,kisa,neden,istenen,ip,bilgi,kural,puf,kalip='düz',on='',islem_ad=None,ad2=None):
    """siklar: 5 (şık metni, giriş). giriş: Z kaydı (ya da kendi c, k alanlı sözlük). pred(giriş); kisa(giriş) -> adım özeti; neden(giriş) -> yanlış şıkkın nedeni."""
    opts=[]
    for d,e in siklar:
        opts.append((d,e,'' if pred(e) else f"{e['c'].rstrip('.')} → {neden(e)}",'islem'))
    # doğru şıkkın cel boş (soru() zaten yalnız yanlışları kullanır); yanlışlarda sözlükten
    dg=[(d,e) for d,e in siklar if pred(e)][0]
    ad=[A('Ölçütü belirle',kural,istenen[:60]),
        A('Şıkları tek tek çözümle',*(ad2 or ('Her şıkkı köküne ve eklerine ayırıp ölçüte göre sına.',' · '.join(f"{(islem_ad or (lambda d,e:d))(d,e)}: {kisa(e)}" for d,e in siklar)))),
        A('Sonucu bul',f"{dg[1]['c'].rstrip('.')}. Ölçüt yalnız bu şıkta sağlanır.",f"{dg[0]}: {kisa(dg[1])}")]
    soru(Q,no,kart,zor,kazanim,adim,on+kok,opts,harf,lambda e:pred(e),istenen,ip,bilgi,ad,puf,kalip=kalip)
def psoru(no,kart,zor,kazanim,adim,txt,kok,harf,pred,kisa,neden,istenen,ip,bilgi,kural,puf):
    disp,ws=parca(txt); assert len(ws)==5,(no,ws)
    for w in ws: assert w in Z,(no,w)
    sik=[(ROM[i],Z[w]) for i,w in enumerate(ws)]
    dsoru(no,kart,zor,kazanim,adim,kok,sik,harf,pred,kisa,neden,istenen,ip,bilgi,kural,puf,kalip='öncüllü',on=disp+'\n\n',islem_ad=lambda d,e:f"{d} ({e['w']})")
# bilgi kutuları
B_YAPI=B('Basit, türemiş, birleşik','basit: ek almamış tek kök (masa) · türemiş: kök + yapım eki (göz+lük) · birleşik: iki sözcüğün kaynaşması (baş+kent). Yapıca sınıflamada çekim ekleri dikkate alınmaz.')
B_EK=B('Yapım eki / çekim eki','yapım eki yeni sözcük türetir (balık → balıkçı) · çekim eki sözcüğü cümleye bağlar: çoğul -ler, iyelik -im, hâl -e/-de/-den, tamlayan -in (evlerde, defterim)')
B_TUR=B('Yapım ekinin türü','ek, kökün türüne ve türettiği sözcüğe göre adlandırılır: göz+lük isimden isim · oku+yucu fiilden isim · temiz+le isimden fiil · yaz+dır fiilden fiil')
B_SIRA=B('Ek sırası','önce yapım ekleri, sonra çekim ekleri gelir; çekimde sıra çoğul → iyelik → hâl: ev+ler+imiz+den')
B_GOV=B('Kök ve gövde','kök: sözcüğün bölünemeyen ilk parçası (göz) · gövde: kök ya da kök + yapım ekleri (gözlük); çekim ekleri gövdeye gelir: göz+lük+ler')
# ===== K01 =====
YP=lambda e:e['yapi']
def yk(e): return e['yapi']
dsoru('0001','K-DBYP-01','kolay','Birleşik yapılı sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisi yapıca birleşik bir sözcüktür?',
 [('sulu',Z['sulu']),('deniz',Z['deniz']),('başkent',Z['başkent']),('gözlük',Z['gözlük']),('masa',Z['masa'])],'C',lambda e:e['yapi']=='birleşik',yk,
 lambda e:{'basit':'ek almamış, tek parçalı bir sözcüktür; birleşik değildir.','türemiş':'yapım eki almıştır; türemiştir, birleşik değildir.'}[e['yapi']],
 'Yapıca birleşik olan sözcük.','Sözcüğü iki anlamlı parçaya ayırıp ayıramadığına bak; ek olarak değil, sözcük olarak ayrılıyor mu?',[B_YAPI],
 'Birleşik sözcük iki ayrı sözcüğün kaynaşmasıdır; parçalardan biri ek değil, anlamlı bir sözcüktür.','Parçaların ikisi de tek başına sözcükse birleşiktir; biri yalnız ekse türemiştir.')
dsoru('0002','K-DBYP-01','orta','Yapıca ötekilerden farklı olan sözcüğü bulur.',3,'Aşağıdaki sözcüklerden hangisi yapıca ötekilerden farklıdır?',
 [('başkent',Z['başkent']),('gecekondu',Z['gecekondu']),('karabiber',Z['karabiber']),('akarsu',Z['akarsu']),('balıkçı',Z['balıkçı'])][::-1][::-1],'E',lambda e:e['yapi']!='birleşik',yk,
 lambda e:'birleşik yapılıdır; öteki sözcüklerle aynı gruptadır.',
 'Yapıca ötekilerden farklı olan sözcük.','Her sözcüğü parçalara ayır; dördü iki sözcükten, biri sözcük + ekten oluşur.',[B_YAPI],
 'Dört sözcük iki sözcüğün birleşmesidir; biri kök + yapım ekinden oluşur.','Parçalardan biri yalnız ekse sözcük türemiştir.')
SYAPI=lambda ws:[(w,y) for w,y in ws]
def cumle(ws):
    return ' '.join(w for w,_ in ws),dict(c=None,sayi=sum(1 for _,y in ws if y=='T'),var={y for _,y in ws},ws=ws)
S3=[('Akıllı çocuk kitaplıkta kalem aradı.',[('Akıllı','T'),('çocuk','b'),('kitaplıkta','T'),('kalem','b'),('aradı','b')]),
 ('Balıkçı sessiz denizde sulu çorba içti.',[('Balıkçı','T'),('sessiz','T'),('denizde','b'),('sulu','T'),('çorba','b'),('içti','b')]),
 ('Yaşlı adam masada eski defteri açtı.',[('Yaşlı','T'),('adam','b'),('masada','b'),('eski','b'),('defteri','b'),('açtı','b')]),
 ('Dağcı sabah erken yola çıktı ve akşam döndü.',[('Dağcı','T'),('sabah','b'),('erken','b'),('yola','b'),('çıktı','b'),('ve','b'),('akşam','b'),('döndü','b')]),
 ('Evcil kuşlar sessiz odada uyudu.',[('Evcil','T'),('kuşlar','b'),('sessiz','T'),('odada','b'),('uyudu','b')])]
def turemis_say(ws): return [y for _,y in ws].count('T')
def sen(cs,ck):
    out=[]
    for m,ws in cs:
        assert ' '.join(w for w,_ in ws)+'.'==m,(m,)
        out.append((m,dict(c=m,ws=ws)))
    return out
def tum(e): return f"{turemis_say(e['ws'])} türemiş"
def tdesc(e): return ', '.join(f"{w}: {'türemiş' if y=='T' else ('birleşik' if y=='Bi' else 'basit')}" for w,y in e['ws'] if y!='b') or 'türemiş sözcük yok'
S3o=[(m,dict(c=f"“{m}” türemişler → {tdesc(dict(ws=ws))} (toplam {turemis_say(ws)})",ws=ws)) for m,ws in S3]
dsoru('0003','K-DBYP-01','orta','Cümlelerdeki türemiş sözcük sayısını karşılaştırır.',3,'Çekim ekleri dikkate alınmamak koşuluyla, aşağıdaki cümlelerin hangisinde türemiş sözcük sayısı en fazladır?',
 S3o,'B',lambda e:turemis_say(e['ws'])==3,lambda e:f"{turemis_say(e['ws'])} türemiş",lambda e:f"türemiş sözcük sayısı {turemis_say(e['ws'])}'dir; en fazla olan değildir.",
 'Türemiş sözcük sayısı en fazla olan cümle.','Her cümlede yapım eki almış sözcükleri say; çekim ekleri sayıya girmez.',[B_YAPI],
 'Sözcükleri tek tek köküne ayırıp yapım eki alanları say; çekim ekli sözcükleri basit say.','Çekim ekleri (-da, -i, -lar) sözcüğü türemiş yapmaz.',
 islem_ad=lambda d,e:'Cümle '+'ABCDE'[[m for m,_ in S3o].index(d)])
def yd(y): return {'T':'türemiş','Bi':'birleşik','b':'basit'}[y]
S4=[('Başkent Ankara’nın sessiz sokaklarında yürüdük.',[('Başkent','Bi'),('Ankara’nın','b'),('sessiz','T'),('sokaklarında','b'),('yürüdük','b')]),
 ('Gözlükçü dükkânında yeni çerçeveler gördük.',[('Gözlükçü','T'),('dükkânında','b'),('yeni','b'),('çerçeveler','b'),('gördük','b')]),
 ('Karabiber çorbaya güzel bir lezzet katıyor.',[('Karabiber','Bi'),('çorbaya','b'),('güzel','b'),('bir','b'),('lezzet','b'),('katıyor','b')]),
 ('Dağcılar sabah yola çıkıp zirveye doğru tırmandı.',[('Dağcılar','T'),('sabah','b'),('yola','b'),('çıkıp','b'),('zirveye','b'),('doğru','b'),('tırmandı','b')]),
 ('Kuruyemiş dükkânı çarşının köşesinde duruyor.',[('Kuruyemiş','Bi'),('dükkânı','b'),('çarşının','b'),('köşesinde','b'),('duruyor','b')])]
S4o=[]
for m,ws in S4:
    assert ' '.join(w for w,_ in ws)+'.'==m,m
    S4o.append((m,dict(c=f"“{m}” → türler: {', '.join(sorted({yd(y) for _,y in ws}))}",var={y for _,y in ws})))
dsoru('0004','K-DBYP-01','orta','Bir cümledeki sözcüklerin yapı türlerini birlikte değerlendirir.',4,'Çekim ekleri dikkate alınmamak koşuluyla, aşağıdaki cümlelerin hangisinde yapıca basit, türemiş ve birleşik sözcüklerin üçü de bulunur?',
 S4o,'A',lambda e:e['var']=={'b','T','Bi'},lambda e:'/'.join(sorted(yd(y) for y in e['var'])),lambda e:'üç yapı türünün hepsini birden taşımaz.',
 'Basit, türemiş ve birleşik sözcüklerin üçünü birden içeren cümle.','Her cümlede önce birleşik sözcükleri, sonra yapım eki almış sözcükleri bul.',[B_YAPI],
 'Cümledeki her sözcüğü kök ve eklerine ayır; üç yapıyı da yazıp hangi cümlede eksik olmadığını denetle.','Önce birleşik ve türemiş sözcükleri işaretle; kalan sözcükler basittir.',
 islem_ad=lambda d,e:'Cümle '+'ABCDE'[[m for m,_ in S4o].index(d)])
# ===== K02 =====
dsoru('0005','K-DBYP-02','kolay','Yalnız çekim eki taşıyan sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisinde yalnız çekim eki vardır?',
 [('balıkçı',Z['balıkçı']),('gözlük',Z['gözlük']),('sessiz',Z['sessiz']),('kitaplarda',Z['kitaplarda']),('akıllı',Z['akıllı'])],'D',lambda e:e['ya']==0 and e['ce']>0,lambda e:tek(e['ya'],e['ce']),
 lambda e:'yapım eki almıştır; yalnız çekim eki içermez.','Yalnız çekim eki taşıyan sözcük.','Eki çıkardığında yeni bir sözcük kavramı kayboluyorsa ek yapım ekidir.',[B_EK],
 'Yapım eki yeni sözcük türetir, çekim eki türetmez; yalnız çekim eki olan sözcükte yapım eki bulunmaz.','Çoğul, hâl ve iyelik ekleri çekim ekidir.')
dsoru('0006','K-DBYP-02','orta','Hem yapım hem çekim eki taşıyan sözcüğü belirler.',3,'Aşağıdaki sözcüklerden hangisinde hem yapım eki hem çekim eki vardır?',
 [('gözlükte',Z['gözlükte']),('evlerde',Z['evlerde']),('kitaplar',dict(Z['çocuklar'],c='kitaplar: kitap (kök, ad) + -lar (çoğul, çekim)',w='kitaplar')),('denizden',Z['denizden']),('masada',dict(Z['masaya'],c='masada: masa (kök, ad) + -da (bulunma hâli, çekim)',w='masada'))],'A',
 lambda e:e['ya']>=1 and e['ce']>=1,lambda e:tek(e['ya'],e['ce']),lambda e:'yalnız çekim eki içerir; yapım eki yoktur.',
 'Hem yapım hem çekim eki bulunan sözcük.','Her sözcükteki ekleri ayrı ayrı yaz; yapım ve çekim sütununda ikisi de dolu olanı seç.',[B_EK],
 'Ekleri iki sütuna ayır; ikisi de dolu olan sözcük aranan sözcüktür.','Yapım ekini kökün hemen yanında, çekim eklerini sonda ara.')
# 0007 öncüllü
K7=[('gözlüklerim',Z['gözlüklerim']),('balıkçı',Z['balıkçı']),('evlerim',Z['evlerim']),('sessizlik',Z['sessizlik'])]
def altk(ks):
    return frozenset(i for i,(w,e) in enumerate(K7) if e['ya']>=1 and e['ce']==0)
SET7={'I ve III':{0,2},'II ve III':{1,2},'II ve IV':{1,3},'I, II ve IV':{0,1,3},'III ve IV':{2,3}}
OK7={i for i,(w,e) in enumerate(K7) if e['ya']>=1 and e['ce']==0}
assert OK7=={1,3}
def c7(v):
    fazla=sorted(v-OK7); eksik=sorted(OK7-v)
    return '; '.join(([f"{ROM[i]}. {K7[i][0]} yalnız yapım ekli değil ({tek(K7[i][1]['ya'],K7[i][1]['ce'])})" for i in fazla])+([f"{ROM[i]}. {K7[i][0]} yalnız yapım ekli olduğu hâlde alınmamış" for i in eksik]))
def secenek7(): return [(k,dict(c=f"{k}",s=v,n=c7(v))) for k,v in SET7.items()]
dsoru('0007','K-DBYP-02','orta','Öncüllerdeki sözcüklerden yalnız yapım eki taşıyanları belirler.',4,'Yukarıdaki sözcüklerden hangileri yalnız yapım eki almıştır?',
 secenek7(),'C',lambda e:e['s']==OK7,lambda e:'yalnız yapım ekli öncüller seçilmiş' if e['s']==OK7 else 'seçim tutmuyor',
 lambda e:e['n'],
 'Yalnız yapım eki almış sözcüklerin hangileri olduğu.','Her öncülü ekleriyle çözümle: yapım ve çekim eki sayılarını yaz.',[B_EK],
 'Önce her öncülün yapım ve çekim eklerini bul: I: 1 yapım, 2 çekim · II: 1 yapım · III: 2 çekim · IV: 2 yapım; sonra yalnız yapım ekli olanları seç.','Öncülleri tek tek çözümle, sonra seçeneklerle karşılaştır.',
 kalip='öncüllü',on='I. gözlüklerim\nII. balıkçı\nIII. evlerim\nIV. sessizlik\n\n',ad2=('Öncülleri çöz: I göz+lük+ler+im, II balık+çı, III ev+ler+im, IV ses+siz+lik.','I: 1 yapım, 2 çekim ✗ · II: 1 yapım ✓ · III: 2 çekim ✗ · IV: 2 yapım ✓'))
psoru('0008','K-DBYP-02','orta','Numaralı sözcüklerden çekim eki taşımayanı bulur.',3,
 'Elif hafta sonu kasabadaki eski kitaplıkta[1] bir saat geçirdi. Eve dönünce gözlükleri[2] kayboldu diye bütün odaları aradı. Mahalledeki balıkçılara[3] bile sordu, ama kimse görmemişti. Evlerde[4] aranmadık yer bırakmadı. Sonunda yan dükkândaki gözlükçü[5] gözlüğü yolda bulup getirdi.',
 'Bu parçada numaralanmış sözcüklerden hangisinde çekim eki yoktur?','E',lambda e:e['ce']==0,lambda e:tek(e['ya'],e['ce']),lambda e:'çekim eki taşır; “çekim eki yoktur” ölçütüne uymaz.',
 'Çekim eki bulunmayan numaralı sözcük.','Her numaralı sözcükte çoğul, iyelik ve hâl eklerini ara.',[B_EK],
 'Her numaralı sözcüğü ek ek çöz; çoğul, iyelik ya da hâl eki olmayan sözcüğü bul.','Sözcüğün sonunda çoğul, iyelik ya da hâl eki yoksa çekim eki yoktur.')
# ===== K03 =====
dsoru('0009','K-DBYP-03','zor','İsimden fiil türeten yapım ekini tanır.',3,'Mastar ekleri (-mak, -mek) dikkate alınmamak koşuluyla, aşağıdaki sözcüklerden hangisi isimden fiil yapan bir ek almıştır?',
 [('okutmak',Z['okutmak']),('temizlemek',Z['temizlemek']),('sevinmek',Z['sevinmek']),('yazdırmak',Z['yazdırmak']),('döndürmek',Z['döndürmek'])],'B',lambda e:'isimden fiil' in e['tur'],lambda e:', '.join(e['tur']),
 lambda e:'isimden fiil yapan bir ek yoktur; ek '+', '.join(e['tur'])+' türündedir.',
 'İsimden fiil türeten yapım eki almış sözcük.','Kökü bul: kök isimse ve sözcük fiil olduysa ek isimden fiil yapar.',[B_TUR],
 'Kökün türüne bak: kök ad soylu, türeyen sözcük fiilse ek isimden fiil yapım ekidir.','Kök “-mak” almadan önce isimse ve sözcük fiil olduysa ek isimden fiil yapar.')
dsoru('0010','K-DBYP-03','kolay','Fiilden isim türeten yapım ekini tanır.',2,'Aşağıdaki sözcüklerden hangisi fiilden türetilmiş bir isimdir?',
 [('koşucu',Z['koşucu']),('gözlük',Z['gözlük']),('sessiz',Z['sessiz']),('balıkçı',Z['balıkçı']),('evsiz',Z['evsiz'])],'A',lambda e:'fiilden isim' in e['tur'],lambda e:', '.join(e['tur']),
 lambda e:'kökü isimdir; fiilden türememiştir.',
 'Fiilden türetilmiş isim.','Her sözcüğün kökünü bul; fiil kökü olanı (-mak alabilen) seç.',[B_TUR],
 'Kökü “-mak” alabilen (koş-, oku-, sat-) ve türeyen sözcüğü isim olan sözcük fiilden isimdir.','Fiil kökü + yapım eki = fiilden isim (okuyucu, satıcı).')
dsoru('0011','K-DBYP-03','zor','Ek sırasından ekin türlerini belirler.',4,'Aşağıdaki sözcüklerden hangisinde ekler sırasıyla isimden fiil ve fiilden isim türetmiştir?',
 [('gözlükçü',Z['gözlükçü']),('okuyucu',Z['okuyucu']),('balıkçılık',Z['balıkçılık']),('temizleyici',Z['temizleyici']),('sevindirici',Z['sevindirici'])],'D',lambda e:e['tur']==['isimden fiil','fiilden isim'],lambda e:' → '.join(e['tur']),
 lambda e:'ek türleri '+' → '.join(e['tur'])+' sırasındadır; “isimden fiil, fiilden isim” sırasına uymaz.',
 'Ek türleri sırasıyla isimden fiil ve fiilden isim olan sözcük.','Sözcüğü köke kadar çöz ve her ekin türünü soldan sağa yaz.',[B_TUR],
 'Her sözcüğü köke ayır, ekleri sırayla adlandır; dizi tam olarak “isimden fiil, fiilden isim” olmalı.','Ekleri soldan sağa tek tek adlandır.')
S12=[('Sessiz bir gecede dağcılar kampa döndü.',['sessiz','dağcılar'],False),
 ('Tuzlu çorbayı kimse içmedi.',['tuzlu'],False),
 ('Yeni satıcı bütün sebzeleri ucuza sattı.',['satıcı'],True),
 ('Evcil kediler akşam bahçede uyudu.',['evcil'],False),
 ('Kitaplıkta eski defterler duruyordu.',['kitaplıkta'],False)]
TD={'sessiz':'ses+siz (isimden isim)','dağcılar':'dağ+cı (isimden isim)','tuzlu':'tuz+lu (isimden isim)','satıcı':'sat-+ıcı (fiilden isim)','evcil':'ev+cil (isimden isim)','kitaplıkta':'kitap+lık (isimden isim)'}
S12o=[(m,dict(c=f"“{m}” → yapım ekli sözcükler: "+'; '.join(TD[w] for w in ws),fi=fi)) for m,ws,fi in S12]
dsoru('0012','K-DBYP-03','orta','Cümledeki yapım ekinin türünü belirler.',3,'Aşağıdaki cümlelerin hangisinde fiilden isim türeten bir yapım eki almış sözcük vardır?',
 S12o,'C',lambda e:e['fi'],lambda e:'fiilden isim ekli sözcük var' if e['fi'] else 'yalnız isimden isim ekleri',lambda e:'yapım ekli sözcükleri isimden isim türetir; fiilden isim yapan ek içermez.',
 'Fiilden isim yapım eki almış sözcük içeren cümle.','Cümledeki yapım ekli sözcüklerin köküne bak; kökü fiil olanı ara.',[B_TUR],
 'Her cümlede yapım eki almış sözcüğü bul, kökünün isim mi fiil mi olduğuna bak.','Kök fiilse (sat-, oku-, koş-) ek fiilden isim yapar.',
 islem_ad=lambda d,e:'Cümle '+'ABCDE'[[m for m,_ in S12o].index(d)])
# ===== K04 =====
S13=[('Bu yaz dedemle birlikte köye gideceğiz.','yönelme (köye), ilgeç “ile” (dedemle)',False),
 ('Çocuklar okuldan eve koşarak döndü.','okuldan: ayrılma hâli (-dan)',True),
 ('Annem pencerenin önüne yeni bir saksı koydu.','pencerenin: tamlayan (-in), önüne: yönelme (-e)',False),
 ('Elif’in defterinde güzel resimler vardı.','Elif’in: tamlayan, defterinde: bulunma hâli (-de)',False),
 ('Öğretmenimiz bize ödevi yarın verecek.','bize: yönelme, ödevi: belirtme (-i)',False)]
S13o=[(m,dict(c=f"“{m}” → {a}",ab=ab)) for m,a,ab in S13]
dsoru('0013','K-DBYP-04','kolay','Cümlede ayrılma hâli ekini bulur.',3,'Aşağıdaki cümlelerin hangisinde ayrılma hâli (-den, -dan) eki almış bir sözcük vardır?',
 S13o,'B',lambda e:e['ab'],lambda e:'ayrılma hâli var' if e['ab'] else 'ayrılma hâli yok',lambda e:'ayrılma hâli eki taşıyan bir sözcük yoktur; ekler başka hâllere aittir.',
 'Ayrılma hâli eki almış sözcük bulunan cümle.','Ayrılma hâli “nereden?” sorusunu yanıtlar; -den, -dan eklerini ara.',[B_EK,B('Hâl ekleri','belirtme -i · yönelme -e · bulunma -de · ayrılma -den · tamlayan (ilgi) -in')],
 'Cümlelerdeki ekleri hâl adlarıyla eşleştir; “-den/-dan” taşıyan sözcüğü bul.','Ayrılma hâli: “nereden?”, -den/-dan.',islem_ad=lambda d,e:'Cümle '+'ABCDE'[[m for m,_ in S13o].index(d)])
dsoru('0014','K-DBYP-04','kolay','İyelik eki almış sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisi iyelik eki almıştır?',
 [('evlerde',Z['evlerde']),('denizden',Z['denizden']),('masaya',Z['masaya']),('çocuklar',Z['çocuklar']),('defterim',Z['defterim'])],'E',lambda e:'iyelik' in e['c'],lambda e:'iyelik var' if 'iyelik' in e['c'] else 'iyelik yok',
 lambda e:'iyelik eki içermez; ekleri çoğul ya da hâl ekidir.','İyelik eki almış sözcük.','İyelik eki “kimin?” sorusuna yanıt verir: -im, -in, -i, -imiz…',[B_EK],
 'İyelik eki varlığın kime ait olduğunu bildirir (defter-im).','Sahiplik bildiren ek iyelik ekidir.')
O15=[('sessizlikten: ses + -lik + -siz + -ten',dict(c='Doğru sıra ses + -siz + -lik + -ten olmalıdır; yapım eklerinin sırası yanlış verilmiştir.',ok=False)),
 ('evlerimizden: ev + -ler + -imiz + -den',dict(c='evlerimizden: sıra çoğul + iyelik + hâl; doğru verilmiştir.',ok=True)),
 ('gözlüklerim: göz + -lük + -ler + -im',dict(c='gözlüklerim: yapım eki sonra çoğul ve iyelik; sıra doğrudur.',ok=True)),
 ('dağcılarımız: dağ + -cı + -lar + -ımız',dict(c='dağcılarımız: yapım, çoğul, iyelik sırası doğrudur.',ok=True)),
 ('balıkçıdan: balık + -çı + -dan',dict(c='balıkçıdan: yapım eki önce, hâl eki sonra; doğrudur.',ok=True))]
dsoru('0015','K-DBYP-04','orta','Ek sırası yanlış çözümlenmiş sözcüğü belirler.',4,'Aşağıdaki sözcüklerin hangisinde ekler sırası yanlış verilmiştir?',
 O15,'A',lambda e:not e['ok'],lambda e:'sıra doğru' if e['ok'] else 'sıra yanlış',lambda e:'çözümlemedeki ek sırası doğrudur.',
 'Ek sırası yanlış verilmiş çözümleme.','Önce yapım eklerini, sonra çoğul, iyelik ve hâl eklerini sırala.',[B_SIRA],
 'Türkçede yapım ekleri çekim eklerinden önce gelir; çekimde çoğul, iyelik, hâl sırası korunur; her çözümlemeyi bu sıraya göre denetle.','Sıra: yapım → çoğul → iyelik → hâl.',
 islem_ad=lambda d,e:d.split(':')[0])
# ===== K05 =====
G16=[('evlerim',dict(c='evlerim: gövde ev (basit); ev + -ler + -im, ekler çekim ekidir.',g='basit')),
 ('kitaplarda',dict(c='kitaplarda: gövde kitap (basit); ekler çekim ekidir.',g='basit')),
 ('başkentte',dict(c='başkentte: gövde başkent (birleşik); -te çekim ekidir.',g='birleşik')),
 ('gözlüklerim',dict(c='gözlüklerim: kök göz; gövde gözlük (türemiş: göz + -lük); ekler çoğul ve iyelik.',g='türemiş')),
 ('masalarımız',dict(c='masalarımız: gövde masa (basit); ekler çekim ekidir.',g='basit'))]
dsoru('0016','K-DBYP-05','orta','Sözcüğün gövdesinin yapısını belirler.',3,'Aşağıdaki sözcüklerden hangisinin gövdesi türemiş yapılıdır?',
 G16,'D',lambda e:e['g']=='türemiş',lambda e:'gövde '+e['g'],lambda e:'gövdesi '+e['g']+' yapılıdır; türemiş değildir.',
 'Gövdesi türemiş olan sözcük.','Çekim eklerini sözcükten at; geriye kalan gövdenin yapım eki alıp almadığına bak.',[B_GOV],
 'Çekim eklerini çıkar; kalan gövdede yapım eki varsa gövde türemiştir.','Gövde = kök + yapım ekleri; çekim ekleri gövdeye gelir.')
T17=[('kitaplıklarımızdan',Z['kitaplıklarımızdan']),('sessizliklerimizde',Z['sessizliklerimizde']),('balıkçılarımızdan',Z['balıkçılarımızdan']),('yolcularımızdan',Z['yolcularımızdan']),('sütçülerimizden',Z['sütçülerimizden'])]
dsoru('0017','K-DBYP-05','orta','Sözcüklerdeki toplam ek sayısını karşılaştırır.',4,'Aşağıdaki sözcüklerden hangisinde toplam ek sayısı en fazladır?',
 T17,'B',lambda e:e['ya']+e['ce']==5,lambda e:f"{e['ya']+e['ce']} ek",lambda e:f"toplam {e['ya']+e['ce']} ek vardır; en fazla olan değildir.",
 'Toplam ek sayısı en fazla olan sözcük.','Her sözcüğü köke kadar ayır; hem yapım hem çekim eklerini say.',[B_EK],
 'Yapım ve çekim eklerini birlikte say; en çok ekli sözcük aranan sözcüktür.','Önce kökü bul, sonra kalan eklerin hepsini say.')
dsoru('0018','K-DBYP-05','kolay','Kökü fiil olan sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisinin kökü fiildir?',
 [('gözlük',Z['gözlük']),('balıkçı',Z['balıkçı']),('kitaplık',Z['kitaplık']),('sessiz',Z['sessiz']),('okuyucu',Z['okuyucu'])],'E',lambda e:'fiilden isim' in e['tur'],lambda e:'kök '+e['k'].split(' ')[0],
 lambda e:'kökü isimdir; fiil kökü yoktur.','Kökü fiil olan sözcük.','Kökün “-mak/-mek” alıp alamadığına bak.',[B_TUR],'Kökü bulup “-mak/-mek” ekleyebiliyorsan kök fiildir.','Fiil kökü: oku-, koş-, sat-.')
# ===== K06 numaralı parça =====
tur_ad=lambda e:e['yapi']
psoru('0019','K-DBYP-06','orta','Numaralı sözcüklerden yapıca farklı olanı bulur.',3,
 'Kasabamızın en eski esnafı olan gözlükçü[1] Salih Usta yıllardır aynı dükkânda çalışır. Sabahları sessizlik[2] içinde camları siler. Öğleden sonra mahalledeki gecekondu[3] bölgesinden gelen müşterilere bakar. Her akşam sütçü[4] komşusuyla çay içer; hafta sonları ise sulu[5] bir yemek yapıp çocuklarını çağırır.',
 'Bu parçada numaralanmış sözcüklerden hangisi yapıca ötekilerden farklıdır?','C',lambda e:e['yapi']!='türemiş',tur_ad,lambda e:'türemiş yapılıdır; ötekilerle aynı gruptadır.',
 'Yapıca ötekilerden farklı olan numaralı sözcük.','Numaralı sözcüklerin her birini kök ve eklerine ayır.',[B_YAPI],
 'Dört sözcük kök + yapım ekinden oluşur; biri iki sözcüğün birleşmesidir.','Sözcüğün parçaları ek mi sözcük mü diye bak.')
psoru('0020','K-DBYP-06','orta','Numaralı sözcüklerden yapıca basit olanı bulur.',3,
 'Her yaz tatilinde dedemin köyüne giderdik. Köyün hemen yanındaki deniz[1] bizi çağırırdı. Sabahları balıkçı[2] amcalarla birlikte kayığa biner, öğleye doğru akıllı[3] bir çocuk gibi sessizce dönerdik. Akşamları yemeği kitaplık[4] bulunan odada, tuzlu[5] peynirle yerdik.',
 'Bu parçada numaralanmış sözcüklerden hangisi yapıca ötekilerden farklıdır?','A',lambda e:e['yapi']!='türemiş',tur_ad,lambda e:'türemiş yapılıdır; ötekilerle aynı gruptadır.',
 'Yapıca ötekilerden farklı olan numaralı sözcük.','Numaralı sözcüklerde yapım eki olup olmadığına bak.',[B_YAPI],
 'Dört sözcük yapım eki almıştır; biri ek almamış tek kökten oluşur.','Yapım eki almamış sözcük basittir.')
psoru('0021','K-DBYP-06','orta','Numaralı sözcüklerden fiilden türemiş olanı bulur.',3,
 'Kasabanın pazar yerinde sabahtan akşama kadar hareket vardır. Köşedeki çiçekçi[1] dükkânının önünde çocuklar toplanır. Bir yanda balıkçı[2] amcanın sesi yükselir, öbür yanda dağcı[3] gençler sırt çantalarını alır. Meyve tezgâhındaki satıcı[4] müşterilerine ikramda bulunurken sessizlik[5] hiç olmaz.',
 'Bu parçada numaralanmış sözcüklerden hangisi, kökü bakımından ötekilerden farklıdır?','D',lambda e:'fiilden isim' in e['tur'],lambda e:', '.join(e['tur']),lambda e:'kökü isimdir; ek isimden isim yapar, fiil kökü yoktur.',
 'Fiil kökünden türemiş numaralı sözcük.','Her sözcüğün kökünü bul; kök türü ötekilerden ayrılanı ara.',[B_TUR],
 'Dört sözcüğün kökü isimdir; birinin kökü fiildir.','Kökü “-mak” alabilen sözcük fiilden türemiştir.')
psoru('0022','K-DBYP-06','zor','Numaralı sözcüklerde yapım ve çekim eki sayısını karşılaştırır.',4,
 'Çocukluğumuzun geçtiği mahallede yaşlı komşular hep bir arada otururdu. Gözlüklerimiz[1] kırılınca birlikte tamire giderdik. Balıkçılar[2] sabah erkenden denize açılırdı, bizse dağlarda[3] koşardık. Hafta sonları evlerde[4] toplanıp radyo dinlerdik. Sessizlikte[5] bile sohbetin tadı başkaydı.',
 'Bu parçada numaralanmış sözcüklerden hangisinde yapım eki sayısı çekim eki sayısından fazladır?','E',lambda e:e['ya']>e['ce'],lambda e:tek(e['ya'],e['ce']),lambda e:'yapım eki sayısı çekim eki sayısından fazla değildir.',
 'Yapım eki sayısı çekim eki sayısından fazla olan numaralı sözcük.','Her sözcükte yapım ve çekim eklerini ayrı ayrı say, sonra karşılaştır.',[B_EK],
 'Her sözcüğün yapım ve çekim eklerini say; yapım sayısı büyük olanı seç.','Eşitlik fazlalık sayılmaz.')
psoru('0023','K-DBYP-06','zor','Numaralı sözcüklerden türemiş olmayanı bulur.',4,
 'Yaz akşamları sahil boyunca uzun yürüyüşler yaparız. Sessizlikte[1] dalgaların sesi daha güzel gelir. Denizlerde[2] yüzen balıklar gibi hafif adımlarla ilerleriz. Gözlüklerim[3] tuzdan lekelenir, onları her seferinde silerim. Yoldaki dağcılara[4] selam veririz. Sofradaki tuzlukta[5] kalan son tuzu da yemeğe katarız.',
 'Bu parçada numaralanmış sözcüklerden hangisi türemiş yapılı değildir?','B',lambda e:e['yapi']!='türemiş',tur_ad,lambda e:'yapım eki almıştır; türemiş yapılıdır.',
 'Türemiş yapılı olmayan numaralı sözcük.','Çekim eklerini at; gövdede yapım eki kalıyor mu bak.',[B_YAPI,B_EK],
 'Çekim eklerini çıkar; gövdede yapım eki olmayan sözcük türemiş değildir.','Çekim eki sözcüğü türemiş yapmaz.')
psoru('0024','K-DBYP-06','zor','Numaralı sözcüklerde yapım eklerinin sırasını (ek türlerini) değerlendirir.',4,
 'Babam yıllarca esnaflık yaptı. Gözlükçülük[1] mesleğini babasından öğrenmişti. Amcam ise balıkçılık[2] yaparak ailenin geçimine katkı sağladı. Satıcılık[3] ise ikisinin de ortak yeteneğiydi. İş yerlerinde sessizlik[4] pek bulunmaz, müşteriler sürekli gelirdi. Dükkânı temizleyici[5] bir görevli her akşam silip süpürürdü.',
 'Bu parçada numaralanmış sözcüklerden hangisinde önce fiilden isim, sonra isimden isim yapan ek bulunur?','C',lambda e:e['tur']==['fiilden isim','isimden isim'],lambda e:' → '.join(e['tur']),lambda e:'ek türleri '+' → '.join(e['tur'])+' sırasındadır; “fiilden isim, isimden isim” sırasına uymaz.',
 'Ek türleri sırasıyla fiilden isim ve isimden isim olan numaralı sözcük.','Her sözcüğü köke kadar çöz, ek türlerini soldan sağa yaz.',[B_TUR],
 'Kökü fiil olan ve sonra isimden isim eki alan sözcüğü bul.','Kök fiilse ilk ek fiilden isim olabilir.')
psoru('0025','K-DBYP-06','kolay','Numaralı sözcüklerden birleşik yapılı olanı bulur.',3,
 'Eski bir apartmanın üst katında oturuyorum. Pencerenin önündeki masa[1] her zaman çiçeklerle doludur. Sabahları sessiz[2] bir sokakta yürürüm. Yolda sütçü[3] dükkânından geçip karabiber[4] ve tuz alırım. Akşamları sütlü[5] bir kahve içip kitap okurum.',
 'Bu parçada numaralanmış sözcüklerden hangisi birleşik yapılıdır?','D',lambda e:e['yapi']=='birleşik',tur_ad,lambda e:'birleşik yapılı değildir; '+e['yapi']+' yapılıdır.',
 'Birleşik yapılı numaralı sözcük.','Parçaları ek mi sözcük mü diye ayır; iki sözcükten oluşanı bul.',[B_YAPI],
 'İki ayrı sözcüğün kaynaşmasıyla oluşan sözcük birleşiktir.','Parçaların ikisi de anlamlı sözcükse birleşiktir.')
psoru('0026','K-DBYP-06','zor','Numaralı sözcüklerden isimden fiil türeten ek almış olanı bulur.',3,
 'Hafta sonu bütün aile evi temizledi[1]. Komşumuz küçük kızına ders okuttu[2]. Sütçü[3] amca kapıya gelip bize taze süt verdi. Annem ağlayan kardeşimi susturdu[4]. Akşam gelen misafirler hepimizi sevindirdi[5].',
 'Bu parçada numaralanmış sözcüklerden hangisi isimden fiil türeten bir yapım eki almıştır?','A',lambda e:'isimden fiil' in e['tur'],lambda e:', '.join(e['tur']),lambda e:'ek '+', '.join(e['tur'])+' türündedir; isimden fiil yapmaz.',
 'İsimden fiil yapım eki almış numaralı sözcük.','Fiil olan numaralı sözcüğün kökünün isim olup olmadığına bak.',[B_TUR],
 'Fiil olan sözcüğün kökü isimse ek isimden fiil yapmıştır.','Kök isim, türeyen sözcük fiil: isimden fiil.')
bitir(Q)
