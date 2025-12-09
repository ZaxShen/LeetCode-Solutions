from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefix = res = 0

        for i in nums:
            prefix += i
            target = prefix - k

            res += seen[target]

            seen[prefix] += 1

        return res