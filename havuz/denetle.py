"""Soru havuzu denetleyicisi. Kullanım: python3 havuz/denetle.py havuz/tyt-mat/*.json [--benzerlik osym.json yayin.json]
Her soruyu kayıt standartlarına göre kontrol eder; HATA varsa çıkış kodu 1."""
import json,re,sys,os,glob
from fractions import Fraction
from collections import Counter,defaultdict
H=os.path.dirname(os.path.abspath(__file__))
TIP={t['tipId']:t for ks in json.load(open(f'{H}/kartlar/soru-tipleri.json'))['konular'].values() for t in ks}
KART={}
for f in glob.glob(f'{H}/kartlar/*.json'):
    d=json.load(open(f))
    for k in d.get('kartlar',[]): KART[k['id']]=k
UYG={'mat|Temel Kavramlar','mat|Rasyonel Sayılar','mat|Sayı Basamakları','mat|Bölme ve Bölünebilme','mat|Ebob – ekok','mat|Basit Eşitsizlikler','mat|Mutlak Değer','mat|Üslü Sayılar','mat|Köklü Sayılar','mat|Çarpanlara Ayırma','mat|Oran Orantı','mat|Denklem Çözme'}
ZOR={'kolay','orta','zor'}; KALIP={'düz','hikâyeli','öncüllü','tablo','grafik','şekilli','yeni nesil'}
GEREK=['id','ders','konu','k','kazanim','tipId','tip','zorluk','seviye','kalip','adimSayisi','metin','sekil','siklar','cevap','celdiriciler','istenen','bilgi','ipuclari','adimlar','puf','kaynakKart','dogrulama']
def sayi(v):
    v=v.replace('−','-').replace(',','.').strip()
    try: return Fraction(v)
    except Exception: return None
def norm(s): return re.findall(r'[a-zçğıöşü0-9]+',s.lower().replace('İ','i').replace('I','ı'))
def sh(s,n=4):
    w=norm(s); return {' '.join(w[i:i+n]) for i in range(max(0,len(w)-n+1))}
