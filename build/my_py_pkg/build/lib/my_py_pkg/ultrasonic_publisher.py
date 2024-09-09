#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
distance = [10, 20, 30, 40, 50]
i = 0

class UltrasonicNode(Node):
    def __init__(self):
        super().__init__("ultrasonic_publisher")
        self.dist_pub_ = self.create_publisher(int, "sensor_data", 10)
        self.timer_ = self.create_timer(0.5, self.send_dist_command)
        self.get_logger().info("Ultrasonic publisher node has been started")

    def send_dist_command(self):
        msg = distance[i]
        self.dist_pub_.publish(distance[i] % 5)
        i += 1

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicNode()
    rclpy.spin(node)
    rclpy.shutdown()