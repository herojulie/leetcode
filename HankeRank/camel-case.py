#!/bin/python3

class Operation:
    SPLIT = 'S'
    COMBINE = 'C'


class Type:
    METHOD = 'M'
    CLASS = 'C'
    VARIABLE = 'V'


def do_conversion(testcase):
    # Write your code here
    op, tp, word = [string.strip('()') for string in testcase.split(';')]
    answer = ''
    if op == Operation.SPLIT:
        answer = word[0].lower()
        for i in range(1, len(word)):
            answer += word[i] if word[i].islower() else f' {word[i].lower()}'
    elif op == Operation.COMBINE:
        answer = word[0].upper() if tp == Type.CLASS else word[0].lower()
        case_toggle_flag = False
        for i in range(1, len(word)):
            if word[i] == ' ':
                case_toggle_flag = True
                continue

            if case_toggle_flag:
                answer += word[i].upper()
                case_toggle_flag = False
            else:
                answer += word[i].lower()
        answer += '()' if tp == Type.METHOD else ''

    print(answer)


if __name__ == '__main__':
    while True:
        try:
            s = input().strip()
            do_conversion(s)
        except EOFError:
            break;