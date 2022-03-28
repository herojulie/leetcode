import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * num for num in nums]
        heapq.heapify(nums)
        i = 0
        while i < k:
            ans = heapq.heappop(nums)
            i += 1
        return ans * -1


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))

