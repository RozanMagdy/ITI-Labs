#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import math 

def menger_curvature( point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
            
        curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
        return curvature

class my_node(Node):
    def __init__(self):
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.create_subscription(Path,"plan",self.timer_call_sub,10)
        
        

    def timer_call_sub(self,msg_path):
        poses_size= len(msg_path.poses)
        point_1_x = msg_path.poses[0].pose.position.x
        point_1_y = msg_path.poses[0].pose.position.y
        point_2_x = msg_path.poses[int(poses_size/3)].pose.position.x
        point_2_y = msg_path.poses[int(poses_size/3)].pose.position.y
        point_3_x = msg_path.poses[int(poses_size/2)].pose.position.x
        point_3_y = msg_path.poses[int(poses_size/2)].pose.position.y
        curvature = menger_curvature( point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)

        if (curvature >= (0.02)):  ## radiuas > 50 is considers as stright line  then C < (1/50) is straight line 
            self.get_logger().info("The robot is turning with a curvature "+ str(curvature))
        else:
             self.get_logger().info("The path is straight")
        

    
def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

