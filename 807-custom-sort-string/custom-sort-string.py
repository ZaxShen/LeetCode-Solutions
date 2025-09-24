from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)

        res = []
        for char in order:
            res.append(char * count[char])
            del count[char]

        for k, v in count.items():
            res.append(k * v)

        return "".join(res)