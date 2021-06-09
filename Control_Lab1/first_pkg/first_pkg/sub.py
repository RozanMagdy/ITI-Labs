#!/usr/bin/env python3 
import math
import random
import timeit
import  rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class my_node(Node):
    def __init__(self):
        self.x1=0.0
        self.y1=0.0
        self.theta1=0.0

        self.x2=9.0
        self.y2=9.0
        self.theta2=3.1415926536

        self.uCum_Error=0
        self.uRate_Error=0
        self.aCum_Error=0
        self.aRate_Error=0
        self.uKP=1
        self.uKI=1
        self.uKD=1
        self.aKP=1
        self.aKI=0
        self.aKD=0
        self.ulastError=0
        self.alastError=0
        self.start=0
        self.stop=0

        super().__init__("control_node")
        self.get_logger().info("Control_node is Started")
        #-----------------PUB---------
        self.create_timer(2,self.timer_call_pub)
        self.start = timeit.default_timer()
        self.obj_pub_1=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        #---------------SUB-----------        
        self.create_subscription(Pose,"turtle1/pose",self.timer_call_sub,10)
        self.stop = timeit.default_timer()
       
       
       
    
    def timer_call_pub(self):
        Twist_msg=Twist()
        #self.start = timeit.default_timer()
        error_in_theta=math.atan2((self.y2-self.y1),(self.x2-self.x1))-self.theta1
        error_in_linear= math.sqrt((self.x2 - self.x1)**2+(self.y2 - self.y1)**2)
        elapsedTime= self.stop-self.start
        
        self.uCum_Error += error_in_linear * elapsedTime
        self.uRate_Error = (error_in_linear - self.ulastError)/elapsedTime

        self.aCum_Error += error_in_theta * elapsedTime
        self.aRate_Error = (error_in_theta - self.alastError)/elapsedTime

        uPID=(self.uKP*(error_in_linear))+(self.uKI*(self.uCum_Error)+(self.uKD*self.uRate_Error))
        aPID=(self.aKP*(error_in_theta))+(self.aKI*(self.aCum_Error)+(self.aKD*self.aRate_Error))
      
        if (abs(error_in_theta)>0.2):
            Twist_msg.angular.z= aPID
            Twist_msg.linear.x=0.0
        elif(abs(error_in_theta)<0.2):
            Twist_msg.angular.z=0.0
            Twist_msg.linear.x= uPID
        if (error_in_linear<0.2):        
            Twist_msg.angular.z= 0.0
            Twist_msg.linear.x=0.0
        self.obj_pub_1.publish(Twist_msg)

        self.ulastError=error_in_linear
        self.alastError=error_in_theta
        self.get_logger().info("Current Loc: X= " +str(self.x1)+", Y= "+str(self.y1))
        #self.stop = timeit.default_timer()

        
                   
               
    def timer_call_sub(self,pos_msg):
        self.x1 =pos_msg.x
        self.y1=pos_msg.y
        self.theta1=pos_msg.theta
    
   
        

    

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
