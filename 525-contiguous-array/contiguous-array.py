from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        seen[0] = -1
        prefix = res = 0

        for idx, i in enumerate(nums):
            prefix += 1 if i == 1 else -1
            
            if prefix in seen:
                res = max(res, idx - seen[prefix])

            if prefix not in seen:
                seen[prefix] = idx

        return res