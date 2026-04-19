from conan import ConanFile
from conan.tools.cmake import cmake_layout

class EngineReceipt(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  generators = "CMakeToolchain", "CMakeDeps"

  def requirements(self):
    self.requires("libcore/1.0.1")
    self.requires("libmarket/1.0.0")
    self.requires("libutils/1.0.0")

  def layout(self):
    cmake_layout(self)
