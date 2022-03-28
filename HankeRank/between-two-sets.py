#!/bin/python3

def is_factors(arr: [int], num):
    for n in arr:
        if num % n != 0:
            return False
    return True


def is_factor(num, arr:[int]):
    for n in arr:
        if n % num != 0:
            return False
    return True


def getTotalX(a, b):
    # Write your code here
    a.sort()
    b.sort()
    candidate = []
    for number in range(a[-1], b[0] + 1):
        if is_factors(a, number) and is_factor(number, b):
            candidate.append(number)
    return len(candidate)


if __name__ == '__main__':
    print(getTotalX([2, 4], [16, 32, 96]))
