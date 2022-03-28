from heapq import heapify, heappush, heappop
from typing import List


class KthLargest1:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top = [n for n in nums[:k]]
        heapify(self.top)
        # it turned out I didn't need to keep the leftover cause we don't do pop!!!
        self.bottom = []
        for n in nums[k:]:
            if n > self.top[0]:
                node = heappop(self.top)
                self.bottom.append(node)
                heappush(self.top, n)
            else:
                self.bottom.append(n)
        heapify(self.bottom)

    def add(self, val: int) -> int:
        heappush(self.top, val)
        if len(self.top) > self.k:
            heappush(self.bottom, heappop(self.top))
        return self.top[0]


class KthLargest:
    def __init__(self, k, nums):
        self.hp = nums
        self.k = k
        heapify(self.hp)

    def add(self, val):
        heappush(self.hp, val)
        while len(self.hp) > self.k:
            heappop(self.hp)
        return self.hp[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k=3, nums=[4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))

# ["KthLargest", "add", "add", "add", "add", "add"]
# [[1, []], [-3], [-2], [-4], [0], [4]]
# obj2 = KthLargest(k=1, nums=[])
# print(obj2.add(-3))
# print(obj2.add(-2))
# print(obj2.add(-4))
# print(obj2.add(0))
# print(obj2.add(4))
