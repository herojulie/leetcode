from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = deque()
        for i in range(len(s)):
            if s[i] in pair.keys():
                stack.append(s[i])
            elif s[i] in pair.values():
                if len(stack) > 0:
                    par = stack.pop()
                    if pair[par] != s[i]:
                        return False
                else:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False


if __name__ == '__main__':
    print(Solution().isValid('['))
