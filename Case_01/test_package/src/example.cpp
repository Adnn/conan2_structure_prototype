// Note: This mid.h header includes up_a header, which causes an error
// since up_a headers ar marked non-transitive in mid package.
#include "mid.h"
#include <vector>
#include <string>

int main() {
    mid();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    mid_print_vector(vec);

    // Up
    forward_up();
}
