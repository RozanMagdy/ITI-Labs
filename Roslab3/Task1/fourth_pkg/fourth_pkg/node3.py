#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
#from example_interfaces.srv import  SetBool
from third_pkg.srv import First

class my_node(Node):
    def __init__(self):
        super().__init__("node3")
        self.get_logger().info("Node3 is Started")
        self.service_clinet(False)

    def service_clinet(self,data):
        client_obj=self.create_client(First,"My_Server")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=First.Request()
        req.check=data
        future_obj=client_obj.call_async(req)
        
        
        


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
