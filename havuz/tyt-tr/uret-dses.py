"""TYT Türkçe · Ses Bilgisi genişletmesi: 16 soru (hafif mod). Metinler özgündür.
Ünlü uyumu denetimi ve ses olayı etiketleri kodla tutulur; şık açıklamaları sözlükten üretilir."""
import sys,os,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hafif_db import *
KY='ÖSYM TYT Türkçe 2018–2026 · Bilgi Sarmal Dil Bilgisi SB (ÖSYM Tipi) · TDK Yazım Kılavuzu'
def K(alt,fikir,tuzak,zor,kalip,adim,tip): return dict(alt=alt,fikir=fikir,tuzak=tuzak,zorluk=zor,kalip=kalip,adim=adim,tipId=tip,kaynak=KY)
KARTLAR={
 'K-DBSS-01':K('Büyük ve Küçük Ünlü Uyumu','Sözcüğün ve ekin büyük ya da küçük ünlü uyumuna uyup uymadığını ünlüleri sınıflayarak belirlemek; uyuma girmeyen ekleri (-ken, -yor, -ki, -leyin) tanımak.','Ekten gelen aykırılığı kökten gelen sanmak; küçük ünlü uyumunu hiç denetlememek.','orta','düz',3,'dss-uyum'),
 'K-DBSS-02':K('Ünlü Düşmesi ve Daralması','Ünlü düşmesini (ağız → ağzı) ve ünlü daralmasını (başlıyor, diyor) ötekilerden ayırmak.','Bağlama ünlüsünü (geliyor, yazıyor) daralma sanmak; yumuşamayla düşmeyi karıştırmak.','orta','düz',3,'dss-unlu'),
 'K-DBSS-03':K('Ünsüz Yumuşaması ve Benzeşmesi','p, ç, t, k’nin yumuşamasını ve eklerdeki sertleşmeyi (benzeşme) birbirinden ayırmak; ikisini birlikte taşıyan sözcüğü bulmak.','Yumuşamayı benzeşme sanmak; yumuşama göstermeyen sözcükleri (sepeti, topu) yumuşamış saymak.','orta','düz',3,'dss-unsuz'),
 'K-DBSS-04':K('Ünsüz Düşmesi, Türemesi ve Kaynaştırma','Ünsüz düşmesi (küçülmek), ünsüz türemesi (hakkı) ve kaynaştırma ünsüzlerini ayırt etmek.','Ünsüz türemesini yumuşama sanmak; kaynaştırmayı ünsüz türemesi saymak.','orta','düz',4,'dss-dusme'),
 'K-DBSS-05':K('Ses Olayı Eşleştirme ve Numaralı Parça','Sözcüğün karşısındaki ses olayının adını doğrulamak; numaralı parçada ses olayı olmayan ya da farklı olan sözcüğü bulmak; ulamayı tanımak.','Ünlü daralmasını ünlü düşmesi sanmak; ünlü ünlüye çarpan söyleyişi ulama saymak.','zor','öncüllü',4,'dss-eslestirme'),
}
TIPLER={'dss-uyum':'Büyük ve küçük ünlü uyumu','dss-unlu':'Ünlü düşmesi ve daralması','dss-unsuz':'Ünsüz yumuşaması ve benzeşmesi','dss-dusme':'Ünsüz düşmesi, türemesi, kaynaştırma','dss-eslestirme':'Ses olayı eşleştirme ve numaralı parça'}
Q=kur('dses','Ses Bilgisi','tr|Ses Bilgisi',KARTLAR,TIPLER); Q.n=16
# ---- ünlü uyumu denetimi (kodla) ----
UN='aeıioöuü'; KALIN='aıou'; DUZ='aeıi'; YUV='oöuü'
def buyuk(s):
    v=[c for c in s if c in UN]; return all(x in KALIN for x in v) or all(x not in KALIN for x in v)
def kucuk(s):
    v=[c for c in s if c in UN]
    for p,x in zip(v,v[1:]):
        if p in DUZ and x not in DUZ: return False
        if p in YUV and x not in 'aeuü': return False
    return True
for w,b,k in [('gözlükçü',1,1),('okullarda',1,1),('kavunlar',1,0),('kitaplık',0,1),('ağaçlık',1,1),('anne',0,1),('okur',1,1),('okurken',0,1),('kitaplar',0,1),('evlerde',1,1),('dağlarda',1,1),('kalemler',0,1),('kapı',1,1),('ağaç',1,1),('yıldız',1,1),('gözlük',1,1)]:
    assert (buyuk(w),kucuk(w))==(bool(b),bool(k)),w
