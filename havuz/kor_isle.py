"""Kör çözüm sonucunu anahtarla karşılaştırır; tutanları korCozum=True yapar.
Kullanım: python3 havuz/kor_isle.py <cevaplar.txt> <json…>   (cevaplar: 'id | şık' satırları)"""
import json,sys,re
cev={}
for l in open(sys.argv[1]):
    m=re.match(r'\s*(\S+)\s*\|\s*([A-E])',l)
    if m: cev[m.group(1)]=m.group(2)
tut=0; fark=[]
for f in sys.argv[2:]:
    Q=json.load(open(f))
    for q in Q:
        if q['id'] in cev:
            if cev[q['id']]==q['cevap']['sik']: q['dogrulama']['korCozum']=True; tut+=1
            else: fark.append((q['id'],q['cevap']['sik'],cev[q['id']]))
    json.dump(Q,open(f,'w'),ensure_ascii=False,indent=1)
print('tutan',tut,'· farklı',len(fark)); [print('  FARK',*x) for x in fark]
