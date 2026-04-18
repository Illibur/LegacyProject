#include <iostream>
#include "libcore.h"
#include "libmarket.h"

void market_hello() {
  std::cout << "[libmarket] Accessing market data..." << std::endl;
  core_hello();
}
