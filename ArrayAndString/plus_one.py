from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover = 1
        for i in reversed(range(len(digits))):
            sum = digits[i] + carryover
            digits[i] = sum % 10
            if sum < 10:
                return digits
            carryover = sum // 10
        if carryover > 0:
            digits.insert(0, carryover)
        return digits


if __name__ == '__main__':
    testcase = [9, 9]
    print(Solution().plusOne(testcase))
