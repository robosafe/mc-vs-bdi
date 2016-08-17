#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan August 2016
"""

import sys
import os
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Int8

collided = 0


def process_this(data):
	global collided
	for i,value in enumerate(data.ranges):
		if value < 0.2:
			collided = 1
			print value
			break
		#else:
		#	print 0

def main():
	rospy.init_node('sensors', anonymous=True) #Start node first
	rospy.loginfo("Start reading")
	pub = rospy.Publisher('collision_sensor', Int8, queue_size=1,latch=True)
	global collided
	
	while not rospy.is_shutdown():
		rospy.Subscriber("/scan",LaserScan,process_this)
		rospy.sleep(0.5)
		if collided == 1:
			pub.publish(1)
			rospy.sleep(0.5)
			collided = 0
		else:
			pub.publish(0)
	
#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
