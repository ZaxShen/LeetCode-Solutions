# Last updated: 8/4/2025, 10:45:18 PM
class Solution:
    def maxPower(self, s: str) -> int:
        left = max_power = 0
        while left < len(s):
            right = left
            while right < len(s) and s[left] == s[right]:
                right += 1
            max_power = max(max_power, right - left)
            left = right
            
        return max_power