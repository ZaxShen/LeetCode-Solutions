# Last updated: 8/9/2025, 10:09:22 PM
class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        power = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            power = max(power, j - i)
            i = j

        return power