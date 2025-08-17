# Last updated: 8/16/2025, 10:53:31 PM
from collections import Counter

class Solution:
    # O(n), O(n)
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
        