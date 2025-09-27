from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        desc = deque()
        res = []

        for i, num in enumerate(nums):
            # Monotonic queue in descending order
            while desc and nums[desc[-1]] < num:
                desc.pop()
            desc.append(i)

            # Maintain queue size
            if desc[0] + k == i:
                desc.popleft()

            # Append res
            if i + 1 >= k:
                res.append(nums[desc[0]])

        return res