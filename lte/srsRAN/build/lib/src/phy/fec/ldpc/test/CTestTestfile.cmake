# CMake generated Testfile for 
# Source directory: /home/jonbackman/srsRAN/lib/src/phy/fec/ldpc/test
# Build directory: /home/jonbackman/srsRAN/build/lib/src/phy/fec/ldpc/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(LDPC-chain "/home/jonbackman/srsRAN/build/lib/src/phy/fec/ldpc/test/ldpc_chain_test")
set_tests_properties(LDPC-chain PROPERTIES  _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/lib/src/phy/fec/ldpc/test/CMakeLists.txt;145;add_test;/home/jonbackman/srsRAN/lib/src/phy/fec/ldpc/test/CMakeLists.txt;0;")
add_test(LDPC-RM-chain "/home/jonbackman/srsRAN/build/lib/src/phy/fec/ldpc/test/ldpc_rm_chain_test" "-E" "1" "-B" "1")
set_tests_properties(LDPC-RM-chain PROPERTIES  LABELS "nr;lib;phy;fec;ldpc" _BACKTRACE_TRIPLES "/home/jonbackman/srsRAN/CMakeLists.txt;628;add_test;/home/jonbackman/srsRAN/lib/src/phy/fec/ldpc/test/CMakeLists.txt;224;add_nr_test;/home/jonbackman/srsRAN/lib/src/phy/fec/ldpc/test/CMakeLists.txt;0;")
