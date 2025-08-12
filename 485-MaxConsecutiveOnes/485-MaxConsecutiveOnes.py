# Last updated: 8/12/2025, 7:48:44 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = res = 0

        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0

        return res
