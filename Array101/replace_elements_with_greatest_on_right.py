from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            arr[0] = -1
            return arr
        arr = arr[::-1]
        maximum = arr[0]

        for i, num in enumerate(arr):
            arr[i] = maximum
            maximum = max(maximum, num)
        arr[0] = -1
        return arr[::-1]


if __name__ == '__main__':
    print(Solution().replaceElements(arr=[17,18,5,4,6,1]))
