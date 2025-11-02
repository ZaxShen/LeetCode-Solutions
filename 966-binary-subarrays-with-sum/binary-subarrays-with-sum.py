from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        res = prefix = 0

        for i in nums:
            prefix += i
            lookup = prefix - goal

            if lookup in seen:
                res += seen[lookup]

            seen[prefix] += 1

        return res
            