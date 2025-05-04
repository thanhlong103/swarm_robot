from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Declare launch arguments
    robot_id_arg = DeclareLaunchArgument(
        'robot_id',
        default_value='1',
        description='ID of the robot for the odom_to_robot_odom and navigation_process nodes'
    )

    return LaunchDescription([
        robot_id_arg,
        # Launch odom_to_robot_odom node
        Node(
            package='slave',
            executable='odom_to_robot_odom',
            name='odom_to_robot_odom_node',
            output='screen',
            parameters=[
                {'robot_id': LaunchConfiguration('robot_id')}
            ]
        ),
        # Launch navigation_process node
        Node(
            package='slave',
            executable='navigation_process',
            name='navigation_process_node',
            output='screen',
            parameters=[
                {'robot_id': LaunchConfiguration('robot_id')}
            ]
        )
    ])