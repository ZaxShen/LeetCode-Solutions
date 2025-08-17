# Last updated: 8/17/2025, 1:34:28 PM
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Base case: impossible to win
        if k == 0 or n >= k + maxPts - 1:
            return 1.0
        
        # dp[i] = probability of winning starting from i points
        dp = [0.0] * (k + maxPts)
        
        # Base cases: if we've stopped drawing (points >= k)
        for i in range(k, min(n + 1, k + maxPts)):
            dp[i] = 1.0  # Win if final score <= n
        
        # Fill DP table backwards (from k-1 down to 0)
        window_sum = sum(dp[k:k + maxPts])  # Sum of probabilities we can reach
        
        for i in range(k - 1, -1, -1):
            dp[i] = window_sum / maxPts  # Average of all possible next states
            
            # Update sliding window: remove dp[i + maxPts], add dp[i]
            window_sum += dp[i] - dp[i + maxPts]
        
        return dp[0]