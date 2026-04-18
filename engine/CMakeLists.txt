cmake_minimum_required(VERSION 3.15)
project(engine CXX)

add_executable(engine src/main.cpp)

target_include_directories(engine PRIVATE
  ../libcore/include
  ../libmarket/include
  ../libutils/include)

target_link_directories(engine PRIVATE
  ../libcore/build
  ../libmarket/build
  ../libutils/build)

# Explicitly link all three
target_link_libraries(engine libmarket libcore libutils)
