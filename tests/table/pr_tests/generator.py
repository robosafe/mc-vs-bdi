#!/usr/bin/env python
"""
This script generates a number of abstract tests into files. An alphabet is needed, constrained. 

n -- number of tests (e.g., n = 1 gives 1 test)

Written by Dejanira Araiza-Illan, May 2015.
Modified Feb 2016. 
"""

import random
import sys

#Alphabet 
list_a = ['set_param location = 1', 'set_param location = 0', 'set_param pressure = 1', 'set_param pressure = 0', 'set_param gaze = 1', 'set_param gaze = 0', 'tell leg', 'tell humanReady', 'receivesignal', 'bored']


def main(n):
	for i in range (1,int(n)+1): #Number of tests required
		#Open files to write
		f = open('stimulus_'+str(i)+'.txt', 'w')
		random.seed(100+i)
		k = random.randint(5, 20)
		for j in range(1,k):
			select = random.randint(0, len(list_a)-1)
			f.write(list_a[select]+'\n')
		f.close()

	
if __name__ == '__main__':
    main(sys.argv[1]) #Arguments: number of abstract tests needed

