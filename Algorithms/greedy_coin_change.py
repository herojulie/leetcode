# 500, 100, 50, 10 원 동전 이용해서 동전 갯수가 최소가 되게 잔돈 거슬러주기

n = 1260
count = 0

coin_set = [500, 100, 50, 10]
for coin in coin_set:
    count += n // coin
    n = n % coin

print(count)
    