# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/chrellep/ROS_workspaces/mavros_lecture_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/chrellep/ROS_workspaces/mavros_lecture_ws/build

# Include any dependencies generated for this target.
include mavros/libmavconn/CMakeFiles/mavconn-test.dir/depend.make

# Include the progress variables for this target.
include mavros/libmavconn/CMakeFiles/mavconn-test.dir/progress.make

# Include the compile flags for this target's objects.
include mavros/libmavconn/CMakeFiles/mavconn-test.dir/flags.make

mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o: mavros/libmavconn/CMakeFiles/mavconn-test.dir/flags.make
mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o: /home/chrellep/ROS_workspaces/mavros_lecture_ws/src/mavros/libmavconn/test/test_mavconn.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/chrellep/ROS_workspaces/mavros_lecture_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o"
	cd /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o -c /home/chrellep/ROS_workspaces/mavros_lecture_ws/src/mavros/libmavconn/test/test_mavconn.cpp

mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.i"
	cd /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/chrellep/ROS_workspaces/mavros_lecture_ws/src/mavros/libmavconn/test/test_mavconn.cpp > CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.i

mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.s"
	cd /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/chrellep/ROS_workspaces/mavros_lecture_ws/src/mavros/libmavconn/test/test_mavconn.cpp -o CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.s

mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.requires:

.PHONY : mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.requires

mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.provides: mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.requires
	$(MAKE) -f mavros/libmavconn/CMakeFiles/mavconn-test.dir/build.make mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.provides.build
.PHONY : mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.provides

mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.provides.build: mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o


# Object files for target mavconn-test
mavconn__test_OBJECTS = \
"CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o"

# External object files for target mavconn-test
mavconn__test_EXTERNAL_OBJECTS =

/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o
/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: mavros/libmavconn/CMakeFiles/mavconn-test.dir/build.make
/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: gtest/libgtest.so
/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: /home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn.so
/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test: mavros/libmavconn/CMakeFiles/mavconn-test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/chrellep/ROS_workspaces/mavros_lecture_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test"
	cd /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mavconn-test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
mavros/libmavconn/CMakeFiles/mavconn-test.dir/build: /home/chrellep/ROS_workspaces/mavros_lecture_ws/devel/lib/libmavconn/mavconn-test

.PHONY : mavros/libmavconn/CMakeFiles/mavconn-test.dir/build

mavros/libmavconn/CMakeFiles/mavconn-test.dir/requires: mavros/libmavconn/CMakeFiles/mavconn-test.dir/test/test_mavconn.cpp.o.requires

.PHONY : mavros/libmavconn/CMakeFiles/mavconn-test.dir/requires

mavros/libmavconn/CMakeFiles/mavconn-test.dir/clean:
	cd /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn && $(CMAKE_COMMAND) -P CMakeFiles/mavconn-test.dir/cmake_clean.cmake
.PHONY : mavros/libmavconn/CMakeFiles/mavconn-test.dir/clean

mavros/libmavconn/CMakeFiles/mavconn-test.dir/depend:
	cd /home/chrellep/ROS_workspaces/mavros_lecture_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/chrellep/ROS_workspaces/mavros_lecture_ws/src /home/chrellep/ROS_workspaces/mavros_lecture_ws/src/mavros/libmavconn /home/chrellep/ROS_workspaces/mavros_lecture_ws/build /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn /home/chrellep/ROS_workspaces/mavros_lecture_ws/build/mavros/libmavconn/CMakeFiles/mavconn-test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : mavros/libmavconn/CMakeFiles/mavconn-test.dir/depend

