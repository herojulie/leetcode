from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
