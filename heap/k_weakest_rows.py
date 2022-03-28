from typing import List
from heapq import heapify, heappop


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_points = [1000 * sum(row) + i for i, row in enumerate(mat)]
        heapify(row_points)
        ans = []
        for i in range(k):
            ans.append(heappop(row_points) % 1000)
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.kWeakestRows(mat=
                         [[1, 0, 0, 0],
                          [1, 1, 1, 1],
                          [1, 0, 0, 0],
                          [1, 0, 0, 0]],
                         k=2)
    print(ret)
