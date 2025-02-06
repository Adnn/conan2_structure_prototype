set(TARGET_NAME "up_b")


add_library(${TARGET_NAME} up_b.cpp)
target_include_directories(${TARGET_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})


# Alias consistent with the cmake_target_name declared in cpp_info
# (not useful for Conan workflow, but makes it so CMake workflow can use the same names)
add_library(up::${TARGET_NAME} ALIAS ${TARGET_NAME})


# PUBLIC_HEADER property is notably making the headers available in the conan package
set_target_properties(${TARGET_NAME} PROPERTIES PUBLIC_HEADER "up_b.h")
install(TARGETS ${TARGET_NAME}
    PUBLIC_HEADER DESTINATION "include/up_b/")
