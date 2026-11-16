"""karsilastir.py <paket> <asama> onek...
asama=ilk : kör çözüm (/tmp/kor/<paket>-cevap.txt) ile anahtarı karşılaştırır.
asama=son : düzeltmeden sonra; metni ve doğru değeri aynı kalanları <paket>-son.txt'ye yazar, değişenleri <paket>-mini.txt'ye. Şekli değişip metni aynı kalanlar için ZORLA=ebobsek-0005,... ortam değişkeni.
asama=bitir: <paket>-mini-cevap.txt'yi ekler, kor_isle çalıştırır, denetler."""
import json,re,sys,subprocess,os
P,A=sys.argv[1],sys.argv[2]; O=sys.argv[3:]; H='/home/claude/zekacademy-app/havuz'
def oku(f):
    c={}
    for l in open(f):
        m=re.match(r'\s*(\S+)\s*\|\s*([A-E])\b',l)
        if m: c[m.group(1)]=(m.group(2),'EMİN' in l)
    return c
cev=oku(f'/tmp/kor/{P}-cevap.txt')
D=os.environ.get('DERS','tyt-mat'); BZ=os.environ.get('BENZER','/home/claude/kutup/osym_metin.json /home/claude/kutup/sorular.json').split()
Q={o:json.load(open(f'{H}/{D}/{o}-1.json')) for o in O}
if A=='ilk':
    n=0
    for o in O:
        for q in Q[o]:
            c=cev.get(q['id'])
            if not c or c[0]!=q['cevap']['sik'] or c[1]: print('!!',q['id'],q['cevap']['sik'],c)
            else: n+=1
    print('tutan',n,'/',sum(len(v) for v in Q.values()))
elif A=='son':
    old={}
    for o in O:
        for b in open(f'/tmp/kor/{o}-once.txt').read().split('### ')[1:]:
            L=b.strip().split('\n'); old[L[0].strip()]=({x[0]:x[3:] for x in L if re.match(r'[A-E]\) ',x)},'\n'.join(x for x in L[1:] if not re.match(r'[A-E]\) |\[ŞEKİL',x)).strip())
    out=open(f'/tmp/kor/{P}-son.txt','w'); mini=open(f'/tmp/kor/{P}-mini.txt','w'); n=0
    for o in O:
        for q in Q[o]:
            i=q['id']; c=cev.get(i)
            if not any(i.endswith(z) for z in os.environ.get('ZORLA','').split(',') if z) and c and not c[1] and i in old and old[i][1]==q['metin'].strip() and old[i][0].get(c[0])==q['cevap']['deger']: out.write(f"{i} | {q['cevap']['sik']}\n")
            else: n+=1; mini.write(f"### {i}\n{q['metin']}\n"+('[ŞEKİL: /tmp/kor/'+i+'.png]\n' if q.get('sekil') else '')+''.join(f"{k}) {v}\n" for k,v in q['siklar'].items())+'\n')
    print('mini kör çözüme giden',n)
elif A=='bitir':
    m=oku(f'/tmp/kor/{P}-mini-cevap.txt') if os.path.exists(f'/tmp/kor/{P}-mini-cevap.txt') else {}
    with open(f'/tmp/kor/{P}-son.txt','a') as f:
        for i,(s,e) in m.items():
            if e: print('EMİN DEĞİLİM',i)
            else: f.write(f'{i} | {s}\n')
    fs=[f'{H}/{D}/{o}-1.json' for o in O]
    print(subprocess.run(['python3',f'{H}/kor_isle.py',f'/tmp/kor/{P}-son.txt']+fs,capture_output=True,text=True).stdout)
    r=subprocess.run(['python3',f'{H}/denetle.py']+fs+['--benzerlik']+BZ,capture_output=True,text=True).stdout.split('\n')
    print('\n'.join(r[:3])); print([l for l in r if 'HATA' in l][:5])
    for o in O: print(o,'bayraksız',[q['id'][-4:] for q in json.load(open(f'{H}/{D}/{o}-1.json')) if not q['dogrulama']['korCozum']])
