from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if target >= nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[2, 3, 4, 5, 6, 7, 1], target=7))
