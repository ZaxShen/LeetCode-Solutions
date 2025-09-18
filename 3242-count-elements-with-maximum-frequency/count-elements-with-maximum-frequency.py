from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())

        return sum(val for val in count.values() if val == max_freq)