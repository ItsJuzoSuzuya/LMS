# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 4.0

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /bin/cmake

# The command to remove a file.
RM = /bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/nick/LMS/notify

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/nick/LMS/notify/build

# Include any dependencies generated for this target.
include CMakeFiles/MyNotificationServer.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/MyNotificationServer.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/MyNotificationServer.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MyNotificationServer.dir/flags.make

CMakeFiles/MyNotificationServer.dir/codegen:
.PHONY : CMakeFiles/MyNotificationServer.dir/codegen

CMakeFiles/MyNotificationServer.dir/main.cpp.o: CMakeFiles/MyNotificationServer.dir/flags.make
CMakeFiles/MyNotificationServer.dir/main.cpp.o: /home/nick/LMS/notify/main.cpp
CMakeFiles/MyNotificationServer.dir/main.cpp.o: CMakeFiles/MyNotificationServer.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/nick/LMS/notify/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MyNotificationServer.dir/main.cpp.o"
	/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/MyNotificationServer.dir/main.cpp.o -MF CMakeFiles/MyNotificationServer.dir/main.cpp.o.d -o CMakeFiles/MyNotificationServer.dir/main.cpp.o -c /home/nick/LMS/notify/main.cpp

CMakeFiles/MyNotificationServer.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/MyNotificationServer.dir/main.cpp.i"
	/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/nick/LMS/notify/main.cpp > CMakeFiles/MyNotificationServer.dir/main.cpp.i

CMakeFiles/MyNotificationServer.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/MyNotificationServer.dir/main.cpp.s"
	/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/nick/LMS/notify/main.cpp -o CMakeFiles/MyNotificationServer.dir/main.cpp.s

# Object files for target MyNotificationServer
MyNotificationServer_OBJECTS = \
"CMakeFiles/MyNotificationServer.dir/main.cpp.o"

# External object files for target MyNotificationServer
MyNotificationServer_EXTERNAL_OBJECTS =

/home/nick/LMS/notify/MyNotificationServer: CMakeFiles/MyNotificationServer.dir/main.cpp.o
/home/nick/LMS/notify/MyNotificationServer: CMakeFiles/MyNotificationServer.dir/build.make
/home/nick/LMS/notify/MyNotificationServer: CMakeFiles/MyNotificationServer.dir/compiler_depend.ts
/home/nick/LMS/notify/MyNotificationServer: /usr/lib/libpq.so
/home/nick/LMS/notify/MyNotificationServer: CMakeFiles/MyNotificationServer.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/nick/LMS/notify/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/nick/LMS/notify/MyNotificationServer"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MyNotificationServer.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MyNotificationServer.dir/build: /home/nick/LMS/notify/MyNotificationServer
.PHONY : CMakeFiles/MyNotificationServer.dir/build

CMakeFiles/MyNotificationServer.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MyNotificationServer.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MyNotificationServer.dir/clean

CMakeFiles/MyNotificationServer.dir/depend:
	cd /home/nick/LMS/notify/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/nick/LMS/notify /home/nick/LMS/notify /home/nick/LMS/notify/build /home/nick/LMS/notify/build /home/nick/LMS/notify/build/CMakeFiles/MyNotificationServer.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/MyNotificationServer.dir/depend

