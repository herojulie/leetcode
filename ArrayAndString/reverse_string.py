from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) == 0:
            return
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString3(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.my_recursion(s, 0)

    def my_recursion(self, s: List[str], index: int) -> None:
        if index > (len(s) - 1) // 2:
            return

        temp = s[index]
        s[index] = s[len(s) - 1 - index]
        s[len(s) - 1 - index] = temp
        self.my_recursion(s, index + 1)

    def reverseString2(self, s: List[str]) -> None:
        def helper(my_str, ans):
            if len(my_str) == 0:
                return ans
            return helper(my_str[1:], my_str[0] + ans)
        return helper(s, '')


if __name__ == '__main__':
    print(Solution().reverseString2('julie'))
