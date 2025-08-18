class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        left = res = 0
        k = 1

        for right, char in enumerate(s):
            counter[char] = counter.get(char, 0) + 1

            while counter[char] > k:
                counter[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
