#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
import tf2_ros
import serial
import math
import time

class OdometryNode(Node):
    def __init__(self):
        super().__init__('odometry_node')

        # Robot parameters
        self.wheel_radius = 0.0325  # meters
        self.wheel_base = 0.215     # meters
        self.ticks_per_rev = 1000   # Encoder ticks per wheel revolution
        self.m_per_tick = (2 * math.pi * self.wheel_radius) / self.ticks_per_rev

        # State variables
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        self.last_time = self.get_clock().now()

        # Serial port configuration
        self.serial_port = '/dev/ttyUSB0'  # Adjust to your Arduino's port
        self.baud_rate = 115200
        try:
            self.ser = serial.Serial(self.serial_port, self.baud_rate, timeout=1)
            self.get_logger().info(f"Connected to {self.serial_port}")
        except serial.SerialException as e:
            self.get_logger().error(f"Failed to connect to {self.serial_port}: {e}")
            return

        # Publishers
        self.odom_pub = self.create_publisher(Odometry, '/odom', 10)
        self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)

        # Timer to read serial and compute odometry (20 Hz, matching Arduino's 0.05s)
        self.timer = self.create_timer(0.05, self.update_odometry)

    def update_odometry(self):
        try:
            # Read serial data
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').strip()
                if ',' in line:
                    left_ticks, right_ticks = map(int, line.split(','))

                    # Compute distances
                    left_distance = left_ticks * self.m_per_tick
                    right_distance = right_ticks * self.m_per_tick

                    # Time delta
                    current_time = self.get_clock().now()
                    dt = (current_time - self.last_time).nanoseconds / 1e9  # seconds

                    # Compute velocities
                    v_left = left_distance / dt
                    v_right = right_distance / dt
                    v = (v_right + v_left) / 2.0
                    omega = (v_right - v_left) / self.wheel_base

                    # Update pose
                    self.x += v * math.cos(self.theta) * dt
                    self.y += v * math.sin(self.theta) * dt
                    self.theta += omega * dt

                    # Normalize theta to [-pi, pi]
                    self.theta = math.atan2(math.sin(self.theta), math.cos(self.theta))

                    # Create odometry message
                    odom = Odometry()
                    odom.header.stamp = current_time.to_msg()
                    odom.header.frame_id = 'odom'
                    odom.child_frame_id = 'origin_link'

                    # Set pose
                    odom.pose.pose.position.x = self.x
                    odom.pose.pose.position.y = self.y
                    odom.pose.pose.position.z = 0.0
                    odom.pose.pose.orientation.z = math.sin(self.theta / 2.0)
                    odom.pose.pose.orientation.w = math.cos(self.theta / 2.0)

                    # Set velocity
                    odom.twist.twist.linear.x = v
                    odom.twist.twist.angular.z = omega

                    # Set covariance (tune these values)
                    odom.pose.covariance = [
                        0.01, 0.0, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.01, 0.0, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.01, 0.0, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.01, 0.0, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.01, 0.0,
                        0.0, 0.0, 0.0, 0.0, 0.0, 0.01
                    ]
                    odom.twist.covariance = odom.pose.covariance

                    # Publish odometry
                    self.odom_pub.publish(odom)

                    # Broadcast transform
                    t = TransformStamped()
                    t.header.stamp = current_time.to_msg()
                    t.header.frame_id = 'odom'
                    t.child_frame_id = 'origin_link'
                    t.transform.translation.x = self.x
                    t.transform.translation.y = self.y
                    t.transform.translation.z = 0.0
                    t.transform.rotation = odom.pose.pose.orientation
                    self.tf_broadcaster.sendTransform(t)

                    print(self.x, self.y)

                    # Update last time
                    self.last_time = current_time

        except Exception as e:
            self.get_logger().error(f"Error processing serial data: {e}")

    def __del__(self):
        if hasattr(self, 'ser') and self.ser.is_open:
            self.ser.close()
            self.get_logger().info("Serial port closed")

def main(args=None):
    rclpy.init(args=args)
    node = OdometryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()