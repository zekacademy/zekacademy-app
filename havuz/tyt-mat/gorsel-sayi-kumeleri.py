"""Sayı Kümeleri çözüm adımı görselleri. Kullanım: python3 gorsel-sayi-kumeleri.py <parti.json> ..."""
import json,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
import gorsel as G
from fractions import Fraction as Fr
V={ # id: {adım_indeksi: svg}
'0003':{0:G.dizi_aralik(7,'7 direk ⇒ 6 aralık, her biri 0,6 m',vurgu=4),5:G.iki_sira('3.6',7,4,10,6,'direkler','lambalar')},
'0004':{3:G.gosterge_say(40,60,4,8)},
'0009':{3:G.sayi_dogrusu(120,[(48,'2/5'),(50,'5/12'),(120*3/7,'3/7')],(49,'49/120'))},
'0010':{2:G.tepsi(6,2,3,4)},
'0012':{3:G.zaman_seridi([(40,'yeşil','#16A34A'),(5,'','#E0A100'),(30,'kırmızı','#D93636')],65,'65. sn')},
'0014':{3:G.kutular([(1,6,8),(2,4,9),(3,5,7)],9)},
'0023':{3:G.otopark(9,4,3,7,9)},
}
# veri kontrolleri (görseldeki sayılar soruyla tutarlı)
assert Fr('3.6')/6*3==Fr('1.8') and Fr('3.6')/9*5==2
assert 40+8*4==72 and 4*Fr(1,18)==Fr(2,9) and 1040%75==65
assert sorted(map(sum,[(1,6,8),(2,4,9),(3,5,7)]))==[15,15,15] and 9*4==36 and 3*4==12 and 7+9==16
for f in sys.argv[1:]:
    Q=json.load(open(f))
    for q in Q:
        for a in q['adimlar']: a.pop('gorsel',None)
        for i,svg in V.get(q['id'][-4:],{}).items(): q['adimlar'][i]['gorsel']=svg
    json.dump(Q,open(f,'w'),ensure_ascii=False,indent=1)
print('ok')
