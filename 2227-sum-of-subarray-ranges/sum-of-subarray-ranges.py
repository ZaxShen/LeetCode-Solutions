class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        asc_stack = []
        desc_stack = []
        mins = [0] * len(nums)
        maxs = [0] * len(nums)

        for idx, i in enumerate(nums):
            while asc_stack and nums[asc_stack[-1]] > i:
                asc_stack.pop()
            
            if asc_stack:
                prev_sum = mins[asc_stack[-1]]
                mins[idx] = prev_sum + i * (idx - asc_stack[-1])
            else:
                mins[idx] = i * (idx + 1)

            asc_stack.append(idx)

            while desc_stack and nums[desc_stack[-1]] < i:
                desc_stack.pop()

            if desc_stack:
                prev_sum = maxs[desc_stack[-1]]
                maxs[idx] = prev_sum + i * (idx - desc_stack[-1])
            else:
                maxs[idx] = i * (idx + 1)

            desc_stack.append(idx)

        return sum(i - j for i, j in zip(maxs, mins))