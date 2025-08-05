# Last updated: 8/4/2025, 10:43:41 PM
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        stack_min = []
        stack_max = []
        dp_min = [0] * len(nums)
        dp_max = [0] * len(nums)

        for i, v in enumerate(nums):
            while stack_min and nums[stack_min[-1]] >= v:
                stack_min.pop()
            if stack_min:
                dp_min[i] = dp_min[stack_min[-1]] + (i - stack_min[-1]) * v
            else:
                dp_min[i] = (i + 1) * v
            stack_min.append(i)

            while stack_max and nums[stack_max[-1]] < v:
                stack_max.pop()
            if stack_max:
                dp_max[i] = dp_max[stack_max[-1]] + (i - stack_max[-1]) * v
            else:
                dp_max[i] = (i + 1) * v
            stack_max.append(i)

        return sum([i - j for i, j in zip(dp_max, dp_min)])