#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive: int = 0
    negative: int = 0
    zero: int = 0

    if len(arr) == 0:
        return format_answer(0.0), format_answer(0.0), format_answer(0.0)

    for element in arr:
        if element > 0:
            positive += 1
        elif element == 0:
            zero += 1
        else:
            negative += 1

    print(format_answer(positive / len(arr)))
    print(format_answer(negative / len(arr)))
    print(format_answer(zero / len(arr)))


def format_answer(number: float) -> float:
    return format(number, '.6f')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
