#!/usr/bin/env python

'''
Written by Dejanira Araiza Illan, August 2016

Run from directory above /results (downloaded from the Github repository)
'''

import re

passed = 0
failed = 0
checked = []
result=[]

for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/assertion1.txt','r')): 
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
print 160-passed-failed
print len(checked)
print len(result)
print '----'

passed = 0
failed = 0
checked = []
result=[]

for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/assertion2.txt','r')): 
	getdata = re.split("Assertion 2 at test",line)
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
print 160-passed-failed
print len(checked)
print len(result)
print '----'


passed = 0
failed = 0
checked = []
result=[]

for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/assertion3.txt','r')): 
	getdata = re.split("Assertion 3 at test",line)
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
print 160-passed-failed
print len(checked)
print len(result)
print '----'

passed = 0
failed = 0
checked = []
result=[]

for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/assertion4.txt','r')): 
	getdata = re.split("Assertion 4 at trace",line)
	gettest = re.split("[:]",getdata[1]) #test at 0
	getporf = re.split("at global time",gettest[1])
	if len(checked)<1:
		if re.search('True',getporf[0]):
			passed=passed+1
			result.append(1)
	else:
		if re.search('True',getporf[0]) and checked[len(checked)-1]!=int(gettest[0]):
			passed=passed+1
			result.append(1)
		if checked[len(checked)-1]!=int(gettest[0]):
			checked.append(int(gettest[0]))
print passed
print 160-passed
print len(checked)
print len(result)
print '----'


passed = 0
failed = 0
checked = []
result=[]

for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/assertion5.txt','r')): 
	getdata = re.split("Assertion 5 at test",line)
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
print 160-passed-failed
print len(checked)
print len(result)
print '----'


passed = 0
failed = 0
checked = []
result=[]

for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/assertion6.txt','r')): 
	getdata = re.split("Assertion 6 at test",line)
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
print 160-passed-failed
print len(checked)
print len(result)
print '----'
