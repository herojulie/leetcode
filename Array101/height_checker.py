from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return 0
        expected = sorted(heights)
        count = 0

        # O(N)
        # pair_each_index = [*zip(expected, heights)]
        # for pair in pair_each_index:
        #     count = count + 1 if len(set(pair)) != 1 else count

        # O(N) and simpler
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count


if __name__ == '__main__':
    print(Solution().heightChecker(heights=[1, 3, 2]))
