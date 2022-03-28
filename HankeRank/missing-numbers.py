#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    answer = []
    brr.sort()
    arr.sort()
    dist = [0] * 100
    minimum = brr[0]
    for number in brr:
        dist[number - minimum] += 1
    for number in arr:
        dist[number - minimum] -= 1
    for i in range(0, len(dist)):
        if dist[i] > 0:
            answer.append(i + minimum)
    return answer

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)
    print(result)
