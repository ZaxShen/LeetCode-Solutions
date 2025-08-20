from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)

        max_freq = max(counter.values())
        res = 0
        for k, v in counter.items():
            if v == max_freq:
                res += v

        return res