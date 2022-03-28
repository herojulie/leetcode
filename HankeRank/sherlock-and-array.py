#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#
sum_up_to_index: [int]


def init_sum_up_to_index(arr: [int]) -> None:
    global sum_up_to_index
    sum_up_to_index = [0] * len(arr)
    sum_so_far = 0
    for i in range(len(arr)):
        sum_so_far += arr[i]
        sum_up_to_index[i] = sum_so_far


def find_answer() -> str:
    global sum_up_to_index

    if sum_up_to_index[-1] - sum_up_to_index[0] == 0:
        return 'YES'
    if sum_up_to_index[-2] == 0:
        return 'YES'

    for i in range(1, len(sum_up_to_index) - 1):
        sum_left = sum_up_to_index[i - 1]
        sum_right = sum_up_to_index[-1] - sum_up_to_index[i]
        if sum_left == sum_right:
            return 'YES'

    return 'NO'


def balancedSums(arr):
    # Write your code here
    init_sum_up_to_index(arr)
    return find_answer()


if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result + '\n')

