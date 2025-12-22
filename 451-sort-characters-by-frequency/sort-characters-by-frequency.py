from collections import Counter

class Solution:
    # O(n), O(k)
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        desc_s = sorted(count, key=count.get, reverse=True)
        res = []

        for i in desc_s:
            res.append(i * count[i])

        return ''.join(res)