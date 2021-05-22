#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import pandas as pd
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import numpy as np





def euler_from_quaternion(quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w

        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)

        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)

        return roll, pitch, yaw 


class my_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.get_logger().info("Node1 is Started")
        self.create_subscription(Odometry,"odom",self.timer_call_sub,10)
        self.df  = pd.read_csv("pose.csv")
        self.angX_list= list(self.df[self.df.columns[0]])
        self.angY_list= list(self.df[self.df.columns[1]])
        self.yaw_list =  list(self.df[self.df.columns[2]])
        self.index=0
        

    def timer_call_sub(self,odom_msg):
        currentX=odom_msg.pose.pose.position.x 
        currentY=odom_msg.pose.pose.position.y
        _,_,currentYAW=euler_from_quaternion(odom_msg.pose.pose.orientation)*(180/pi)
        self.get_logger().info("current data "+str(currentX)+' '+str(currentY)+' '+str(currentYAW))
        expectedX=self.angX_list[self.index]    
        expectedY=self.angY_list[self.index]  
        expectedYAW=self.yaw_list[self.index]  
        if(abs(currentX-expectedX)==0.5) and (abs(currentY-expectedY)==0.5) and (abs(currentYAW-expectedYAW)==5):
            self.index= self.index+1
            if self.index>len(self.yaw_list):
                 self.get_logger().info("i execute all position and last one is"+ str(currentX)+","+ str(currentY)+","+ str(currentYAW))
                 self.index=0

        


        

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
