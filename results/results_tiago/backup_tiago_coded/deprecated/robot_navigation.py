#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan August 2016
"""

import sys
import os
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from std_msgs.msg import Int8
import math

thegoal = 'recharge'
vx = 0
vy = 0


def process_goal(data):
	global thegoal
	thegoal = data.data
	

	

def main():
	rospy.init_node('robot_navigation', anonymous=True) #Start node first
	rospy.loginfo("Start motion and collision avoidance")
	global previous_place
	global stop
	global thegoal
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	pubdone = rospy.Publisher('done', Int8, queue_size=1,latch=True)
	while True:
		rospy.Subscriber("goal", String, process_goal) # Check for current goal
		rospy.sleep(0.1)
		print thegoal
		
		if thegoal == 'fridge':
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
			else:
				rospy.loginfo('Cannot go there')
			pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			
		elif thegoal == 'sink':
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
			pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			
				
		elif thegoal == 'recharge':
			# If in fridge
			if abs(data.pose.position.x + 2.8) < 0.1 and abs(data.pose.position.y - 0.405) < 0.1:
				for i in range(0,44):
					pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
					rospy.sleep(0.2)
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
			pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			
			
		elif thegoal == 'human':
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
			pubdone.publish(1)
			rospy.sleep(0.5)
			pubdone.publish(0)
			


if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
