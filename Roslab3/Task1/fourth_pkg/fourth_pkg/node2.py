#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from third_pkg.msg import Firstone
from example_interfaces.msg import UInt64
#from example_interfaces.srv import SetBool
from third_pkg.srv import First

class my_node(Node):
    def __init__(self):
        super().__init__("node2")
        self.counter=0
        self.flag= True
        self.get_logger().info("Node2 is Started")
        self.create_subscription(Firstone,"uint64_topic",self.timer_call_sub,10)

        self.create_timer(2,self.timer_call_pub_one)
        self.obj_pub_one=self.create_publisher(UInt64,"counter_topic",10)

        self.create_service(First,"My_Server",self.srv_call)

    def timer_call_sub(self,msg_Firstone):
        self.get_logger().info('i get data and the counter is '+ str(self.counter))
        self.counter=self.counter+msg_Firstone.number

    def timer_call_pub_one(self):
        msg_counter=UInt64()
        msg_counter.data=self.counter
        self.obj_pub_one.publish(msg_counter)

    def srv_call(self,rq,req):
        self.flag=rq.check
        if self.flag==False:
            self.counter=0
        self.get_logger().info('Done Rest counter is '+str(self.counter))
        return(req)
    

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

