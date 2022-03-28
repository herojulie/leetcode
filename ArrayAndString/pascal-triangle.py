from functools import lru_cache
from typing import List


class Solution:
    def __init__(self):
        self.ans = [[1]]

    @lru_cache(maxsize=None)
    def get_value(self, i: int, j: int):
        if j == 0 or i == j:
            return 1
        return self.ans[i - 1][j - 1] + self.ans[i - 1][j]

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return None

        for i in range(1, numRows):
            temp = []
            for j in range(i + 1):
                temp.append(self.get_value(i, j))
            self.ans.append(temp)

        return self.ans


if __name__ == '__main__':
    print(Solution().generate(5))

