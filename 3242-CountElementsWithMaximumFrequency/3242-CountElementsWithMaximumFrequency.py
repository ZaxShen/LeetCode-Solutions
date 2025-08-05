# Last updated: 8/4/2025, 10:43:27 PM
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        count = Counter(nums)

        max_freq = max(count.values())
        # if max_freq == 1:
        #     return max(count)

        res = 0
        for num, freq in count.items():
            if freq == max_freq:
                res += freq

        return res