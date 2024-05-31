"""
구간 합 빠르게 계산하기
N 개의 정수로 구성된 수열이 있다.
[int, int] 형식의 M 개의 쿼리가 주어졌을 때, 각 쿼리에 대한 sum(arr[left:right+1]) 을 출력하라.
"""


def prefix_sum(arr: list[int], input: list[list[int]]) -> list[int]:
    acc = [0] * len(arr)
    acc[0] = arr[0]
    for i in range(1, len(arr)):
        acc[i] += acc[i - 1] + arr[i]

    ans = []
    for start, end in input:
        if start <= end:
            result = acc[end] - acc[start - 1] if start > 0 else acc[end]
        else:
            result = None
        ans.append(result)
    return ans


if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    queries = [
        [2, 3],
        [1, 4],
        [5, 6],
        [0, 7],
        [4, 3]
    ]
    print(prefix_sum(arr, queries))
