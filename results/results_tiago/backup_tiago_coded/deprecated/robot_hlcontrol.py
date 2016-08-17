#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan August 2016
"""

import sys
import os
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8

nextorder = 1
allorders=[]
order = 'none'

def next_order(data):
	global nextorder
	if data.data == 1:
		nextorder = 1
		
def getorder(data):
	global order
	order = data.data
	print data.data

def main():
	rospy.init_node('robot_hl', anonymous=True) #Start node first
	rospy.loginfo("Start node")
	#Listen to human, accumulate instructions, and send orders to low level navigation control
  	while not rospy.is_shutdown():
  		global nextorder
  		global order
	  	rospy.Subscriber('orders',String,getorder) 
	  	rospy.sleep(0.01)
	  	rospy.loginfo(order)
	  	if not order == 'none' and len(allorders)>0:
	  		if not order == allorders[len(allorders)-1]:
	  			allorders.append(order)
	  	print allorders
		rospy.Subscriber('done',Int8,next_order)
		rospy.sleep(0.01)
		if nextorder == 1:
	  		pub = rospy.Publisher('goal', String, queue_size=1,latch=True)
	  		if len(allorders) > 0:
				pub.publish(allorders.pop(0))
				rospy.loginfo('sent')
				rospy.sleep(1)
				nextorder == 0

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
