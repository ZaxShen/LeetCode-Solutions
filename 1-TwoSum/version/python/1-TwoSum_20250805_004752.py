# Last updated: 8/5/2025, 12:47:52 AM
# O(n), O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff not in d:
                d[num] = idx
            else:
                return [d[diff], idx]
        return [-1, -1]

        