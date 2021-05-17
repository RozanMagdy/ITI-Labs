#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class my_node(Node):
    def __init__(self):
        super().__init__("node2")
        self.counter=0
        self.flag= True
        self.get_logger().info("Node2 is Started")
        self.create_subscription(String,"String_topic",self.timer_call_sub,10)

        

    def timer_call_sub(self,msg_String):
        self.get_logger().info("I Heard: "+ msg_String.data)
        

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

