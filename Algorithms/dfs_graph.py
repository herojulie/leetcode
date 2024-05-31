
def dfs(graph: list[list[int]]):
    visited = [False] * (len(graph) + 1)
    my_dfs(graph, 1, visited)


def my_dfs(graph: list[list[int]], curr_v: int, visited: list[bool]):
    visited[curr_v] = True
    print(curr_v, end=' ')

    for i in graph[curr_v]:
        if not visited[i]:
            my_dfs(graph, i, visited)


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
    dfs(g)
