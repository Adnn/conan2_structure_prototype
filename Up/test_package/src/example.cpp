#include "up_a.h"
// Works only if we target_link_libraries() against up::up_b
// This is correct
//#include "up_b.h"
#include <vector>
#include <string>

int main() {
    up();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    up_print_vector(vec);
}
