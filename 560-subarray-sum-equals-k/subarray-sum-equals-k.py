class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}
        prefix = count = 0

        for i, num in enumerate(nums):
            prefix += num
            lookup = prefix - k

            count += seen.get(lookup, 0)

            seen[prefix] = seen.get(prefix, 0) + 1

        return count