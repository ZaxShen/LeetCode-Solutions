# Last updated: 8/4/2025, 10:44:16 PM
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        stack_size = len(nums) - k

        for v in nums:
            while stack_size and stack and stack[-1] > v:
                stack.pop()
                stack_size -= 1
            stack.append(v)

        return stack[:k]