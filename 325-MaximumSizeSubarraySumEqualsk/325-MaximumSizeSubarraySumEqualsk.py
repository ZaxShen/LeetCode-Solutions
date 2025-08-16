# Last updated: 8/16/2025, 2:47:55 AM
class Solution:
    # O(n), O(n)
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Handle empty prefix
        seen = {0: -1}

        prefix_sum = res = 0
        for i, num in enumerate(nums):
            prefix_sum += num

            # Look for: prefix_sum - target
            if (prefix_sum - k) in seen:
                # Found! Update result
                res = max(res, i - seen[prefix_sum - k])

            # Update seen: Store first occurrence only (for maximum length)
            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return res
