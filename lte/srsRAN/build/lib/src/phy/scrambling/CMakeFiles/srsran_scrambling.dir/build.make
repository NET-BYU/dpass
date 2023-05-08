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
include lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/compiler_depend.make

# Include the progress variables for this target.
include lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/progress.make

# Include the compile flags for this target's objects.
include lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/flags.make

lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.o: lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/flags.make
lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.o: ../lib/src/phy/scrambling/scrambling.c
lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.o: lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jonbackman/srsRAN/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.o"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/scrambling && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.o -MF CMakeFiles/srsran_scrambling.dir/scrambling.c.o.d -o CMakeFiles/srsran_scrambling.dir/scrambling.c.o -c /home/jonbackman/srsRAN/lib/src/phy/scrambling/scrambling.c

lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/srsran_scrambling.dir/scrambling.c.i"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/scrambling && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/jonbackman/srsRAN/lib/src/phy/scrambling/scrambling.c > CMakeFiles/srsran_scrambling.dir/scrambling.c.i

lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/srsran_scrambling.dir/scrambling.c.s"
	cd /home/jonbackman/srsRAN/build/lib/src/phy/scrambling && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/jonbackman/srsRAN/lib/src/phy/scrambling/scrambling.c -o CMakeFiles/srsran_scrambling.dir/scrambling.c.s

srsran_scrambling: lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/scrambling.c.o
srsran_scrambling: lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/build.make
.PHONY : srsran_scrambling

# Rule to build all files generated by this target.
lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/build: srsran_scrambling
.PHONY : lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/build

lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/clean:
	cd /home/jonbackman/srsRAN/build/lib/src/phy/scrambling && $(CMAKE_COMMAND) -P CMakeFiles/srsran_scrambling.dir/cmake_clean.cmake
.PHONY : lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/clean

lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/depend:
	cd /home/jonbackman/srsRAN/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jonbackman/srsRAN /home/jonbackman/srsRAN/lib/src/phy/scrambling /home/jonbackman/srsRAN/build /home/jonbackman/srsRAN/build/lib/src/phy/scrambling /home/jonbackman/srsRAN/build/lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/src/phy/scrambling/CMakeFiles/srsran_scrambling.dir/depend

