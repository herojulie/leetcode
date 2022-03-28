from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color: int = image[sr][sc]
        if newColor == old_color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = newColor
        while queue:
            r, c = queue.popleft()
            # up r-1, c
            if r - 1 >= 0 and image[r - 1][c] == old_color:
                queue.append((r - 1, c))
                image[r - 1][c] = newColor
            # down r+1, c
            if r + 1 < len(image) and image[r + 1][c] == old_color:
                queue.append((r + 1, c))
                image[r + 1][c] = newColor
            # right r, c+1
            if c + 1 < len(image[r]) and image[r][c + 1] == old_color:
                queue.append((r, c + 1))
                image[r][c + 1] = newColor
            # left r, c-1
            if c - 1 >= 0 and image[r][c - 1] == old_color:
                queue.append((r, c - 1))
                image[r][c - 1] = newColor
        return image


if __name__ == '__main__':
    # print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
    print(Solution().floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1))
