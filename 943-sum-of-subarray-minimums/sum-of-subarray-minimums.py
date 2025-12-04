class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        mono_stack = []
        res = [0] * len(arr)

        # 0: 3: 3 = 3
        # 1: 1: 1 * 2 = 2
        # 2: 1, 2: 2 + (1 * 2) = 4
        # 3: 1, 2, 4: 4 + (2 + 1 * 2) = 8

        # 0: 11: 11
        # 1: 11, 81: 81 + 11
        # 2: 11, 81, 94, 2: 94 + (81 + 11)
        # 3: 11, 43
        # 4: 3:

        for idx, i in enumerate(arr):
            while mono_stack and arr[mono_stack[-1]] > i:
                mono_stack.pop()

            if mono_stack:
                prev_sum = res[mono_stack[-1]]
                res[idx] = prev_sum + i * (idx - mono_stack[-1])
            else:
                res[idx] = i * (idx + 1)

            mono_stack.append(idx)

        return sum(res) % MOD




