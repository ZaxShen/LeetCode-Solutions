from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = []
        sorted_count = sorted(count, key=count.get, reverse=True)

        for i in sorted_count:
            res.append(i * count[i])

        return ''.join(res)