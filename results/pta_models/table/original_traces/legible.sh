#!/bin/bash

COUNTER=1
while [ $COUNTER -lt 92 ]; do
	python legible_traces.py trace-$COUNTER table
	let COUNTER=COUNTER+1
done


