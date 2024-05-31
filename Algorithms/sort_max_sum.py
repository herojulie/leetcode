"""
두 배열의 원소 교체
N 개의 원소로 이루어진 두 개의 배열 A, B 가 있다. (N 은 자연수)
A와 B 사이 최대 K 번의 바꿔치기를 수행하여 만들 수 있는 배열 A 의 모든 원소의 합을 출력하라
"""


def max_sum(a: list[int], b: list[int], k: int) -> int:
    a.sort()
    b.sort()
    return sum(a[k:]) + sum(b[-k:])


if __name__ == '__main__':
    arr1 = [1,2,5,4,3]
    arr2 = [5,5,6,6,5]
    print(max_sum(arr1, arr2, 3))
