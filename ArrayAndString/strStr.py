class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        temp = haystack.split(needle)
        if len(temp) < 2:
            return -1

        return len(temp[0])

    def strStr2(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        if needle in haystack:
            return haystack.index(needle)
        return -1


if __name__ == '__main__':
    print(Solution().strStr("", ""))
