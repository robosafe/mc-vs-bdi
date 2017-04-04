#!/usr/bin/env python

'''
Written by Dejanira Araiza Illan, January 2017
'''

import re

passed = 0
failed = 0
checked = []
result=[]
for ii in range(10,51):
	for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_mc/assertion1_'+str(ii)+'.txt','r')): 
		getdata = re.split("Assertion 1 at test",line)
		gettest = re.split("[:]",getdata[1]) #test at 0
		getporf = re.split("at global time",gettest[1])
		if len(checked)<1:
			if re.search('Passed',getporf[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]):
				failed=failed+1
				result.append(0)
			checked.append(int(gettest[0]))
		else:
			if re.search('Passed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				failed=failed+1
				result.append(0)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]==int(gettest[0]):
				if result[len(result)-1]==1:
					passed=passed-1
					failed=failed+1
					result[len(result)-1]=0
			if checked[len(checked)-1]!=int(gettest[0]):
				checked.append(int(gettest[0]))

print passed
print failed
print passed+failed
print len(checked)
print len(result)
print 2050 - len(checked)
print '----'

passed = 0
failed = 0
checked = []
result=[]
for ii in range(10,51):
	for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_mc/assertion2_'+str(ii)+'.txt','r')): 
		getdata = re.split("Assertion 1 at test",line)
		gettest = re.split("[:]",getdata[1]) #test at 0
		getporf = re.split("at global time",gettest[1])
		if len(checked)<1:
			if re.search('Passed',getporf[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]):
				failed=failed+1
				result.append(0)
			checked.append(int(gettest[0]))
		else:
			if re.search('Passed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				failed=failed+1
				result.append(0)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]==int(gettest[0]):
				if result[len(result)-1]==1:
					passed=passed-1
					failed=failed+1
					result[len(result)-1]=0
			if checked[len(checked)-1]!=int(gettest[0]):
				checked.append(int(gettest[0]))
print passed
print failed
print passed+failed
print len(checked)
print len(result)
print 2050-len(checked)
print '----'


passed = 0
failed = 0
checked = []
result=[]
for ii in range(10,51):
	for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_mc/assertion3_'+str(ii)+'.txt','r')): 
		getdata = re.split("Assertion 4 at test",line)
		gettest = re.split("[:]",getdata[1]) #test at 0
		getporf = re.split("at global time",gettest[1])
		if len(checked)<1:
			if re.search('Passed',getporf[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]):
				failed=failed+1
				result.append(0)
			checked.append(int(gettest[0]))
		else:
			if re.search('Passed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				failed=failed+1
				result.append(0)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]==int(gettest[0]):
				if result[len(result)-1]==1:
					passed=passed-1
					failed=failed+1
					result[len(result)-1]=0
			if checked[len(checked)-1]!=int(gettest[0]):
				checked.append(int(gettest[0]))
print passed
print failed
print passed+failed
print len(checked)
print len(result)
print 2050 - len(checked)
print '----'

passed = 0
failed = 0
checked = []
result=[]
for ii in range(10,51):
	for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_mc/assertion4_'+str(ii)+'.txt','r')):  
		getdata = re.split("Assertion 4 at test",line)
		gettest = re.split("[:]",getdata[1]) #test at 0
		getporf = re.split("at global time",gettest[1])
		if len(checked)<1:
			if re.search('Passed',getporf[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]):
				failed=failed+1
				result.append(0)
			checked.append(int(gettest[0]))
		else:
			if re.search('Passed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				passed=passed+1
				result.append(1)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
				failed=failed+1
				result.append(0)
			elif re.search('Failed',getporf[0]) and checked[len(checked)-1]==int(gettest[0]):
				if result[len(result)-1]==1:
					passed=passed-1
					failed=failed+1
					result[len(result)-1]=0
			if checked[len(checked)-1]!=int(gettest[0]):
				checked.append(int(gettest[0]))
print passed
print failed
print passed+failed
print len(checked)
print len(result)
print 2050 - len(checked)
print '----'

