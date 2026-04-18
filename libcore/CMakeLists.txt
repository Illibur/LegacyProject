cmake_minimum_required(VERSION 3.15)
project(libcore CXX)

# this replaces the 'g++ -shared' steps
add_library(libcore SHARED src/libcore.cpp)

# this replaces the '-Iinclude' flag
target_include_directories(libcore PUBLIC include)

# changes for conan
set_target_properties(libcore PROPERTIES PUBLIC_HEADER include/libcore.h)
install(TARGETS libcore
  LIBRARY DESTINATION lib
  PUBLIC_HEADER DESTINATION include)
