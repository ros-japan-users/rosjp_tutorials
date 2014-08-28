#!/usr/bin/env python
import math

import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('dynamic_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        angle = rospy.Time.now().to_sec() * math.pi
        br.sendTransform((10 * math.sin(angle), 10 * math.cos(angle), 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         'carrot1', 'turtle1')
        rate.sleep()
