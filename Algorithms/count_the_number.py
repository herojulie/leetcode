"""
정렬된 배열에서 특정 수의 개수 구하기
N 개의 원소를 포함하고 있는 수열이 오름차순 정렬되어 있다.
이 수열에서 x 가 등장하는 횟수를 구하라. 시간복잡도 O(logN)
ex. {1,1,2,2,2,2,3} x = 2 일 경우, 답은 4
"""

from bisect import bisect_left, bisect_right


def count_number(arr: list[int], target: int):
    left_index = bisect_left(arr, target, 0, len(arr) - 1)
    right_index = bisect_right(arr, target, 0, len(arr) - 1)
    print(right_index - left_index)


def binary_search_lowest(arr: list[int], target: int):
    start, end = 0, len(arr) - 1
    ans = end + 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            ans = min(ans, mid)
            end = mid - 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return ans


def binary_search_highest(arr: list[int], target: int):
    start, end = 0, len(arr) - 1
    ans = start - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            ans = max(ans, mid)
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return ans


if __name__ == '__main__':
    array = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    # using built-in method
    count_number(array, target)

    # binary search
    left_index = binary_search_lowest(array, target)
    right_index = binary_search_highest(array, target)
    ans = -1 if left_index == -1 else right_index - left_index + 1
    print(ans)
