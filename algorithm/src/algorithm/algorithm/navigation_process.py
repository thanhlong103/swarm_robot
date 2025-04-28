#!/usr/bin/env python

import rclpy
from rclpy.node import Node
from communication_msgs.msg import Robot, TaskAllocationArray, TaskAllocation, Task
from nav_msgs.msg import Path, Odometry
from geometry_msgs.msg import PoseStamped, Point, Quaternion
from std_msgs.msg import Header
import tf_transformations  # For quaternion to Euler conversion
import math

class NavigationProcessNode(Node):
    def __init__(self):
        super().__init__('navigation_process_node')
        
        # Declare parameter for robot_id
        self.declare_parameter('robot_id', 0)
        self.robot_id = self.get_parameter('robot_id').get_parameter_value().integer_value
        
        # Initialize storage
        self.tasks = {}  # Dictionary to store task data: {task_id: (pickup_x, pickup_y, dropoff_x, dropoff_y, available)}
        self.current_pose = None  # Store latest odometry: (x, y, theta)
        
        # Subscribers
        self.alloc_sub = self.create_subscription(
            TaskAllocationArray,
            '/task_allocations',
            self.task_allocation_callback,
            10
        )
        self.task_sub = self.create_subscription(
            Task,
            '/task_locations',
            self.task_location_callback,
            10
        )
        self.odom_sub = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        
        # Publishers
        self.robot_status_pub = self.create_publisher(
            Robot,
            '/robot_status',
            10
        )
        self.waypoints_pub = self.create_publisher(
            Path,
            '/waypoints',
            10
        )
        
        self.get_logger().info(f'Navigation Process Node started for Robot {self.robot_id}')
    
    def odom_callback(self, msg):
        """Store the robot's current position and orientation from odometry."""
        try:
            x = msg.pose.pose.position.x
            y = msg.pose.pose.position.y
            # Convert quaternion to Euler angles (yaw = theta)
            quaternion = (
                msg.pose.pose.orientation.x,
                msg.pose.pose.orientation.y,
                msg.pose.pose.orientation.z,
                msg.pose.pose.orientation.w
            )
            _, _, theta = tf_transformations.euler_from_quaternion(quaternion)
            self.current_pose = (x, y, theta)
            self.get_logger().debug(f'Robot {self.robot_id} odometry: x={x:.2f}, y={y:.2f}, theta={theta:.2f}')
        except Exception as e:
            self.get_logger().error(f'Error processing odometry: {e}')

    def task_location_callback(self, msg):
        """Store task data from /task_locations."""
        self.tasks[msg.task_id] = {
            'pickup_x': msg.pickup_x,
            'pickup_y': msg.pickup_y,
            'dropoff_x': msg.dropoff_x,
            'dropoff_y': msg.dropoff_y,
            'available': msg.available
        }
        self.get_logger().debug(f'Task {msg.task_id} updated: pickup=({msg.pickup_x}, {msg.pickup_y}), '
                               f'dropoff=({msg.dropoff_x}, {msg.dropoff_y}), available={msg.available}')

    def task_allocation_callback(self, msg):
        """Process task allocations and publish waypoints if assigned to this robot."""
        for allocation in msg.tasks:
            if allocation.robot_id == self.robot_id and allocation.task_ids:
                self.get_logger().info(f'Received task allocation for Robot {self.robot_id}: Tasks {allocation.task_ids}')
                
                # Update robot status to unavailable
                robot_status = Robot()
                robot_status.robot_id = self.robot_id
                robot_status.available = False
                
                # Use current pose if available, else default to (0, 0)
                if self.current_pose:
                    robot_status.x, robot_status.y = self.current_pose[0], self.current_pose[1]
                else:
                    robot_status.x, robot_status.y = 0.0, 0.0
                    self.get_logger().warn(f'No odometry data for Robot {self.robot_id}, using default position (0, 0)')
                
                try:
                    self.robot_status_pub.publish(robot_status)
                    self.get_logger().info(f'Robot {self.robot_id} set to unavailable')
                except Exception as e:
                    self.get_logger().error(f'Error publishing robot status: {e}')
                    continue
                
                # Create waypoints from task list
                path = Path()
                path.header = Header()
                path.header.stamp = self.get_clock().now().to_msg()
                path.header.frame_id = 'map'
                
                # Get current orientation for waypoints
                theta = self.current_pose[2] if self.current_pose else 0.0
                
                for task_id in allocation.task_ids:
                    task = self.tasks.get(task_id)
                    if not task:
                        self.get_logger().warn(f'Task {task_id} not found in task storage')
                        continue
                    
                    # Pickup waypoint
                    pickup_pose = PoseStamped()
                    pickup_pose.header = path.header
                    pickup_pose.pose.position = Point(x=task['pickup_x'], y=task['pickup_y'], z=0.0)
                    pickup_pose.pose.orientation = self.angle_to_quaternion(theta)
                    path.poses.append(pickup_pose)
                    
                    # Dropoff waypoint
                    dropoff_pose = PoseStamped()
                    dropoff_pose.header = path.header
                    dropoff_pose.pose.position = Point(x=task['dropoff_x'], y=task['dropoff_y'], z=0.0)
                    dropoff_pose.pose.orientation = self.angle_to_quaternion(theta)
                    path.poses.append(dropoff_pose)
                
                if path.poses:
                    try:
                        self.waypoints_pub.publish(path)
                        self.get_logger().info(f'Published {len(path.poses)} waypoints for Robot {self.robot_id}')
                    except Exception as e:
                        self.get_logger().error(f'Error publishing waypoints: {e}')
                else:
                    self.get_logger().warn(f'No valid waypoints generated for Robot {self.robot_id}')

                # Placeholder for future task completion logic
                # Example: Monitor robot position and mark tasks as completed
                # self.monitor_task_completion(allocation.task_ids)

    def angle_to_quaternion(self, yaw):
        """Convert yaw angle (theta) to quaternion."""
        quaternion = tf_transformations.quaternion_from_euler(0, 0, yaw)
        return Quaternion(x=quaternion[0], y=quaternion[1], z=quaternion[2], w=quaternion[3])

    def monitor_task_completion(self, task_ids):
        """Placeholder for future task completion logic."""
        # Future development: Monitor robot position via /odom and check proximity to waypoints
        # Update task availability and robot status when tasks are completed
        self.get_logger().debug(f'Monitoring tasks {task_ids} (not implemented)')
        pass

def main():
    rclpy.init()
    node = NavigationProcessNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Shutting down Navigation Process Node')
    except Exception as e:
        node.get_logger().error(f'Unexpected error: {e}')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()