class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_stack = []
        max_stack = []
        mins = [0] * len(nums)
        maxs = [0] * len(nums)

        for i, v in enumerate(nums):
            while min_stack and nums[min_stack[-1]] > v:
                min_stack.pop()
            if min_stack:
                prev_min = mins[min_stack[-1]]
                mins[i] = prev_min + v * (i - min_stack[-1])
            else:
                mins[i] = v * (i + 1)
            min_stack.append(i)

            while max_stack and nums[max_stack[-1]] < v:
                max_stack.pop()
            if max_stack:
                prev_max = maxs[max_stack[-1]]
                maxs[i] = prev_max + v * (i - max_stack[-1])
            else:
                maxs[i] = v * (i + 1)
            max_stack.append(i)

        return sum(max_v - min_v for max_v, min_v in zip(maxs, mins))