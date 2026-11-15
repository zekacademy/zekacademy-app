# ÖSYM ders profili ölçümü (15 Kasım 2026). Kullanım: python3 havuz/osym_profil_olcum.py  (girdi: /home/claude/kutup/dersler/osym_*.txt). Görsel ölçümü metin ipuçlarına dayanır, alt sınırdır.
import re,json,statistics as st,collections
D='/home/claude/kutup/dersler/'
SEK=re.compile(r'şekil|grafi[kğ]|tablo|harita|görsel|düzenek|diyagram|çizelge|soy ?ağac|kesit|fotoğraf|resim|gösterilen|numaralandırıl|işaretlen|harflerle|okla|aşağıda verilen .{0,30}(alan|nokta|yer|bölge|merkez)|verilen (alanlar|noktalar|merkezler)',re.I)
NEG=re.compile(r'değildir|olamaz|ulaşılamaz|söylenemez|yoktur|yanlıştır|değinilmemiştir|bulunmaz|çıkarılamaz|gösterilemez|gerekmez|değinilmemiş|beklenemez|kullanılmamıştır|başvurulmamıştır',re.I)
def sinir(sayfa):
    pos=[m.start(1) for l in sayfa.split('\n') for m in [re.search(r'\s(\d{1,2})\.\s{2,}\S',l.replace('\t','    '))] if m and m.start(1)>55]
    return (min(pos)-1) if pos else 98
def sorular(f):
    t=open(D+f).read(); out=[]
    for sayfa in t.split('=== PDF sayfa')[1:]:
        b=sinir(sayfa)
        for side in (0,1):
            col='\n'.join((l.replace('\t','    ')[:b] if side==0 else l.replace('\t','    ')[b:]) for l in sayfa.split('\n'))
            ch=re.split(r'20[12]\d-TYT',col)
            for c in ch[:-1]:
                if 'A)' in c and 'E)' in c: out.append(c)
    return out
def ozellik(b):
    kok=b.split('A)')[0]
    secs=[re.sub(r'\s+',' ',s).strip() for s in re.split(r'[A-E]\)',b)[1:6]]
    bos=sum(1 for s in secs if len(re.sub(r'[^\wçğıöşüÇĞİÖŞÜ]','',s))<1)
    onc=bool(re.search(r'(?m)^\s*I\.\s',kok) and re.search(r'(?m)^\s*II\.\s',kok)) or bool(re.search(r'Yalnız I\b',b))
    return dict(sekil=bool(SEK.search(kok)) or bos>=3, gorsel_sik=bos>=3, onc=onc, neg=bool(NEG.search(kok)),
                kesin=bool(re.search(r'kesinlikle',kok,re.I)), kokkel=len(kok.split()))
def profil(f):
    Q=[ozellik(b) for b in sorular(f)]; n=len(Q)
    return dict(n=n, yil=len(re.findall(r'20[12]\d-TYT',open(D+f).read())), sekil=round(sum(q['sekil'] for q in Q)/n,2),
      gorsel_sik=round(sum(q['gorsel_sik'] for q in Q)/n,2), oncullu=round(sum(q['onc'] for q in Q)/n,2),
      olumsuz=round(sum(q['neg'] for q in Q)/n,2), kesinlikle=round(sum(q['kesin'] for q in Q)/n,2), kok_med=st.median(q['kokkel'] for q in Q))
if __name__=='__main__':
    for d in ['turkce','fizik','kimya','biyoloji','tarih','cografya','felsefe']: print(d,profil(f'osym_{d}.txt'))
