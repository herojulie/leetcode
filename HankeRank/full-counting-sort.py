#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    max_x = 0
    for x, _ in arr:
        max_x = int(x) if int(x) > max_x else max_x

    temp = [[] for n in range(max_x + 1)]

    mid = len(arr) // 2
    for index in range(len(arr)):
        x: int = int(arr[index][0])
        s: str = arr[index][1]
        if index < mid:
            temp[x].append('-')
        else:
            temp[x].append(s)

    answer = ''
    for item in temp:
        if len(item) > 0:
            answer += ' '.join(item) + ' '

    print(answer)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
