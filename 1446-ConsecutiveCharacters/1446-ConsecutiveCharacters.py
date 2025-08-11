# Last updated: 8/10/2025, 8:06:41 PM
class Solution:
    # O(n), O(1)
    def maxPower(self, s: str) -> int:
        count = power = 1
        for i in range(len(s) - 1): # 0, 1
            if s[i] == s[i + 1]:
                count += 1
            else:
                count = 1
            power = max(power, count)

        return power