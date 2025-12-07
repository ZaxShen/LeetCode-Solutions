class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        mins = [0] * len(arr)
        mono_stack = []
        res = 0

        for idx, i in enumerate(arr):
            while mono_stack and arr[mono_stack[-1]] > i:
                mono_stack.pop()
            
            if mono_stack:
                prev_min = mins[mono_stack[-1]]
                curr_min = prev_min + i * (idx - mono_stack[-1])
            else:
                curr_min = i * (idx + 1)
            mins[idx] = curr_min
            
            res += curr_min
            mono_stack.append(idx)

        return res % MOD
            