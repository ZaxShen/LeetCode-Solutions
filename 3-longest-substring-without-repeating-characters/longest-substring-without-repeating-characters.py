from collections import Counter

class Solution:
    # O(n), O(k)
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        left = res = 0

        k = 1
        for right, char in enumerate(s):
            count[char] += 1

            while count[char] > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res