#!/usr/bin/env python

'''
Written by Dejanira Araiza Illan, August 2016

Run from directory above /results (downloaded from the Github repository)
'''

import re
import os

idle=[]
fri=[]
sin=[]
hum = []
end = []
frid = []
sink = []
clean = []
feed = []
oth = []
for i in range(1,51):
	fridges = 0
	sinks = 0
	human = 0
	idl = 0
	finished = 0
	for num,line in enumerate(open(os.getcwd()+'/results/results_tiago/mc_logs/log_files/robot'+str(i),'r')): 
		if re.search('State machine starting in initial state',line) and re.search('Fridge',line):	
			fridges = fridges + 1
		if re.search('State machine starting in initial state',line) and re.search('Sink',line):	
			sinks = sinks + 1
		if re.search('State machine starting in initial state',line) and re.search('Human',line):
			human = human + 1
		if re.search('ended', line):
			finished = finished + 1
		if re.search('dle',line):
			idl = idl + 1
	fri.append(fridges)
	sin.append(sinks)
	hum.append(human)
	end.append(finished)
	idle.append(idl)
	
	hfri = 0
	hsink = 0
	hfeed = 0
	hclean = 0
	hother = 0
	for num,line in enumerate(open(os.getcwd()+'/results/results_tiago/mc_logs/log_files/human'+str(i),'r')): 
		if re.search("fridge",line):	
			hfri = hfri + 1
		elif re.search("sink", line):
			hsink = hsink + 1
		elif re.search("feed", line):
			hfeed = hfeed + 1
		elif re.search("clean", line):
			hclean = hclean + 1
		elif not re.search("Human started",line) and not re.search("ended",line) and not re.search("Wait",line):	
			print line
			hother = hother + 1
	frid.append(hfri)
	sink.append(hsink)
	clean.append(hclean)
	feed.append(hfeed)
	oth.append(hother)
	#print str(hfri) +' , '+ str(hsink) + ' , ' + str(hclean) + ' , '+ str(hfeed) +' , '+ str(hother) 

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
for i in range(1,51):
	a1 = frid.pop(0)
	a2 = sink.pop(0)
	a3 = clean.pop(0)
	a4 = feed.pop(0)
	a5 = oth.pop(0)
	a6 = fri.pop(0)
	a7 = sin.pop(0)
	a8 = hum.pop(0)
	a9 = end.pop(0)
	a10 = idle.pop(0)
	if (a4 >= 2 or a3 >= 2 or (a4>=1 and a3>=1)): #More than once
		c5 = c5 + 1
	elif a4 >= 1 and a6 >= 1: #Feed
		c1 = c1 + 1
	elif a3 >= 1 and a8 >= 1: #Clean
		c2 = c2 + 1
	elif a1 >= 1 and a6 >= 1: # Fridge
		c3 = c3 + 1
	elif a2 >= 1 and a7 >= 1: #Sink
		c4 = c4 + 1
	elif a5 >= 1: #Others
		c6 = c6 + 1
	else:
		print str(a1) + ' , '+ str(a2)+ ' , '+  str(a3)+ ' , '+  str(a4)+ ' , '+  str(a5)+ ' , '+  str(a6) + ' , '+  str(a7) + ' , '+  str(a8) + ' , '+  str(a9) + ' , '+  str(a10)
		
print c1
print c2
print c3
print c4
print c5
print c6
