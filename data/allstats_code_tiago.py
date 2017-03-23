import matplotlib.pyplot as plt
import numpy as np
import re
from math import sqrt

bdi_results1=[]
pr_results1=[]
mb_results1=[]
max_bdi1 = [] # Max coverage for all individual seeds
lmeans_bdi1 = [] #Means for all individual seeds
max_pr1 = []
lmeans_pr1 = []
max_mb1 = []
lmeans_mb1 = []
varieties_bdi1 = []
varieties_pr1 = []
varieties_mb1 = []
for jj in range(10,51):
	temp_bdi=[]
	temp_var_bdi=[]
	for num,line in enumerate(open('/home/da13683/temporary/data_diffseeds_tiago_bdi/stats_'+str(jj)+'.txt','r')): 
		if re.search("Covered percentage",line):
			getdata = re.split("Covered percentage[:]",line)
			getdata = re.split("[%]",getdata[1])
			bdi_results1.append(float(getdata[0]))
			temp_bdi.append(float(getdata[0]))
			if not (float(getdata[0]) in temp_var_bdi):
				temp_var_bdi.append(float(getdata[0]))
	max1 = max(temp_bdi)
	lmeans_bdi1.append(np.mean(temp_bdi))
	max_bdi1.append(max1)
	varieties_bdi1.append(len(temp_var_bdi))
	temp_pr=[]
	temp_var_pr=[]
	for num,line in enumerate(open('/home/da13683/temporary/data_diffseeds_tiago_pr/stats_'+str(jj)+'.txt','r')): 
		if re.search("Covered percentage",line):
			getdata = re.split("Covered percentage[:]",line)
			getdata = re.split("[%]",getdata[1])
			pr_results1.append(float(getdata[0]))
			temp_pr.append(float(getdata[0]))
			if not (float(getdata[0]) in temp_var_pr):
				temp_var_pr.append(float(getdata[0]))
	max2 = max(temp_pr)
	lmeans_pr1.append(np.mean(temp_pr))
	max_pr1.append(max2)
	varieties_pr1.append(len(temp_var_pr))
	temp_mb=[]
	temp_var_mb=[]
	for num,line in enumerate(open('/home/da13683/temporary/data_diffseeds_tiago_mc/stats_'+str(jj)+'.txt','r')): 
		if re.search("Covered percentage",line):
			getdata = re.split("Covered percentage[:]",line)
			getdata = re.split("[%]",getdata[1])
			mb_results1.append(float(getdata[0]))
			temp_mb.append(float(getdata[0]))
			if not (float(getdata[0]) in temp_var_mb):
				temp_var_mb.append(float(getdata[0]))
	max3 = max(temp_mb)
	lmeans_mb1.append(np.mean(temp_mb))
	max_mb1.append(max3)
	varieties_mb1.append(len(temp_var_mb))
mean_bdi1 = np.mean(bdi_results1)
mean_pr1 = np.mean(pr_results1)
mean_mb1 = np.mean(mb_results1)
print mean_bdi1, mean_pr1, mean_mb1
print '--- the averages'
print lmeans_bdi1
print lmeans_mb1
print lmeans_pr1
bdi=0
mc=0
pr=0
for num,item in enumerate(lmeans_bdi1):
	#print num
	if item > lmeans_mb1[num] and item > lmeans_pr1[num]:
		bdi= bdi+1
	elif lmeans_mb1[num] > item and lmeans_mb1[num] > lmeans_pr1[num]:
		mc=mc+1
	elif lmeans_pr1[num] > item and lmeans_pr1[num] > lmeans_mb1[num]:
		pr=pr+1
print bdi, mc, pr
print '--- the maxs'
print max_bdi1
print max_mb1
print max_pr1
#BDI max vs MC max
allbdi=0
allmc=0
allpr=0
for num,item in enumerate(max_bdi1):
	#print num
	if item > max_mb1[num] and item > max_pr1[num]:
		allbdi= allbdi+1
	elif max_mb1[num] > item and max_mb1[num] > max_pr1[num]:
		allmc=allmc+1
	elif max_pr1[num] > item and max_pr1[num] > max_mb1[num]:
		allpr=allpr+1
print allbdi, allmc, allpr
print '--- the varieties'
print varieties_bdi1
print varieties_mb1
print varieties_pr1
#BDI var vs MC var
allbdi_var=0
allmc_var=0
allpr_var=0
for num,item in enumerate(varieties_bdi1):
	#print num
	if item > varieties_mb1[num] and item > varieties_pr1[num]:
		allbdi_var= allbdi_var+1
	elif varieties_mb1[num] > item and varieties_mb1[num] > varieties_pr1[num]:
		allmc_var=allmc_var+1
	elif varieties_pr1[num] > item and varieties_pr1[num] > varieties_mb1[num]:
		allpr_var=allpr_var+1
print allbdi_var,allmc_var, allpr_var



fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

x1 = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
x2 = [x-0.2 for x in x1]
x3 = [x+0.2 for x in x1]
ax1.bar(x2, lmeans_bdi1,width=0.2,color='b',align='center',label='BDI agents')
ax1.bar(x1, lmeans_mb1,width=0.2,color='r',align='center',label='Model checking timed automata')
ax1.bar(x3, lmeans_pr1,width=0.2,color='g',align='center',label='Pseudorandom')
ax2.plot(x2, max_bdi1,color='b')
ax2.plot(x1, max_mb1,color='r')
ax2.plot(x3, max_pr1,color='g')
ax1.axis([9, 51, 0, 105])
ax2.axis([9, 51, 0, 105])
ax1.legend(bbox_to_anchor=(0.97, 0.2), loc=1, borderaxespad=1.0,prop={'size':8})
ax1.set_ylabel('Average code coverage [bars] (%)')
ax2.set_ylabel('Maximum code coverage by any test [lines] (%)')
ax1.set_xlabel('Seed')
plt.rcParams.update({'font.size': 10})
plt.savefig('allstatsb.pdf')
plt.savefig('allstatsb.eps')

x1 = range(1,2051)
doublemean_bdi = 0.0
doublemean_mc = 0.0
doublemean_pr = 0.0
mean_bdi = []
mean_mc = []
mean_pr = []
for jj in range(0,2050):
	doublemean_bdi= doublemean_bdi + bdi_results1[jj]
	doublemean_mc = doublemean_mc + mb_results1[jj]
	doublemean_pr = doublemean_pr + pr_results1[jj]
	mean_bdi.append(doublemean_bdi/(jj+1.0))
	mean_mc.append(doublemean_mc/(jj+1.0))
	mean_pr.append(doublemean_pr/(jj+1.0))

plt.plot(x1,mean_bdi,color='b',label='BDI agents')
plt.plot(x1,mean_mc,color='r',label='Model checking timed automata')
plt.plot(x1,mean_pr,color='g',label='Pseudorandom')
plt.legend(bbox_to_anchor=(0.97, 0.2), loc=1, borderaxespad=1.0,prop={'size':8})
plt.ylabel('Average code coverage (%)')
plt.xlabel('Tests')
plt.axis([0, 2050, 0, 105])
plt.savefig('convergenceb.eps')
