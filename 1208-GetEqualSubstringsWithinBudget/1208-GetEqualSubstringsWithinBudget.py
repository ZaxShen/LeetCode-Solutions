# Last updated: 8/13/2025, 2:16:57 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = max_len = cost = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            if cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len