# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "markerlocator: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imarkerlocator:/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(markerlocator_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" NAME_WE)
add_custom_target(_markerlocator_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "markerlocator" "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(markerlocator
  "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/markerlocator
)

### Generating Services

### Generating Module File
_generate_module_cpp(markerlocator
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/markerlocator
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(markerlocator_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(markerlocator_generate_messages markerlocator_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" NAME_WE)
add_dependencies(markerlocator_generate_messages_cpp _markerlocator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(markerlocator_gencpp)
add_dependencies(markerlocator_gencpp markerlocator_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS markerlocator_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(markerlocator
  "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/markerlocator
)

### Generating Services

### Generating Module File
_generate_module_eus(markerlocator
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/markerlocator
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(markerlocator_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(markerlocator_generate_messages markerlocator_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" NAME_WE)
add_dependencies(markerlocator_generate_messages_eus _markerlocator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(markerlocator_geneus)
add_dependencies(markerlocator_geneus markerlocator_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS markerlocator_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(markerlocator
  "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/markerlocator
)

### Generating Services

### Generating Module File
_generate_module_lisp(markerlocator
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/markerlocator
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(markerlocator_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(markerlocator_generate_messages markerlocator_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" NAME_WE)
add_dependencies(markerlocator_generate_messages_lisp _markerlocator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(markerlocator_genlisp)
add_dependencies(markerlocator_genlisp markerlocator_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS markerlocator_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(markerlocator
  "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/markerlocator
)

### Generating Services

### Generating Module File
_generate_module_nodejs(markerlocator
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/markerlocator
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(markerlocator_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(markerlocator_generate_messages markerlocator_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" NAME_WE)
add_dependencies(markerlocator_generate_messages_nodejs _markerlocator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(markerlocator_gennodejs)
add_dependencies(markerlocator_gennodejs markerlocator_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS markerlocator_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(markerlocator
  "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/markerlocator
)

### Generating Services

### Generating Module File
_generate_module_py(markerlocator
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/markerlocator
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(markerlocator_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(markerlocator_generate_messages markerlocator_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chrellep/ROS_workspaces/mavros_lecture_ws/src/MarkerLocator/msg/markerpose.msg" NAME_WE)
add_dependencies(markerlocator_generate_messages_py _markerlocator_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(markerlocator_genpy)
add_dependencies(markerlocator_genpy markerlocator_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS markerlocator_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/markerlocator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/markerlocator
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(markerlocator_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/markerlocator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/markerlocator
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(markerlocator_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/markerlocator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/markerlocator
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(markerlocator_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/markerlocator)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/markerlocator
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(markerlocator_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/markerlocator)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/markerlocator\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/markerlocator
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(markerlocator_generate_messages_py std_msgs_generate_messages_py)
endif()
