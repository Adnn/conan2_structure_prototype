#include "mid.h"
#include <vector>
#include <string>

// This is intended to work, even though it should not be done
// (dowstreams should not rely on the fact that mid_a happens to use up_a)
#include "up_a.h"

// #SHOULD_FAIL On the other hand, including "up_b.h" should not work
// up_b is not in the dependency graph of this test package
// Introducing `cpp_info.requires` in Conan recipe does restrict availability
// to only Conan components explicitly listed (instead of the default "all components").
//#include "up_b.h"

int main() {
    mid();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    mid_print_vector(vec);

    // Up
    forward_up();
}
