#!/bin/bash
# Kullanım: paket.sh <paketadı> klasor/onek ...  → denetim özeti, /tmp/kor/<paket>.txt
cd /home/claude/zekacademy-app; P=$1; shift; : > /tmp/kor/$P.txt
declare -A BZ=([tyt-mat]="/home/claude/kutup/osym_metin.json /home/claude/kutup/sorular.json" [tyt-geo]="/home/claude/kutup/osym_metin.json" [tyt-tr]=/home/claude/kutup/dersler/osym_turkce.txt [tyt-fiz]=/home/claude/kutup/dersler/osym_fizik.txt [tyt-kim]=/home/claude/kutup/dersler/osym_kimya.txt [tyt-bio]=/home/claude/kutup/dersler/osym_biyoloji.txt [tyt-tar]=/home/claude/kutup/dersler/osym_tarih.txt [tyt-cog]=/home/claude/kutup/dersler/osym_cografya.txt [tyt-fel]=/home/claude/kutup/dersler/osym_felsefe.txt)
for a in "$@"; do kl=${a%/*}; o=${a#*/}
  echo "== $a: $(python3 havuz/denetle.py havuz/$kl/$o-1.json havuz/$kl/$o-1-kardes.json --benzerlik ${BZ[$kl]} 2>/dev/null | sed -n '1p;/HATA/p')"
  python3 havuz/kalite.py $a "$o" >/dev/null && cat /tmp/kor/$o.txt >> /tmp/kor/$P.txt
done; echo "paket: $(grep -c '^###' /tmp/kor/$P.txt) soru, $(grep -c 'ŞEKİL' /tmp/kor/$P.txt) şekil"
