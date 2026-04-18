cmake_minimum_required(VERSION 3.15)
project(libutils CXX)

# Use STATIC instead of SHARED
add_library(libutils STATIC src/libutils.cpp)

target_include_directories(libutils PUBLIC include)

# changes for conan
set_target_properties(libutils PROPERTIES PUBLIC_HEADER include/libutils.h)
install(TARGETS libutils
  ARCHIVE DESTINATION lib
  PUBLIC_HEADER DESTINATION include)
