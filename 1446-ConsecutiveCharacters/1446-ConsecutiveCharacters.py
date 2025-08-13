# Last updated: 8/13/2025, 11:44:43 AM
class Solution:
    def maxPower(self, s: str) -> int:
        power = count = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                power = max(power, count)
            else:
                count = 1

        return power