import random


class RandomizedSet:
    def __init__(self):
        self._my_set = set()

    def insert(self, val: int) -> bool:
        if val in self._my_set:
            return False
        self._my_set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self._my_set:
            self._my_set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self._my_set) - 1)
        return list(self._my_set)[random_index]


if __name__ == '__main__':
    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())
