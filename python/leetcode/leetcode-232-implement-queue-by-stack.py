class MyQueue(object):

    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
obj.push(2)
obj.push(2)
print(obj.output)
param_2 = obj.pop()
print(obj.output)
param_3 = obj.peek()
print(obj.output)
obj.push(3)
print(obj.output)
obj.peek()
print(obj.output)

param_4 = obj.empty()
