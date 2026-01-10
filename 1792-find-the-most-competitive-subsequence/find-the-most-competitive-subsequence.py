class Solution:
    # O(n), O(1)
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Edge case
        if k == 0: return nums

        stack = []
        remove_count = len(nums) - k
        
        for i in nums:
            while remove_count and stack and stack[-1] > i:
                stack.pop()
                remove_count -= 1
            stack.append(i)

        return stack[:k]

