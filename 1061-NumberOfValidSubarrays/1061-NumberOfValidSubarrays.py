# Last updated: 8/4/2025, 10:46:24 PM
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for i, v in enumerate(nums):
            while stack and stack[-1] > v:
                stack.pop()
            stack.append(v)
            count += len(stack)

        return count