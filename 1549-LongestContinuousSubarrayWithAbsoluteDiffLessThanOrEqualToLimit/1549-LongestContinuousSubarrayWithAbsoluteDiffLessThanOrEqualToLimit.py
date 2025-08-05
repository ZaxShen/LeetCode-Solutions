# Last updated: 8/4/2025, 10:45:15 PM
from collections import deque

class Solution:
    # O(n), O(n)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        result = 0
        left = 0

        for right, num in enumerate(nums):
            while increasing and increasing[-1] > num:
                increasing.pop()
            while decreasing and decreasing[-1] < num:
                decreasing.pop()
            
            increasing.append(num)
            decreasing.append(num)

            # print(increasing, decreasing)
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == increasing[0]:
                    increasing.popleft()
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                left += 1
            
            result = max(result, right - left + 1)

        return result