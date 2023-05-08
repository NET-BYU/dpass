# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

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
CMAKE_COMMAND = /usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jonbackman/srsRAN

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jonbackman/srsRAN/build

# Include any dependencies generated for this target.
include lib/examples/CMakeFiles/usrp_capture_sync.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include lib/examples/CMakeFiles/usrp_capture_sync.dir/compiler_depend.make

# Include the progress variables for this target.
include lib/examples/CMakeFiles/usrp_capture_sync.dir/progress.make

# Include the compile flags for this target's objects.
include lib/examples/CMakeFiles/usrp_capture_sync.dir/flags.make

lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o: lib/examples/CMakeFiles/usrp_capture_sync.dir/flags.make
lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o: ../lib/examples/usrp_capture_sync.c
lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o: lib/examples/CMakeFiles/usrp_capture_sync.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jonbackman/srsRAN/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o"
	cd /home/jonbackman/srsRAN/build/lib/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o -MF CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o.d -o CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o -c /home/jonbackman/srsRAN/lib/examples/usrp_capture_sync.c

lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.i"
	cd /home/jonbackman/srsRAN/build/lib/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/jonbackman/srsRAN/lib/examples/usrp_capture_sync.c > CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.i

lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.s"
	cd /home/jonbackman/srsRAN/build/lib/examples && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/jonbackman/srsRAN/lib/examples/usrp_capture_sync.c -o CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.s

# Object files for target usrp_capture_sync
usrp_capture_sync_OBJECTS = \
"CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o"

# External object files for target usrp_capture_sync
usrp_capture_sync_EXTERNAL_OBJECTS =

lib/examples/usrp_capture_sync: lib/examples/CMakeFiles/usrp_capture_sync.dir/usrp_capture_sync.c.o
lib/examples/usrp_capture_sync: lib/examples/CMakeFiles/usrp_capture_sync.dir/build.make
lib/examples/usrp_capture_sync: lib/src/phy/libsrsran_phy.a
lib/examples/usrp_capture_sync: lib/src/phy/rf/libsrsran_rf.so.22.04.0
lib/examples/usrp_capture_sync: lib/src/phy/rf/libsrsran_rf_utils.a
lib/examples/usrp_capture_sync: lib/src/phy/libsrsran_phy.a
lib/examples/usrp_capture_sync: /usr/lib/x86_64-linux-gnu/libfftw3f.so
lib/examples/usrp_capture_sync: lib/examples/CMakeFiles/usrp_capture_sync.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jonbackman/srsRAN/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable usrp_capture_sync"
	cd /home/jonbackman/srsRAN/build/lib/examples && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/usrp_capture_sync.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/examples/CMakeFiles/usrp_capture_sync.dir/build: lib/examples/usrp_capture_sync
.PHONY : lib/examples/CMakeFiles/usrp_capture_sync.dir/build

lib/examples/CMakeFiles/usrp_capture_sync.dir/clean:
	cd /home/jonbackman/srsRAN/build/lib/examples && $(CMAKE_COMMAND) -P CMakeFiles/usrp_capture_sync.dir/cmake_clean.cmake
.PHONY : lib/examples/CMakeFiles/usrp_capture_sync.dir/clean

lib/examples/CMakeFiles/usrp_capture_sync.dir/depend:
	cd /home/jonbackman/srsRAN/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jonbackman/srsRAN /home/jonbackman/srsRAN/lib/examples /home/jonbackman/srsRAN/build /home/jonbackman/srsRAN/build/lib/examples /home/jonbackman/srsRAN/build/lib/examples/CMakeFiles/usrp_capture_sync.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/examples/CMakeFiles/usrp_capture_sync.dir/depend
