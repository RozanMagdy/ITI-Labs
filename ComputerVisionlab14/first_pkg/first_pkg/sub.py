#!/usr/bin/env python3 
import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2 
from cv_bridge import CvBridge
from matplotlib import pyplot as plt
import timeit





class my_node(Node):
    def __init__(self): 
        self.lastavragedistance=0
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.cv_image_current=cv2.imread('/home/rouzan/ROSWS/src/first_pkg/first_pkg/frame1.png')
        self.cv_image_last=cv2.imread('/home/rouzan/ROSWS/src/first_pkg/first_pkg/frame2.png')
        self.create_subscription(Image,"intel_realsense_d435_depth/image_raw",self.scan_cb, rclpy.qos.qos_profile_sensor_data)
         
    def scan_cb(self,msg):
        bridge = CvBridge()
        self.cv_image_current = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        start = timeit.timeit()
        # Initiate ORB object
        orb = cv2.ORB_create()
        # find the keypoints with ORB
        self.cv_image_current = cv2.cvtColor( self.cv_image_current, cv2.COLOR_BGR2GRAY)
        keypoints_current, descriptors_current = orb.detectAndCompute(self.cv_image_current, None)
        keypoints_last, descriptors_last = orb.detectAndCompute(self.cv_image_last, None)
        #feature matching
        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
        matches = bf.match(descriptors_current, descriptors_last)
        matches = sorted(matches, key = lambda x:x.distance)
        distances=0
        average_distance=0
        for i in range(len(matches)):
             distances=distances+matches[i].distance
        try:
            average_distance=(distances/len(matches))
        except:
                self.get_logger().info("zero division")
        if(average_distance> self.lastavragedistance):
            self.get_logger().info("robot is movong right")
        else:
            self.get_logger().info("robot is movong left")
        self.get_logger().info(str(average_distance))
        self.get_logger().info("Done")
        end = timeit.timeit()
        self.get_logger().info("Detection time "+ str(end - start))
        img = cv2.drawMatches(self.cv_image_current , keypoints_current, self.cv_image_last, keypoints_last, matches, self.cv_image_last, flags=2)
        plt.figure(figsize=(25,15))
        plt.imshow(img)
        plt.show()
        self.cv_image_last= self.cv_image_current
        self.lastavragedistance=average_distance
        
        
        
    
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()