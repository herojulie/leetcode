import math
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(1, k + 1):
                if i + j < len(nums) and abs(nums[i + j] - nums[i]) <= t:
                    return True
        return False

    def containsNearbyAlmostDuplicate_bucket_sort(self, nums: List[int], k: int, t: int) -> bool:
        buckets = dict()
        bucket_num, offset = 0, 0
        for i in range(len(nums)):
            num = nums[i]
            if t:
                bucket_num = math.floor(num / t)
                offset = 1
            else:
                bucket_num = num
                offset = 0
            for j in range(bucket_num - offset, bucket_num + offset + 1):
                if j in buckets and abs(buckets[j] - num) <= t:
                    return True

            buckets[bucket_num] = num

            if len(buckets) >= k:
                del buckets[math.floor(nums[i - k] / t)]
            else:
                del buckets[nums[i - k]]

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().containsNearbyAlmostDuplicate(nums=nums, k=3, t=0))
    # print(Solution().containsNearbyAlmostDuplicate_bucket_sort(nums=nums, k=2, t=0))
