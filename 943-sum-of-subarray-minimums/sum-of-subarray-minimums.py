class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        mins = [0] * len(arr)
        mono_stack = []

        for idx, i in enumerate(arr):
            while mono_stack and arr[mono_stack[-1]] > i:
                mono_stack.pop()
            
            if mono_stack:
                prev_sum = mins[mono_stack[-1]]
                mins[idx] = prev_sum + i * (idx - mono_stack[-1])
            else:
                mins[idx] = i * (idx + 1)

            mono_stack.append(idx)

        return sum(mins) % MOD
            