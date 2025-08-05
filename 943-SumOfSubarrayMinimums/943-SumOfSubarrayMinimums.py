# Last updated: 8/4/2025, 10:46:34 PM
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        dp = [0] * len(arr)
        
        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                stack.pop()

            if stack:
                dp[i] = dp[stack[-1]] + v * (i - stack[-1])
            else:
                dp[i] = v * (i + 1)

            stack.append(i)

        return sum(dp) % MOD
