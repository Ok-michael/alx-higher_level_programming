#!/bin/bash

i=0
while [ $i -le 5 ]
do
	./1-last_digit.py
	sleep $i
	let "i++"
done
