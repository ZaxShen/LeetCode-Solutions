from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)

        res = []

        for k in sorted(count, key=count.get, reverse=True):
            res.append(k * count[k])
            
        return ''.join(res)