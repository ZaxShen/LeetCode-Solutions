class Solution:
    # O(n), O(1)
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        asc_stack = []
        # Use stack_size to restrict the nums[-k:]
        stack_size = len(nums) - k

        for i in nums:
            while stack_size and asc_stack and asc_stack[-1] > i:
                asc_stack.pop()
                stack_size -= 1
            asc_stack.append(i)

        return asc_stack[:k]