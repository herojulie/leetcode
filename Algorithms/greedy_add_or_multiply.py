"""
문제: 더하기 혹은 곱하기
각 자리가 숫자 (0-9) 로 이루어진 문자열 S 가 주어졌을 때,
왼쪽부터 오른쪽으로 * 혹은 + 연산을 하여 만들어질 수 있는 가장 큰 수 찾기
"""

nums=[1, 3, 5, 5, 6]
ans = nums[0]

for i, n in enumerate(nums[1:]):
    if ans < 2 or n < 2:
        ans += n
    else:
        ans *= n

print(ans)

