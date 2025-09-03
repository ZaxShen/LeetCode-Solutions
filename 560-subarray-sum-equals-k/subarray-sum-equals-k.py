from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = Counter()
        seen[0] = 1
        prefix = count = 0

        for i, num in enumerate(nums):
            prefix += num
            lookup = prefix - k

            count += seen[lookup]

            seen[prefix] += 1

        return count