from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        def find_index_of_the_largest(n: int) -> int:
            for i in range(len(nums)):
                if nums[i] == n:
                    return i
            return -1
        if len(nums) <= 0:
            return -1
        if len(nums) == 1:
            return 0

        sorted_nums: [int] = [num for num in nums]
        sorted_nums.sort()
        if sorted_nums[-1] >= sorted_nums[-2] * 2:
            return find_index_of_the_largest(sorted_nums[-1])
        return -1


if __name__ == '__main__':
    testcase = [1, 3, 4, 8, 2, 0]
    print(Solution().dominantIndex(testcase))
