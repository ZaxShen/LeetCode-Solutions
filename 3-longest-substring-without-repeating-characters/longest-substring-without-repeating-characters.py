class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}

        left = res = 0
        k = 1
        for right, char in enumerate(s):
            count[char] = count.get(char, 0) + 1
            
            while count[char] > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res