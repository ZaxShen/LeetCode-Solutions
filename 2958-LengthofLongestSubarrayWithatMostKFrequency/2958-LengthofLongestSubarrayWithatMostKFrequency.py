# Last updated: 8/11/2025, 9:24:41 PM
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left = 0
        max_len = 0
        
        for right, num in enumerate(nums):
            # Expand window: add current element
            freq[num] += 1
            
            # Contract window: remove elements from left until valid
            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Update maximum length (standard formula)
            max_len = max(max_len, right - left + 1)
        
        return max_len