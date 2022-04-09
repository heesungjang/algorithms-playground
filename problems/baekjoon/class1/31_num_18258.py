import sys


class Queue():
    def __init__(self):
        self.list = []
        self.tail = 0
        self.top = 0

    def push(self, num):
        self.list.append(num)
        self.tail += 1

    def pop(self):
        if self.tail - self.top == 0:
            return -1
        pop_result = self.list[self.top]
        self.top += 1
        return pop_result

    def size(self):
        return self.tail - self.top

    def empty(self):
        return 0 if self.tail - self.top else 1

    def front(self):
        if self.tail - self.top == 0:
            return -1
        return self.list[self.top]

    def back(self):
        if self.tail - self.top == 0:
            return -1
        return self.list[self.tail - 1]


num = int(input())
queue = Queue()
command = [list(sys.stdin.readline().split()) for _ in range(num)]

for i in range(num):
    if command[i][0] == "push":
        queue.push(command[i][1])
    elif command[i][0] == "pop":
        print(queue.pop())
    elif command[i][0] == "size":
        print(queue.size())
    elif command[i][0] == "empty":
        print(queue.empty())
    elif command[i][0] == "front":
        print(queue.front())
    elif command[i][0] == "back":
        print(queue.back())
