from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return -1
        if len(nums) == 1:
            return 0

        # init sums
        sums = [0] * len(nums)
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        for i in range(len(sums)):
            left_sum = sums[i - 1] if i >= 1 else 0
            right_sum = sums[-1] - sums[i]
            if left_sum == right_sum:
                return i
        return -1


if __name__ == '__main__':
    testcase: [int] = [2, 1, -1]
    print(Solution().pivotIndex(testcase))
