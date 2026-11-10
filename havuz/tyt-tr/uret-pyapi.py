"""TYT Türkçe · Paragrafın Yapısı (pyapi): 56 soru, hafif mod. PARCA=1 ortamında yalnız 1. parça (taslak çıktı)."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _hafif_pyapi import *
import _pyapi_p1
if os.environ.get('PARCA')=='1':
    bitir_(os.path.join(H,'pyapi-parca1.json'),28)
else:
    import _pyapi_p2
    bitir_(os.path.join(H,'pyapi-1.json'),56)
for no,(t,z,h) in sorted(Q.say.items()): pass
print('sıralama sıra sayıları:',Q.sira_kayit)
