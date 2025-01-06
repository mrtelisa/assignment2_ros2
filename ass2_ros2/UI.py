#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

# Implementing the Publisher and the Subscriber

class OdomSub(Node):

    def __init__(self):
        super().__init__('odom_subscriber')

        # creating a publisher for the velocity and a subscriber to a message of "Odometry" type
        self.create_subscription(Odometry, 'odom', self.listener_callback, 10)
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)

    def listener_callback(self, msg: Odometry) -> None:
        vel: Twist = Twist()

        # setting the default velocity
        vel.linear.x = 1.0
        vel.angular.z = 0.0

        # making the robot turn
        if msg.pose.pose.position.x > 8.0:
            vel.linear.x = 0.9
            vel.angular.z = 1.2

        if msg.pose.pose.position.x < 2.0:
            vel.linear.x = 0.9
            vel.angular.z = -1.2
        
        # stopping the robot
        if msg.pose.pose.position.y > 9.0:
            vel.linear.x = 0.0
            vel.angular.z = 0.0

        # publishing the velocity
        self.pub.publish(vel)


def main(args = None):
    rclpy.init(args=args)

    # creating an object belonging to the OdomSub class
    odom_sub: OdomSub = OdomSub()
    rclpy.spin(odom_sub)
    
    # when the simulation is done, the node is destroyed and closed correctly (terminanting the client ROS2)
    odom_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()