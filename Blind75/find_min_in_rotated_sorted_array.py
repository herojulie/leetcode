# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    l, r = 0, len(nums) -1
    while l <= r:
        if nums[l] <= nums[r]:
            res = min(res, nums[l])
            break

        mid = (l + r) // 2
        res = min(res, nums[mid])
        if nums[l] <= nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return res


if __name__ == '__main__':
    print(findMin([4,5,1,2,3]))
