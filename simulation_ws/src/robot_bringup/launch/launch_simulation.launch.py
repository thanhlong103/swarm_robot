import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, OpaqueFunction, GroupAction
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():

    # Launch arguments
    robot_count = LaunchConfiguration('robot_count', default='1')  # Number of robots
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')  # Sim time

    # Package name
    package_name = 'robot_bringup'  # Change to your package name

    # Function to create a GroupAction for each robot
    def create_robot_group(robot_id):
        namespace = f'robot_{robot_id}'
        robot_name = f'robot_{robot_id}'

        # Include the robot_state_publisher launch file
        rsp = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(get_package_share_directory(package_name), 'launch', 'robot_state_publisher.launch.py')]
            ),
            launch_arguments={'use_sim_time': use_sim_time, 'namespace': namespace}.items(),
        )

        # Run the spawner node for this robot
        spawn_entity = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=[
                '-topic', f'/{namespace}/robot_description',
                '-entity', robot_name,
                '-robot_namespace', namespace,
            ],
            output='screen',
        )

        return GroupAction([
            rsp,
            spawn_entity,
        ])

    # Function to dynamically create robot groups at runtime
    def create_robot_groups(context):
        robot_count_value = int(context.perform_substitution(robot_count))
        return [create_robot_group(i) for i in range(robot_count_value)]

    # Include the Gazebo launch file
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]
        ),
        launch_arguments={'use_sim_time': use_sim_time}.items(),
    )

    # Launch description
    return LaunchDescription([
        DeclareLaunchArgument('robot_count', default_value='1', description='Number of robots to spawn'),
        DeclareLaunchArgument('use_sim_time', default_value='true', description='Use simulation time'),
        gazebo,
        OpaqueFunction(function=create_robot_groups),
    ])
