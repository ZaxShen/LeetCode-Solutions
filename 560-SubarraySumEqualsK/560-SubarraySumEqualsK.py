# Last updated: 8/14/2025, 11:10:53 AM
from collections import defaultdict, Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix = defaultdict(int)
        prefix = Counter()
        # Initialize with 0:1 to handle the case when curr equals k
        prefix[0] = 1
        curr = count = 0

        for num in nums:
            curr += num
            count += prefix[curr - k]
            prefix[curr] += 1

        return count

        