class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        pass
        # new_node = Node(value)
        #
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     self.tail.next = new_node
        #     self.tail = self.tail.next

    def dequeue(self):
        pass
        # if self.head is None:
        #     return -1
        #
        # front = self.head.data
        # self.head = self.head.next
        #
        # if self.head is None:
        #     self.tail = None
        # return front
