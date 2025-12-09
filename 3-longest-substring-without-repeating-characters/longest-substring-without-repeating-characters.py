class Solution:
    # O(n), O(k)
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = res = 0

        for right, i in enumerate(s):
            while i in seen:
                seen.remove(s[left])
                left += 1
            seen.add(i)
            res = max(res, right - left + 1)

        return res