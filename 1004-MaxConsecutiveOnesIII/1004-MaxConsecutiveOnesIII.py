# Last updated: 8/10/2025, 1:26:31 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        # Clever approach - window size only grows or stays same
        for right, v in enumerate(nums):
            if v != 1:  # Found a 0
                k -= 1  # Use one flip

            if k < 0:  # Window becomes invalid
                if nums[left] != 1:  # If left pointer is on 0
                    k += 1  # Get back one flip
                left += 1  # Always move left (maintain size)

        return right - left + 1  # Window size is the answer
