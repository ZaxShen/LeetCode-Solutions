# Last updated: 8/4/2025, 10:45:41 PM
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = count = 0

        for num in nums:
            curr += num % 2
            count += prefix[curr - k]
            prefix[curr] += 1

        return count
        