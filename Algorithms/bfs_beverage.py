"""
음료수 얼려 먹기
N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1.
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
ex.
input:
00110
00011
11111
00000
output:
3
"""

from collections import deque


def my_dfs(map: list[list[int]], i, j):
    q = deque()
    q.append((i, j))

    dir = [(0, -1), (0, 1), (1, 0)]  # left, down, right
    while q:
        r, c = q.popleft()
        for i in range(len(dir)):
            new_r, new_c = r + dir[i][0], c + dir[i][1]
            if 0 <= new_r < len(map) and 0 <= new_c < len(map[i]):
                if map[new_r][new_c] == 0:
                    q.append((new_r, new_c))
                    map[new_r][new_c] = 1
    return map


def how_many_ice_creams(tray: list[list[int]]) -> int:
    count = 0
    for i in range(len(tray)):
        for j in range(len(tray[i])):
            if tray[i][j] == 0:
                tray = my_dfs(tray, i, j)
                count += 1
    return count


if __name__ == '__main__':
    tray = [[0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]]
    print(how_many_ice_creams(tray))
