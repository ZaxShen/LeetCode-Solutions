class Solution:
    def maxPower(self, s: str) -> int:
        max_power = power = 0

        left = 0
        for _ in range(len(s)):
            right = left
            while right < len(s) and s[left] == s[right]:
                right += 1
            max_power = max(max_power, right - left)
            left = right

        return max_power
