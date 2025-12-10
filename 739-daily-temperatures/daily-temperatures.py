class Solution:
    # O(n), O(1)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        res = [0] * len(temperatures)

        for idx, i in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]] < i:
                popped = mono_stack.pop()
                res[popped] = idx - popped
            mono_stack.append(idx)

        return res