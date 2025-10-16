class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # 2, 1, 3
        # 0, 1, 0
        # 0

        for i, v in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < v:
                popped = stack.pop()
                res[popped] += i - popped
            stack.append(i)

        return res
            