#!/usr/bin/env python
import roslib
roslib.load_manifest('learning_cv_bridge')
import rospy
import cv2 as cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageConverter:
    def __init__(self):
        image = rospy.get_param('~image')
        self.pub = rospy.Publisher('cv_image', Image)
        self.bridge = CvBridge()
        self.sub = rospy.Subscriber(image, Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv(data, 'bgr8')
        except CvBridgeError:
            raise

        # TODO: Do something with cv_image.

        try:
            self.pub.publish(self.bridge.cv_to_imgmsg(cv_image, 'bgr8'))
        except CvBridgeError:
            raise

if __name__ == '__main__':
    rospy.init_node('cv_bridge_broadcaster')
    ic = ImageConverter()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        cv.destroyAllWindows()
