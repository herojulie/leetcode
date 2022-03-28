from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat) == 0:
            return mat

        R, C = len(mat), len(mat[0])
        DIR = [0, -1, 0, 1, 0]
        queue = deque()
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1

        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nc < 0 or nr >= R or nc >= C or mat[nr][nc] != -1:
                    continue

                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))

        return mat


if __name__ == '__main__':
    print(Solution().updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
