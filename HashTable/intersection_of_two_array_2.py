from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i, num in enumerate(nums1):
            if num in nums2:
                ans.append(num)
                nums2.remove(num)
                if len(nums2) == 0:
                    break
        return ans


if __name__ == '__main__':
    print(Solution().intersect(nums1=[4], nums2=[9]))
