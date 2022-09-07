from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
import sys
from launch.actions import OpaqueFunction
import launch


def launch_setup(context, *args, **kwargs):
    param = launch.substitutions.LaunchConfiguration("turtlesim_ns").perform(context)
    print(param)

    turtlesim_node = Node(
        package="demo_nodes_cpp",
        executable="talker",
        name="sim_talker",
    )

    return [turtlesim_node]


def generate_launch_description():
    turtlesim_ns_launch_arg = DeclareLaunchArgument(
        "turtlesim_ns", default_value="turtlesim1"
    )

    # for arg in sys.argv:
    #     if arg.startswith("turtlesim_ns:="):
    #         turtlesim_ns = arg.split(":=")[1]
    #         print(turtlesim_ns)

    return LaunchDescription(
        [turtlesim_ns_launch_arg, OpaqueFunction(function=launch_setup)]
    )
