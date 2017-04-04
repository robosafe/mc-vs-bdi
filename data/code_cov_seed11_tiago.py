#!/usr/bin/env python
'''
Written by Dejanira Araiza Illan, January 2017
'''

import matplotlib.pyplot as plt
import numpy as np
import re
from math import sqrt
import os

bdi_results1=[0]
pr_results1=[0]
mb_results1=[0]


for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_bdi/stats_11.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		bdi_results1.append(getdata[0])
max1 = max(bdi_results1)

		
for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_pr/stats_11.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		pr_results1.append(getdata[0])
max2 = max(pr_results1)


	
for num,line in enumerate(open(os.getcwd()+'/data_diffseeds_tiago_mc/stats_11.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		mb_results1.append(getdata[0])
max3 = max(mb_results1)

pr_results1a = sorted(pr_results1,key=int)
mb_results1a = sorted(mb_results1,key=int)
bdi_results1a = sorted(bdi_results1,key=int)

bdi_2=[0]
pr_2=[0]
mb_2=[0]
for i,item in enumerate(bdi_results1):
	if item > bdi_2[len(bdi_2)-1]:
		bdi_2.append(item)
	else:
		bdi_2.append(bdi_2[len(bdi_2)-1])

for i,item in enumerate(pr_results1):
	if item > pr_2[len(pr_2)-1]:
		pr_2.append(item)
	else:
		pr_2.append(pr_2[len(pr_2)-1])

for i,item in enumerate(mb_results1):
	if item > mb_2[len(mb_2)-1]:
		mb_2.append(item)
	else:
		mb_2.append(mb_2[len(mb_2)-1])

f, axarr = plt.subplots(2, sharex=True)

axarr[0].plot(bdi_results1a,'-b',label='BDI agents',lw=1.5)
axarr[0].plot(mb_results1a,'-r',label='Model checking timed automata.',lw=1.5)
axarr[0].plot(pr_results1a,'-g',label='Pseudorandom',lw=1.5)

axarr[0].axis([1, 50, 0, 105])
axarr[0].set_ylabel('Ordered code coverage (%)')

axarr[1].plot(bdi_2,'-b',label='BDI agents',lw=1.5)
axarr[1].plot(mb_2,'-r',label='Model checking timed automata.',lw=1.5)
axarr[1].plot(pr_2,'-g',label='Pseudorandom',lw=1.5)
axarr[1].axis([1, 50, 0, 105])
axarr[1].set_ylabel('Accumulated code coverage (%)')
axarr[1].set_xlabel('Test number')
axarr[1].legend(bbox_to_anchor=(0.97, 0.55), loc=1, borderaxespad=1.0,prop={'size':8})

plt.subplots_adjust(hspace=0.4)
plt.rcParams['pdf.fonttype'] = 42

plt.rcParams.update({'font.size': 13})
#plt.savefig('codecoverageb.pdf')
plt.savefig('codecoverageb2.eps')



