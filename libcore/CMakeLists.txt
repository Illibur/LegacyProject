cmake_minimum_required(VERSION 3.15)
project(libcore CXX)

# This replaces the 'g++ -shared' steps
add_library(libcore SHARED src/libcore.cpp)

# This replaces the '-Iinclude' flag
target_include_directories(libcore PUBLIC include)
