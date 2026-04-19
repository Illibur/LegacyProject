from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout

class LibMarketConan(ConanFile):
  name = "libmarket"
  version = "1.0.0"
  package_type = "shared-library"

  settings = "os", "compiler", "build_type", "arch"
  generators = "CMakeToolchain", "CMakeDeps"
  exports_sources = "CMakeLists.txt", "src/*", "include/*"

  # the important line that adds the dependency
  def requirements(self):
    self.requires("libcore/1.0.1")

  def layout(self):
    cmake_layout(self)

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def package(self):
    cmake = CMake(self)
    cmake.install()

  def package_info(self):
    self.cpp_info.libs = ["libmarket"]
