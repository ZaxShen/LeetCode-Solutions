from collections import Counter

class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for i in s:
            if count[i] == 1:
                return s.index(i)

        return -1