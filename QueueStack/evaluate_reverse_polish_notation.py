from typing import List
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        operators = ['+', '-', '*', '/']
        stack = deque()
        for token in tokens:
            if token in operators:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if token == '+':
                    stack.append(operand_1 + operand_2)
                elif token == '-':
                    stack.append(operand_1 - operand_2)
                elif token == '*':
                    stack.append(operand_1 * operand_2)
                elif token == '/':
                    stack.append(int(operand_1 / operand_2))
            else:
                stack.append(int(token))
        return stack[-1]


if __name__ == '__main__':
    print(Solution().evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
