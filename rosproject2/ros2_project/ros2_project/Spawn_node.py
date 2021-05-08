#!/usr/bin/env python3 
import  rclpy
from rclpy.node import Node
from turtlesim.srv import Spawn
from third_pkg.srv import First

class my_node(Node):
    def __init__(self):
        super().__init__("Spawn_node")
        self.get_logger().info("Spawn_node is Started")
        self.create_service(First,"First",self.srv_call)

    def srv_call(self,rq,req):
        self.service_clinet_spawn(rq.x,rq.y,rq.theta,rq.name)  
        return(req)

    def service_clinet_spawn(self,x,y,theta,name):
        client_obj=self.create_client(Spawn,"spawn")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=Spawn.Request()
        req.x=x
        req.y=y
        req.theta=theta
        req.name=name
        future_obj=client_obj.call_async(req)

     

        



        
  

    

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
