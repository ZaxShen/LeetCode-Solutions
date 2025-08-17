# Last updated: 8/17/2025, 7:22:31 PM
from collections import defaultdict

class Solution:
    # O(n*logm), O(k)
    def maximumSum(self, nums: List[int]) -> int:
        largest_seen = defaultdict(int)
        max_sum = -1
        
        for num in nums:
            digit_sum = sum(map(int, str(num)))
            
            if digit_sum in largest_seen:
                max_sum = max(max_sum, largest_seen[digit_sum] + num)
            
            largest_seen[digit_sum] = max(num, largest_seen[digit_sum])
        
        return max_sum