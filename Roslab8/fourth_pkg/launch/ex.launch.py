from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    obj_launch=LaunchDescription()
    node1=Node(
        package='fourth_pkg',
        executable='py_node_one',
        name='node1'
    )
    node2=Node(
        package='fourth_pkg',
        executable='py_node_two',
        name='node2'
    )

    obj_launch.add_action(node1)
    obj_launch.add_action(node2)
    return obj_launch