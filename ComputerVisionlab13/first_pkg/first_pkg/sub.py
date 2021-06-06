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
        self.linear_x=0.0
        self.angular_z=0.0
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.create_subscription(Image,"intel_realsense_d435_depth/image_raw",self.scan_cb, rclpy.qos.qos_profile_sensor_data)
         
    def scan_cb(self,msg):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        black= np.ones_like(cv_image)
        gray = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
        start = timeit.timeit()
        corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
        for i in corners:
            x,y = i.ravel()
            cv2.circle(black,(x,y),3,255,-1)
        end = timeit.timeit()
        self.get_logger().info("Corner Detection time "+ str(end - start))
        cv2.imshow("img", black)
        cv2.imshow("coreners", cv_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        
        
        
    
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

