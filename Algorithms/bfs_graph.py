def bfs(graph: list[list[int]]):
    my_bfs_while(graph)


def my_bfs_while(graph: list[list[int]]):
    if len(graph) < 2:
        return
    visited = [False] * (len(graph) + 1)
    q = list()
    q.append(1)
    while q:
        n = q.pop(0)
        print(n, end=' ')

        for i in graph[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


if __name__ == '__main__':
    g = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    bfs(g)
