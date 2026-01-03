class Solution:
    # O(n), O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = res = 0
        for right, i in enumerate(nums):
            if i == 0:
                left = right + 1
            else:
                res = max(res, right - left + 1)

        return res