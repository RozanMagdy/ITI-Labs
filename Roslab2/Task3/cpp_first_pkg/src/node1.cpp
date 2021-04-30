#include <chrono>
#include<string>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
 
class Node1 : public rclcpp::Node
{
public:
    Node1():Node("string_publisher")
    {
        RCLCPP_INFO(this->get_logger(),"string_publisher has started");
        string_publisher_ = this->create_publisher<std_msgs::msg::String>("str_topic",10);
        string_timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&Node1::timer_cb_pub_one, this) );
        int_publisher_ = this->create_publisher<std_msgs::msg::String>("int_topic",10);
        int_timer_ = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&Node1::timer_cb_pub_two, this) );
        flag_subscriber_ = this->create_subscription<std_msgs::msg::String>("flag_topic",10, std::bind(&Node1::timer_cb_sub, this, std::placeholders::_1));
    }
private:
    void timer_cb_pub_one()
    {
        std_msgs::msg::String string_msg = std_msgs::msg::String();
        string_msg.data = "Rouzan is puplishing, "+std::to_string(Node1::counter);
        Node1::counter++;
        string_publisher_->publish(string_msg);
    }
    void timer_cb_pub_two()
    {
        std_msgs::msg::String int_msg = std_msgs::msg::String();
        int_msg.data = std::to_string(Node1::counter);
        int_publisher_->publish(int_msg);
    }
    void timer_cb_sub(const std_msgs::msg::String::SharedPtr flag_msg)
    {
        Node1::flag=*(flag_msg->data.c_str());
        if (Node1::flag=='1'){
           Node1::counter=0;
           Node1::flag='0';
        }
       
    }
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr string_publisher_;
    rclcpp::TimerBase::SharedPtr string_timer_;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr int_publisher_;
    rclcpp::TimerBase::SharedPtr int_timer_;
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr flag_subscriber_;
    int counter =0;
    char flag ='0';
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc,argv);
    rclcpp::spin(std::make_shared<Node1>());
    rclcpp::shutdown();
    return 0;
} 
