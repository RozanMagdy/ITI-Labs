#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
#from example_interfaces.srv import  
from std_srvs.srv import Empty


class my_node(Node):
    def __init__(self):
        super().__init__("nodeturtle")
        self.get_logger().info("nodeturtle is Started")
        self.service_clinet()

    def service_clinet(self):
        client_obj=self.create_client(Empty,"reset")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=Empty.Request()
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
