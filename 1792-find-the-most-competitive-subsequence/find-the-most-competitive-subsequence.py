class Solution:
    # O(n), O(1)
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        count = len(nums) - k
        stack = []

        for i in nums:
            while count and stack and stack[-1] > i:
                stack.pop()
                count -= 1
            stack.append(i)

        return stack[:k]
