from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()

        left = res = 0
        for right, num in enumerate(nums):
            count[num] += 1

            while count[num] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res