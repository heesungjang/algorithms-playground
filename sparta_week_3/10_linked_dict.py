class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        key_to_index = hash("key") % len(self.items)
        linked_tuple = self.items[key_to_index]
        linked_tuple.add(key, value)

    def get(self, key):
        key_to_index = hash("key") % len(self.items)
        linked_tuple = self.items[key_to_index]
        value = linked_tuple.get(key)
        return value

