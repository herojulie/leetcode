from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        ans = []
        for n in set1:
            if n in set2:
                ans.append(n)
        return ans

    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     return [*set(nums1).intersection(nums2)]


if __name__ == '__main__':
    print(Solution().intersection(nums1=[1, 2, 2, 1], nums2=[2, 2]))
