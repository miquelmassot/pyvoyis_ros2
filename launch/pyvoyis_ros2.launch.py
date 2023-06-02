from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    pyvoyis_ros2_node = Node(
        package="pyvoyis_ros2",
        executable="pyvoyis_ros2",
    )
    ld.add_action(pyvoyis_ros2_node)
    return ld