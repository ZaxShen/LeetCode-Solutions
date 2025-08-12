# Last updated: 8/11/2025, 9:24:58 PM
from collections import defaultdict, deque

class Solution:
	# O(n), O(n)
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        hashmap = defaultdict(deque)
        left = max_len = 0

        for right, num in enumerate(nums):
            hashmap[num].append(right)
            if len(hashmap[num]) > k:
                # move left to next index of the 1st occurance
                # or prevent from left move back again
                left = max(left, hashmap[num].popleft() + 1)
            max_len = max(max_len, right - left + 1)

        return max_len