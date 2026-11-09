#!/bin/bash
# HAZIR olup işlenmemiş önekleri listeler: klasör/önek
cd /home/claude/zekacademy-app/havuz
for f in tyt-*/*.HAZIR; do [ -e "$f" ] || continue; o=$(basename $f -1.HAZIR); grep -qx "$o" /home/claude/islenen.txt || echo "$(dirname $f)/$o"; done
