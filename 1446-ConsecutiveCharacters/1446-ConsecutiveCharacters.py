# Last updated: 8/10/2025, 8:00:02 PM
class Solution:
    def maxPower(self, s: str) -> int:
        left = max_power = 0
        while left < len(s):
            right = left
            while right < len(s) and s[right] == s[left]:
                max_power = max(max_power, right - left + 1)
                right += 1
            left = right

        return max_power
