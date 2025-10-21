class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashset = set()
        prefix = res = left = 0

        for right, i in enumerate(nums):
            prefix += i
            while i in hashset:
                prefix -= nums[left]
                hashset.remove(nums[left])
                left += 1
            hashset.add(i)
            res = max(res, prefix)

        return res