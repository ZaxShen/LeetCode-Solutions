# Last updated: 8/4/2025, 10:46:40 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for curr_date, curr_temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_temperature:
                last_date = stack.pop()
                res[last_date] = curr_date - last_date
            stack.append(curr_date)

        return res
