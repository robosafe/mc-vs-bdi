#!/usr/bin/env python
# This script translates and separates the traces computed with UPPAAL model checking and the tracer tool (libutap). The traces are originally in a *.xtr file format. The specified automata transitions are separated from the global traces (the human, the setting of gaze, pressure and location), and transformed into a *.txt file with a list of high-level commands for the human machine in the simulator (sending signals, waiting for signals, setting parameters).
# Written by Dejanira Araiza-Illan, March 2015
# Modified for the table scenario, July 2016
import rospy
import re
import os
import sys

variables_keep = ['sink','fridge','feed','clean','whatever']

def extract(nameFile):

# -------------- PARSING OF THE MODEL INTO USEFUL STRUCTURES
	 	#automata = raw_input("Name of the automata with commas and no spaces (e.g. aut1,aut2,aut3):")
		automaton = 'human'
		#automata = 'Human,Gaze,Pressure,Location'
		#automaton = re.split(",",automata)

		type_of_trace=0
		transitions=[]
		states=[]
		traces=[]
		delays=[]
		numberfile=re.split('\D+',nameFile)
	#	print numberfile
		for i, line in enumerate(open(nameFile+ '.tr', 'r')): 
			for match in re.finditer("Initial state",line): #If from legible_traces.py
				type_of_trace=1
			for match in re.finditer("Trace",line): #Separate multiple traces
				traces.append(i)
			for match in re.finditer("Transitions:", line):
				transitions.append(i)
			for match in re.finditer("State:", line):
				states.append(i)
			for match in re.finditer("Delay:", line):
				delays.append(i)
		#Eliminate states and keep transitions
	#	print type_of_trace
#		print traces
#		print transitions
#		print states
#		print delays
	
		f=open('stimulus_'+numberfile[1]+'.txt', 'w')
		trans_content=[]
		for i in range(0,len(transitions)):
			for j, line in enumerate(open(nameFile+ '.tr', 'r')):
				if j>transitions[i] and j<(states[i]):
					if line!='\n':
						trans_content.append(line)
#		print trans_content
		#Eliminate unimportant transitions
		important=[]
		for i, line in enumerate(trans_content):
			for j, aut in enumerate(automaton):
				if aut != ',':
					if re.match(aut+'.', line)!=None:	
						important.append(line)
#		print important
		#Check each transition and determine if human: sends signal, receives signal, sets variables
		global variables_keep
		for i,trans in enumerate(important):
			var_split = re.split('; ',trans)
			#print var_split
			if var_split[1] != '0': #Signals
				for match in re.finditer('!',var_split[1]):
					signal = re.split('!',var_split[1])
					for kk,variable in enumerate(variables_keep):
						if re.search('\\b'+signal[0]+'\\b',variable):
							#Write send signal 
							f.write('tell '+signal[0]+'\n')
				for match in re.finditer('\?',var_split[1]):
				#Write receive signal
					for kk,variable in enumerate(variables_keep):
						if re.search('\\b'+signal[0]+'\\b',variable):
							signal = re.split('\?',var_split[1])
							f.write('receivesignal\n')
		
			if var_split[2] != '0}\n': #Variables
				commas = re.split(',',var_split[2])
				#print commas
				for j,part in enumerate(commas):
					if commas!='':
						new_string = corrected(part)
						#print new_string
						for kk,variable in enumerate(variables_keep):
							if re.search(variable,new_string):
								f.write(new_string+'\n')
			

def corrected(expr):
	expr_new=''
	modif1 = re.split("\:=",expr)
#	print modif1[0]
	global variables_keep
	for kk,variable in enumerate(variables_keep):
		if re.search('\\b'+modif1[0]+'\\b',variable):
			if re.search('fridge',modif1[0]) and re.search('true',modif1[1]):
				expr_new='fridge'
			elif re.search('sink',modif1[0]) and re.search('true',modif1[1]):
				expr_new='sink'
			elif re.search('clean',modif1[0]) and re.search('true',modif1[1]):
				expr_new='clean'
			elif re.search('feed',modif1[0]) and re.search('true',modif1[1]):
				expr_new='feed'
			elif re.search('whatever',modif1[0]) and re.search('true',modif1[1]):
				expr_new='whatever'
			else:
				expr_new=''
#	print expr_new
	return expr_new
	
	
def corrected2(expr):
	expr_new=''
	modif1 = re.split(" \:= ",expr)
	expr_new=expr_new+modif1[0]+'='
    	if re.match(modif1[0],modif1[1]):
    		modif2 = re.split('\s*[+]|[-]\s*',modif1[1])
    		modif3 = re.split('\s*[}]\n',modif2[1])
    		expr_new=expr_new+modif3[0]
	elif re.match('rand_v',modif1[1]):
		expr_new = ''
	else:
		modif4 = re.split(' }\n',modif1[1])
		expr_new=expr_new+modif4[0]
#	print expr_new
	return expr_new


if __name__ == "__main__":
	if len(sys.argv) == 2: #arguments passed by command line: program, trace file 
		extract(sys.argv[1])
	else:
		print 'extract.py [trace file or .tr]'
		sys.exit(1)

