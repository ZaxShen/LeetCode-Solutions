class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ds = []  # Descending stack
        res = [0] * len(heights)

        for i, v in enumerate(heights):
            while ds and heights[ds[-1]] < v:
                res[ds.pop()] += 1
            if ds:
                res[ds[-1]] += 1
            ds.append(i)

        return res