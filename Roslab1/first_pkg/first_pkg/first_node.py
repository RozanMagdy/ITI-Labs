#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.msg import String 

class my_node(Node):
    def __init__(self):
        super().__init__("My_Node")
        self.flag=''
        self.counter=0
        self.get_logger().info("Node is Started")
        self.create_timer(2,self.timer_call_pub)
        self.obj_pub=self.create_publisher(String,"str_topic",10)
        self.create_subscription(String,"Flag_topic",self.timer_call_sub_one,10)
        self.create_subscription(String,"int_topic",self.timer_call_sub_two,10)
	
    def timer_call_pub(self):
        msg_str=String()
        number= str(self.counter)
        self.counter+=1
        msg_str.data='Rouzan is publish, '+ number
        self.obj_pub.publish(msg_str)

    def timer_call_sub_one(self,msg_flag):
        self.flag=msg_flag.data
        if (self.flag =='stop'):
            self.counter=0
            self.flag=''
    def timer_call_sub_two(self,msg_int):
        self.get_logger().info(msg_int.data)


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
