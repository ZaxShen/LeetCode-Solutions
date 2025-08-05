# Last updated: 8/4/2025, 10:46:30 PM
from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        queue = self.queue
        queue.append(t)
        while queue[0] < t - 3000:
            queue.popleft()

        return len(queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)