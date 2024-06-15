#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node_s {
  int data;
  struct Node_s *next;
} Node;

void init_node(Node *node, int data) {
  node->data = data;
  node->next = NULL;
}
void append(Node *first, Node *next) { first->next = next; }
short len(Node *node) {
  short length = 0;

  Node *curr = node;
  while (curr) {
    length += 1;
    curr = node->next;
  };

  return length;
}

int main(void) {
  Node root_node;
  init_node(&root_node, 1);

  assert(len(NULL) == 0);
  assert(len(&root_node) == 1);

  return 0;
}
