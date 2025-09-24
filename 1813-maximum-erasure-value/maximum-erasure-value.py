class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        prefix = i = res = 0

        for num in nums:
            prefix += num

            while num in seen:
                prefix -= nums[i]
                seen.remove(nums[i])
                i += 1
            res = max(res, prefix)

            seen.add(num)

        return res