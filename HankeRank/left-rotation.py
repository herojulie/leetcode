#!/bin/python3

def rotateLeft(d, arr):
    # Write your code here
    if d == len(arr):
        return arr

    answer_left = arr[0:d]
    answer_right = arr[d:len(arr)]
    return answer_right + answer_left


if __name__ == '__main__':
    result = rotateLeft(d, arr)
    print(result)

