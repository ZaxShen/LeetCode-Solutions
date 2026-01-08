from collections import Counter

class Solution:
    # O(n), O(k)
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()

        left = res = 0
        for right, i in enumerate(nums):
            count[i] += 1
            while count[i] > k:
                count[nums[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res