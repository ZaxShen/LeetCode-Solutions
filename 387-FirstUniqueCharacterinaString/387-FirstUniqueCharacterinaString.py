# Last updated: 8/11/2025, 12:09:52 AM
class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for k, v in d.items():
            if v == 1:
                return s.index(k)

        return -1