def sz(l): return l
# ---- ses olayı sözlüğü ----
OLAY={'udus':'ünlü düşmesi','udar':'ünlü daralması','yum':'ünsüz yumuşaması','ben':'ünsüz benzeşmesi','unsd':'ünsüz düşmesi','unst':'ünsüz türemesi','kay':'kaynaştırma'}
S={}
def s(w,c,*o): S[w]=dict(w=w,c=f'{w}: {c}',o=set(o))
s('ağzı','ağız + -ı → ünlü düşmesi (ağız’daki ı düşer)','udus')
s('burnu','burun + -u → ünlü düşmesi (burun’daki u düşer)','udus')
s('resmi','resim + -i → ünlü düşmesi (resim’deki i düşer)','udus')
s('omzu','omuz + -u → ünlü düşmesi (omuz’daki u düşer)','udus')
s('kaybı','kayıp + -ı → ünlü düşmesi (ı düşer) ve ünsüz yumuşaması (p → b)','udus','yum')
s('kitabı','kitap + -ı → ünsüz yumuşaması (p → b)','yum')
s('ağacı','ağaç + -ı → ünsüz yumuşaması (ç → c)','yum')
s('ayağı','ayak + -ı → ünsüz yumuşaması (k → ğ)','yum')
s('kanadı','kanat + -ı → ünsüz yumuşaması (t → d)','yum')
s('ağacın','ağaç + -ın → ünsüz yumuşaması (ç → c)','yum')
s('çocuğu','çocuk + -u → ünsüz yumuşaması (k → ğ)','yum')
s('sepeti','sepet + -i → ek ünlüyle başlıyor ama sözcük yumuşamaz; ses olayı yoktur')
s('evi','ev + -i → ünsüz yumuşaması yok, ünlü düşmesi yok; ses olayı yoktur')
s('okula','okul + -a → ses olayı yoktur')
s('kitapta','kitap + -ta → ünsüz benzeşmesi (-da → -ta)','ben')
s('sokaktan','sokak + -tan → ünsüz benzeşmesi (-dan → -tan)','ben')
s('yaprakta','yaprak + -ta → ünsüz benzeşmesi (-da → -ta)','ben')
s('kitapçığı','kitap + -çık + -ı → ünsüz benzeşmesi (-cık → -çık) ve ünsüz yumuşaması (k → ğ)','ben','yum')
s('küçülmek','küçük + -ül- + -mek → ünsüz düşmesi (küçük’teki k düşer)','unsd')
s('kısalmak','kısa + -l- + -mak → ünsüz düşmesi yok')
s('güzelleşmek','güzel + -leş- + -mek → ünsüz düşmesi yok')
s('sarılmak','sar- + -ıl- + -mak → ünsüz düşmesi yok')
s('yazdırmak','yaz- + -dır- + -mak → ünsüz düşmesi yok')
s('hakkı','hak + -ı → ünsüz türemesi (k ikizleşir)','unst')
s('sırrı','sır + -ı → ünsüz türemesi (r ikizleşir)','unst')
s('hissi','his + -i → ünsüz türemesi (s ikizleşir)','unst')
s('affı','af + -ı → ünsüz türemesi (f ikizleşir)','unst')
s('zamanı','zaman + -ı → ses olayı yoktur; ünsüz türemesi görülmez')
s('diyor','de- + -yor → ünlü daralması (e → i)','udar')
s('başlıyor','başla- + -yor → ünlü daralması (a → ı)','udar')
s('geliyor','gel- + -i- + -yor → -i- bağlama ünlüsüdür; daralma yoktur')
s('okuyor','oku- + -yor → ünlü daralması yok (kök ünlüsü u değişmemiş)')
s('yazıyor','yaz- + -ı- + -yor → -ı- bağlama ünlüsüdür; daralma yoktur')
s('gülüyor','gül- + -ü- + -yor → -ü- bağlama ünlüsüdür; daralma yoktur')
s('bakkala','bakkal + -a → çift ünsüz (ll) kökte vardır, sonradan türememiştir; ünsüz türemesi yoktur')
s('diyerek','de- + -yerek → ünlü daralması (e → i)','udar')
s('mutfağa','mutfak + -a → ünsüz yumuşaması (k → ğ)','yum')
s('odaya','oda + -ya → kaynaştırma ünsüzü y','kay')
s('masaya','masa + -ya → kaynaştırma ünsüzü y','kay')
s('masaya_','masa + -ya → kaynaştırma ünsüzü y','kay')
s('evlerimizde','ev + -ler + -imiz + -de → ses olayı yoktur')
S['yaptı']=dict(w='yaptı',c='yaptı: yap- + -tı → ünsüz benzeşmesi (-dı → -tı)',o={'ben'})
def ol(e,k): return k in e['o']
def ad(e): return ', '.join(OLAY[x] for x in sorted(e['o'])) or 'ses olayı yok'
# ---- parça ----
def parca(txt):
    ws=[]
    def f(m):
        w=(m.group(1) or m.group(3)); ws.append(w.lower()); i=len(ws)-1; n=int(m.group(2) or m.group(4)); assert n==i+1,txt[:30]
        return f'{w} ({ROM[i]})'
    return re.sub(r'\{([^}]+)\}\[(\d)\]|([^\s\[\]{}]+)\[(\d)\]',f,txt),ws
