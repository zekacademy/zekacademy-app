"""pyapi (Paragrafın Yapısı) yardımcıları · hafif mod. Her şık etiketlenir, tek doğru şık assert edilir.
Yapı sorularında doğruluk bağlaç / gönderim sözcüğü / düşünce akışı etiketleriyle, sıralamada brute-force ile gösterilir."""
import sys,os,random,re,itertools
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tr_ortak import *

KY='ÖSYM TYT Türkçe 2018–2026 · Paraf İQ · Sıfır Risk (paragrafın yapısı)'
KARTLAR={
 'K-PYA-01':dict(alt='Tamamlama: Giriş Cümlesi',fikir='Boşluk paragrafın başındaysa cümle konuyu açmalı, bağlaç/gönderme taşımamalı ve sonraki cümlelerin dayandığı kavramı hazırlamalıdır.',tuzak='Konuya yakın ama sonraki cümleyle bağ kurmayan cümleyi seçmek; başta “bu yüzden, ancak” gibi öncül isteyen cümleyi doğru saymak.',zorluk='orta',kalip='düz',adim=3,tipId='pya-tamgiris',kaynak=KY),
 'K-PYA-02':dict(alt='Tamamlama: Ortadaki Boşluk',fikir='Boşluğun hem önündeki hem arkasındaki cümleyle bağ (bağlaç, zamir, düşünce yönü) kurmak.',tuzak='Yalnız önceki cümleye uyan şıkkı seçip sonraki cümlenin “bu, böyle, oysa” gibi göndermesini atlamak.',zorluk='orta',kalip='düz',adim=3,tipId='pya-tamorta',kaynak=KY),
 'K-PYA-03':dict(alt='Tamamlama: Sonuç Cümlesi',fikir='Paragrafın sonundaki boşluğa, öncekilerden çıkan sonucu ya da genel yargıyı veren cümleyi getirmek.',tuzak='Parçanın söylediğinden fazlasını (aşırı genelleme) ya da yan düşünceyi sonuç yapan şıkkı seçmek.',zorluk='orta',kalip='düz',adim=3,tipId='pya-tamsonuc',kaynak=KY),
 'K-PYA-04':dict(alt='Düşüncenin Akışını Bozan Cümle',fikir='Parçanın odağını belirleyip bu odaktan sapan cümleyi, bağlaç ve gönderme zincirini izleyerek bulmak.',tuzak='Parçayla aynı anahtar sözcüğü taşıyan ama farklı bir yönü anlatan cümleyi uygun sanmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='pya-akis',kaynak=KY),
 'K-PYA-05':dict(alt='Paragrafı İkiye Bölme',fikir='Konunun ya da bakış açısının değiştiği cümleyi (yeni bir yön, “peki, öte yandan, gelelim”) bulup ikinci paragrafın başlangıcı yapmak.',tuzak='Zamir ya da bağlaçla öncekine bağlı cümlede paragrafı ayırmak.',zorluk='orta',kalip='öncüllü',adim=3,tipId='pya-bolme',kaynak=KY),
 'K-PYA-06':dict(alt='Cümle Sıralama',fikir='Zamir, bağlaç ve zaman/neden–sonuç ilişkileriyle cümleler arasındaki zorunlu öncelikleri bulup tek tutarlı sırayı kurmak.',tuzak='Genel görünen cümleyi hemen başa koymak; “hemen ardından gelmek zorunda” olan cümle çiftini ayırmak.',zorluk='orta',kalip='öncüllü',adim=4,tipId='pya-siralama',kaynak=KY),
 'K-PYA-07':dict(alt='Giriş Cümlesi Olabilen / Olamayan Cümle',fikir='Giriş cümlesi kendi başına anlaşılır olmalı; zamir, gönderme sözcüğü ya da öncekine dayanan bağlaç taşıyan cümle giriş olamaz.',tuzak='Cümle ortasındaki iç bağlacı (ama, oysa) öncüle bağlı sanmak; “aynı, söz konusu” gibi örtük göndermeleri kaçırmak.',zorluk='orta',kalip='düz',adim=3,tipId='pya-giris',kaynak=KY),
}
TIPLER={'pya-tamgiris':'Tamamlama: giriş cümlesi','pya-tamorta':'Tamamlama: ortadaki boşluk','pya-tamsonuc':'Tamamlama: sonuç cümlesi','pya-akis':'Düşüncenin akışını bozan cümle','pya-bolme':'Paragrafı ikiye bölme','pya-siralama':'Cümle sıralama','pya-giris':'Giriş cümlesi olabilen / olamayan cümle'}
Q=Konu('pyapi','Paragraf','tr|Paragraf',KARTLAR,TIPLER)
AD=A

B_TG=B('Boşluk başta (giriş)','giriş cümlesi konuyu açar, öncül istemez; sonraki cümleler ona bağlanır. Örnek: “Su hiç tükenmez, biçim değiştirir.” ardından döngü anlatılır')
B_TO=B('Boşluk ortada','önceki cümleyle düşünce yönü, sonraki cümleyle bağlaç/zamir uyuşmalı. Örnek: sonrası “Bu yüzden …” diye başlıyorsa boşluk bir neden/durum bildirmelidir')
B_TS=B('Boşluk sonda (sonuç)','son cümle öncekilerden çıkan sonucu ya da özeti verir; parçada olmayan yeni bir bilgi ya da aşırı genelleme getirmez. Örnek: “Kısacası …”')
B_AK=B('Akışı bozan cümle','parçanın odağını bul; konuyla aynı sözcüğü taşısa da odaktan başka bir yöne geçen cümle akışı bozar. Örnek: sağlıklı beslenme anlatılırken market fiyatlarına geçmek')
B_BO=B('Paragraf bölme','yeni paragraf, konunun ya da bakış açısının değiştiği cümlede başlar (“peki, öte yandan, gelelim, ikinci olarak”). “Bu, böylece, çünkü” gibi öncekine bağlanan cümle paragrafı başlatmaz')
B_SI=B('Cümle sıralama','zamir (bu, onlar), bağlaç (çünkü, ancak, böylece) ve zaman sözcükleri bir cümlenin yerini belirler. Örnek: “Bunun yerine …” cümlesi, önerilen yöntemin anlatıldığı cümleden sonra gelir')
B_GI=B('Giriş cümlesi','paragrafı başlatan cümle kendi başına anlaşılmalıdır. “Bu, şu, ancak, ayrıca, böylece, söz konusu” gibi öncüle dayanan sözcük taşıyan cümle giriş olamaz')

ROMS=ROM
ORD={1:'ilk',2:'ikinci',3:'üçüncü',4:'dördüncü',5:'beşinci'}
BAGIMLI=['bu','şu','o','onlar','bunlar','şunlar','bunun','buna','bunu','bundan','bunda','bunların','böylece','böyle','ancak','ayrıca','oysa','çünkü','üstelik','nitekim','dolayısıyla','yine','öte','söz','aynı','diğer','öteki','sonuç','kısacası','ne','buna','bunca','bu tür','işte','peki','ama','fakat','lakin','ise','de','da','ki']
BAGIMLI_KATI=['bu','şu','onlar','bunlar','şunlar','bunun','buna','bunu','bundan','bunların','böylece','böyle','ancak','ayrıca','oysa','çünkü','üstelik','nitekim','dolayısıyla','söz konusu','aynı','diğer','öteki','kısacası','işte','peki','fakat','lakin','yine de','öte yandan','sonuç olarak','bunca','ne var ki','tersine','bununla','bunlara','bunlarla','bunların']

def _sozc(s): return re.findall(r'[a-zçğıöşü]+',s.lower().replace('İ','i').replace('I','ı'))
def bagimli_mi(s):
    t=' '.join(_sozc(s))
    return [b for b in BAGIMLI_KATI if re.search(rf'(?<![a-zçğıöşü]){b}(?![a-zçğıöşü])',t)]

def yerlestir(harf,dogru,yanlislar):
    L='ABCDE'; o=list(yanlislar); o.insert(L.index(harf),dogru); assert len(o)==5; return o

def soru_(no,kart,zor,kazanim,kalip,adim,metin,opts,harf,pred,istenen,ip,bilgi,adimlar,puf):
    """opts: A–E sırasıyla (metin, etiket, cel, tur). Tek şık pred'i sağlamalı ve harf olmalı."""
    assert len(opts)==5 and len(set(o[0] for o in opts))==5,no
    ok=[i for i,o in enumerate(opts) if pred(o[1])]
    assert len(ok)==1 and 'ABCDE'[ok[0]]==harf,(no,ok,harf)
    yan=[(o[0],o[2],o[3]) for i,o in enumerate(opts) if i!=ok[0]]
    for m,c,t in yan: assert c and len(c)>=12 and t in TURLER,(no,m)
    assert 3<=len(adimlar)<=5 and isinstance(ip,str) and metin.rstrip().endswith('?'),no
    c=Q.kartlar[kart]; tipId=c['tipId']
    sk,h,cel,tur=sikla(opts[ok[0]][0],yan,harf)
    Q.P.R(no,tipId,Q.tipler[tipId],zor,c['alt'],kazanim,kalip,adim,f"{kart} ({c['alt']}) · özgün metin",metin,sk,h,istenen,[ip],bilgi,adimlar,puf,cel,tur)
    Q.say=getattr(Q,'say',{}); Q.say[no]=(tipId,zor,harf)

ADIM={'kolay':2,'orta':3,'zor':4}
NEDEN={'baglac':'bağlaç/gönderme uyumsuz','akis':'akışı tersine çevirir ya da çelişir','konu':'konudan sapar'}

# ---------- tamamlama ----------
KOK_TAM='Bu parçada boş bırakılan yere aşağıdakilerden hangisi getirilmelidir?'
KOK_SON='Bu parça aşağıdaki cümlelerden hangisiyle tamamlanabilir?'
def tam(no,zor,konum,par,dogru,yan,harf,cevre,gerekce,ip,puf,kok=None):
    """par: '........' tek boşluklu parça. yan: 4 × (metin, {baglac,akis,konu: bool}, cel, tur). Doğru: üç etiket de True."""
    assert par.count('........')==1,no
    if konum=='giris': assert par.startswith('........')
    elif konum=='sonuc': assert par.rstrip().endswith('........')
    else: assert not par.startswith('........') and not par.rstrip().endswith('........')
    n=len(re.findall(r'\w+',par.replace('........',dogru)))
    assert 55<=n<=165 and (zor!='zor' or 100<=n<=150),(no,n)
    for m,f,c,t in yan:
        assert set(f)=={'baglac','akis','konu'} and not all(f.values()),(no,m)
    assert len(dogru)<=max(len(y[0]) for y in yan) and not all(len(dogru)>len(y[0]) for y in yan),(no,'doğru şık en uzun')
    kart={'giris':'K-PYA-01','orta':'K-PYA-02','sonuc':'K-PYA-03'}[konum]
    ok=dict(baglac=True,akis=True,konu=True)
    opts=yerlestir(harf,(dogru,ok,'',''),[(m,f,c,t) for m,f,c,t in yan])
    def neden(f): return ' + '.join(NEDEN[k] for k in ('baglac','akis','konu') if not f[k])
    sirala=' · '.join(f"{'ABCDE'[i]}: {'uygun' if o[1]==ok else neden(o[1])}" for i,o in enumerate(opts))
    yer={'giris':'Boşluk parçanın başında; cümle konuyu açmalı ve sonrakilere zemin hazırlamalı.','orta':'Boşluk ortada; hem önceki hem sonraki cümleyle bağ kurmalı.','sonuc':'Boşluk sonda; cümle öncekilerden çıkan sonucu ya da özeti vermeli.'}[konum]
    adimlar=[AD('Boşluğun yerini belirle',yer,{'giris':'başta → konuyu aç','orta':'ortada → iki yana bağ','sonuc':'sonda → sonuç'}[konum]),
             AD('Çevresini oku',cevre[0],cevre[1]),
             AD('Şıkları sına','Her şık bağlaç/gönderme uyumu, düşünce yönü ve konu bakımından denenir.',sirala),
             AD('Seçimi doğrula',gerekce,f'{harf}: doğru')]
    kk=kok or (KOK_SON if konum=='sonuc' else KOK_TAM)
    soru_(no,kart,zor,{'giris':'Paragrafın başındaki boşluğa konuyu açan cümleyi getirir.','orta':'Boşluğun öncesi ve sonrasıyla bağ kurarak boşluğa gelecek cümleyi belirler.','sonuc':'Paragrafın sonuna öncekilerden çıkan cümleyi getirir.'}[konum],
          'düz',ADIM[zor],par+'\n'+kk,opts,harf,lambda e:e==ok,'Boşluğa gelecek cümle.',ip,[{'giris':B_TG,'orta':B_TO,'sonuc':B_TS}[konum]],adimlar,puf)

# ---------- akış bozan ----------
def akis(no,zor,cum,roller,bozan,odak,bozan_ac,cikar,ip,puf,kok=None):
    """cum: 5 cümle; roller: 5 × (rol, bağ sözcüğü ya da ''); bozan: 0–4."""
    assert len(cum)==5 and len(roller)==5 and roller[bozan][0]=='sapma',no
    for c,(r,b) in zip(cum,roller):
        if b: assert b in c,(no,b)
    assert sum(r=='sapma' for r,_ in roller)==1
    n=len(re.findall(r'\w+',' '.join(cum))); assert 50<=n<=160 and (zor!='zor' or 100<=n<=150),(no,n)
    metin=' '.join(f'({ROM[i]}) {c}' for i,c in enumerate(cum))+'\n'+(kok or 'Bu parçadaki numaralanmış cümlelerden hangisi düşüncenin akışını bozmaktadır?')
    opts=[]
    for i in range(5):
        r,b=roller[i]
        cel='' if i==bozan else f'{ROM[i]}. cümle parçanın odağına hizmet eder ({r}); akışı bozmaz.'
        opts.append((ROM[i],r,cel,'' if i==bozan else 'dikkat'))
    ozet=' · '.join(f'{ROM[i]}: {"sapma" if i==bozan else "odakta"}' for i in range(5))
    adimlar=[AD('Odağı bul',odak,'odak belirlendi'),
             AD('Cümleleri tek tek sına','Her cümlenin bağlaç ya da gönderme sözcüğüne bakıp önceki cümleyle bağını izle.',ozet),
             AD('Sapmayı yakala',bozan_ac,f'{ROM[bozan]}: odak dışı'),
             AD('Çıkararak doğrula',cikar,f'{ROM[bozan]} yok → akış sürer')]
    soru_(no,'K-PYA-04',zor,'Parçanın odağını belirleyip düşüncenin akışını bozan cümleyi bulur.','öncüllü',ADIM[zor],metin,opts,'ABCDE'[bozan],lambda e:e=='sapma',
          'Akışı bozan cümle.',ip,[B_AK],adimlar,puf)

# ---------- paragraf bölme ----------
def bolme(no,zor,cum,isaret,odak1,odak2,ip,puf,kok=None):
    """cum: 6 cümle. isaret: 6 × (tur, işaret sözcüğü, açıklama); tur 'bas' (ilk) / 'devam' / 'yeni'. Seçenekler II–VI."""
    assert len(cum)==6 and len(isaret)==6 and isaret[0][0]=='bas'
    yeni=[i for i,x in enumerate(isaret) if x[0]=='yeni']; assert len(yeni)==1 and yeni[0]>=1,no
    kes=yeni[0]
    for c,(t,m,a) in zip(cum,isaret):
        if m: assert m in c,(no,m)
        if t=='yeni': assert a.startswith('“'),(no,'açıklama alıntıyla başlamalı',a)
    n=len(re.findall(r'\w+',' '.join(cum))); assert 60<=n<=165 and (zor!='zor' or 100<=n<=150),(no,n)
    metin=' '.join(f'({ROM[i]}) {c}' for i,c in enumerate(cum))+'\n'+(kok or 'Bu parça iki paragrafa ayrılmak istense ikinci paragraf numaralanmış cümlelerin hangisiyle başlar?')
    opts=[]
    for i in range(1,6):
        t,m,a=isaret[i]
        opts.append((ROM[i],t,'' if t=='yeni' else f'{ROM[i]}. cümle {a}; konu sürdüğü için ikinci paragraf buradan başlamaz.','' if t=='yeni' else 'dikkat'))
    t,m,a=isaret[kes]
    adimlar=[AD('Konuyu izle',odak1,'1. paragraf: önceki konu'),
             AD('Kırılma noktasını bul',f'{ROM[kes]}. cümledeki {a}.',f'{ROM[kes]}: yeni yön'),
             AD('Sonrasını doğrula',odak2,(f'{ROM[kes]}–{ROM[5]}: yeni paragraf' if kes<5 else f'{ROM[5]}: yeni paragraf')),
             AD('Diğer şıkları ele','Diğer cümleler zamir, bağlaç ya da aynı konunun sürmesiyle öncekine bağlıdır.',' · '.join(f'{ROM[i]}: devam' for i in range(1,6) if i!=kes))]
    soru_(no,'K-PYA-05',zor,'Konunun değiştiği cümleyi bularak parçayı iki paragrafa ayırır.','öncüllü',ADIM[zor],metin,opts,'ABCDE'[kes-1],lambda e:e=='yeni',
          'İkinci paragrafı başlatan cümle.',ip,[B_BO],adimlar,puf)

# ---------- sıralama ----------
def sira(no,zor,cum,kurallar,roller,konum,harf,baglar,ip,puf,seed):
    """cum: doğru sıradaki 5 cümle. kurallar: (tip,a,b,ipucu,açıklama); tip: once|hemen|ilk|son (indeksler doğru sıradadır).
    Tüm 120 sıra taranır; kuralları sağlayan tek sıra cum'un sırası olmalıdır. konum: >0 baştan, <0 sondan."""
    n=len(cum); assert n==5 and len(roller)==5
    nw=len(re.findall(r'\w+',' '.join(cum))); assert zor!='zor' or 100<=nw<=150,(no,nw)
    def tamam(p):
        pos={x:i for i,x in enumerate(p)}
        for tip,a,b,_,_ in kurallar:
            if tip=='once' and not pos[a]<pos[b]: return False
            if tip=='hemen' and pos[b]!=pos[a]+1: return False
            if tip=='ilk' and pos[a]!=0: return False
            if tip=='son' and pos[a]!=n-1: return False
        return True
    for tip,a,b,ip_,ac in kurallar:
        if tip in('once','hemen'): assert ip_ in cum[b],(no,ip_)
        elif ip_: assert ip_ in cum[a],(no,ip_)
        if tip=='ilk': assert not bagimli_mi(cum[a]),(no,'ilk cümle bağımlı',bagimli_mi(cum[a]))
        assert len(ac)>=8
    sol=[p for p in itertools.permutations(range(n)) if tamam(p)]
    assert sol==[tuple(range(n))],(no,'tek tutarlı sıra değil',sol[:5],len(sol))
    p=konum if konum>0 else n+konum+1      # 1 tabanlı konum
    dogru_idx=p-1
    rng=random.Random(seed); L='ABCDE'
    while True:
        perm=list(range(n)); rng.shuffle(perm)   # perm[d] = ekran numarası d+1'de görünen cümlenin doğru-sıra indeksi
        if perm!=list(range(n)) and perm[L.index(harf)]==dogru_idx: break
    metin=' '.join(f'({ROM[d]}) {cum[perm[d]]}' for d in range(n))
    dizi=[ROM[perm.index(j)] for j in range(n)]       # doğru sıradaki ekran numaraları
    if konum==1: kok='Bu cümleler anlamlı bir paragraf oluşturacak biçimde sıralandığında paragraf hangi cümleyle başlar?'
    elif konum==-1: kok='Bu cümleler anlamlı bir paragraf oluşturacak biçimde sıralandığında paragraf hangi cümleyle biter?'
    elif konum>0: kok=f'Bu cümleler anlamlı bir bütün oluşturacak biçimde sıralandığında baştan {ORD[konum]} cümle hangisi olur?'
    else: kok=f'Bu cümleler anlamlı bir bütün oluşturacak biçimde sıralandığında sondan {ORD[-konum]} cümle hangisi olur?'
    opts=[]
    for d in range(n):
        j=perm[d]
        cel='' if j==dogru_idx else f'{ROM[d]}. cümle doğru sırada {j+1}. sıradadır ({roller[j]}); istenen sırada değildir.'
        opts.append((ROM[d],j,cel,'' if j==dogru_idx else 'dikkat'))
    ilk=[k for k in kurallar if k[0]=='ilk']
    adimlar=[AD('Girişi bul',(ilk[0][4] if ilk else 'Önce hiçbir zamir ya da bağlaç taşımayan, konuyu açan cümleyi ara.'),f'başlangıç: {ROM[perm.index(0)]}'),
             AD('Bağlantıları kur',baglar,'zamir/bağlaç zinciri'),
             AD('Sırayı yaz','Zincir kurulunca ekrandaki numaralarla sıra yazılır.',' – '.join(dizi)),
             AD('İstenen sırayı bul',f'Sorunun istediği sıradaki cümlenin numarası cevaptır.',f'cevap: {ROM[perm.index(dogru_idx)]}')]
    soru_(no,'K-PYA-06',zor,'Zamir ve bağlaçlardan yararlanarak cümleleri anlamlı bir bütün oluşturacak biçimde sıralar.','öncüllü',ADIM[zor] if zor!='kolay' else 3,metin+'\n'+kok,opts,harf,lambda e:e==dogru_idx,
          'İstenen sıradaki cümle.',ip,[B_SI],adimlar,puf)
    Q.sira_kayit=getattr(Q,'sira_kayit',{}); Q.sira_kayit[no]=len(sol)

# ---------- giriş cümlesi olabilen / olamayan ----------
def giris(no,zor,mod,dogru,yan,harf,ip,puf,kok=None):
    """mod 'olamaz': doğru = bağımlı cümle (dogru=(metin,işaret)); yan = 4 bağımsız (metin,cel,tur).
    mod 'olabilir': doğru = bağımsız cümle (dogru=(metin,'')); yan = 4 bağımlı (metin,işaret,cel,tur)."""
    L='ABCDE'
    if mod=='olamaz':
        dm,dis=dogru; assert dis and dis in dm and bagimli_mi(dm),(no,'doğru bağımlı değil')
        for m,c,t in yan: assert not bagimli_mi(m),(no,'bağımsız sanılan cümle bağımlı',m,bagimli_mi(m))
        opts=yerlestir(harf,(dm,'dep','',''),[(m,'ind',c,t) for m,c,t in yan]); pred=lambda e:e=='dep'
        kk=kok or 'Aşağıdakilerden hangisi bir paragrafın giriş cümlesi olamaz?'
        ac=f'“{dis}” sözcüğü önceden söylenmiş bir şeye gönderme yapar; bu cümle paragrafı başlatamaz.'
        ayak=' · '.join(f'{L[i]}: {"öncüle bağlı" if o[1]=="dep" else "bağımsız"}' for i,o in enumerate(opts))
        istenen='Giriş cümlesi olamayan cümle.'
    else:
        dm,_=dogru; assert not bagimli_mi(dm),(no,'doğru bağımlı',bagimli_mi(dm))
        for m,mk,c,t in yan: assert mk in m and bagimli_mi(m),(no,'bağımlı sanılan cümlede işaret yok',m)
        opts=yerlestir(harf,(dm,'ind','',''),[(m,'dep',c,t) for m,mk,c,t in yan]); pred=lambda e:e=='ind'
        kk=kok or 'Aşağıdakilerden hangisi bir paragrafın giriş cümlesi olabilir?'
        ac='Bu cümle zamir, gönderme sözcüğü ya da öncekine dayanan bağlaç taşımaz; kendi başına anlaşılır.'
        ayak=' · '.join(f'{L[i]}: {"bağımsız" if o[1]=="ind" else "öncüle bağlı"}' for i,o in enumerate(opts))
        istenen='Giriş cümlesi olabilen cümle.'
    allm=[o[0] for o in opts]; cor=[o[0] for o in opts if pred(o[1])][0]
    assert not all(len(cor)>len(m) for m in allm if m!=cor),(no,'doğru en uzun')
    adimlar=[AD('Ölçütü hatırla','Giriş cümlesi öncekine dayanmaz: zamir (bu, şu), gönderme (söz konusu, aynı) ya da bağlaç (ancak, ayrıca) taşımaz.','giriş = bağımsız cümle'),
             AD('Şıkları tara','Her şıkta cümlenin başına ve içine bakıp öncüle bağlayan sözcük var mı diye ara.',ayak),
             AD('Sonucu bul',ac,f'{harf}: doğru')]
    soru_(no,'K-PYA-07',zor,'Bir cümlenin paragraf başında kullanılıp kullanılamayacağını bağlaç ve gönderme sözcüklerine bakarak belirler.','düz',ADIM[zor],kk,opts,harf,pred,istenen,ip,[B_GI],adimlar,puf)

def bitir_(cikti,n):
    for q in Q.P.ANA: q['kardes']=None
    kl=[]
    for kid,c in Q.kartlar.items():
        kl.append(dict(id=kid,konu=Q.konu_adi,alt=c['alt'],fikir=c['fikir'],tuzak=c['tuzak'],zorluk=c['zorluk'],kalip=c['kalip'],adim=c['adim'],tipId=c['tipId'],tip=Q.tipler[c['tipId']],kaynak=c['kaynak']))
    tl=[dict(tipId=t,ad=ad,kartlar=[k for k,c in Q.kartlar.items() if c['tipId']==t],uygulamaKonu=Q.k) for t,ad in Q.tipler.items()]
    json.dump(dict(konu=Q.konu_adi,surum=1,kartlar=kl,tipler=tl),open(f'{HAVUZ}/kartlar/pyapi.json','w'),ensure_ascii=False,indent=1)
    Q.P.yaz(cikti,'/tmp/bos-pyapi.json')
    assert len(Q.P.ANA)==n,(len(Q.P.ANA),n)
