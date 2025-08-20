from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1

        prefix_sum = res = 0
        for num in nums:
            prefix_sum += num
            lookup = prefix_sum - goal

            res += seen[lookup]

            seen[prefix_sum] += 1

        return res
