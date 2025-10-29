class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = res = flips = 0

        for right, i in enumerate(nums):
            if i == 0:
                flips += 1
            while flips > k:
                flips -= nums[left] == 0
                left += 1
            else:
                res = max(res, right - left + 1)

        return res