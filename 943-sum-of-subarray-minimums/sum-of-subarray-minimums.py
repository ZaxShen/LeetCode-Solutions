class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        mono_stack = []
        res = [0] * len(arr)

        for idx, i in enumerate(arr):
            while mono_stack and arr[mono_stack[-1]] > i:
                mono_stack.pop()

            if mono_stack:
                # prev_sum = res[idx - 1]
                prev_sum = res[mono_stack[-1]]
                res[idx] = prev_sum + i * (idx - mono_stack[-1])
            else:
                res[idx] = i * (idx + 1)

            mono_stack.append(idx)

        return sum(res) % MOD