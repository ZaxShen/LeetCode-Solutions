from collections import deque

class Solution:
    # O(n), O(k)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # Stores indices (not values!)
        res = []
        
        for i in range(len(nums)):
            # Remove indices outside current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices with smaller values (maintain decreasing order)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add current index
            dq.append(i)
            
            # Record maximum when window is complete
            if i >= k - 1:
                res.append(nums[dq[0]])  # Front has max
        
        return res