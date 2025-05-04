from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    return LaunchDescription([
        # Launch ACO node
        Node(
            package='master',
            executable='aco',
            name='aco_node',
            output='screen',
        ),
        # Launch statusReceiver node
        Node(
            package='master',
            executable='statusReceiver',
            name='status_receiver_node',
            output='screen',
        )
    ])