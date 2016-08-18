#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan August 2016
"""

import sys
import os
import rospy
import random
import math
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

rx = 0
ry = 0
rtheta = 0

def main(seeds):
	rospy.init_node('dog', anonymous=True) #Start node first
	rospy.loginfo("Dog_motion")
	random.seed(seeds)
	
	while not rospy.is_shutdown():
  		rospy.sleep(0.5)
  		getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		data = getmodel('dog','')
		robot = getmodel('tiago_steel','')
		
		rx = random.randint(-100,100)
		ry = random.randint(-100,100)
		rtheta = random.randint(-700,700)
		
		while data.pose.position.x + 15*(rx/1000.0) > 0.5 or data.pose.position.x + 15*(rx/1000.0) <-2.5 or data.pose.position.y + 15*(ry/1000.0)<-5.5 or data.pose.position.y + 15*(ry/1000.0)>-0.5:
			if math.sqrt(math.pow(robot.pose.position.x + 0.2 - data.pose.position.x - 0.15 - 15*(rx/1000.0),2) + math.pow(robot.pose.position.y + 0.2 - data.pose.position.y - 0.15 - 15*(rx/1000.0),2)) < 0.55:
				rx = random.randint(-1000,1000)
				ry = random.randint(-1000,1000)
				rtheta = random.randint(-700,700)
				getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
				data = getmodel('dog','')
				robot = getmodel('tiago_steel','')
			else:
				rx = random.randint(-100,100)
				ry = random.randint(-100,100)
				rtheta = random.randint(-700,700)
				getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
				data = getmodel('dog','')
				robot = getmodel('tiago_steel','')
		for i in range(0,15):
			getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
			#robot = getmodel('tiago_steel','')
			data = getmodel('dog','')
			#if math.sqrt(math.pow(robot.pose.position.x + 0.2 - data.pose.position.x - 0.15,2) + math.pow(robot.pose.position.y + 0.2 - data.pose.position.y - 0.15,2)) > 0.55:
			#data = getmodel('dog','')
			setmodel = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)	
			setmodel(ModelState('dog',Pose(Point(data.pose.position.x+(rx/1000.0),data.pose.position.y+(ry/1000.0),0.0),Quaternion(0.0,0.0,0.0,1.0)),Twist(Vector3(0.0,0.0,0.0),Vector3(0.0,0.0,rtheta/1000.0)),'world'))
			rospy.sleep(0.2)
		#print str(data.pose.position.x) +','+ str(data.pose.position.y)
  	

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main(sys.argv[1])
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
        	
