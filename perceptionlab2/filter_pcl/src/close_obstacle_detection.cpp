#include<string>
#include <iostream>
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/point_cloud2.hpp"
#include "carkyo_msgs/msg/camera_emergency.hpp"

#include <pcl_conversions/pcl_conversions.h>


 
using namespace std;

class PointcloudFilter : public rclcpp::Node
{
  
  public:
    PointcloudFilter()
    : Node("pcl_filter_node")
    {
      
            
      RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "create sub");
      subscriber_ = this->create_subscription<sensor_msgs::msg::PointCloud2>("intel/cropped", 5, std::bind(&PointcloudFilter::subscribe_message, this, std::placeholders::_1));
      publisher_emergency = this->create_publisher<carkyo_msgs::msg::CameraEmergency>("CameraEmergency", 10);
     
    }
  
  private:

    void subscribe_message(const sensor_msgs::msg::PointCloud2::SharedPtr message) const
    {
      pcl::PCLPointCloud2 pcl_pc2;
	    pcl_conversions::toPCL(*message,pcl_pc2);
	    pcl::PointCloud<pcl::PointXYZ>::Ptr inputCloudI(new pcl::PointCloud<pcl::PointXYZ>);
	    pcl::fromPCLPointCloud2(pcl_pc2,*inputCloudI);
      pcl::PointCloud<pcl::PointXYZ>::Ptr inputCloudII (new pcl::PointCloud<pcl::PointXYZ>);
      int array_size = inputCloudI->points.size();
      float array_Z [array_size];
        for (size_t i = 0; i < inputCloudI->points.size(); i++){
            float x = inputCloudI->points[i].x;
            float y = inputCloudI->points[i].y;
            float z = inputCloudI->points[i].z;
            array_Z[i]=inputCloudI->points[i].z;
           
            // x is right and left , + is left
            // z is forward and back , + is forward (all data should be + , close obst should be 0:1m)
            // y is down and up , +ve is down, ground obst should be > 0.1
            //if (z < 1 &&  y < 0.1)    // Another way to filter without using processpointclouf file        
            inputCloudII->push_back (pcl::PointXYZ (x, y, z));
        }
      float min = array_Z[0];
      // search num in inputArray from index 0 to elementCount-1 
      for(int i = 0; i < array_size; i++){
        if(array_Z[i] < min){
            min = array_Z[i];
        }
      }
      carkyo_msgs::msg::CameraEmergency CameraEmergency = carkyo_msgs::msg:: CameraEmergency();
      if (message->data.size()>10)
        {
          CameraEmergency.close_obstacle_detected = true;
          CameraEmergency.min_distance = min;
        }
      else
        {  
          CameraEmergency.close_obstacle_detected = false;
          CameraEmergency.min_distance = min;
        }
      publisher_emergency->publish(CameraEmergency);
    }
    rclcpp::Node::SharedPtr nh_;
    rclcpp::Publisher<carkyo_msgs::msg::CameraEmergency>::SharedPtr publisher_emergency;    
    rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr subscriber_;
  
};

int main(int argc, char * argv[])
{
  RCLCPP_INFO(rclcpp::get_logger("rclcpp"), "Ready");
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<PointcloudFilter>());
  rclcpp::shutdown();
  return 0;
}
