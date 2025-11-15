from collections import Counter

class Solution:
    # O(n), O(1)
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []

        for i in order:
            if i in count:
                res.append(i * count[i])
                del count[i]

        for k, v in count.items():
            res.append(k * v)

        return ''.join(res)

        
