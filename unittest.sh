#!/bin/bash

python2.7 kobyDate.py 999 &

sleep 3

curl -s http://localhost:999/tikal | grep "KOBY TEST" > /dev/null
if [ $? -ne 0 ] ; then
	echo "FAILED!"
	exit 1
fi

kill -9 $!
