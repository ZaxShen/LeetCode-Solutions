# Last updated: 8/11/2025, 12:10:28 AM
class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        
        for k, v in d.items():
            if v == 1:
                return s.index(k)

        return -1