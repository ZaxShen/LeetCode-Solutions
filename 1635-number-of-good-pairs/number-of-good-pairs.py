from collections import Counter

class Solution:
	# O(n), O(k)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = 0
        for num in nums:
            count[num] -= 1
            res += count[num]

        return res