import collections
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = collections.Counter(a + b for a in nums1 for b in nums2)
        return sum(AB[-c - d] for c in nums3 for d in nums4)


if __name__ == '__main__':
    print(Solution().fourSumCount(nums1=[1, 2], nums2=[-2, -1], nums3=[-1, 2], nums4=[0, 2]))
