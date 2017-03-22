execute_process(COMMAND "/home/chrellep/ROS_workspaces/mavros_lecture_ws/build/MarkerLocator/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/chrellep/ROS_workspaces/mavros_lecture_ws/build/MarkerLocator/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
