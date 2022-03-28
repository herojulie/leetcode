from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}

        for s in strs:
            key = ''.join(sorted(list([*s])))
            if key in dict_strs:
                dict_strs[key].append(s)
            else:
                dict_strs[key] = [s]

        return dict_strs.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(strs=["", 'a', 'b']))
