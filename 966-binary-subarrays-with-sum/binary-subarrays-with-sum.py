from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefix = res = 0

        for num in nums:
            prefix += num
            target = prefix - goal

            if target in seen:
                res += seen[target]

            seen[prefix] += 1

        return res

