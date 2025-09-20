from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        prefix = res = 0

        for i, num in enumerate(nums):
            prefix += num
            target = prefix - k

            if target in seen:
                res = max(res, i - seen[target])

            if prefix not in seen:
                seen[prefix] = i

        return res
