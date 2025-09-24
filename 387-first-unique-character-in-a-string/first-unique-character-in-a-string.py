from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for char in s:
            if count[char] == 1:
                return s.index(char)

        return -1