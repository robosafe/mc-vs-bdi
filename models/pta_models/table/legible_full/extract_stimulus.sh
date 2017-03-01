#!/bin/bash

COUNTER=1
while [ $COUNTER -lt 92 ]; do
	python extract.py legibletrace-$COUNTER
	let COUNTER=COUNTER+1

done
