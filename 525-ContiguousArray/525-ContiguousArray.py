# Last updated: 8/15/2025, 8:44:30 PM
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        seen[0] = -1  # Handle empty prefix

        prefix_sum = res = 0
        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            # Look for: prefix_sum - target
            if prefix_sum in seen:
                # Found! Update result
                res = max(res, i - seen[prefix_sum])
            # Update seen
            else:
                seen[prefix_sum] = i
            
        return res
