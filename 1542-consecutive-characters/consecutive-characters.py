class Solution:
    def maxPower(self, s: str) -> int:
        max_power = power = 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                power += 1
                max_power = max(max_power, power)
            else:
                power = 1

        return max_power