def denetle(Q,korpus=None):
    hata=[];uyari=[]
    ids=Counter(q.get('id') for q in Q)
    for q in Q:
        i=q.get('id','?'); H_=lambda m:hata.append(f'{i}: {m}'); U=lambda m:uyari.append(f'{i}: {m}')
        for g in GEREK:
            if g not in q: H_(f'eksik alan {g}')
        if ids[i]>1: H_('tekrar eden id')
        if not re.fullmatch(r'tytmat-[a-z]+-\d{4}k?',i): H_('id biçimi')
        if i.endswith('k') and not q.get('ana'): H_('kardeş sorunun ana bağlantısı yok')
        if q.get('kisaYol') is not None and (not isinstance(q['kisaYol'],str) or len(q['kisaYol'])<20): H_('kısa yol çok kısa ya da biçimi yanlış')
        if q.get('zorluk') not in ZOR: H_('zorluk')
        if q.get('kalip') not in KALIP: H_(f"kalıp '{q.get('kalip')}'")
        if q.get('k') not in UYG: H_(f"uygulama konusu '{q.get('k')}'")
        t=TIP.get(q.get('tipId'))
        if not t: H_('tipId yok')
        else:
            if t['ad']!=q.get('tip'): H_('tip adı uyuşmuyor')
            if t.get('uygulamaKonu') and t['uygulamaKonu']!=q.get('k'): H_('k, tipin uygulama konusu değil')
        m=re.match(r'(K-[A-Z]+-\d+)',q.get('kaynakKart',''))
        if not m or m.group(1) not in KART: H_('kaynak kart bulunamadı')
        elif t and KART[m.group(1)].get('tipId')!=q.get('tipId'): H_('kartın tipi ile sorunun tipi farklı')
        s=q.get('siklar',{})
        if list(s)!=list('ABCDE'): H_('şıklar A–E değil')
        if len(set(s.values()))!=5: H_('aynı değerli şık')
        c=q.get('cevap',{})
        if c.get('sik') not in s or s.get(c.get('sik'))!=c.get('deger'): H_('cevap şıkla uyuşmuyor')
        nums=[sayi(v) for v in s.values()]
        if all(n is not None for n in nums):
            if nums!=sorted(nums) and nums!=sorted(nums,reverse=True): H_('sayısal şıklar sıralı değil')
            kes=[('/' in v) for v in s.values()]
            if any(kes) and not all(kes) and not all(('/' in v) or v.lstrip('−-').isdigit() for v in s.values()): U('şık biçimleri karışık')
        cd=q.get('celdiriciler',{})
        if set(cd)!=set('ABCDE')-{c.get('sik')}: H_('çeldirici açıklamaları doğru şık hariç 4 şık olmalı')
        if any(len(v)<12 for v in cd.values()): H_('çok kısa çeldirici açıklaması')
        ip=q.get('ipuclari',[])
        if len(ip)!=3: H_('ipucu sayısı 3 değil')
        dv=str(c.get('deger',''))
        if dv and len(dv)<=8 and any(re.search(rf'(?<![\d,/]){re.escape(dv)}(?![\d,/])',x) for x in ip) and not dv.isalpha(): U(f'ipucu cevabı ({dv}) içeriyor olabilir')
        a=q.get('adimlar',[])
        if not 3<=len(a)<=7: H_('anlatım adımı 3–7 değil')
        if not isinstance(q.get('adimSayisi'),int) or not 1<=q['adimSayisi']<=7: H_('adimSayisi (ÖSYM ölçüsü) 1–7 olmalı')
        for x in a:
            if not {'baslik','aciklama','islem'}<=set(x) or set(x)-{'baslik','aciklama','islem','gorsel'}: H_('adım alanları')
            if x.get('gorsel') and ('currentColor' not in x['gorsel'] or 'viewBox' not in x['gorsel']): H_('adım görseli currentColor/viewBox kullanmıyor')
            if len(x.get('baslik','').split())>6: U(f"uzun adım başlığı: {x.get('baslik')}")
            if len(re.findall(r'(?<!\d)[.!?](\s+[A-ZÇĞİÖŞÜ0-9*]|\s*$)',x.get('aciklama','')))>3: U('adım açıklaması 3 cümleden uzun')
        if len(q.get('bilgi',[]))>3: H_('bilgi en fazla 3')
        # sıfırdan anlatım: soruda geçen temel kavram "Bilmen gereken"de açıklanmalı
        bt=json.dumps(q.get('bilgi',[]),ensure_ascii=False).lower(); mt=q.get('metin','')
        if re.search(r'basamaklı (sayı|doğal sayı)?[^.]{0,40}\b[A-Z]{2,3}\b',mt) and '10 ×' not in bt: H_('sıfırdan anlatım: basamak çözümlemesi (AB = 10 × A + B) bilgi kutusunda yok')
        if re.search(r'[\dn)]\s?!|faktöriyel',mt) and 'faktöriyel' not in bt: H_('sıfırdan anlatım: faktöriyel tanımı bilgi kutusunda yok')
        if re.search(r'\basal\b',mt.lower()) and 'asal' not in bt: H_('sıfırdan anlatım: asal sayı tanımı bilgi kutusunda yok')
        if re.search(r'\b(tek|çift) sayı',mt.lower()) and 'tek' not in bt: H_('sıfırdan anlatım: tek-çift kuralları bilgi kutusunda yok')
        mt=q.get('metin','')
        if not mt.rstrip().endswith('?'): H_('soru kökü soru işaretiyle bitmiyor')
        if re.search(r'koç(un|una|uma|u)\b',mt+q.get('puf','')+json.dumps(a,ensure_ascii=False)): H_('ürün ilkesi: koça yönlendirme')
        if '$' in mt or '\\frac' in mt: H_('LaTeX')
        if q.get('sekil') and 'currentColor' not in q['sekil']: H_('şekil currentColor kullanmıyor')
        d=q.get('dogrulama',{})
        if not d.get('yontem2'): H_('ikinci yöntem doğrulaması yok')
        if korpus:
            S=sh(mt)
            if S:
                en=max(((len(S&K)/len(S|K)),ad) for ad,K in korpus)
                if en[0]>=0.25: H_(f'kaynak metne çok benziyor ({en[1]}, Jaccard {en[0]:.2f})')
                elif en[0]>=0.15: U(f'kaynak metne benzerlik ({en[1]}, {en[0]:.2f})')
    # ana–kardeş tutarlılığı
    ID={q['id']:q for q in Q}
    for q in Q:
        if q.get('kardes') and q['kardes'] in ID:
            k=ID[q['kardes']]
            if k.get('ana')!=q['id']: hata.append(f"{q['id']}: kardeşin ana bağlantısı tutmuyor")
            if k['tipId']!=q['tipId'] or k['zorluk']!=q['zorluk']: hata.append(f"{q['id']}: kardeşin tipi/zorluğu farklı")
            if k['metin']==q['metin'] or k['siklar']==q['siklar']: hata.append(f"{q['id']}: kardeş ana soruyla aynı")
    # tekrar: havuz içi benzerlik (ana–kardeş çiftleri hariç)
    for x in range(len(Q)):
        for y in range(x+1,len(Q)):
            if Q[x]['id'].rstrip('k')==Q[y]['id'].rstrip('k'): continue
            A,B=sh(Q[x]['metin']),sh(Q[y]['metin'])
            if A and B and len(A&B)/len(A|B)>=0.3: hata.append(f"{Q[x]['id']} ~ {Q[y]['id']}: havuz içinde benzer soru")
    return hata,uyari
def tablo(Q):
    tz=defaultdict(Counter)
    for q in Q: tz[q['tip']][q['zorluk']]+=1
    satir=[f"{'Soru tipi':40} kolay orta zor"]
    for t in sorted(tz): satir.append(f"{t:40} {tz[t]['kolay']:5} {tz[t]['orta']:4} {tz[t]['zor']:3}")
    return '\n'.join(satir)
if __name__=='__main__':
    dosyalar=[a for a in sys.argv[1:] if a.endswith('.json') and 'tyt-mat' in a]
    korpus=None
    if '--benzerlik' in sys.argv:
        korpus=[]
        for f in sys.argv[sys.argv.index('--benzerlik')+1:]:
            d=json.load(open(f))
            for n,x in enumerate(d):
                m=x if isinstance(x,str) else x['metin']; ad=f"ÖSYM#{n}" if isinstance(x,str) else f"{x['kitap']} s{x['sayfa']} #{x['no']}"
                korpus.append((ad,sh(m)))
    Q=[q for f in dosyalar for q in json.load(open(f))]
    h,u=denetle(Q,korpus)
    print(f'{len(Q)} soru · {len(h)} hata · {len(u)} uyarı')
    for x in h: print('HATA ',x)
    for x in u: print('uyarı',x)
    print('Cevap harfleri:',dict(sorted(Counter(q['cevap']['sik'] for q in Q).items())),'· Zorluk:',dict(Counter(q['zorluk'] for q in Q)))
    print(tablo(Q))
    sys.exit(1 if h else 0)
