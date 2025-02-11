cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

# Seems to make all components available
#find_package(up CONFIG REQUIRED)

# #SHOULD_FAIL thanks to CMakeDeps.check_components_exist
#find_package(up CONFIG REQUIRED COMPONENTS up::up_a up::nonexistent)

# TODO The namespace is undesired in find_package().
# The component uses the cmake_target_name, which is preceded by the namespace
find_package(up CONFIG REQUIRED COMPONENTS up::up_a)

add_executable(example src/example.cpp)

# The targets names, as declared in Conan generators,
# are defined by cpp_info property cmake_target_name
target_link_libraries(example up::up_a)

# TODO #SHOULD_FAIL because we did not request up::up:b
target_link_libraries(example up::up_a up::up_b)

# #SHOULD_FAIL because up::nonexistent target does not exist
#target_link_libraries(example up::nonexistent)

