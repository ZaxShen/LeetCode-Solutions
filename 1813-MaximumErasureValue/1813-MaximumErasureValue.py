# Last updated: 8/4/2025, 10:44:13 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashset = set()
        left = curr = max_sum = 0

        for right, v in enumerate(nums):
            curr += v
            while v in hashset:
                hashset.remove(nums[left])
                curr -= nums[left]
                left += 1
            max_sum = max(max_sum, curr)
            hashset.add(v)

        return max_sum