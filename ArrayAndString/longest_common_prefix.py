from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = []
        chars = [*zip(*strs)]
        for char in chars:
            if len(set(char)) == 1:
                answer.append(char[0])
            else:
                break

        return ''.join(answer)


if __name__ == '__main__':
    testcase = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(testcase))
