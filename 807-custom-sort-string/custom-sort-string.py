from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        count = Counter(s)
        
        for i in order:
            if i in count:
                res.append(i * count[i])
                del count[i]

        for k, v in count.items():
            res.append(k * v)

        return ''.join(res)
