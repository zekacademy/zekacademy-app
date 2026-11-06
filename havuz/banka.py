"""Havuz → uygulama Soru Bankası (public/app.js BANKA) biçimi.
Kullanım: python3 havuz/banka.py havuz/tyt-mat/*.json > banka.js
Alanlar: {id, k, z, q, s, d, ad:[[başlık, açıklama, işlem]], puf} + ek: tip, tipId, cel (çeldirici açıklamaları), ip (ipuçları), ist (ne isteniyor)."""
import json,sys
out=[]
for f in sys.argv[1:]:
    for q in json.load(open(f)):
        out.append(dict(id=q['id'],k=q['k'],z=q['zorluk'],q=q['metin'],s=q['siklar'],d=q['cevap']['sik'],
            ad=[[a['baslik'],a['aciklama'],a['islem']]+([a['gorsel']] if a.get('gorsel') else []) for a in q['adimlar']],puf=q['puf'],
            tip=q['tip'],tipId=q['tipId'],cel=q['celdiriciler'],ip=q['ipuclari'],ist=q['istenen'],sekil=q['sekil'],bilgi=q['bilgi']))
print('const BANKA = '+json.dumps(out,ensure_ascii=False,indent=0)+';')
