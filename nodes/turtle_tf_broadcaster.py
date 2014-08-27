#!/usr/bin/env python
import roslib
roslib.load_manifest('learning_tf')
import rospy
import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtle_name):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtle_name,
                     'world')

if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')
    turtle_name = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtle_name,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtle_name)
    rospy.spin()
