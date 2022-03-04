class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        key_to_idx = hash(key) % len(self.items)
        self.items[key_to_idx] = value
        return

    def get(self, key):
        key_to_idx = hash(key) % 8
        return self.items[key_to_idx]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
