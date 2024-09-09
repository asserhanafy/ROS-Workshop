#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class UltrasonicNode(Node):
    
    def __init__(self):
        super().__init__("ultrasonic_subscriber")
        self.pose_subscriber_ = self.create_subscription(
            int, "sensor_data", self.dist_callback, 10)

    def dist_callback(self, msg: int):
        if msg >= 10:
            self.get_logger().info("Too close!")
        if msg >= 20:
            self.get_logger().info("Close.")
        if msg >= 30:
            self.get_logger().info("Average.")
        if msg >= 40:
            self.get_logger().info("Far.")
        if msg >= 50:
            self.get_logger().info("Very Far!")
    
def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicNode()
    rclpy.spin(node)
    rclpy.shutdown()