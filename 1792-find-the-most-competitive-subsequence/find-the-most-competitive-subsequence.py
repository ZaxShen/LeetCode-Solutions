class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        stack_count = len(nums) - k

        for i in nums:
            while stack_count > 0 and stack and stack[-1] > i:
                stack.pop()
                stack_count -= 1
            stack.append(i)

        return stack[:k]