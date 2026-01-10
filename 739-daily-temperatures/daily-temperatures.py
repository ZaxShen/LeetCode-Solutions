class Solution:
    # O(n), O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        desc_stack = []

        for idx, i in enumerate(temperatures):
            while desc_stack and temperatures[desc_stack[-1]] < i:
                popped = desc_stack.pop()
                answer[popped] = idx - popped
            desc_stack.append(idx)

        return answer