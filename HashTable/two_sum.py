from typing import List


class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i, n in enumerate(nums):
            delta = target - n
            if delta in nums_set:
                i_delta = nums.index(delta)
                if i != i_delta:
                    return sorted([i, i_delta])
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = [i]
            else:
                nums_dict[num].append(i)

        for num, indexes in nums_dict.items():
            delta = target - num
            if delta == num and len(indexes) >= 2:
                return indexes[:2]
            if delta != num and delta in nums_dict:
                return [indexes[0], nums_dict[delta][0]]
        return None


if __name__ =='__main__':
    print(Solution().twoSum(nums=[3,2,4], target=6))
