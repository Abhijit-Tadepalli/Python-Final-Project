#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from moveit_commander import MoveGroupCommander, RobotCommander, PlanningSceneInterface
from geometry_msgs.msg import Pose

class UR5Controller(Node):
    def __init__(self):
        super().__init__('ur5_command_controller')
        self.robot = RobotCommander()
        self.scene = PlanningSceneInterface()
        self.group = MoveGroupCommander("ur_manipulator")
        self.group.set_max_velocity_scaling_factor(0.5)
        self.group.set_max_acceleration_scaling_factor(0.5)
        self.get_logger().info("UR5 MoveIt Controller Initialized")

    def move_by_command(self, command):
        pose = self.group.get_current_pose().pose

        if "forward" in command:
            pose.position.x += 0.05
        elif "backward" in command:
            pose.position.x -= 0.05
        elif "left" in command:
            pose.position.y += 0.05
        elif "right" in command:
            pose.position.y -= 0.05
        elif "up" in command:
            pose.position.z += 0.05
        elif "down" in command:
            pose.position.z -= 0.05
        else:
            self.get_logger().warn("Unknown command.")
            return

        self.group.set_pose_target(pose)
        success = self.group.go(wait=True)
        self.group.stop()
        self.group.clear_pose_targets()

        if success:
            self.get_logger().info(f"Moved: {command}")
        else:
            self.get_logger().warn("Motion failed.")

def main(args=None):
    rclpy.init(args=args)
    controller = UR5Controller()

    try:
        while rclpy.ok():
            command = input("Enter command (e.g., forward, up, left): ")
            controller.move_by_command(command)
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down.")
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()

