# Last updated: 8/16/2025, 12:00:28 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}

        prefix_sum = res = 0
        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            
            if prefix_sum in seen:
                res = max(res, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i

        return res

