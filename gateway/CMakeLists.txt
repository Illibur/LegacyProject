cmake_minimum_required(VERSION 3.15)
project(gateway CXX)

add_executable(gateway src/main.cpp)

target_include_directories(gateway PRIVATE
  ../libcore/include
  ../libutils/include)

target_link_directories(gateway PRIVATE
  ../libcore/build
  ../libutils/build)

target_link_libraries(gateway libcore libutils)
