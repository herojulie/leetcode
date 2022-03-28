from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        count_dir_changed = 0
        diff = arr[1] - arr[0]
        if diff <= 0:
            return False
        for i in range(2, len(arr)):
            new_diff = arr[i] - arr[i-1]
            if diff * new_diff < 0:
                if count_dir_changed == 0:
                    count_dir_changed = 1
                else:
                    return False
            if diff * new_diff == 0:
                return False
            diff = new_diff
        return True if count_dir_changed == 1 else False


if __name__ == '__main__':
    print(Solution().validMountainArray(arr=[0,1,2,3,4,5,6,7,8,9]))
