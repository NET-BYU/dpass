# CMake generated Testfile for 
# Source directory: /home/jonbackman/srsRAN/lib/examples/test
# Build directory: /home/jonbackman/srsRAN/build/lib/examples/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(enb1 "/usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake" "-DCMD=/home/jonbackman/srsRAN/build/lib/examples/npdsch_enodeb" "-DARG=-o;/tmp/enbtest1.bin;-n;512;-t;2" "-V" "-P" "/home/jonbackman/srsRAN/lib/examples/test/iqtests.cmake")
set_tests_properties(enb1 PROPERTIES  _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;32;add_test;/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;0;")
add_test(npdsch_npdcch_file1 "/usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake" "-DCMD=/home/jonbackman/srsRAN/build/lib/src/phy/phch/test/npdsch_npdcch_file_test" "-DARG=-i;/tmp/enbtest1.bin;-m;512;-t;2;-w;0;-k" "-V" "-P" "/home/jonbackman/srsRAN/lib/examples/test/iqtests.cmake")
set_tests_properties(npdsch_npdcch_file1 PROPERTIES  DEPENDS "enb1" PASS_REGULAR_EXPRESSION "pkt_ok=1" _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;39;add_test;/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;0;")
add_test(npdsch_npdcch_file2 "/usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake" "-DCMD=/home/jonbackman/srsRAN/build/lib/src/phy/phch/test/npdsch_npdcch_file_test" "-DARG=-i;/tmp/enbtest1.bin;-m;512;-t;2;-w;0;-r;0x1234" "-V" "-P" "/home/jonbackman/srsRAN/lib/examples/test/iqtests.cmake")
set_tests_properties(npdsch_npdcch_file2 PROPERTIES  DEPENDS "enb1" PASS_REGULAR_EXPRESSION "pkt_ok=512" _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;48;add_test;/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;0;")
add_test(enb2 "/usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake" "-DCMD=/home/jonbackman/srsRAN/build/lib/examples/npdsch_enodeb" "-DARG=-o;/tmp/enbtest2.bin;-n;10;-t;0;-i;1;-m;4;-r;2" "-V" "-P" "/home/jonbackman/srsRAN/lib/examples/test/iqtests.cmake")
set_tests_properties(enb2 PROPERTIES  _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;64;add_test;/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;0;")
add_test(npdsch_npdcch_file3 "/usr/local/lib/python3.8/dist-packages/cmake/data/bin/cmake" "-DCMD=/home/jonbackman/srsRAN/build/lib/src/phy/phch/test/npdsch_npdcch_file_test" "-DARG=-i;/tmp/enbtest2.bin;-m;512;-w;0;-r;0x1234" "-V" "-P" "/home/jonbackman/srsRAN/lib/examples/test/iqtests.cmake")
set_tests_properties(npdsch_npdcch_file3 PROPERTIES  DEPENDS "enb2" PASS_REGULAR_EXPRESSION "pkt_ok=5" _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;69;add_test;/home/jonbackman/srsRAN/lib/examples/test/CMakeLists.txt;0;")
