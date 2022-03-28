class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_s: {str: int} = dict()
        for ch in s:
            try:
                dict_s[ch] += 1
            except KeyError:
                dict_s[ch] = 1

        for i in range(len(s)):
            if dict_s[s[i]] == 1:
                return i

        return -1


if __name__ == '__main__':
    print(Solution().firstUniqChar("l"))
