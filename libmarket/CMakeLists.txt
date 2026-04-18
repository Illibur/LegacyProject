cmake_minimum_required(VERSION 3.15)
project(libmarket CXX)

# this should be searched for in conan packages
find_package(libcore REQUIRED)

# 1. Define this library
add_library(libmarket SHARED src/libmarket.cpp)
target_include_directories(libmarket PUBLIC include)

# conan shoudl provice the libcore (Namespace::Name)
target_link_libraries(libmarket libcore::libcore)

set_target_properties(libmarket PROPERTIES PUBLIC_HEADER include/libmarket.h)
install(TARGETS libmarket
  LIBRARY DESTINATION lib
  PUBLIC_HEADER DESTINATION include)
