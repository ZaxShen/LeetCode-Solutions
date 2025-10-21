from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for i in nums:
            count[i] -= 1
            res += count[i]

        return res