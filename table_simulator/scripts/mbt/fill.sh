#!/bin/bash

COUNTER=1
MCOUNT=92
while [ $COUNTER -lt 92 ]; do
	cp ~/uppaal-4.0.14/cover/table/mbt/stimulus_$COUNTER.txt ./stimulus_$MCOUNT.txt
	let COUNTER=COUNTER+1
	let MCOUNT=MCOUNT+1

done


