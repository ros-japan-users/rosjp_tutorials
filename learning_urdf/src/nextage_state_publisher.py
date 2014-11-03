#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

import rospy
from sensor_msgs.msg import JointState
from hrpsys import rtm
from nextage_ros_bridge import nextage_client


if __name__ == '__main__':
    rospy.init_node('nextage_state_publisher')
    rtm.nshost = rospy.get_param('~host', 'localhost')
    name = rospy.get_param('~name', 'HiroNX(Robot)0')
    model_file = rospy.get_param('~model_file', '')

    robot = nextage_client.NextageClient()
    robot.init(robotname=name, url=model_file)

    publisher = rospy.Publisher('joint_states', JointState, queue_size=5)
    rate = rospy.Rate(rospy.get_param('~rate', 10))

    try:
        while not rospy.is_shutdown():
            msg = JointState()
            msg.header.stamp = rospy.Time.now()
            msg.position = [math.radians(deg)
                            for deg in robot.getJointAngles()[9:15]]
            msg.velocity = len(msg.position) * [0.0]
            msg.effort = len(msg.position) * [0.0]
            msg.name = ['LARM_JOINT0', 'LARM_JOINT1', 'LARM_JOINT2',
                        'LARM_JOINT3', 'LARM_JOINT4', 'LARM_JOINT5']

            publisher.publish(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
