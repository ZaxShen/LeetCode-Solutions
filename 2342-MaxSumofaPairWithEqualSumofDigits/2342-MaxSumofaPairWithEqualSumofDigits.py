# Last updated: 8/17/2025, 7:07:30 PM
from collections import defaultdict, Counter

class Solution:
    # O(n*m), O(k)
    def maximumSum(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        max_sum = -1
        
        for num in nums:
            sum_digits = sum(map(int, str(num)))
            if sum_digits in seen:
                max_sum = max(max_sum, seen[sum_digits] + num)
            seen[sum_digits] = max(num, seen[sum_digits])

        return max_sum