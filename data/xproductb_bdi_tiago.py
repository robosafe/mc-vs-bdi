#!/usr/bin/env python

import re
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
for kk in range(10,51):
	for i in range(1,51):
		fridges = 0
		sinks = 0
		human = 0
		idl = 0
		finished = 0
		for num,line in enumerate(open('/home/da13683/temporary/data_diffseeds_tiago_bdi/seed'+str(kk)+'/robot'+str(i),'r')): 
			if re.search('State machine starting in initial state',line) and re.search('Fridge',line):	
				fridges = fridges + 1
			if re.search('State machine starting in initial state',line) and re.search('Sink',line):	
				sinks = sinks + 1
			if re.search('State machine starting in initial state',line) and re.search('Human',line):
				human = human + 1
			if re.search('ended', line):
				finished = finished + 1
			if re.search('idle',line):
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
		for num,line in enumerate(open('/home/da13683/temporary/data_diffseeds_tiago_bdi/seed'+str(kk)+'/human'+str(i),'r')): 
			if re.search("fridge",line):	
				hfri = hfri + 1
			elif re.search("sink", line):
				hsink = hsink + 1
			elif re.search("feed", line):
				hfeed = hfeed + 1
			elif re.search("clean", line):
				hclean = hclean + 1
			elif not re.search("Human started",line) and not re.search("ended",line) and not re.search("Wait",line):	
				hother = hother + 1
		frid.append(hfri)
		sink.append(hsink)
		clean.append(hclean)
		feed.append(hfeed)
		oth.append(hother)
		#print str(legs) +' , '+ str(badlegs) + ' , ' + str(to2) + ' ,,, '+ str(activ) +' , '+ str(bored) + ' , ' + str(activ2)

print "Robot counters -> motions"
print "Fridge: " , fri
print "Sink: " , sin
print "Human: " , hum
print "Finished tasks: " , end
print "Idle: " , idle
print "Human counters -> requests"
print "Fridge: " , frid
print "Sink: " , sink
print "Clean: " , clean
print "Feed: " , feed
print "Other requests: " , oth

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
print "Not in any cross-product items"
for i in range(1,len(frid)+1):
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
		
print "item 1 : " ,c1
print "item 2 : " ,c2
print "item 3 : " ,c3
print "item 4 : " ,c4
print "item 5 : " ,c5
print "item 5 : " ,c6
