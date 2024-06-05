# https://leetcode.com/problems/maximum-product-subarray/description/

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = max(nums)
    curMax, curMin = 1, 1
    for n in nums:
        tmp = curMax * n
        curMax = max(tmp, curMin * n, n)
        curMin = min(tmp, curMin * n, n)
        res = max(res, curMax)
    return res


if __name__ == '__main__':
    print(maxProduct([2,3,-1,4]))
