class Solution:
    # O(n), O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = left = 0
        for right, i in enumerate(nums):
            if i == 1:
                res = max(res, right - left + 1)
            else:
                left = right + 1  # Move left one position greater than right for next iteration

        return res