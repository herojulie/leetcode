# 다음의 두 과정 중 하나를 반복적으로 선택. N을 1로 만드는 최소 횟수 구하기
# 1. N-1
# 2. N // K ( N % K == 0 일 때만 가능 )

n = 17
k = 4
count = 0

while True:
    target = (n // k) * k
    count += n - target

    n = target
    if n < k:
        count += n - 1
        break

    count += 1
    n //= k

# while n > 1:
#     if n % k == 0:
#         print(f'{n // k} = {n} // {k}')
#         n = n // k
#     else:
#         print(f'{n - 1} = {n} - 1')
#         n -= 1
#     count += 1

print(count)
