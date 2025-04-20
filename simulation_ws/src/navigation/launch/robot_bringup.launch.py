import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use sim time if true'
    )

    # Process the URDF file
    package_name = 'navigation'
    pkg_path = os.path.join(get_package_share_directory(package_name))
    xacro_file = os.path.join(pkg_path, 'description', 'swarm_bot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file)

     # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        # namespace="Robot0",
        executable='robot_state_publisher',
        output='screen',
        parameters=[params],
        arguments=['--ros-args', '--log-level', 'debug']
    )

    node_lidar_scan = Node(
        
        package='rplidar_ros',
        executable='rplidar_c1_launch',
        name='rplidar_node',
        output='screen',
        parameters=[{'serial_port': '/dev/ttyUSB0', 'frame_id': 'laser_frame'}]

    )

    node_joint_state = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    return LaunchDescription([
        declare_use_sim_time,
        node_robot_state_publisher,
        # node_lidar_scan,
        # node_joint_state,
    ])
