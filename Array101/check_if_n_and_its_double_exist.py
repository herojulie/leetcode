from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i, number in enumerate(arr):
            if i + 1 == len(arr):
                return False
            try:
                if arr.index(number * 2, i + 1):
                    return True
            except ValueError:
                continue
        return False


if __name__ == '__main__':
    print(Solution().checkIfExist(arr=[7, 1, 14, 11]))
