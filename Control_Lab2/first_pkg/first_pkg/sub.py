#!/usr/bin/env python3 
from io import StringIO
import math
import random
import timeit
import  rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from example_interfaces.msg import String

import serial 


class my_node(Node):
    def __init__(self):
        self.Vleft_fb=0
        self.Vright_fb=0

        self.Vleft_calc=0
        self.Vright_calc=0

        self.liner_velocity=0
        self.angular_velocity=0

        self.length=0.58

        self.LeftCum_Error=0
        self.LeftRate_Error=0
        self.RightCum_Error=0
        self.RightRate_Error=0
        self.LeftKP=1
        self.LeftKI=0
        self.LeftKD=0
        self.RightKP=1
        self.RightKI=0
        self.RightKD=0
        self.LeftlastError=0
        self.RightlastError=0
        self.start=0
        self.stop=0

        self.LeftPID=0
        self.rightPID= 0

        super().__init__("control_node")
        self.get_logger().info("Control_node is Started")
        self.start = timeit.default_timer()
        #-----------------PUB---------
        self.create_timer(2,self.timer_call_pub)
        self.obj_pub_1=self.create_publisher(String,"PWM",10)
        #---------------SUB-----------        
        self.create_subscription(Twist,"cmd_vel",self.timer_call_sub,10)
        #-------------serial---------
        self.ser = serial.Serial('/dev/ttyACM0', 9600) 
        #-------------------
        self.stop = timeit.default_timer()
  
       
       
       
    
    def timer_call_pub(self):
        #-------------
        PIDmsg=String()
        PIDmsg.data = str(self.rightPID)+","+str(self.LeftPID)
        self.obj_pub_1.publish(PIDmsg)
        self.get_logger().info(PIDmsg.data)
        self.ser.write(PIDmsg.data)
        

        
                   
               
    def timer_call_sub(self,Twist_msg):
        Velocities= self.ser.readline().split(",")
        self.Vleft_fb= int(Velocities[0])
        self.Vright_fb= int(Velocities[1])

        self.angular_velocity=Twist_msg.angular.z
        self.liner_velocity=Twist_msg.linear.x

        self.Vleft_calc= ((2*self.liner_velocity)-(self.length*self.angular_velocity))/2
        self.Vright_calc= ((2*self.liner_velocity)+(self.length*self.angular_velocity))/2

        error_in_Vleft=abs(self.Vleft_fb- self.Vleft_calc)
        error_in_Vright=abs( self.Vright_fb-self.Vright_calc)

        elapsedTime= self.stop-self.start
        
        self.LeftCum_Error += error_in_Vleft * elapsedTime
        self.LeftRate_Error = (error_in_Vleft - self.LeftlastError)/elapsedTime

        self.RightCum_Error += error_in_Vright * elapsedTime
        self.RightRate_Error = (error_in_Vright - self.RightlastError)/elapsedTime

        self.LeftPID=(self.LeftKP*(error_in_Vleft))+(self.LeftKI*(self.LeftCum_Error)+(self.LeftKD*self.LeftRate_Error))
        self.rightPID=(self.RightKP*(error_in_Vright))+(self.RightKI*(self.RightCum_Error)+(self.RightKD*self.RightRate_Error))


        self.LeftlastError=error_in_Vleft
        self.RightlastError=error_in_Vright



        

   
        

    

def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()
