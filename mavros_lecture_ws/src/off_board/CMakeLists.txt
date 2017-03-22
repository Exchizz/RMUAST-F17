cmake_minimum_required(VERSION 2.8.3)
project(off_board)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  genmsg
  cv_bridge
  image_transport
  sensor_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(off_board_node src/off_board_node.cpp)
target_link_libraries(${PROJECT_NAME}_node
  ${catkin_LIBRARIES}
 )
