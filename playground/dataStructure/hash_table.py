import collections


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(Node)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value in None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = Node(key, value)
            return
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = p.value
                return
            if p.next is None:
                break
            p = p.next
        p.next = Node(key, value)

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]

        if p.key == key:
            self.table[index] = Node() if p.next is None else p.next
            return
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
