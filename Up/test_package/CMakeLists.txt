cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

# Seems to make all components available
#find_package(up CONFIG REQUIRED)

# #SHOULD_FAIL thanks to CMakeDeps.check_components_exist
#find_package(up CONFIG REQUIRED COMPONENTS up::up_a up::nonexistent)

# TODO The component use the cmake_target_name, which is preceded by the namespace
# The namespace is undesired.
find_package(up CONFIG REQUIRED COMPONENTS up::up_a)

add_executable(example src/example.cpp)

# The targets names, as declared in Conan generators,
# are defined by cpp_info property cmake_target_name
target_link_libraries(example up::up_a)
