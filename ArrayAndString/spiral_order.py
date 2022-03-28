from typing import List


class Solution:
    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

    def spiralOrder2(self, matrix):
        n, m = len(matrix), len(matrix[0])

        direction = 1
        i = 0
        j = -1
        ans = []

        while n > 0 and m > 0:
            for _ in range(m):
                j += direction
                ans.append(matrix[i][j])
            n -= 1

            for _ in range(n):
                i += direction
                ans.append(matrix[i][j])
            m -= 1
            direction *= -1

        return ans




if __name__ == '__main__':
    testcase = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder2(testcase))
