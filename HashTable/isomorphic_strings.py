class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)
        if len(set_s) != len(set_t):
            return False

        pairs = set([*zip(list(s), list(t))])
        return len(pairs) == len(set_s)


if __name__ == '__main__':
    print(Solution().isIsomorphic('egg', 'adc'))
