# Last updated: 8/14/2025, 9:46:40 AM
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])

        for i in nums[1:]:
            res &= set(i)

        return sorted(res)