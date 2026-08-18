class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            pos = self.keys.index(key)
            self.values[pos] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key: int) -> int:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                return self.values[i]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.keys)):
            if self.keys[i] == key:
                self.keys.pop(i)
                self.values.pop(i)
                break



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)