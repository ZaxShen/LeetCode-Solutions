# Last updated: 8/16/2025, 12:14:40 PM
class Solution:
    # O(n), O(n)
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}  # Handle empty prefix

        prefix_sum = res = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            lookup = prefix_sum - k

            if lookup in seen:
                res = max(res, i - seen[lookup])

            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return res

