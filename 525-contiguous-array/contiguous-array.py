class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        prefix = res = 0

        for i, num in enumerate(nums):
            prefix += 1 if num == 1 else -1

            if prefix in seen:
                res = max(res, i - seen[prefix])
            
            if prefix not in seen:
                seen[prefix] = i

        return res