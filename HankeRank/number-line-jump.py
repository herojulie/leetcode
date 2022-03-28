#!/bin/python3

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return 'YES'
        return 'NO'

    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    result = kangaroo(0, 2, 5, 3)
    print(result)
