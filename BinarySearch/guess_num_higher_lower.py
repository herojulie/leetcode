# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while True:
            mid = (low + high) // 2
            res = guess(mid)
            if res == -1:
                high = mid - 1
            elif res == 1:
                low = mid + 1
            else:
                return mid
        return -1
