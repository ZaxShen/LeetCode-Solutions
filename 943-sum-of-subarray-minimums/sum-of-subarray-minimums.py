class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        res = [0] * len(arr)

        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] > v:
                stack.pop()
            if stack:
                prev_sum = res[stack[-1]]
                res[i] = prev_sum + v * (i - stack[-1])
            else:
                res[i] = v * (i + 1)
            stack.append(i)

        return sum(res) % MOD