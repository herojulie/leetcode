#!/bin/python3

def is_next_matched(expected: str, start_i: int, s: str) -> int:
    if len(expected) <= (len(s) - start_i):
        end_i = start_i + len(expected)
        next_n = s[start_i: end_i]
        return end_i if int(expected) == int(next_n) else -1
    else:
        return -1


def checkRules(s, split) -> bool:
    expected = int(s[0:split]) + 1
    next_i = split
    while next_i < len(s):
        next_i = is_next_matched(str(expected), next_i, s)
        if next_i == -1:
            return False
        expected += 1
    return True


def separateNumbers(s):
    # Write your code here
    if len(s) == 1:
        print('NO')
        return

    for split in range(1, len(s)):
        if checkRules(s, split):
            print(f'YES {s[0:split]}')
            return
    print('NO')


if __name__ == '__main__':
    separateNumbers("1")
