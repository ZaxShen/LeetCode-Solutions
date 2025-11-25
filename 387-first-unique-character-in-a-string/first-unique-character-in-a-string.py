from collections import Counter

class Solution:
    # O(n), O(n)
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for idx, i in enumerate(s):
            if count[i] == 1:
                return idx

        return -1