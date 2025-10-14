from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        res = 0
        left = 0

        for right, v in enumerate(s):
            count[v] += 1
            while count[v] == 2:
                count[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res