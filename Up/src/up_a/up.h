#pragma once

#include <vector>
#include <string>


#ifdef _WIN32
  #define UP_EXPORT __declspec(dllexport)
#else
  #define UP_EXPORT
#endif

UP_EXPORT void up();
UP_EXPORT void up_print_vector(const std::vector<std::string> &strings);