def dsoru(no,kart,zor,kazanim,adim,kok,siklar,harf,pred,kisa,neden,istenen,ip,bilgi,kural,puf,kalip='düz',on='',islem_ad=None,ad2=None):
    opts=[(d,e,'' if pred(e) else f"{e['c'].rstrip('.')} → {neden(e)}",'islem') for d,e in siklar]
    dg=[(d,e) for d,e in siklar if pred(e)][0]
    adm=[A('Ölçütü belirle',kural,istenen[:60]),
        A('Şıkları tek tek çözümle',*(ad2 or ('Her şıkkı ses olaylarına göre çözümleyip ölçüte göre sına.',' · '.join(f"{(islem_ad or (lambda d,e:d))(d,e)}: {kisa(e)}" for d,e in siklar)))),
        A('Sonucu bul',f"{dg[1]['c'].rstrip('.')}. Ölçüt yalnız bu şıkta sağlanır.",f"{dg[0]}: {kisa(dg[1])}")]
    soru(Q,no,kart,zor,kazanim,adim,on+kok,opts,harf,lambda e:pred(e),istenen,ip,bilgi,adm,puf,kalip=kalip)
def psoru(no,kart,zor,kazanim,adim,txt,kok,harf,pred,kisa,neden,istenen,ip,bilgi,kural,puf,tablo=None):
    disp,ws=parca(txt); assert len(ws)==5,(no,ws)
    T=tablo or S
    for w in ws: assert w in T,(no,w)
    sik=[(ROM[i],T[w]) for i,w in enumerate(ws)]
    dsoru(no,kart,zor,kazanim,adim,kok,sik,harf,pred,kisa,neden,istenen,ip,bilgi,kural,puf,kalip='öncüllü',on=disp+'\n\n',islem_ad=lambda d,e:f"{d} ({e['w']})")
B_UYUM=B('Ünlü uyumları','büyük ünlü uyumu: sözcükteki ünlüler hep kalın (a ı o u) ya da hep ince (e i ö ü) · küçük ünlü uyumu: düz ünlüden sonra düz, yuvarlak ünlüden sonra a, e, u, ü gelir · -ken, -yor, -ki, -leyin ünlü uyumuna girmez (okurken, gülüyor)')
B_UDUS=B('Ünlü düşmesi / daralması','ünlü düşmesi: ağız → ağzı, resim → resmi, kayıp → kaybı · ünlü daralması: -yor ekinden önceki a/e daralır: başla- → başlıyor, de- → diyor; geliyor, yazıyor’daki ı/i bağlama ünlüsüdür')
B_UNS=B('Ünsüz yumuşaması / benzeşmesi','yumuşama: p, ç, t, k → b, c, d, ğ (kitap → kitabı, ağaç → ağacı); sepet → sepeti, top → topu gibi bazı sözcükler yumuşamaz · benzeşme: sert ünsüzden sonra ek sertleşir (-da → -ta: kitapta, -cı → -çı: kitapçı)')
B_DUS=B('Ünsüz düşmesi / türemesi / kaynaştırma','düşme: küçük + -ül- → küçülmek · türeme: hak → hakkı, af → affı, sır → sırrı, his → hissi · kaynaştırma: ünlüyle biten sözcüğe ünlüyle başlayan ek gelirken araya y, s, ş, n girer (masa+ya, oda+sı)')
B_OLAY=B('Ses olayları','ünlü düşmesi · ünlü daralması · ünsüz yumuşaması · ünsüz benzeşmesi · ünsüz düşmesi · ünsüz türemesi · kaynaştırma · ulama (ünsüzle biten sözcükten sonra ünlüyle başlayan sözcük gelince söyleyişte kaynaşma: bir elma → bi-rel-ma)')
# ============ K01 ============
U1=[('kitaplar',dict(w='kitaplar',c='kitaplar: kök kitap, i–a ünlüleriyle büyük ünlü uyumuna uymaz; aykırılık kökten gelir',k=False,t=False)),
 ('evlerde',dict(w='evlerde',c='evlerde: e–e–e ünlüleri hep ince; uyuma uyar',k=True,t=True)),
 ('okurken',dict(w='okurken',c='okurken: kök oku- (o–u kalın) uyumlu; -ken eki kalın köke ince e ile gelir, uyuma girmez',k=True,t=False)),
 ('dağlarda',dict(w='dağlarda',c='dağlarda: a–a–a ünlüleri hep kalın; uyuma uyar',k=True,t=True)),
 ('kalemler',dict(w='kalemler',c='kalemler: kök kalem, a–e ünlüleriyle uyuma uymaz; aykırılık kökten gelir',k=False,t=False))]
