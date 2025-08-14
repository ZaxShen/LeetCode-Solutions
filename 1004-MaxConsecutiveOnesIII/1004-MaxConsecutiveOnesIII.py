# Last updated: 8/14/2025, 1:04:31 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            # max_len = max(max_len, right - left + 1)

        return right - left + 1
