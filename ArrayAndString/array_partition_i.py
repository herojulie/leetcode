from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        ans = 0
        for num in nums[::2]:
            ans += num

        return ans


if __name__ == '__main__':
    print(Solution().arrayPairSum([1, 3, 4, 2]))
