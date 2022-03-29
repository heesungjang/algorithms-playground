class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(Node(value))

    def depth_first_search(self, array):
        array.append(self.value)
        for child in self.children:
            child.depth_first_search(array)

        return array
