#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def get_xor(arr: [int]):
    if len(arr) == 1:
        return arr[0]
    else:
        xor = arr[0] ^ arr[1]
        for i in range(2, len(arr)):
            xor ^= arr[i]
        return xor

def sansaXor(arr):
    # Write your code here
    if len(arr) % 2 == 0:
        return 0
    sub_result = []
    num_element = (len(arr) + 1) // 2
    for i in range(num_element):
        if (i + 1) % 2 == 1:
            sub_result.append(arr[i])
            sub_result.append(arr[len(arr) - 1 - i])
    if num_element % 2 == 1:
        sub_result.append(arr[num_element])
    return get_xor(sub_result)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        print(str(result) + '\n')

