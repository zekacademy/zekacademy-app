"""TYT Kimya · Periyodik Sistem · ek paket (periyodikiki): 22 soru, kardeş yok, ipucu 1. Şekil verileri (kesit, grafik, tablo) Python'da atom numaralarından hesaplanır."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import _hafif_kim2 as H
from _hafif_kim2 import *
KONU_='Periyodik Sistem'; UK='kim|Periyodik Sistem'
H.KONU=KONU_
P=Parti('periyodikiki',KONU_,UK,ders='TYT Kimya',idon='tytkim')
KY='ÖSYM 2018–2025 TYT Kimya (yalnız mantık) · MEB 9. sınıf Periyodik Sistem'
SEMB=['','H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca']
def kab(Z):
    k=[];r=Z
    for c in (2,8,8,2):
        t=min(r,c)
        if t>0: k.append(t); r-=t
    assert r==0; return k
def yer(Z):
    k=kab(Z); return len(k),k[-1]
def kol(Z):
    """18 sütunlu tabloda sütun numarası (A grubu → 1,2,13..18)."""
    p,g=yer(Z)
    if Z==2: return 18
    if Z==1: return 1
    return g if g<=2 else g+10
def ad_(s): return ('Yalnız '+s[0]) if len(s)==1 else (' ve '.join(s) if len(s)==2 else ', '.join(s[:-1])+' ve '+s[-1])
def onc(durum,secenekler):
    T=frozenset(k for k,v in durum.items() if v[0])
    ops=[tuple(s) for s in secenekler]; assert len(ops)==5 and len(set(ops))==5
    es=[o for o in ops if frozenset(o)==T]; assert len(es)==1,(T,ops)
    sira=[ad_(o) for o in ops]; yan=[]
    for o in ops:
        if frozenset(o)==T: continue
        W=frozenset(o); p=[]
        for x in sorted(W-T): p.append(f'{x} öncülünü doğru sanmış; oysa {durum[x][1]}')
        for x in sorted(T-W): p.append(f'{x} öncülünü yanlış sanmış; oysa doğrudur: {durum[x][1]}')
        yan.append((ad_(o),'. '.join(p)+'.','bilgi'))
    return dict(dogru=ad_(es[0]),yan=yan,sira=sira)
def tek(secenekler,hedef=True,tur='bilgi'):
    assert len(secenekler)==5
    h=[s for s in secenekler if s[1]==hedef]; assert len(h)==1,[s[0] for s in h]
    yan=[]
    for m,b,n in secenekler:
        if b==hedef: continue
        yan.append((m,(f'Bu ifadeyi doğru sanmış; oysa {n}' if hedef else f'Bu ifadeyi yanlış sanmış; oysa doğrudur: {n}'),tur))
    return dict(dogru=h[0][0],yan=yan,sira=[s[0] for s in secenekler])
def etk(d): return ' · '.join(f'{k}: '+('doğru' if v[0] else 'yanlış') for k,v in d.items())
TM={'bohr':'yer','toplam':'yer','tablo-dizilim':'yer','iyon-kesit':'yer','kesit-z':'yer','kesit-iyon':'yer',
    'gelisim':'gelisim',
    'sinif-ng':'sinif','kesit-grup':'sinif','grup-ozellik':'sinif','tablo-sinif':'sinif','sinif-yarimetal':'sinif','h-soygaz':'sinif',
    'kesit-yaricap':'egilim','ie-en':'egilim','metalik':'egilim','periyotta':'egilim','kesit-yargi':'egilim','en-sira':'egilim','grafik-yaricap':'egilim',
    'grafik-ie1':'iyonlasma','ardisik-ie':'iyonlasma','tablo-ie':'iyonlasma','tablo-yargi':'iyonlasma'}
TADLAR={'yer':'Konumdan periyot, grup ve atom numarası','gelisim':'Periyodik sistemin gelişimi','sinif':'Grup adları, özellikler ve element sınıfları','egilim':'Periyodik özelliklerin değişimi ve sıralama','iyonlasma':'İyonlaşma enerjisi grafik ve tablo yorumu'}
def kartla(n,alt,fikir,tuzak,z,kalip,adim,tipad,tip):
    t=TM[tipad]; kart(f'K-KMPS2-{n}',alt,fikir,tuzak,z,kalip,adim,f'km-ps2-{t}',TADLAR[t],KY)
def q(no,ad,**k):
    assert len(k['ip'])==1
    t=TM[k['tipId'].replace('km-ps2-','')]; k['tipId']=f'km-ps2-{t}'; k['tip']=TADLAR[t]
    mk(P,no,ad=ad,adim=len(ad),alt=k.pop('alt','Periyodik Sistem'),**k)
HEAD='\\begin{tikzpicture}[line cap=round,line join=round,font=\\small]\n'
TAIL='\n\\end{tikzpicture}'
def tk(g): return tikz_svg(HEAD+g+TAIL)
def bohr(Z,ad='X'):
    k=kab(Z); s=f'\\node[circle,draw,thick,inner sep=2pt,fill=vurgu!15] at (0,0) {{\\textbf{{{ad}}}}};'
    for i,n in enumerate(k):
        r=.75+.5*i; s+=f'\\draw[thin] (0,0) circle ({r});'
        for j in range(n): s+=f'\\fill ({90+360*j/n}:{r}) circle (.07);'
    return tk(s)
def kesit(harf,rows=3,gizle_bos=False):
    """harf: {atom numarası: 'X'}; tablonun ilk 'rows' periyodu, hücreler 18 sütunlu düzende (A grupları başlıklı)."""
    c=.5; var={}
    for Z,h in harf.items():
        p,_=yer(Z); var[(p,kol(Z))]=h
    cells=lambda p:[1,18] if p==1 else ([1,2]+list(range(13,19)) if p<=3 else list(range(1,19)))
    s=''
    for p in range(1,rows+1):
        y=-(p-1)*c
        s+=f'\\node[font=\\footnotesize] at (-.3,{y-c/2}) {{{p}}};'
        for g in cells(p):
            x=(g-1)*c; h=var.get((p,g))
            if h: s+=f'\\draw[thick,fill=vurgu!22] ({x},{y}) rectangle ({x+c},{y-c}); \\node at ({x+c/2},{y-c/2}) {{\\textbf{{{h}}}}};'
            else: s+=f'\\draw[thin] ({x},{y}) rectangle ({x+c},{y-c});'
    for g,t in [(1,'1A'),(2,'2A')]+[(g,f'{g-10}A') for g in range(13,19)]:
        s+=f'\\node[font=\\footnotesize] at ({(g-1)*c+c/2},.26) {{{t}}};'
    s+=f'\\node[font=\\scriptsize,anchor=east] at (-.5,{c/2-.1}) {{Periyot}};' if False else ''
    if rows>=3 and not gizle_bos: s+=f'\\node[font=\\footnotesize,text=gray] at ({7.5*c+.0},{-1.5*c}) {{B grupları}};' if rows==3 else ''
    assert len(var)==len(harf),'iki harf aynı hücrede'
    return tk(s)
# ---- yardımcı: aynı grup / aynı periyot
def ayg(a,b): return yer(a)[1]==yer(b)[1] and (a>2)==(b>2)
def ayp(a,b): return yer(a)[0]==yer(b)[0]
# ================= 01 · Bohr modelinden periyot ve grup · kolay · şekilli =================
kartla('01','Katman diyagramından periyot ve grup','Çizilen katman sayısı periyodu, son katmandaki elektron sayısı A grubunu verir.','Son katmandaki elektron sayısını ilk katmanla ya da toplam elektronla karıştırmak.','kolay','şekilli',3,'bohr','Katman diyagramından periyot ve grup')
Zx=16; assert kab(Zx)==[2,8,6] and yer(Zx)==(3,6)
SK=bohr(Zx,'X')
S=[('2. periyot 6A',False,'şekilde üç katman çizilmiştir; periyot katman sayısına eşittir'),
   ('3. periyot 6A',True,''),
   ('3. periyot 8A',False,'son katmanda 8 değil 6 elektron vardır; 8, ikinci katmanın kapasitesidir'),
   ('4. periyot 6A',False,'şekilde dördüncü bir katman yoktur'),
   ('3. periyot 2A',False,'ilk katmandaki 2 elektron son katman sanılmış; oysa son katman en dıştaki katmandır')]
r=tek(S,True)
q('0001',tipId='km-ps2-bohr',tip='Katman diyagramından periyot ve grup',z='kolay',kaz='Bohr modeli ile gösterilen atomun periyot ve grubunu bulur.',kalip='şekilli',
 kart='K-KMPS2-01 (katman diyagramı) · 2, 8, 6',sekil=SK,
 metin='Bir kimya öğretmeni, nötr hâldeki X atomunun elektronlarının katmanlara dağılımını şekildeki gibi Bohr modeliyle çizmiş ve öğrencilerden bu atomun periyodik sistemdeki yerini bulmalarını istemiştir. Çizimde çekirdeğin çevresindeki her daire bir elektron katmanını, noktalar ise o katmandaki elektronları göstermektedir.\nBuna göre X elementi periyodik sistemde hangi periyot ve grupta yer alır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='X elementinin periyodu ve grubu.',ip=['Dairelerin sayısını ve en dıştaki dairedeki noktaların sayısını ayrı ayrı say.'],
 bilgi=[B('Periyot ve grup','Katman sayısı periyot numarasını, son katmandaki elektron sayısı A grubu numarasını verir. Örnek: 2, 8, 1 dizilimli atom 3. periyot 1A grubundadır')],
 ad=[A('Katmanları say','Şekilde çekirdeğin çevresinde üç daire vardır.','3 katman → 3. periyot'),A('Son katman','En dış daireye çizilen noktalar sayılır.','6 elektron → 6A'),A('Sonuç','Periyot ve grup birleştirilir.','3. periyot 6A')],
 puf='Daire sayısı periyodu, en dış dairedeki nokta sayısı grubu verir.')
# ================= 02 · metal–ametal–soy gaz yargıları · orta · öncüllü =================
kartla('02','Atom numarasından metal, ametal ve soy gaz','Elektron dizilimlerinden periyot ve grup bulunur; 1A ve 2A grubu metaldir, 6A–7A ametaldir, 8A soy gazdır.','Aynı sayıda katmanı olmayan elementleri aynı periyotta saymak.','orta','öncüllü',3,'sinif-ng','Atom numarasından metal, ametal ve soy gaz')
assert yer(12)==(3,2) and yer(8)==(2,6) and yer(17)==(3,7) and yer(18)==(3,8) and not ayp(8,17)
d={'I':(True,'X (Li) ve T (Mg) 1A ve 2A gruplarında yer alan metallerdir'),
   'II':(False,'Y 2. periyotta, Z 3. periyottadır; ikisi de ametal olsa da aynı periyotta değildir'),
   'III':(True,'R’nin dizilimi 2, 8, 8’dir; 8A grubundaki soy gazdır')}
r=onc(d,[('I',),('II',),('I','II'),('I','III'),('I','II','III')])
q('0002',tipId='km-ps2-sinif-ng',tip='Atom numarasından metal, ametal ve soy gaz',z='orta',kaz='Atom numaralarından elementlerin periyot, grup ve metal–ametal–soy gaz sınıfını yorumlar.',kalip='öncüllü',
 kart='K-KMPS2-02 (atom numarasından sınıf) · 3, 8, 12, 17, 18',
 metin='Bir öğrenci, atom numaraları sırasıyla 3, 8, 12, 17 ve 18 olan X, Y, T, Z ve R elementlerinin elektron dizilimlerini yazarak periyodik sistemdeki yerlerini belirliyor. Daha sonra bu elementleri metal, ametal ve soy gaz olarak sınıflandırıyor ve aşağıdaki yargıları yazıyor.\nI. X ve T metaldir.\nII. Y ve Z ametaldir ve aynı periyotta bulunur.\nIII. R, soy gazdır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her elementin elektron dizilimini yaz; katman sayısı periyodu, son katmandaki elektron sayısı grubu gösterir.'],
 bilgi=[B('Metal, ametal ve soy gaz','1A ve 2A grupları (hidrojen hariç) metaldir; 6A ve 7A grupları ametaldir; 8A grubu soy gazlardır. Örnek: 2, 8, 2 dizilimli element 3. periyot 2A’dadır ve metaldir')],
 ad=[A('Dizilimleri yaz','Atom numaralarından dizilimler bulunur.','X: 2, 1 · Y: 2, 6 · T: 2, 8, 2 · Z: 2, 8, 7 · R: 2, 8, 8'),A('Konumlar','Dizilimlerden periyot ve grup okunur.','X: 2. per. 1A · Y: 2. per. 6A · T: 3. per. 2A · Z: 3. per. 7A · R: 3. per. 8A'),A('Yargıları incele','Her yargı konumla karşılaştırılır.',etk(d)),A('Sonuç','Doğrular toplanır.',r['dogru'])],
 puf='Dizilimi yaz: katman sayısı periyodu, son katman elektron sayısı grubu verir.')
# ================= 03 · gelişim · kolay · olumsuz =================
kartla('03','Periyodik sistemin gelişimi (nitel)','Mendeleyev elementleri atom kütlesine göre dizip boşluk bıraktı; Moseley atom numarasını belirleyerek sıralamayı atom numarasına dayandırdı.','Modern tablonun atom kütlesine göre dizildiğini sanmak.','kolay','düz',2,'gelisim','Periyodik sistemin gelişimi')
S=[('Mendeleyev, elementleri artan atom kütlelerine göre sıralamıştır.',True,'Mendeleyev’in dizim ölçütü atom kütlesiydi'),
   ('Mendeleyev, henüz keşfedilmemiş bazı elementlere tabloda boş yer bırakmıştır.',True,'Mendeleyev boşlukları yeni elementlerin keşfi için ayırdı'),
   ('Moseley, elementlerin atom numaralarını belirleyerek sıralamanın atom numarasına dayanmasını sağlamıştır.',True,'Moseley sıralamayı atom numarasına dayandırdı'),
   ('Modern periyodik sistemde elementler artan atom numaralarına göre dizilmiştir.',True,'modern tablonun ölçütü atom numarasıdır'),
   ('Modern periyodik sistemde elementler artan atom kütlelerine göre dizilmiştir.',False,'modern tablonun ölçütü atom kütlesi değil, atom numarasıdır')]
r=tek(S,False)
q('0003',tipId='km-ps2-gelisim',tip='Periyodik sistemin gelişimi',z='kolay',kaz='Periyodik sistemin gelişiminde Mendeleyev ve Moseley’in katkılarını ayırt eder.',kalip='düz',
 kart='K-KMPS2-03 (gelişim, nitel) · Mendeleyev ve Moseley',
 metin='Bir kimya kulübünde hazırlanan sunumda, elementlerin sınıflandırılmasında 19. yüzyıldan günümüze yaşanan gelişim anlatılıyor. Sunumda Mendeleyev’in tablosunun özellikleri ile Moseley’in çalışmalarının tabloyu nasıl değiştirdiği karşılaştırılıyor ve bugün kullanılan modern periyodik sistemin dizim ölçütü vurgulanıyor.\nBu sunumdaki bilgilerle ilgili aşağıdakilerden hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan ifade.',ip=['Modern tablonun, atom numarası ile atom kütlesinden hangisine göre dizildiğini hatırla.'],
 bilgi=[B('Periyodik sistemin gelişimi','Mendeleyev elementleri atom kütlesine göre dizdi ve keşfedilmemiş elementler için boşluk bıraktı. Moseley atom numarasını belirledi; modern tablo artan atom numarasına göre dizilidir. Örnek: Mendeleyev’in boşluklarından biri sonradan keşfedilen bir elemente ayrılmıştı')],
 ad=[A('Mendeleyev','Dizim ölçütü atom kütlesidir ve boşluklar bırakmıştır.','ifadeler 1 ve 2 doğru'),A('Moseley','Atom numarasını belirleyerek dizimi değiştirmiştir.','ifade 3 doğru'),A('Modern tablo','Ölçüt atom numarasıdır; atom kütlesi değildir.','ifade 4 doğru · ifade 5 yanlış'),A('Sonuç','Yanlış olan ifade bulunur.','E')],
 puf='Mendeleyev: atom kütlesi · Moseley ve modern tablo: atom numarası.')
# ================= 04 · A grubu adları kesit · kolay =================
kartla('04','Kesitte grup adları','1A (H hariç) alkali metaller, 2A toprak alkali metaller, 7A halojenler, 8A soy gazlardır; helyumun son katmanında 2 elektron vardır.','Hidrojeni alkali metal saymak; helyumun 8 değerlik elektronu olduğunu sanmak.','kolay','şekilli',3,'kesit-grup','Kesitte grup adları')
dZ={3:'A',12:'B',17:'C',2:'D',19:'E',1:'G'}
SK=kesit(dZ,4)
S=[('A ve E aynı grupta bulunan alkali metallerdir.',ayg(3,19) and yer(3)[1]==1,'Li ve K 1A grubundadır, ikisi de alkali metaldir'),
   ('B elementi bir halojendir.',False,'B, 2. grupta (2A) yer alan toprak alkali metaldir'),
   ('C elementi, 3. periyotta yer alan bir toprak alkali metaldir.',False,'C, 7A grubundadır; halojendir'),
   ('D elementinin değerlik elektron sayısı 8’dir.',False,'D helyumdur; son katmanında 2 elektron vardır'),
   ('G elementi bir alkali metaldir.',False,'G hidrojendir; 1A’dadır ama ametaldir')]
r=tek(S,True)
q('0004',tipId='km-ps2-kesit-grup',tip='Kesitte grup adları',z='kolay',kaz='Kesitte harflerle verilen elementlerin A grubu adlarını ve özelliklerini belirler.',kalip='şekilli',
 kart='K-KMPS2-04 (grup adları) · Li, Mg, Cl, He, K, H',sekil=SK,
 metin='Şekilde periyodik sistemin ilk dört periyodunu gösteren bir kesitte bazı elementlerin yerleri A, B, C, D, E ve G harfleriyle işaretlenmiştir. Bir öğrenci bu elementlerin hangi gruba ait olduğunu belirleyip grup adlarını ve değerlik elektron sayılarını yazıyor.\nBuna göre öğrencinin yazdıklarından hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Her harfin sütununa bak: 1A, 2A, 7A ve 8A gruplarının adlarını hatırla, hidrojen ile helyumu ayrıca düşün.'],
 bilgi=[B('A grupları','1A (H hariç): alkali metaller · 2A: toprak alkali metaller · 7A: halojenler · 8A: soy gazlar. Helyumun son katmanında 2, diğer soy gazların 8 elektron vardır. Örnek: Ca toprak alkali metal, F halojendir')],
 ad=[A('Konumları oku','Harflerin yeri belirlenir.','A: 2. per. 1A · B: 3. per. 2A · C: 3. per. 7A · D: 1. per. 8A · E: 4. per. 1A · G: 1. per. 1A'),A('Grup adları','Sütunlardan grup adları bulunur.','A, E: alkali · B: toprak alkali · C: halojen · D: soy gaz · G: hidrojen'),A('Şıkları ele','Her ifade konumla karşılaştırılır.','A ve E: aynı grup, alkali → doğru'),A('Sonuç','Tek doğru ifade seçilir.',r['dogru'])],
 puf='H 1A’dadır ama alkali metal değildir; He 8A’dadır ama 2 değerlik elektronu vardır.')
# ================= 05 · A gruplarının özellikleri · orta · öncüllü =================
kartla('05','A gruplarının özellikleri','Alkali metaller +1, toprak alkali metaller +2 yüklü iyon verir; halojenler elektron alarak −1 yüklü iyon oluşturur.','Halojenlerin elektron verdiğini sanmak; toprak alkalilerin değerlik elektronunu 1 saymak.','orta','öncüllü',3,'grup-ozellik','A gruplarının özellikleri')
assert yer(12)==(3,2)
d={'I':(True,'alkali metallerin değerlik elektron sayısı 1’dir, bileşiklerinde +1 yüklü iyon oluştururlar'),
   'II':(True,'atom numarası 12 olan elementin dizilimi 2, 8, 2’dir; 2A grubunda olduğundan iki elektron verip +2 yüklü iyon oluşturur'),
   'III':(False,'halojenlerin son katmanında 7 elektron vardır; elektron alıp −1 yüklü iyon oluştururlar')}
r=onc(d,[('I',),('II',),('I','II'),('I','III'),('II','III')])
q('0005',tipId='km-ps2-grup-ozellik',tip='A gruplarının özellikleri',z='orta',kaz='Alkali metal, toprak alkali metal ve halojenlerin değerlik elektronu ve iyon yükü özelliklerini ayırt eder.',kalip='öncüllü',
 kart='K-KMPS2-05 (A grubu özellikleri) · değerlik elektronu ve iyon yükü',
 metin='Bir öğrenci, laboratuvar defterine A gruplarına ait elementlerin bileşiklerinde oluşturdukları iyonlarla ilgili not alıyor. Notlarını yazarken elementlerin değerlik elektron sayılarından ve elektron verme ya da alma eğilimlerinden yararlanıyor. Notlarındaki yargılar aşağıda verilmiştir.\nI. Alkali metaller, bileşiklerinde +1 yüklü iyon oluşturur.\nII. Atom numarası 12 olan element, bileşiklerinde +2 yüklü iyon oluşturur.\nIII. Halojenler, bileşiklerinde +1 yüklü iyon oluşturur.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Grup numarası A grubu elementlerinin değerlik elektron sayısını verir; metaller elektron verir, ametaller elektron alır.'],
 bilgi=[B('Grup özellikleri','1A: 1 değerlik elektronu, +1 iyon · 2A: 2 değerlik elektronu, +2 iyon · 7A: 7 değerlik elektronu, elektron alarak −1 iyon. Örnek: değerlik elektron sayısı 3 olan bir metal, 3 elektron verirse +3 yüklü iyon oluşturur')],
 ad=[A('I. yargı','Alkali metaller 1A grubundadır, 1 elektron verir.','+1 iyon → I doğru'),A('II. yargı','Atom numarası 12: 2, 8, 2 → 2A.','2 elektron verir → +2 → II doğru'),A('III. yargı','Halojenlerin son katmanında 7 elektron vardır.','elektron alır → −1 → III yanlış'),A('Sonuç','Doğrular toplanır.',etk(d)+' · '+r['dogru'])],
 puf='A grubu numarası = değerlik elektron sayısı; metaller elektron verir, ametaller alır.')
# ================= 06 · tablo: katman dizilimi · kolay =================
kartla('06','Katman dizilimlerinden periyot ve grup','Katman sayısı periyodu, son katman elektron sayısı grubu verir; son katmanları eşit elementler (He hariç) aynı gruptadır.','Aynı sayıda katmanı olanları aynı grupta saymak.','kolay','tablo',3,'tablo-dizilim','Katman dizilimlerinden periyot ve grup')
EL={'X':4,'Y':12,'Z':16,'T':19,'R':8}
rows=[[h,', '.join(map(str,kab(z)))] for h,z in EL.items()]
SK=tablo_svg(['Element','Katman dağılımı'],rows)
def bs(a,b): return ayg(EL[a],EL[b]),ayp(EL[a],EL[b])
assert bs('X','Y')==(True,False) and bs('Y','Z')==(False,True) and bs('Y','T')==(False,False) and bs('Z','R')==(True,False) and bs('X','T')==(False,False)
S=[('X ile T aynı grupta bulunur.',False,'X’in son katmanında 2, T’ninkinde 1 elektron vardır; grupları 2A ve 1A’dır'),
   ('Y ile T aynı periyottadır.',False,'Y’nin 3, T’nin 4 katmanı vardır'),
   ('Z ile R aynı periyottadır.',False,'Z’nin 3, R’nin 2 katmanı vardır'),
   ('X ile Y aynı grupta, Y ile Z aynı periyottadır.',True,''),
   ('T elementi 2. periyot 1A grubundadır.',False,'T’nin dört katmanı vardır; 4. periyottadır')]
r=tek(S,True)
q('0006',tipId='km-ps2-tablo-dizilim',tip='Katman dizilimlerinden periyot ve grup',z='kolay',kaz='Elektron dizilimi tablosundan elementlerin periyot ve gruplarını karşılaştırır.',kalip='tablo',
 kart='K-KMPS2-06 (dizilim tablosu) · X, Y, Z, T, R',sekil=SK,
 metin='Aşağıdaki tabloda, nötr hâldeki X, Y, Z, T ve R atomlarının elektronlarının katmanlara dağılımı verilmiştir. Bir öğrenci bu verilere bakarak elementlerin periyodik sistemdeki yerlerini karşılaştırmak istiyor.\nBuna göre bu elementlerle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Satır başına katman sayısını ve son katmandaki elektron sayısını yaz; ardından karşılaştır.'],
 bilgi=[B('Dizilimden konum','Katman sayısı = periyot; son katmandaki elektron sayısı = A grubu. Örnek: 2, 8, 3 → 3. periyot 3A; 2, 3 → 2. periyot 3A, yani ikisi aynı gruptadır')],
 ad=[A('K ve L','X: 2 katman, 2 e⁻ · Y: 3 katman, 2 e⁻.','ikisi de 2A'),A('Periyotlar','Katman sayıları sayılır.','X: 2 · Y: 3 · Z: 3 · T: 4 · R: 2'),A('Şıkları ele','Her şık grup ve periyotla karşılaştırılır.','X–Y aynı grup · Y–Z aynı periyot'),A('Sonuç','Tek doğru ifade bulunur.',r['dogru'])],
 puf='Aynı grup: son katman elektronu eşit; aynı periyot: katman sayısı eşit.')
# ================= 07 · kesit: atom yarıçapı sıralaması · orta =================
kartla('07','Kesitte atom yarıçapı sıralaması','Grupta aşağı inildikçe katman sayısı artar, yarıçap büyür; periyotta sağa gidildikçe çekirdek çekimi artar, yarıçap küçülür.','Katman sayısına bakmadan yalnız atom numarasına göre sıralamak.','orta','şekilli',4,'kesit-yaricap','Kesitte atom yarıçapı sıralaması')
dZ={13:'X',20:'Y',12:'Z',14:'T'}
assert yer(13)==(3,3) and yer(20)==(4,2) and yer(12)==(3,2) and yer(14)==(3,4)
SK=kesit(dZ,4)
S=[('Y > Z > T > X',False,'3. periyotta soldan sağa gidildikçe yarıçap azalır; X (3A), T’nin (4A) solundadır, X > T olur'),
   ('Y > Z > X > T',True,''),
   ('Z > Y > X > T',False,'Y dört katmanlıdır, Z üç katmanlıdır; Y > Z olur'),
   ('T > X > Z > Y',False,'bu sıra, yarıçapın periyotta soldan sağa arttığı ve grupta aşağı inildikçe azaldığı yanılgısından gelir; ikisi de tersidir'),
   ('Y > X > Z > T',False,'Z, X’in solundadır; aynı periyotta soldaki büyüktür, Z > X olur')]
r=tek(S,True)
q('0007',tipId='km-ps2-kesit-yaricap',tip='Kesitte atom yarıçapı sıralaması',z='orta',kaz='Kesitte yeri verilen elementlerin atom yarıçaplarını grup ve periyottaki yerlerine göre sıralar.',kalip='şekilli',
 kart='K-KMPS2-07 (yarıçap sıralaması) · Al, Ca, Mg, Si',sekil=SK,
 metin='Bir öğrenci, periyodik sistemin ilk dört periyodunu gösteren şekildeki kesitte X, Y, Z ve T elementlerini işaretlemiştir. Öğrenci bu elementlerin atom yarıçaplarını büyükten küçüğe sıralayacak ve bunu aynı grupta ve aynı periyotta yarıçapın nasıl değiştiğine dayandıracaktır.\nBuna göre bu elementlerin atom yarıçapları arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Atom yarıçaplarının büyükten küçüğe sıralaması.',ip=['Önce aynı grupta olanları, sonra aynı periyotta olanları kendi aralarında karşılaştır.'],
 bilgi=[B('Atom yarıçapı','Aynı grupta yukarıdan aşağı yarıçap artar (katman sayısı artar). Aynı periyotta soldan sağa yarıçap azalır (çekirdek yükü artar). Örnek: Na > Li ve Na > Cl')],
 ad=[A('Konumları oku','Harfler periyot ve gruba göre okunur.','X: 3. per. 3A · Y: 4. per. 2A · Z: 3. per. 2A · T: 3. per. 4A'),A('Aynı grup','Y ve Z 2A grubundadır; Y daha aşağıdadır.','Y > Z'),A('Aynı periyot','Z, X, T 3. periyottadır; soldaki büyüktür.','Z > X > T'),A('Birleştir','Y > Z olduğundan zincir tamamlanır.','Y > Z > X > T')],
 puf='Önce grup içi, sonra periyot içi karşılaştır; zinciri bu iki bilgiyle birleştir.')
# ================= 08 · iyonlaşma enerjisi ve elektronegatiflik yargıları · orta · öncüllü =================
kartla('08','İyonlaşma enerjisi ve elektronegatiflik yargıları','Periyotta sağa gidildikçe iyonlaşma enerjisi ve elektronegatiflik artar, grupta aşağı inildikçe azalır.','Eğilimleri ters yorumlamak.','orta','öncüllü',4,'ie-en','İyonlaşma enerjisi ve elektronegatiflik yargıları')
assert yer(3)==(2,1) and yer(7)==(2,5) and yer(15)==(3,5) and yer(10)==(2,8)
d={'I':(False,'X, 2. periyotta 1A’dadır, T ise aynı periyotta 8A’dadır; periyotta sağa gidildikçe iyonlaşma enerjisi artar, bu yüzden T’ninki X’ten büyüktür'),
   'II':(True,'Y ile Z aynı gruptadır (5A); aşağıdaki Z’nin iyonlaşma enerjisi daha küçüktür'),
   'III':(True,'aynı grupta yukarıdaki Y’nin elektronegatifliği Z’ninkinden büyüktür')}
r=onc(d,[('II',),('III',),('I','II'),('I','III'),('II','III')])
q('0008',tipId='km-ps2-ie-en',tip='İyonlaşma enerjisi ve elektronegatiflik yargıları',z='orta',kaz='Atom numarasından konum bulup elementlerin iyonlaşma enerjisi ve elektronegatifliklerini karşılaştırır.',kalip='öncüllü',
 kart='K-KMPS2-08 (iyonlaşma enerjisi ve elektronegatiflik) · atom numaraları 3, 7, 10, 15',
 metin='Atom numaraları sırasıyla 3, 7, 15 ve 10 olan X, Y, Z ve T elementlerinin elektron dizilimlerinden periyodik sistemdeki yerleri bulunuyor. Bir öğrenci, bu elementlerin birinci iyonlaşma enerjileri ile elektronegatiflikleri arasındaki ilişkiyi yorumlayarak aşağıdaki yargıları yazıyor.\nI. X’in birinci iyonlaşma enerjisi, T’ninkinden büyüktür.\nII. Z’nin birinci iyonlaşma enerjisi, Y’ninkinden küçüktür.\nIII. Y’nin elektronegatifliği, Z’ninkinden büyüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Her yargıda karşılaştırılan iki elementin aynı grupta mı aynı periyotta mı olduğuna bak.'],
 bilgi=[B('İyonlaşma enerjisi ve elektronegatiflik','İyonlaşma enerjisi: gaz hâlindeki atomdan bir elektron koparmak için gereken enerji; elektronegatiflik: bağ elektronlarını çekme eğilimi. İkisi de periyotta sağa doğru artar, grupta aşağı doğru azalır. Örnek: Cl > Na ve F > Cl')],
 ad=[A('Konumları bul','Dizilimler yazılır.','X: 2, 1 · Y: 2, 5 · Z: 2, 8, 5 · T: 2, 8'),A('Konumlar','Periyot ve gruplar okunur.','X: 2. per. 1A · Y: 2. per. 5A · Z: 3. per. 5A · T: 2. per. 8A'),A('Yargıları incele','Aynı periyot ve aynı grup karşılaştırmaları yapılır.',etk(d)),A('Sonuç','Doğrular toplanır.',r['dogru'])],
 puf='İyonlaşma enerjisi ve elektronegatiflik: sağa ↑, aşağı ↓.')
# ================= 09 · grafik: ardışık 9 elementin 1. iyonlaşma enerjisi · zor =================
kartla('09','İyonlaşma enerjisi grafiğinden element yorumu','Ardışık atom numaralı elementlerin birinci iyonlaşma enerjisi grafiğinde tepe noktası soy gaza, tepeden hemen sonraki çukur alkali metale karşılık gelir.','Grafikteki yüksekliği atom yarıçapıyla karıştırmak; soy gazı halojen saymak.','zor','grafik',4,'grafik-ie1','Birinci iyonlaşma enerjisi grafiği')
IE1=[520,900,801,1086,1402,1314,1681,2081,496]; LB='ABCDEFGHI'
# aynı desen 3–11 ve 11–19 için geçerli; yargılar her iki durumda aynı sonucu verir
for Z0 in (3,11):
    Zl=dict(zip(LB,range(Z0,Z0+9)))
    assert ayg(Zl['A'],Zl['I']) and yer(Zl['H'])[1]==8 and yer(Zl['G'])[1]==7 and yer(Zl['B'])[1]==2 and ayp(Zl['F'],Zl['G'])
IE2=[738,578,786,1012,1000,1251,1521,419]  # 11–19 desen kontrolü (Mg…K)
coords=' '.join(f'({i+1},{v})' for i,v in enumerate(IE1))
g='\\begin{axis}[width=7.4cm,height=5.4cm,xmin=.3,xmax=9.7,ymin=0,ymax=2500,xtick=\\empty,ytick=\\empty,axis lines=left,xlabel={Atom numarası artar $\\rightarrow$},ylabel={1. iyonlaşma enerjisi},xlabel style={font=\\small},ylabel style={font=\\small}]\n'
g+=f'\\addplot[thick,vurgu,mark=*,mark size=1.6pt] coordinates {{{coords}}};\n'
for i,(l,v) in enumerate(zip(LB,IE1)):
    pos='above' if i in (0,1,3,4,6,7,8) else 'below'
    g+=f'\\node[{pos},font=\\small\\bfseries] at (axis cs:{i+1},{v}) {{{l}}};\n'
g+='\\end{axis}'
SK=tk(g)
S=[('A ve I elementleri aynı grupta yer alır.',True,''),
   ('B elementi bir alkali metaldir.',False,'B, A’dan sonra gelir ve 2A grubundadır; alkali metaller grafikte çukurda yer alan A ve I’dır'),
   ('G elementi bir soy gazdır.',False,'soy gaz, grafikteki en yüksek tepe noktasındaki H’dir; G bir halojendir'),
   ('H elementi 7A grubunda yer alan bir halojendir.',False,'H, grafikteki en yüksek tepe noktasındadır; soy gazdır, 8A grubundadır'),
   ('F’nin atom yarıçapı G’ninkinden küçüktür.',False,'F ile G aynı periyottadır; F soldadır, yarıçapı G’ninkinden büyüktür')]
r=tek(S,True)
q('0009',tipId='km-ps2-grafik-ie1',tip='Birinci iyonlaşma enerjisi grafiği',z='zor',kaz='Ardışık elementlerin birinci iyonlaşma enerjisi grafiğinden elementlerin grup ve özelliklerini yorumlar.',kalip='grafik',
 kart='K-KMPS2-09 (IE1 grafiği) · ardışık dokuz element',sekil=SK,
 metin='Atom numaraları 20’den küçük olan ve ardışık olarak artan dokuz elementin birinci iyonlaşma enerjileri şekildeki grafikte gösterilmiştir. Elementler atom numarası artış sırasıyla A’dan I’ya kadar harflendirilmiş, kimlikleri verilmemiştir. Öğrenci grafikteki tepe ve çukurlardan hangi elementin hangi grupta olduğunu çıkaracaktır.\nBuna göre bu elementlerle ilgili aşağıdakilerden hangisi doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan ifade.',ip=['Grafikteki en yüksek noktanın hangi grup elementine ait olduğunu düşün, sonra komşularının gruplarını sırayla belirle.'],
 bilgi=[B('Grafikte iyonlaşma enerjisi','Bir periyotta iyonlaşma enerjisi soldan sağa genelde artar; soy gazda en yüksektir, hemen sonraki alkali metalde ani düşer. Bir periyotta 8 element bulunduğundan 8 element arayla aynı grup tekrarlanır. Örnek: Ar’dan sonra gelen K grafikte keskin bir çukur oluşturur')],
 ad=[A('Tepeyi bul','En yüksek nokta H’dir.','H: soy gaz (8A)'),A('Komşuları yerleştir','H’den önceki G halojen, sonraki I yeni periyodun ilk elementidir.','G: 7A · F: 6A · I: 1A · B: 2A'),A('A’yı bul','A ile I arasında 8 element vardır; aynı grup tekrar eder.','A: 1A → A ve I aynı grup'),A('İfadeleri ele','Her ifade bulunan konumlarla karşılaştırılır.',r['dogru'])],
 puf='İyonlaşma enerjisi grafiğinde tepe: soy gaz; tepeden sonraki çukur: yeni periyodun alkali metali.')
# ================= 10 · ardışık iyonlaşma enerjisi · orta · grafik =================
kartla('10','Ardışık iyonlaşma enerjilerinden atom numarası','Ardışık iyonlaşma enerjilerinde ani sıçrama değerlik elektronları bittikten sonra olur; sıçramanın yeri grup numarasını verir.','Sıçrama sayısını atom numarası sanmak; katman sayısını eklemeyi unutmak.','orta','grafik',4,'ardisik-ie','Ardışık iyonlaşma enerjilerinden atom numarası')
Xv=[1012,1907,2914,4964,6274,21267]
def grup(v):
    oran=[v[i+1]/v[i] for i in range(len(v)-1)]; return oran.index(max(oran))+1
assert grup(Xv)==5
ZX=sum(kab(15)); assert kab(15)==[2,8,5] and ZX==15 and yer(15)==(3,5)
assert 5==grup(Xv) and 2+8==10 and 16==2+8+6 and 23==2+8+8+5
coords=' '.join(f'({i+1},{v})' for i,v in enumerate(Xv))
g='\\begin{axis}[scaled y ticks=false,ybar,bar width=14pt,width=7.4cm,height=5.4cm,xmin=.4,xmax=6.6,ymin=0,ymax=22000,xtick={1,...,6},ytick={0,5000,10000,15000,20000},yticklabel style={font=\\scriptsize},/pgf/number format/.cd,1000 sep={},xticklabel style={font=\\scriptsize},axis lines=left,xlabel={Koparılan elektron sırası},ylabel={Enerji (kJ/mol)},xlabel style={font=\\small},ylabel style={font=\\small}]\n'
g+=f'\\addplot[fill=vurgu!35,draw=black] coordinates {{{coords}}};\n\\end{{axis}}'
SK=tk(g)
q('0010',tipId='km-ps2-ardisik-ie',tip='Ardışık iyonlaşma enerjilerinden atom numarası',z='orta',kaz='Ardışık iyonlaşma enerjisi grafiğinden değerlik elektron sayısını bulup elementin atom numarasını belirler.',kalip='grafik',
 kart='K-KMPS2-10 (ardışık IE) · 3. periyot 5A',sekil=SK,
 metin='Bir kimyacı, atom numarası 20’den küçük olan ve nötr hâlde üç elektron katmanına sahip X elementinin gaz hâlindeki atomundan elektronları sırayla koparıyor. Her koparma için gereken enerjiyi ölçüp şekildeki grafiği çiziyor.\nBuna göre X elementinin atom numarası kaçtır?',
 dogru=15,yan=[(5,'Sıçramanın beşinci elektrondan sonra olduğunu görmüş ama grup numarasını atom numarası sanmış.','bilgi'),(10,'Yalnız iki iç katmandaki elektronları (2 + 8) saymış, değerlik elektronlarını eklememiş.','islem'),(16,'Sıçramayı 6. çubukta aramış (6A saymış): 2 + 8 + 6 = 16; sıçramadan önceki basamak sayısı grubu verir.','dikkat'),(23,'Dört katmanlı sanıp 2 + 8 + 8 + 5 yazmış; soruda üç katman verilmiştir.','dikkat')],
 istenen='X elementinin atom numarası.',ip=['Çubuk yüksekliğinin ani arttığı basamağı bul; bu basamak değerlik elektron sayısını gösterir.'],
 bilgi=[B('Ardışık iyonlaşma enerjileri','Değerlik elektronları koparılırken enerji yavaş artar; tam dolu iç katmandan elektron koparmaya geçilince enerji ani olarak çok yükselir. Sıçramadan önceki basamak sayısı değerlik elektron sayısıdır. Örnek: sıçrama 2. ile 3. arasındaysa element 2A grubundadır')],
 ad=[A('Sıçramayı bul','Çubuklar 5. basamağa kadar yavaş artar, 6. çubuk çok yüksektir.','5. ile 6. çubuk arasında ani sıçrama'),A('Grubu belirle','Sıçramadan önce beş elektron koparılmıştır.','5A grubu'),A('Dizilimi yaz','Üç katman; son katmanda 5 elektron.','2, 8, 5'),A('Atom numarası','Elektronlar toplanır.','2 + 8 + 5 = 15')],
 puf='Ani sıçramadan önceki basamak sayısı grup numarasıdır; katman sayısı periyodu verir.')
# ================= 11 · tablo: ardışık iyonlaşma enerjisinden grup · orta =================
kartla('11','Tabloda ardışık iyonlaşma enerjisinden grup','Ardışık iyonlaşma enerjileri tablosunda en büyük sıçrama, değerlik elektron sayısını (A grubunu) gösterir.','Sıçramanın bulunduğu sütundan bir fazlasını okumak.','orta','tablo',3,'tablo-ie','Tabloda ardışık iyonlaşma enerjisinden grup')
TV={'X':[496,4562,6912,9543],'Y':[738,1451,7733,10543],'Z':[578,1817,2745,11577]}
gr={k:grup(v) for k,v in TV.items()}; assert gr=={'X':1,'Y':2,'Z':3}
SK=tablo_svg(['Element','İE₁','İE₂','İE₃','İE₄'],[[k]+[f'{x:,}'.replace(',','.') for x in v] for k,v in TV.items()])
q('0011',tipId='km-ps2-tablo-ie',tip='Tabloda ardışık iyonlaşma enerjisinden grup',z='orta',kaz='Ardışık iyonlaşma enerjileri tablosundan elementlerin A grubunu belirler.',kalip='tablo',
 kart='K-KMPS2-11 (ardışık IE tablosu) · X, Y, Z',sekil=SK,
 metin='Aşağıdaki tabloda, atom numaraları 20’den küçük olan X, Y ve Z elementlerinin gaz hâlindeki atomlarından birinci, ikinci, üçüncü ve dördüncü elektronu koparmak için gereken enerjiler (kJ/mol) verilmiştir. Bir öğrenci, her elementin hangi A grubunda yer aldığını bu verilerden bulmaya çalışmaktadır.\nBuna göre X, Y ve Z elementlerinin grupları sırasıyla aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru='1A, 2A, 3A',sira=['1A, 2A, 3A','2A, 3A, 4A','1A, 2A, 4A','3A, 2A, 1A','1A, 3A, 3A'],
 yan=[('2A, 3A, 4A','Sıçramanın bulunduğu basamağı bir fazla okumuş; sıçramadan önceki basamak sayısı grubu verir.','dikkat'),('1A, 2A, 4A','Z için dördüncü basamaktaki büyük değere bakıp 4A demiş; sıçrama 3. ile 4. arasındadır, yani 3A.','dikkat'),('3A, 2A, 1A','Gruplarını ters sıralamış: büyük enerjileri olan elementleri daha büyük gruplarda sanmış.','bilgi'),('1A, 3A, 3A','Y’de 7.733 gibi büyük bir değere rastlayınca bunu üçüncü basamakta saymış ve Y’yi 3A sanmış; oysa Y’de sıçrama 2. ile 3. arasında, yani 2A’dır.','dikkat')],
 istenen='X, Y ve Z’nin A grupları.',ip=['Her satırda bir önceki değere göre en büyük artışın hangi iki sütun arasında olduğuna bak.'],
 bilgi=[B('Ardışık iyonlaşma enerjileri','Değerlik elektronları koparılırken enerji yavaş artar; tam dolu iç katmana geçildiğinde ani ve büyük bir artış olur. Bu artıştan önceki elektron sayısı A grubudur. Örnek: 300, 2400, 3600, 4800 değerlerinde sıçrama 1. ile 2. arasındadır')],
 ad=[A('X’i incele','496 → 4.562 büyük sıçrama.','1. ile 2. arasında → 1A'),A('Y’yi incele','738 → 1.451 → 7.733.','2. ile 3. arasında → 2A'),A('Z’yi incele','578 → 1.817 → 2.745 → 11.577.','3. ile 4. arasında → 3A'),A('Sonuç','Gruplar sırayla yazılır.','1A, 2A, 3A')],
 puf='Büyük sıçrama kaçıncı ile kaçıncı arasındaysa, ilk sayı grup numarasıdır.')
# ================= 12 · metalik karakter · orta · düz =================
kartla('12','Metalik karakter sıralaması','Metalik karakter grupta aşağı inildikçe artar, periyotta sağa gidildikçe azalır.','Metalik karakteri ametalik karakter ya da yarıçapla ters yorumlamak.','orta','düz',3,'metalik','Metalik karakter sıralaması')
Zm={'X':13,'Y':11,'Z':19}; assert yer(13)==(3,3) and yer(11)==(3,1) and yer(19)==(4,1)
S=[('Y > Z > X',False,'Z, Y ile aynı grupta ve altındadır; aşağıdaki daha metaliktir'),('X > Y > Z',False,'3. periyotta sağa gidildikçe metalik karakter azalır; X, Y’nin sağındadır'),('Z > Y > X',True,''),('Z > X > Y',False,'X, Y ile aynı periyottadır ve Y’nin sağındadır; Y > X olur'),('Y > X > Z',False,'Z, Y’nin altındadır ve en metalik olandır')]
r=tek(S,True)
q('0012',tipId='km-ps2-metalik',tip='Metalik karakter sıralaması',z='orta',kaz='Atom numarasından konum bulup elementlerin metalik karakterlerini karşılaştırır.',kalip='düz',
 kart='K-KMPS2-12 (metalik karakter) · atom numaraları 13, 11, 19',
 metin='Atom numaraları sırasıyla 13, 11 ve 19 olan X, Y ve Z elementleri için bir öğrenci, bu üç elementin elektron dizilimlerini yazarak periyodik sistemdeki yerlerini bulmuş ve elektron verme eğilimlerine göre bir sıralama yapmak istemektedir.\nBuna göre bu elementlerin metalik karakterleri arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Metalik karakterin büyükten küçüğe sıralaması.',ip=['Elektron dizilimlerinden konumları bul; elektron vermenin kolaylaştığı yönü düşün.'],
 bilgi=[B('Metalik karakter','Metaller elektron verme eğilimindedir. Grupta aşağı doğru metalik karakter artar; periyotta sağa doğru azalır. Örnek: Mg, Be’den; Na ise Mg’den daha metaliktir')],
 ad=[A('Konumlar','Dizilimler yazılır.','X: 2, 8, 3 (3. per. 3A) · Y: 2, 8, 1 (3. per. 1A) · Z: 2, 8, 8, 1 (4. per. 1A)'),A('Aynı grup','Y ve Z 1A grubundadır; Z daha aşağıdadır.','Z > Y'),A('Aynı periyot','X ve Y 3. periyottadır; Y daha soldadır.','Y > X'),A('Sıralama','İki sonuç birleştirilir.','Z > Y > X')],
 puf='Metalik karakter: aşağı ↑ ve sola ↑.')
# ================= 13 · tablo: metal–ametal–yarı metal–soy gaz · orta =================
kartla('13','Özelliklerden element sınıfı','Elementler metal, ametal, yarı metal ve soy gaz olarak sınıflandırılır; sınıflama görünüm, iletkenlik, işlenebilirlik ve tepkimeye girme eğilimine dayanır.','Parlak her elementi metal saymak.','kolay','tablo',3,'tablo-sinif','Özelliklerden element sınıfı')
SK=tablo_svg(['Element','Görünüm','İletkenlik','Oda koşullarında'],[['A','Parlak','İyi iletken','Katı, dövülebilir'],['B','Mat','İletken değil','Katı, kırılgan'],['C','Parlak','Yarı iletken','Katı, kırılgan'],['D','Renksiz','İletken değil','Gaz, tepkimeye girmez']])
q('0013',tipId='km-ps2-tablo-sinif',tip='Özelliklerden element sınıfı',z='kolay',kaz='Özellikleri verilen elementleri metal, ametal, yarı metal ve soy gaz olarak sınıflandırır.',kalip='tablo',
 kart='K-KMPS2-13 (özelliklerden sınıf) · A, B, C, D',sekil=SK,
 metin='Bir laboratuvarda dört ayrı element örneği incelenmiş ve gözlemler aşağıdaki tabloda toplanmıştır. İletkenlik sütunu ısı ve elektrik iletkenliğini gösterir. Öğrencilerden bu gözlemlere dayanarak her bir elementi metal, ametal, yarı metal ya da soy gaz olarak sınıflandırmaları isteniyor. Elementlerin kimliği öğrencilere söylenmemiştir.\nBuna göre A, B, C ve D elementleri sırasıyla aşağıdakilerden hangisinde doğru sınıflandırılmıştır?',
 dogru='metal, ametal, yarı metal, soy gaz',sira=['ametal, metal, yarı metal, soy gaz','metal, ametal, yarı metal, soy gaz','metal, yarı metal, ametal, soy gaz','yarı metal, ametal, metal, soy gaz','metal, ametal, yarı metal, yarı metal'],
 yan=[('metal, yarı metal, ametal, soy gaz','B ile C’yi karıştırmış; parlak ve yarı iletken olanın yarı metal, mat ve yalıtkan olanın ametal olduğunu görmemiş.','bilgi'),('ametal, metal, yarı metal, soy gaz','A ile B’yi ters yazmış; iyi iletken ve dövülebilen elementin metal olduğunu bilmemiş.','bilgi'),('yarı metal, ametal, metal, soy gaz','A ile C’yi karıştırmış; yalnız parlaklığa bakmış, iletkenlik ve dövülebilirliği hesaba katmamış.','dikkat'),('metal, ametal, yarı metal, yarı metal','D’yi yarı metal saymış; yarı metaller katı ve yarı iletkendir, D ise hiçbir elementle tepkimeye girmeyen bir gazdır, yani soy gazdır.','bilgi')],
 istenen='A, B, C ve D’nin sınıfları.',ip=['Önce iletkenliğe bak: iyi iletken, yarı iletken ve iletken olmayan; sonra oda koşullarındaki hâle ve tepkimeye bak.'],
 bilgi=[B('Element sınıfları','Metaller iyi iletken ve dövülebilir; ametaller yalıtkan ve kırılgandır; yarı metaller bu iki sınıfın arasında yarı iletken özellik gösterir; soy gazlar 8A grubundadır ve tepkimeye girme eğilimleri çok düşüktür')],
 ad=[A('A’yı incele','Parlak, iyi iletken, dövülebilir.','A: metal'),A('B ve C','B mat ve yalıtkan; C parlak ama kırılgan ve yarı iletken.','B: ametal · C: yarı metal'),A('D’yi incele','Gaz, tepkimeye girmiyor.','D: soy gaz'),A('Sonuç','Sınıflar sırayla yazılır.','metal, ametal, yarı metal, soy gaz')],
 puf='İletkenlik sırası: metal iyi, yarı metal orta (yarı iletken), ametal yok.')
# ================= 14 · periyotta değişim · kolay · öncüllü =================
kartla('14','Periyotta soldan sağa değişim','2. periyotta Li’dan Ne’a gidildikçe atom yarıçapı küçülür, iyonlaşma enerjisi genel olarak artar, katman sayısı değişmez.','Periyotta katman sayısının arttığını sanmak.','kolay','öncüllü',3,'periyotta','Periyotta soldan sağa değişim')
d={'I':(True,'çekirdek yükü artarken katman sayısı sabit kalır; elektronlar daha çok çekilir, yarıçap küçülür'),
   'II':(True,'soldan sağa gidildikçe elektronlar daha sıkı tutulur, iyonlaşma enerjisi genel olarak artar'),
   'III':(False,'aynı periyottaki atomların katman sayıları eşittir, soldan sağa değişmez')}
r=onc(d,[('I',),('III',),('I','II'),('I','III'),('II','III')])
q('0014',tipId='km-ps2-periyotta',tip='Periyotta soldan sağa değişim',z='kolay',kaz='Aynı periyotta soldan sağa atom yarıçapı, iyonlaşma enerjisi ve katman sayısının değişimini yorumlar.',kalip='öncüllü',
 kart='K-KMPS2-14 (periyotta değişim) · 2. periyot Li → Ne',
 metin='Bir öğretmen tahtaya periyodik sistemin 2. periyodunda yer alan Li, Be, B, C, N, O, F ve Ne elementlerini soldan sağa doğru yazıyor. Öğrencilerden bu sıra boyunca atom özelliklerinin nasıl değiştiğine dair birer yargı yazmalarını istiyor. Öğrencilerin yargıları aşağıda verilmiştir.\nI. Atom yarıçapı genel olarak azalır.\nII. Birinci iyonlaşma enerjisi genel olarak artar.\nIII. Atomların katman sayısı artar.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['2. periyottaki bütün atomların elektronlarının kaç katmana yerleştiğini düşün.'],
 bilgi=[B('Periyotta değişim','Aynı periyotta katman sayısı sabittir; atom numarası arttıkça çekirdek yükü artar. Bu yüzden soldan sağa atom yarıçapı azalır, iyonlaşma enerjisi ve elektronegatiflik genel olarak artar. Örnek: Cl atomu Na atomundan küçüktür')],
 ad=[A('Katman sayısı','2. periyotta her atom iki katmanlıdır.','III yanlış'),A('Yarıçap','Çekirdek yükü arttıkça elektronlar daha güçlü çekilir.','I doğru'),A('İyonlaşma enerjisi','Elektronlar daha sıkı tutulur.','II doğru'),A('Sonuç','Doğrular toplanır.',etk(d)+' · '+r['dogru'])],
 puf='Aynı periyotta katman sabit, çekirdek yükü artar: yarıçap ↓, iyonlaşma enerjisi ↑.')
# ================= 15 · iyon ve konumdan atom numaraları toplamı · zor · düz =================
kartla('15','İyon eşitliği ve konumdan atom numaraları toplamı','Konumdan X ve Y bulunur; Y³⁻ iyonunun elektron sayısı Z²⁺ ile eşitlenerek Z’nin atom numarası bulunur.','Anyonda elektron sayısını yük kadar eksiltmek; iyondaki elektron sayısını atom numarası sanmak.','zor','düz',5,'toplam','İyon eşitliği ve konumdan atom numaraları toplamı')
ZX_,ZY_=7,15; assert yer(ZX_)==(2,5) and yer(ZY_)==(3,5)
eY3=ZY_+3; ZZ_=eY3+2; assert eY3==18 and ZZ_==20 and ZX_+ZY_+ZZ_==42
assert ZX_+ZY_+(ZY_-3+2)==36 and ZX_+ZY_+(eY3-2)==38 and ZX_+ZY_+eY3==40 and ZX_+ZY_+(eY3+2+2)==44
q('0015',tipId='km-ps2-toplam',tip='İyon eşitliği ve konumdan atom numaraları toplamı',z='zor',kaz='Konumdan atom numarasını bulup iyonların elektron sayısı eşitliğinden diğer elementin atom numarasını belirler.',kalip='düz',
 kart='K-KMPS2-15 (konum + izoelektronik iyon, toplam) · N, P, Ca',
 metin='Periyodik sistemin ilk dört periyodunda yer alan X, Y ve Z elementleri için şu bilgiler veriliyor.\n• X, 2. periyotta 5A grubundadır.\n• Y, X ile aynı grupta ve 3. periyottadır.\n• Y³⁻ iyonu ile Z²⁺ iyonunun elektron sayıları eşittir.\nBuna göre X, Y ve Z’nin atom numaraları toplamı kaçtır?',
 dogru=42,yan=[(36,'Y³⁻ iyonunda elektron sayısını yük kadar eksiltip 12 bulmuş; anyon elektron almıştır: 15 + 3 = 18.','islem'),(38,'Z²⁺ iyonunda 18 elektron olduğunu bulmuş ama Z’nin atom numarasını 18 − 2 = 16 almış; katyonda atom numarası elektron sayısından 2 fazladır.','islem'),(40,'Z²⁺ iyonundaki elektron sayısını (18) Z’nin atom numarası sanmış.','bilgi'),(44,'Z’nin atom numarasını bulurken yükü iki kez eklemiş: 18 + 2 + 2 = 22.','islem')],
 istenen='X, Y ve Z’nin atom numaraları toplamı.',ip=['Önce X ve Y’nin atom numaralarını dizilimden bul; sonra Y³⁻ iyonundaki elektron sayısını hesapla.'],
 bilgi=[B('Konum ve iyon elektron sayısı','Konumdan elektron dizilimi ve atom numarası bulunur. Anyon, yükü kadar elektron almıştır; katyon, yükü kadar elektron vermiştir. Elektron sayıları eşit olan taneciklere izoelektronik denir. Örnek: 2, 8, 3 dizilimli atom 3. periyot 3A’dadır ve atom numarası 13’tür')],
 ad=[A('X ve Y','X: 2. periyot 5A; Y: 3. periyot 5A.','X: 2, 5 → 7 · Y: 2, 8, 5 → 15'),A('Y³⁻ iyonu','Anyon 3 elektron almıştır.','15 + 3 = 18 elektron'),A('Z²⁺ iyonu','Katyon 2 elektron vermiştir; elektron sayısı 18’dir.','Z atomunda 18 + 2 = 20 elektron'),A('Z’nin yeri','Z’nin atom numarası 20’dir.','Z: 4. periyot 2A'),A('Toplam','Üç atom numarası toplanır.','7 + 15 + 20 = 42')],
 puf='Katyonda atom numarası = iyondaki elektron + yük; anyonda iyondaki elektron − yük.')
# ================= 16 · kesit: üç yargı · zor · öncüllü =================
kartla('16','Kesitte periyodik özellik yargıları','Atom yarıçapı, elektronegatiflik ve metalik karakter eğilimleri periyotta ve grupta zincirle birleştirilir.','Eğilimlerin yönünü karıştırmak; farklı grup ve periyottaki elementleri doğrudan kıyaslamak.','zor','öncüllü',5,'kesit-yargi','Kesitte periyodik özellik yargıları')
dZ={11:'X',13:'Y',17:'Z',9:'T'}
assert yer(11)==(3,1) and yer(13)==(3,3) and yer(17)==(3,7) and yer(9)==(2,7)
d={'I':(False,'X, Y’nin solunda olduğundan X’in atom yarıçapı Y’ninkinden büyüktür; Y > X değildir'),
   'II':(True,'T ve Z aynı grupta (T yukarıda), Z ve Y aynı periyotta (Z sağda), Y ve X aynı periyotta (Y sağda): T > Z > Y > X'),
   'III':(True,'X, Y, Z aynı periyotta soldan sağa dizilidir; T, Z’nin üstündedir: metalik karakter X > Y > Z > T')}
r=onc(d,[('I',),('II',),('I','II'),('II','III'),('I','II','III')])
SK=kesit(dZ,3)
q('0016',tipId='km-ps2-kesit-yargi',tip='Kesitte periyodik özellik yargıları',z='zor',kaz='Kesitte yeri verilen elementlerin atom yarıçapı, elektronegatiflik ve metalik karakterini karşılaştırır.',kalip='öncüllü',
 kart='K-KMPS2-16 (kesit, üç yargı) · Na, Al, Cl, F',sekil=SK,
 metin='Şekildeki kesitte periyodik sistemin ilk üç periyodunda yer alan X, Y, Z ve T elementleri işaretlenmiştir. Bir öğrenci, elementlerin periyodik özelliklerini karşılaştırmak için kesite bakıp aşağıdaki yargıları yazmıştır.\nI. Atom yarıçapı Y > X’tir.\nII. Elektronegatiflik T > Z > Y > X’tir.\nIII. Metalik karakter X > Y > Z > T’dir.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Elementlerin ikili karşılaştırmalarını önce aynı grup ya da aynı periyottakiler arasında yap, sonra zinciri birleştir.'],
 bilgi=[B('Periyodik özelliklerin zinciri','Elektronegatiflik sağa ve yukarı artar; metalik karakter ve atom yarıçapı sola ve aşağı artar. Ara elementler arasında doğrudan karşılaştırma yapılamıyorsa zincir kurulur. Örnek: O > S (grupta yukarı) ve S > P (periyotta sağa)')],
 ad=[A('Konumlar','Harfler okunur.','X: 3. per. 1A · Y: 3. per. 3A · Z: 3. per. 7A · T: 2. per. 7A'),A('I. yargı','X, Y’nin solundadır.','yarıçap X > Y → I yanlış'),A('II. yargı','T > Z (grup), Z > Y > X (periyot).','II doğru'),A('III. yargı','Metalik karakter elektronegatifliğin tersine değişir.','III doğru'),A('Sonuç','Doğrular toplanır.',r['dogru'])],
 puf='Metalik karakter, elektronegatifliğin tersi yönde değişir.')
# ================= 17 · grafik: atom yarıçapı çubuk grafiği · zor · olumsuz =================
kartla('17','Atom yarıçapı grafiğinden element yorumu','Aynı grupta aşağıdaki elementin yarıçapı büyüktür; aynı periyotta soldaki elementin yarıçapı büyüktür. Yarıçap grafiği, elementlerin göreli konumunu verir.','Yarıçapı büyük olanın iyonlaşma enerjisini de büyük sanmak.','zor','grafik',5,'grafik-yaricap','Atom yarıçapı grafiğinden element yorumu')
RV=[('X',186),('Y',152),('Z',99),('T',71)]
assert yer(11)==(3,1) and yer(3)==(2,1) and yer(17)==(3,7) and yer(9)==(2,7) and ayp(11,17) and ayp(3,9)
coords=' '.join(f'({i+1},{v})' for i,(_,v) in enumerate(RV))
g='\\begin{axis}[scaled y ticks=false,ybar,bar width=16pt,width=7.4cm,height=5.4cm,xmin=.4,xmax=4.6,ymin=0,ymax=200,xtick={1,2,3,4},xticklabels={X,Y,Z,T},ytick={0,50,100,150,200},yticklabel style={font=\\scriptsize},xticklabel style={font=\\small},axis lines=left,xlabel={Element},ylabel={Atom yarıçapı (pm)},xlabel style={font=\\small},ylabel style={font=\\small}]\n'
g+=f'\\addplot[fill=vurgu!35,draw=black] coordinates {{{coords}}};\n\\end{{axis}}'
SK=tk(g)
S=[('X’in birinci iyonlaşma enerjisi Y’ninkinden büyüktür.',False,'X, Y ile aynı grupta ve Y’nin altındadır; aşağı inildikçe iyonlaşma enerjisi azalır, X’in değeri Y’ninkinden küçüktür'),
   ('Y’nin atom numarası X’inkinden küçüktür.',True,'Y, X ile aynı grupta ve X’in üstündedir; üstteki elementin atom numarası küçüktür'),
   ('Z’nin elektronegatifliği T’ninkinden küçüktür.',True,'aynı grupta T, Z’nin üstündedir; yukarıdaki T’nin elektronegatifliği büyüktür'),
   ('X ve Z’nin katman sayıları eşittir.',True,'ikisi de aynı periyottadır'),
   ('Y ve T aynı periyottadır.',True,'X ve Z 3. periyotta olduğundan, onların üstündeki Y ve T 2. periyottadır')]
r=tek(S,False)
q('0017',tipId='km-ps2-grafik-yaricap',tip='Atom yarıçapı grafiğinden element yorumu',z='zor',kaz='Atom yarıçapı grafiğinden elementlerin göreli konumlarını bulup periyodik özelliklerini karşılaştırır.',kalip='grafik',
 kart='K-KMPS2-17 (yarıçap grafiği) · Li, Na, F, Cl',sekil=SK,
 metin='İlk üç periyotta yer alan X, Y, Z ve T elementlerinin atom yarıçapları şekildeki çubuk grafikte verilmiştir. X ile Y 1A grubunda, Z ile T 7A grubundadır. X ve Z elementleri aynı periyottadır. Öğrenciler, grafikteki verilerden elementlerin konumlarını bulup aralarındaki farkları yorumluyor.\nBuna göre aşağıdaki yorumlardan hangisi yanlıştır?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Yanlış olan yorum.',ip=['Aynı gruptaki iki elementten yarıçapı büyük olanın tablonun neresinde olduğunu düşün; sonra periyotları belirle.'],
 bilgi=[B('Yarıçap ve konum','Aynı grupta yukarıdan aşağı yarıçap artar; aynı periyotta soldan sağa azalır. Bu nedenle yarıçap grafiği elementlerin göreli konumunu verir. Örnek: aynı gruptaki iki elementten yarıçapı büyük olan daha alt periyottadır')],
 ad=[A('Grup içi karşılaştır','X, Y’den; Z, T’den büyük yarıçaplıdır.','X, Y’nin altında · Z, T’nin altında'),A('Periyotları bul','X ve Z aynı periyottadır, X ve Z altta olduğundan 3. periyottadır.','X, Z: 3. per. · Y, T: 2. per.'),A('Özellikleri karşılaştır','Gruplarda aşağı inildikçe iyonlaşma enerjisi ve elektronegatiflik azalır.','İE: Y > X · EN: T > Z'),A('Yorumları ele','Her yorum bulunan konumlarla karşılaştırılır.','tek yanlış yorum seçilir'),A('Sonuç','X’in iyonlaşma enerjisi Y’ninkinden küçüktür.',r['dogru'])],
 puf='Yarıçap büyükse aşağıdasın ya da soldasın: iyonlaşma enerjisi ve elektronegatiflik küçülür.')
# ================= 18 · metal, yarı metal ve ametal yargıları · orta · öncüllü =================
kartla('18','Metal, yarı metal ve ametal yargıları','3. periyotta Al metal, Si yarı metal, S ametaldir; sınıflama konumdan yapılır.','Alüminyumu yarı metal ya da kükürdü metal saymak.','orta','öncüllü',4,'sinif-yarimetal','Metal, yarı metal ve ametal yargıları')
assert yer(13)==(3,3) and yer(14)==(3,4) and yer(16)==(3,6)
d={'I':(True,'14. element silisyumdur; metal ile ametal arasında yer alan, yarı iletken bir yarı metaldir'),
   'II':(True,'13. element alüminyumdur; 14. elementin solunda yer alan, elektriği iyi ileten bir metaldir'),
   'III':(False,'16. element kükürttür; 6A grubunda yer alan bir ametaldir, metal değildir')}
r=onc(d,[('I',),('I','II'),('I','III'),('II','III'),('I','II','III')])
q('0018',tipId='km-ps2-sinif-yarimetal',tip='Metal, yarı metal ve ametal yargıları',z='orta',kaz='Atom numarasından elementin konumunu bulup metal, yarı metal ve ametal olarak sınıflandırır.',kalip='öncüllü',
 kart='K-KMPS2-18 (metal, yarı metal, ametal) · atom numaraları 13, 14, 16',
 metin='Atom numaraları sırasıyla 13, 14 ve 16 olan X, Y ve Z elementleri için bir öğrenci elektron dizilimlerini yazıp periyodik sistemdeki yerlerini buluyor. Daha sonra elementleri metal, yarı metal ve ametal olarak sınıflandırmak için aşağıdaki yargıları yazıyor.\nI. Y bir yarı metaldir.\nII. X, Y’nin solunda yer alan bir metaldir.\nIII. Z bir metaldir ve 3. periyotta yer alır.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Tabloda metaller soldadır, ametaller sağdadır; ikisinin arasında bir geçiş bölgesi vardır.'],
 bilgi=[B('Metal, yarı metal, ametal','Tablonun sol tarafındaki elementlerin çoğu metaldir; sağ tarafı ametallerdir. Metal–ametal sınırında yarı metaller bulunur; bunlar parlak ama kırılgandır ve yarı iletkendir. Örnek: bor ve germanyum yarı metaldir')],
 ad=[A('Dizilimler','Atom numaralarından dizilimler bulunur.','X: 2, 8, 3 · Y: 2, 8, 4 · Z: 2, 8, 6'),A('Konumlar','Hepsi 3. periyottadır.','X: 3A · Y: 4A · Z: 6A'),A('Yargıları incele','Her yargı konum ve sınıfla karşılaştırılır.',etk(d)),A('Sonuç','Doğrular toplanır.',r['dogru'])],
 puf='Metal–ametal sınırındaki elementler yarı metaldir.')
# ================= 19 · kesit: izoelektronik iyon · zor =================
kartla('19','İyon elektron sayısından kesitte konum','X²⁻ iyonunun elektron sayısı bulunur; Y⁺ aynı sayıda elektronluysa Y’nin atom numarası bir fazladır.','Y⁺ yerine Y⁻ ya da Y²⁺ düşünmek; nötr atomun elektron sayısını iyonunkiyle karıştırmak.','zor','şekilli',5,'iyon-kesit','İyon elektron sayısından kesitte konum')
dZ={8:'X',3:'1',11:'2',12:'3',19:'4',10:'5'}
assert yer(8)==(2,6) and 8+2==10 and 11-1==10 and 12-2==10 and 3-1==2 and 19-1==18
SK=kesit(dZ,4)
q('0019',tipId='km-ps2-iyon-kesit',tip='İyon elektron sayısından kesitte konum',z='zor',kaz='İyonların elektron sayısı eşitliğinden elementin atom numarasını bulup kesitteki yerini belirler.',kalip='şekilli',
 kart='K-KMPS2-19 (izoelektronik iyon, kesit) · X²⁻ ve Y⁺',sekil=SK,
 metin='Şekilde periyodik sistemin ilk dört periyodunu gösteren kesitte X harfiyle ve 1, 2, 3, 4, 5 numaralarıyla beş element işaretlenmiştir. X²⁻ iyonu ile Y⁺ iyonunun elektron sayıları birbirine eşittir. Y elementi numaralı elementlerden biridir ve nötr atom hâlinde düşünülmelidir.\nBuna göre Y elementi şekilde hangi numarayla gösterilmiştir?',
 dogru='2',sira=['1','2','3','4','5'],yan=[('1','Y’nin 1A’da olması gerektiğini bulmuş ama 2. periyottaki elementi seçmiş; o elementin iyonunda yalnızca 2 elektron vardır.','dikkat'),('3','2. gruptaki elementi seçmiş; oysa bu elementin iyonu 2+ yüklüdür, Y⁺ değildir.','dikkat'),('4','Aynı grupta daha aşağıdaki elementi seçmiş; o elementin iyonunda 18 elektron vardır.','dikkat'),('5','10 sayısını atom numarası sanıp son sütundaki elementi seçmiş; Y⁺ iyonu 10 elektronluysa Y’nin atom numarası 11’dir.','bilgi')],
 istenen='Y elementinin şekildeki numarası.',ip=['Önce X²⁻ iyonundaki elektron sayısını bul; sonra Y atomunun kaç elektronu olduğunu yükten yararlanarak hesapla.'],
 bilgi=[B('İyon ve elektron sayısı','Anyon, yükü kadar elektron almıştır; katyon, yükü kadar elektron vermiştir. Elektron sayıları eşit olan taneciklere izoelektronik denir. Örnek: S²⁻ ve Ca²⁺ ikisi de 18 elektronludur')],
 ad=[A('X’i bul','X, 2. periyot 6A’dadır.','2, 6 → 8 elektron'),A('X²⁻ iyonu','2 elektron almıştır.','8 + 2 = 10 elektron'),A('Y atomu','Y⁺, bir elektron vermiştir.','Y: 10 + 1 = 11 elektron → 2, 8, 1'),A('Kesitte yeri','3. periyot 1A.','3. satır, 1A sütunu')],
 puf='Katyonda nötr atomun elektron sayısı = iyondaki + yük; anyonda = iyondaki − yük.')
# ================= 20 · soy gaz ve hidrojen · orta · öncüllü =================
kartla('20','Hidrojen ve soy gazlar','Hidrojen 1A’dadır ama ametaldir; helyumun son katmanında 2 elektron vardır; soy gazların kimyasal tepkimeye girme eğilimi çok düşüktür.','Hidrojeni alkali metal saymak; tüm soy gazlarda 8 değerlik elektronu aramak.','kolay','öncüllü',3,'h-soygaz','Hidrojen ve soy gazlar')
d={'I':(False,'helyumun son katmanında 2 elektron vardır; diğer soy gazlarda 8’dir'),
   'II':(True,'hidrojen 1A grubunda yer alır ancak metal değil, ametaldir'),
   'III':(True,'soy gazların son katmanları doludur; kimyasal tepkimeye girme eğilimleri çok düşüktür')}
r=onc(d,[('I',),('II',),('I','II'),('I','III'),('II','III')])
q('0020',tipId='km-ps2-h-soygaz',tip='Hidrojen ve soy gazlar',z='kolay',kaz='Hidrojenin ve soy gazların periyodik sistemdeki yerini ve özelliklerini yorumlar.',kalip='öncüllü',
 kart='K-KMPS2-20 (hidrojen, soy gazlar) · H, He, Ne, Ar',
 metin='Bir lise öğrencisi, periyodik sistemin sol üst köşesinde yer alan hidrojenle sağ sütundaki soy gazları karşılaştıran bir poster hazırlıyor. Posterde hidrojenin periyodik sistemdeki yeri ve ametal ya da metal özelliği ile helyum, neon ve argon gibi soy gazların değerlik elektron sayıları ve tepkimeye girme eğilimleri yer alıyor.\nI. Soy gazların hepsinin son katmanında 8 elektron vardır.\nII. Hidrojen, 1A grubunda yer almasına karşın ametaldir.\nIII. Soy gazların kimyasal tepkimeye girme eğilimleri çok düşüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Helyum 1. periyotta yer alır; ilk katmanın kaç elektron alabileceğini düşün.'],
 bilgi=[B('Hidrojen ve soy gazlar','Hidrojen 1A’dadır ve ametaldir. Soy gazlar 8A’dadır; He’un son katmanında 2, diğerlerinde 8 elektron vardır. Kararlı oldukları için tepkimeye girme eğilimleri çok düşüktür. Örnek: Ne ve Ar doğada tek atomlu gazlardır')],
 ad=[A('I. yargı','He’un dizilimi 1. katmanda 2 elektronla sınırlıdır.','I yanlış'),A('II. yargı','H, 1A’dadır; ametaldir.','II doğru'),A('III. yargı','Son katmanları doludur.','III doğru'),A('Sonuç','Doğrular toplanır.',etk(d)+' · '+r['dogru'])],
 puf='H: 1A ama ametal; He: 8A ama 2 değerlik elektronu.')
# ================= 21 · elektronegatiflik sıralaması · orta · düz =================
kartla('21','Elektronegatiflik sıralaması','Elektronegatiflik periyotta sağa, grupta yukarı gidildikçe artar.','Atom numarası büyük olanın elektronegatifliğinin büyük olduğunu sanmak.','orta','düz',3,'en-sira','Elektronegatiflik sıralaması')
Ze={'X':7,'Y':8,'Z':15}; assert yer(7)==(2,5) and yer(8)==(2,6) and yer(15)==(3,5)
S=[('X > Y > Z',False,'Y, X ile aynı periyottadır ve sağdadır; Y > X olur'),('Y > Z > X',False,'Z, X’in altındadır; yukarıdaki X’in elektronegatifliği daha büyüktür'),('Z > Y > X',False,'Z, 3. periyottadır; aşağıda olduğu için elektronegatifliği küçüktür'),('Z > X > Y',False,'Z’yi en elektronegatif, Y’yi en küçük sanmak eğilimlerin ikisini de ters yorumlamaktır'),('Y > X > Z',True,'')]
r=tek(S,True)
q('0021',tipId='km-ps2-en-sira',tip='Elektronegatiflik sıralaması',z='orta',kaz='Atom numarasından konum bulup elementlerin elektronegatifliklerini sıralar.',kalip='düz',
 kart='K-KMPS2-21 (elektronegatiflik) · atom numaraları 7, 8, 15',
 metin='Bir öğrenci, atom numaraları sırasıyla 7, 8 ve 15 olan X, Y ve Z elementlerinden oluşan bileşiklerde bağ elektronlarının hangi atoma daha çok kaydığını tahmin etmek istiyor. Bunun için önce elektron dizilimlerinden elementlerin periyodik sistemdeki yerlerini bulacak, sonra elektronegatiflik eğilimlerinden yararlanacaktır.\nBuna göre X, Y ve Z elementlerinin elektronegatiflikleri arasındaki ilişki aşağıdakilerden hangisinde doğru verilmiştir?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Elektronegatifliğin büyükten küçüğe sıralaması.',ip=['Elektron dizilimlerinden periyot ve grup bul; elektronegatifliğin periyotta ve grupta hangi yöne arttığını düşün.'],
 bilgi=[B('Elektronegatiflik','Bağdaki elektronları çekme eğilimidir. Periyotta soldan sağa artar, grupta yukarıdan aşağı azalır. Örnek: F, Cl’dan; Cl ise Na’dan daha elektronegatiftir')],
 ad=[A('Konumlar','Dizilimler yazılır.','X: 2, 5 (2. per. 5A) · Y: 2, 6 (2. per. 6A) · Z: 2, 8, 5 (3. per. 5A)'),A('Aynı periyot','X ve Y 2. periyottadır; Y daha sağdadır.','Y > X'),A('Aynı grup','X ve Z 5A’dadır; X yukarıdadır.','X > Z'),A('Sıralama','İki sonuç birleştirilir.','Y > X > Z')],
 puf='Elektronegatiflik: sağa ↑, yukarı ↑.')
# ================= 22 · tablo: birinci iyonlaşma enerjisi ve yargılar · orta · öncüllü =================
kartla('22','Tabloda birinci iyonlaşma enerjisi ve yargılar','Atom yarıçapı periyotta sağa küçülür; iyonlaşma enerjisi yorumu verilen gerçek değerlerle yapılır.','Birinci iyonlaşma enerjisinin periyotta her zaman arttığını varsaymak.','orta','öncüllü',4,'tablo-yargi','Tabloda birinci iyonlaşma enerjisi ve yargılar')
T2={'X':900,'Y':801,'Z':1086,'T':1402}
assert T2['Y']<T2['X'] and T2['T']>T2['Z']
SK=tablo_svg(['Element','İE₁ (kJ/mol)'],[[k,f'{v:,}'.replace(',','.')] for k,v in T2.items()])
d={'I':(True,'X 2A grubunda yer alan bir toprak alkali metaldir'),
   'II':(False,'tabloda Y’nin birinci iyonlaşma enerjisi (801) X’inkinden (900) küçüktür'),
   'III':(True,'T, Z’nin sağındadır; aynı periyotta sağa gidildikçe atom yarıçapı küçülür')}
r=onc(d,[('I',),('II',),('I','II'),('I','III'),('I','II','III')])
q('0022',tipId='km-ps2-tablo-yargi',tip='Tabloda birinci iyonlaşma enerjisi ve yargılar',z='orta',kaz='Birinci iyonlaşma enerjisi tablosunu ve konumları kullanarak periyodik özellikler hakkındaki yargıları değerlendirir.',kalip='öncüllü',
 kart='K-KMPS2-22 (tablo, yargılar) · Be, B, C, N',sekil=SK,
 metin='Atom numaraları ardışık artan ve 2. periyotta yer alan X, Y, Z ve T elementlerinden X, 2A grubundadır. Bu elementlerin gaz hâlindeki atomlarından birer elektron koparmak için gereken enerjiler (kJ/mol) tabloda verilmiştir. Bir öğrenci tablodaki verilerden ve periyodik özelliklerden yararlanarak yargılar yazıyor.\nI. X, toprak alkali metaldir.\nII. Y’nin birinci iyonlaşma enerjisi, X’inkinden büyüktür.\nIII. T’nin atom yarıçapı, Z’ninkinden küçüktür.\nBuna göre bu yargılardan hangileri doğrudur?',
 dogru=r['dogru'],yan=r['yan'],sira=r['sira'],istenen='Doğru olan yargılar.',ip=['Elementlerin periyottaki sırasını belirle; her yargıda hangi bilginin tablodan, hangisinin konumdan geldiğine bak.'],
 bilgi=[B('Yarıçap ve iyonlaşma enerjisi','Aynı periyotta soldan sağa atom yarıçapı azalır. İyonlaşma enerjisi sorularında verilen sayısal değerler dikkate alınır. Örnek: 2A grubu elementlerine toprak alkali metaller denir')],
 ad=[A('Konumlar','Ardışık elementler 2A’dan başlayarak sağa doğru dizilir.','X: 2A · Y: 3A · Z: 4A · T: 5A'),A('I. yargı','2A grubu toprak alkali metaldir.','I doğru'),A('II. yargı','Tablodaki değerler karşılaştırılır.','801 < 900 → II yanlış'),A('III. yargı','T, Z’nin sağındadır.','yarıçap Z > T → III doğru'),A('Sonuç','Doğrular toplanır.',r['dogru'])],
 puf='Atom yarıçapı eğilimini konumdan, iyonlaşma enerjisini ise verilen değerlerden oku.')
bitir(P,'periyodikiki',UK)
