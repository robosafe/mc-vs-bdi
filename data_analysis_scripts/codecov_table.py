'''
Written by Dejanira Araiza Illan, August 2016

Run in directory above /results (downloaded from the Github repository)
'''
import matplotlib.pyplot as plt
import numpy as np
import re
import os

bdi_results1=[0]
pr_results1=[0]
mb_results1=[0]


for num,line in enumerate(open(os.getcwd()+'/results/results_table/bdi_logs/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		bdi_results1.append(getdata[0])
max1 = max(bdi_results1)
		
for num,line in enumerate(open(os.getcwd()+'/results/results_table/pr_logs/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		pr_results1.append(getdata[0])
max2 = max(pr_results1)
	
for num,line in enumerate(open(os.getcwd()+'/results/results_table/mc_logs/stats.txt','r')): 
	if re.search("Covered percentage",line):
		getdata = re.split("Covered percentage[:]",line)
		getdata = re.split("[%]",getdata[1])
		mb_results1.append(getdata[0])
max3 = max(mb_results1)

plt.plot(pr_results1,'-b',label='Pseudorandom',lw=1.5)
plt.plot(bdi_results1,'-r',label='PTA model checking',lw=1.5)
plt.plot(mb_results1,'-g',label='BDI agents',lw=1.5)

maxt=max(max1,max2,max3)
themax=[]
for i in range(0,161):
	themax.append(maxt)
plt.plot(themax,'-k',label='Max coverage [%] per test',lw=1.5)


plt.axis([1, 160, 0, 105])
plt.ylabel('Code coverage (%)')
plt.xlabel('Test number')
plt.rcParams.update({'font.size': 14})
plt.legend(bbox_to_anchor=(0.97, 0.27), loc=1, borderaxespad=0.,prop={'size':14})
plt.savefig('codecoveragea.pdf')


