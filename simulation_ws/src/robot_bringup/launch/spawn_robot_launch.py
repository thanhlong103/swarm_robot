from launch import LaunchDescription
import launch.actions
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory
import xacro


def generate_launch_description():
    # Define robot parameters
    robot_urdf_path = launch.substitutions.LaunchConfiguration('robot_urdf')
    robot_name = launch.substitutions.LaunchConfiguration('robot_name')
    robot_namespace = launch.substitutions.LaunchConfiguration('robot_namespace')
    x = launch.substitutions.LaunchConfiguration('x')
    y = launch.substitutions.LaunchConfiguration('y')
    z = launch.substitutions.LaunchConfiguration('z')

    # Process the URDF file using xacro
    pkg_path = os.path.join(get_package_share_directory('robot_bringup'))
    xacro_file = os.path.join(pkg_path, 'descriptions', 'robot.urdf.xacro')
    robot_description_config = xacro.process_file(xacro_file).toxml()

    # Robot State Publisher node
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        namespace=robot_namespace,  # Unique namespace for each robot
        parameters=[{'robot_description': robot_description_config}]
    )


    # Spawn Robot node
    spawn_robot_node = launch_ros.actions.Node(
        package='robot_bringup',
        executable='spawn_robot.py',
        output='screen',
        arguments=[
            '--robot_urdf', robot_urdf_path,
            '--robot_name', robot_name,
            '--robot_namespace', robot_namespace,
            '-x', x,
            '-y', y,
            '-z', z
        ]
    )

    return LaunchDescription([
        # Declare parameters
        launch.actions.DeclareLaunchArgument('robot_urdf', description='Path to robot URDF file'),
        launch.actions.DeclareLaunchArgument('robot_name', description='Name of the robot'),
        launch.actions.DeclareLaunchArgument('robot_namespace', description='Namespace of the robot'),
        launch.actions.DeclareLaunchArgument('x', default_value='0.0', description='Initial x position'),
        launch.actions.DeclareLaunchArgument('y', default_value='0.0', description='Initial y position'),
        launch.actions.DeclareLaunchArgument('z', default_value='0.0', description='Initial z position'),

        # Nodes
        robot_state_publisher_node,
        spawn_robot_node
    ])
