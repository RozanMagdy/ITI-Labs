#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from rclpy.qos_event import QoSLivelinessLostInfo

class my_node(Node):
    def __init__(self):
        super().__init__("node1")
        self.messaage=["Hi","Hello"]
        self.flipflop=0
        self.get_logger().info("Node1 is Started")
        self.create_timer(1,self.timer_call_pub)
        self.obj_pub=self.create_publisher(String,"String_topic",10)
        
	
    def timer_call_pub(self):
        msg_String=String()
        msg_String.data=self.messaage[self.flipflop]
        self.obj_pub.publish(msg_String)
        if self.flipflop == 0:
            self.flipflop=1
        elif self.flipflop==1:
            self.flipflop=0
        

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
