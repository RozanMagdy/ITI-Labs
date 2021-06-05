#!/usr/bin/env python3 
import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist




class my_node(Node):
    def __init__(self): 
        self.linear_x=0.0
        self.angular_z=0.0
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.create_subscription(LaserScan,"scan",self.scan_cb, rclpy.qos.qos_profile_sensor_data)
        self.create_subscription(Twist,"key_cmd_vel",self.cmd_vel_cb, 10)
        self.obj_pub=self.create_publisher(Twist,"cmd_vel",10)

    def cmd_vel_cb(self,msg):
        self.linear_x= msg.linear.x
        self.angular_z =msg.angular.z

        
    def scan_cb(self,msg):
        #print(len(msg.ranges))
        regions = {
        'right':  min(min(msg.ranges[0:72]), 10),
        'fright': min(min(msg.ranges[73:144]), 10),
        'front':  min(min(msg.ranges[145:216]), 10),
        'fleft':  min(min(msg.ranges[217:288]), 10),
        'left':   min(min(msg.ranges[289:359]), 10),
        }

        self.take_action(regions)

    def take_action (self,regions):
        msg = Twist()
        state_description = ''
        if regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] > 1:
            state_description = 'case 1 - nothing'
        elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] > 1:
            state_description = 'case 2 - front'
            self.linear_x = 0.0
            self.angular_z = -0.3
        elif regions['front'] > 1 and regions['fleft'] > 1 and regions['fright'] < 1:
            state_description = 'case 3 - fright'           
        elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] > 1:
            state_description = 'case 4 - fleft'           
        elif regions['front'] < 1 and regions['fleft'] > 1 and regions['fright'] < 1:
            state_description = 'case 5 - front and fright'
            self.linear_x = 0.0
            self.angular_z = -0.3
        elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] > 1:
            state_description = 'case 6 - front and fleft'
            self.linear_x = 0.0
            self.angular_z = 0.3
        elif regions['front'] < 1 and regions['fleft'] < 1 and regions['fright'] < 1:
            state_description = 'case 7 - front and fleft and fright'
            self.linear_x = 0.0
            self.angular_z = -0.3
        elif regions['front'] > 1 and regions['fleft'] < 1 and regions['fright'] < 1:
            state_description = 'case 8 - fleft and fright'    

        else:
            state_description = 'unknown case'
        msg.linear.x = self.linear_x
        msg.angular.z = self.angular_z
        self.obj_pub.publish(msg)


        
        
        
    
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

