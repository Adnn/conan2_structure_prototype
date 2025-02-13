#pragma once

// Demonstrate public header inclusion (mid package marks up headers as transitive)
#include "up_a.h"

// Note: the failure point, when the current header of mid_a is included by test_package.
#include "up_b.h"

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

