class Solution:
    # O(n), O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = res = 0

        for right, i in enumerate(nums):
            if i == 0:
                k -= 1
            
            if k < 0:
                k += nums[left] == 0
                left += 1
            else:
                res = max(res, right - left + 1)

        return res