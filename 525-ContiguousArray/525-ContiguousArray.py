# Last updated: 8/15/2025, 11:14:20 PM
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Define seen and handle empty 
        seen = {0: -1}

        prefix_sum = res = 0
        for i, num in enumerate(nums):
            # Update prefix_sum
            prefix_sum += 1 if num == 1 else -1

            # Looking for a valid prefix_sum
            if prefix_sum in seen:
                res = max(res, i - seen[prefix_sum])
            else:
                # Update seen
                seen[prefix_sum] = i

        return res
