from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * n for n in stones]
        heapify(stones)

        while len(stones) > 1:
            stone_one = -1 * heappop(stones)
            stone_two = -1 * heappop(stones)
            weight_diff = abs(stone_one - stone_two)
            if weight_diff > 0:
                heappush(stones, -1 * weight_diff)

        return 0 if len(stones) == 0 else -1 * stones[0]


if __name__ == '__main__':
    s = Solution()
    ans = s.lastStoneWeight(stones=[3,3,3,3])
    print(ans)
