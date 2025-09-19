from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        res = -1

        for num in nums:
            digit_sum = sum(map(int, str(num)))
            if digit_sum in seen:
                res = max(res, seen[digit_sum] + num)
            
            seen[digit_sum] = max(num, seen[digit_sum])

        return res
