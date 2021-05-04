#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from third_pkg.msg import Firstone

class my_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.counter=5
        self.get_logger().info("Node1 is Started")
        self.create_timer(2,self.timer_call_pub)
        self.obj_pub=self.create_publisher(Firstone,"uint64_topic",10)
        
	
    def timer_call_pub(self):
        msg_Firstone=Firstone()
        msg_Firstone.message="Rouzan is buplishing , 5"
        msg_Firstone.number= self.counter
        self.obj_pub.publish(msg_Firstone)
        self.get_logger().info(msg_Firstone.message)
        self.get_logger().info(str(msg_Firstone.number))


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
