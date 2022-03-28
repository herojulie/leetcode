from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = len(nums) + 1
        ans = INF
        left, right = 0, 0
        my_sum = 0

        for right in range(len(nums)):
            my_sum += nums[right]
            while my_sum >= target:
                ans = min(ans, right - left + 1)
                my_sum -= nums[left]
                left += 1
        return ans if ans != INF else 0


if __name__ == '__main__':
    print(Solution().minSubArrayLen(5, [1, 4, 4, 2, 2, 5]))
