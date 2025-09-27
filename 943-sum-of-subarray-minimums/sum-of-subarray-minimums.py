class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        mins_sum = [0] * len(arr)

        for i, v in enumerate(arr):
            # Asc stack
            while stack and arr[stack[-1]] > v:
                stack.pop()

            if stack:
                prev_sum = mins_sum[stack[-1]]
                mins_sum[i] = prev_sum + v * (i - stack[-1])
            else:
                mins_sum[i] = v * (i + 1)
            stack.append(i)

        return sum(mins_sum) % MOD