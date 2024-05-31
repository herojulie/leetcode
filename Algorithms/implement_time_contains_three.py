"""
시각.
정수 N 이 입력되면, 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오. ( 0 <= N <= 23 )
- 00시 00분 03초 -> 카운트
- 01시 00분 21초 -> !카운트
"""

N = 5
count = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in f'{str(h)}:{str(m)}:{str(s)}':
                count += 1
print(count)


def my_func(n: int) -> int:
    exclude_three = 5 * 9 * 5 * 9
    hr = 60 * 60
    answer = 0
    for i in range(n + 1):
        if i != 3 and i != 13 and i != 23:
            answer += (hr - exclude_three)
        else:
            answer += hr
    return answer

print(my_func(N))
