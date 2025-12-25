class MyQueue:

    def __init__(self):
        self.enstack = []
        self.destack = []

    def push(self, x: int) -> None:
        self.enstack.append(x)

    def pop(self) -> int:
        self.peek()

        return self.destack.pop()

    def peek(self) -> int:
        enstack, destack = self.enstack, self.destack

        if not destack:
            while enstack:
                destack.append(enstack.pop())

        return destack[-1]
    

    def empty(self) -> bool:
        return not self.enstack and not self.destack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()