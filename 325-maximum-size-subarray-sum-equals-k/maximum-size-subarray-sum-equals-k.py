class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        prefix = max_len = 0

        for i, num in enumerate(nums):
            prefix += num
            lookup = prefix - k

            if lookup in seen:
                max_len = max(max_len, i - seen[lookup])

            # Storing the 1st appearance for max length
            if prefix not in seen:
                seen[prefix] = i

        return max_len
