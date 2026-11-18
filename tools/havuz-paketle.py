#!/usr/bin/env python3
"""Soru havuzunu functions/havuz/ altına paketler (yalnız koç erişimi için, havuzGetir ile sunulur).
Kullanım: python3 tools/havuz-paketle.py /yol/havuz"""
import json, glob, os, re, sys, shutil, gzip, subprocess, base64
from collections import OrderedDict

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KOK, "functions", "havuz")
DERSLER = [("mat", "TYT Matematik", ["mat", "prob", "matd"]), ("geo", "TYT Geometri", ["geo"]),
           ("fiz", "TYT Fizik", ["fiz"]), ("kim", "TYT Kimya", ["kim"]), ("bio", "TYT Biyoloji", ["bio"]),
           ("amat", "AYT Matematik", ["amat"])]
KLASOR = {"amat": "ayt-mat"}  # diğerleri tyt-<id>
SINAV = {"amat": "AYT"}  # diğerleri TYT
ALANLAR = ["id", "konu", "kazanim", "zorluk", "kalip", "metin", "sekil", "siklar", "sekilPng", "cevap", "adimlar", "ipuclari", "bilgi", "puf", "celdiriciler", "kardes", "kartId"]
TR = str.maketrans("çğıöşüâîûÇĞİÖŞÜÂÎÛ", "cgiosuaiuCGIOSUAIU")

def slug(s):
    s = s.translate(TR).lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "konu"

BUYUK = 100 * 1024

def png(svg):
    r = subprocess.run(["rsvg-convert", "-w", "640", "-f", "png"], input=svg.encode("utf-8"), capture_output=True, check=True)
    return "data:image/png;base64," + base64.b64encode(r.stdout).decode()

def kucult(o):
    """100 KB'tan büyük SVG'yi PNG'ye çevirir: sekil boşalır, sekilPng dolar."""
    if isinstance(o.get("sekil"), str) and len(o["sekil"]) > BUYUK:
        o["sekilPng"] = png(o["sekil"]); o["sekil"] = ""
        print("PNG:", o.get("id"), file=sys.stderr)
    return o

def yaz(yol, veri):
    b = json.dumps(veri, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    with open(yol + ".gz", "wb") as h, gzip.GzipFile(filename="", mode="wb", fileobj=h, compresslevel=9, mtime=0) as f:
        f.write(b)  # mtime=0: aynı veri aynı dosyayı üretir

def norm(s):
    s = s.translate(TR).lower()
    s = re.sub(r"\bve\b", " ", s)
    return re.sub(r"[^a-z0-9]+", "", s)

def app_sirasi(hav):
    """app.js içindeki CUR.TYT konu sırası: {ders: [norm adlar]}"""
    src = open(os.path.join(KOK, "public", "app.js"), encoding="utf-8").read()
    m = re.search(r"^const CUR = (\{.*\});\s*$", src, re.M)
    out = {}
    if not m:
        return out
    try:
        cur = json.loads(m.group(1))
    except Exception:
        return out
    for d, _, onekler in DERSLER:
        sira = []
        for o in onekler:
            for x in cur.get(SINAV.get(d, "TYT"), []):
                if x["k"] == o:
                    sira += [norm(t) for t in x["t"]]
        out[d] = sira
    return out

def main():
    if len(sys.argv) < 2:
        sys.exit("Kullanım: havuz-paketle.py <havuz-klasörü>")
    hav = os.path.abspath(sys.argv[1])
    kartlar = json.load(open(os.path.join(hav, "tekrar", "kartlar.json"), encoding="utf-8"))
    soru_kart = json.load(open(os.path.join(hav, "tekrar", "soru-kart.json"), encoding="utf-8"))
    sira = app_sirasi(hav)
    if os.path.isdir(CIKTI):
        shutil.rmtree(CIKTI)
    os.makedirs(os.path.join(CIKTI, "kartlar"))
    index = {"dersler": []}
    enb = [0]
    for d, ad, onekler in DERSLER:
        os.makedirs(os.path.join(CIKTI, d), exist_ok=True)
        konular = OrderedDict()  # k -> [sorular]
        gor = set()
        for f in sorted(glob.glob(os.path.join(hav, KLASOR.get(d, f"tyt-{d}"), "*.json"))):
            x = json.load(open(f, encoding="utf-8"))
            x = x if isinstance(x, list) else x.get("sorular", [])
            kardes = os.path.basename(f).endswith("-kardes.json")
            for q in x:
                if not isinstance(q, dict) or "cevap" not in q:
                    continue
                k = q.get("k", "")
                if k.split("|")[0] not in onekler:
                    raise SystemExit(f"Beklenmeyen konu anahtarı {k} ({f})")
                o = {a: q.get(a) for a in ALANLAR if a not in ("kardes", "kartId")}
                o["kardes"] = kardes
                o["kartId"] = soru_kart.get(q.get("id"))
                kucult(o)
                if q["id"] in gor:
                    raise SystemExit(f"Yinelenen soru kimliği {q['id']}")
                gor.add(q["id"])
                konular.setdefault(k, []).append(o)
        ilk = {k: i for i, k in enumerate(konular)}
        sr = sira.get(d, [])
        def anahtar(k):
            n = norm(k.split("|", 1)[1])
            return (0, sr.index(n), 0) if n in sr else (1, 0, ilk[k])
        liste = []
        for k in sorted(konular, key=anahtar):
            qs = konular[k]
            if k.split("|", 1)[1] and norm(k.split("|", 1)[1]) not in sr:
                print(f"UYARI: {k} uygulama listesinde bulunamadı, sona eklendi", file=sys.stderr)
            dosya = slug(k.replace("|", " ")) + ".json"
            yaz(os.path.join(CIKTI, d, dosya), qs)
            acik = len(json.dumps(qs, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
            enb[0] = max(enb[0], acik)
            z = {"kolay": 0, "orta": 0, "zor": 0}
            for q in qs:
                z[q["zorluk"]] = z.get(q["zorluk"], 0) + 1
            liste.append({"k": k, "ad": k.split("|", 1)[1], "adet": len(qs), "sekilli": sum(1 for q in qs if q.get("sekil")), "zorluk": z, "dosya": dosya})
        assert len({k["dosya"] for k in liste}) == len(liste), "dosya adı çakışması"
        index["dersler"].append({"id": d, "ad": ad, "adet": sum(k["adet"] for k in liste), "konular": liste})
        kd = OrderedDict((c["id"], kucult(dict(c))) for c in kartlar if c.get("k", "").split("|")[0] in onekler)
        yaz(os.path.join(CIKTI, "kartlar", d + ".json"), kd)
        print(d, len(liste), "konu", index["dersler"][-1]["adet"], "soru", len(kd), "kart")
    yaz(os.path.join(CIKTI, "index.json"), index)
    toplam = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(CIKTI) for f in fs)
    print(f"Toplam: {toplam/1048576:.1f} MB")
    print(f"En büyük konu dosyası (açılmış): {enb[0]/1048576:.2f} MB")
    if enb[0] > 5 * 1048576:
        sys.exit("HATA: bir konu dosyası 5 MB sınırını aşıyor")
    if toplam > 60 * 1048576:
        sys.exit("HATA: functions/havuz 60 MB sınırını aşıyor")

main()
