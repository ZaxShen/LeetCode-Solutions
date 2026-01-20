class Solution:
    # O(n), O(k)
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = res = 0

        for i in s:
            while i in seen:
                seen.remove(s[left])
                left += 1
            seen.add(i)
            res = max(res, len(seen))

        return res