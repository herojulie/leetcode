"""
상하좌우.
여행가 A 는 N*N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 * 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1) 이고, 가장 오른쪽 아래 좌표는 (N, N) 이다.
여행가 A 는 상하좌우로 이동할 수 있고, 시작 좌표는 항상 (1, 1) 이다.
A 의 이동 계획이 적힌 계획서를 참고하여 최종 위치를 출력하라.
이 때 N * N 범위를 벗어나는 움직임은 무시한다.
계획서 포맷: L L R U D
의미: left -> left -> right -> up -> down
"""

dir = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
MAX = 5
plan = 'R R R D D'

x, y = 1, 1
for next_move in plan.split():
    new_x, new_y = x + dir[next_move.upper()][0], y + dir[next_move.upper()][1]
    if (1 <= new_x <= MAX) and (1 <= new_y <= MAX):
        x, y = new_x, new_y

print(x, y)
