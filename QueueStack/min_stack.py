from collections import deque


class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = deque()

    def push(self, val: int) -> None:
        # I dont need to append all the pushed val.
        # ex. cur state: min_stack = [3] stack=[3]
        # now I push 5. 5 will always be popped before 3 as this is a stack.
        # so no need to append it into min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.stack.append(val)
        self.min_stack.append(val)

    def pop(self) -> None:
        removed_node = self.stack.pop()
        if removed_node == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
