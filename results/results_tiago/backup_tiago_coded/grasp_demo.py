#!/usr/bin/env python

import rospy
import actionlib
from play_motion_msgs.msg import PlayMotionAction, PlayMotionGoal
from sensor_msgs.msg import JointState

if __name__ == "__main__":
  rospy.init_node("grasp_demo")
  rospy.loginfo("Waiting for play_motion...")
  client = actionlib.SimpleActionClient("/play_motion", PlayMotionAction)
  client.wait_for_server()
  rospy.loginfo("...connected.")

  rospy.wait_for_message("/joint_states", JointState)
  rospy.sleep(3.0)

  rospy.loginfo("Grasping demo...")
  goal = PlayMotionGoal()

  goal.motion_name = 'home'
  goal.skip_planning = True
  client.send_goal(goal)
  client.wait_for_result(rospy.Duration(15.0))

  goal.motion_name = 'look_at_object_demo'
  goal.skip_planning = True
  client.send_goal(goal)
  client.wait_for_result(rospy.Duration(5.0))

  goal.motion_name = 'pregrasp_demo'
  goal.skip_planning = True
  client.send_goal(goal)
  client.wait_for_result(rospy.Duration(40.0))

  goal.motion_name = 'grasp_demo'
  goal.skip_planning = True
  client.send_goal(goal)
  client.wait_for_result(rospy.Duration(80.0))

  goal.motion_name = 'pick_demo'
  goal.skip_planning = True
  client.send_goal(goal)
  client.wait_for_result(rospy.Duration(40.0))

  rospy.loginfo("Grasping demo OK.")
