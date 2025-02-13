set(TARGET_NAME "mid_a")


add_library(${TARGET_NAME} mid.cpp)
target_include_directories(${TARGET_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Describe the requirement from mid_a to up::up_a at the CMake level.
# Note: even though we restricted `mid_a` cpp_info.requires to `up::up_a` only
# `up::up_b` can still be found.
find_package(up CONFIG REQUIRED COMPONENTS up::up_a up::up_b)
target_link_libraries(${TARGET_NAME} PUBLIC up::up_a up::up_b)

# Alias consistent with the cmake_target_name declared in cpp_info
# (not useful for Conan workflow, but makes it so CMake workflow can use the same names)
add_library(mid::${TARGET_NAME} ALIAS ${TARGET_NAME})


# PUBLIC_HEADER property is notably making the headers available in the conan package
set_target_properties(${TARGET_NAME} PROPERTIES PUBLIC_HEADER "mid.h")
install(TARGETS ${TARGET_NAME}
    PUBLIC_HEADER DESTINATION "include/mid_a/")
