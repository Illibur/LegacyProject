#include <iostream>
#include <fstream>
#include <string>
#include "libcore.h"
#include "libmarket.h"
#include "libutils.h"

void load_config(const std::string& filename) {
  std::ifstream file(filename);
  std::string line;
  std::cout << "--- Loading Config: " << filename << " ---" << std::endl;
  if (file.is_open()) {
    while (std::getline(file, line)) {
      std::cout << "Config Param: " << line << std::endl;
    }
  } else {
    std::cout << "Warning: " << filename << " not found. Using defaults." << std::endl;
  }
  std::cout << std::endl;
}

int main() {
  std::cout << "[Engine] Starting high-performance engine..." << std::endl;

  load_config("config.ini");
  // depending on the cofnig we can adjust the behavior based on the client needs

  core_hello();
  market_hello();
  utils_hello();

  return 0;
}
