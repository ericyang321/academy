#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_chars(char *string) {
  int string_length = strlen(string);
  int idx = 0;
  while (idx < string_length) {
    int forward = sizeof(char) * idx;
    printf("%c", *(string + forward));
    idx += 1;
  }
  printf("\n");
}

char *copy_string(char *string) {
  // get the length of the string in bytes
  // manually allocate memory of string length size
  // use strcopy to copy the string from one memory location to another
  int string_length = strlen(string);
  // + 1 for null byte size
  char *new_string = malloc(sizeof(char) * (string_length + 1));

  strcpy(new_string, string);

  return new_string;
}

struct coordinates {
  int x;
  int y;
};

int main(int argc, char *argv[]) {
  // type, *var_name[size] = {pre, set, items}
  // chars is pointer to the first item in the array
  // int int_array[3] = {1, 2, 3};

  // heap assignment to create array
  // int_block is a pointer to the start of the array
  // int *int_block = malloc(sizeof(int) * 3);

  // adding to memory address shifts the pointer to x elements
  // in an array
  // kind've the equivalent of array[idx]
  // *(int_block + 2 * sizeof(int)) = 8;

  // printf("%d\n", *(int_block + 100 * sizeof(int)));

  // declaring a struct on the stack
  struct coordinates china;
  // reading attributes
  printf("china (%d, %d)", china.x, china.y);
  // updating attributes of a struct on the stack
  china.x = 1;
  china.y = 1;

  // declaring a struct on the heap
  struct coordinates *us = malloc(sizeof(struct coordinates));
  // updating attributes of a struct on the heap
  (*us).x = 2;
  (*us).y = 2;
  // theres a shorthand to ^ that shitty syntax above
  us -> x = 2;
  us -> y = 2;

  return 0;
}


