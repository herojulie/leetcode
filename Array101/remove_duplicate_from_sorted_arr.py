from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return len(nums)

        total_len = len(nums)
        prev = nums[0]
        i = 1

        while i < total_len:
            curr = nums[i]
            if prev == curr:
                nums.pop(i)
                total_len -= 1
                continue
            else:
                prev = curr
                i += 1
        return len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0]))
