# Last updated: 8/12/2025, 6:19:54 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = left = meax_len = 0

        for right in range(len(s)):
            cost += abs(ord(s[right]) - ord(t[right]))
            if cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

        return right - left + 1
