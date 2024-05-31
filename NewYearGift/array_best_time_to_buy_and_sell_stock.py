from typing import List


class Solution:
    # O(N^2)
    def maxProfit_poor(self, prices: List[int]) -> int:
        profit = 0
        for i, buy in enumerate(prices[:-1]):
            sell = max(prices[i + 1:])
            new_profit = sell - buy if sell > buy else 0
            profit = max(profit, new_profit)
        return profit

    # O(N)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
