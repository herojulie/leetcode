#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def gamingArray(arr):
    # Write your code here
    max_count = 0
    max_value = arr[0]
    for e in arr[1:]:
        if e > max_value:
            max_value = e
            max_count += 1

    return 'BOB' if max_count % 2 == 0 else 'ANDY'


if __name__ == '__main__':
    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        print(result + '\n')
