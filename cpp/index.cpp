#include <iostream>
#define CONST_NUM 1

int main() {
  // variable making
  // COPY initialization
  int copiedNum = 3;
  // DIRECT initialization
  int directInit(3);
  // BRACE initialization: a new feature in C++ 11
  // unifies COPY and DIRECT initialization with braces
  int braceCopyNum = {3};
  int braceDirectInitNum{3};

  // int input;
  // // hangs thread and waits for terminal input
  // std::cin >> input;
  // std::cout << input;

  return EXIT_SUCCESS;
}
