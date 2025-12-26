class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        asc_stack = []
        count = len(nums) - k

        for i in nums:
            while asc_stack and asc_stack[-1] > i and count > 0:
                asc_stack.pop()
                count -= 1
            asc_stack.append(i)

        return asc_stack[:k]