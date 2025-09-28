class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        desc = []
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            # Maintain stack in desc order
            while desc and temperatures[desc[-1]] < v:
                j = desc.pop()
                res[j] = i - j
            desc.append(i)

        return res