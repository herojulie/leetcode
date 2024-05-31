"""
특정한 합을 가지는 부분 연속 수열 갯수 찾기
"""


def two_pointer(arr: list[int], target: int) -> int:
    end = 0
    count = 0
    total = 0

    for start in range(len(arr)):
        while total < target and end < len(arr):
            total += arr[end]
            end += 1
        if total == target:
            count += 1
        total -= arr[start]

    return count


if __name__ == '__main__':
    ar = [1, 2, 3, 2, 5]
    print(two_pointer(ar, 5))
