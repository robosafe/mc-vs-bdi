#!/usr/bin/env python

'''
Written by Dejanira Araiza Illan, January 2016
'''

import re
import os

legcount=[]
badlegcount=[]
timeout2 = []
activations = []
boredoms = []
activations2 = []

for jj in range(10,51):
	for i in range(1,161):
		legs = 0
		badlegs = 0
		to2 = 0
		for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_table_bdi/seed'+str(jj)+'/robotout'+str(i),'r')): 
			if re.search("GPL is OK",line):	
				legs = legs + 1
			if re.search("GPL is not OK", line):
				badlegs = badlegs + 1
			if re.search('Timeout2',line) and not re.search('Discard',line):
				to2 = to2 + 1
		legcount.append(legs)
		badlegcount.append(badlegs)
		timeout2.append(to2)
	
		activ = 0
		bored = 0
		activ2 = 0
		for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_table_bdi/seed'+str(jj)+'/humanout'+str(i),'r')): 
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

print "Robot reports:"
print legcount
print badlegcount
print timeout2
print "Human reports:"
print activations
print boredoms
print activations2
print "---"
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

for i in range(1,6561):
	a1 = legcount.pop(0)
	a2 = badlegcount.pop(0)
	a3 = timeout2.pop(0)
	a4 = activations.pop(0)
	a5 = boredoms.pop(0)
	a6 = activations2.pop(0)
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
print "item 1: ", c1
print "item 2: ", c2
print "item 3: ", c3
print "item 4: ", c4
print "item 5: ", c5
print "item 6: ", c6
print "item 7: ", c7
print "item 8: ", c8
print "item 9: ", c9
print "item 10: ", c10
print "item 11: ", c11
print "item 12: ", c12
print "item 13: ", c13
print "item 14: ", c14
