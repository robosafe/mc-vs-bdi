#!/usr/bin/env python
"""
Implements assertion 1: if 'flag1==1', wait then check 'flag1==0'

Written by Dejanira Araiza-Illan, August 2016
"""
import sys
import rospy
import smach
import smach_ros
import math
import random
import time
from std_msgs.msg import Int8

receivedflag1=0
receivedflag2=0
stats = open('assertion1.txt','a')
fileno = 0
thetime=0
globaltime = 0

class Flag1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
	global receivedflag1
	global thetime
	receivedflag1 = 0
	rospy.sleep(0.01)
	rospy.Subscriber('food', Int8, callback1)
	if receivedflag1 == 1:
		receivedflag1 = 0
		thetime = time.time()
		return 'outcome1'
        else:
		return 'outcome2'

class Flag2(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
	global receivedflag2
	global start
	global stats
	receivedflag2 = 0
	rospy.sleep(0.01)
	rospy.Subscriber("food", Int8, callback2)
	if receivedflag2 == 1:
		if (time.time()-thetime) < 300:
			stats.write('Assertion 1 at test '+ str(fileno) +': Passed at global time '+ str(time.time()-globaltime) +'\n')
			receivedflag2 = 0
			return 'outcome1'
	else:
		if (time.time()-thetime) > 300:
			stats.write('Assertion 1 at test '+ str(fileno) +': Failed at global time '+ str(time.time()-globaltime) +'\n')
			receivedflag2 = 0
			return 'outcome1'
        	else:
			return 'outcome2'

def callback1(data):
	global receivedflag1
	if data.data==1:
		receivedflag1 = 1
	else:
		receivedflag1 = 0
	

def callback2(data):
	global receivedflag2
	if data.data==0:
		receivedflag2 = 1
	else:
		receivedflag2 = 0

def main(number):
	rospy.init_node('assertion1', anonymous=True) #Start node first
	global globaltime
	globaltime=time.time()
	global fileno
	fileno = number
	# Create a SMACH state machine
    	sm = smach.StateMachine(outcomes=['Done'])

   	 # Open the container
   	with sm:
		#Receive signal
		smach.StateMachine.add('Flag1', Flag1(), 
                transitions={'outcome1':'Flag2','outcome2':'Flag1'})

		#Receive signal
		smach.StateMachine.add('Flag2', Flag2(),
		transitions={'outcome1':'Flag1','outcome2':'Flag2'})		


	# Execute SMACH plan
    	outcome = sm.execute()

if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except	rospy.ROSInterruptException:
		pass
