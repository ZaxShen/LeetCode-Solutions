from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for i in nums:
            res += count[i] - 1
            count[i] -= 1

        return res