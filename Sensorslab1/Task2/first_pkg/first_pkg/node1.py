#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion
from math import sin, cos, pi
import pandas as pd


def quaternion_from_euler(roll, pitch, yaw):
        qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
        qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
        qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
        qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
        return qx, qy,qz, qw


class my_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.get_logger().info("Node1 is Started")
        self.create_timer(2,self.timer_call_pub)
        self.obj_pub=self.create_publisher(Imu,"zed2_imu",10)
        self.df  = pd.read_csv("imu_data.csv", header=None)
        self.yaw_list =  list(self.df[self.df.columns[6]])
        self.angX_list= list(self.df[self.df.columns[3]])
        self.angY_list= list(self.df[self.df.columns[4]])
        self.angZ_list= list(self.df[self.df.columns[5]])
        self.accX_list= list(self.df[self.df.columns[0]])
        self.accY_list= list(self.df[self.df.columns[1]])
        self.accZ_list= list(self.df[self.df.columns[2]])
        self.index=0
        
	
    def timer_call_pub(self):
        imu_msg=Imu()
        imu_msg.header.frame_id= "zed2_imu_link"
        imu_msg.header.stamp= self.get_clock().now().to_msg()
        X,Y,Z,W = quaternion_from_euler(0, 0,(self.yaw_list[self.index]*(pi/180)))
        imu_msg.orientation.w = W
        imu_msg.orientation.x = X
        imu_msg.orientation.y = Y
        imu_msg.orientation.z = Z
        imu_msg.orientation_covariance = [0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.001]
        # angular velocity
        imu_msg.angular_velocity.x =  self.angX_list[self.index]
        imu_msg.angular_velocity.y = self.angY_list[self.index]
        imu_msg.angular_velocity.z = self.angZ_list[self.index]
        imu_msg.angular_velocity_covariance=[0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.001]
        #linear acceleration
        imu_msg.linear_acceleration.x =  self.accX_list[self.index]*9.8
        imu_msg.linear_acceleration.y = self.accY_list[self.index]*9.8
        imu_msg.linear_acceleration.z = self.accZ_list[self.index]*9.8
        imu_msg.linear_acceleration_covariance=[0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.001]
        self.obj_pub.publish(imu_msg)
        self.get_logger().info(str(imu_msg))
        self.index=self.index+1
        

        
        

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
