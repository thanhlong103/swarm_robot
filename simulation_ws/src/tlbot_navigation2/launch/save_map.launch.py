import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Define the map directory
    map_dir = os.path.join(
        get_package_share_directory('tlbot_navigation2'),
        'map')
    
    # Make sure the directory exists
    os.makedirs(map_dir, exist_ok=True)
    
    # Create a process to save the map
    save_map_process = ExecuteProcess(
        cmd=['ros2', 'run', 'nav2_map_server', 'map_saver_cli', 
             '-f', os.path.join(map_dir, 'simmap')],
        output='screen'
    )
    
    return LaunchDescription([
        save_map_process
    ])