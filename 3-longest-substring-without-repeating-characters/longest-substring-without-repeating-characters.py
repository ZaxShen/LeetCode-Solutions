class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = res = 0

        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            res = max(res, right - left + 1)

            seen.add(char)

        return res
