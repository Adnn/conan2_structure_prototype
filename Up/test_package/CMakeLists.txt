cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(up CONFIG REQUIRED)

add_executable(example src/example.cpp)
# The name is defined by cpp_info property cmake_target_name
target_link_libraries(example up::up_a)
