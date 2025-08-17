# Last updated: 8/16/2025, 10:51:56 PM
from collections import Counter

class Solution:
    # O(n), O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = Counter()

        left = res = 0
        k = 1
        for right, char in enumerate(s):
            counter[char] += 1

            while counter[char] > k:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)

        return res
