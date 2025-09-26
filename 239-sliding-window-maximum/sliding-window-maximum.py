from collections import deque

class Solution:
    # O(n), O(k)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res = []
        queue = deque()
        
        for i, num in enumerate(nums):
            # Maintain monotonic decreasing
            while queue and num > nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            # Remove the oldest num exceeding the window size
            if queue[0] + k == i:
                queue.popleft()

            # Only add to the answer once our window has reached size k
            if i >= k - 1:
                res.append(nums[queue[0]])

        return res