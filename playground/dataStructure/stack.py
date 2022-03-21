class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Node(value, None)
        else:
            curr_top = self.top
            self.top = Node(value, curr_top)

    def pop(self):
        if self.top is not None:
            curr_top = self.top
            self.top = curr_top.next
            return curr_top.value

    def is_empty(self):
        return self.top is None
