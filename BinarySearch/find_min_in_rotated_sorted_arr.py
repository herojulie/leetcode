from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2

            if nums[start] <= nums[mid]:
                if nums[start] < nums[end]:
                    end = mid
                else:
                    start = mid + 1
            else:
                end = mid

        if start < len(nums) and start == end:
            return nums[start]
        return -1


if __name__ == '__mian__':
    s = Solution()
    print(s.findMin([2, 1]))
