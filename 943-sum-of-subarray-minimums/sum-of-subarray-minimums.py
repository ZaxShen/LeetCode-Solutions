class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        sum_mins = [0] * len(arr)
        stack = []

        for i, v in enumerate(arr):
            # Maintain stack in asc order
            while stack and arr[stack[-1]] > v:
                stack.pop()

            # v is not the minimum for current subarrys
            if stack:
                sum_mins[i] = sum_mins[stack[-1]] + v * (i - stack[-1])
            # v is the minimum for current subarrys
            else:
                sum_mins[i] = v * (i + 1)

            # Append stack
            stack.append(i)

        return sum(sum_mins) % MOD