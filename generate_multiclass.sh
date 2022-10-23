#!/bin/bash

names=("a.cam.com" "cam.cam.com" "howlongcanimakeadomainname.cam.com" "windows-dns.cam.com" "windows-client.cam.com" "ubuntu-client.cam.com")

for i in {0..299999..1}
do
	rand=$[$RANDOM % 7]
	if [ $rand == 0 ]
	then
		q ubuntu-dns.cam.com A @tls://192.168.126.131 > /dev/null
		echo "0, ubuntu-dns.cam.com" >> labels_multiclass.txt
	fi

	if [ $rand == 1 ]
	then
		q a.cam.com A @tls://192.168.126.131 > /dev/null
		echo "1, a.cam.com" >> labels_multiclass.txt
	fi

	if [ $rand == 2 ]
	then
		q cam.cam.com A @tls://192.168.126.131 > /dev/null
		echo "2, cam.cam.com" >> labels_multiclass.txt
	fi

	if [ $rand == 3 ]
	then
		q howlongcanimakeadomainname.cam.com A @tls://192.168.126.131 > /dev/null
		echo "3, howlongcanimakeadomainname.cam.com" >> labels_multiclass.txt
	fi

	if [ $rand == 4 ]
	then
		q windows-dns.cam.com A @tls://192.168.126.131 > /dev/null
		echo "4, windows-dns.cam.com" >> labels_multiclass.txt
	fi

	if [ $rand == 5 ]
	then
		q windows-client.cam.com A @tls://192.168.126.131 > /dev/null
		echo "5, windows-client.cam.com" >> labels_multiclass.txt
	fi

	if [ $rand == 6 ]
	then
		q ubuntu-client.cam.com A @tls://192.168.126.131 > /dev/null
		echo "6, ubuntu-client.cam.com" >> labels_multiclass.txt
	fi
done
