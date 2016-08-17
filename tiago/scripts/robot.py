#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan July-August 2016
"""

import sys
import os
import rospy
import actionlib
import smach
import smach_ros
import math
import time
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from std_msgs.msg import Int8
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

client = actionlib.SimpleActionClient("/play_motion", PlayMotionAction)
order='none'
stop = 0

## MOTIONS ##

def moveuntilreached(x,y):
	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	phi = math.atan2(2*(data.pose.orientation.w*data.pose.orientation.z + data.pose.orientation.x*data.pose.orientation.y), 1 - 2*(math.pow(data.pose.orientation.y,2)+math.pow(data.pose.orientation.z,2)))
	while abs(y - data.pose.position.y) > 0.02 and abs(x - data.pose.position.x) > 0.1:
		#Correct angle
		while abs(math.atan2(y - data.pose.position.y,x - data.pose.position.x) - phi) > 0.1 : 
			if math.atan2(y - data.pose.position.y,x - data.pose.position.x)  > 0 and phi > 0:
				if math.atan2(y - data.pose.position.y,x - data.pose.position.x) > phi:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.25)
				else: 
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
					rospy.sleep(0.25)
			elif math.atan2(y - data.pose.position.y,x - data.pose.position.x) < 0 and phi < 0:
				if abs(math.atan2(y - data.pose.position.y,x - data.pose.position.x)) > abs(phi):
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
					rospy.sleep(0.25)
				else:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.25)
			elif math.atan2(y - data.pose.position.y,x - data.pose.position.x) > 0 and phi < 0:
				if abs(math.atan2(y - data.pose.position.y,x - data.pose.position.x)) > 1.5 and abs(phi) > 1.5:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
					rospy.sleep(0.25)
				elif abs(math.atan2(y - data.pose.position.y,x - data.pose.position.x)) < 1.5 and abs(phi) < 1.5:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.25)
				else:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.25)
			else:
				if abs(math.atan2(y - data.pose.position.y,x - data.pose.position.x)) > 1.5 and abs(phi) > 1.5:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.25)
				elif abs(math.atan2(y - data.pose.position.y,x - data.pose.position.x)) < 1.5 and abs(phi) < 1.5:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
					rospy.sleep(0.25)
				else:
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.25)
			getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
			data = getmodel('tiago_steel','')
			phi = math.atan2(2*(data.pose.orientation.w*data.pose.orientation.z + data.pose.orientation.x*data.pose.orientation.y), 1 - 2*(math.pow(data.pose.orientation.y,2)+math.pow(data.pose.orientation.z,2)))
		#Then advance for a bit
		for i in range(0,1):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.1)
		#Check for collisions
		rospy.Subscriber("collision_sensor", Int8, stopnow) 
		while stop != 0:
			rospy.Subscriber("collision_sensor", Int8, stopnow) 
			rospy.sleep(0.1)
		#Recheck if angle is not good anymore and fix
		getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		data = getmodel('tiago_steel','')
	

def stopnow(data):
	global stop
	if data.data == 1:
		stop = 1
	else:
		stop = 0


##---------------------------------
class Recharge(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	#If in human
	if abs(data.pose.position.x + 2.4) < 0.15 and abs(data.pose.position.y + 3.95) < 0.15:
		#Move to centre of room
		moveuntilreached(-0.25,-0.5)
		#Continue to recharge
		moveuntilreached(1.35,0.015)
	else:
		moveuntilreached(1.35,0.015)
        return 'outcome1'

##----------------------------------
class Cooker(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
        return 'outcome1'

## ---------------------------------
class Fridge(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	phi = math.atan2(2*(data.pose.orientation.w*data.pose.orientation.z + data.pose.orientation.x*data.pose.orientation.y), 1 - 2*(math.pow(data.pose.orientation.y,2)+math.pow(data.pose.orientation.z,2)))
	#If in human
	if abs(data.pose.position.x + 2.4) < 0.15 and abs(data.pose.position.y + 3.95) < 0.15:
		#Move to centre of room
		moveuntilreached(-0.25,-0.5)
		#Continue towards fridge
		moveuntilreached(-2.8,0.405)
	else:	
		moveuntilreached(-2.8,0.405)
        return 'outcome1'

## -----------------------------
class Sink(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	phi = math.atan2(2*(data.pose.orientation.w*data.pose.orientation.z + data.pose.orientation.x*data.pose.orientation.y), 1 - 2*(math.pow(data.pose.orientation.y,2)+math.pow(data.pose.orientation.z,2)))
	#If in human
	if abs(data.pose.position.x + 2.4) < 0.15 and abs(data.pose.position.y + 3.95) < 0.15:
		#Move to centre of room
		moveuntilreached(-0.25,-0.5)
		#Continue towards sink	
		moveuntilreached(-2.03,3.055)
	else:
		moveuntilreached(-2.03,3.055)
	pubfood = rospy.Publisher('food', Int8, queue_size=1,latch=True)
  	pubfood.publish(0)
  	rospy.sleep(0.1)
        return 'outcome1'

## ------------------------------------
class Human(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	phi = math.atan2(2*(data.pose.orientation.w*data.pose.orientation.z + data.pose.orientation.x*data.pose.orientation.y), 1 - 2*(math.pow(data.pose.orientation.y,2)+math.pow(data.pose.orientation.z,2)))
	#Move to centre first
	moveuntilreached(-0.25,-0.5)
	#Approach table now
	moveuntilreached(-2.4,-3.95)
	pubfood = rospy.Publisher('food', Int8, queue_size=1,latch=True)
  	pubfood.publish(0)
  	rospy.sleep(0.1)
        return 'outcome1'

## -------------------------------
class Grab(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	
    	goal = PlayMotionGoal()
	goal.motion_name = 'close_hand'
  	goal.skip_planning = True
  	global client
  	client.send_goal(goal)
  	client.wait_for_result(rospy.Duration(3.0))
  	rospy.loginfo("grabbed")
  	pubfood = rospy.Publisher('food', Int8, queue_size=1,latch=True)
  	pubfood.publish(1)
  	rospy.sleep(0.1)
	return 'outcome1'

## -------------------------------------
class Drop(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	goal = PlayMotionGoal()
	goal.motion_name = 'open_hand'
  	goal.skip_planning = True
  	global client
  	client.send_goal(goal)
  	client.wait_for_result(rospy.Duration(3.0))
  	rospy.loginfo("dropped")
	return 'outcome1'



## -----------------------------------
class Tuck(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	goal = PlayMotionGoal()
	goal.motion_name = 'home'
  	goal.skip_planning = True
  	global client
  	client.send_goal(goal)
  	client.wait_for_result(rospy.Duration(10.0))
  	rospy.loginfo("Arm tucked.")
	return 'outcome1'

## MAIN ##	
def getgoal(data):
	global order
	order = data.data
	print order


def main():
	rospy.init_node('robot_navigation', anonymous=True) #Start node first
	rospy.loginfo("Waiting for motion servers...")
	#Variables
	global client
	global order
	
	#Start connections
  	client.wait_for_server()
  	rospy.loginfo("...connected.")
	rospy.wait_for_message("/joint_states", JointState)
  	rospy.sleep(3)
  	rospy.loginfo("Robot is ready")
  	thetimestart = 1000000000000000
  	
  	#Listen to human and send orders to low level navigation control
  	while not rospy.is_shutdown():
	  	rospy.Subscriber('orders',String,getgoal) 
	  	rospy.sleep(0.1)
	  	rospy.loginfo(order)
	  	if order == 'feed':
	  		sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to fridge
				smach.StateMachine.add('Fridge', Fridge(), transitions={'outcome1':'Grabfood'})
				#Grab food from fridge
				smach.StateMachine.add('Grabfood', Grab(), transitions={'outcome1':'Human'})
				#Take it to person
				smach.StateMachine.add('Human', Human(), transitions={'outcome1':'Recharge'})
				#Go to recharge
				smach.StateMachine.add('Recharge', Recharge(), transitions={'outcome1':'nextOrder'})
	  		outcome = sm.execute()
	  		pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
	  		pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			thetimestart = time.time()
	  	elif order == 'clean':
	  		sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
	  			#Move to person
				smach.StateMachine.add('Human', Human(), transitions={'outcome1':'Grabfood'})
				#Grab food from table
				smach.StateMachine.add('Grabfood', Grab(), transitions={'outcome1':'Sink'})
				#Move to sink
				smach.StateMachine.add('Sink', Sink(), transitions={'outcome1':'Dropfood'})
				#Drop into sink
				smach.StateMachine.add('Dropfood', Drop(), transitions={'outcome1':'Recharge'})
				#Go to recharge
				smach.StateMachine.add('Recharge', Recharge(), transitions={'outcome1':'nextOrder'})
	  		outcome = sm.execute()	
	  		pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
	  		pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			thetimestart = time.time()
		elif order == 'fridge':
			sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to fridge
				smach.StateMachine.add('Fridge', Fridge(), transitions={'outcome1':'Recharge'})
				#Go to recharge
				smach.StateMachine.add('Recharge', Recharge(), transitions={'outcome1':'nextOrder'})
			outcome = sm.execute()	
	  		pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
	  		pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			thetimestart = time.time()
		elif order == 'sink':
			sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to sink
				smach.StateMachine.add('Sink', Sink(), transitions={'outcome1':'Recharge'})
				#Go to recharge
				smach.StateMachine.add('Recharge', Recharge(), transitions={'outcome1':'nextOrder'})
			outcome = sm.execute()	
	  		pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
	  		pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			thetimestart = time.time()
		elif order == 'ended':
			rospy.loginfo('ended')
			break
		else:
			rospy.loginfo('I cannot do this')
		#Check if idle for a time, then send to recharge
		if time.time()-thetimestart > 30:
			order = 'recharge'
			pubdone = rospy.Publisher('idle', Int8, queue_size=1,latch=True)
	  		pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			rospy.loginfo('idle')
			sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Go to recharge
				smach.StateMachine.add('Recharge', Recharge(), transitions={'outcome1':'nextOrder'})
			outcome = sm.execute()	
			pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
	  		pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			thetimestart = time.time()
			

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
        	
