# def two_sum(ar: list[int], target) -> list[int]:
#     for i in range(len(ar)):
#         try:
#             j = ar.index(target - ar[i], i + 1, len(ar))
#             return list([i, j])
#         except ValueError:
#             continue

# https://leetcode.com/problems/two-sum/description/
def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums:
            j = nums.index(diff)
            if i != j:
                return [i, j]
    return [-1, -1]


if __name__ == '__main__':
    arr = [0, -1, 3, 2, 7]
    print(twoSum(arr, 1))
