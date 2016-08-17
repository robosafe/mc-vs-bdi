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




def main():
	rospy.init_node('robot_navigation', anonymous=True) #Start node first
	rospy.loginfo("Waiting for motion servers...")
	pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1,latch=True)
	
	
  	#Listen to human and send orders to low level navigation control
  	while not rospy.is_shutdown():
		getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		data = getmodel('tiago_steel','')
	
		while abs(data.pose.position.x + 2.8) > 0.02 and abs(data.pose.position.y - 0.405) > 0.02:
			pub.publish(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,0.5))
			rospy.sleep(0.25) #0.25 update in control, velocity can be varied to control motion. 
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
  	
	
	

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
        	
