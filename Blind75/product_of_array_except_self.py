# https://leetcode.com/problems/product-of-array-except-self/description/
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= postfix
        postfix *= nums[i]
    return ans


if __name__ == '__main__':
    print(productExceptSelf([1,2,3,4]))

