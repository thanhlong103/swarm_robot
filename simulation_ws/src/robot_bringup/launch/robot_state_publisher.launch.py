import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, GroupAction
from launch_ros.actions import Node
from launch_ros.descriptions import Group

import xacro


def generate_launch_description():

    # Number of robots to spawn
    robot_count = LaunchConfiguration('robot_count')

    # Use sim time or not
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Get package path
    pkg_path = os.path.join(get_package_share_directory('robot_bringup'))
    xacro_file = os.path.join(pkg_path, 'descriptions', 'robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file).toxml()

    # Function to create a GroupAction for each robot
    def create_robot_group(robot_id):
        namespace = f'robot_{robot_id}'

        return GroupAction([
            # Namespace for the robot
            Group(namespace=namespace),

            # Robot State Publisher for this robot
            Node(
                package='robot_bringup',
                executable='robot_state_publisher',
                output='screen',
                namespace=namespace,
                parameters=[{
                    'robot_description': robot_description_config,
                    'use_sim_time': use_sim_time
                }]
            )
        ])

    # Create robot groups for the specified number of robots
    robot_groups = [create_robot_group(i) for i in range(int(robot_count))]

    # Launch description
    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_count',
            default_value=1,
            description='Number of robots to spawn'
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation time'
        ),
        *robot_groups  # Add all robot groups to the launch description
    ])
