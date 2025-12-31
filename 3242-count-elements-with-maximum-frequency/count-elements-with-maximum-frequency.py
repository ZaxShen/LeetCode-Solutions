from collections import Counter

class Solution:
    # O(n), O(k)
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())

        return sum(filter(lambda x: x == max_freq, count.values()))