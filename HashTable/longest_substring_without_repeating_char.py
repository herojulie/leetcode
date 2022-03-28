class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        ans = 0
        used = set()
        substring = []
        i = 0
        while i < len(s):
            if s[i] not in used:
                substring.append(s[i])
                used.add(s[i])
            else:
                ans = max(ans, len(substring))
                duplicate_char_index = substring.index(s[i])
                substring = substring[duplicate_char_index + 1:] + [s[i]]
                used = set(substring)
            i += 1

        return max(ans, len(substring))


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s="au"))
