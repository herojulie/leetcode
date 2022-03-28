from collections import deque


class Solution:
    def __init__(self):
        self.stack = deque()

    def get_repeat_number(self):
        repeat = []
        while self.stack and '0' <= self.stack[-1] <= '9':
            repeat.append(self.stack.pop())
        return int(''.join(repeat[::-1]))

    def decode(self):
        s = []
        ch = self.stack.pop()
        while ch != '[':
            s.append(ch)
            ch = self.stack.pop()
        repeat = self.get_repeat_number()
        target_str = ''.join(s[::-1])
        decoded = ''.join([target_str for _ in range(repeat)])
        for ch in decoded:
            self.stack.append(ch)

    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return 0

        size = len(s)
        i = 0
        while i < size:
            if s[i] != ']':
                self.stack.append(s[i])
            else:
                self.decode()
            i += 1

        return ''.join(self.stack)


class Solution2:
    def decodeString(self, s: str) -> str:
        stack = deque()
        i = 0
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
            else:
                repeat = []
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.append(stack.pop())

                # discard [
                stack.pop()

                while stack and '0' <= stack[-1] <= '9':
                    repeat.append(stack.pop())

                converted_repeat = int(''.join(repeat[::-1]))
                converted_tmp = ''.join(tmp[::-1])
                decoded_str = converted_repeat * converted_tmp

                for ch in decoded_str:
                    stack.append(ch)
            i += 1

        return ''.join(stack)


if __name__ == '__main__':
    print(Solution2().decodeString(s="2[abc]3[cd]ef"))
