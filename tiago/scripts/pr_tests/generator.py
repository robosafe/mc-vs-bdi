#!/usr/bin/env python
"""
This script generates programs for the human. An alphabet of code is needed.

n -- number of tests (e.g., n = 1 gives 1 test)

Written by Dejanira Araiza-Illan, August 2016. 
"""

import random
import sys

#Alphabet 
list_a = ['feed','clean','fridge','sink','chase','opendoor','recharge']


def main(n):
	for i in range (1,int(n)+1): 
		#Open files to write
		f = open('abstract_test'+str(i)+'.txt', 'w')
		random.seed(100+i)
		k = random.randint(1,3)
		for j in range(0,k):
			select = random.randint(0, len(list_a)-1)
			f.write(list_a[select]+'\n')
		f.close()

	
if __name__ == '__main__':
    main(sys.argv[1]) #Arguments: number of programs

