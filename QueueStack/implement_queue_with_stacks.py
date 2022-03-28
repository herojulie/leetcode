from collections import deque

class MyQueue:
    def __init__(self):
        self.stack_for_push = deque()
        self.stack_for_pop = deque()

    def push(self, x: int) -> None:
        while self.stack_for_pop:
            self.stack_for_push.append(self.stack_for_pop.pop())
        self.stack_for_push.append(x)

    def pop(self) -> int:
        while self.stack_for_push:
            self.stack_for_pop.append(self.stack_for_push.pop())
        return self.stack_for_pop.pop()

    def peek(self) -> int:
        while self.stack_for_push:
            self.stack_for_pop.append(self.stack_for_push.pop())
        return self.stack_for_pop[-1] if not self.empty() else None

    def empty(self) -> bool:
        return False if self.stack_for_push or self.stack_for_pop else True


# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Your MyQueue object will be instantiated and called as such:
if __name__ =='__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_3 = obj.peek()
    param_2 = obj.pop()
    param_4 = obj.empty()

    print(param_3, param_2, param_4)
