#include <chrono>
#include<string>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class Node2 : public rclcpp::Node
{
public:
    
    Node2():Node("string_subscriber")
    {
        RCLCPP_INFO(this->get_logger(),"string_subscriber has started");
        string_subscriber_ = this->create_subscription<std_msgs::msg::String>("str_topic",10, std::bind(&Node2::timer_cb_sub, this, std::placeholders::_1));
        flag_publisher_ = this->create_publisher<std_msgs::msg::String>("flag_topic",10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&Node2::timer_cb_pub, this) );
        
    }
private:
    void timer_cb_sub(const std_msgs::msg::String::SharedPtr string_msg)
    {
        RCLCPP_INFO(this->get_logger(),"'%s' ",string_msg->data.c_str());
        if(*(string_msg->data.c_str()+22)=='5'){
           Node2::flag=1;
        }
    }
     void timer_cb_pub()
    {
        std_msgs::msg::String flag_msg = std_msgs::msg::String();
        flag_msg.data = std::to_string(Node2::flag);
        flag_publisher_->publish(flag_msg);
        //RCLCPP_INFO(this->get_logger(),flag_msg.data);
        if (Node2::flag==1){
            Node2::flag=0;
        }
        
        
    }
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr string_subscriber_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr flag_publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    int flag='0';
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Node2>());
    rclcpp::shutdown();
    return 0;
}