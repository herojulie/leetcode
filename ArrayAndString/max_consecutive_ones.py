from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        left = 0
        while left < len(nums):
            if nums[left] == 1:
                right = left + 1
                while right < len(nums):
                    if nums[right] == 1:
                        right += 1
                        continue
                    else:
                        break
                max_ones = max(max_ones, right - left)
                left = right + 1
            else:
                left += 1
        return max_ones


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1]))
