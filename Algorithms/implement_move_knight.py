"""
왕실의 나이트
8 * 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는
경우의 수를 출력하시오. 열 위치는 a 부터 h 로 표현합니다.
c2 = (2,c)
"""

MAX = 8


def my_func(loc: str) -> int:
    directions = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                  (2, -1), (1, -2), (-1, -2), (-2, -1)]
    ans = 0
    # 주의. 주어진 좌표에서 앞이 y 임
    x, y = int(loc[1]), ord(loc[0]) - 96
    for d in directions:
        new_x, new_y = x + d[0], y + d[1]
        if (1 <= new_x <= MAX) and (1 <= new_y <= MAX):
            ans += 1
    return ans


print(my_func('a1'))
