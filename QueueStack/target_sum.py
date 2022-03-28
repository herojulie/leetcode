from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.ans = 0
        self.size = 0
        self.target = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.size = len(nums)
        self.target = target
        self.dfs(nums, 0, 0)
        return self.ans

    def dfs(self, num_arr: List[int], my_sum: int, i: int):
        if i == self.size:
            if my_sum == self.target:
                self.ans += 1
        else:
            self.dfs(num_arr, my_sum + num_arr[i], i + 1)
            self.dfs(num_arr, my_sum - num_arr[i], i + 1)


if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
