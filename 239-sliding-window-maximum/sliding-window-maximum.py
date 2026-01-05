from collections import deque

class Solution:
    # O(n), O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        desc_queue = deque()
        res = []

        for idx, i in enumerate(nums):
            while desc_queue and nums[desc_queue[-1]] < i:
                desc_queue.pop()
            desc_queue.append(idx)

            # Maintain window size
            if desc_queue[0] + k == idx:
                desc_queue.popleft()

            # Append window maximum
            if idx + 1 >= k:
                res.append(nums[desc_queue[0]])

        return res