for w,e in U1: assert (buyuk(w[:-3] if w=='okurken' else w) if w in('okurken',) else True)
dsoru('0001','K-DBSS-01','orta','Büyük ünlü uyumunun bozulmasının ekten mi kökten mi kaynaklandığını ayırt eder.',3,'Aşağıdaki sözcüklerin hangisinde büyük ünlü uyumunun bozulması yalnız ekten kaynaklanır?',
 U1,'C',lambda e:e['k'] and not e['t'],lambda e:'kök ✓ ek ✗' if (e['k'] and not e['t']) else ('uyuyor' if e['t'] else 'kök ✗'),lambda e:'uyuyor, aykırılık yok.' if e['t'] else 'bozulma kökten gelir, ekten gelmez.',
 'Uyum bozukluğu yalnız ekten gelen sözcük.','Önce kökün uyumlu olup olmadığına bak; sonra eki ekle ve uyumun bozulup bozulmadığına bak.',[B_UYUM],
 'Kökü tek başına denetle; kök uyumlu, sözcük uyumsuzsa bozulma ekten gelir.','-ken, -yor, -ki, -leyin ünlü uyumuna girmez.')
W2=[('gözlükçü',True,True,'ö–ü–ü: hepsi ince; ö → ü, ü → ü küçük uyuma uygun'),('kavunlar',True,False,'a–u–a hepsi kalın; fakat düz a’dan sonra yuvarlak u geliyor, küçük ünlü uyumuna uymaz'),
 ('okullarda',True,True,'o–u–a–a hepsi kalın; yuvarlak ünlüden sonra u, a gelmiş; iki uyuma da uyar'),('kitaplık',False,True,'kitap kökü i–a ünlüleriyle büyük ünlü uyumuna uymaz'),('ağaçlık',True,True,'a–a–ı hepsi kalın ve düz; iki uyuma da uyar')]
for w,b,k,_ in W2: assert (buyuk(w),kucuk(w))==(b,k),w
SET2={'I ve II':{0,1},'II ve IV':{1,3},'III ve V':{2,4},'I, III ve V':{0,2,4},'I, II ve III':{0,1,2}}
OK2={i for i,(w,b,k,_) in enumerate(W2) if b and k}
assert OK2=={0,2,4}
def n2(v):
    f=sorted(v-OK2); m=sorted(OK2-v)
    return '; '.join([f"{ROM[i]}. {W2[i][0]} iki uyuma birden uymuyor ({W2[i][3]})" for i in f]+[f"{ROM[i]}. {W2[i][0]} iki uyuma da uyduğu hâlde alınmamış" for i in m])
dsoru('0002','K-DBSS-01','orta','Öncüllerdeki sözcüklerin büyük ve küçük ünlü uyumuna uyup uymadığını belirler.',3,'Yukarıdaki sözcüklerden hangileri hem büyük hem küçük ünlü uyumuna uyar?',
 [(k,dict(c=k,s=v,n=n2(v))) for k,v in SET2.items()],'D',lambda e:e['s']==OK2,lambda e:'doğru küme' if e['s']==OK2 else 'küme tutmuyor',lambda e:e['n'],
 'İki ünlü uyumuna birden uyan sözcükler.','Önce ünlülerin hepsi kalın ya da ince mi diye bak; sonra düz–yuvarlak sıralamasını denetle.',[B_UYUM],
 'Her sözcüğün ünlülerini sırala; önce kalın–ince denetimi, sonra düz–yuvarlak denetimi yap.','Büyük uyuma uymayan sözcük küçük uyuma bakmadan elenir.',
 kalip='öncüllü',on='I. gözlükçü\nII. kavunlar\nIII. okullarda\nIV. kitaplık\nV. ağaçlık\n\n',
 ad2=('Ünlüleri yaz: I ö–ü–ü · II a–u–a · III o–u–a–a · IV i–a–ı · V a–a–ı.','I: iki uyum ✓ · II: küçük ✗ · III: iki uyum ✓ · IV: büyük ✗ · V: iki uyum ✓'))
dsoru('0003','K-DBSS-01','kolay','Büyük ünlü uyumuna uymayan sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisi büyük ünlü uyumuna uymaz?',
 [('kapı',dict(w='kapı',c='kapı: a–ı ünlüleri kalındır; uyar',u=True)),('anne',dict(w='anne',c='anne: a kalın, e ince; büyük ünlü uyumuna uymaz',u=False)),('ağaç',dict(w='ağaç',c='ağaç: a–a ünlüleri kalındır; uyar',u=True)),('yıldız',dict(w='yıldız',c='yıldız: ı–ı ünlüleri kalındır; uyar',u=True)),('gözlük',dict(w='gözlük',c='gözlük: ö–ü ünlüleri incedir; uyar',u=True))],'B',lambda e:not e['u'],lambda e:'uyar' if e['u'] else 'uymaz',lambda e:'ünlüleri aynı kalınlıkta; büyük ünlü uyumuna uyar.',
 'Büyük ünlü uyumuna uymayan sözcük.','Ünlüleri tek tek yaz; hepsi kalın ya da hepsi ince mi diye bak.',[B_UYUM],
 'Ünlüleri kalın (a ı o u) ve ince (e i ö ü) diye sınıfla; karışık olan sözcük uyuma uymaz.','Kalın–ince karışıksa büyük ünlü uyumu bozulur.')
