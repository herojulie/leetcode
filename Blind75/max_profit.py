# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfitBruteForce(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    ans = 0
    for i in range(len(prices)):
        buy = prices[i]
        for j in range(i + 1, len(prices)):
            sell = prices[j]
            if (sell - buy) > ans:
                ans = sell - buy
    return ans


def maxProfitTwoPointer(prices: list[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    maxP = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


if __name__ == '__main__':
    print(maxProfitTwoPointer([7,1,5,3,6,4]))
