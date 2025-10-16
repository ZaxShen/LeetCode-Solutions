class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        stack = []
        sum_min = [0] * len(arr)
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] > v:
                stack.pop()

            if stack:
                prev_sum = sum_min[stack[-1]]
                sum_min[i] = prev_sum + v * (i - stack[-1])
            else:
                sum_min[i] = v * (i + 1)

            stack.append(i)

        return sum(sum_min) % MOD