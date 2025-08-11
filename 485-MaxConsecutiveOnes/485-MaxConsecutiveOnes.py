# Last updated: 8/11/2025, 11:15:31 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = curr_len = 0

        for num in nums:
            if num == 1:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0

        return max_len