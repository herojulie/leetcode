class MyHashSet:
    def __init__(self):
        self.total_bucket = 10
        self.buckets = [[] for _ in range(self.total_bucket)]

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        self.buckets[self.hash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            index = self.buckets[self.hash(key)].index(key)
            self.buckets[self.hash(key)].pop(index)

    def contains(self, key: int) -> bool:
        return True if key in self.buckets[self.hash(key)] else False

    def hash(self, key):
        return key % 10


if __name__ == '__main__':
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    print(obj.add(9))
    print(obj.remove(19))
    print(obj.add(14))
    print(obj.remove(19))
    print(obj.remove(9))
    print(obj.add(0))
    print(obj.add(3))
    print(obj.add(4))
    print(obj.add(0))
    print(obj.remove(9))
    # print(obj.contains(1))
    # print(obj.contains(3))
    # print(obj.add(2))
    # print(obj.contains(2))
    # print(obj.remove(2))
    # print(obj.contains(2))
