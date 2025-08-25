from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        
        prefix = count = 0

        for num in nums:
            prefix += num
            lookup = prefix - goal

            count += seen[lookup]

            seen[prefix] += 1

        return count