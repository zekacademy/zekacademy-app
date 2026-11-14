r"""TikZ ile şekil üretimi (geometri, devre, düzenek, üç boyutlu cisim, şema).
Kullanım:
    from cizim import tikz_svg
    svg = tikz_svg(r'''\\begin{tikzpicture} ... \\end{tikzpicture}''')   # sekil alanına yazılacak SVG metni
Paketler: tikz, tkz-euclide (geometri), circuitikz (devre), tikz-3dplot ve pgfplots (3B, grafik), mhchem (kimya formülü).
chemfig bu ortamda ÇALIŞMIYOR (simplekv eksik). Devreleri 'circuitikz' ortamıyla değil 'tikzpicture' içinde çiz
(\draw ... to[R,l=$R_1$] ...); yoksa şekil sayfa genişliğinde çıkar. Yazı tipi serifsizdir (cmss + sfmath). Siyah çizgiler 'currentColor' yapılır (uygulamanın açık/koyu temasına uyar);
vurgu rengi için TikZ'te 'vurgu' rengini kullan (uygulamadaki yeşil). Genişlik ≤ 640 olacak biçimde ölçeklenir."""
import subprocess,tempfile,os,re,hashlib
BAS=r'''\documentclass[tikz,border=3pt]{standalone}
\usepackage[utf8]{inputenc}\usepackage[T1]{fontenc}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{amsmath,amssymb}\usepackage[cm]{sfmath}\usepackage[version=4]{mhchem}
\usepackage{tkz-euclide}\usepackage[european]{circuitikz}\usepackage{tikz-3dplot}\usepackage{pgfplots}\pgfplotsset{compat=1.17}
\usetikzlibrary{angles,quotes,calc,3d,arrows.meta,decorations.pathmorphing,decorations.markings,patterns,shapes.geometric,positioning,intersections}
\definecolor{vurgu}{HTML}{16A34A}
\begin{document}
'''
SON='\n\\end{document}\n'
def tikz_svg(govde,en_cok=640,onbellek='/tmp/tikz-onbellek'):
    os.makedirs(onbellek,exist_ok=True); h=hashlib.sha1((BAS+govde).encode()).hexdigest()[:16]; hedef=f'{onbellek}/{h}.svg'
    if not os.path.exists(hedef):
        with tempfile.TemporaryDirectory() as d:
            open(f'{d}/s.tex','w').write(BAS+govde+SON)
            r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','s.tex'],cwd=d,capture_output=True,text=True)
            if r.returncode: raise RuntimeError('TikZ derlenemedi:\n'+'\n'.join(l for l in r.stdout.split('\n') if l.startswith('!') or l.startswith('l.'))[:800])
            subprocess.run(['pdftocairo','-svg','s.pdf','s.svg'],cwd=d,check=True)
            os.replace(f'{d}/s.svg',hedef)
    s=open(hedef).read()
    s=re.sub(r'<\?xml[^>]*\?>\s*','',s)
    m=re.search(r'width="([\d.]+)(?:pt)?" height="([\d.]+)(?:pt)?"',s); w,hh=float(m.group(1)),float(m.group(2))
    px=min(en_cok,round(w*1.9)); assert w<=420,('şekil çok geniş (TikZ ölçeğini küçült)',w)
    s=s.replace(m.group(0),f'style="width:100%;max-width:{px}px;height:auto" role="img"',1)
    s=re.sub(r'(?i)(fill|stroke)="rgb\(0%,\s*0%,\s*0%\)"',r'\1="currentColor"',s)
    s=re.sub(r'(?i)(fill|stroke):\s*rgb\(0%,\s*0%,\s*0%\)',r'\1:currentColor',s)
    # kimlik çakışmasını önle (aynı sayfada birden çok SVG)
    s=re.sub(r'\b(id="|xlink:href="#|url\(#)(?=[A-Za-z])',lambda m_:m_.group(1)+f't{h[:6]}-',s)
    return s.strip()
if __name__=='__main__':
    import sys
    print(len(tikz_svg(r'\begin{tikzpicture}\draw[thick] (0,0) rectangle (2,1);\node at (1,.5) {$\Omega$ deneme};\end{tikzpicture}')))
