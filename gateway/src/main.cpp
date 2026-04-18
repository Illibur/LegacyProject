#include <iostream>
#include "libcore.h"
#include "libutils.h"

int main() {
  std::cout << "[Gateway] Starting API Gateway..." << std::endl;

  core_hello();
  utils_hello();

  return 0;
}
