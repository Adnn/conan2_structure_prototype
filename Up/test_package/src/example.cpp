#include "up.h"
#include <vector>
#include <string>

int main() {
    up();

    std::vector<std::string> vec;
    vec.push_back("test_package");

    up_print_vector(vec);
}
