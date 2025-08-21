class Solution:
    # O(n), O(n)
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = {0: 1}
        prefix = res = 0

        for num in nums:
            prefix += num
            lookup = prefix - goal

            # if lookup in seen:
                # res += seen[lookup]
            res += seen.get(lookup, 0)

            seen[prefix] = seen.get(prefix, 0) + 1

        return res
