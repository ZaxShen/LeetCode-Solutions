class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        mono_stack = []
        res = 0

        for i in nums:
            while mono_stack and mono_stack[-1] > i:
                mono_stack.pop()
            mono_stack.append(i)

            res += len(mono_stack)

        return res