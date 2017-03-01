#!/usr/bin/env python

import pexpect
import time
import re

# Tree of belief decisions to write into meta agent
choose_belief_1 = ["feed","clean"] #For max coverage
choose_belief_2 = ["clean","feed"] #For max coverage
choose_belief_3 = ["fridge", "sink"] #For X product coverage
choose_belief_4 = ["fridge", "sink","feed","clean","whatever"] #For X product coverage
choose_belief_5 = ["fridge", "sink","feed","clean","whatever"] #For X product coverage

# Try combinations in MAS
for i1,bel in enumerate(choose_belief_1):
	f = open('meta_orders.txt', 'w')
	f.write(bel+'\n')
	f.write(choose_belief_2[i1]+'\n')		
	f.close()
	child = pexpect.spawn('./tiago.jar')
	time.sleep(1)
	pexpect.signal.SIGINT
	f1 = open('output.txt', 'a')
	f1.write('------------\n')
	f1.close()
			
for i3 in choose_belief_3:
	for i4 in choose_belief_4:
		f = open('meta_orders.txt', 'w')
		f.write(i3+'\n')
		f.write(i4+'\n')
		f.close()
		child = pexpect.spawn('./tiago.jar')
		time.sleep(1)
		pexpect.signal.SIGINT
		f1 = open('output.txt', 'a')
		f1.write('------------\n')
		f1.close()
		
for i3 in choose_belief_3:
	for i4 in choose_belief_4:
		for i5 in choose_belief_5:
			f = open('meta_orders.txt', 'w')
			f.write(i3+'\n') 
			f.write(i4+'\n')
			f.write(i5+'\n')
			f.close()
			child = pexpect.spawn('./tiago.jar')
			time.sleep(1)
			pexpect.signal.SIGINT
			f1 = open('output.txt', 'a')
			f1.write('------------\n')
			f1.close()

#Separate tests in individual files
i = 1
for num,command in enumerate(open('output.txt','r')): 
	f = open('abstract_tests/abstract_test'+str(i)+'.txt', 'a')
	if re.search("-------",command):
		f.close()
		i = i+1
	else:
		f.write(command)
