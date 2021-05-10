#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from turtlesim.msg import Pose 
import pandas as pd
import matplotlib.pyplot as plt

class my_node(Node):
    def __init__(self):
        super().__init__("Sub_node")
        self.get_logger().info("Sub node is Started")
        self.create_subscription(Pose,"turtle1/custom_pose",self.timer_call_sub,rclpy.qos.qos_profile_system_default)
        self.df = pd.DataFrame(columns=['x',  'y'])

    def timer_call_sub(self,msg_str):
        self.get_logger().info(str(msg_str))
        self.df = self.df.append({'x': msg_str.x, 'y':msg_str.y}, ignore_index=True)
        self.df.to_csv (r"pose_data.csv", index = False)
        df  = pd.read_csv("pose_data.csv")
        fig=df.plot(kind='scatter',x='x',y='y').get_figure() # scatter plot
        fig.savefig('test.png')
        
        

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()
    


if __name__=="__main__":
    main()