# ============ K02 ============
dsoru('0004','K-DBSS-02','kolay','Ünlü düşmesi olan sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisinde ünlü düşmesi vardır?',
 [('ağzı',S['ağzı']),('evi',S['evi']),('okula',S['okula']),('kanadı',S['kanadı']),('odaya',S['odaya'])],'A',lambda e:ol(e,'udus'),ad,
 lambda e:'ünlü düşmesi görülmez; '+('başka ses olayı: '+ad(e) if e['o'] else 'ses olayı yoktur')+'.',
 'Ünlü düşmesi bulunan sözcük.','Ekle birleşince kökteki bir ünlünün kaybolup kaybolmadığına bak.',[B_UDUS],
 'Ek gelince kökün ikinci hecesindeki ünlü düşüyorsa ünlü düşmesi vardır (ağız → ağzı).','ağız → ağzı: kök ünlüsünü yitirir.')
dsoru('0005','K-DBSS-02','orta','Ünlü daralması olan sözcüğü belirler.',3,'Aşağıdaki sözcüklerden hangisinde ünlü daralması vardır?',
 [('geliyor',S['geliyor']),('okuyor',S['okuyor']),('yazıyor',S['yazıyor']),('gülüyor',S['gülüyor']),('diyor',S['diyor'])],'E',lambda e:ol(e,'udar'),ad,
 lambda e:'daralma yoktur; '+e['c'].split('→')[1].strip(),
 'Ünlü daralması bulunan sözcük.','-yor ekinden önce a ya da e ile biten kök, ünlüsünü daraltır.',[B_UDUS],
 'Köke -yor gelince kökün sonundaki a/e ı/i/u/ü’ye dönüşüyorsa daralma vardır; ünsüzle biten köklerdeki ı, i, u, ü bağlama ünlüsüdür.','de- → diyor, başla- → başlıyor.')
W6=['kaybı','ağzı','kanadı','ağacı','resmi']
SET6={'I ve II':{0,1},'I, II ve V':{0,1,4},'II, III ve IV':{1,2,3},'III ve IV':{2,3},'I, III ve IV':{0,2,3}}
OK6={i for i,w in enumerate(W6) if 'udus' in S[w]['o']}
assert OK6=={0,1,4}
def n6(v):
    f=sorted(v-OK6); m=sorted(OK6-v)
    return '; '.join([f"{ROM[i]}. {W6[i]}: ünlü düşmesi yok ({OLAY[sorted(S[W6[i]]['o'])[0]]})" for i in f]+[f"{ROM[i]}. {W6[i]}: ünlü düşmesi olduğu hâlde alınmamış" for i in m])
dsoru('0006','K-DBSS-02','zor','Öncüllerdeki sözcüklerde ünlü düşmesi olanları (yumuşamayla birlikte olanı da) bulur.',4,'Yukarıdaki sözcüklerin hangilerinde ünlü düşmesi vardır?',
 [(k,dict(c=k,s=v,n=n6(v))) for k,v in SET6.items()],'B',lambda e:e['s']==OK6,lambda e:'doğru küme' if e['s']==OK6 else 'küme tutmuyor',lambda e:e['n'],
 'Ünlü düşmesi olan sözcüklerin hangileri olduğu.','Her sözcüğün kökünü yaz; ek gelince kökteki ünlü kayboluyor mu?',[B_UDUS],
 'kaybı (kayıp+ı) hem düşme hem yumuşama taşır; kanadı ve ağacı yalnız yumuşamadır.','Ünlü kaybı varsa düşme; yalnız ünsüz değişimi varsa yumuşama.',
 kalip='öncüllü',on='I. kaybı\nII. ağzı\nIII. kanadı\nIV. ağacı\nV. resmi\n\n',
 ad2=('Kökleri yaz: I kayıp+ı · II ağız+ı · III kanat+ı · IV ağaç+ı · V resim+i.','I: ı düşer ✓ · II: ı düşer ✓ · III: yalnız t→d ✗ · IV: yalnız ç→c ✗ · V: i düşer ✓'))
# ============ K03 ============
S7=[('Elif saksıyı pencerenin önüne koydu.','saksıyı: kaynaştırma (y); benzeşme yok',False),
 ('Çocuklar bahçede dün akşam top oynuyordu.','bahçede: bahçe ünlüyle biter, ek -de sertleşmez; benzeşme yok',False),
 ('Akşam yemeğini sokakta yedik.','sokakta: -da → -ta ünsüz benzeşmesi',True),
 ('Ağacın gölgesinde bir süre dinlendik.','ağacın: ünsüz yumuşaması; benzeşme yok',False),
 ('Annem pazardan taze sebze aldı.','pazardan: pazar r (ötümlü) ile biter, ek -dan sertleşmemiş; benzeşme yok',False)]
