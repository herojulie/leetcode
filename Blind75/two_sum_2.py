# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    answer = []
    l, r = 0, len(numbers) - 1
    while l <= r:
        if l > 0 and numbers[l - 1] == numbers[l]:
            l += 1
            continue

        curSum = numbers[l] + numbers[r]

        if curSum < target:
            l += 1
        elif curSum > target:
            r -= 1
        else:
            return [l, r]
    return answer


if __name__ == '__main__':
    print(twoSum([1,1,2,4,6], 8))
