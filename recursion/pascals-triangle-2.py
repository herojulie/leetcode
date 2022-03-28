from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def get_sum(self, i: int, j: int):
        if (i == 0 and j == 0) or (j == 0) or (i == j):
            return 1

        if (i - 1, j - 1) not in self.cache:
            self.cache[(i - 1, j - 1)] = self.get_sum(i - 1, j - 1)
        if (i - 1, j) not in self.cache:
            self.cache[(i - 1, j)] = self.get_sum(i - 1, j)
        return self.cache[(i - 1, j - 1)] + self.cache[(i - 1, j)]

    def getRow(self, rowIndex: int) -> List[int]:
        return [self.get_sum(rowIndex-1, j) for j in range(rowIndex)]


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
