#!/bin/bash


for i in {0..24999..1}
do
		doggo ubuntu-dns.cam.com A @tls://192.168.126.131 --short > /dev/null
		echo "0" >> ssh_labels.txt
		ssh -M -S my-ctrl-socket -fNT cam@192.168.126.132 > /dev/null
		ssh -S my-ctrl-socket -O exit cam@192.168.126.132 > /dev/null

	echo $i
done






