from collections import deque


class MyStack:
    def __init__(self):
        self.head_q = deque()
        self.tail_q = deque()

    def push(self, x: int) -> None:
        while self.tail_q:
            self.head_q.append(self.tail_q.popleft())
        self.tail_q.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        node = self.tail_q.popleft()
        while len(self.head_q) > 1:
            self.tail_q.append(self.head_q.popleft())
        self.head_q, self.tail_q = self.tail_q, self.head_q
        return node

    def top(self) -> int:
        if self.empty():
            return None
        return self.tail_q[0]

    def empty(self) -> bool:
        return True if len(self.tail_q) == 0 else False

["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
# Your MyStack object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    param_5 = obj.top()
    param_6 = obj.pop()
    print(param_2, param_3, param_4, param_5, param_6)