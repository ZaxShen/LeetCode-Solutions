from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = 0

        for k, v in count.items():
            if v == max(count.values()):
                res += v

        return res