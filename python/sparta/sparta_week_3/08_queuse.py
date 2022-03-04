class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head/tail tail.next
    # [4] -> [2] -> [3]
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
        return

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        removed_queue = self.head
        self.head = self.head.next
        return removed_queue.data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")

        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
queue.dequeue()
print(queue.peek())
queue.enqueue(5)
queue.dequeue()
print(queue.peek())