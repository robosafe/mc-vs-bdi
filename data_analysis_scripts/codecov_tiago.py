'''
Written by Dejanira Araiza Illan, August 2016

Run in directory above /results (downloaded from the Github repository)
'''

import matplotlib.pyplot as plt2
import numpy as np
import re


bdi_results2=[0]
pr_results2=[0]
mb_results2=[0]


for num,line in enumerate(open(os.getcwd()+'/results/results_tiago/bdi_logs/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		bdi_results2.append(getdata[0])
max4 = max(bdi_results2)
		
for num,line in enumerate(open(os.getcwd()+'/results/results_tiago/pr_logs/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		pr_results2.append(getdata[0])
max5 = max(pr_results2)
	
for num,line in enumerate(open(os.getcwd()+'/results/results_tiago/mc_logs/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		mb_results2.append(getdata[0])
max6 = max(mb_results2)

plt2.plot(pr_results2,'-b',label='Pseudorandom',lw=1.5)
plt2.plot(bdi_results2,'-r',label='PTA model checking',lw=1.5)
plt2.plot(mb_results2,'-g',label='BDI agents',lw=1.5)

maxt2=max(max4,max5,max6)
themax2=[]
for i in range(0,51):
	themax2.append(maxt2)
plt2.plot(themax2,'-k',label='Max coverage [%] per test',lw=1.5)


plt2.axis([1, 50, 0, 105])
plt2.ylabel('Code coverage (%)')
plt2.xlabel('Test number')
plt2.rcParams.update({'font.size': 14})
plt2.legend(bbox_to_anchor=(0.97, 0.27), loc=1, borderaxespad=0.,prop={'size':14})
plt2.savefig('codecoverageb.pdf')


