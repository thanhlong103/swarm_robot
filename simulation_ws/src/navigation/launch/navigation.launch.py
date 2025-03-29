import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Configurations
    use_sim_time = LaunchConfiguration("use_sim_time", default="false")
    
    # Get directories of existing packages
    cartographer_dir = get_package_share_directory("cartographer")
    nav2_dir = get_package_share_directory("tlbot_navigation2")

    # Paths to required files
    cartographer_launch = os.path.join(cartographer_dir, "launch", "cartographer.launch.py")
    occupancy_grid_launch = os.path.join(cartographer_dir, "launch", "occupancy_grid.launch.py")
    nav2_launch = os.path.join(nav2_dir, "launch", "navigation2.launch.py")

    return LaunchDescription([
        DeclareLaunchArgument("use_sim_time", default_value="false", description="Use simulation clock if true"),

        # Start Cartographer (for mapping)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(cartographer_launch),
            launch_arguments={"use_sim_time": use_sim_time}.items(),
        ),

        # Start Occupancy Grid Node (to publish the map)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(occupancy_grid_launch),
            launch_arguments={"use_sim_time": use_sim_time}.items(),
        ),

        # Start Navigation (using the generated map)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch),
            launch_arguments={"use_sim_time": use_sim_time}.items(),
        ),
    ])
