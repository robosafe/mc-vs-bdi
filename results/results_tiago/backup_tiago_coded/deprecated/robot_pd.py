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
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	# If in fridge
	if abs(data.pose.position.x + 2.8) < 0.1 and abs(data.pose.position.y - 0.405) < 0.1:
		for i in range(0,44):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2) #0.25 update in control, velocity can be varied to control motion. 
		for i in range(0,2):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.1)
		for i in range(0,1800):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		for i in range(0,40):
  			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		rospy.loginfo('In recharge')
	#If in sink
	elif abs(data.pose.position.x + 2.03) < 0.1 and abs(data.pose.position.y - 3.05) < 0.1:
		for i in range(0,60):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,1870):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		for i in range(0,44):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
			rospy.sleep(0.2)
		rospy.loginfo('In recharge')
	#If in human
	elif abs(data.pose.position.x + 2.43) < 0.1 and abs(data.pose.position.y + 4.02) < 0.1:
		for i in range(0,70):
			pub.publish(Vector3(-0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
		for i in range(0,60):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,1750):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		for i in range(0,25):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
			rospy.sleep(0.2)
		for i in range(0,910):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			if i > 200:
				while stop != 0:
					rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
					rospy.sleep(0.1)
		for i in range(0,40):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		rospy.loginfo('In recharge')
	else:
		rospy.loginfo('Cannot go there')
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
	#If in recharge
	if abs(data.pose.position.x - 1.35) < 0.1 and abs(data.pose.position.y - 0.015) < 0.1:
		for i in range(0,5):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,1720):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
			if i > 200:
				while stop != 0:
					rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
					rospy.sleep(0.1)
		rospy.loginfo('In the fridge')
	#If in human
	elif abs(data.pose.position.x + 2.5) < 0.15 and abs(data.pose.position.y + 3.95) < 0.15:
		for i in range(0,70):
			pub.publish(Vector3(-0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
		for i in range(0,63):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,1750):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		for i in range(0,21):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,720):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			if i > 200:
				while stop != 0:
					rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
					rospy.sleep(0.1)
		rospy.loginfo('In the fridge')
	else:
		rospy.loginfo('Cannot go there')
        return 'outcome1'

## -----------------------------
class Sink(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	#If in recharge
	if abs(data.pose.position.x - 1.35) < 0.1 and abs(data.pose.position.y - 0.015) < 0.1:
		for i in range(0,1800):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		for i in range(0,6):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
			rospy.sleep(0.2)
		for i in range(0,80):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		rospy.loginfo('In the sink')
	#If in human
	elif abs(data.pose.position.x + 2.5) < 0.1 and abs(data.pose.position.y + 3.95) < 0.1:
		for i in range(0,70):
			pub.publish(Vector3(-0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
		for i in range(0,63):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,2350):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		rospy.loginfo('In the sink')
				####
	else:
		rospy.loginfo('Cannot go there')
        return 'outcome1'

## ------------------------------------
class Human(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1','outcome2'])
    
    def execute(self, userdata):
    	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	#If in recharge
	if abs(data.pose.position.x - 1.35) < 0.1 and abs(data.pose.position.y - 0.015) < 0.1:
		for i in range(0,17):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,1200):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			while stop != 0:
				rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
				rospy.sleep(0.1)
		for i in range(0,10):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.2)
		for i in range(0,1160):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
			if i > 200:
				while stop != 0:
					rospy.Subscriber("collision_sensor", Int8, stopnow) # Check for collisions
					rospy.sleep(0.1)
		for i in range(0,22):
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,-0.5))
			rospy.sleep(0.2)
		for i in range(0,90):
			pub.publish(Vector3(0.25,0.0,0.0),Vector3(0.0,0.0,0.0))
			rospy.sleep(0.01)
		rospy.loginfo('In table')
	#If in fridge
			
	#If in sink
			###
	else:
		rospy.loginfo('Cannot go there')
        return 'outcome1'

