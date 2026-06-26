class MyHashMap:

    def __init__(self):
        self.slots = 10 ** 6
        self.store = [-1 for _ in range(self.slots)]

    def put(self, key: int, value: int) -> None:
        hash = key % self.slots
        self.store[hash] = value

    def get(self, key: int) -> int:
        hash = key % self.slots
        return self.store[hash]

    def remove(self, key: int) -> None:
        hash = key % self.slots
        self.store[hash] = -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
