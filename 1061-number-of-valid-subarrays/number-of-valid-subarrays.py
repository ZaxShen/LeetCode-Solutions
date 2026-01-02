class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        asc_stack = []
        res = 0

        for i in nums:
            while asc_stack and asc_stack[-1] > i:
                asc_stack.pop()
            asc_stack.append(i)

            res += len(asc_stack)

        return res
        