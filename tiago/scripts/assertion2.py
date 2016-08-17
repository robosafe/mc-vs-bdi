#!/usr/bin/env python
"""
Implements assertion 1: if 'flag1==1', wait then check Gazebo location

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
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

receivedflag1=0
stats = open('assertion2.txt','a')
fileno = 0
globaltime = 0

class Flag1(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])

    def execute(self, userdata):
	global receivedflag1
	global thetime
	receivedflag1 = 0
	rospy.sleep(0.01)
	rospy.Subscriber('idle', Int8, callback1)
	if receivedflag1 == 1:
		receivedflag1 = 0
		rospy.sleep(40)
		return 'outcome1'
        else:
		return 'outcome2'

class Check(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])

    def execute(self, userdata):
    	global globaltime
	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	if abs(data.pose.position.x - 1.35) < 0.15 and abs(data.pose.position.y - 0.015) < 0.15:
		stats.write('Assertion 1 at test '+ str(fileno) +': Passed at global time '+ str(time.time()-globaltime) +'\n')
		
	else:
		stats.write('Assertion 1 at test '+ str(fileno) +': Failed at global time '+ str(time.time()-globaltime) +'\n')
	return 'outcome1'

def callback1(data):
	global receivedflag1
	if data.data==1:
		receivedflag1 = 1
	else:
		receivedflag1 = 0


def main(number):
	rospy.init_node('assertion2', anonymous=True) #Start node first
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
		smach.StateMachine.add('Flag2', Check(),
		transitions={'outcome1':'Flag1'})		


	# Execute SMACH plan
    	outcome = sm.execute()

if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except	rospy.ROSInterruptException:
		pass
