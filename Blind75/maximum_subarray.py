# https://leetcode.com/problems/maximum-subarray/description/

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curSum = nums[0]
    maxSum = 0
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


if __name__ == '__main__':
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1]))
