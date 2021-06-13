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
        list_kp1 = [keypoints_current[mat.queryIdx].pt for mat in matches] 
        list_kp2 = [keypoints_last[mat.trainIdx].pt for mat in matches]
        x1= 0
        y1=0
        x2= 0
        y2=0
        for i in range(len(list_kp1)):
            x2+=(int (list_kp1[i][0]) -int (list_kp2[i][0]))
            y2+=(int (list_kp1[i][1]) -int (list_kp2[i][1]))

        try: 
            x2/=len(list_kp1)
            y2/=len(list_kp1)
        except:
            self.get_logger().info("Zero Divison")
        
        #Draw direction
        start_point = (int (self.cv_image_current.shape[0]/2),int (self.cv_image_current.shape[1]/2) )  
        end_point = (int (self.cv_image_current.shape[0]/2)+int (x2*5),int (self.cv_image_current.shape[1]/2)+int (y2*5)) 
        image = cv2.arrowedLine(self.cv_image_current, start_point, end_point,(0,255,0), 4)
        end = timeit.timeit()
        self.get_logger().info("Detection time "+ str(end - start))
        cv2.imshow("My_Image", image)
        if (cv2.waitKey(1) & 0xff) == ord('q'):
            cv2.destroyAllWindows()  
        self.cv_image_last= self.cv_image_current

        
        
    
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()