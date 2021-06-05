#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
from example_interfaces.msg import String
import math 
import numpy as np

def menger_curvature(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
    triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
        
    try:
        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
        return curvature
    except:
        return 0 

def euler_from_quaternion(quaternion):
    """
    Converts quaternion (w in last place) to euler roll, pitch, yaw
    quaternion = [x, y, z, w]
    Bellow should be replaced when porting for ROS 2 Python tf_conversions is done.
    """
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
        self.curvaturemsg=""
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.create_subscription(Path,"local_plan",self.timer_call_sub,10)
        self.create_timer(2,self.timer_call_pub_one)
        self.obj_pub_one=self.create_publisher(String,"curvature_topic",10)
        
        

    def timer_call_sub(self,msg_path):
        try:
            poses_size= len(msg_path.poses)
            point_1_x = msg_path.poses[0].pose.position.x
            point_1_y = msg_path.poses[0].pose.position.y
            point_2_x = msg_path.poses[int(poses_size/2)].pose.position.x
            point_2_y = msg_path.poses[int(poses_size/2)].pose.position.y
            point_3_x = msg_path.poses[-1].pose.position.x
            point_3_y = msg_path.poses[-1].pose.position.y
            curvature = menger_curvature( point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)
            _,_, yaw_now = euler_from_quaternion(msg_path.poses[0].pose.orientation)
            _,_, yaw_goal = euler_from_quaternion(msg_path.poses[-1].pose.orientation)

            if (curvature >= (0.8)):  ## radiuas > 50 is considers as stright line  then C < (1/50) is straight line 
                if(yaw_now >= yaw_goal):
                    self.get_logger().info("The robot is turning right with a curvature "+ str(curvature))
                    self.curvaturemsg="The robot is turning right with a curvature "+ str(curvature)
                else:
                    self.get_logger().info("The robot is turning left with a curvature "+ str(curvature))
                    self.curvaturemsg="The robot is turning left with a curvature "+ str(curvature)

            else:
                self.get_logger().info("The path is straight")
                self.curvaturemsg="The path is straight"
        except:
            self.get_logger().info("Failed to calculate the path")
            self.curvaturemsg="Failed to calculate the path"



    def timer_call_pub_one(self):
        msg_curvature=String()
        msg_curvature.data= self.curvaturemsg
        self.obj_pub_one.publish(msg_curvature)
        
    
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

