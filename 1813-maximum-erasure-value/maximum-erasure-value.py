class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()

        left = prefix = res = 0
        for num in nums:
            prefix += num
            while num in seen:
                prefix -= nums[left]
                seen.remove(nums[left])
                left += 1

            res = max(res, prefix)
            seen.add(num)

        return res