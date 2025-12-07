class Solution:
    # O(n), O(n)
    def subArrayRanges(self, nums: List[int]) -> int:
        asc_stack = []
        desc_stack = []
        mins = [0] * len(nums)
        maxs = [0] * len(nums)
        res = 0

        for idx, i in enumerate(nums):
            while asc_stack and nums[asc_stack[-1]] > i:
                asc_stack.pop()
            
            if asc_stack:
                prev_min = mins[asc_stack[-1]]
                curr_min = prev_min + i * (idx - asc_stack[-1])
            else:
                curr_min = i * (idx + 1)
            
            mins[idx] = curr_min
            asc_stack.append(idx)

            while desc_stack and nums[desc_stack[-1]] < i:
                desc_stack.pop()

            if desc_stack:
                prev_max = maxs[desc_stack[-1]]
                curr_max = prev_max + i * (idx - desc_stack[-1])
            else:
                curr_max = i * (idx + 1)

            maxs[idx] = curr_max
            desc_stack.append(idx)

            res += curr_max - curr_min

        return res