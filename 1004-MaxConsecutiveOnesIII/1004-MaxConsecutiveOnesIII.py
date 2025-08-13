# Last updated: 8/13/2025, 12:48:24 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_len = 0

        for right, num in enumerate(nums):
            if num == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
