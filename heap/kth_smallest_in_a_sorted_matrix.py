from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(k):
            r = i // n
            c = i % n
            heap.append(-1 * matrix[r][c])
        heapify(heap)
        i = k
        while i < n**2:
            r = i // n
            c = i % n
            if -1 * heap[0] > matrix[r][c]:
                heappop(heap)
                heappush(heap, -1 * matrix[r][c])
            i += 1
        return -1 * heap[0]


if __name__ == '__main__':
    s = Solution()
    # ans = s.kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8)
    ans = s.kthSmallest(matrix=[[1, 2], [1, 3]], k=2)
    print(ans)
