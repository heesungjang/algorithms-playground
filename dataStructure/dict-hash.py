
class Dict:
    def __init__(self) -> None:
        self.items = [None] * 8
    
    def put(self, key, value) -> None:
        self.items[hash(key)%8]  = value
    
    def get(self, key):
        return self.items[hash(key)%8]
    

new_dict = Dict()

print(new_dict.items)
    
new_dict.put("fast", "빠른")

print(new_dict.get("fast"))