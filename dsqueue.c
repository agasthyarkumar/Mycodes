#include <stdio.h>
#include <stdlib.h>

// Node structure for the linked list
struct Node {
    int data;
    struct Node* next;
};

// Queue structure
struct Queue {
    struct Node* front;
    struct Node* rear;
};

// Function to create a new node
struct Node* newNode(int data) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

// Function to create a new queue
struct Queue* createQueue() {
    struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}

// Function to add an element to the queue
void enqueue(struct Queue* q, int data) {
    struct Node* temp = newNode(data);
    if (q->rear == NULL) {
        q->front = q->rear = temp;
        return;
    }
    q->rear->next = temp;
    q->rear = temp;
}

// Function to remove an element from the queue
int dequeue(struct Queue* q) {
    if (q->front == NULL) {
        printf("Queue is empty\n");
        return -1;
    }
    struct Node* temp = q->front;
    q->front = q->front->next;
    if (q->front == NULL) {
        q->rear = NULL;
    }
    int data = temp->data;
    free(temp);
    return data;
}

// Function to display the queue contents
void displayQueue(struct Queue* q) {
    struct Node* temp = q->front;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    struct Queue* q = createQueue();
    enqueue(q, 10);
    enqueue(q, 20);
    enqueue(q, 30);

    printf("Queue contents: ");
    displayQueue(q);

    printf("Dequeued element: %d\n", dequeue(q));

    printf("Queue contents after dequeue: ");
    displayQueue(q);

    return 0;
}
