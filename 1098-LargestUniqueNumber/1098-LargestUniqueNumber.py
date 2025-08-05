# Last updated: 8/4/2025, 10:46:23 PM
from collections import defaultdict

class Solution:
    # O(n), O(k)
    def largestUniqueNumber(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        max_num = -1
        
        for i in nums:
            counts[i] += 1
            
        for k, v in counts.items():
            if v == 1:
                max_num = max(max_num, k)
                
        return max_num