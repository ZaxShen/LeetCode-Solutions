from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for i, v in enumerate(nums):
            # Check q
            while q and nums[q[-1]] < v:
                q.pop()
            q.append(i)

            # Check window size
            if q[0] + k == i:
                q.popleft()

            # Get window max
            if i >= k - 1:
                res.append(nums[q[0]])

        return res
