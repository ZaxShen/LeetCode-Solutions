from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i, num in enumerate(nums):
            # Maintain monotonic queue in descending order
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)

            # Maintain window size
            if dq[0] + k == i:
                dq.popleft()

            # Check if window_size valid
            if i + 1 >= k:
                res.append(nums[dq[0]])

        return res
