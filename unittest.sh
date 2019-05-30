#!/bin/bash


curl -s http://localhost/tikal | grep "KOBY TEST" > /dev/null
if [ $? -ne 0 ] ; then
	echo "FAILED!"
	exit 1
fi
