#!/bin/python3

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2)
    a[mid - 1], a[n - 1] = a[n - 1], a[mid - 1]

    st = mid
    ed = n - 2
    while st < ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


if __name__ == '__main__':
    findZigZagSequence([1, 2, 3, 4, 5, 6, 7], 7)
