cmake_minimum_required(VERSION 3.15)
project(gateway CXX)

find_package(libcore REQUIRED)
find_package(libutils REQUIRED)

add_executable(gateway src/main.cpp)

target_link_libraries(gateway
  libcore::libcore
  libutils::libutils
)
