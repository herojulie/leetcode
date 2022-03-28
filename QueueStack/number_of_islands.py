from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1':
                    # grid = self.bfs(grid, r, c)
                    grid = self.dfs(grid, r, c)
                    ans += 1
        return ans

    # mark an island including grid[r][c] visited
    def bfs(self, grid, r, c) -> List[List[str]]:
        if len(grid) == 0 or r < 0 or c < 0:
            return grid

        queue = [[r, c]]
        grid[r][c] = '-1'
        while len(queue) > 0:
            r, c = queue.pop(0)
            # up
            if r - 1 >= 0 and grid[r - 1][c] == '1':
                queue.append([r - 1, c])
                grid[r - 1][c] = '-1'
            # down
            if r + 1 < len(grid) and grid[r + 1][c] == '1':
                queue.append([r + 1, c])
                grid[r + 1][c] = '-1'
            # left
            if c - 1 >= 0 and grid[r][c - 1] == '1':
                queue.append([r, c - 1])
                grid[r][c - 1] = '-1'
            # right
            if c + 1 < len(grid[r]) and grid[r][c + 1] == '1':
                queue.append([r, c + 1])
                grid[r][c + 1] = '-1'

        return grid

    def dfs(self, grid, r, c) -> List[List[str]]:
        if len(grid) == 0 or r < 0 or c < 0:
            return grid

        stack = deque([[r, c]])
        while stack:
            r, c = stack.pop()
            if grid[r][c] == '1':
                if r - 1 >= 0 and grid[r-1][c] == '1':
                    stack.append([r-1, c])
                    grid[r-1][c] == '-1'
                if c + 1 < len(grid[r]) and grid[r][c+1] == '1':
                    stack.append([r, c+1])
                    grid[r][c+1] == '-1'
                if r + 1 < len(grid) and grid[r+1][c] == '1':
                    stack.append([r+1, c])
                    grid[r+1][c] == '-1'
                if c - 1 >= 0 and grid[r][c-1] == '1':
                    stack.append([r, c-1])
                    grid[r][c-1] == '-1'
            grid[r][c] = '-1'
        return grid


if __name__ == '__main__':
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [['0'], ['0'], ['1'], ['1'], ['0'], ['1']]
    grid3 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(Solution().numIslands(grid3))
