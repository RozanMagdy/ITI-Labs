#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.msg import String 

class my_node(Node):
    def __init__(self):
        super().__init__("Sub_node")
        self.flag=''
        self.counter=''
        self.get_logger().info("Sub node is Started")
        self.create_subscription(String,"str_topic",self.timer_call_sub,10)
        self.create_timer(2,self.timer_call_pub_one)
        self.obj_pub_one=self.create_publisher(String,"Flag_topic",10)
        self.create_timer(2,self.timer_call_pub_two)
        self.obj_pub_two=self.create_publisher(String,"int_topic",10)

    def timer_call_sub(self,msg_str):
        self.get_logger().info(msg_str.data)
        self.counter=msg_str.data[-1]
        if msg_str.data[-1]=='5':
            self.flag='stop'

    def timer_call_pub_one(self):
        msg_flag=String()
        msg_flag.data=self.flag
        self.obj_pub_one.publish(msg_flag)
        if (self.flag =='stop'):
            self.flag=''

    def timer_call_pub_two(self):
        msg_int=String()
        msg_int.data=self.counter
        self.obj_pub_two.publish(msg_int)

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

