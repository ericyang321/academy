#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/*
  Avoid:
    - casts
    - signed ints

  Notes:

  - in C, 0 is false and not-zero is true
*/

int main() {
  unsigned long int bigboi = 3000000UL;

  printf("%lu", bigboi);
}
