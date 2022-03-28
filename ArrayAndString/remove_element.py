from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for number in nums:
            if number == val:
                continue
            nums[k] = number
            k += 1
        return k


if __name__ == '__main__':
    print(Solution().removeElement([0], 1))
