from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class midRecipe(ConanFile):
    name = "case_02"
    version = "1.0.0"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of mid package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def requirements(self):
        self.requires(
                "up/1.4.0",
                # Seems required for downstreams of mid to find headers of up
                # (up headers are publicly included by mid headers)
                transitive_headers=True)

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
        self.cpp_info.includedirs = ["include/mid_a"]
        self.cpp_info.libs = ["mid_a"]
        self.cpp_info.set_property("cmake_target_name", "case_02::mid_a")
        # TODO: apparently, adding an explicit requirement from mid_a to up_a
        # prevents from including up_b headers in mid_a downstreams,
        # **even though** mid_a is linked against up_b by CMake.
        # (Note: the fact that up_b target is available at all in CMake is another discussion)
        self.cpp_info.requires = ["up::up_a",]
        # Note:  Adding up_b in requires (as well as removing requires entirely)
        # would fix the inclusion error
        #self.cpp_info.requires = ["up::up_a", "up::up_b"]
