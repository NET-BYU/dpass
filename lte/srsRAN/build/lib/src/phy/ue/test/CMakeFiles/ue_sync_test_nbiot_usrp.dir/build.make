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
include lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/compiler_depend.make

# Include the progress variables for this target.
include lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/progress.make

# Include the compile flags for this target's objects.
include lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/flags.make

lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o: lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/flags.make
lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o: ../lib/src/phy/ue/test/ue_sync_test_nbiot_usrp.c
lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o: lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jonbackman/srsRAN/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/ue/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o -MF CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o.d -o CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o -c /home/jonbackman/srsRAN/lib/src/phy/ue/test/ue_sync_test_nbiot_usrp.c

lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.i"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/ue/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/jonbackman/srsRAN/lib/src/phy/ue/test/ue_sync_test_nbiot_usrp.c > CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.i

lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.s"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/ue/test && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/jonbackman/srsRAN/lib/src/phy/ue/test/ue_sync_test_nbiot_usrp.c -o CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.s

# Object files for target ue_sync_test_nbiot_usrp
ue_sync_test_nbiot_usrp_OBJECTS = \
"CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o"

# External object files for target ue_sync_test_nbiot_usrp
ue_sync_test_nbiot_usrp_EXTERNAL_OBJECTS =

lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/ue_sync_test_nbiot_usrp.c.o
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/build.make
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/rf/libsrsran_rf.so.22.04.0
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/libsrsran_phy.a
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/rf/libsrsran_rf_utils.a
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/libsrsran_phy.a
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: /usr/lib/x86_64-linux-gnu/libfftw3f.so
lib/src/phy/ue/test/ue_sync_test_nbiot_usrp: lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jonbackman/srsRAN/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable ue_sync_test_nbiot_usrp"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/ue/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/ue_sync_test_nbiot_usrp.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/build: lib/src/phy/ue/test/ue_sync_test_nbiot_usrp
.PHONY : lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/build

lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/clean:
	cd /home/jonbackman/srsRAN/build/lib/src/phy/ue/test && $(CMAKE_COMMAND) -P CMakeFiles/ue_sync_test_nbiot_usrp.dir/cmake_clean.cmake
.PHONY : lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/clean

lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/depend:
	cd /home/jonbackman/srsRAN/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jonbackman/srsRAN /home/jonbackman/srsRAN/lib/src/phy/ue/test /home/jonbackman/srsRAN/build /home/jonbackman/srsRAN/build/lib/src/phy/ue/test /home/jonbackman/srsRAN/build/lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/src/phy/ue/test/CMakeFiles/ue_sync_test_nbiot_usrp.dir/depend

