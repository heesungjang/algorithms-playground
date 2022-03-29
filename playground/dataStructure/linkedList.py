class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        curr = self.head

        if self.head is None:
            self.head = Node(value)
            return

        new_node = Node(value)
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

    def get_nth_node(self, index):
        curr = self.head

        count = 0

        while count < index:
            curr = curr.next
            count += 1

        return curr

    def insert(self, index, value):
        curr = self.head
        new_node = Node(value)

        if index == 0:
            new_node.next = curr
            self.head = new_node

        else:
            prev = self.get_nth_node(index - 1)
            old_next = prev.next
            prev.next = new_node
            new_node.next = old_next

    def delete(self, index):

        if index == 0:
            self.head = self.head.next

        else:
            prev = self.get_nth_node(index - 1)
            prev.next = prev.next.next

    def print_all(self):
        list = []
        curr = self.head
        while curr is not None:
            list.append(curr.value)
            curr = curr.next

        print(list)

    def delete_end(self):
        curr = self.head
        prev = None
        if curr.next is None:
            self.head = None
            return

        # [1] [2] [3] [4] [5] [6] --> None
        #                     curr
        while curr.next is not None:
            prev = curr
            curr = curr.next
        prev.next = None


a = LinkedList(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.delete(1)
a.print_all()
a.delete_end()
a.print_all()
a.delete_end()
a.print_all()
a.delete_end()
a.print_all()
a.delete_end()
a.print_all()
a.append(1)
a.print_all()
a.append(1)
a.append(1)
a.append(1)
a.append(1)
a.print_all()
