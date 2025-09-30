class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        asc = []
        res = 0

        for i, v in enumerate(nums):
            while asc and nums[asc[-1]] > v:
                asc.pop()
            asc.append(i)
            res += len(asc)

        return res

