"""
미래 도시.
미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해 연결되어 있다.
방문 판매원 쥬리는 현재 1 번 회사에 위치해 있으며, X 번 회사에 방문해 물건을 판매하고자 한다.
미래 도시에서 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하다.
또한 연결된 2 개의 회사는 양방향으로 이동할 수 있다. 회사와 회사가 도로로 연결된 경우, 1 만큼의 시간으로 이동할 수 있다.
쥬리는 오늘 기대하던 소개팅에도 참석하고자 한다. 소개팅 상대는 K 번 회사에서 근무한다. 쥬리는 X 번 회사에 가기 전
소개팅 상대 회사에 찾아가 함께 커피를 마실 예정이다. 따라서 쥬리는 1 번 회사에서 출발하여 K 번 회사를 방문한 뒤에
X 번 회사로 가는 것이 목표다. 쥬리가 회사 사이를 이동하는 최소 시간을 계산하는 프로그램을 작성하라.
"""


def find_shortest_time(input: list[int], num_companies: int, k: int, x: int) -> int:
    INF = int(1e9)
    N = num_companies
    t = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        t[i][i] = 0
    for start, end in input:
        t[start][end], t[end][start] = 1, 1

    for middle in range(1, N + 1):
        for start in range(1, N + 1):
            if start == middle:
                continue
            for end in range(1, N + 1):
                if end == middle:
                    continue
                t[start][end] = min(t[start][end], t[start][middle] + t[middle][end])

    return t[1][k] + t[k][x] if t[1][k] + t[k][x] != INF else -1


if __name__ == '__main__':
    cities = [
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 4],
        [3, 4],
        [3, 5],
        [4, 5]
    ]
    print(find_shortest_time(cities, 5, 5, 4))
