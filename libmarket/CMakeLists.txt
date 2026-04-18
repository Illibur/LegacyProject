cmake_minimum_required(VERSION 3.15)
project(libmarket CXX)

# 1. Define this library
add_library(libmarket SHARED src/libmarket.cpp)
target_include_directories(libmarket PUBLIC include)

# 2. Tell CMake where the 'libcore' dependency is
# For now, we point to the local folders. 
# (Later, Conan will do this automatically)
target_include_directories(libmarket PRIVATE ../libcore/include)
target_link_directories(libmarket PRIVATE ../libcore/build)
target_link_libraries(libmarket libcore)
