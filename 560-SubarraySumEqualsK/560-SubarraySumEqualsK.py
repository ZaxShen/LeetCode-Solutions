# Last updated: 8/15/2025, 8:14:56 PM
from collections import defaultdict


class Solution:
    # O(n), O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        # Initialize with 0:1 to handle the case when prefix_sum equals k
        seen[0] = 1

        prefix_sum = res = 0
        for num in nums:
            prefix_sum += num
            # Find the number of subarrays ending here with sum k
            if prefix_sum - k in seen:
                res += seen[prefix_sum - k]
            # Record the current sum into the map
            seen[prefix_sum] += 1

        return res
