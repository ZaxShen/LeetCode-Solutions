# Last updated: 8/15/2025, 8:15:22 PM
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1  # Handle empty prefix
        
        prefix_sum = res = 0
        for num in nums:
            prefix_sum += num  # Key transformation
            
            # Look for: prefix_sum - target
            if prefix_sum - k in seen:
                # Found! Update result
                res += seen[prefix_sum - k]
            seen[prefix_sum] += 1

        return res

