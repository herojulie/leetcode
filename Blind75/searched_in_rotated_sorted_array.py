# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m

        # left sorted
        if nums[l] <= nums[m]:
            if target < nums[l] or nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m] or nums[r] < target:
                r = m - 1
            else:
                l = m + 1
    return -1


if __name__ == '__main__':
    print(search([4, 5, 6, 1, 2, 3], 2))
