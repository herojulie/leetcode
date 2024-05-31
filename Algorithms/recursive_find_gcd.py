"""
최대 공약수 찾기
두 개의 자연수에 대한 최대 공약수를 찾으셈
"""


def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == '__main__':
    print(gcd(192, 162))
