from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class LibCoreConan(ConanFile):
  name = "libcore"
  version = "1.0.1"
  package_type = "shared-library"

  # Binary configuration
  settings = "os", "compiler", "build_type", "arch"

  # This tells Conan to generate files that CMake understands
  generators = "CMakeToolchain", "CMakeDeps"

  # Which files to copy into the Conan build folder
  exports_sources = "CMakeLists.txt", "src/*", "include/*"

  def layout(self):
    # This organizes the build folders automatically
    cmake_layout(self)

  def build(self):
    # This is what happens when Conan builds the library
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def package(self):
    # This copies the .so and .h files into the final Conan package
    cmake = CMake(self)
    cmake.install()

  def package_info(self):
    # This tells consumers (like libmarket) what to link against
    self.cpp_info.libs = ["libcore"]
