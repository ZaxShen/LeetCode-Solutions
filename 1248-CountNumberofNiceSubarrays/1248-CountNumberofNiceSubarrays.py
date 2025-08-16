# Last updated: 8/15/2025, 8:29:59 PM
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1  # Handle empty prefix

        prefix_sum = res = 0
        for num in nums:
            prefix_sum += num % 2  # Key transformation

            # Look for: prefix_sum - target
            if prefix_sum - k in seen:
                # Found! Update result
                res += seen[prefix_sum - k]
            # Update seen
            seen[prefix_sum] += 1

        return res
