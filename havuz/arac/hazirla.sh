#!/bin/bash
# hazirla.sh <paket> onek...  → /tmp/kor/<paket>.txt (+ <onek>-once.txt)
cd /home/claude/zekacademy-app/havuz; P=$1; shift; : > /tmp/kor/$P.txt
for o in "$@"; do python3 kalite.py tyt-mat/$o $o; cp /tmp/kor/$o.txt /tmp/kor/$o-once.txt; cat /tmp/kor/$o.txt >> /tmp/kor/$P.txt; done
echo "$P: $(grep -c '^###' /tmp/kor/$P.txt) soru, şekil $(grep -c ŞEKİL /tmp/kor/$P.txt)"
