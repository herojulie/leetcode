# https://leetcode.com/problems/3sum/description/
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and nums[i - 1] == a:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                ans.append([a, nums[l], nums[r]])
                l += 1
                # out of index without l < r!!!
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return ans
