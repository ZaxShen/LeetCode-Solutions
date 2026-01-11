class Solution:
    # O(n), O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            res = max(res, count)

        return res