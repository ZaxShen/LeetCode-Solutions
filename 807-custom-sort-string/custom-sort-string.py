from collections import Counter

class Solution:
    # O(n), O(1)
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []

        for char in order:
            if char in count:
                res.append(char * count[char])
                del count[char]

        for char, freq in count.items():
            res.append(char * freq)

        return ''.join(res)