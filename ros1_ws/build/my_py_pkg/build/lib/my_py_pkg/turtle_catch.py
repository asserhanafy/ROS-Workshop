#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from turtlesim.srv import Spawn
from functools import partial
from random import uniform
import time

class main_turtle(Node):
    def __init__(self):
        super().__init__("Main_Turtle")
        self.main_turtle_pose_subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.main_turtle_pose_callback, 10)
        self.spawned_turtle_name = 'turtle2'
        self.spawned_turtle_pose = None
        self.spawned_turtle_pose_subscriber_ = self.create_subscription(Pose, '/turtle2/pose', self.spawned_turtle_pose_callback, 10)
        self.spawn_turtle(uniform(1.0, 10.0), uniform(1.0, 10.0), uniform(0.0, 3.14))
        self.get_logger().info("Turtle game has started")

    def main_turtle_pose_callback(self, msg):
        if self.spawned_turtle_pose is not None and self.is_touching(msg, self.spawned_turtle_pose):
            self.kill_turtle(self.spawned_turtle_name)
            time.sleep(2)
            self.spawn_turtle(uniform(1.0, 10.0), uniform(1.0, 10.0), uniform(0.0, 3.14))

    def is_touching(self, main_pose, turtle_pose, threshold = 0.5):
        distance = ((main_pose.x - turtle_pose.x) ** 2 + (main_pose.y - turtle_pose.y) ** 2) ** 0.5
        return distance < threshold
    
    def spawned_turtle_pose_callback(self, msg):
        self.spawned_turtle_pose = msg

    def spawn_turtle(self, x, y, theta):
        client = self.create_client(Spawn, "/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")

        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = self.spawned_turtle_name

        future = client.call_async(request)
        future.add_done_callback(partial(self.spawn_callback))

    def spawn_callback(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed:  %r" % (e,))
    
        

    def kill_turtle(self, name):
        client = self.create_client(Kill, "/kill")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service...")

        request = Kill.Request()
        request.name = name
    
        future = client.call_async(request)
        future.add_done_callback(partial(self.kill_callback))

    def kill_callback(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed:  %r" % (e,))
        

def main(args = None):
    rclpy.init(args = args)
    node = main_turtle()
    rclpy.spin(node)
    rclpy.shutdown()