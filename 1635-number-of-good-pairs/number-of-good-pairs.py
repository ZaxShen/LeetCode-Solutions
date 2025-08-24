from collections import defaultdict

class Solution:
	# O(n), O(k)
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count = defaultdict(int)
        res = 0

        for num in nums:
            res += count[num]
            count[num] += 1
        
        return res