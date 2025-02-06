#pragma once

// Demonstrate public header inclusion
#include "up_a.h"
// #SHOULD_FAIL, because we target_link_libraries to up::up_a, not up::up_b
//#include "up_b.h"

#include <vector>
#include <string>


#ifdef _WIN32
  #define MID_EXPORT __declspec(dllexport)
#else
  #define MID_EXPORT
#endif

MID_EXPORT void mid();
MID_EXPORT void mid_print_vector(const std::vector<std::string> &strings);

UP_EXPORT void forward_up();

