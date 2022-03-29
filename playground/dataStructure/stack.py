class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    # [curr]
    # [next]
    # [next]


class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.size = 0

    def push(self, value):
        new_node = Node(value)

        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        curr = self.top

        while curr.next is not None:
            curr = curr.next

    def get_top(self):
        if self.top is not None:
            return self.top.value

    def is_empty(self):
        pass

    def clear(self):
        pass

    def print_all(self):
        curr = self.top
        stack = []
        while curr is not None:
            stack.append(curr.value)
            curr = curr.next

        print(stack)


a = Stack(1)
print(a.get_top())
a.push(2)
a.push(3)
a.push(4)
a.push(5)

a.print_all()
