cmake_minimum_required(VERSION 3.15)
project(libutils CXX)

# Use STATIC instead of SHARED
add_library(libutils STATIC src/libutils.cpp)

target_include_directories(libutils PUBLIC include)
