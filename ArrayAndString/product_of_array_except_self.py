# https://leetcode.com/problems/product-of-array-except-self/
from itertools import accumulate
from operator import mul
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in nums]
        # calculate the left part first
        # left = 1
        # for i in range(1, len(nums)):
        #     left = left * nums[i - 1]
        #     answer[i] = left
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        right = 1
        for j in reversed(range(len(nums))):
            answer[j] = answer[j] * right
            right = right * nums[j]

        return answer


class Solution2:
    def productExceptSelf(self, nums):
        pre, suf, n = list(accumulate(nums, mul)), list(accumulate(nums[::-1], mul))[::-1], len(nums)
        return [(pre[i-1] if i else 1) * (suf[i+1] if i+1 < n else 1) for i in range(n)]


if __name__ == '__main__':
    print(Solution2().productExceptSelf(nums=[1, 2, 3, 4, 5]))
    print(Solution().productExceptSelf(nums=[1, 1, 1, 1, 1]))
