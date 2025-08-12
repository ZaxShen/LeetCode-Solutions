# Last updated: 8/11/2025, 9:22:46 PM
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left = 0  # Start at 0, not -1
        max_len = 0
        
        for right, num in enumerate(nums):
            # Expand window by including current element
            freq[num] += 1
            
            # Contract window while current element frequency exceeds k
            while freq[num] > k:
                # Remove leftmost element from window
                freq[nums[left]] -= 1
                # if freq[nums[left]] == 0:
                #     del freq[nums[left]]  # Clean up empty entries
                left += 1
            
            # Update maximum window length seen so far
            max_len = max(max_len, right - left + 1)
        
        return max_len