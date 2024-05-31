# https://leetcode.com/problems/contains-duplicate/description/
# return true is there's duplicate
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) == len(set(nums))


if __name__ == '__main__':
    print(containsDuplicate([1,2,3,1]))
