# Last updated: 8/17/2025, 12:30:16 PM
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])

        for i in nums[1:]:
            res &= set(i)

        return sorted(res)