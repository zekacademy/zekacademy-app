"""Soru üretim betikleri için ortak yardımcılar.
Kullanım (örnek):
    import sys,os; sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
    from ortak import *
    P=Parti('uslu','Üslü Sayılar','mat|Üslü Sayılar')
    P.R('0001', tipId=..., ...)   # ana soru
    P.K('0001', metin=..., ...)   # kardeşi
    P.yaz('havuz/tyt-mat/uslu-1.json','havuz/tyt-mat/uslu-1-kardes.json')
"""
import json,os
from fractions import Fraction as Fr
from itertools import product,permutations,combinations
from math import factorial,gcd
import gorsel as G

B=lambda ad,ifade:dict(ad=ad,ifade=ifade)
def A(baslik,aciklama,islem,gorsel=None):
    d=dict(baslik=baslik,aciklama=aciklama,islem=islem)
    if gorsel: d['gorsel']=gorsel
    return d
TURLER={'bilgi','islem','dikkat'}

class Parti:
    def __init__(s,onek,konu_adi,k,ders='TYT Matematik',idon='tytmat'):
        """onek: yalnız küçük harf (ör. 'uslu', 'yuzdeprob'); konu_adi: 'Üslü Sayılar'; k: uygulama anahtarı 'mat|Üslü Sayılar'.
        ders/idon: diğer dersler için ör. ders='TYT Fizik', idon='tytfiz'."""
        assert onek.isalpha() and onek.islower() and idon.isalpha(), 'önek yalnız küçük İngilizce harf olmalı'
        s.onek=onek; s.konu_adi=konu_adi; s.k=k; s.ders=ders; s.idon=idon; s.ANA=[]; s.KAR=[]
    def _id(s,no): return f'{s.idon}-{s.onek}-{no}'
    def R(s,no,tipId,tip,zorluk,alt,kazanim,kalip,adim,kart,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,tur,kisa=None,sekil=None):
        """Ana soru. alt: alt konu adı (konu alanı 'Konu · Alt' olur). siklar: 5 değer listesi (A–E sırasıyla). cel/tur: doğru şık hariç 4 şık."""
        S=dict(zip('ABCDE',siklar)); assert sik in S and set(cel)==set(tur)==set('ABCDE')-{sik} and set(tur.values())<=TURLER
        s.ANA.append(dict(id=s._id(no),ders=s.ders,konu=f'{s.konu_adi} · {alt}' if alt else s.konu_adi,k=s.k,kazanim=kazanim,tipId=tipId,tip=tip,zorluk=zorluk,
            seviye='ÖSYM',kalip=kalip,adimSayisi=adim,metin=metin,sekil=sekil,siklar=S,cevap=dict(sik=sik,deger=S[sik]),celdiriciler=cel,celTur=tur,
            istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,kardes=s._id(no)+'k',kaynakKart=kart,
            dogrulama=dict(yontem2=True,tarama=True,korCozum=False)))
    def K(s,no,metin,siklar,sik,istenen,ipuclari,bilgi,adimlar,puf,cel,tur,kisa=None,sekil=None):
        """Kardeş soru: aynı tip ve zorluk, yeni kurgu ve sayılar. Ana sorudan sonra çağrılır."""
        a=[x for x in s.ANA if x['id']==s._id(no)][0]; S=dict(zip('ABCDE',siklar))
        assert sik in S and set(cel)==set(tur)==set('ABCDE')-{sik} and set(tur.values())<=TURLER
        s.KAR.append(dict(id=a['id']+'k',ana=a['id'],ders=a['ders'],konu=a['konu'],k=a['k'],kazanim=a['kazanim'],tipId=a['tipId'],tip=a['tip'],zorluk=a['zorluk'],
            seviye='ÖSYM',kalip=a['kalip'],adimSayisi=a['adimSayisi'],metin=metin,sekil=sekil,siklar=S,cevap=dict(sik=sik,deger=S[sik]),celdiriciler=cel,celTur=tur,
            istenen=istenen,bilgi=bilgi,ipuclari=ipuclari,adimlar=adimlar,puf=puf,kisaYol=kisa,
            kaynakKart=a['kaynakKart'].split(' · ')[0]+f' · kardeş ({no}): aynı tip ve zorluk, yeni kurgu ve sayılar',dogrulama=dict(yontem2=True,tarama=True,korCozum=False)))
    def yaz(s,ana_yol,kardes_yol):
        json.dump(s.ANA,open(ana_yol,'w'),ensure_ascii=False,indent=1)
        json.dump(s.KAR,open(kardes_yol,'w'),ensure_ascii=False,indent=1)
        from collections import Counter
        print(len(s.ANA),'ana',len(s.KAR),'kardeş · harfler',dict(Counter(q['cevap']['sik'] for q in s.ANA+s.KAR)),'· zorluk',dict(Counter(q['zorluk'] for q in s.ANA)))
