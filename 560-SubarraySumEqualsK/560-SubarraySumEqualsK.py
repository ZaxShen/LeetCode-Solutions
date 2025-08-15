# Last updated: 8/15/2025, 4:43:26 PM
from collections import defaultdict

class Solution:
    # O(n), O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        # Init prefix
        prefix[0] = 1
        curr = count = 0

        for i, v in enumerate(nums):
            curr += v
            count += prefix[curr - k]
            prefix[curr] += 1

        return count