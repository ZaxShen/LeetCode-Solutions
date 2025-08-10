# Last updated: 8/9/2025, 10:25:18 PM
class Solution:
    def maxPower(self, s: str) -> int:
        count = power = 1
        for i in range(len(s) - 1): # 0, 1
            if s[i] == s[i + 1]:
                count += 1
            else:
                count = 1
            power = max(power, count)

        return power