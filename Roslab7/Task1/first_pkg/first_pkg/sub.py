#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.msg import String 

class my_node(Node):
    def __init__(self):
        super().__init__("Sub_node")
        self.counter=0
        self.get_logger().info("Sub node is Started")
        self.create_subscription(String,"my_topic",self.timer_call_sub,rclpy.qos.qos_profile_system_default)
        

    def timer_call_sub(self,msg_str):
       
        self.get_logger().info(msg_str.data)
        self.get_logger().info("Rouzan heard :" +msg_str.data +","+str(self.counter)+" times")
        self.counter+=1

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

