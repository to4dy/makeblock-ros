cmake_minimum_required(VERSION 2.8.3)
project(makeblock_ros)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_python_setup()

catkin_package(
)

catkin_install_python(PROGRAMS nodes/makeblock_ros_ultrasensor.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
