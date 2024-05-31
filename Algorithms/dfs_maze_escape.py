"""
미로 탈출
쥬리는 N * M 크기의 직사각형 미로에 갇혔다. 미로에는 여러 괴물이 있어 이를 피해 탈출해야 한다.
쥬리의 위치는 (1, 1) 이며, 미로의 출구는 (N, M)의 위치에 존재한다.
한 번에 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0, 없는 부분은 1.
미로는 반드시 탈출할 수 있는 형태로 제시된다.
탈출을 위해 움직혀야 하는 최소 칸의 개수를 구하라.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
"""

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def escape(graph: list[list[int]]) -> int:
    R = len(graph)
    C = len(graph[0])
    q = list()
    q.append((0, 0))
    count = 0
    while q:
        r, c = q.pop(0)
        for d in direction:
            nr = r + d[0]
            nc = c + d[1]

            if 0 <= nr < R and 0 <= nc < C:
                if graph[nr][nc] == 1:
                    graph[nr][nc] = graph[r][c] + 1
                    q.append((nr, nc))
    return graph[R - 1][C - 1]


if __name__ == '__main__':
    maze = [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    print(escape(maze))
