from math import sqrt
from typing import List
from heapq import heapify, heappop, heappush, heappushpop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_distance(x1: int, y1: int) -> float:
            return sqrt(x1 ** 2 + y1 ** 2)

        n = len(points)
        heap = []
        for point in points[:k]:
            heap.append((-1 * get_distance(point[0], point[1]), point))
        heapify(heap)
        i = k
        while i < n:
            new_point = points[i]
            new_distance = get_distance(new_point[0], new_point[1])
            max_distance, max_point = heap[0]
            max_distance *= -1
            if new_distance < max_distance:
                heappushpop(heap, (-1 * new_distance, new_point))
            i += 1

        ret = []
        while heap:
            ret.append(heappop(heap)[1])
        return ret

    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]


if __name__ == '__main__':
    s = Solution()
    print(s.kClosest2(points=[[1, 3], [-2, 2]], k=1))
