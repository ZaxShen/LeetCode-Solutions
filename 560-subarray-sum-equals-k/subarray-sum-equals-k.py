from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        prefix = res = 0

        for i in nums:
            prefix += i
            target = prefix - k

            if target in seen:
                res += seen[target]

            if prefix in seen:
                seen[prefix] += 1
            else:
                seen[prefix] = 1

        return res