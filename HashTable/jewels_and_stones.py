class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set([jewel for jewel in jewels])
        ans = 0
        for stone in stones:
            if stone in jewels_set:
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().numJewelsInStones(jewels="aA", stones="aaAAAbbBBB"))
