#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.msg import UInt64 

class my_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.counter=3
        self.get_logger().info("Node1 is Started")
        self.create_timer(2,self.timer_call_pub)
        self.obj_pub=self.create_publisher(UInt64,"uint64_topic",10)
        
	
    def timer_call_pub(self):
        msg_uint64=UInt64()
        msg_uint64.data= self.counter
        self.obj_pub.publish(msg_uint64)
        self.get_logger().info(str(msg_uint64.data))


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
