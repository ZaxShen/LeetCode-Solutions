class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        asc_stack = []
        stack_size = len(nums) - k

        for i in nums:
            while stack_size > 0 and asc_stack and asc_stack[-1] > i:
                asc_stack.pop()
                stack_size -= 1
            asc_stack.append(i)

        return asc_stack[:k]