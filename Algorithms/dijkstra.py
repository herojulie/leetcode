import heapq

INF = int(1e9)


def get_shortest_node(distance, visited, n_node) -> int:
    min_value = INF
    index = 0
    for i in range(1, n_node + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra_list(graph: list[list[int]], n_node: int, start: int):
    visited = [False] * (n_node + 1)
    distance = [INF] * (n_node + 1)

    g = [[] for _ in range(n_node + 1)]
    for src, dst, cost in graph:
        g[src].append((dst, cost))

    distance[start] = 0
    visited[start] = True
    for dst, cost in g[start]:
        distance[dst] = cost

    for _ in range(n_node - 1):
        now = get_shortest_node(distance, visited, n_node)
        visited[now] = True
        for dst, cost in g[now]:
            cost = distance[now] + cost
            if cost < distance[dst]:
                distance[dst] = cost

    for i in range(1, n_node + 1):
        if distance[i] == INF:
            print("INFINITY", end=' ')
        else:
            print(distance[i], end=' ')


def dijkstra_heap(input: list[list[int]], n: int, start: int):
    # create graph
    g = [[] for _ in range(n + 1)]
    for src, dst, so_far in input:
        g[src].append((dst, so_far))

    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        so_far, dst = heapq.heappop(q)
        if so_far > distance[dst]:
            continue

        for next_dst, cost in g[dst]:
            dist = so_far + cost
            if dist < distance[next_dst]:
                distance[next_dst] = dist
                heapq.heappush(q, (distance[next_dst], next_dst))

    for i in range(1, n + 1):
        if distance[i] == INF:
            print("INF", end=' ')
        else:
            print(distance[i], end=' ')


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

    num_nodes = 5

    dijkstra_list(g, num_nodes, 1)
    print('\nusing heap: ')
    dijkstra_heap(g, num_nodes, 1)
