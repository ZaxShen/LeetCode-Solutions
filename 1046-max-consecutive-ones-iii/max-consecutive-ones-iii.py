class Solution:
    # O(n), O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_len = 0
        # Clever approach - window size only grows or stays same
        for right, num in enumerate(nums):
            if num == 0:  # Found a 0
                k -= 1  # Use one flip

            if k < 0:  # Window becomes invalid
                k += nums[left] == 0  # If left pointer is on 0, get back one flip
                left += 1  # Always move right (maintain size)
            else:
	            max_len = max(max_len, right - left + 1)

        return max_len