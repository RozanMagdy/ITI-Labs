#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from example_interfaces.srv import  SetBool


class my_node(Node):
    def __init__(self):
        super().__init__("node3")
        self.get_logger().info("Node3 is Started")
        self.service_clinet(False)

    def service_clinet(self,data):
        client_obj=self.create_client(SetBool,"My_Server")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=SetBool.Request()
        req.data=data
        future_obj=client_obj.call_async(req)
        #future_obj.add_done_callback(self.futur_call)

    #def futur_call(self, Future_msg): 
        #self.get_logger().error(str(Future_msg))
        
        


def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
