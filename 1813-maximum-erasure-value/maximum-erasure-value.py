from collections import Counter


class Solution:
    # O(n), O(n)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashset = set()

        left = prefix = res = 0
        for num in nums:
            prefix += num

            while num in hashset:
                prefix -= nums[left]
                hashset.remove(nums[left])
                left += 1

            hashset.add(num)
            res = max(res, prefix)

        return res