dsoru('0007','K-DBSS-03','orta','Cümlede ünsüz benzeşmesi olan sözcüğü bulur.',3,'Aşağıdaki cümlelerin hangisinde ünsüz benzeşmesi (sertleşme) olan bir sözcük vardır?',
 [(m,dict(c=f'“{m}” → {a}',b=b)) for m,a,b in S7],'C',lambda e:e['b'],lambda e:'benzeşme var' if e['b'] else 'benzeşme yok',lambda e:'ünsüz benzeşmesi görülmez.',
 'Ünsüz benzeşmesi bulunan sözcük içeren cümle.','Sert ünsüzle biten sözcüğe gelen ekin c, d, g yerine ç, t, k ile başlayıp başlamadığına bak.',[B_UNS],
 'Sert ünsüzle (f s t k ç ş h p) biten sözcüğe gelen -da, -dan, -cı gibi eklerde d/c/g’nin t/ç/k’ye dönüşüp dönüşmediğini denetle.','Ek sertleşiyorsa benzeşme, kök yumuşuyorsa yumuşamadır.',
 islem_ad=lambda d,e:'Cümle '+'ABCDE'[[x[0] for x in S7].index(d)])
dsoru('0008','K-DBSS-03','orta','Ünsüz yumuşaması göstermeyen sözcüğü belirler.',3,'Aşağıdaki sözcüklerden hangisinde ünsüz yumuşaması yoktur?',
 [('ağacı',S['ağacı']),('kitabı',S['kitabı']),('ayağı',S['ayağı']),('kanadı',S['kanadı']),('sepeti',S['sepeti'])],'E',lambda e:not ol(e,'yum'),ad,lambda e:'ünsüz yumuşaması vardır ('+re.search(r'\((\S+ → \S+)\)',e['c']).group(1)+').',
 'Ünsüz yumuşaması olmayan sözcük.','Ekle birleşince kök sonundaki p, ç, t, k’nin b, c, d, ğ’ye dönüşüp dönüşmediğine bak.',[B_UNS],
 'Dört sözcükte p, ç, k, t yumuşamıştır; biri ünlüyle başlayan eki alsa da sert ünsüzünü korur.','sepet → sepeti: t yumuşamaz.')
T9={'kitapçığı':S['kitapçığı'],'sokaktan':S['sokaktan'],'ağacın':S['ağacın'],'kanadı':S['kanadı'],'yaprakta':S['yaprakta']}
psoru('0009','K-DBSS-03','zor','Numaralı sözcüklerden hem yumuşama hem benzeşme olanı bulur.',4,
 'Dedem yıllar önce kendi yazdığı kitapçığı[1] bana armağan etti. Her sabah sokaktan[2] geçen çocuklar penceremize bakardı. Evimizin önündeki ağacın[3] gölgesinde otururduk. Kuşlar gelirdi, kanadı[4] kırık bir serçeyi de getirirlerdi. Sonbaharda yaprakta[5] kalan son damlayı izlerdik.',
 'Bu parçada numaralanmış sözcüklerden hangisinde hem ünsüz yumuşaması hem ünsüz benzeşmesi görülür?','A',lambda e:ol(e,'yum') and ol(e,'ben'),ad,lambda e:'iki ses olayını birlikte taşımaz ('+ad(e)+').',
 'Hem yumuşama hem benzeşme olan numaralı sözcük.','Her sözcüğü köküne ve eklerine ayır; hem kök sonu yumuşuyor hem ek sertleşiyorsa o sözcüğü seç.',[B_UNS],
 'Her numaralı sözcüğün hangi ses olaylarını taşıdığını yaz; ikisi birden olan sözcük aranan sözcüktür.','kitapçık + ı: hem -cık → -çık hem k → ğ.',tablo=T9)
# ============ K04 ============
dsoru('0010','K-DBSS-04','kolay','Ünsüz düşmesi olan sözcüğü belirler.',2,'Aşağıdaki sözcüklerden hangisinde ünsüz düşmesi vardır?',
 [('kısalmak',S['kısalmak']),('küçülmek',S['küçülmek']),('güzelleşmek',S['güzelleşmek']),('sarılmak',S['sarılmak']),('yazdırmak',S['yazdırmak'])],'B',lambda e:ol(e,'unsd'),ad,lambda e:'ünsüz düşmesi görülmez.',
 'Ünsüz düşmesi olan sözcük.','Kök ile ek birleşince köke ait bir ünsüzün kaybolup kaybolmadığına bak.',[B_DUS],
 'küçük + -ül- → küçülmek: kökteki k düşer.','Ek gelince kökün sonundaki ünsüz kayboluyorsa ünsüz düşmesidir.')
