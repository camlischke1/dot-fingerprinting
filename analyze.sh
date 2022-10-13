#!/bin/bash

for stream in {0..100000}

do
    tshark -r dot.pcapng -Y "tcp.stream==$stream && tls" -T fields -E header=y -E separator=, -E occurrence=f \
	-E quote=s -e tcp.stream -e ip.src -e ip.dst -e ip.len -e ip.ttl -e ip.proto -e tcp.window_size \
	-e tcp.ack -e tcp.seq -e tcp.len -e frame.time_relative -e frame.time_delta \
	-e tcp.time_relative -e tcp.time_delta -e tls.record.content_type -e _ws.col.Length \
	-e tls.record.length -e tls.app_data >> dot.csv
done
