# Last updated: 8/9/2025, 10:00:55 PM
class Solution:
    # O(n), O(1)
    def maxPower(self, s: str) -> int:
        count = power = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                power = max(power, count)
            else:
                count = 1 
        
        return power