dsoru('0011','K-DBSS-04','zor','Ünsüz türemesi olmayan sözcüğü belirler.',3,'Aşağıdaki sözcüklerin hangisinde ünsüz türemesi yoktur?',
 [('hakkı',S['hakkı']),('sırrı',S['sırrı']),('hissi',S['hissi']),('bakkala',S['bakkala']),('affı',S['affı'])],'D',lambda e:not ol(e,'unst'),ad,lambda e:'ünsüz türemesi (ikizleşme) vardır.',
 'Ünsüz türemesi olmayan sözcük.','Ek gelince kökün son ünsüzünün ikizleşip ikizleşmediğine bak.',[B_DUS],
 'hak → hakkı, sır → sırrı, his → hissi, af → affı gibi sözcüklerde son ünsüz ikizleşir; bakkal → bakkala’da çift ünsüz kökte vardır, sonradan türememiştir.','Son ünsüz ikizleşiyorsa ünsüz türemesi vardır.')
S12=[('Kardeşim çantayı omzuna astı.','çantayı: kaynaştırma (y); omzuna: ünlü düşmesi (omuz → omzu) ve kaynaştırma (n)',True,True),
 ('Annem çiçeği vazoya koydu.','çiçeği: yumuşama; vazoya: kaynaştırma (y); ünlü düşmesi yok',False,True),
 ('Dün okula yürüyerek gittik.','yürüyerek: kaynaştırma (y); ünlü düşmesi yok',False,True),
 ('Ayağı yaralanan sporcu sedyeye alındı.','ayağı: yumuşama; sedyeye: kaynaştırma (y); ünlü düşmesi yok',False,True),
 ('Bahçeden gelen sesi duydum.','kaynaştırma yok, ünlü düşmesi yok',False,False)]
dsoru('0012','K-DBSS-04','zor','Cümlede hem ünlü düşmesi hem kaynaştırma bulunduğunu belirler.',4,'Aşağıdaki cümlelerin hangisinde hem ünlü düşmesi hem kaynaştırma örneği vardır?',
 [(m,dict(c=f'“{m}” → {a}',d=d,k=k)) for m,a,d,k in S12],'A',lambda e:e['d'] and e['k'],lambda e:('düşme '+('✓' if e['d'] else '✗')+' kaynaştırma '+('✓' if e['k'] else '✗')),lambda e:'iki ses olayını birlikte taşımaz.',
 'Hem ünlü düşmesi hem kaynaştırma bulunan cümle.','Cümledeki sözcükleri ünlü kaybı ve araya giren y, s, ş, n bakımından sına.',[B_DUS,B_UDUS],
 'Önce ünlü düşmesi olan sözcüğü (omuz → omzu), sonra ünlüyle biten sözcüğe gelen ekin kaynaştırma ünsüzünü ara.','Ünlüyle biten sözcük + ünlüyle başlayan ek arasında y, s, ş, n varsa kaynaştırmadır.',
 islem_ad=lambda d,e:'Cümle '+'ABCDE'[[x[0] for x in S12].index(d)])
# ============ K05 ============
E13=[('ağzı – ünlü düşmesi',dict(c='ağzı: ağız + -ı; ağız’daki ünlü düşer',ok=True)),('ayağı – ünsüz yumuşaması',dict(c='ayağı: ayak + -ı; k → ğ',ok=True)),
 ('başlıyor – ünlü düşmesi',dict(c='başlıyor: başla- + -yor; a → ı bir ünlü daralmasıdır, düşme değil',ok=False)),('küçülmek – ünsüz düşmesi',dict(c='küçülmek: küçük + -ül-; k düşer',ok=True)),('hakkı – ünsüz türemesi',dict(c='hakkı: hak + -ı; k ikizleşir',ok=True))]
dsoru('0013','K-DBSS-05','orta','Sözcük–ses olayı eşleştirmesinde yanlış eşleşmeyi bulur.',4,'Aşağıdaki sözcüklerden hangisinin karşısında yazılan ses olayı yanlıştır?',
 E13,'C',lambda e:not e['ok'],lambda e:'eşleşme doğru' if e['ok'] else 'eşleşme yanlış',lambda e:'bu eşleşme doğrudur; aranan yanlış eşleşme değildir.',
 'Ses olayı yanlış eşleştirilmiş sözcük.','Her sözcükte kökün ve ekin ne yaptığını yaz; ses olayının adı onunla uyuşuyor mu?',[B_OLAY],
 'Ünlü kayboluyorsa düşme; ünlü başka ünlüye (a/e → ı/i) dönüşüyorsa daralmadır.','Düşme: ünlü yok olur. Daralma: ünlü başka ünlüye dönüşür.',
 islem_ad=lambda d,e:d.split(' – ')[0])
