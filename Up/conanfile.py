from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class upRecipe(ConanFile):
    name = "up"
    version = "1.4.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of up package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # up_a
        # Use subfolder so "linking" a CMake target to up_a does not make up_b headers visible
        self.cpp_info.components["up_a"].includedirs = ["include/up_a"]
        self.cpp_info.components["up_a"].libs = ["up_a"]
        # Set the target name, which is also used as the `find_package()` COMPONENT name.
        # Note: default target name is <package>::<component>, unless `cmake_target_name` overrides it.
        self.cpp_info.components["up_a"].set_property("cmake_target_name", "up_a")
        # This can be used to **add** aliases for `cmake_target_name`.
        self.cpp_info.components["up_a"].set_property("cmake_target_aliases", ["up::up_a",])

        # up_b
        # Use subfolder so "linking" a CMake target to up_b does not make up_a headers visible
        self.cpp_info.components["up_b"].includedirs = ["include/up_b"]
        self.cpp_info.components["up_b"].libs = ["up_b"]
        self.cpp_info.components["up_b"].set_property("cmake_target_name", "up::up_b")
