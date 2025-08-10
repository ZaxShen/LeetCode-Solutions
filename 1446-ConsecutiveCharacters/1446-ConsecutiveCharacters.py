# Last updated: 8/10/2025, 7:33:40 PM
class Solution:
    def maxPower(self, s: str) -> int:
        count = max_power = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
                max_power = max(max_power, count)
            else:
                count = 1

        return max_power
