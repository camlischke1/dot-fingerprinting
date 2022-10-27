#!/bin/bash

while true
do
		ssh -M -S my-ctrl-socket -fNT cam@192.168.126.133 > /dev/null
		ssh -S my-ctrl-socket -O exit cam@192.168.126.133 > /dev/null

done






