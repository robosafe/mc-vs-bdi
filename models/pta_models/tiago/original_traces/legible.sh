#!/bin/bash

COUNTER=1
while [ $COUNTER -lt 23 ]; do
	python legible_traces.py trace$COUNTER tiago
	let COUNTER=COUNTER+1
done


