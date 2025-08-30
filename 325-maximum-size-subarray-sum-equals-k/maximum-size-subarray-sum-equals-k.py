class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        seen = {0: -1}
        prefix = res = 0

        for i, num in enumerate(nums):
            prefix += num
            lookup = prefix - k

            if lookup in seen:
                res = max(res, i - seen[lookup])

            if prefix in seen:
                seen[prefix] = min(seen[prefix], i)
            else:
                seen[prefix] = i

        return res