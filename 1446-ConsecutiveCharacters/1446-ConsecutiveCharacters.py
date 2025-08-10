# Last updated: 8/9/2025, 10:11:13 PM
class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        power = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            else:
                power = max(power, j - i)
                i = j

        return power