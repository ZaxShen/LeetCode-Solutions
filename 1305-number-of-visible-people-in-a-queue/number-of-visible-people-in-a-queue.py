class Solution:
    # O(n), O(n)
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        d_s = []
        res = [0] * len(heights)

        for idx, i in enumerate(heights):
            while d_s and heights[d_s[-1]] < i:
                res[d_s.pop()] += 1
            if d_s:
                res[d_s[-1]] += 1
            d_s.append(idx)

        return res