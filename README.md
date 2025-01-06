# Assignment 2 ROS2

This repository contains the 2nd part (regarding ROS2) of the 2nd assignment of the Research Track 1 course.

## Description
The goal of the project was to create a node which makes the robot move in the Gazebo environment. The code that controls the movement is written in the UI file. The velocity and the positions are updated thanks to a publisher that publishes the velocity of the robot continuosly.

## Prerequisits

- ROS2 Foxy
- Colcon workspace
- Run the following commands:
    ```bash
    apt-get update
    apt-get upgrade
    apt-get install ros-foxy-xacro  ros-foxy-joint-state-publisher ros-foxy-gazebo*
    ```
- Clone the following repository in the workspace of  your project:

    ```bash
    git clone https://github.com/CarmineD8/robot_urdf 
    ```
    Then switch to the ROS2 branch, entering in the repository and executing:

    ```bash
    git switch ros2
    ```
- Clone also this repository in the workspace.

## Usage

1. **Launching the simulation environment**:

    ```bash
    ros2 launch robot_urdf gazebo.launch.py
    ```
    
2. **Launching the UI_node**
    After gazebo is open and the robot is spawned in the environment in the (2,2) position, run the following command:
    
    ```bash
    ros2 run assignment2_ros2 UI_node
    ```


