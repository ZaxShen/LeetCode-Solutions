class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ds = []  # Descending stack
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while ds and temperatures[ds[-1]] < v:
                j = ds.pop()
                res[j] = i - j
            ds.append(i)

        return res