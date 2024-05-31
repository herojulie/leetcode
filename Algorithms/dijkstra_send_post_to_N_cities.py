"""
전보.
어떤 나라에는 N 개의 도시가 있다.
각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X 라는 도시에서 Y 라는 도시로 전보를 보내고자 하면, X -> Y 인 통로가 있어야 한다.
X -> Y 는 있지만 Y -> X 는 없는 경우, Y 는 X 로 전보를 보낼 수 없다.
또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
어느 날 C 라는 도시에서 위급 상황이 발생했다. C 는 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C 에서 출발해서 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C 에서 보낸 메시지를 받게 되는 도시의
개수는 총 몇 개이며 도시들이 모두 전보를 받기까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하라.
"""
import heapq


def who_receive_post(input: list[int], num_cities: int, start: int) -> (int, int):
    INF = int(1e9)
    N = num_cities

    # create a graph
    graph = [[] for _ in range(N)]
    for src, dst, cost in input:
        graph[src].append((dst, cost))

    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * N
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_dst, next_cost in graph[now]:
            if distance[next_dst] > dist + next_cost:
                distance[next_dst] = dist + next_cost
                heapq.heappush(q, (distance[next_dst], next_dst))

    reachable_cities = [i for i in range(N) if distance[i] != INF and i != start]
    reachable_cities_distance = [distance[i] for i in range(len(reachable_cities))]
    return len(reachable_cities), max(reachable_cities_distance)


if __name__ == '__main__':
    g = [
        [0, 1, 4],
        [0, 2, 2]
    ]
    print(who_receive_post(g, 3, 0))
