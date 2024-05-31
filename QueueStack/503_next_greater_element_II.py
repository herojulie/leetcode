def nextGreaterElements(nums: list[int]) -> list[int]:
    ans = [-1 for n in range(len(nums))]
    s = []

    for i in range(len(nums) - 1, -1, -1):
        while s and s[-1] <= nums[i]:
            s.pop()
        
        ans[i] = s[-1] if s else -1
        s.append(nums[i])
    
    return ans


print(nextGreaterElements(nums = [1,2,1]))
