from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num in nums:
            if num in count:
                res += count[num] - 1
                count[num] -= 1

        return res
