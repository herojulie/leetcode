from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return None

        rotate = k % len(nums)
        if rotate != 0:
            nums[:rotate], nums[rotate:] = nums[-rotate:], nums[:-rotate]

        print(nums)


if __name__ == '__main__':
    Solution().rotate([1], 1)
