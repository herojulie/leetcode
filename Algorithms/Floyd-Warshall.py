# 모든 노드에서 다른 모든 노드로의 최단 거리 구하기. O(N^3)
# Dijkstra 대비 구현이 쉬워 노드, 간선의 갯수가 적을 경우 활용할 수 있다.


INF = int(1e9)


def floyd_warshall(input: list[list[int]], n: int):
    t = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        t[i][i] = 0
    for start, end, cost in input:
        t[start][end] = cost

    for middle in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                t[start][end] = min(t[start][end], t[start][middle] + t[middle][end])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if INF == t[i][j]: print("-", end=' ')
            else: print(t[i][j], end=' ')
        print('')


if __name__ == '__main__':
    g = [
        [1, 2, 6],
        [1, 4, 1],
        [2, 1, 6],
        [2, 4, 2],
        [2, 3, 5],
        [2, 5, 2],
        [3, 2, 5],
        [3, 5, 5],
        [4, 1, 1],
        [4, 2, 2],
        [4, 5, 1]
    ]
    n = 5
    floyd_warshall(g, n)
