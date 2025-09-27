from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i, num in enumerate(nums):
            # Maintain queue in descending order
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)

            # Maintain queue size
            if dq[0] + k == i:
                dq.popleft()

            # Add result
            if i + 1 >= k:
                res.append(nums[dq[0]])

        return res