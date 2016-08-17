#!/usr/bin/env python
"""
Implements assertion : if 'Gazebo state'... (for velocity monitoring)

Written by Dejanira Araiza-Illan, February 2016
"""
import sys
import rospy
import time
import math
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

stats = open('assertion3.txt','a')
globaltime = 0
x = 0
y = 0

def main(number):
	rospy.init_node('assertion3', anonymous=True) #Start node first
	global fileno
	global fail
	fileno = number
	
	getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
	data = getmodel('tiago_steel','')
	x = data.pose.position.x
	y = data.pose.position.y
	
	while not rospy.is_shutdown():
		rospy.sleep(1)
		getmodel = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
		data = getmodel('tiago_steel','')
       		if math.sqrt(math.pow(data.pose.position.x-x,2)+math.pow(data.pose.position.y-y,2)) >=0.25:	
               		stats.write('Assertion 4 at test '+ str(fileno) +': Failed at global time '+ str(time.time()-globaltime) +'\n')
               	else:
               		stats.write('Assertion 4 at test '+ str(fileno) +': Passed at global time '+ str(time.time()-globaltime) +'\n')
      		x = data.pose.position.x
      		y = data.pose.position.y          
              
if __name__ == '__main__':
	try:
		main(sys.argv[1])
	except	rospy.ROSInterruptException:
		pass

