"""
선택정렬, 삽입정렬 둘다 O(N^2)
"""


# 선택 정렬 O(N^2)
def selection_sort(arr: list[int]):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


# 삽입 정렬 O(N^2)
def insertion_sort(arr: list[int]):
    # 삽입정렬은 이미 정렬되어 있을 경우, 매번 break 걸리므로 O(N) 이 된다
    for i in range(1, len(arr)):
        # for (j = i; j > 0; j--)
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    print(arr)


# 퀵 정렬 O(N log N). 최악의 경우 O(N^2) : 이미 정렬된 배열에 대해 퀵 정렬을 수행할 때
def quick_sort(arr: list[int], start, end) -> list[int]:
    # 원소가 1개인 경우
    if start >= end:
        return arr
    pivot = start
    left, right = start + 1, end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        # 엇갈린 경우 작은 데이터와 피벗 교체
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr = quick_sort(arr, start, right - 1)
    arr = quick_sort(arr, right + 1, end)
    return arr


# 카운팅 소트 O(N + K)
def counting_sort(arr: list[int], max_num: int):
    count = [0] * (max_num + 1)
    ans = list()

    for i in arr:
        count[i] += 1
    for j in range(len(count)):
        for k in range(count[j]):
            ans.append(j)
    print(ans)


if __name__ == '__main__':
    numbers = [5, 2, 5, 8, 4, 6, 7, 9, 2, 3, 5, 8]
    selection_sort(numbers)
    insertion_sort(numbers)
    print(quick_sort(numbers, 0, len(numbers) - 1))
    counting_sort(numbers, 9)
