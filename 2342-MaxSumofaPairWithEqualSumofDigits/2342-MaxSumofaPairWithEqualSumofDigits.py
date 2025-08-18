# Last updated: 8/18/2025, 9:08:03 AM
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        largest_seen = {}

        max_sum = -1
        for num in nums:
            digits_sum = sum(map(int, str(num)))
            if digits_sum in largest_seen:
                max_sum = max(max_sum, num + largest_seen[digits_sum])
            largest_seen[digits_sum] = max(largest_seen.get(digits_sum, -1), num)

        return max_sum

