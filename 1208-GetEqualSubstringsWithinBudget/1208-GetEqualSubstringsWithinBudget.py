# Last updated: 8/11/2025, 7:23:37 PM
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curr_cost = max_len = left = 0

        for right in range(len(s)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len