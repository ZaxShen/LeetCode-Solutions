# Last updated: 8/9/2025, 10:07:40 PM
class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        count = power = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                count += 1
                j += 1
            else:
                power = max(power, count)
                count = 0
            i += 1

        return power