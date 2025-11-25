class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = res = 0
        for right, i in enumerate(nums):
            if i == 1:
                res = max(res, right - left + 1)
            else:
                left = right + 1

        return res
