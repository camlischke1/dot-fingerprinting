#!/bin/bash

names=("a.cam.com" "cam.cam.com" "howlongcanimakeadomainname.cam.com" "windows-dns.cam.com" "windows-client.cam.com" "ubuntu-client.cam.com")

for i in {0..199999..1}
do
	rand=$[$RANDOM/16383]
	echo -n $rand >> labels.txt
	if [ $rand == 1 ]
	then
		q ubuntu-dns.cam.com A @tls://192.168.126.131 > /dev/null
		echo ", ubuntu-dns.cam.com" >> labels.txt
	fi

	if [ $rand != 1 ]
	then
		index=$[RANDOM % 5]
		q ${names[$index]} A @tls://192.168.126.131 > /dev/null
		echo ", ${names[$index]}" >> labels.txt
	fi
done
