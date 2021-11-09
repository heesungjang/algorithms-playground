
class Dict:
    def __init__(self) -> None:
        self.items = [None] * 8
    
    def put(self, key, value) -> None:
        self.items[hash(key)% len(self.items)]  = value
    
    def get(self, key):
        index = hash(key)%len(self.items)
         
        return self.items[index]
    

new_dict = Dict()

print(new_dict.items)
    
new_dict.put("fast", "빠른")

print(new_dict.get("fast"))



