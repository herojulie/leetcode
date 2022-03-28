from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return None

        for index, number in enumerate(numbers):
            delta = target - number
            if delta in numbers[index+1:]:
                return [index+1, numbers[index+1:].index(delta)+1+index+1]
        return None


if __name__ == '__main__':
    testcase = [-1, 0, 0, 15]
    print(Solution().twoSum(testcase, 0))