## -------------------------------
class Grab(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
    	goal = PlayMotionGoal()
	goal.motion_name = 'close_hand'
  	goal.skip_planning = True
  	global client
  	client.send_goal(goal)
  	client.wait_for_result(rospy.Duration(3.0))
  	rospy.loginfo("grabbed")
  	pubdone.publish(1)
	rospy.sleep(0.5)
	pubdone.publish(0)
	return 'outcome1'

## -------------------------------------
class Drop(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
    	goal = PlayMotionGoal()
	goal.motion_name = 'open_hand'
  	goal.skip_planning = True
  	global client
  	client.send_goal(goal)
  	client.wait_for_result(rospy.Duration(3.0))
  	rospy.loginfo("dropped")
  	pubdone.publish(1)
	rospy.sleep(0.5)
	pubdone.publish(0)
	return 'outcome1'



## -----------------------------------
class Tuck(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
    	goal = PlayMotionGoal()
	goal.motion_name = 'home'
  	goal.skip_planning = True
  	global client
  	client.send_goal(goal)
  	client.wait_for_result(rospy.Duration(10.0))
  	rospy.loginfo("Arm tucked.")
  	pubdone.publish(1)
	rospy.sleep(0.5)
	pubdone.publish(0)
	return 'outcome1'

## -------------------------------
class Wait(smach.State):
    def __init__(self):
    	smach.State.__init__(self, outcomes=['outcome1'])
    
    def execute(self, userdata):
    	rospy.sleep(5)
        return 'outcome1'

## PREDEFINED PLANS ##
## Cook a meal: go to kitchen, go to fridge, grab food, go to cooker, drop food in cooker, wait, if burnt discard else grab food and go to living room, go to human and drop food in table, tuck arm and go to recharge
#def cook_meal():
#    	sm = smach.StateMachine(outcomes=['end_task']) # Create a SMACH state machine
#   	with sm: # Open the container
#		smach.StateMachine.add('GotoFridge', Fridge(), transitions={'outcome1':'Grab_food1'})
#		smach.StateMachine.add('Grab_food1', Grab(), transitions={'outcome1':'GotoCooker'})
#		smach.StateMachine.add('GotoCooker', Cooker(), transitions={'outcome1':'Drop_food1'})
#		smach.StateMachine.add('Drop_food1', Drop(), transitions={'outcome1':'Grab_food2'})
#		smach.StateMachine.add('Wait', Wait(), transitions={'outcome1':'Burned','outcome2':'Grab_food2'})
#		smach.StateMachine.add('Burned', Burned(), transitions={'outcome1':'GotoFridge','outcome2':'end_task'})
#		smach.StateMachine.add('Grab_food2', Grab(), transitions={'outcome1':'GotoHuman'})
#		smach.StateMachine.add('GotoHuman', Human(), transitions={'outcome1':'Drop_food2'})
#		smach.StateMachine.add('Drop_food2', Drop(), transitions={'outcome1':'Tuck_arm'})
#		smach.StateMachine.add('Tuck_arm', Tuck(), transitions={'outcome1':'end_task'})
#    	outcome = sm.execute()

## Wash dishes: go to human, grab food, go to sink, drop food in sink, wait, go to recharge if no new order


## MAIN ##	
def getgoal(data):
	global order
	order = data.data	


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
  	
  	#Listen to human and send orders to low level navigation control
  	while not rospy.is_shutdown():
	  	rospy.Subscriber("goal",String,getgoal) 
	  	rospy.sleep(0.2)
	  	rospy.loginfo(order)
	  	if order == 'fridge':
	  		sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to fridge
				smach.StateMachine.add('Fridge', Fridge(), transitions={'outcome1':'Grabfood'})
				#Grab food from fridge
				smach.StateMachine.add('Grabfood', Grab(), transitions={'outcome1':'nextOrder'})
	  		outcome = sm.execute()
	  	elif order == 'sink':
	  		sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to sink
				smach.StateMachine.add('Sink', Sink(), transitions={'outcome1':'Dropfood'})
				#Drop empty plates, or don't do anything if carrying nothing
				smach.StateMachine.add('Dropfood', Drop(), transitions={'outcome1':'nextOrder'})
	  		outcome = sm.execute()
	  	elif order == 'human':
	  		sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to table
				smach.StateMachine.add('Table', Human(), transitions={'outcome1':'Grabfood','outcome2':'Dropfood'})
				#Drop food if it has food, or take empty plates if carrying nothing
				smach.StateMachine.add('Dropfood', Drop(), transitions={'outcome1':'nextOrder'})
				smach.StateMachine.add('Grabfood', Grab(), transitions={'outcome1':'nextOrder'})
	  		outcome = sm.execute()
	  	elif order == 'recharge':
	  		sm = smach.StateMachine(outcomes=['nextOrder'])
	  		with sm:
				#Move to sink
				smach.StateMachine.add('Recharge', Recharge(), transitions={'outcome1':'nextOrder'})
	  		outcome = sm.execute()
	  	
	  	#cook_meal()
  	
	
	

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
        	
