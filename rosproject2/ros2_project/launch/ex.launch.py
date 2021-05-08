from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    obj_launch=LaunchDescription()
    node0=Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )
    node1=Node(
        package='ros2_project',
        executable='py_node_one',
        name='control_node'
    )
    node2=Node(
        package='ros2_project',
        executable='py_node_two',
        name='Spawn_node'
    )
    obj_launch.add_action(node0)
    obj_launch.add_action(node1)
    obj_launch.add_action(node2)
    return obj_launch
