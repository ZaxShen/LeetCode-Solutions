class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        desc_stack = []

        for idx, i in enumerate(heights):
            while desc_stack and heights[desc_stack[-1]] < i:
                res[desc_stack.pop()] += 1
            if desc_stack:
                res[desc_stack[-1]] += 1
            desc_stack.append(idx)

        return res