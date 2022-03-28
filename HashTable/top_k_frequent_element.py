from operator import itemgetter
from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        nums_list = [(num, freq) for num, freq in nums_dict.items()]
        nums_list.sort(key=itemgetter(1), reverse=True)
        return [num for num, _ in nums_list[:k]]


if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    print(Solution().topKFrequent(nums=[0, 0], k=1))
