import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Launch configuration variables
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    map_dir = LaunchConfiguration(
        'map',
        default=os.path.join(
            get_package_share_directory('tlbot_navigation2'),
            'map',
            'simumap.yaml'))

    param_file_name = 'tlbot.yaml'
    param_dir = LaunchConfiguration(
        'params_file',
        default=os.path.join(
            get_package_share_directory('tlbot_navigation2'),
            'param',
            param_file_name))

    nav2_launch_file_dir = os.path.join(get_package_share_directory('nav2_bringup'), 'launch')

    rviz_config_dir = os.path.join(
        get_package_share_directory('nav2_bringup'),
        'rviz',
        'nav2_default_view.rviz')

    return LaunchDescription([
        # Declare launch arguments
        DeclareLaunchArgument(
            'map',
            default_value=map_dir,
            description='Full path to map YAML file to load'),

        DeclareLaunchArgument(
            'params_file',
            default_value=param_dir,
            description='Full path to parameter file to load'),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        # Include the Nav2 bringup launch file with remapping for /Robot0/cmd_vel
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/bringup_launch.py']),
            launch_arguments={
                'map': map_dir,
                'use_sim_time': use_sim_time,
                'params_file': param_dir,
            }.items(),
            # Remap the cmd_vel topic to /Robot0/cmd_vel
            remappings=[('/cmd_vel', '/Robot0/cmd_vel')],
        ),

        # Static transform publisher: map -> base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='map_to_base_link',
            arguments=['0', '0', '0', '0', '0', '0', 'map', 'base_link'],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen',
        ),

        # Static transform publisher: base_link -> odom
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_odom',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'odom'],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen',
        ),

        # RViz2 node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen',
        ),
    ])