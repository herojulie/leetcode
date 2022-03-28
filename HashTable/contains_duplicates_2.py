from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_nums = {}
        for i, number in enumerate(nums):
            if number in dict_nums and abs(i - dict_nums[number]) <= k:
                return True
            else:
                dict_nums[number] = i
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
