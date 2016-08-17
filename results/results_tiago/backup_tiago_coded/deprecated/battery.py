#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan August 2016
"""

import sys
import os
import rospy

def main():
	rospy.init_node('battery', anonymous=True) #Start node first
	rospy.loginfo("Start battery")

  	rospy.sleep(5)
  	# Reset robot always
  	
	
	

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main()
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
        	
