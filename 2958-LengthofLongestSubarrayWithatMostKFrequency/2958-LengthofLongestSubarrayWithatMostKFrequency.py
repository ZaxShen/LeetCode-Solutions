# Last updated: 8/15/2025, 4:26:20 PM
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = res = 0

        for right, num in enumerate(nums):
            counter[num] += 1
            
            while counter[num] > k:
                counter[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res       
        