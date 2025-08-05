# Last updated: 8/4/2025, 10:43:29 PM
from collections import defaultdict

class Solution:
	# O(n), O(n)
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        left, max_len = -1, 0

        for right, num in enumerate(nums):
            freq[num] += 1
            while freq[num] > k:
                print(left)
                left += 1
                freq[nums[left]] -= 1
            max_len = max(max_len, right - left)
            # print(nums)

        return max_len