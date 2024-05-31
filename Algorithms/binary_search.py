# O(log2 N)


from typing import Optional


def binary_search_recursive(arr: list[int], target: int, start: int, end: int) -> Optional[int]:
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursive(arr, target, start, end)


def binary_search_while(arr: list[int], target: int) -> Optional[int]:
    if not arr:
        return None
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


if __name__ == '__main__':
    ar = [2, 4, 6, 8, 10, 13, 14, 16, 18]
    print(binary_search_recursive(ar, 13, 0, len(ar) - 1))
    print(binary_search_while(ar, 13))
