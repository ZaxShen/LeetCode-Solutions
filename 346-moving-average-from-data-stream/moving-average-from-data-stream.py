from collections import deque

class MovingAverage:
    # O(1), O(n)
    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)

        if len(self.q) > self.size:
            self.sum += val - self.q.popleft()
        else:
            self.sum += val

        res = self.sum / len(self.q)
        
        return res


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)