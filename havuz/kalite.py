"""Kullanım: python3 kalite.py <onek> [başlık]  → /tmp/kor/<onek>.txt + şekil PNG'leri, önizleme HTML /home/claude/uret/<onek>.html"""
import json,sys,os,subprocess
R='/home/claude/zekacademy-app'; a=sys.argv[1]; kl,o=(a.split('/') if '/' in a else ('tyt-mat',a)); bas=sys.argv[2] if len(sys.argv)>2 else o
Q=json.load(open(f'{R}/havuz/{kl}/{o}-1.json'))+json.load(open(f'{R}/havuz/{kl}/{o}-1-kardes.json'))
os.makedirs('/tmp/kor',exist_ok=True)
birlesik=f'/tmp/kor/{o}-tum.json'; json.dump(Q,open(birlesik,'w'),ensure_ascii=False)
sek=[]
with open(f'/tmp/kor/{o}.txt','w') as f:
    for q in Q:
        f.write(f"### {q['id']}\n{q['metin']}\n")
        if q.get('sekil'):
            p=f"/tmp/kor/{q['id']}.png"; sek.append((q['sekil'],p)); f.write(f"[ŞEKİL: {p} dosyasındaki resme bak]\n")
        for k,v in q['siklar'].items(): f.write(f"{k}) {v}\n")
        f.write('\n')
if sek:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':520,'height':400})
        for svg,p in sek:
            pg.set_content(f'<html><body style="margin:0;background:#fff;color:#111;font-family:Plus Jakarta Sans,sans-serif"><div style="width:480px;padding:10px">{svg}</div></body></html>')
            pg.locator('div').screenshot(path=p)
        b.close()
# önizleme: tyt-mat yolunu taklit etmek için birleşik dosyayı geçici tyt-mat klasörüne koy
os.makedirs('/tmp/tyt-mat',exist_ok=True); tp=f'/tmp/tyt-mat/{o}-tum.json'; json.dump(Q,open(tp,'w'),ensure_ascii=False)
subprocess.run(['python3',f'{R}/havuz/onizleme/onizleme.py',tp,f'/home/claude/uret/{o}.html',bas],check=True,capture_output=True)
print(len(Q),'soru ·',len(sek),'şekil · /tmp/kor/'+o+'.txt')
