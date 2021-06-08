#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from carkyo_msgs.msg import CameraEmergency

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(LaserScan,"scan",self.scan_cb, rclpy.qos.qos_profile_sensor_data)
        self.create_subscription(Twist,"key_cmd_vel",self.twist_cb, rclpy.qos.qos_profile_sensor_data)  
        self.create_subscription(CameraEmergency,"CameraEmergency",self.CameraEmergency_cb, 10)  
        self.twist_pub = self.create_publisher(Twist,"cmd_vel", 10)      
        self.twist_msg = Twist()
        self.create_timer(1/5., self.timer_cb)
        self.LIDAR_close_forward_obstacles = False
        self.CAMERA_close_forward_obstacles= False

    def CameraEmergency_cb (self,message):
        if message.close_obstacle_detected == True:
        	self.CAMERA_close_forward_obstacles = True
        else:
            self.CAMERA_close_forward_obstacles = False
    def scan_cb(self,message):
        laser_data = message.ranges
        laser_data_length = len(laser_data)
        forward_data = []
        forward_data.extend(laser_data[:int(laser_data_length/10.)])
        forward_data.extend(laser_data[int(9*laser_data_length/10.):])
        print("len", len(laser_data), len(forward_data))

        min_forward_value = min(forward_data)
        
        
        if (min_forward_value < 0.5):
            print(min_forward_value, laser_data.index(min_forward_value))
            self.LIDAR_close_forward_obstacles = True
        else:
            self.LIDAR_close_forward_obstacles = False
        
    def timer_cb(self):
        if((self.CAMERA_close_forward_obstacles) or (self.LIDAR_close_forward_obstacles and self.twist_msg.linear.x > 0. )):
            self.twist_msg.linear.x = 0.
        self.twist_pub.publish(self.twist_msg)    
    
    def twist_cb(self, message):
        self.twist_msg = message

              
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()


