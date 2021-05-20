#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
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
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.create_subscription(Imu,"imu",self.timer_call_sub,10)
       

    def timer_call_sub(self,imu_msg):
        roll, pitch, yaw = euler_from_quaternion(imu_msg.orientation)
        if (yaw >=-2 ) and (yaw<=2) :
            self.get_logger().info("The robot is nearly heading north .. Heading is: "+ str(yaw) +"degrees.")

        if(abs(imu_msg.linear_acceleration.x)==0.3):
            self.get_logger().warning("Warning !! .. linear acceleration x exceeded the limit. Current acceleration is " + str(imu_msg.linear_acceleration.x) +"m/s^2.")
        if (abs(imu_msg.angular_velocity.z)==0.3):      
            self.get_logger().warning("Warning !! .. angular velocity z exceeded the limit. Current acceleration is " + str(imu_msg.angular_velocity.z)+ "rad/sec.")



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()
    


if __name__=="__main__":
    main()

