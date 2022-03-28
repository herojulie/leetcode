from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        while i < size:
            if arr[i] == 0:
                arr[i + 1:] = arr[i:-1]
                i += 1
            i += 1
        print(arr)


if __name__ == '__main__':
    print(Solution().duplicateZeros(arr=[1, 0, 2, 3, 0, 4, 5, 0]))
