#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
arr: [[int]]
lastAnswer = 0
answer = []
N = 0


def init(n):
    global arr, lastAnswer, answer, N
    arr = [[] for i in range(n)]
    lastAnswer = 0
    answer = []
    N = n


def get_idx(x: int) -> int:
    return (x ^ lastAnswer) % N


def do_func_one(x: int, y: int):
    idx = get_idx(x)
    arr[idx].append(y)


def do_func_two(x: int, y: int):
    global lastAnswer
    idx = get_idx(x)
    lastAnswer = arr[idx][y % len(arr[idx])]
    answer.append(lastAnswer)


def dynamicArray(n, queries):
    # Write your code here
    init(n)

    for query in queries:
        if query[0] == 1:
            do_func_one(query[1], query[2])
        elif query[0] == 2:
            do_func_two(query[1], query[2])

    return answer


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
