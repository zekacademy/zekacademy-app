#!/bin/bash
# en az $1 bekleyen konu (varsayılan 3) birikene kadar ~110 sn bekler; sonra paket $2 oluşturur ve önekleri işlenen listesine ekler
N=${1:-3}; P=$2
for i in $(seq 1 11); do n=$(/home/claude/bekleyen.sh | wc -l); [ $n -ge $N ] && break; sleep 10; done
L=$(/home/claude/bekleyen.sh | head -4); [ -z "$L" ] && { echo "bekleyen yok"; exit 0; }
/home/claude/paket.sh $P $L; for a in $L; do echo ${a#*/} >> /home/claude/islenen.txt; done; echo "PAKET $P: $L"
