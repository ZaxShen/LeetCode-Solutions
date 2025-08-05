# Last updated: 8/4/2025, 10:46:31 PM
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = res  = 0

        for num in nums:
            curr += num
            res += prefix[curr - goal]
            prefix[curr] += 1

        return res