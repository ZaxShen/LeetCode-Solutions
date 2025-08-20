from collections import Counter

class Solution:
    # O(n), O(n)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = Counter()

        left = res = prefix = 0
        for right, num in enumerate(nums):
            prefix += num
            count[num] += 1
            
            while count[num] == 2:
                prefix -= nums[left]
                count[nums[left]] -= 1
                left += 1
            
            res = max(res, prefix)

        return res


