from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for k, v in count.items():
            if v == 1:
                return s.find(k)

        return -1