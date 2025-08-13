# Last updated: 8/13/2025, 2:00:31 PM
class Solution:
    def maxPower(self, s: str) -> int:
        left = power = 0

        while left < len(s):
            right = left
            while right < len(s) and s[right] == s[left]:
                right += 1
            power = max(power, right - left)
            left = right

        return power