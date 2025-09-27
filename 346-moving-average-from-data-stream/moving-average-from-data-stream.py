from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.win_size = size
        self.q = deque()
        self.moving_sum = 0

    def next(self, val: int) -> float:
        q, win_size = self.q, self.win_size

        q.append(val)
        self.moving_sum += val
        if len(q) > win_size:
            self.moving_sum -= q.popleft()
        
        return self.moving_sum / len(q)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)