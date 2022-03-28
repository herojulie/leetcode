#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    first = s[:mid]
    second = s[mid:]
    first_count = [0 for i in range(26)]
    second_count = [0 for i in range(26)]
    INT_A = ord('a')
    delta = 0

    for i in range(mid):
        first_i = ord(first[i]) - INT_A
        first_count[first_i] += 1
        second_i = ord(second[i]) - INT_A
        second_count[second_i] += 1

    for i in range(26):
        if first_count[i] > second_count[i]:
            delta += first_count[i] - second_count[i]

    return delta


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result) + '\n')
