# Last updated: 8/12/2025, 7:39:07 PM
from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = 0
        max_len = 0

        for right, num in enumerate(nums):
            counter[num] += 1
            while counter[num] > k:
                counter[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len