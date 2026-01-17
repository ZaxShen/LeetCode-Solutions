class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = res = 0
        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))
            maxCost -= cost
            while maxCost < 0:
                cost = abs(ord(s[left]) - ord(t[left])) 
                maxCost += cost
                left += 1
            res = max(res, right - left + 1)

        return res