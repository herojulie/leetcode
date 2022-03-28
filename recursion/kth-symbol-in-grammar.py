import math


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(row: int, index: int) -> int:
            if row == 1:
                return 0
            length = int(math.pow(2, row - 1)) // 2
            if index <= length:
                return helper(row - 1, index) & 1
            else:
                return helper(row - 1, index - length) ^ 1

        return helper(n, k)


if __name__ == '__main__':
    print(Solution().kthGrammar(3, 3))
