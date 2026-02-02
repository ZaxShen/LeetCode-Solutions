class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        mono_stack = []

        # 0 1 
        # 1 0 0 0 0 0

        for idx, i in enumerate(heights):
            
            while mono_stack and heights[mono_stack[-1]] < i:
                res[mono_stack.pop()] += 1
            if mono_stack:
                res[mono_stack[-1]] += 1
            mono_stack.append(idx)

        return res