#!/bin/bash

names=("a.cam.com" "cam.cam.com" "howlongcanimakeadomainname.cam.com" "windows-dns.cam.com" "windows-client.cam.com" "ubuntu-client.cam.com")

for i in {0..100000..1}
do
	rand=$[$RANDOM/16383]
	echo $rand >> labels
	if [ $rand == 1 ]
	then
		q ubuntu-dns.cam.com @tls://192.168.126.131 > /dev/null
	fi
	
	if [ $rand != 1 ]
	then
		index=$[RANDOM % 5]
		q ${names[$index]} @tls://192.168.126.131 > /dev/null
	fi
done