T14={'sepeti':S['sepeti'],'sokakta':S['kitapta'],'mutfağa':S['mutfağa'],'diyerek':S['diyerek'],'omzu':S['omzu']}
T14['sokakta']=dict(S['kitapta'],w='sokakta',c='sokakta: sokak + -ta → ünsüz benzeşmesi (-da → -ta)')
psoru('0014','K-DBSS-05','orta','Numaralı sözcüklerden ünlü düşmesi olanı bulur.',3,
 'Hafta sonu dedemin evine gittik. Dedem sepeti[1] masanın üstüne bırakıp bizi bahçeye çağırdı. Sokakta[2] oynayan çocukları izledik. Annem sofrayı hazırlarken kardeşim tabakları mutfağa[3] taşıdı. Babam “Yarın da gelin,” diyerek[4] bizi uğurladı. Küçük kardeşimin omzu[5] ağrıyormuş.',
 'Bu parçada numaralanmış sözcüklerden hangisinde ünlü düşmesi vardır?','E',lambda e:ol(e,'udus'),ad,lambda e:'ünlü düşmesi görülmez; ses olayı: '+ad(e)+'.',
 'Ünlü düşmesi olan numaralı sözcük.','Her numaralı sözcükte ek gelince kökten bir ünlünün düşüp düşmediğine bak.',[B_UDUS],
 'Her numaralı sözcüğün ses olayını adlandır; ünlü düşmesi olanı seç.','omuz → omzu: kök ünlüsü düşer.',tablo=T14)
T15={'ağzı':S['ağzı'],'kitapta':S['kitapta'],'sırrı':S['sırrı'],'evlerimizde':S['evlerimizde'],'ayağı':S['ayağı']}
psoru('0015','K-DBSS-05','orta','Numaralı sözcüklerden ses olayı bulunmayanı belirler.',4,
 'Yaz tatilinde dedemin köyüne gittik. Ağzı[1] kulaklarına varan çocuklar bizi karşıladı. Akşam yemeğinden sonra kitapta[2] okuduğumuz oyunları oynadık. Gece olunca herkes küçük bir sırrı[3] saklamaya söz verdi. Evlerimizde[4] bile yapmadığımız şeyleri orada yapmak güzeldi. Dönüşte kardeşimin ayağı[5] burkulunca onu sırtımızda taşıdık.',
 'Bu parçada numaralanmış sözcüklerden hangisinde herhangi bir ses olayı görülmez?','D',lambda e:not e['o'],ad,lambda e:'ses olayı vardır: '+ad(e)+'.',
 'Hiçbir ses olayı taşımayan numaralı sözcük.','Her numaralı sözcüğü kök ve eklerine ayırıp ünlü ya da ünsüz değişimi var mı diye sına.',[B_OLAY],
 'Dört sözcükte bir ses olayı vardır (düşme, benzeşme, kaynaştırma, yumuşama); biri kökünü ve ekini aynen korur.','Kök ve ek aynen korunuyorsa ses olayı yoktur.',tablo=T15)
U16={'dört elma':dict(w='dört elma',c='dört elma: t + e → ünsüzle biten sözcükten sonra ünlüyle başlayan sözcük; ulama vardır',u=True),'bir arkadaş':dict(w='bir arkadaş',c='bir arkadaş: r + a → ulama vardır',u=True),
 'yedi ördek':dict(w='yedi ördek',c='yedi ördek: i + ö → ünlüyle biten sözcükten sonra ünlü gelir; ünsüz–ünlü birleşmesi olmadığı için ulama yoktur',u=False),
 'kış akşamları':dict(w='kış akşamları',c='kış akşamları: ş + a → ulama vardır',u=True),'bir akşam':dict(w='bir akşam',c='bir akşam: r + a → ulama vardır',u=True)}
psoru('0016','K-DBSS-05','orta','Numaralı söz öbeklerinden ulama olmayanı bulur.',3,
 'Annem pazardan {dört elma}[1] aldı. Kapıda {bir arkadaş}[2] bekliyordu. Masada {yedi ördek}[3] yumurtası duruyordu. Ocakta {kış akşamları}[4] hep çorba kaynardı. Yarın {bir akşam}[5] yemeğine davetliyiz.',
 'Bu parçadaki numaralanmış söz öbeklerinden hangisinde söyleyişte ulama yoktur?','C',lambda e:not e['u'],lambda e:'ulama var' if e['u'] else 'ulama yok',lambda e:'bu öbekte ulama vardır; aranan öbek değildir.',
 'Ulama olmayan numaralı söz öbeği.','Her öbekte birinci sözcüğün sonuna ve ikinci sözcüğün başına bak.',[B_OLAY],
 'Ulama için öbekte ünsüzle biten sözcüğü ünlüyle başlayan sözcük izlemelidir.','ünsüz + ünlü = ulama; ünlü + ünlü ulama değildir.',tablo=U16)
bitir(Q)
