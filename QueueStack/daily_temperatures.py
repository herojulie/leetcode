from typing import List
from collections import deque


class Solution:
    # TLE
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break
        return ans

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []

        ans = [0 for _ in range(len(temperatures))]
        stack = deque()
        for cur_i, temp in enumerate(temperatures):
            if not stack:
                stack.append((cur_i, temp))
                continue

            top_i, top_temp = stack[-1]
            while top_temp < temp:
                ans[top_i] = cur_i - top_i
                stack.pop()
                if not stack:
                    break
                top_i, top_temp = stack[-1]
            if not stack or top_temp >= temp:
                stack.append((cur_i, temp))

        return ans


if __name__ == '__main__':
    print(Solution().dailyTemperatures(temperatures=[20, 10, 5, 30]))
