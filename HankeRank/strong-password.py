#!/bin/python3
MIN_LENGTH = 6
numbers = [c for c in "0123456789"]
lower_cases = [c for c in "abcdefghijklmnopqrstuvwxyz"]
upper_cases = [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
specials = [c for c in "!@#$%^&*()-+"]


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    number = lower = upper = special = 1
    for c in password:
        if c in numbers:
            number = 0
        elif c in lower_cases:
            lower = 0
        elif c in upper_cases:
            upper = 0
        elif c in specials:
            special = 0

    ans1 = number + lower + upper + special
    ans2 = MIN_LENGTH - len(password)
    return ans1 if ans1 > ans2 else ans2


if __name__ == '__main__':
    answer = minimumNumber(11, '#HackerRank')
    print(answer)
