from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}
        for r in range(len(mat)):
            for c in range(len(mat[r])):
                if r + c not in d:
                    d[r + c] = [mat[r][c]]
                else:
                    d[r + c].append(mat[r][c])

        ans = []
        for items in d.items():
            if items[0] % 2 == 0:
                [ans.append(x) for x in items[1]]
            else:
                [ans.append(x) for x in reversed(items[1])]
        print(ans)
        return ans


if __name__ == '__main__':
    testcase = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().findDiagonalOrder(testcase)
