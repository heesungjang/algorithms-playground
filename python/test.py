class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self, value):
        self.top = Node(value)

    def get_top(self):
        return self.top.value

    def append(self, value):
        cur_top = self.top

        cur_top.next = Node(value)

        self.top = cur_top.next

    def pop(self):
        pass


stack = Stack(2)

stack.append(3)

print(stack.get_top())


def some(a):
    pass
