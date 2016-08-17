#!/usr/bin/env python
"""
Written by Dejanira Araiza-Illan August 2016
"""

import sys
import os
import rospy
import random
import re
from std_msgs.msg import String

def main(name_file,seed):
	rospy.init_node('human', anonymous=True) #Start node first
	rospy.loginfo("Human started")
	random.seed(seed)
	pub = rospy.Publisher("orders",String,queue_size=1,latch=True)
	#Read the abstract test, execute it, and concretize it
	for num,command in enumerate(open(os.getcwd()+'/src/tiago_simulation/tiago_gazebo/scripts/pr_tests/'+name_file+'.txt','r')): 
		thecommand = re.split('\n',command)
		pub.publish(thecommand[0])
		rospy.loginfo(thecommand[0])
		rospy.sleep(1)
		pub.publish('')
		if thecommand[0] == 'fridge' or thecommand[0] == 'sink' or thecommand[0] == 'recharge':
			waittime = random.randint(90,120) #Concrete test: waiting intervals
		elif thecommand[0] == 'clean':
			waittime = random.randint(150,180)
		else:
			waittime = random.randint(300,350)
		rospy.loginfo('Wait '+ str(waittime) +' secs')
  		rospy.sleep(waittime)
  	rospy.loginfo('ended')
  	pub.publish('ended')
  	rospy.sleep(1)
  		
  	
	
	

#---------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	try:
    		main(sys.argv[1],sys.argv[2])
	except rospy.ROSInterruptException: #to stop the code when pressing Ctr+c
		pass
        	
        	
