#!/bin/python3

def get_difference(a: int, b: int) -> int:
    return abs(a - b) if a >= b else abs(b - a)


def closestNumbers(arr: [int]):
    # Write your code here
    arr.sort()
    min_diff = get_difference(arr[0], arr[1])
    answer = []
    for i in range(1, len(arr)):
        diff = get_difference(arr[i - 1], arr[i])
        if min_diff > diff:
            min_diff = diff
            answer = [arr[i - 1], arr[i]]
        elif min_diff == diff:
            answer = answer + [arr[i-1], arr[i]]
    return answer


if __name__ == '__main__':
    print(closestNumbers([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))
    # print(closestNumbers([5, 4, 3, 2, 1]))
