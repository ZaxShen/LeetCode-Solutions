from collections import deque

class Solution:
    # O(n), O(1)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for idx, i in enumerate(nums):
            while dq and nums[dq[-1]] < i:
                dq.pop()
            dq.append(idx)

            if dq[0] + k == idx:
                dq.popleft()

            if idx + 1 >= k:
                res.append(nums[dq[0]])

        return res