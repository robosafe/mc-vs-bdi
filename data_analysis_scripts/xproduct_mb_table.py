#!/usr/bin/env python

'''
Written by Dejanira Araiza Illan, August 2016

Run from directory above /results (downloaded from the Github repository)
'''

import re
import os

legcount=[]
badlegcount=[]
timeout2 = []
activations = []
boredoms = []
activations2 = []
for i in range(1,161):
	legs = 0
	badlegs = 0
	to2 = 0
	for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/log_files/robotout'+str(i),'r')): 
		if re.search('GPL is OK',line):	
			legs = legs + 1
			#print line, i
		if re.search('GPL is not OK', line):
			badlegs = badlegs + 1
		if re.search('Timeout2',line) and not re.search('Discard',line):
			to2 = to2 + 1
	#print legs
	legcount.append(legs)
	badlegcount.append(badlegs)
	timeout2.append(to2)
	
	activ = 0
	bored = 0
	activ2 = 0
	for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/log_files/humanout'+str(i),'r')): 
		if re.search('State machine transitioning \'SendA1',line):	
			activ = activ + 1
			#print line
		if re.search('Bored', line):
			bored = bored + 1
		if re.search('State machine transitioning \'SendA2',line):	
			activ2 = activ2 + 1
	activations.append(activ)
	boredoms.append(bored)
	activations2.append(activ2)
	#print str(legs) +' , '+ str(badlegs) + ' , ' + str(to2) + ' ,,, '+ str(activ) +' , '+ str(bored) + ' , ' + str(activ2)

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0

for i in range(1,161):
	a1 = legcount.pop(0)
	a2 = badlegcount.pop(0)
	a3 = timeout2.pop(0)
	a4 = activations.pop(0)
	a5 = boredoms.pop(0)
	a6 = activations2.pop(0)
	#print a1, a4
	if a4 == 0: #0 legs, timeout
		c14 = c14 + 1
	if a4 >= 1 and a5 >= 1 and a1 == 0 and a2 == 0: # 1 to 4 legs, timeout1 or 2
		c13 = c13 + 1
	if a4 >= 1 and a5 ==0 and a1 == 0 and a2 == 0: # 1 to 4 legs, timeout1
		c13 = c13 + 1
	if a4 == 1 and a5 == 1: 
		if a3 == 1: #1 leg 1 boredom, 1 timeout2
			c12 = c12 + 1
		else: #Timeout1
			c12 = c12 + 1
	if a4 == 1 and a2 == 1: # 1 leg, 1 bad
		c11 = c11 + 1
	if a4 == 1 and a1 == 1: # 1 leg, 1 good
		c10 = c10 + 1
	if a4 == 2 and a5 >= 1:
		if a3 >= 1: #2 legs 1 boredom, 1 timeout2
			c9 = c9 + 1
		else:#Timeout1
			c10 = c10 + 1
	if a4 == 2 and a2 >= 1: # 2 legs, 1 bad
		c8 = c8 + 1
	if a4 == 2 and a1 >= 1: # 2 legs, 1 good
		c7 = c7 + 1
	if a4 == 3 and a5 >= 1:
		if a3>=1:#3 legs 1 boredom, 1 timeout2
			c6 = c6 + 1
		else: #Timeout1
			c6 = c6 + 1 
	if a4 == 3 and a2 >= 1: # 3 legs, 1 bad
		c5 = c5 + 1
	if a4 == 3 and a1 >= 1: # 3 legs, 1 good
		c4 = c4 + 1
	if a4 >= 4 and a5 >=1:
		if a3 >= 1: # 4 legs 1 boredom, 1 timeout2
			c3 = c3 + 1
		else: #Timeout1
			c3 = c3 + 1
	if a4 >= 4 and a2 >=1: # 4 legs, 1 bad
		c2 = c2 + 1
	if a4 >= 4 and a1 >=1: #4 legs, 1 good
		c1 = c1 + 1
print c1
print c2
print c3
print c4
print c5
print c6
print c7
print c8
print c9
print c10
print c11
print c12
print c13
print c14
