class MyCircularQueue:
    def __init__(self, k: int):
        self.MAX = k
        self.queue = [-1 for i in range(self.MAX)]
        self.head, self.tail = -1, -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head, self.tail = 0, 0
            self.queue[self.head] = value
            return True

        self.tail = self.tail + 1 if self.tail + 1 < self.MAX else 0
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.head] = -1
        if self.head == self.tail:
            self.head, self.tail = -1, -1
        else:
            self.head = self.head + 1 if self.head + 1 < self.MAX else 0
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return self.head == self.tail + 1 or (self.head == 0 and self.tail == self.MAX - 1)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()


if __name__ == '__main__':
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1))
    print(myCircularQueue.enQueue(2))
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.deQueue())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.enQueue(5))
    print(myCircularQueue.deQueue())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.deQueue())
