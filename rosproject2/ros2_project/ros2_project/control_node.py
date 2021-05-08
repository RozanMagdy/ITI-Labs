#!/usr/bin/env python3 
import math
import random
import  rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from third_pkg.srv import First
from std_srvs.srv import Empty

class my_node(Node):
    def __init__(self):
        self.x1=0.0
        self.y1=0.0
        self.theta1=0.0

        self.x2=random.uniform(1,10)
        self.y2=random.uniform(1,10)
        self.theta2=random.uniform(1,3.1415926536)
        self.name_goal='turtle2'
        super().__init__("control_node")
        self.get_logger().info("Control_node is Started")
        #-----------------PUB---------
        self.create_timer(2,self.timer_call_pub)
        self.obj_pub_1=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        #---------------SUB-----------        
        self.create_subscription(Pose,"turtle1/pose",self.timer_call_sub,10)
        #-------------client-Spwan_node--------------
        #self.service_loop
        self.service_clinet_spawn(self.x2,self.y2,self.theta2,self.name_goal) 
       
    
    def timer_call_pub(self):
        Twist_msg=Twist()
        error_in_theta=math.atan2((self.y2-self.y1),(self.x2-self.x1))-self.theta1
        error_in_linear= math.sqrt((self.x2 - self.x1)**2+(self.y2 - self.y1)**2)
        if (abs(error_in_theta)>0.2):
            Twist_msg.angular.z= error_in_theta
            Twist_msg.linear.x=0.0
        elif(abs(error_in_theta)<0.2):
            Twist_msg.angular.z=0.0
            Twist_msg.linear.x= error_in_linear
        self.obj_pub_1.publish(Twist_msg)
        if (error_in_linear<0.2):        
             #-------------client-kill--------------
            self.service_clinet_kill('turtle2')
            Twist_msg.angular.z= 0.0
            Twist_msg.linear.x=0.0
                   
               
    def timer_call_sub(self,pos_msg):
        self.x1 =pos_msg.x
        self.y1=pos_msg.y
        self.theta1=pos_msg.theta
    
    def service_clinet_kill(self,name):
        client_obj=self.create_client(Kill,"kill")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=Kill.Request()
        req.name=name
        future_obj=client_obj.call_async(req)
        future_obj.add_done_callback(self.futur_call)

    def futur_call(self,futur_message): 
        self.service_clinet_clear()
        self.x2=random.uniform(1,10)
        self.y2=random.uniform(1,10)
        self.theta2=random.uniform(1,1415926536)
        self.service_clinet_spawn(self.x2,self.y2,self.theta2,self.name_goal)  

    def service_clinet_spawn(self,x,y,theta,name):
        client_obj=self.create_client(First,"First")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=First.Request()
        req.x=x
        req.y=y
        req.theta=theta
        req.name=name
        future_obj=client_obj.call_async(req)

    def service_clinet_clear(self):
        client_obj=self.create_client(Empty,"clear")
        while client_obj.wait_for_service(0.5)==False:
            self.get_logger().warn('wait for server')
        req=Empty.Request()
        future_obj=client_obj.call_async(req)
        

    

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
