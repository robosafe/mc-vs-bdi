#!/usr/bin/env python

import rospy
import actionlib
import math
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion

if __name__ == "__main__":
  rospy.init_node("tuck_arm")
  rospy.loginfo("Waiting for play_motion...")
  client = actionlib.SimpleActionClient("/play_motion", PlayMotionAction)
  client.wait_for_server()
  rospy.loginfo("...connected.")

  rospy.wait_for_message("/joint_states", JointState)
  rospy.sleep(3.0)

  rospy.loginfo("Tuck arm...")
  goal = PlayMotionGoal()
  goal.motion_name = 'reset'
  goal.skip_planning = True
  
  client.send_goal(goal)
  client.wait_for_result(rospy.Duration(10.0))
  rospy.loginfo("Arm tucked.")
  
  rospy.loginfo("In reset position")

