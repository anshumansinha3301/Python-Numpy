#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

struct Stack {
    int arr[MAX_SIZE];
    int top;
};

void initialize(struct Stack *stack) {
    stack->top = -1;
}

int isFull(struct Stack *stack) {
    return stack->top == MAX_SIZE - 1;
}

void push(struct Stack *stack, int value) {
    if (isFull(stack)) {
        printf("Stack overflow\n");
        return;
    }

    stack->arr[++stack->top] = value;
    printf("%d pushed to the stack\n", value);
}

void display(struct Stack *stack) {
    if (stack->top == -1) {
        printf("Stack is empty\n");
        return;
    }

    printf("Elements in the stack: ");
    for (int i = 0; i <= stack->top; ++i) {
        printf("%d ", stack->arr[i]);
    }
    printf("\n");
}

int main() {
    struct Stack stack;
    initialize(&stack);

    push(&stack, 40);
    push(&stack, 20);
    push(&stack, 30);

    // Display the elements in the stack
    display(&stack);

    return 0;
}
