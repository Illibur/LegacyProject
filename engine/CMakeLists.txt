cmake_minimum_required(VERSION 3.15)
project(engine CXX)

find_package(libcore REQUIRED)
find_package(libmarket REQUIRED)
find_package(libutils REQUIRED)

add_executable(engine src/main.cpp)

target_link_libraries(engine
  libmarket::libmarket
  libcore::libcore
  libutils::libutils
)
