# Last updated: 8/16/2025, 10:51:20 PM
from collections import defaultdict, Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()

        left = res = 0
        for right, char in enumerate(s):
            counter[char] += 1

            while counter[char] > 1:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
