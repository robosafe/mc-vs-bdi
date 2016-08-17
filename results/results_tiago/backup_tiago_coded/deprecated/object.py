#!/usr/bin/env python

"""
This script draws a cylindrical object in Gazebo, and keeps a node with the location of its mass center in x,y,z coordinates (absolute from an origin at the base of the robot. The node is updated via a state machine. 

Written by Dejanira Araiza-Illan, March 2015.
"""

import rospy
import smach
import smach_ros
import random
import os
from bert2_simulator.msg import *
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Vector3
from std_msgs.msg import Int8

correction = 0

def main():
	rospy.init_node('object', anonymous=True)
	
	while True:
    		getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		data = getmodel('tiago_steel','')
		print data.pose
		rospy.sleep(0.5)
	
    	

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
